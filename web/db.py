"""Shared PostgreSQL access for the dashboards.

The dashboards build FHIR bundles live from the `mimic_pg` Docker database
instead of reading pre-generated JSON files. A fresh read-only connection is
opened per request (psycopg2 connections are not thread-safe and FastAPI's
sync endpoints run in a threadpool).
"""

import os

import psycopg2
import psycopg2.extras

DSN = os.getenv(
    "MIMIC_DSN",
    "host=localhost port=5433 dbname=mimiciv user=mimic password=mimic",
)


def connect():
    """Open a read-only autocommit connection to the MIMIC database."""
    conn = psycopg2.connect(DSN)
    conn.set_session(readonly=True, autocommit=True)
    return conn


def dict_cursor(conn):
    return conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)


# Cap the patient list so the UI stays responsive. The full dataset has
# ~365k patients; listing them all freezes the browser dropdown and makes
# population analytics unusable. Override with MIMIC_PATIENT_LIMIT.
PATIENT_LIMIT = int(os.getenv("MIMIC_PATIENT_LIMIT", "10000"))


def list_subject_ids() -> list[str]:
    """The first PATIENT_LIMIT patient subject_ids, ascending (as strings)."""
    conn = connect()
    try:
        cur = conn.cursor()
        cur.execute(
            "SELECT subject_id FROM hosp.patients ORDER BY subject_id LIMIT %s",
            (PATIENT_LIMIT,),
        )
        return [str(r[0]) for r in cur.fetchall()]
    finally:
        conn.close()


def patient_count() -> int:
    """Number of patients the dashboard exposes (capped at PATIENT_LIMIT)."""
    conn = connect()
    try:
        cur = conn.cursor()
        cur.execute(
            "SELECT count(*) FROM (SELECT 1 FROM hosp.patients LIMIT %s) t",
            (PATIENT_LIMIT,),
        )
        return int(cur.fetchone()[0])
    finally:
        conn.close()
