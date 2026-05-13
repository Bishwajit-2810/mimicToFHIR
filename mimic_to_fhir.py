#!/usr/bin/env python3
"""
Convert MIMIC-IV (PostgreSQL) to FHIR R4 NDJSON.

Mappings
--------
hosp.patients          -> Patient
hosp.admissions        -> Encounter  (hospital)
icu.icustays           -> Encounter  (ICU, partOf hospital encounter)
hosp.diagnoses_icd     -> Condition
hosp.procedures_icd    -> Procedure
hosp.labevents         -> Observation (laboratory)
icu.chartevents        -> Observation (vital-signs / clinical)
hosp.prescriptions     -> MedicationRequest
hosp.microbiologyevents-> DiagnosticReport + Observation
hosp.omr               -> Observation (survey / outpatient measurements)

Output: one .ndjson file per resource type in ./fhir_output/
"""

import json
import os
import re
import sys
import uuid
from datetime import date, datetime
from pathlib import Path
from typing import Any

import psycopg2
import psycopg2.extras

# ── connection ────────────────────────────────────────────────────────────────
DSN = os.getenv(
    "MIMIC_DSN",
    "host=localhost port=5433 dbname=mimiciv user=mimic password=mimic",
)
OUTPUT_DIR = Path("fhir_output")

# Stable UUID namespace so resource IDs are UUID-shaped but still reproducible.
_NS = uuid.UUID("6ba7b810-9dad-11d1-80b4-00c04fd430c8")
_RANGE_RE = re.compile(r"^(\d*\.?\d+)-(\d*\.?\d+)$")

# ── helpers ───────────────────────────────────────────────────────────────────


def _dt(v) -> str | None:
    """Return ISO-8601 string or None for datetime/date values."""
    if v is None:
        return None
    if isinstance(v, datetime):
        return v.isoformat()
    if isinstance(v, date):
        return v.isoformat()
    return str(v)


def _uuid(*keys) -> str:
    return str(uuid.uuid5(_NS, "mimic-iv::" + "::".join(str(k) for k in keys)))


def _numeric_value(value: Any) -> int | float | Any:
    if isinstance(value, str):
        stripped = value.strip()
        if not stripped:
            return value
        try:
            number = float(stripped)
        except ValueError:
            return value
        return int(number) if number.is_integer() else number
    return value


def _quantity(value: Any, unit: str | None = None, system: str | None = None) -> dict:
    quantity: dict[str, Any] = {"value": _numeric_value(value)}
    if unit:
        quantity["unit"] = unit
    if system:
        quantity["system"] = system
    return quantity


def _dose_and_rate(dose_value: Any, dose_unit: str | None) -> dict | None:
    if dose_value is None or not dose_unit:
        return None

    if isinstance(dose_value, str):
        stripped = dose_value.strip()
        range_match = _RANGE_RE.match(stripped)
        if range_match:
            return {
                "doseRange": {
                    "low": _quantity(
                        range_match.group(1), dose_unit, "http://unitsofmeasure.org"
                    ),
                    "high": _quantity(
                        range_match.group(2), dose_unit, "http://unitsofmeasure.org"
                    ),
                }
            }
        dose_value = stripped

    return {
        "doseQuantity": _quantity(dose_value, dose_unit, "http://unitsofmeasure.org")
    }


def _ref(resource_type: str, id_: Any) -> dict:
    return {"reference": f"{resource_type}/{id_}"}


def _coding(system: str, code: str, display: str | None = None) -> dict:
    c = {"system": system, "code": str(code)}
    if display:
        c["display"] = display
    return c


def _icd_system(version: int) -> str:
    return (
        "http://hl7.org/fhir/sid/icd-10-cm"
        if version == 10
        else "http://hl7.org/fhir/sid/icd-9-cm"
    )


# ── resource builders ─────────────────────────────────────────────────────────


def build_patient(row: dict) -> dict:
    r: dict = {
        "resourceType": "Patient",
        "id": _uuid("patient", row["subject_id"]),
        "gender": "female" if row["gender"] == "F" else "male",
        "extension": [
            {
                "url": "http://mimic.mit.edu/fhir/StructureDefinition/anchor-age",
                "valueInteger": row["anchor_age"],
            },
            {
                "url": "http://mimic.mit.edu/fhir/StructureDefinition/anchor-year-group",
                "valueString": row["anchor_year_group"],
            },
        ],
    }
    if row["dod"]:
        r["deceasedDateTime"] = _dt(row["dod"])
    return r


