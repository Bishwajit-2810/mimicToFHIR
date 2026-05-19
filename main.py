#!/usr/bin/env python3
"""Entry point for the MIMIC-IV → PostgreSQL → FHIR R4 pipeline.

Three output pipelines:
  bundle   → fhir_bundles/          Full data: conditions, meds, notes, vitals, labs
  golddata → golddata_fhir_bundles/ Blind:  no conditions, no meds, no notes
  testing  → testing/               Blind + notes: no conditions, no meds, WITH notes

Use `all` to generate all three from the same random patient sample.
"""

import argparse
from pathlib import Path


def cmd_load(args):
    from etl.load_mimic import main as load_main
    only = [t.strip() for t in args.tables.split(",")] if args.tables else None
    load_main(
        data_dir=Path(args.data_dir) if args.data_dir else None,
        note_dir=Path(args.note_dir) if args.note_dir else None,
        dsn=args.dsn,
        only_tables=only,
    )


def cmd_reindex(args):
    import os
    import psycopg2
    from etl.load_mimic import DSN as _DSN
    dsn = args.dsn or os.getenv("MIMIC_DSN") or _DSN
    sql_path = Path(__file__).parent / "sql" / "02_indexes.sql"
    sql = sql_path.read_text()
    print("Creating indexes (this takes 10–30 minutes on the full dataset)...")
    conn = psycopg2.connect(dsn)
    conn.autocommit = True
    cur = conn.cursor()
    for stmt in [s.strip() for s in sql.split(";") if s.strip() and not s.strip().startswith("--")]:
        idx_name = stmt.split("idx_")[1].split(" ")[0] if "idx_" in stmt else "?"
        print(f"  {idx_name} ...", end=" ", flush=True)
        cur.execute(stmt)
        print("done")
    cur.close()
    conn.close()
    print("\nAll indexes created. Queries will now be fast.")


def cmd_convert(args):
    from etl.mimic_to_fhir import convert, DSN, OUTPUT_DIR
    convert(dsn=args.dsn or DSN, output_dir=Path(args.output) if args.output else OUTPUT_DIR)


def cmd_bundle(args):
    from etl.mimic_to_bundle import convert, DSN, OUTPUT_DIR
    sids = [int(s.strip()) for s in args.subject_ids.split(",")] if args.subject_ids else None
    convert(
        dsn=args.dsn or DSN,
        output_dir=Path(args.output) if args.output else OUTPUT_DIR,
        limit=args.limit,
        offset=args.offset,
        subject_ids=sids,
        random_sample=args.random,
    )


def cmd_golddata(args):
    from etl.golddata_fhir_gen import convert, DSN, OUTPUT_DIR
    sids = [int(s.strip()) for s in args.subject_ids.split(",")] if args.subject_ids else None
    convert(
        dsn=args.dsn or DSN,
        output_dir=Path(args.output) if args.output else OUTPUT_DIR,
        include_notes=False,
        limit=args.limit,
        offset=args.offset,
        subject_ids=sids,
        random_sample=args.random,
    )


def cmd_testing(args):
    from etl.testing_gen import convert, DSN, OUTPUT_DIR
    sids = [int(s.strip()) for s in args.subject_ids.split(",")] if args.subject_ids else None
    convert(
        dsn=args.dsn or DSN,
        output_dir=Path(args.output) if args.output else OUTPUT_DIR,
        limit=args.limit,
        offset=args.offset,
        subject_ids=sids,
        random_sample=args.random,
    )


def cmd_all(args):
    """Run all three pipelines on the same randomly selected patients."""
    import psycopg2
    import psycopg2.extras
    from etl.mimic_to_bundle import convert as bundle_convert, DSN, OUTPUT_DIR as BUNDLE_OUT
    from etl.golddata_fhir_gen import convert as gold_convert, OUTPUT_DIR as GOLD_OUT
    from etl.testing_gen import convert as test_convert, OUTPUT_DIR as TEST_OUT

    dsn = args.dsn or DSN

    if args.subject_ids:
        sids = [int(s.strip()) for s in args.subject_ids.split(",")]
        print(f"Using {len(sids)} specified patients: {sids}\n")
    else:
        limit = args.limit if args.limit is not None else 5
        print(f"Selecting {limit} random patients from database...")
        conn = psycopg2.connect(dsn)
        conn.set_session(readonly=True, autocommit=True)
        cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        cur.execute("SELECT subject_id FROM hosp.patients ORDER BY RANDOM() LIMIT %s", (limit,))
        sids = [r["subject_id"] for r in cur.fetchall()]
        cur.close()
        conn.close()
        print(f"Selected patients: {sids}\n")

    print("=== Step 1/3: Full FHIR bundles ===")
    bundle_convert(
        dsn=dsn,
        output_dir=Path(args.output) / "fhir_bundles" if args.output else BUNDLE_OUT,
        subject_ids=sids,
        random_sample=False,
    )

    print("\n=== Step 2/3: GoldData FHIR bundles ===")
    gold_convert(
        dsn=dsn,
        output_dir=Path(args.output) / "golddata_fhir_bundles" if args.output else GOLD_OUT,
        include_notes=False,
        subject_ids=sids,
        random_sample=False,
    )

    print("\n=== Step 3/3: Testing FHIR bundles ===")
    test_convert(
        dsn=dsn,
        output_dir=Path(args.output) / "testing" if args.output else TEST_OUT,
        subject_ids=sids,
        random_sample=False,
    )

    print(f"\nAll three pipelines complete. Same {len(sids)} patients across all outputs.")


