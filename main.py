#!/usr/bin/env python3
"""Entry point: load MIMIC-IV into PostgreSQL, then convert to FHIR R4."""

import argparse
from pathlib import Path


def cmd_load(args):
    from load_mimic import main as load_main
    load_main()


def cmd_convert(args):
    from mimic_to_fhir import convert, DSN, OUTPUT_DIR
    dsn = args.dsn or DSN
    out = Path(args.output) if args.output else OUTPUT_DIR
    convert(dsn=dsn, output_dir=out)


def cmd_bundle(args):
    from mimic_to_bundle import convert, DSN, OUTPUT_DIR
    dsn = args.dsn or DSN
    out = Path(args.output) if args.output else OUTPUT_DIR
    convert(dsn=dsn, output_dir=out)


def main():
    parser = argparse.ArgumentParser(
        description="MIMIC-IV → PostgreSQL → FHIR R4 pipeline"
    )
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("load", help="Load MIMIC-IV CSVs into PostgreSQL")

    p_convert = sub.add_parser("convert", help="Convert PostgreSQL → FHIR R4 NDJSON (flat, one file per resource type)")
    p_convert.add_argument("--dsn", default=None, help="Override PostgreSQL DSN")
    p_convert.add_argument("--output", default=None, help="Output directory (default: fhir_output/)")

    p_bundle = sub.add_parser("bundle", help="Convert PostgreSQL → FHIR R4 transaction Bundles (one JSON per patient)")
    p_bundle.add_argument("--dsn", default=None, help="Override PostgreSQL DSN")
    p_bundle.add_argument("--output", default=None, help="Output directory (default: fhir_bundles/)")

    args = parser.parse_args()
    if args.command == "load":
        cmd_load(args)
    elif args.command == "convert":
        cmd_convert(args)
    elif args.command == "bundle":
        cmd_bundle(args)


if __name__ == "__main__":
    main()