def build_encounter_hosp(row: dict) -> dict:
    r: dict = {
        "resourceType": "Encounter",
        "id": _uuid("encounter-hosp", row["hadm_id"]),
        "status": "finished",
        "class": _coding(
            "http://terminology.hl7.org/CodeSystem/v3-ActCode",
            "IMP",
            "inpatient encounter",
        ),
        "subject": _ref("Patient", _uuid("patient", row["subject_id"])),
        "period": {"start": _dt(row["admittime"])},
        "type": [
            {
                "coding": [
                    _coding(
                        "http://snomed.info/sct",
                        "11429006",
                        row["admission_type"],
                    )
                ],
                "text": row["admission_type"],
            }
        ],
    }
    if row["dischtime"]:
        r["period"]["end"] = _dt(row["dischtime"])
    if row["hospital_expire_flag"]:
        r["hospitalization"] = {
            "dischargeDisposition": {
                "coding": [
                    _coding(
                        "http://terminology.hl7.org/CodeSystem/discharge-disposition",
                        "exp",
                        "Expired",
                    )
                ]
            }
        }
    elif row["discharge_location"]:
        r.setdefault("hospitalization", {})["dischargeDisposition"] = {
            "text": row["discharge_location"]
        }
    if row["admission_location"]:
        r.setdefault("hospitalization", {})["admitSource"] = {
            "text": row["admission_location"]
        }
    # Race / ethnicity as extension
    if row["race"]:
        r.setdefault("extension", []).append(
            {
                "url": "http://hl7.org/fhir/us/core/StructureDefinition/us-core-race",
                "valueString": row["race"],
            }
        )
    return r


def build_encounter_icu(row: dict) -> dict:
    return {
        "resourceType": "Encounter",
        "id": _uuid("encounter-icu", row["stay_id"]),
        "status": "finished",
        "class": _coding(
            "http://terminology.hl7.org/CodeSystem/v3-ActCode", "ACUTE", "ICU"
        ),
        "subject": _ref("Patient", _uuid("patient", row["subject_id"])),
        "partOf": _ref("Encounter", _uuid("encounter-hosp", row["hadm_id"])),
        "period": {
            "start": _dt(row["intime"]),
            **({"end": _dt(row["outtime"])} if row["outtime"] else {}),
        },
        "location": [
            {
                "location": {"display": row["first_careunit"]},
                "status": "completed",
            }
        ],
        "extension": [
            {
                "url": "http://mimic.mit.edu/fhir/StructureDefinition/los",
                "valueDecimal": round(float(row["los"]), 4) if row["los"] else None,
            }
        ],
    }


def build_condition(row: dict) -> dict:
    return {
        "resourceType": "Condition",
        "id": _uuid("condition", row["hadm_id"], row["seq_num"]),
        "subject": _ref("Patient", _uuid("patient", row["subject_id"])),
        "encounter": _ref("Encounter", _uuid("encounter-hosp", row["hadm_id"])),
        "code": {
            "coding": [
                _coding(
                    _icd_system(row["icd_version"]),
                    row["icd_code"],
                    row.get("long_title"),
                )
            ],
            "text": row.get("long_title"),
        },
        "category": [
            {
                "coding": [
                    _coding(
                        "http://terminology.hl7.org/CodeSystem/condition-category",
                        "encounter-diagnosis",
                        "Encounter Diagnosis",
                    )
                ]
            }
        ],
        "clinicalStatus": {
            "coding": [
                _coding(
                    "http://terminology.hl7.org/CodeSystem/condition-clinical", "active"
                )
            ]
        },
        "verificationStatus": {
            "coding": [
                _coding(
                    "http://terminology.hl7.org/CodeSystem/condition-ver-status",
                    "confirmed",
                )
            ]
        },
    }


def build_procedure(row: dict) -> dict:
    return {
        "resourceType": "Procedure",
        "id": _uuid("procedure", row["hadm_id"], row["seq_num"]),
        "status": "completed",
        "subject": _ref("Patient", _uuid("patient", row["subject_id"])),
        "encounter": _ref("Encounter", _uuid("encounter-hosp", row["hadm_id"])),
        "code": {
            "coding": [
                _coding(
                    _icd_system(row["icd_version"]),
                    row["icd_code"],
                    row.get("long_title"),
                )
            ],
            "text": row.get("long_title"),
        },
        **(
            {"performedDateTime": _dt(row["chartdate"])} if row.get("chartdate") else {}
        ),
    }