def _add_batch_args(p):
    p.add_argument("--dsn", default=None, help="Override PostgreSQL DSN")
    p.add_argument("--output", default=None, help="Output directory")
    p.add_argument("--limit", type=int, default=None, help="Max patients to process (default: 20 when --random)")
    p.add_argument("--offset", type=int, default=0, help="Skip first N patients (only used with --no-random)")
    p.add_argument("--subject-ids", default=None, help="Comma-separated subject_ids")
    p.add_argument("--random", action=argparse.BooleanOptionalAction, default=True,
                   help="Random patient sample (default: on). Use --no-random for sequential.")


def main():
    parser = argparse.ArgumentParser(
        description="MIMIC-IV → PostgreSQL → FHIR R4 pipeline",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Pipelines:
  bundle    fhir_bundles/           Full data: conditions, meds, notes, vitals, labs
  golddata  golddata_fhir_bundles/  Blind: no conditions, no meds, no notes
  testing   testing/                Blind + notes: no conditions, no meds, WITH notes
""",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    # ── load ──────────────────────────────────────────────────────────────────
    p_load = sub.add_parser("load", help="Load MIMIC-IV CSVs into PostgreSQL")
    p_load.add_argument("--dsn", default=None)
    p_load.add_argument(
        "--data-dir", default=None,
        help="Path to MIMIC-IV data root containing hosp/ and icu/ (default: dataset/)",
    )
    p_load.add_argument(
        "--note-dir", default=None,
        help="Path to note directory with discharge.csv.gz / radiology.csv.gz (default: dataset/note/)",
    )
    p_load.add_argument(
        "--tables", default=None,
        help="Comma-separated table names to reload only (e.g. prescriptions,emar_detail)",
    )

    # ── reindex ───────────────────────────────────────────────────────────────
    p_reindex = sub.add_parser("reindex", help="Create subject_id indexes after loading (run once, makes queries fast)")
    p_reindex.add_argument("--dsn", default=None)

    # ── convert (flat NDJSON) ─────────────────────────────────────────────────
    p_convert = sub.add_parser("convert", help="PostgreSQL → FHIR R4 NDJSON (one file per resource type)")
    p_convert.add_argument("--dsn", default=None)
    p_convert.add_argument("--output", default=None)

    # ── bundle (full) ─────────────────────────────────────────────────────────
    p_bundle = sub.add_parser(
        "bundle",
        help="Full pipeline → fhir_bundles/ (conditions + meds + notes + vitals/labs)",
    )
    _add_batch_args(p_bundle)

    # ── golddata (blind, no notes) ────────────────────────────────────────────
    p_gold = sub.add_parser(
        "golddata",
        help="Blind pipeline → golddata_fhir_bundles/ (no conditions, no meds, no notes)",
    )
    _add_batch_args(p_gold)

    # ── testing (blind + notes) ───────────────────────────────────────────────
    p_test = sub.add_parser(
        "testing",
        help="Testing pipeline → testing/ (no conditions, no meds, WITH clinical notes)",
    )
    _add_batch_args(p_test)

    # ── all (same patients across all three) ──────────────────────────────────
    p_all = sub.add_parser(
        "all",
        help="Run all three pipelines on the same random patients (recommended)",
    )
    p_all.add_argument("--dsn", default=None, help="Override PostgreSQL DSN")
    p_all.add_argument("--output", default=None, help="Base output directory (creates fhir_bundles/, golddata_fhir_bundles/, testing/ inside)")
    p_all.add_argument("--limit", type=int, default=5, help="Number of random patients (default: 5)")
    p_all.add_argument("--subject-ids", default=None, help="Comma-separated subject_ids; skips random selection")

    args = parser.parse_args()

    dispatch = {
        "load":     cmd_load,
        "reindex":  cmd_reindex,
        "convert":  cmd_convert,
        "bundle":   cmd_bundle,
        "golddata": cmd_golddata,
        "testing":  cmd_testing,
        "all":      cmd_all,
    }
    dispatch[args.command](args)


if __name__ == "__main__":
    main()
