#!/usr/bin/env python3
"""
golddata_fhir_gen.py — GoldData FHIR Bundle Generator

Produces one FHIR R4 transaction bundle per patient into golddata_fhir_bundles/.

Key difference from the standard pipeline (mimic_to_bundle.py):
  For each patient's LATEST (most-recent) hospital encounter the following are
  intentionally EXCLUDED to prevent outcome/diagnosis leakage:
    • Condition resources  (ICD diagnoses)
    • Discharge disposition from the Encounter (outcome signal)

Everything else is INCLUDED for all encounters — including the latest:
    • Encounter (hospital + ICU)
    • Observation — vitals (chartevents), labs (labevents), OMR
    • Procedure  — ICD-coded procedures already performed
    • MedicationRequest — medications administered
    • DiagnosticReport + microbiology Observations
    • ICU procedure events (as Observations)

Historical encounters include full data (conditions, discharge disposition).

Usage:
    python golddata_fhir_gen.py [--dsn DSN] [--output DIR]

Env:
    GOLDDATA_DSN  — PostgreSQL DSN (falls back to MIMIC_DSN, then built-in default)
    GOLDDATA_OUT  — output directory (default: golddata_fhir_bundles)
"""

import argparse
import json
import os
import sys
from collections import defaultdict
from itertools import groupby
from pathlib import Path

import psycopg2
import psycopg2.extras

import golddata_bundle_builder as bb

# ── Configuration ──────────────────────────────────────────────────────────────

_DEFAULT_DSN = "host=localhost port=5433 dbname=mimiciv user=mimic password=mimic"

DSN = os.getenv("GOLDDATA_DSN") or os.getenv("MIMIC_DSN") or _DEFAULT_DSN
OUTPUT_DIR = Path(os.getenv("GOLDDATA_OUT", "golddata_fhir_bundles"))

# ICU chart items to fetch (vitals + common monitors)
_CHART_ITEM_IDS = list(bb.CHART_LOINC.keys())


# ── Per-patient pipeline ───────────────────────────────────────────────────────


def _latest_hadm_id(cur, subject_id: int) -> int | None:
    cur.execute(
        """
        SELECT hadm_id FROM hosp.admissions
        WHERE subject_id = %s
        ORDER BY admittime DESC
        LIMIT 1
        """,
        (subject_id,),
    )
    row = cur.fetchone()
    return row["hadm_id"] if row else None