def build_lab_observation(row: dict) -> dict:
    obs: dict = {
        "resourceType": "Observation",
        "id": _uuid("lab", row["labevent_id"]),
        "status": "final",
        "category": [
            {
                "coding": [
                    _coding(
                        "http://terminology.hl7.org/CodeSystem/observation-category",
                        "laboratory",
                    )
                ]
            }
        ],
        "code": {
            "coding": [
                _coding("http://loinc.org", str(row["itemid"]), row.get("label"))
            ],
            "text": row.get("label"),
        },
        "subject": _ref("Patient", _uuid("patient", row["subject_id"])),
        **(
            {"encounter": _ref("Encounter", _uuid("encounter-hosp", row["hadm_id"]))}
            if row["hadm_id"]
            else {}
        ),
        **({"effectiveDateTime": _dt(row["charttime"])} if row["charttime"] else {}),
    }
    if row["valuenum"] is not None:
        obs["valueQuantity"] = {
            **_quantity(
                float(row["valuenum"]),
                row["valueuom"] or None,
                "http://unitsofmeasure.org",
            ),
        }
    elif row["value"]:
        obs["valueString"] = row["value"]

    if row["flag"]:
        obs["interpretation"] = [
            {
                "coding": [
                    _coding(
                        "http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation",
                        (
                            "H"
                            if "abnormal" in (row["flag"] or "").lower()
                            else row["flag"][0].upper()
                        ),
                        row["flag"],
                    )
                ]
            }
        ]
    if row["ref_range_lower"] is not None or row["ref_range_upper"] is not None:
        rr: dict = {}
        if row["ref_range_lower"] is not None:
            rr["low"] = _quantity(
                float(row["ref_range_lower"]),
                row["valueuom"] or None,
                "http://unitsofmeasure.org",
            )
        if row["ref_range_upper"] is not None:
            rr["high"] = _quantity(
                float(row["ref_range_upper"]),
                row["valueuom"] or None,
                "http://unitsofmeasure.org",
            )
        obs["referenceRange"] = [rr]
    return obs


# LOINC codes for common ICU chart items (itemid → loinc)
_CHART_LOINC = {
    220045: "8867-4",  # Heart Rate
    220050: "8480-6",  # Systolic BP
    220051: "8462-4",  # Diastolic BP
    220052: "8478-0",  # Mean BP
    220210: "9279-1",  # Respiratory Rate
    223761: "8310-5",  # Temperature F
    223762: "8310-5",  # Temperature C
    220277: "2708-6",  # SpO2
    226253: "29463-7",  # Weight
}


def build_chart_observation(row: dict) -> dict:
    loinc = _CHART_LOINC.get(row["itemid"])
    coding = []
    if loinc:
        coding.append(_coding("http://loinc.org", loinc, row.get("label")))
    coding.append(
        _coding(
            "http://mimic.mit.edu/fhir/CodeSystem/d-items",
            str(row["itemid"]),
            row.get("label"),
        )
    )

    obs: dict = {
        "resourceType": "Observation",
        "id": _uuid("chart", row["stay_id"], row["itemid"], _dt(row["charttime"])),
        "status": "final",
        "category": [
            {
                "coding": [
                    _coding(
                        "http://terminology.hl7.org/CodeSystem/observation-category",
                        "vital-signs" if loinc else "survey",
                    )
                ]
            }
        ],
        "code": {"coding": coding, "text": row.get("label")},
        "subject": _ref("Patient", _uuid("patient", row["subject_id"])),
        "encounter": _ref("Encounter", _uuid("encounter-icu", row["stay_id"])),
        "effectiveDateTime": _dt(row["charttime"]),
    }
    if row["valuenum"] is not None:
        obs["valueQuantity"] = {
            **_quantity(
                float(row["valuenum"]),
                row["valueuom"] or None,
                "http://unitsofmeasure.org",
            ),
        }
    elif row["value"]:
        obs["valueString"] = str(row["value"])
    return obs


