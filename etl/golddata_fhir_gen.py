#!/usr/bin/env python3
"""
golddata_fhir_gen.py — GoldData FHIR Bundle Generator

Produces one FHIR R4 transaction bundle per patient into golddata_fhir_bundles/.

What is INCLUDED (all encounters):
    • Encounter  — hospital + ICU (with full discharge disposition)
    • Observation — vitals (chartevents), labs (labevents), OMR
    • Procedure   — ICD-coded procedures
    • DiagnosticReport + microbiology Observations
    • ICU procedure events (as Observations)
    • Practitioner + Organization

What is EXCLUDED (full blind — no diagnosis or treatment leakage):
    • Condition        (ALL ICD diagnoses, all encounters)
    • MedicationRequest (ALL prescriptions, all encounters)
    • DocumentReference (clinical notes — see testing_gen.py for the +notes variant)

The testing pipeline (testing_gen.py) adds DocumentReference back but keeps
Condition and MedicationRequest excluded.

Usage:
    python -m etl.golddata_fhir_gen [--dsn DSN] [--output DIR]
    python main.py golddata [options]

Env:
    MIMIC_DSN    — PostgreSQL DSN (default: localhost:5433)
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

from etl import golddata_builder as bb

# ── Configuration ──────────────────────────────────────────────────────────────

_DEFAULT_DSN = "host=localhost port=5433 dbname=mimiciv user=mimic password=mimic"
DSN = os.getenv("MIMIC_DSN") or _DEFAULT_DSN
OUTPUT_DIR = Path(os.getenv("GOLDDATA_OUT", "golddata_fhir_bundles"))

_CHART_ITEM_IDS = list(bb.CHART_LOINC.keys())


# ── Per-patient pipeline ───────────────────────────────────────────────────────


def _latest_hadm_id(cur, subject_id: int) -> int | None:
    cur.execute(
        "SELECT hadm_id FROM hosp.admissions WHERE subject_id = %s ORDER BY admittime DESC LIMIT 1",
        (subject_id,),
    )
    row = cur.fetchone()
    return row["hadm_id"] if row else None


def convert_patient(
    cur,
    subject_id: int,
    output_dir: Path,
    include_notes: bool = False,
) -> tuple[int, int | None]:
    """Build a blinded bundle for one patient (no conditions, no medications).

    include_notes=True adds DocumentReference (discharge + radiology) — used by
    testing_gen.py to produce the testing/ variant.

    Returns (entry_count, latest_hadm_id).
    """
    entries: list[dict] = []

    def add(resource: dict) -> None:
        entries.append(bb._entry(resource))

    patient_uid = bb._uuid("patient", subject_id)

    # Keep latest_hadm for the bundle meta tag (informational only)
    latest_hadm = _latest_hadm_id(cur, subject_id)

    # ── Organization ─────────────────────────────────────────────────────────
    add(bb.build_organization())

    # ── Patient ───────────────────────────────────────────────────────────────
    cur.execute("SELECT * FROM hosp.patients WHERE subject_id = %s", (subject_id,))
    pat_row = cur.fetchone()
    if pat_row is None:
        return 0, None

    cur.execute(
        "SELECT * FROM hosp.admissions WHERE subject_id = %s ORDER BY admittime DESC LIMIT 1",
        (subject_id,),
    )
    latest_admission = cur.fetchone()
    add(bb.build_patient(pat_row, latest_admission))

    # ── Practitioners ─────────────────────────────────────────────────────────
    cur.execute(
        """
        SELECT DISTINCT admit_provider_id AS provider_id FROM hosp.admissions
        WHERE subject_id = %s AND admit_provider_id IS NOT NULL
        UNION
        SELECT DISTINCT order_provider_id FROM hosp.poe
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

    # ── Hospital encounters — full metadata, no blinding ──────────────────────
    cur.execute(
        "SELECT * FROM hosp.admissions WHERE subject_id = %s ORDER BY admittime",
        (subject_id,),
    )
    admissions = cur.fetchall()
    hosp_enc_uids: dict[int, str] = {}
    for adm in admissions:
        p_uid = provider_uids.get(adm.get("admit_provider_id") or "")
        enc = bb.build_encounter_hosp(adm, patient_uid, bb.BIDMC_UUID, p_uid)
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

    # ── CONDITIONS — excluded entirely ───────────────────────────────────────
    # (intentional: no diagnosis leakage in gold/testing pipelines)

    # ── MEDICATIONS — excluded entirely ──────────────────────────────────────
    # (intentional: no treatment leakage in gold/testing pipelines)

    # ── DRG codes per admission (used for Claim line items only) ─────────────
    cur.execute(
        "SELECT * FROM hosp.drgcodes WHERE subject_id = %s ORDER BY hadm_id",
        (subject_id,),
    )
    drg_per_hadm: dict[int, list] = defaultdict(list)
    for row in cur.fetchall():
        drg_per_hadm[row["hadm_id"]].append(row)

    # ── Claims + ExplanationOfBenefits — one per hospital encounter ──────────
    for adm in admissions:
        hadm_id = adm["hadm_id"]
        enc_uid = hosp_enc_uids[hadm_id]
        drg_rows = list(drg_per_hadm.get(hadm_id, []))
        p_uid = provider_uids.get(adm.get("admit_provider_id") or "")
        claim = bb.build_claim(adm, patient_uid, bb.BIDMC_UUID, enc_uid, drg_rows)
        add(claim)
        add(bb.build_eob(adm, patient_uid, bb.BIDMC_UUID, p_uid, claim["id"], enc_uid))

    # ── Procedures (ICD) — included (already-performed, not diagnostic) ──────
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

    # ── Lab observations — capped per patient ─────────────────────────────────
    cur.execute(
        """
        SELECT l.*, d.label
        FROM hosp.labevents l
        LEFT JOIN hosp.d_labitems d ON l.itemid = d.itemid
        WHERE l.subject_id = %s
        ORDER BY l.charttime DESC NULLS LAST
        LIMIT 500
        """,
        (subject_id,),
    )
    seen_labs: set[str] = set()
    for row in cur.fetchall():
        enc_uid = hosp_enc_uids.get(row["hadm_id"]) if row.get("hadm_id") else None
        obs = bb.build_lab_observation(row, patient_uid, enc_uid)
        if obs["id"] not in seen_labs:
            seen_labs.add(obs["id"])
            add(obs)

    # ── ICU chart observations (vitals) ───────────────────────────────────────
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

    # ── ICU procedure events ──────────────────────────────────────────────────
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

    # ── OMR observations ──────────────────────────────────────────────────────
    cur.execute(
        "SELECT * FROM hosp.omr WHERE subject_id = %s ORDER BY chartdate, seq_num",
        (subject_id,),
    )
    for row in cur.fetchall():
        add(bb.build_omr_observation(row, patient_uid))

    # ── Microbiology ──────────────────────────────────────────────────────────
    cur.execute(
        "SELECT * FROM hosp.microbiologyevents WHERE subject_id = %s ORDER BY micro_specimen_id, test_seq",
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

    # ── Clinical notes — only in testing variant ──────────────────────────────
    if include_notes:
        cur.execute(
            """
            SELECT * FROM note.discharge
            WHERE subject_id = %s
            ORDER BY charttime DESC NULLS LAST
            LIMIT 20
            """,
            (subject_id,),
        )
        for row in cur.fetchall():
            enc_uid = hosp_enc_uids.get(row["hadm_id"]) if row.get("hadm_id") else None
            add(bb.build_document_reference(row, patient_uid, enc_uid))

        cur.execute(
            """
            SELECT * FROM note.radiology
            WHERE subject_id = %s
            ORDER BY charttime DESC NULLS LAST
            LIMIT 20
            """,
            (subject_id,),
        )
        for row in cur.fetchall():
            enc_uid = hosp_enc_uids.get(row["hadm_id"]) if row.get("hadm_id") else None
            add(bb.build_document_reference(row, patient_uid, enc_uid))

    # ── Write bundle ──────────────────────────────────────────────────────────
    bundle = bb.build_bundle(entries, latest_hadm_id=latest_hadm)
    out_path = output_dir / f"{subject_id}.json"
    out_path.write_text(json.dumps(bundle, default=str, indent=2), encoding="utf-8")
    return len(entries), latest_hadm


# ── Full pipeline ──────────────────────────────────────────────────────────────


def convert(
    dsn: str = DSN,
    output_dir: Path = OUTPUT_DIR,
    include_notes: bool = False,
    limit: int | None = None,
    offset: int = 0,
    subject_ids: list[int] | None = None,
    random_sample: bool = True,
) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)

    variant = "Testing (blind + notes)" if include_notes else "GoldData (blind)"
    print(f"{variant} FHIR Generator")
    print(f"  DSN    : {dsn}")
    print(f"  Output : {output_dir.resolve()}/")
    print(f"  Mode   : Conditions + Medications excluded from all encounters")
    print(f"  Notes  : {'included' if include_notes else 'excluded'}\n")

    conn = psycopg2.connect(dsn)
    conn.set_session(readonly=True, autocommit=True)
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

    if subject_ids is not None:
        sids = subject_ids
    else:
        effective_limit = limit if limit is not None else (20 if random_sample else None)
        if random_sample:
            query = "SELECT subject_id FROM hosp.patients ORDER BY RANDOM()"
        else:
            query = "SELECT subject_id FROM hosp.patients ORDER BY subject_id"
            if offset:
                query += f" OFFSET {offset}"
        if effective_limit:
            query += f" LIMIT {effective_limit}"
        cur.execute(query)
        sids = [r["subject_id"] for r in cur.fetchall()]

    total = len(sids)
    width = len(str(total))
    print(f"Processing {total:,} patients → {output_dir.resolve()}/\n")

    total_entries = 0
    errors = 0
    for i, sid in enumerate(sids, 1):
        try:
            n, latest_hadm = convert_patient(cur, sid, output_dir, include_notes=include_notes)
            total_entries += n
            print(
                f"  [{i:{width}d}/{total}]  subject {sid:>10}  "
                f"{n:5d} entries  → {sid}.json"
            )
        except Exception as exc:
            errors += 1
            print(f"  [{i:{width}d}/{total}]  subject {sid:>10}  ERROR: {exc}")

    cur.close()
    conn.close()

    print(f"\nDone. {total - errors:,}/{total:,} bundles, {total_entries:,} total entries.")
    if errors:
        print(f"  {errors} patient(s) skipped due to errors.")
        sys.exit(1)


