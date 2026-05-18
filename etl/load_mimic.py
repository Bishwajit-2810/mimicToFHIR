#!/usr/bin/env python3
"""Load MIMIC-IV CSVs into PostgreSQL.

Environment variables:
  MIMIC_DSN       PostgreSQL connection string (default: localhost:5433)
  MIMIC_DATA_DIR  Root directory containing hosp/ and icu/ subdirectories
                  (default: project root — works for demo dataset in-tree)
  MIMIC_NOTE_DIR  Directory containing note/ subdirectory with discharge/radiology CSVs
                  (default: <MIMIC_DATA_DIR>/note — skip notes if missing)
"""

import gzip
import os
import sys
import time
from pathlib import Path

import psycopg2

DSN = os.getenv("MIMIC_DSN", "host=localhost port=5433 dbname=mimiciv user=mimic password=mimic")

# Default data dir: dataset/ inside the project root
_PROJECT_ROOT = Path(__file__).parent.parent
_DEFAULT_DATA_DIR = _PROJECT_ROOT / "dataset"

DATA_DIR = Path(os.getenv("MIMIC_DATA_DIR", str(_DEFAULT_DATA_DIR)))
NOTE_DIR = Path(os.getenv("MIMIC_NOTE_DIR", str(DATA_DIR / "note")))

