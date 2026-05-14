#!/usr/bin/env python3
"""Load MIMIC-IV demo CSVs into PostgreSQL."""

import gzip
import io
import os
import sys
import time
from pathlib import Path

import psycopg2

DSN = os.getenv("MIMIC_DSN", "host=localhost port=5433 dbname=mimiciv user=mimic password=mimic")

BASE = Path(__file__).parent.parent

TABLES = [
    # (schema, table, csv_path)
    # hosp — dictionaries first (no FK deps, but good practice)
    ("hosp", "provider",           BASE / "hosp/provider.csv.gz"),
    ("hosp", "d_icd_diagnoses",    BASE / "hosp/d_icd_diagnoses.csv.gz"),
    ("hosp", "d_icd_procedures",   BASE / "hosp/d_icd_procedures.csv.gz"),
    ("hosp", "d_hcpcs",            BASE / "hosp/d_hcpcs.csv.gz"),
    ("hosp", "d_labitems",         BASE / "hosp/d_labitems.csv.gz"),
    # hosp — core
    ("hosp", "patients",           BASE / "hosp/patients.csv.gz"),
    ("hosp", "admissions",         BASE / "hosp/admissions.csv.gz"),
    ("hosp", "transfers",          BASE / "hosp/transfers.csv.gz"),
    ("hosp", "services",           BASE / "hosp/services.csv.gz"),
    # hosp — clinical
    ("hosp", "diagnoses_icd",      BASE / "hosp/diagnoses_icd.csv.gz"),
    ("hosp", "procedures_icd",     BASE / "hosp/procedures_icd.csv.gz"),
    ("hosp", "drgcodes",           BASE / "hosp/drgcodes.csv.gz"),
    ("hosp", "hcpcsevents",        BASE / "hosp/hcpcsevents.csv.gz"),
    ("hosp", "labevents",          BASE / "hosp/labevents.csv.gz"),
    ("hosp", "microbiologyevents", BASE / "hosp/microbiologyevents.csv.gz"),
    ("hosp", "omr",                BASE / "hosp/omr.csv.gz"),
    # hosp — medications
    ("hosp", "poe",                BASE / "hosp/poe.csv.gz"),
    ("hosp", "poe_detail",         BASE / "hosp/poe_detail.csv.gz"),
    ("hosp", "prescriptions",      BASE / "hosp/prescriptions.csv.gz"),
    ("hosp", "pharmacy",           BASE / "hosp/pharmacy.csv.gz"),
    ("hosp", "emar",               BASE / "hosp/emar.csv.gz"),
    ("hosp", "emar_detail",        BASE / "hosp/emar_detail.csv.gz"),
    # icu
    ("icu",  "caregiver",          BASE / "icu/caregiver.csv.gz"),
    ("icu",  "d_items",            BASE / "icu/d_items.csv.gz"),
    ("icu",  "icustays",           BASE / "icu/icustays.csv.gz"),
    ("icu",  "chartevents",        BASE / "icu/chartevents.csv.gz"),
    ("icu",  "datetimeevents",     BASE / "icu/datetimeevents.csv.gz"),
    ("icu",  "outputevents",       BASE / "icu/outputevents.csv.gz"),
    ("icu",  "inputevents",        BASE / "icu/inputevents.csv.gz"),
    ("icu",  "ingredientevents",   BASE / "icu/ingredientevents.csv.gz"),
    ("icu",  "procedureevents",    BASE / "icu/procedureevents.csv.gz"),
]


def wait_for_db(dsn: str, retries: int = 20, delay: float = 3.0) -> psycopg2.extensions.connection:
    for i in range(retries):
        try:
            conn = psycopg2.connect(dsn)
            print("Connected to database.")
            return conn
        except psycopg2.OperationalError:
            print(f"  Waiting for database... ({i+1}/{retries})")
            time.sleep(delay)
    print("Could not connect to database after retries. Is the container running?")
    sys.exit(1)


def load_table(cur, schema: str, table: str, csv_path: Path) -> int:
    with gzip.open(csv_path, "rt", encoding="utf-8") as f:
        header = f.readline().strip()
        columns = header.lower()  # postgres is case-insensitive but keep it clean
        buf = io.StringIO()
        buf.write(columns + "\n")
        buf.write(f.read())
        buf.seek(0)

    cur.copy_expert(
        f"COPY {schema}.{table} ({columns}) FROM STDIN WITH (FORMAT CSV, HEADER TRUE, NULL '')",
        buf,
    )
    return cur.rowcount


def main():
    conn = wait_for_db(DSN)
    conn.autocommit = False

    total = 0
    with conn:
        cur = conn.cursor()

        # Truncate in reverse order to avoid FK issues, then reload cleanly.
        print("Truncating existing data...")
        for schema, table, _ in reversed(TABLES):
            cur.execute(f"TRUNCATE TABLE {schema}.{table} CASCADE")
        conn.commit()

        for schema, table, path in TABLES:
            if not path.exists():
                print(f"  SKIP  {schema}.{table} — file not found: {path}")
                continue
            print(f"  Loading {schema}.{table} ...", end=" ", flush=True)
            rows = load_table(cur, schema, table, path)
            print(f"{rows} rows")
            total += rows
        conn.commit()

    print(f"\nDone. {total} total rows loaded.")
    conn.close()


if __name__ == "__main__":
    main()
