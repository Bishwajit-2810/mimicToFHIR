#!/usr/bin/env python3
"""Entry point for the MIMIC-IV → PostgreSQL → FHIR R4 pipeline.

Three output pipelines:
  bundle   → fhir_bundles/          Full data: conditions, meds, notes, vitals, labs
  golddata → golddata_fhir_bundles/ Blind:  no conditions, no meds, no notes
  testing  → testing/               Blind + notes: no conditions, no meds, WITH notes
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

    args = parser.parse_args()

    dispatch = {
        "load":     cmd_load,
        "convert":  cmd_convert,
        "bundle":   cmd_bundle,
        "golddata": cmd_golddata,
        "testing":  cmd_testing,
    }
    dispatch[args.command](args)


if __name__ == "__main__":
    main()