TABLES = [
    # (schema, table, csv_path)
    # hosp — dictionaries first (no FK deps)
    ("hosp", "d_icd_diagnoses",    DATA_DIR / "hosp/d_icd_diagnoses.csv.gz"),
    ("hosp", "d_icd_procedures",   DATA_DIR / "hosp/d_icd_procedures.csv.gz"),
    ("hosp", "d_hcpcs",            DATA_DIR / "hosp/d_hcpcs.csv.gz"),
    ("hosp", "d_labitems",         DATA_DIR / "hosp/d_labitems.csv.gz"),
    ("hosp", "provider",           DATA_DIR / "hosp/provider.csv.gz"),
    # hosp — core
    ("hosp", "patients",           DATA_DIR / "hosp/patients.csv.gz"),
    ("hosp", "admissions",         DATA_DIR / "hosp/admissions.csv.gz"),
    ("hosp", "transfers",          DATA_DIR / "hosp/transfers.csv.gz"),
    ("hosp", "services",           DATA_DIR / "hosp/services.csv.gz"),
    # hosp — clinical
    ("hosp", "diagnoses_icd",      DATA_DIR / "hosp/diagnoses_icd.csv.gz"),
    ("hosp", "procedures_icd",     DATA_DIR / "hosp/procedures_icd.csv.gz"),
    ("hosp", "drgcodes",           DATA_DIR / "hosp/drgcodes.csv.gz"),
    ("hosp", "hcpcsevents",        DATA_DIR / "hosp/hcpcsevents.csv.gz"),
    ("hosp", "labevents",          DATA_DIR / "hosp/labevents.csv.gz"),
    ("hosp", "microbiologyevents", DATA_DIR / "hosp/microbiologyevents.csv.gz"),
    ("hosp", "omr",                DATA_DIR / "hosp/omr.csv.gz"),
    # hosp — medications
    ("hosp", "poe",                DATA_DIR / "hosp/poe.csv.gz"),
    ("hosp", "poe_detail",         DATA_DIR / "hosp/poe_detail.csv.gz"),
    ("hosp", "prescriptions",      DATA_DIR / "hosp/prescriptions.csv.gz"),
    ("hosp", "pharmacy",           DATA_DIR / "hosp/pharmacy.csv.gz"),
    ("hosp", "emar",               DATA_DIR / "hosp/emar.csv.gz"),
    ("hosp", "emar_detail",        DATA_DIR / "hosp/emar_detail.csv.gz"),
    # icu (absent in MIMIC-IV v3.1 full download — skipped if missing)
    ("icu",  "caregiver",          DATA_DIR / "icu/caregiver.csv.gz"),
    ("icu",  "d_items",            DATA_DIR / "icu/d_items.csv.gz"),
    ("icu",  "icustays",           DATA_DIR / "icu/icustays.csv.gz"),
    ("icu",  "chartevents",        DATA_DIR / "icu/chartevents.csv.gz"),
    ("icu",  "datetimeevents",     DATA_DIR / "icu/datetimeevents.csv.gz"),
    ("icu",  "outputevents",       DATA_DIR / "icu/outputevents.csv.gz"),
    ("icu",  "inputevents",        DATA_DIR / "icu/inputevents.csv.gz"),
    ("icu",  "ingredientevents",   DATA_DIR / "icu/ingredientevents.csv.gz"),
    ("icu",  "procedureevents",    DATA_DIR / "icu/procedureevents.csv.gz"),
    # note (MIMIC-IV-Note v2.2 — skipped if MIMIC_NOTE_DIR not set or missing)
    ("note", "discharge",          NOTE_DIR / "discharge.csv.gz"),
    ("note", "radiology",          NOTE_DIR / "radiology.csv.gz"),
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


class _StreamWithHeader:
    """File-like wrapper that prepends a replacement header then streams the rest.

    Reads the body one line at a time so the in-memory buffer stays small even
    for multi-GB uncompressed files.  On a truncated gzip (EOFError), the stream
    signals clean EOF so COPY commits whatever complete rows were already read.
    """

    def __init__(self, header: str, body):
        self._buf = header  # starts with just the header line
        self._body = body
        self._body_done = False
        self.truncated = False

    def _fill(self, want: int) -> None:
        while not self._body_done and len(self._buf) < want:
            try:
                line = self._body.readline()
            except EOFError:
                self.truncated = True
                self._body_done = True
                return
            if not line:
                self._body_done = True
                return
            self._buf += line

    def read(self, size=-1):
        if size == -1:
            while not self._body_done:
                self._fill(65536)
            data, self._buf = self._buf, ""
            return data
        self._fill(size)
        data, self._buf = self._buf[:size], self._buf[size:]
        return data


def load_table(cur, schema: str, table: str, csv_path: Path) -> tuple[int, bool]:
    """Returns (row_count, was_truncated)."""
    with gzip.open(csv_path, "rt", encoding="utf-8") as f:
        columns = f.readline().strip().lower()
        stream = _StreamWithHeader(columns + "\n", f)
        cur.copy_expert(
            f"COPY {schema}.{table} ({columns}) FROM STDIN WITH (FORMAT CSV, HEADER TRUE, NULL '')",
            stream,
        )
    return cur.rowcount, stream.truncated


def main(
    data_dir: Path | None = None,
    note_dir: Path | None = None,
    dsn: str | None = None,
    only_tables: list[str] | None = None,
):
    effective_dsn = dsn or DSN

    tables = TABLES
    if data_dir is not None or note_dir is not None:
        _data = data_dir or DATA_DIR
        _note = note_dir or (_data / "note")
        tables = [
            (s, t, _data / p.relative_to(DATA_DIR) if s != "note" else _note / p.relative_to(NOTE_DIR))
            for s, t, p in TABLES
        ]

    # Filter to specific tables when --tables is given
    if only_tables:
        tables = [(s, t, p) for s, t, p in tables if t in only_tables]
        if not tables:
            print(f"No matching tables found for: {only_tables}")
            return

    conn = wait_for_db(effective_dsn)
    conn.autocommit = False

    total = 0
    with conn:
        cur = conn.cursor()

        print("Truncating selected table(s)..." if only_tables else "Truncating existing data...")
        for schema, table, _ in reversed(tables):
            cur.execute(
                "SELECT 1 FROM information_schema.tables "
                "WHERE table_schema=%s AND table_name=%s",
                (schema, table),
            )
            if cur.fetchone():
                cur.execute(f"TRUNCATE TABLE {schema}.{table} CASCADE")
        conn.commit()

        errors: list[str] = []
        for schema, table, path in tables:
            if not path.exists():
                print(f"  SKIP  {schema}.{table} — file not found: {path}")
                continue
            print(f"  Loading {schema}.{table} ...", end=" ", flush=True)
            try:
                rows, truncated = load_table(cur, schema, table, path)
                conn.commit()
                if truncated:
                    print(f"{rows:,} rows  WARNING: file truncated, partial data loaded")
                else:
                    print(f"{rows:,} rows")
                total += rows
            except Exception as exc:
                conn.rollback()
                msg = str(exc).splitlines()[0]
                print(f"ERROR — {msg}")
                errors.append(f"{schema}.{table}: {msg}")

    print(f"\nDone. {total:,} total rows loaded.")
    if errors:
        print(f"\n{len(errors)} table(s) failed to load:")
        for e in errors:
            print(f"  ✗ {e}")
    conn.close()


if __name__ == "__main__":
    main()
