#!/usr/bin/env python3
"""
Convert MIMIC-IV (PostgreSQL) to FHIR R4 NDJSON.

Mappings
--------
hosp.patients           -> Patient
hosp.admissions         -> Encounter  (hospital)
icu.icustays            -> Encounter  (ICU, partOf hospital encounter)
hosp.diagnoses_icd      -> Condition
hosp.procedures_icd     -> Procedure
hosp.labevents          -> Observation (laboratory)
icu.chartevents         -> Observation (vital-signs / clinical)
icu.datetimeevents      -> Observation (ICU datetime events)
icu.outputevents        -> Observation (ICU output events)
icu.inputevents         -> MedicationAdministration (ICU input events)
icu.ingredientevents    -> MedicationAdministration (ICU ingredient events)
icu.caregiver           -> Practitioner (ICU caregivers)
hosp.prescriptions      -> MedicationRequest
hosp.microbiologyevents -> DiagnosticReport + Observation
hosp.omr                -> Observation (survey / outpatient measurements)
ed.edstays              -> Encounter (ED)
ed.diagnosis            -> Condition (ED)
ed.triage               -> Observation (ED triage vitals + chief complaint + acuity)
ed.vitalsign            -> Observation (ED vital-signs)
ed.medrecon             -> MedicationStatement (ED medication reconciliation)
ed.pyxis                -> MedicationDispense (ED pyxis dispenses)
note.discharge          -> DocumentReference (discharge summaries)
note.radiology          -> DocumentReference (radiology notes)

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
_RANGE_RE = re.compile(r"^(\d*\.?\d+)\s*-\s*(\d*\.?\d+)$")

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


def _numeric_value(value: Any) -> int | float | None:
    if isinstance(value, (int, float)):
        return value
    if isinstance(value, str):
        stripped = value.strip()
        if not stripped:
            return None
        # MIMIC dose strings like "25,000" use comma as a thousands separator;
        # FHIR's `decimal` type forbids it, so HAPI rejects the whole bundle.
        cleaned = stripped.replace(",", "")
        try:
            number = float(cleaned)
        except ValueError:
            return None
        return int(number) if number.is_integer() else number
    return None


def _quantity(value: Any, unit: str | None = None, system: str | None = None) -> dict:
    quantity: dict[str, Any] = {}
    numeric = _numeric_value(value)
    if numeric is not None:
        quantity["value"] = numeric
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


_SERVICE_DISPLAY: dict[str, str] = {
    "CMED":  "Cardiac Medicine",
    "CSURG": "Cardiac Surgery",
    "DENT":  "Dentistry",
    "ENT":   "Ear, Nose & Throat",
    "EYE":   "Ophthalmology",
    "GU":    "Genitourinary",
    "GYN":   "Gynecology",
    "MED":   "Medicine",
    "NB":    "Newborn",
    "NBB":   "Newborn",
    "NMED":  "Neurology Medicine",
    "NSURG": "Neurosurgery",
    "OBS":   "Obstetrics",
    "OMED":  "Oncology Medicine",
    "ORTHO": "Orthopedics",
    "PSURG": "Plastic Surgery",
    "PSYCH": "Psychiatry",
    "SURG":  "Surgery",
    "TRAUM": "Trauma",
    "TSURG": "Thoracic Surgery",
    "VSURG": "Vascular Surgery",
}


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


def build_encounter_hosp(
    row: dict,
    service_code: str | None = None,
    transfer_rows: list[dict] | None = None,
) -> dict:
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
    if service_code:
        r["serviceType"] = {
            "coding": [
                _coding(
                    "http://mimic.mit.edu/fhir/CodeSystem/services",
                    service_code,
                    _SERVICE_DISPLAY.get(service_code, service_code),
                )
            ],
            "text": _SERVICE_DISPLAY.get(service_code, service_code),
        }

    if transfer_rows:
        r["location"] = [
            {
                "location": {"display": t["careunit"]},
                "status": "completed",
                "period": {
                    "start": _dt(t["intime"]),
                    **({"end": _dt(t["outtime"])} if t.get("outtime") else {}),
                },
            }
            for t in transfer_rows
            if t.get("careunit")
        ]

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


_ED_VITAL_LOINC: dict[str, tuple[str, str, str]] = {
    "temperature": ("8310-5",  "Temperature",              "Cel"),
    "heartrate":   ("8867-4",  "Heart Rate",               "/min"),
    "resprate":    ("9279-1",  "Respiratory Rate",         "/min"),
    "o2sat":       ("2708-6",  "Oxygen Saturation",        "%"),
    "sbp":         ("8480-6",  "Systolic Blood Pressure",  "mm[Hg]"),
    "dbp":         ("8462-4",  "Diastolic Blood Pressure", "mm[Hg]"),
}

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


def build_icu_caregiver(row: dict) -> dict:
    """Build a Practitioner resource from an ICU caregiver row."""
    return {
        "resourceType": "Practitioner",
        "id": _uuid("caregiver", row["caregiver_id"]),
        "identifier": [
            {
                "system": "http://mimic.mit.edu/fhir/caregiver",
                "value": str(row["caregiver_id"]),
            }
        ],
        "active": True,
    }


def build_datetime_observation(row: dict) -> dict:
    """Build an Observation for an ICU datetime event."""
    uid = _uuid("datetime-event", row["stay_id"], row["itemid"], str(row.get("charttime") or ""))
    obs: dict = {
        "resourceType": "Observation",
        "id": uid,
        "status": "final",
        "category": [
            {
                "coding": [
                    _coding(
                        "http://terminology.hl7.org/CodeSystem/observation-category",
                        "procedure",
                    )
                ]
            }
        ],
        "code": {
            "coding": [
                _coding(
                    "http://mimic.mit.edu/fhir/CodeSystem/d-items",
                    str(row["itemid"]),
                )
            ]
        },
        "subject": _ref("Patient", _uuid("patient", row["subject_id"])),
        "encounter": _ref("Encounter", _uuid("encounter-icu", row["stay_id"])),
    }
    if row.get("charttime"):
        obs["effectiveDateTime"] = _dt(row["charttime"])
    val = row.get("value")
    if val is not None:
        v_str = str(val)
        try:
            datetime.fromisoformat(v_str)
            obs["valueDateTime"] = _dt(val)
        except (ValueError, TypeError):
            obs["valueString"] = v_str
    return obs


def build_output_observation(row: dict) -> dict:
    """Build an Observation for an ICU output event."""
    uid = _uuid("output-event", row["stay_id"], row["itemid"], str(row.get("charttime") or ""))
    obs: dict = {
        "resourceType": "Observation",
        "id": uid,
        "status": "final",
        "category": [
            {
                "coding": [
                    _coding(
                        "http://terminology.hl7.org/CodeSystem/observation-category",
                        "procedure",
                    )
                ]
            }
        ],
        "code": {
            "coding": [
                _coding(
                    "http://mimic.mit.edu/fhir/CodeSystem/d-items",
                    str(row["itemid"]),
                )
            ]
        },
        "subject": _ref("Patient", _uuid("patient", row["subject_id"])),
        "encounter": _ref("Encounter", _uuid("encounter-icu", row["stay_id"])),
    }
    if row.get("charttime"):
        obs["effectiveDateTime"] = _dt(row["charttime"])
    if row.get("value") is not None:
        obs["valueQuantity"] = _quantity(
            float(row["value"]),
            row.get("valueuom") or None,
            "http://unitsofmeasure.org",
        )
    return obs


def build_input_event(row: dict) -> dict:
    """Build a MedicationAdministration for an ICU input event."""
    uid = _uuid("input-event", row["stay_id"], row["orderid"])
    status = "stopped" if row.get("statusdescription") == "Stopped" else "completed"
    category_name = row.get("ordercategoryname")
    r: dict = {
        "resourceType": "MedicationAdministration",
        "id": uid,
        "status": status,
        "medicationCodeableConcept": {
            "coding": [
                _coding(
                    "http://mimic.mit.edu/fhir/CodeSystem/d-items",
                    str(row["itemid"]),
                    category_name,
                )
            ],
            "text": category_name or str(row["itemid"]),
        },
        "subject": _ref("Patient", _uuid("patient", row["subject_id"])),
        "context": _ref("Encounter", _uuid("encounter-icu", row["stay_id"])),
    }
    if row.get("starttime") and row.get("endtime"):
        r["effectivePeriod"] = {
            "start": _dt(row["starttime"]),
            "end": _dt(row["endtime"]),
        }
    elif row.get("starttime"):
        r["effectiveDateTime"] = _dt(row["starttime"])
    if row.get("amount") is not None:
        r["dosage"] = {
            "dose": _quantity(
                float(row["amount"]),
                row.get("amountuom") or None,
                "http://unitsofmeasure.org",
            )
        }
    return r


def build_ingredient_event(row: dict) -> dict:
    """Build a MedicationAdministration for an ICU ingredient event."""
    uid = _uuid("ingredient-event", row["stay_id"], row["orderid"], row["itemid"])
    status = "stopped" if row.get("statusdescription") == "Stopped" else "completed"
    r: dict = {
        "resourceType": "MedicationAdministration",
        "id": uid,
        "status": status,
        "medicationCodeableConcept": {
            "coding": [
                _coding(
                    "http://mimic.mit.edu/fhir/CodeSystem/d-items",
                    str(row["itemid"]),
                )
            ]
        },
        "subject": _ref("Patient", _uuid("patient", row["subject_id"])),
        "context": _ref("Encounter", _uuid("encounter-icu", row["stay_id"])),
    }
    if row.get("starttime") and row.get("endtime"):
        r["effectivePeriod"] = {
            "start": _dt(row["starttime"]),
            "end": _dt(row["endtime"]),
        }
    elif row.get("starttime"):
        r["effectiveDateTime"] = _dt(row["starttime"])
    if row.get("amount") is not None:
        r["dosage"] = {
            "dose": _quantity(
                float(row["amount"]),
                row.get("amountuom") or None,
                "http://unitsofmeasure.org",
            )
        }
    return r


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


# ── ED / note builders ────────────────────────────────────────────────────────

def build_encounter_ed(row: dict) -> dict:
    r: dict = {
        "resourceType": "Encounter",
        "id": _uuid("encounter-ed", row["stay_id"]),
        "status": "finished",
        "class": _coding(
            "http://terminology.hl7.org/CodeSystem/v3-ActCode", "EMER", "emergency"
        ),
        "subject": _ref("Patient", _uuid("patient", row["subject_id"])),
        "period": {
            "start": _dt(row["intime"]),
            **({"end": _dt(row["outtime"])} if row.get("outtime") else {}),
        },
    }
    if row.get("hadm_id") is not None:
        r["partOf"] = _ref("Encounter", _uuid("encounter-hosp", row["hadm_id"]))
    hosp: dict = {}
    if row.get("arrival_transport"):
        hosp["admitSource"] = {"text": row["arrival_transport"]}
    if row.get("disposition"):
        hosp["dischargeDisposition"] = {"text": row["disposition"]}
    if hosp:
        r["hospitalization"] = hosp
    return r


def build_ed_condition(row: dict) -> dict:
    return {
        "resourceType": "Condition",
        "id": _uuid("ed-condition", row["stay_id"], row["seq_num"]),
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
        "code": {
            "coding": [
                _coding(
                    _icd_system(row["icd_version"]),
                    row["icd_code"],
                    row.get("icd_title"),
                )
            ],
            "text": row.get("icd_title") or row["icd_code"],
        },
        "subject": _ref("Patient", _uuid("patient", row["subject_id"])),
        "encounter": _ref("Encounter", _uuid("encounter-ed", row["stay_id"])),
    }


def build_triage_observations(row: dict) -> list[dict]:
    obs_list: list[dict] = []

    def _vital_obs(field_name: str, loinc_code: str, display: str, unit: str, value) -> dict:
        return {
            "resourceType": "Observation",
            "id": _uuid("triage-obs", row["stay_id"], field_name),
            "status": "final",
            "category": [
                {
                    "coding": [
                        _coding(
                            "http://terminology.hl7.org/CodeSystem/observation-category",
                            "vital-signs",
                        )
                    ]
                }
            ],
            "code": {
                "coding": [_coding("http://loinc.org", loinc_code, display)],
                "text": display,
            },
            "subject": _ref("Patient", _uuid("patient", row["subject_id"])),
            "encounter": _ref("Encounter", _uuid("encounter-ed", row["stay_id"])),
            "valueQuantity": _quantity(float(value), unit, "http://unitsofmeasure.org"),
        }

    for field_name, (loinc_code, display, unit) in _ED_VITAL_LOINC.items():
        value = row.get(field_name)
        if value is not None:
            obs_list.append(_vital_obs(field_name, loinc_code, display, unit, value))

    if row.get("chiefcomplaint") is not None:
        obs_list.append({
            "resourceType": "Observation",
            "id": _uuid("triage-obs", row["stay_id"], "chiefcomplaint"),
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
            "code": {
                "coding": [_coding("http://loinc.org", "10154-3", "Chief complaint")],
                "text": "Chief complaint",
            },
            "subject": _ref("Patient", _uuid("patient", row["subject_id"])),
            "encounter": _ref("Encounter", _uuid("encounter-ed", row["stay_id"])),
            "valueString": str(row["chiefcomplaint"]),
        })

    if row.get("acuity") is not None:
        obs_list.append({
            "resourceType": "Observation",
            "id": _uuid("triage-obs", row["stay_id"], "acuity"),
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
            "code": {"text": "ED Triage Acuity Level"},
            "subject": _ref("Patient", _uuid("patient", row["subject_id"])),
            "encounter": _ref("Encounter", _uuid("encounter-ed", row["stay_id"])),
            "valueQuantity": {"value": _numeric_value(row["acuity"])},
        })

    return obs_list


def build_ed_vitalsign_observations(row: dict) -> list[dict]:
    ts_key = (
        _dt(row["charttime"]).replace(":", "").replace("-", "").replace("T", "")
        if row.get("charttime")
        else "0"
    )
    obs_list: list[dict] = []

    def _vital_obs(field_name: str, loinc_code: str, display: str, unit: str, value) -> dict:
        obs: dict = {
            "resourceType": "Observation",
            "id": _uuid("ed-vital", row["stay_id"], field_name, ts_key),
            "status": "final",
            "category": [
                {
                    "coding": [
                        _coding(
                            "http://terminology.hl7.org/CodeSystem/observation-category",
                            "vital-signs",
                        )
                    ]
                }
            ],
            "code": {
                "coding": [_coding("http://loinc.org", loinc_code, display)],
                "text": display,
            },
            "subject": _ref("Patient", _uuid("patient", row["subject_id"])),
            "encounter": _ref("Encounter", _uuid("encounter-ed", row["stay_id"])),
            "valueQuantity": _quantity(float(value), unit, "http://unitsofmeasure.org"),
        }
        if row.get("charttime"):
            obs["effectiveDateTime"] = _dt(row["charttime"])
        return obs

    for field_name, (loinc_code, display, unit) in _ED_VITAL_LOINC.items():
        value = row.get(field_name)
        if value is not None:
            obs_list.append(_vital_obs(field_name, loinc_code, display, unit, value))

    if row.get("rhythm") is not None:
        rhythm_obs: dict = {
            "resourceType": "Observation",
            "id": _uuid("ed-vital", row["stay_id"], "rhythm", ts_key),
            "status": "final",
            "category": [
                {
                    "coding": [
                        _coding(
                            "http://terminology.hl7.org/CodeSystem/observation-category",
                            "vital-signs",
                        )
                    ]
                }
            ],
            "code": {"text": "Cardiac Rhythm"},
            "subject": _ref("Patient", _uuid("patient", row["subject_id"])),
            "encounter": _ref("Encounter", _uuid("encounter-ed", row["stay_id"])),
            "valueString": str(row["rhythm"]),
        }
        if row.get("charttime"):
            rhythm_obs["effectiveDateTime"] = _dt(row["charttime"])
        obs_list.append(rhythm_obs)

    return obs_list


def build_ed_medrecon(row: dict) -> dict:
    r: dict = {
        "resourceType": "MedicationStatement",
        "id": _uuid(
            "ed-medrecon",
            row["stay_id"],
            row.get("etc_rn") or 0,
            row.get("name") or "",
        ),
        "status": "active",
        "medicationCodeableConcept": {"text": row.get("name") or ""},
        "subject": _ref("Patient", _uuid("patient", row["subject_id"])),
        "context": _ref("Encounter", _uuid("encounter-ed", row["stay_id"])),
    }
    if row.get("ndc"):
        r["medicationCodeableConcept"]["coding"] = [
            _coding("http://hl7.org/fhir/sid/ndc", row["ndc"], row.get("name"))
        ]
    if row.get("charttime"):
        r["dateAsserted"] = _dt(row["charttime"])
    if row.get("etcdescription"):
        r["note"] = [{"text": row["etcdescription"]}]
    return r


def build_ed_pyxis(row: dict) -> dict:
    r: dict = {
        "resourceType": "MedicationDispense",
        "id": _uuid(
            "ed-pyxis",
            row["stay_id"],
            row.get("med_rn") or 0,
            row.get("charttime") or "",
        ),
        "status": "completed",
        "medicationCodeableConcept": {"text": row.get("name") or ""},
        "subject": _ref("Patient", _uuid("patient", row["subject_id"])),
        "context": _ref("Encounter", _uuid("encounter-ed", row["stay_id"])),
    }
    if row.get("gsn"):
        r["medicationCodeableConcept"]["coding"] = [
            _coding(
                "http://mimic.mit.edu/fhir/CodeSystem/gsn",
                str(row["gsn"]),
                row.get("name"),
            )
        ]
    if row.get("charttime"):
        r["whenHandedOver"] = _dt(row["charttime"])
    return r


_NOTE_TYPE_LOINC: dict[str, tuple[str, str]] = {
    "DS":  ("18842-5", "Discharge summary"),
    "AR":  ("18726-0", "Radiology studies (set)"),
    "RR":  ("18726-0", "Radiology studies (set)"),
    "ECG": ("11524-6", "EKG study"),
    "ECH": ("34750-4", "Echocardiography study"),
    "NUR": ("34119-2", "Nursing facility initial assessment note"),
    "PH":  ("47049-6", "Pharmacy note"),
}


def build_document_reference(row: dict) -> dict:
    import base64
    note_type = (row.get("note_type") or "").upper()
    loinc_code, loinc_display = _NOTE_TYPE_LOINC.get(note_type, ("34109-3", "Note"))
    uid = _uuid("docref", row["note_id"])
    text_bytes = (row.get("text") or "").encode("utf-8")
    doc: dict = {
        "resourceType": "DocumentReference",
        "id": uid,
        "status": "current",
        "type": {
            "coding": [_coding("http://loinc.org", loinc_code, loinc_display)],
            "text": loinc_display,
        },
        "category": [
            {
                "coding": [
                    _coding(
                        "http://hl7.org/fhir/us/core/CodeSystem/us-core-documentreference-category",
                        "clinical-note",
                        "Clinical Note",
                    )
                ]
            }
        ],
        "subject": _ref("Patient", _uuid("patient", row["subject_id"])),
        "content": [
            {
                "attachment": {
                    "contentType": "text/plain",
                    "data": base64.b64encode(text_bytes).decode("ascii"),
                }
            }
        ],
    }
    if row.get("charttime"):
        doc["date"] = _dt(row["charttime"])
    if row.get("hadm_id"):
        doc["context"] = {
            "encounter": [_ref("Encounter", _uuid("encounter-hosp", row["hadm_id"]))]
        }
    return doc


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

    def run_multi(label: str, sql: str, builder):
        print(f"  {label} ...", end=" ", flush=True)
        cur.execute(sql)
        n = 0
        while True:
            rows = cur.fetchmany(batch_size)
            if not rows:
                break
            for row in rows:
                for resource in builder(row):
                    writer.write(resource)
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

    # Pre-load services (last curr_service per hadm_id) and transfers for hospital encounters
    print("  Pre-loading services and transfers ...", end=" ", flush=True)
    cur.execute(
        """
        SELECT DISTINCT ON (hadm_id) hadm_id, curr_service
        FROM hosp.services
        WHERE curr_service IS NOT NULL
        ORDER BY hadm_id, transfertime DESC
        """
    )
    service_per_hadm: dict[int, str] = {r["hadm_id"]: r["curr_service"] for r in cur.fetchall()}
    cur.execute(
        """
        SELECT hadm_id, careunit, intime, outtime
        FROM hosp.transfers
        WHERE careunit IS NOT NULL
        ORDER BY hadm_id, intime
        """
    )
    transfers_per_hadm: dict[int, list] = {}
    for t in cur.fetchall():
        transfers_per_hadm.setdefault(t["hadm_id"], []).append(t)
    print(f"{len(service_per_hadm)} service entries, {len(transfers_per_hadm)} transfer groups")

    # Encounter (hospital)
    print("  Encounter (hospital) ...", end=" ", flush=True)
    cur.execute("SELECT * FROM hosp.admissions")
    n = 0
    while True:
        rows = cur.fetchmany(batch_size)
        if not rows:
            break
        for row in rows:
            writer.write(build_encounter_hosp(
                row,
                service_code=service_per_hadm.get(row["hadm_id"]),
                transfer_rows=transfers_per_hadm.get(row["hadm_id"]),
            ))
            n += 1
    print(n)

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

    # Practitioner (ICU caregiver)
    run(
        "Practitioner (ICU caregiver)",
        "SELECT * FROM icu.caregiver",
        build_icu_caregiver,
    )

    # Observation (ICU datetime events)
    run(
        "Observation (ICU datetime)",
        """
        SELECT de.*, d.label
        FROM icu.datetimeevents de
        LEFT JOIN icu.d_items d ON de.itemid = d.itemid
        """,
        build_datetime_observation,
    )

    # Observation (ICU output events)
    run(
        "Observation (ICU output)",
        """
        SELECT oe.*, d.label
        FROM icu.outputevents oe
        LEFT JOIN icu.d_items d ON oe.itemid = d.itemid
        """,
        build_output_observation,
    )

    # MedicationAdministration (ICU input events)
    run(
        "MedicationAdministration (ICU input)",
        """
        SELECT ie.*, d.label
        FROM icu.inputevents ie
        LEFT JOIN icu.d_items d ON ie.itemid = d.itemid
        """,
        build_input_event,
    )

    # MedicationAdministration (ICU ingredient events)
    run(
        "MedicationAdministration (ICU ingredient)",
        """
        SELECT ige.*, d.label
        FROM icu.ingredientevents ige
        LEFT JOIN icu.d_items d ON ige.itemid = d.itemid
        """,
        build_ingredient_event,
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

    # Encounter (ED)
    run("Encounter (ED)", "SELECT * FROM ed.edstays", build_encounter_ed)

    # Condition (ED)
    run("Condition (ED)", "SELECT * FROM ed.diagnosis", build_ed_condition)

    # Observation (ED triage)
    run_multi("Observation (ED triage)", "SELECT * FROM ed.triage", build_triage_observations)

    # Observation (ED vitalsign)
    run_multi(
        "Observation (ED vitalsign)",
        "SELECT * FROM ed.vitalsign ORDER BY stay_id, charttime",
        build_ed_vitalsign_observations,
    )

    # MedicationStatement (ED medrecon)
    run("MedicationStatement (ED medrecon)", "SELECT * FROM ed.medrecon", build_ed_medrecon)

    # MedicationDispense (ED pyxis)
    run("MedicationDispense (ED pyxis)", "SELECT * FROM ed.pyxis", build_ed_pyxis)

    # DocumentReference (discharge notes)
    run("DocumentReference (discharge)", "SELECT * FROM note.discharge", build_document_reference)

    # DocumentReference (radiology notes)
    run("DocumentReference (radiology)", "SELECT * FROM note.radiology", build_document_reference)

    writer.close()
    cur.close()
    conn.close()

    print("\nSummary:")
    for rt, count in sorted(writer.summary().items()):
        print(f"  {rt:<25} {count:>7,} resources")
    print(f"\nFiles written to: {output_dir.resolve()}/")


if __name__ == "__main__":
    convert()
