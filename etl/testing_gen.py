#!/usr/bin/env python3
"""
testing_gen.py — Testing FHIR Bundle Generator

Identical to the GoldData pipeline PLUS clinical notes (DocumentReference).

What is INCLUDED:
    • Everything from golddata_fhir_gen (encounters, vitals, labs, procedures,
      microbiology, OMR, ICU events)
    • DocumentReference — discharge summaries + radiology reports

What is EXCLUDED (same blind as golddata):
    • Condition        (ALL ICD diagnoses)
    • MedicationRequest (ALL prescriptions)

Output: testing/ directory, served by web/testing_app.py on port 8097.

Shares the same PostgreSQL instance as the Full and GoldData pipelines (port 5433).

Usage:
    python -m etl.testing_gen [--dsn DSN] [--output DIR]
    python main.py testing [options]

Env:
    MIMIC_DSN    — PostgreSQL DSN (default: localhost:5433)
    TESTING_OUT  — output directory (default: testing)
"""

import argparse
import os
from pathlib import Path

from etl.golddata_fhir_gen import convert as _gold_convert

_DEFAULT_DSN = "host=localhost port=5433 dbname=mimiciv user=mimic password=mimic"
DSN = os.getenv("MIMIC_DSN") or _DEFAULT_DSN
OUTPUT_DIR = Path(os.getenv("TESTING_OUT", "testing"))


def convert(
    dsn: str = DSN,
    output_dir: Path = OUTPUT_DIR,
    limit: int | None = None,
    offset: int = 0,
    subject_ids: list[int] | None = None,
    random_sample: bool = True,
) -> None:
    _gold_convert(
        dsn=dsn,
        output_dir=output_dir,
        include_notes=True,
        limit=limit,
        offset=offset,
        subject_ids=subject_ids,
        random_sample=random_sample,
    )


def _parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description="Generate Testing FHIR bundles (no conditions/meds, WITH clinical notes)."
    )
    p.add_argument("--dsn", default=DSN)
    p.add_argument("--output", default=str(OUTPUT_DIR))
    p.add_argument("--limit", type=int, default=None)
    p.add_argument("--offset", type=int, default=0)
    p.add_argument("--subject-ids", default=None, help="Comma-separated subject_ids")
    p.add_argument("--patient", type=int, default=None, help="Single patient (for testing)")
    return p.parse_args()


if __name__ == "__main__":
    args = _parse_args()
    out = Path(args.output)

    if args.patient:
        from etl.golddata_fhir_gen import convert_patient
        import psycopg2, psycopg2.extras
        out.mkdir(parents=True, exist_ok=True)
        conn = psycopg2.connect(args.dsn)
        conn.set_session(readonly=True, autocommit=True)
        cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        n, hadm = convert_patient(cur, args.patient, out, include_notes=True)
        cur.close()
        conn.close()
        print(f"subject {args.patient}: {n} entries → {out}/{args.patient}.json")
    else:
        sids = [int(s.strip()) for s in args.subject_ids.split(",")] if args.subject_ids else None
        convert(dsn=args.dsn, output_dir=out, limit=args.limit, offset=args.offset, subject_ids=sids)