# ── CLI ────────────────────────────────────────────────────────────────────────


def _parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description="Generate GoldData FHIR bundles (no conditions, no medications)."
    )
    p.add_argument("--dsn", default=DSN, help="PostgreSQL DSN")
    p.add_argument("--output", default=str(OUTPUT_DIR), help="Output directory")
    p.add_argument("--notes", action="store_true", help="Include clinical notes (testing variant)")
    p.add_argument("--limit", type=int, default=None, help="Max patients to process")
    p.add_argument("--offset", type=int, default=0, help="Skip first N patients")
    p.add_argument("--subject-ids", default=None, help="Comma-separated subject_ids")
    p.add_argument("--patient", type=int, default=None, help="Single patient (for testing)")
    return p.parse_args()


if __name__ == "__main__":
    args = _parse_args()
    out = Path(args.output)

    if args.patient:
        out.mkdir(parents=True, exist_ok=True)
        conn = psycopg2.connect(args.dsn)
        conn.set_session(readonly=True, autocommit=True)
        cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        n, hadm = convert_patient(cur, args.patient, out, include_notes=args.notes)
        cur.close()
        conn.close()
        print(f"subject {args.patient}: {n} entries → {out}/{args.patient}.json")
    else:
        sids = [int(s.strip()) for s in args.subject_ids.split(",")] if args.subject_ids else None
        convert(
            dsn=args.dsn,
            output_dir=out,
            include_notes=args.notes,
            limit=args.limit,
            offset=args.offset,
            subject_ids=sids,
        )