def build_medication_request(row: dict) -> dict:
    r: dict = {
        "resourceType": "MedicationRequest",
        "id": _uuid(
            "rx",
            row["subject_id"],
            row["hadm_id"],
            row.get("pharmacy_id") or row.get("poe_id") or row.get("starttime"),
        ),
        "status": "completed",
        "intent": "order",
        "subject": _ref("Patient", _uuid("patient", row["subject_id"])),
        "encounter": _ref("Encounter", _uuid("encounter-hosp", row["hadm_id"])),
        "medicationCodeableConcept": {
            "text": row["drug"],
            "coding": [],
        },
    }
    if row["ndc"]:
        r["medicationCodeableConcept"]["coding"].append(
            _coding("http://hl7.org/fhir/sid/ndc", row["ndc"], row["drug"])
        )
    if not r["medicationCodeableConcept"]["coding"]:
        del r["medicationCodeableConcept"]["coding"]

    dosage: dict = {}
    dose_and_rate = _dose_and_rate(row.get("dose_val_rx"), row.get("dose_unit_rx"))
    if dose_and_rate:
        dosage["doseAndRate"] = [dose_and_rate]
    if row["route"]:
        dosage["route"] = {"text": row["route"]}
    if dosage:
        r["dosageInstruction"] = [dosage]

    timing: dict = {}
    if row["starttime"]:
        timing["start"] = _dt(row["starttime"])
    if row["stoptime"]:
        timing["end"] = _dt(row["stoptime"])
    if timing:
        r["dispenseRequest"] = {"validityPeriod": timing}
    return r


def build_diagnostic_report(rows: list[dict]) -> list[dict]:
    """One DiagnosticReport per micro_specimen_id, with child Observations."""
    first = rows[0]
    report_id = _uuid("micro-report", first["micro_specimen_id"])
    obs_resources = []
    obs_refs = []

    for i, row in enumerate(rows):
        obs_id = _uuid("micro-obs", row["micro_specimen_id"], i)
        obs: dict = {
            "resourceType": "Observation",
            "id": obs_id,
            "status": "final",
            "category": [
                {
                    "coding": [
                        _coding(
                            "http://terminology.hl7.org/CodeSystem/observation-category",
                            "laboratory",
                        )
                    ]
                }
            ],
            "code": {
                "text": row["test_name"] or row["spec_type_desc"],
                "coding": [
                    _coding(
                        "http://mimic.mit.edu/fhir/CodeSystem/micro-test",
                        str(row["test_itemid"] or row["spec_itemid"]),
                        row["test_name"],
                    )
                ],
            },
            "subject": _ref("Patient", _uuid("patient", row["subject_id"])),
            **(
                {
                    "encounter": _ref(
                        "Encounter", _uuid("encounter-hosp", row["hadm_id"])
                    )
                }
                if row["hadm_id"]
                else {}
            ),
            **({"effectiveDateTime": _dt(row["charttime"] or row["chartdate"])}),
        }
        if row["org_name"]:
            obs["valueString"] = row["org_name"]
            if row["interpretation"]:
                obs["interpretation"] = [{"text": row["interpretation"]}]
        obs_resources.append(obs)
        obs_refs.append(_ref("Observation", obs_id))

    report: dict = {
        "resourceType": "DiagnosticReport",
        "id": report_id,
        "status": "final",
        "category": [
            {
                "coding": [
                    _coding(
                        "http://terminology.hl7.org/CodeSystem/v2-0074",
                        "MB",
                        "Microbiology",
                    )
                ]
            }
        ],
        "code": {"text": first["spec_type_desc"]},
        "subject": _ref("Patient", _uuid("patient", first["subject_id"])),
        **(
            {"encounter": _ref("Encounter", _uuid("encounter-hosp", first["hadm_id"]))}
            if first["hadm_id"]
            else {}
        ),
        "effectiveDateTime": _dt(first["charttime"] or first["chartdate"]),
        "result": obs_refs,
    }
    return [report] + obs_resources


def build_omr_observation(row: dict) -> dict:
    return {
        "resourceType": "Observation",
        "id": _uuid("omr", row["subject_id"], _dt(row["chartdate"]), row["seq_num"]),
        "status": "final",
        "category": [
            {
                "coding": [
                    _coding(
                        "http://terminology.hl7.org/CodeSystem/observation-category",
                        "survey",
                    )
                ]
            }
        ],
        "code": {"text": row["result_name"]},
        "subject": _ref("Patient", _uuid("patient", row["subject_id"])),
        "effectiveDateTime": _dt(row["chartdate"]),
        "valueString": row["result_value"],
    }


# ── writer ────────────────────────────────────────────────────────────────────