def convert_patient(cur, subject_id: int, output_dir: Path) -> tuple[int, int | None]:
    """Build and write a golddata bundle for one patient.

    Returns (entry_count, latest_hadm_id).
    """
    entries: list[dict] = []

    def add(resource: dict) -> None:
        entries.append(bb._entry(resource))

    patient_uid = bb._uuid("patient", subject_id)

    # ── Identify latest encounter so we can blind its diagnoses ───────────────
    latest_hadm = _latest_hadm_id(cur, subject_id)

    # ── Organization ─────────────────────────────────────────────────────────
    add(bb.build_organization())

    # ── Patient ───────────────────────────────────────────────────────────────
    cur.execute("SELECT * FROM hosp.patients WHERE subject_id = %s", (subject_id,))
    pat_row = cur.fetchone()
    if pat_row is None:
        return 0, None

    # Use the latest admission for patient-level demographics (race, language, etc.)
    cur.execute(
        """
        SELECT * FROM hosp.admissions
        WHERE subject_id = %s
        ORDER BY admittime DESC
        LIMIT 1
        """,
        (subject_id,),
    )
    latest_admission = cur.fetchone()

    add(bb.build_patient(pat_row, latest_admission))

    # ── Practitioners ─────────────────────────────────────────────────────────
    cur.execute(
        """
        SELECT DISTINCT admit_provider_id AS provider_id
        FROM hosp.admissions
        WHERE subject_id = %s AND admit_provider_id IS NOT NULL
        UNION
        SELECT DISTINCT order_provider_id
        FROM hosp.poe
        WHERE subject_id = %s AND order_provider_id IS NOT NULL
        LIMIT 20
        """,
        (subject_id, subject_id),
    )
    provider_uids: dict[str, str] = {}
    for p in cur.fetchall():
        pid = p["provider_id"]
        uid = bb._uuid("practitioner", pid)
        provider_uids[pid] = uid
        add(bb.build_practitioner(pid))

    # ── Hospital encounters ───────────────────────────────────────────────────
    cur.execute(
        "SELECT * FROM hosp.admissions WHERE subject_id = %s ORDER BY admittime",
        (subject_id,),
    )
    admissions = cur.fetchall()
    hosp_enc_uids: dict[int, str] = {}
    for adm in admissions:
        is_latest = adm["hadm_id"] == latest_hadm
        p_uid = provider_uids.get(adm.get("admit_provider_id") or "")
        enc = bb.build_encounter_hosp(
            adm, patient_uid, bb.BIDMC_UUID, p_uid, is_latest=is_latest
        )
        hosp_enc_uids[adm["hadm_id"]] = enc["id"]
        add(enc)

    # ── ICU encounters ────────────────────────────────────────────────────────
    cur.execute(
        "SELECT * FROM icu.icustays WHERE subject_id = %s ORDER BY intime",
        (subject_id,),
    )
    icu_enc_uids: dict[int, str] = {}
    for icu in cur.fetchall():
        hosp_uid = hosp_enc_uids.get(icu["hadm_id"])
        if not hosp_uid:
            continue
        enc = bb.build_encounter_icu(icu, patient_uid, hosp_uid)
        icu_enc_uids[icu["stay_id"]] = enc["id"]
        add(enc)

    # ── Conditions — EXCLUDE for latest encounter ─────────────────────────────
    cur.execute(
        """
        SELECT d.*, i.long_title, a.admittime
        FROM hosp.diagnoses_icd d
        LEFT JOIN hosp.d_icd_diagnoses i
               ON d.icd_code = i.icd_code AND d.icd_version = i.icd_version
        LEFT JOIN hosp.admissions a ON d.hadm_id = a.hadm_id
        WHERE d.subject_id = %s
        ORDER BY d.hadm_id, d.seq_num
        """,
        (subject_id,),
    )
    conditions_excluded = 0
    for row in cur.fetchall():
        if row["hadm_id"] == latest_hadm:
            conditions_excluded += 1
            continue  # intentional exclusion — golddata blind spot
        enc_uid = hosp_enc_uids.get(row["hadm_id"])
        if enc_uid:
            add(bb.build_condition(row, patient_uid, enc_uid))

    # ── Procedures (ICD) — include all (procedures already performed) ─────────
    cur.execute(
        """
        SELECT p.*, i.long_title
        FROM hosp.procedures_icd p
        LEFT JOIN hosp.d_icd_procedures i
               ON p.icd_code = i.icd_code AND p.icd_version = i.icd_version
        WHERE p.subject_id = %s
        ORDER BY p.hadm_id, p.seq_num
        """,
        (subject_id,),
    )
    for row in cur.fetchall():
        enc_uid = hosp_enc_uids.get(row["hadm_id"])
        if enc_uid:
            add(bb.build_procedure(row, patient_uid, enc_uid))

    # ── Lab observations — include all ────────────────────────────────────────
    cur.execute(
        """
        SELECT l.*, d.label
        FROM hosp.labevents l
        LEFT JOIN hosp.d_labitems d ON l.itemid = d.itemid
        WHERE l.subject_id = %s
        """,
        (subject_id,),
    )
    seen_labs: set[str] = set()
    for row in cur.fetchall():
        enc_uid = (
            hosp_enc_uids.get(row["hadm_id"]) if row.get("hadm_id") else None
        )
        obs = bb.build_lab_observation(row, patient_uid, enc_uid)
        # Deduplicate by ID (same labevent_id can appear if join produces duplicates)
        if obs["id"] not in seen_labs:
            seen_labs.add(obs["id"])
            add(obs)

    # ── ICU chart observations (vitals) — include all ─────────────────────────
    if _CHART_ITEM_IDS:
        placeholders = ",".join("%s" for _ in _CHART_ITEM_IDS)
        cur.execute(
            f"""
            SELECT c.*, d.label
            FROM icu.chartevents c
            LEFT JOIN icu.d_items d ON c.itemid = d.itemid
            WHERE c.subject_id = %s AND c.itemid IN ({placeholders})
            """,
            (subject_id, *_CHART_ITEM_IDS),
        )
        seen_charts: set[str] = set()
        for row in cur.fetchall():
            enc_uid = icu_enc_uids.get(row["stay_id"])
            if enc_uid:
                obs = bb.build_chart_observation(row, patient_uid, enc_uid)
                if obs["id"] not in seen_charts:
                    seen_charts.add(obs["id"])
                    add(obs)

    # ── ICU procedure events (ventilation, dialysis, vasopressors, etc.) ──────
    cur.execute(
        """
        SELECT pe.*, d.label
        FROM icu.procedureevents pe
        LEFT JOIN icu.d_items d ON pe.itemid = d.itemid
        WHERE pe.subject_id = %s
        ORDER BY pe.starttime
        """,
        (subject_id,),
    )
    for row in cur.fetchall():
        enc_uid = icu_enc_uids.get(row["stay_id"])
        if enc_uid:
            add(bb.build_icu_procedure_observation(row, patient_uid, enc_uid))

    # ── Medication requests — include all (medications administered) ───────────
    cur.execute(
        "SELECT * FROM hosp.prescriptions WHERE subject_id = %s",
        (subject_id,),
    )
    for row in cur.fetchall():
        enc_uid = hosp_enc_uids.get(row["hadm_id"])
        if enc_uid:
            add(bb.build_medication_request(row, patient_uid, enc_uid))

    # ── OMR observations (outpatient vitals/measurements) — include all ────────
    cur.execute(
        "SELECT * FROM hosp.omr WHERE subject_id = %s ORDER BY chartdate, seq_num",
        (subject_id,),
    )
    for row in cur.fetchall():
        add(bb.build_omr_observation(row, patient_uid))

    # ── Microbiology (DiagnosticReport + Observations) — include all ──────────
    cur.execute(
        """
        SELECT * FROM hosp.microbiologyevents
        WHERE subject_id = %s
        ORDER BY micro_specimen_id, test_seq
        """,
        (subject_id,),
    )
    micro_rows = cur.fetchall()
    for _, group in groupby(micro_rows, key=lambda r: r["micro_specimen_id"]):
        group_list = list(group)
        enc_uid = (
            hosp_enc_uids.get(group_list[0]["hadm_id"])
            if group_list[0].get("hadm_id")
            else None
        )
        for resource in bb.build_diagnostic_report(group_list, patient_uid, enc_uid):
            add(resource)

    # ── Write bundle ──────────────────────────────────────────────────────────
    bundle = bb.build_bundle(entries, latest_hadm_id=latest_hadm)
    out_path = output_dir / f"{subject_id}.json"
    out_path.write_text(json.dumps(bundle, default=str, indent=2), encoding="utf-8")

    return len(entries), latest_hadm


