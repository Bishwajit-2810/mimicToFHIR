#!/usr/bin/env python3
"""Entry point for the MIMIC-IV → PostgreSQL → FHIR R4 pipeline.

Two output pipelines:
  bundle   → fhir_bundles/          Full data: conditions, procedures, meds, notes, vitals, labs
  golddata → golddata_fhir_bundles/ Blind:  latest encounter has no conditions, procedures, meds, notes

Use `all` to generate both from the same random patient sample.
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


def _resolve_filtered_sids(args, dsn):
    """If cohort filters are active, select matching subject_ids and the default
    output subfolder. Returns (sids, filters); sids is None when no filters set."""
    import psycopg2
    import psycopg2.extras
    from etl.filters import extract_filters, select_subject_ids, slug_for

    filters = extract_filters(args)
    if not filters:
        return None, filters

    conn = psycopg2.connect(dsn)
    conn.set_session(readonly=True, autocommit=True)
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    sids = select_subject_ids(
        cur, filters,
        random_sample=getattr(args, "random", True),
        limit=args.limit,
        offset=getattr(args, "offset", 0),
    )
    cur.close()
    conn.close()
    print(f"Cohort '{slug_for(filters)}': {len(sids):,} matching patients\n")
    return sids, filters


def cmd_bundle(args):
    from etl.mimic_to_bundle import convert, DSN, OUTPUT_DIR
    from etl.filters import default_output_base, FHIR_SUBDIR

    dsn = args.dsn or DSN
    filtered_sids, filters = _resolve_filtered_sids(args, dsn)

    if args.subject_ids:
        sids = [int(s.strip()) for s in args.subject_ids.split(",")]
    else:
        sids = filtered_sids  # None unless filters are active

    if args.output:
        output_dir = Path(args.output)
    elif filters:
        output_dir = default_output_base(filters) / FHIR_SUBDIR
    else:
        output_dir = OUTPUT_DIR

    convert(
        dsn=dsn,
        output_dir=output_dir,
        limit=args.limit,
        offset=args.offset,
        subject_ids=sids,
        random_sample=args.random and not filters,
    )


def cmd_golddata(args):
    from etl.golddata_fhir_gen import convert, DSN, OUTPUT_DIR
    from etl.filters import default_output_base, GOLD_SUBDIR

    dsn = args.dsn or DSN
    filtered_sids, filters = _resolve_filtered_sids(args, dsn)

    if args.subject_ids:
        sids = [int(s.strip()) for s in args.subject_ids.split(",")]
    else:
        sids = filtered_sids

    if args.output:
        output_dir = Path(args.output)
    elif filters:
        output_dir = default_output_base(filters) / GOLD_SUBDIR
    else:
        output_dir = OUTPUT_DIR

    convert(
        dsn=dsn,
        output_dir=output_dir,
        include_notes=False,
        limit=args.limit,
        offset=args.offset,
        subject_ids=sids,
        random_sample=args.random and not filters,
    )



def cmd_all(args):
    """Run both pipelines on the same randomly selected patients."""
    import psycopg2
    import psycopg2.extras
    from etl.mimic_to_bundle import convert as bundle_convert, DSN, OUTPUT_DIR as BUNDLE_OUT
    from etl.golddata_fhir_gen import convert as gold_convert, OUTPUT_DIR as GOLD_OUT
    from etl.filters import extract_filters, select_subject_ids, slug_for, default_output_base

    dsn = args.dsn or DSN
    filters = extract_filters(args)
    limit = args.limit if args.limit is not None else 10000

    if args.subject_ids:
        sids = [int(s.strip()) for s in args.subject_ids.split(",")]
        print(f"Using {len(sids)} specified patients: {sids}\n")
    else:
        conn = psycopg2.connect(dsn)
        conn.set_session(readonly=True, autocommit=True)
        cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        if filters:
            print(f"Selecting up to {limit} random patients matching cohort '{slug_for(filters)}'...")
            sids = select_subject_ids(cur, filters, random_sample=True, limit=limit)
        else:
            print(f"Selecting {limit} random patients from database...")
            cur.execute("SELECT subject_id FROM hosp.patients ORDER BY RANDOM() LIMIT %s", (limit,))
            sids = [r["subject_id"] for r in cur.fetchall()]
        cur.close()
        conn.close()
        print(f"Selected {len(sids):,} patients.\n")

    if not sids:
        print("No patients matched the given filters. Nothing to extract.")
        return

    # Filtered extracts go to filtered/<slug>/{fhir,golddata}/; otherwise
    # top-level dirs (legacy). An explicit --output keeps the legacy subfolder names.
    from etl.filters import FHIR_SUBDIR, GOLD_SUBDIR
    if args.output:
        base = Path(args.output)
    elif filters:
        base = default_output_base(filters)
    else:
        base = None

    if filters:
        fhir_name, gold_name = FHIR_SUBDIR, GOLD_SUBDIR
    else:
        fhir_name, gold_name = "fhir_bundles", "golddata_fhir_bundles"

    bundle_out = base / fhir_name if base else BUNDLE_OUT
    gold_out = base / gold_name if base else GOLD_OUT

    print("=== Step 1/2: Full FHIR bundles ===")
    bundle_convert(
        dsn=dsn,
        output_dir=bundle_out,
        subject_ids=sids,
        random_sample=False,
    )

    print("\n=== Step 2/2: GoldData FHIR bundles ===")
    gold_convert(
        dsn=dsn,
        output_dir=gold_out,
        include_notes=False,
        subject_ids=sids,
        random_sample=False,
    )

    dest = base.resolve() if base else "fhir_bundles/ and golddata_fhir_bundles/"
    print(f"\nBoth pipelines complete. Same {len(sids):,} patients across all outputs → {dest}")


def _add_batch_args(p):
    p.add_argument("--dsn", default=None, help="Override PostgreSQL DSN")
    p.add_argument("--output", default=None, help="Output directory")
    p.add_argument("--limit", type=int, default=None, help="Max patients to process (default: 10000 when --random)")
    p.add_argument("--offset", type=int, default=0, help="Skip first N patients (only used with --no-random)")
    p.add_argument("--subject-ids", default=None, help="Comma-separated subject_ids")
    p.add_argument("--random", action=argparse.BooleanOptionalAction, default=True,
                   help="Random patient sample (default: on). Use --no-random for sequential.")
    from etl.filters import add_filter_args
    add_filter_args(p)


def main():
    parser = argparse.ArgumentParser(
        description="MIMIC-IV → PostgreSQL → FHIR R4 pipeline",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Pipelines:
  bundle    fhir_bundles/           Full data: conditions, procedures, meds, notes, vitals, labs
  golddata  golddata_fhir_bundles/  Blind: latest encounter has no conditions, procedures, meds, notes
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

    # ── all (same patients across both) ──────────────────────────────────────
    p_all = sub.add_parser(
        "all",
        help="Run both pipelines on the same random patients (recommended)",
    )
    p_all.add_argument("--dsn", default=None, help="Override PostgreSQL DSN")
    p_all.add_argument("--output", default=None, help="Base output directory (creates fhir_bundles/, golddata_fhir_bundles/ inside)")
    p_all.add_argument("--limit", type=int, default=10000, help="Number of random patients (default: 10000)")
    p_all.add_argument("--subject-ids", default=None, help="Comma-separated subject_ids; skips random selection")
    from etl.filters import add_filter_args as _add_filter_args_all
    _add_filter_args_all(p_all)

    args = parser.parse_args()

    dispatch = {
        "load":     cmd_load,
        "reindex":  cmd_reindex,
        "convert":  cmd_convert,
        "bundle":   cmd_bundle,
        "golddata": cmd_golddata,
        "all":      cmd_all,
    }
    dispatch[args.command](args)


if __name__ == "__main__":
    main()