class NdjsonWriter:
    def __init__(self, output_dir: Path):
        self._dir = output_dir
        self._dir.mkdir(parents=True, exist_ok=True)
        self._files: dict[str, Any] = {}
        self._counts: dict[str, int] = {}

    def write(self, resource: dict):
        rt = resource["resourceType"]
        if rt not in self._files:
            path = self._dir / f"{rt}.ndjson"
            self._files[rt] = open(path, "w", encoding="utf-8")
            self._counts[rt] = 0
        self._files[rt].write(json.dumps(resource, default=str) + "\n")
        self._counts[rt] += 1

    def close(self):
        for f in self._files.values():
            f.close()

    def summary(self) -> dict[str, int]:
        return dict(self._counts)


# ── main pipeline ─────────────────────────────────────────────────────────────


def convert(dsn: str = DSN, output_dir: Path = OUTPUT_DIR, *, batch_size: int = 2000):
    conn = psycopg2.connect(dsn)
    conn.set_session(readonly=True, autocommit=True)
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    writer = NdjsonWriter(output_dir)

    def run(label: str, sql: str, builder):
        print(f"  {label} ...", end=" ", flush=True)
        cur.execute(sql)
        n = 0
        while True:
            rows = cur.fetchmany(batch_size)
            if not rows:
                break
            for row in rows:
                writer.write(builder(row))
                n += 1
        print(n)

    print("Converting MIMIC-IV → FHIR R4")
    print(f"Output: {output_dir.resolve()}\n")

    # Patient
    run(
        "Patient",
        "SELECT * FROM hosp.patients",
        build_patient,
    )

    # Encounter (hospital)
    run(
        "Encounter (hospital)",
        "SELECT * FROM hosp.admissions",
        build_encounter_hosp,
    )

    # Encounter (ICU)
    run(
        "Encounter (ICU)",
        "SELECT * FROM icu.icustays",
        build_encounter_icu,
    )

    # Condition
    run(
        "Condition",
        """
        SELECT d.subject_id, d.hadm_id, d.seq_num, d.icd_code, d.icd_version,
               i.long_title
        FROM hosp.diagnoses_icd d
        LEFT JOIN hosp.d_icd_diagnoses i
               ON d.icd_code = i.icd_code AND d.icd_version = i.icd_version
        """,
        build_condition,
    )

    # Procedure
    run(
        "Procedure",
        """
        SELECT p.subject_id, p.hadm_id, p.seq_num, p.icd_code, p.icd_version,
               p.chartdate, i.long_title
        FROM hosp.procedures_icd p
        LEFT JOIN hosp.d_icd_procedures i
               ON p.icd_code = i.icd_code AND p.icd_version = i.icd_version
        """,
        build_procedure,
    )

    # Observation — lab
    run(
        "Observation (lab)",
        """
        SELECT l.*, d.label
        FROM hosp.labevents l
        LEFT JOIN hosp.d_labitems d ON l.itemid = d.itemid
        """,
        build_lab_observation,
    )

    # Observation — chart (vitals only to keep output manageable; remove WHERE to get all)
    run(
        "Observation (chart vitals)",
        f"""
        SELECT c.*, d.label
        FROM icu.chartevents c
        LEFT JOIN icu.d_items d ON c.itemid = d.itemid
        WHERE c.itemid IN ({','.join(str(k) for k in _CHART_LOINC)})
        """,
        build_chart_observation,
    )

    # MedicationRequest
    run(
        "MedicationRequest",
        "SELECT * FROM hosp.prescriptions",
        build_medication_request,
    )

    # OMR Observations
    run(
        "Observation (OMR)",
        "SELECT * FROM hosp.omr",
        build_omr_observation,
    )

    # DiagnosticReport + Observation (microbiology) — group by specimen
    print("  DiagnosticReport (microbiology) ...", end=" ", flush=True)
    cur.execute("""
        SELECT * FROM hosp.microbiologyevents
        ORDER BY micro_specimen_id, test_seq
        """)
    rows = cur.fetchall()
    from itertools import groupby

    n_reports = 0
    for _, group in groupby(rows, key=lambda r: r["micro_specimen_id"]):
        for resource in build_diagnostic_report(list(group)):
            writer.write(resource)
        n_reports += 1
    print(f"{n_reports} reports")

    writer.close()
    cur.close()
    conn.close()

    print("\nSummary:")
    for rt, count in sorted(writer.summary().items()):
        print(f"  {rt:<25} {count:>7,} resources")
    print(f"\nFiles written to: {output_dir.resolve()}/")


if __name__ == "__main__":
    convert()