# ── Full pipeline ──────────────────────────────────────────────────────────────


def convert(dsn: str = DSN, output_dir: Path = OUTPUT_DIR) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"GoldData FHIR Generator")
    print(f"  DSN        : {dsn}")
    print(f"  Output     : {output_dir.resolve()}/")
    print(f"  Mode       : exclude diagnoses for each patient's latest encounter\n")

    conn = psycopg2.connect(dsn)
    conn.set_session(readonly=True, autocommit=True)
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

    cur.execute("SELECT subject_id FROM hosp.patients ORDER BY subject_id")
    subject_ids = [r["subject_id"] for r in cur.fetchall()]

    print(f"Processing {len(subject_ids)} patients → {output_dir.resolve()}/\n")

    total_entries = 0
    errors = 0
    for i, sid in enumerate(subject_ids, 1):
        try:
            n, latest_hadm = convert_patient(cur, sid, output_dir)
            total_entries += n
            print(
                f"  [{i:3d}/{len(subject_ids)}]  subject {sid:>10}  "
                f"{n:4d} entries  latest_hadm={latest_hadm}  → {sid}.json"
            )
        except Exception as exc:
            errors += 1
            print(f"  [{i:3d}/{len(subject_ids)}]  subject {sid:>10}  ERROR: {exc}")

    cur.close()
    conn.close()

    print(
        f"\nDone. {len(subject_ids) - errors}/{len(subject_ids)} bundles, "
        f"{total_entries:,} total entries."
    )
    if errors:
        print(f"  {errors} patient(s) skipped due to errors.")
        sys.exit(1)


# ── CLI ────────────────────────────────────────────────────────────────────────


def _parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description="Generate GoldData FHIR bundles (diagnosis-blind latest encounter)."
    )
    p.add_argument(
        "--dsn",
        default=DSN,
        help="PostgreSQL DSN (default: GOLDDATA_DSN env or MIMIC_DSN env or built-in)",
    )
    p.add_argument(
        "--output",
        default=str(OUTPUT_DIR),
        help="Output directory (default: golddata_fhir_bundles)",
    )
    p.add_argument(
        "--patient",
        type=int,
        default=None,
        help="Process a single patient by subject_id (for testing)",
    )
    return p.parse_args()


if __name__ == "__main__":
    args = _parse_args()
    out = Path(args.output)

    if args.patient:
        out.mkdir(parents=True, exist_ok=True)
        conn = psycopg2.connect(args.dsn)
        conn.set_session(readonly=True, autocommit=True)
        cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        n, hadm = convert_patient(cur, args.patient, out)
        cur.close()
        conn.close()
        print(f"subject {args.patient}: {n} entries, latest_hadm={hadm} → {out}/{args.patient}.json")
    else:
        convert(dsn=args.dsn, output_dir=out)
