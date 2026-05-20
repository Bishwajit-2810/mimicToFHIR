#!/usr/bin/env python3
"""
Convert MIMIC-IV (PostgreSQL) to Synthea-compatible FHIR R4 transaction Bundles.

Output: one JSON file per patient in fhir_bundles/<subject_id>.json
Each file is a FHIR Bundle (type=transaction) whose entries mirror the
Synthea output format: urn:uuid: fullUrls, POST request entries, and
all of a patient's resources collected in a single bundle.

Sources
-------
hosp.patients           -> Patient
hosp.admissions         -> Encounter (hospital)
icu.icustays            -> Encounter (ICU, partOf hospital)
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
hosp.omr                -> Observation (survey / outpatient measurements)
hosp.microbiologyevents -> DiagnosticReport + Observation
ed.edstays              -> Encounter (ED)
ed.triage               -> Observation (ED triage vitals + chief complaint + acuity)
ed.vitalsign            -> Observation (ED vital-signs)
ed.diagnosis            -> Condition (ED)
ed.medrecon             -> MedicationStatement (ED medication reconciliation)
ed.pyxis                -> MedicationDispense (ED pyxis dispenses)
note.discharge          -> DocumentReference (discharge summaries, with detail)
note.radiology          -> DocumentReference (radiology notes, with detail)
"""

import json
import math
import os
import re
import uuid
from collections import defaultdict
from datetime import date, datetime
from itertools import groupby
from pathlib import Path
from typing import Any

import psycopg2
import psycopg2.extras

DSN = os.getenv(
    "MIMIC_DSN",
    "host=localhost port=5433 dbname=mimiciv user=mimic password=mimic",
)
OUTPUT_DIR = Path("fhir_bundles")

# Deterministic UUID namespace (DNS namespace reused as a stable seed)
_NS = uuid.UUID("6ba7b810-9dad-11d1-80b4-00c04fd430c8")

BIDMC_UUID = str(uuid.uuid5(_NS, "mimic-iv::org::BIDMC"))
BIDMC_NAME = "Beth Israel Deaconess Medical Center"

_RANGE_RE = re.compile(r"^(\d*\.?\d+)\s*-\s*(\d*\.?\d+)$")


# ── helpers ───────────────────────────────────────────────────────────────────


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


def _urn(uid: str) -> str:
    return f"urn:uuid:{uid}"


def _ref(uid: str, display: str | None = None) -> dict:
    r: dict = {"reference": _urn(uid)}
    if display:
        r["display"] = display
    return r


def _coding(system: str, code: str, display: str | None = None) -> dict:
    c: dict = {"system": system, "code": str(code)}
    if display:
        c["display"] = display
    return c


def _dt(v) -> str | None:
    if v is None:
        return None
    if isinstance(v, datetime):
        return v.isoformat()
    if isinstance(v, date):
        return v.isoformat()
    return str(v)


def _icd_system(version: int) -> str:
    return (
        "http://hl7.org/fhir/sid/icd-10-cm"
        if version == 10
        else "http://hl7.org/fhir/sid/icd-9-cm"
    )


def _entry(resource: dict) -> dict:
    uid = resource["id"]
    return {
        "fullUrl": _urn(uid),
        "resource": resource,
        "request": {"method": "POST", "url": resource["resourceType"]},
    }


def _sanitize_for_json(obj):
    """Recursively replace NaN/Inf floats with None for valid JSON output."""
    if isinstance(obj, float):
        return None if (math.isnan(obj) or math.isinf(obj)) else obj
    if isinstance(obj, dict):
        return {k: _sanitize_for_json(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [_sanitize_for_json(v) for v in obj]
    return obj


# ── OMB race / ethnicity mapping ──────────────────────────────────────────────

_RACE_OMB: dict[str, tuple[str, str]] = {
    "WHITE": ("2106-3", "White"),
    "BLACK/AFRICAN AMERICAN": ("2054-5", "Black or African American"),
    "BLACK/CAPE VERDEAN": ("2054-5", "Black or African American"),
    "BLACK/HAITIAN": ("2054-5", "Black or African American"),
    "BLACK/AFRICAN": ("2054-5", "Black or African American"),
    "ASIAN": ("2028-9", "Asian"),
    "ASIAN - CHINESE": ("2028-9", "Asian"),
    "ASIAN - KOREAN": ("2028-9", "Asian"),
    "ASIAN - SOUTH EAST ASIAN": ("2028-9", "Asian"),
    "ASIAN - INDIAN": ("2028-9", "Asian"),
    "ASIAN - ASIAN INDIAN": ("2028-9", "Asian"),
    "ASIAN - JAPANESE": ("2028-9", "Asian"),
    "ASIAN - CAMBODIAN": ("2028-9", "Asian"),
    "ASIAN - FILIPINO": ("2028-9", "Asian"),
    "ASIAN - VIETNAMESE": ("2028-9", "Asian"),
    "NATIVE HAWAIIAN OR OTHER PACIFIC ISLANDER": (
        "2076-8",
        "Native Hawaiian or Other Pacific Islander",
    ),
    "AMERICAN INDIAN/ALASKA NATIVE": ("1002-5", "American Indian or Alaska Native"),
    "MULTIPLE RACE/ETHNICITY": ("2131-1", "Other Race"),
    "OTHER": ("2131-1", "Other Race"),
    "UNKNOWN": ("2131-1", "Other Race"),
    "UNABLE TO OBTAIN": ("2131-1", "Other Race"),
    "PATIENT DECLINED TO ANSWER": ("2131-1", "Other Race"),
}

_LANG_MAP: dict[str, tuple[str, str]] = {
    "ENGLISH": ("en-US", "English"),
    "SPANISH": ("es", "Spanish"),
    "PORTUGUESE": ("pt", "Portuguese"),
    "CHINESE": ("zh", "Chinese"),
    "RUSSIAN": ("ru", "Russian"),
    "ARABIC": ("ar", "Arabic"),
    "VIETNAMESE": ("vi", "Vietnamese"),
    "FRENCH": ("fr", "French"),
    "HAITIAN CREOLE": ("ht", "Haitian Creole"),
    "ITALIAN": ("it", "Italian"),
    "GREEK": ("el", "Greek"),
    "POLISH": ("pl", "Polish"),
    "JAPANESE": ("ja", "Japanese"),
    "CAMBODIAN": ("km", "Cambodian"),
    "KOREAN": ("ko", "Korean"),
}

_MARITAL_MAP: dict[str, tuple[str, str]] = {
    "SINGLE": ("S", "Never Married"),
    "MARRIED": ("M", "Married"),
    "DIVORCED": ("D", "Divorced"),
    "WIDOWED": ("W", "Widowed"),
    "SEPARATED": ("L", "Legally Separated"),
}

_ADMISSION_CLASS: dict[str, tuple[str, str]] = {
    "EMERGENCY":                   ("EMER", "emergency"),
    "EU OBSERVATION":              ("EMER", "emergency"),
    "DIRECT EMER.":                ("EMER", "emergency"),
    "OBSERVATION ADMIT":           ("AMB",  "ambulatory"),
    "AMBULATORY OBSERVATION":      ("AMB",  "ambulatory"),
    "DIRECT OBSERVATION":          ("AMB",  "ambulatory"),
    "SURGICAL SAME DAY ADMISSION": ("AMB",  "ambulatory"),
    "ELECTIVE":                    ("IMP",  "inpatient encounter"),
    "URGENT":                      ("IMP",  "inpatient encounter"),
}

_ENCOUNTER_SNOMED: dict[str, tuple[str, str]] = {
    "EMER": ("50849002", "Emergency room admission"),
    "AMB":  ("11429006", "Consultation"),
    "IMP":  ("32485007", "Hospital admission"),
}

_SERVICE_PLACE: dict[str, tuple[str, str]] = {
    "EMER": ("23", "Emergency Room – Hospital"),
    "AMB":  ("22", "On Campus-Outpatient Hospital"),
    "IMP":  ("21", "Inpatient Hospital"),
}


# ── resource builders ─────────────────────────────────────────────────────────


def build_organization() -> dict:
    return {
        "resourceType": "Organization",
        "id": BIDMC_UUID,
        "identifier": [{"system": "https://www.bidmc.org", "value": BIDMC_UUID}],
        "active": True,
        "type": [
            {
                "coding": [
                    _coding(
                        "http://terminology.hl7.org/CodeSystem/organization-type",
                        "prov",
                        "Healthcare Provider",
                    )
                ],
                "text": "Healthcare Provider",
            }
        ],
        "name": BIDMC_NAME,
        "address": [
            {
                "line": ["330 Brookline Avenue"],
                "city": "Boston",
                "state": "MA",
                "postalCode": "02215",
                "country": "US",
            }
        ],
    }


def build_practitioner(provider_id: str) -> dict:
    uid = _uuid("practitioner", provider_id)
    return {
        "resourceType": "Practitioner",
        "id": uid,
        "identifier": [
            {
                "system": "http://mimic.mit.edu/fhir/provider",
                "value": provider_id,
            }
        ],
        "active": True,
        "name": [{"family": f"Provider-{provider_id}", "given": ["MIMIC"]}],
    }


def build_patient(row: dict, admission: dict | None) -> dict:
    uid = _uuid("patient", row["subject_id"])
    birth_year = int(row["anchor_year"]) - int(row["anchor_age"])
    gender_code = "F" if row["gender"] == "F" else "M"
    gender_display = "female" if row["gender"] == "F" else "male"

    extensions: list[dict] = []

    # us-core-race
    race_raw = (admission or {}).get("race", "") or ""
    race_key = race_raw.upper().split("/")[0].strip() if race_raw else ""
    omb_race = _RACE_OMB.get(race_raw.upper()) or _RACE_OMB.get(race_key)
    race_text = race_raw or "Unknown"
    race_ext: dict = {
        "url": "http://hl7.org/fhir/us/core/StructureDefinition/us-core-race",
        "extension": [],
    }
    if omb_race:
        race_ext["extension"].append(
            {
                "url": "ombCategory",
                "valueCoding": _coding(
                    "urn:oid:2.16.840.1.113883.6.238", omb_race[0], omb_race[1]
                ),
            }
        )
    race_ext["extension"].append({"url": "text", "valueString": race_text})
    extensions.append(race_ext)

    # us-core-ethnicity
    is_hispanic = "HISPANIC" in race_raw.upper() or "LATINO" in race_raw.upper()
    eth_code = "2135-2" if is_hispanic else "2186-5"
    eth_display = "Hispanic or Latino" if is_hispanic else "Not Hispanic or Latino"
    extensions.append(
        {
            "url": "http://hl7.org/fhir/us/core/StructureDefinition/us-core-ethnicity",
            "extension": [
                {
                    "url": "ombCategory",
                    "valueCoding": _coding(
                        "urn:oid:2.16.840.1.113883.6.238", eth_code, eth_display
                    ),
                },
                {"url": "text", "valueString": eth_display},
            ],
        }
    )

    # birthsex
    extensions.append(
        {
            "url": "http://hl7.org/fhir/us/core/StructureDefinition/us-core-birthsex",
            "valueCode": gender_code,
        }
    )

    # anchor-year-group (MIMIC-specific)
    extensions.append(
        {
            "url": "http://mimic.mit.edu/fhir/StructureDefinition/anchor-year-group",
            "valueString": row["anchor_year_group"],
        }
    )

    patient: dict = {
        "resourceType": "Patient",
        "id": uid,
        "text": {
            "status": "generated",
            "div": (
                f'<div xmlns="http://www.w3.org/1999/xhtml">'
                f"MIMIC-IV Patient {row['subject_id']}"
                f"</div>"
            ),
        },
        "extension": extensions,
        "identifier": [
            {
                "type": {
                    "coding": [
                        _coding(
                            "http://terminology.hl7.org/CodeSystem/v2-0203",
                            "MR",
                            "Medical Record Number",
                        )
                    ],
                    "text": "Medical Record Number",
                },
                "system": "http://mimic.mit.edu/fhir/patient",
                "value": str(row["subject_id"]),
            }
        ],
        "name": [
            {
                "use": "official",
                "family": f"Patient-{row['subject_id']}",
                "given": [f"MIMIC-{row['subject_id']}"],
            }
        ],
        "gender": gender_display,
        "birthDate": f"{birth_year}-07-01",
        "multipleBirthBoolean": False,
    }

    if row.get("dod"):
        patient["deceasedDateTime"] = _dt(row["dod"])

    # marital status
    if admission and admission.get("marital_status"):
        ms = (admission["marital_status"] or "").upper()
        ms_code = _MARITAL_MAP.get(ms, ("UNK", ms))
        patient["maritalStatus"] = {
            "coding": [
                _coding(
                    "http://terminology.hl7.org/CodeSystem/v3-MaritalStatus",
                    ms_code[0],
                    ms_code[1],
                )
            ],
            "text": ms_code[1],
        }

    # language
    if admission and admission.get("language"):
        lang = (admission["language"] or "").upper()
        lang_code = _LANG_MAP.get(lang, ("und", lang.title()))
        patient["communication"] = [
            {
                "language": {
                    "coding": [_coding("urn:ietf:bcp:47", lang_code[0], lang_code[1])],
                    "text": lang_code[1],
                }
            }
        ]

    return patient


def build_encounter_hosp(
    row: dict, patient_uid: str, org_uid: str, provider_uid: str | None
) -> dict:
    uid = _uuid("encounter-hosp", row["hadm_id"])
    adm_type_key = (row.get("admission_type") or "").upper()
    cls_code, cls_display = _ADMISSION_CLASS.get(adm_type_key, ("IMP", "inpatient encounter"))
    snomed_code, snomed_display = _ENCOUNTER_SNOMED[cls_code]
    subject_id = row.get("subject_id", "")
    r: dict = {
        "resourceType": "Encounter",
        "id": uid,
        "status": "finished",
        "class": _coding(
            "http://terminology.hl7.org/CodeSystem/v3-ActCode",
            cls_code,
            cls_display,
        ),
        "type": [
            {
                "coding": [_coding("http://snomed.info/sct", snomed_code, snomed_display)],
                "text": snomed_display,
            }
        ],
        "subject": _ref(patient_uid, f"Patient-{subject_id}"),
        "serviceProvider": _ref(org_uid, BIDMC_NAME),
        "period": {"start": _dt(row["admittime"])},
    }
    if row.get("dischtime"):
        r["period"]["end"] = _dt(row["dischtime"])
    if provider_uid:
        r["participant"] = [{"individual": _ref(provider_uid)}]

    hosp: dict = {}
    if row.get("admission_location"):
        hosp["admitSource"] = {"text": row["admission_location"]}
    if row.get("hospital_expire_flag"):
        hosp["dischargeDisposition"] = {
            "coding": [
                _coding(
                    "http://terminology.hl7.org/CodeSystem/discharge-disposition",
                    "exp",
                    "Expired",
                )
            ]
        }
    elif row.get("discharge_location"):
        hosp["dischargeDisposition"] = {"text": row["discharge_location"]}
    if hosp:
        r["hospitalization"] = hosp

    if row.get("insurance"):
        r["extension"] = [
            {
                "url": "http://mimic.mit.edu/fhir/StructureDefinition/insurance",
                "valueString": row["insurance"],
            }
        ]
    return r


def build_encounter_icu(row: dict, patient_uid: str, hosp_uid: str) -> dict:
    uid = _uuid("encounter-icu", row["stay_id"])
    return {
        "resourceType": "Encounter",
        "id": uid,
        "status": "finished",
        "class": _coding(
            "http://terminology.hl7.org/CodeSystem/v3-ActCode", "ACUTE", "ICU"
        ),
        "subject": _ref(patient_uid),
        "partOf": _ref(hosp_uid),
        "period": {
            "start": _dt(row["intime"]),
            **({"end": _dt(row["outtime"])} if row.get("outtime") else {}),
        },
        "location": [
            {"location": {"display": row["first_careunit"]}, "status": "completed"}
        ],
        **({"extension": [{"url": "http://mimic.mit.edu/fhir/StructureDefinition/los",
                            "valueDecimal": round(float(row["los"]), 4)}]}
           if row.get("los") else {}),
    }


def build_condition(row: dict, patient_uid: str, enc_uid: str) -> dict:
    uid = _uuid("condition", row["hadm_id"], row["seq_num"])
    return {
        "resourceType": "Condition",
        "id": uid,
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
                    row.get("long_title"),
                )
            ],
            "text": row.get("long_title") or row["icd_code"],
        },
        "subject": _ref(patient_uid),
        "encounter": _ref(enc_uid),
        **(
            {"onsetDateTime": _dt(row.get("admittime"))} if row.get("admittime") else {}
        ),
        **({"recordedDate": _dt(row.get("admittime"))} if row.get("admittime") else {}),
    }


def build_procedure(row: dict, patient_uid: str, enc_uid: str) -> dict:
    uid = _uuid("procedure", row["hadm_id"], row["seq_num"])
    return {
        "resourceType": "Procedure",
        "id": uid,
        "status": "completed",
        "code": {
            "coding": [
                _coding(
                    _icd_system(row["icd_version"]),
                    row["icd_code"],
                    row.get("long_title"),
                )
            ],
            "text": row.get("long_title") or row["icd_code"],
        },
        "subject": _ref(patient_uid),
        "encounter": _ref(enc_uid),
        **(
            {"performedDateTime": _dt(row["chartdate"])} if row.get("chartdate") else {}
        ),
    }


_CHART_LOINC: dict[int, str] = {
    220045: "8867-4",
    220050: "8480-6",
    220051: "8462-4",
    220052: "8478-0",
    220210: "9279-1",
    223761: "8310-5",
    223762: "8310-5",
    220277: "2708-6",
    226253: "29463-7",
}

_ED_VITAL_LOINC: dict[str, tuple[str, str, str]] = {
    "temperature": ("8310-5",  "Temperature",              "Cel"),
    "heartrate":   ("8867-4",  "Heart Rate",               "/min"),
    "resprate":    ("9279-1",  "Respiratory Rate",         "/min"),
    "o2sat":       ("2708-6",  "Oxygen Saturation",        "%"),
    "sbp":         ("8480-6",  "Systolic Blood Pressure",  "mm[Hg]"),
    "dbp":         ("8462-4",  "Diastolic Blood Pressure", "mm[Hg]"),
}


def build_lab_observation(row: dict, patient_uid: str, enc_uid: str | None) -> dict:
    uid = _uuid("lab", row["labevent_id"])
    lab_coding = []
    if row.get("loinc_code"):
        lab_coding.append(_coding("http://loinc.org", row["loinc_code"], row.get("label")))
    lab_coding.append(
        _coding("http://mimic.mit.edu/fhir/CodeSystem/d-labitems", str(row["itemid"]), row.get("label"))
    )
    obs: dict = {
        "resourceType": "Observation",
        "id": uid,
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
            "coding": lab_coding,
            "text": row.get("label") or str(row["itemid"]),
        },
        "subject": _ref(patient_uid),
        **({"encounter": _ref(enc_uid)} if enc_uid else {}),
        **(
            {"effectiveDateTime": _dt(row["charttime"])} if row.get("charttime") else {}
        ),
    }
    if row.get("valuenum") is not None:
        obs["valueQuantity"] = {
            **_quantity(
                float(row["valuenum"]),
                row.get("valueuom") or None,
                "http://unitsofmeasure.org",
            ),
        }
    elif row.get("value"):
        obs["valueString"] = str(row["value"])
    if row.get("flag"):
        obs["interpretation"] = [
            {
                "coding": [
                    _coding(
                        "http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation",
                        "A",
                        row["flag"],
                    )
                ]
            }
        ]
    if row.get("ref_range_lower") is not None or row.get("ref_range_upper") is not None:
        rr: dict = {}
        if row.get("ref_range_lower") is not None:
            rr["low"] = _quantity(
                float(row["ref_range_lower"]),
                row.get("valueuom") or None,
                "http://unitsofmeasure.org",
            )
        if row.get("ref_range_upper") is not None:
            rr["high"] = _quantity(
                float(row["ref_range_upper"]),
                row.get("valueuom") or None,
                "http://unitsofmeasure.org",
            )
        obs["referenceRange"] = [rr]
    return obs


def build_chart_observation(row: dict, patient_uid: str, enc_uid: str) -> dict:
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
    ts = (
        _dt(row["charttime"]).replace(":", "").replace("-", "").replace("T", "")
        if row.get("charttime")
        else "0"
    )
    uid = _uuid("chart", row["stay_id"], row["itemid"], ts)
    obs: dict = {
        "resourceType": "Observation",
        "id": uid,
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
        "code": {"coding": coding, "text": row.get("label") or str(row["itemid"])},
        "subject": _ref(patient_uid),
        "encounter": _ref(enc_uid),
        **(
            {"effectiveDateTime": _dt(row["charttime"])} if row.get("charttime") else {}
        ),
    }
    if row.get("valuenum") is not None:
        obs["valueQuantity"] = _quantity(
            float(row["valuenum"]),
            row.get("valueuom") or None,
            "http://unitsofmeasure.org",
        )
    elif row.get("value"):
        obs["valueString"] = str(row["value"])
    return obs


def build_icu_caregiver(row: dict) -> dict:
    """Build a Practitioner resource from an ICU caregiver row."""
    uid = _uuid("caregiver", row["caregiver_id"])
    return {
        "resourceType": "Practitioner",
        "id": uid,
        "identifier": [
            {
                "system": "http://mimic.mit.edu/fhir/caregiver",
                "value": str(row["caregiver_id"]),
            }
        ],
        "active": True,
    }


def build_datetime_observation(row: dict, patient_uid: str, enc_uid: str) -> dict:
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
        "subject": _ref(patient_uid),
        "encounter": _ref(enc_uid),
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


def build_output_observation(row: dict, patient_uid: str, enc_uid: str) -> dict:
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
        "subject": _ref(patient_uid),
        "encounter": _ref(enc_uid),
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


def build_input_event(row: dict, patient_uid: str, enc_uid: str) -> dict:
    """Build a MedicationAdministration for an ICU input event."""
    uid = _uuid("input-event", row["stay_id"], row["orderid"], row["itemid"])
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
        "subject": _ref(patient_uid),
        "context": _ref(enc_uid),
    }
    if row.get("starttime") and row.get("endtime"):
        r["effectivePeriod"] = {
            "start": _dt(row["starttime"]),
            "end": _dt(row["endtime"]),
        }
    elif row.get("starttime"):
        r["effectiveDateTime"] = _dt(row["starttime"])
    elif row.get("endtime"):
        r["effectiveDateTime"] = _dt(row["endtime"])
    if row.get("amount") is not None:
        r["dosage"] = {
            "dose": _quantity(
                float(row["amount"]),
                row.get("amountuom") or None,
                "http://unitsofmeasure.org",
            )
        }
    return r


def build_ingredient_event(row: dict, patient_uid: str, enc_uid: str) -> dict:
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
        "subject": _ref(patient_uid),
        "context": _ref(enc_uid),
    }
    if row.get("starttime") and row.get("endtime"):
        r["effectivePeriod"] = {
            "start": _dt(row["starttime"]),
            "end": _dt(row["endtime"]),
        }
    elif row.get("starttime"):
        r["effectiveDateTime"] = _dt(row["starttime"])
    elif row.get("endtime"):
        r["effectiveDateTime"] = _dt(row["endtime"])
    if row.get("amount") is not None:
        r["dosage"] = {
            "dose": _quantity(
                float(row["amount"]),
                row.get("amountuom") or None,
                "http://unitsofmeasure.org",
            )
        }
    return r


def build_medication_request(row: dict, patient_uid: str, enc_uid: str) -> dict:
    uid = _uuid(
        "rx",
        row["subject_id"],
        row["hadm_id"],
        row.get("pharmacy_id") or row.get("poe_id") or row.get("starttime"),
        row.get("drug") or "",
    )
    r: dict = {
        "resourceType": "MedicationRequest",
        "id": uid,
        "status": "completed",
        "intent": "order",
        "medicationCodeableConcept": {"text": row["drug"]},
        "subject": _ref(patient_uid),
        "encounter": _ref(enc_uid),
    }
    if row.get("ndc"):
        r["medicationCodeableConcept"]["coding"] = [
            _coding("http://hl7.org/fhir/sid/ndc", row["ndc"], row["drug"])
        ]
    dosage: dict = {}
    dose_and_rate = _dose_and_rate(row.get("dose_val_rx"), row.get("dose_unit_rx"))
    if dose_and_rate:
        dosage["doseAndRate"] = [dose_and_rate]
    if row.get("route"):
        dosage["route"] = {"text": row["route"]}
    if dosage:
        r["dosageInstruction"] = [dosage]
    timing: dict = {}
    if row.get("starttime"):
        timing["start"] = _dt(row["starttime"])
    if row.get("stoptime"):
        timing["end"] = _dt(row["stoptime"])
    if timing:
        r["dispenseRequest"] = {"validityPeriod": timing}
    return r


def build_diagnostic_report(
    rows: list[dict], patient_uid: str, enc_uid: str | None
) -> list[dict]:
    first = rows[0]
    report_uid = _uuid("micro-report", first["micro_specimen_id"])
    obs_resources = []
    obs_refs = []
    for i, row in enumerate(rows):
        obs_uid = _uuid("micro-obs", row["micro_specimen_id"], i)
        obs: dict = {
            "resourceType": "Observation",
            "id": obs_uid,
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
                "text": row.get("test_name") or row.get("spec_type_desc"),
                "coding": [
                    _coding(
                        "http://mimic.mit.edu/fhir/CodeSystem/micro-test",
                        str(row.get("test_itemid") or row.get("spec_itemid")),
                        row.get("test_name"),
                    )
                ],
            },
            "subject": _ref(patient_uid),
            **({"encounter": _ref(enc_uid)} if enc_uid else {}),
            **(
                {"effectiveDateTime": _dt(row.get("charttime") or row.get("chartdate"))}
                if (row.get("charttime") or row.get("chartdate")) else {}
            ),
        }
        if row.get("org_name"):
            obs["valueString"] = row["org_name"]
        if row.get("interpretation"):
            obs["interpretation"] = [{"text": row["interpretation"]}]
        obs_resources.append(obs)
        obs_refs.append(_ref(obs_uid))

    report: dict = {
        "resourceType": "DiagnosticReport",
        "id": report_uid,
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
        "code": {"text": first.get("spec_type_desc")},
        "subject": _ref(patient_uid),
        **({"encounter": _ref(enc_uid)} if enc_uid else {}),
        **({"effectiveDateTime": _dt(first.get("charttime") or first.get("chartdate"))}
           if (first.get("charttime") or first.get("chartdate")) else {}),
        "result": obs_refs,
    }
    return [report] + obs_resources


def build_omr_observation(row: dict, patient_uid: str) -> dict:
    uid = _uuid("omr", row["subject_id"], _dt(row["chartdate"]), row["seq_num"], row.get("result_name") or "")
    return {
        "resourceType": "Observation",
        "id": uid,
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
        "subject": _ref(patient_uid),
        **({"effectiveDateTime": _dt(row["chartdate"])} if row.get("chartdate") else {}),
        "valueString": str(row["result_value"]),
    }


# ── document reference (clinical notes) ──────────────────────────────────────

_NOTE_TYPE_LOINC: dict[str, tuple[str, str]] = {
    "DS":  ("18842-5", "Discharge summary"),
    "AR":  ("18726-0", "Radiology studies (set)"),
    "RR":  ("18726-0", "Radiology studies (set)"),
    "ECG": ("11524-6", "EKG study"),
    "ECH": ("34750-4", "Echocardiography study"),
    "NUR": ("34119-2", "Nursing facility initial assessment note"),
    "PH":  ("47049-6", "Pharmacy note"),
}

def build_document_reference(row: dict, patient_uid: str, enc_uid: str | None, detail_rows=None) -> dict:
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
        "subject": _ref(patient_uid),
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
    if enc_uid:
        doc["context"] = {"encounter": [_ref(enc_uid)]}
    if detail_rows:
        doc.setdefault("extension", []).append({
            "url": "http://mimic.mit.edu/fhir/StructureDefinition/note-detail",
            "extension": [
                {"url": r["field_name"], "valueString": str(r["field_value"])}
                for r in detail_rows
                if r.get("field_value")
            ],
        })
    return doc


# ── ED / note builders ────────────────────────────────────────────────────────


def build_encounter_ed(row: dict, patient_uid: str, hosp_uid: str | None) -> dict:
    uid = _uuid("encounter-ed", row["stay_id"])
    r: dict = {
        "resourceType": "Encounter",
        "id": uid,
        "status": "finished",
        "class": _coding(
            "http://terminology.hl7.org/CodeSystem/v3-ActCode", "EMER", "emergency"
        ),
        "subject": _ref(patient_uid),
        "period": {
            "start": _dt(row["intime"]),
            **({"end": _dt(row["outtime"])} if row.get("outtime") else {}),
        },
    }
    if hosp_uid is not None:
        r["partOf"] = _ref(hosp_uid)
    hosp: dict = {}
    if row.get("arrival_transport"):
        hosp["admitSource"] = {"text": row["arrival_transport"]}
    if row.get("disposition"):
        hosp["dischargeDisposition"] = {"text": row["disposition"]}
    if hosp:
        r["hospitalization"] = hosp
    return r


def build_triage_observations(row: dict, patient_uid: str, enc_uid: str) -> list[dict]:
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
            "subject": _ref(patient_uid),
            "encounter": _ref(enc_uid),
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
            "subject": _ref(patient_uid),
            "encounter": _ref(enc_uid),
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
            "subject": _ref(patient_uid),
            "encounter": _ref(enc_uid),
            "valueQuantity": {"value": _numeric_value(row["acuity"])},
        })

    return obs_list


def build_ed_vitalsign_observations(row: dict, patient_uid: str, enc_uid: str) -> list[dict]:
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
            "subject": _ref(patient_uid),
            "encounter": _ref(enc_uid),
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
            "subject": _ref(patient_uid),
            "encounter": _ref(enc_uid),
            "valueString": str(row["rhythm"]),
        }
        if row.get("charttime"):
            rhythm_obs["effectiveDateTime"] = _dt(row["charttime"])
        obs_list.append(rhythm_obs)

    return obs_list


def build_ed_condition(row: dict, patient_uid: str, enc_uid: str) -> dict:
    uid = _uuid("ed-condition", row["stay_id"], row["seq_num"])
    return {
        "resourceType": "Condition",
        "id": uid,
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
        "subject": _ref(patient_uid),
        "encounter": _ref(enc_uid),
    }


def build_ed_medrecon(row: dict, patient_uid: str, enc_uid: str) -> dict:
    uid = _uuid(
        "ed-medrecon",
        row["stay_id"],
        row.get("charttime") or row.get("etc_rn") or 0,
        row.get("name") or "",
    )
    r: dict = {
        "resourceType": "MedicationStatement",
        "id": uid,
        "status": "active",
        "medicationCodeableConcept": {"text": row.get("name") or ""},
        "subject": _ref(patient_uid),
        "context": _ref(enc_uid),
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


def build_ed_pyxis(row: dict, patient_uid: str, enc_uid: str) -> dict:
    uid = _uuid(
        "ed-pyxis",
        row["stay_id"],
        row.get("med_rn") or 0,
        row.get("charttime") or "",
    )
    r: dict = {
        "resourceType": "MedicationDispense",
        "id": uid,
        "status": "completed",
        "medicationCodeableConcept": {"text": row.get("name") or ""},
        "subject": _ref(patient_uid),
        "context": _ref(enc_uid),
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


# ── claim / explanation-of-benefit builders ──────────────────────────────────


def build_claim(
    adm: dict,
    patient_uid: str,
    org_uid: str,
    enc_uid: str,
    condition_uids: list[str],
    drg_rows: list[dict],
) -> dict:
    uid = _uuid("claim", adm["hadm_id"])
    insurance = adm.get("insurance") or "Unknown"
    adm_type_key = (adm.get("admission_type") or "").upper()
    cls_code, _ = _ADMISSION_CLASS.get(adm_type_key, ("IMP", ""))
    snomed_code, snomed_display = _ENCOUNTER_SNOMED[cls_code]

    diagnosis_entries = [
        {"sequence": i + 1, "diagnosisReference": {"reference": _urn(cuid)}}
        for i, cuid in enumerate(condition_uids)
    ]

    items: list[dict] = [
        {
            "sequence": 1,
            "productOrService": {
                "coding": [_coding("http://snomed.info/sct", snomed_code, snomed_display)],
                "text": snomed_display,
            },
            "encounter": [{"reference": _urn(enc_uid)}],
        }
    ]
    for j, drg in enumerate(drg_rows, 2):
        item: dict = {
            "sequence": j,
            "productOrService": {
                "coding": [
                    _coding(
                        "http://terminology.hl7.org/CodeSystem/ex-diagnosistype",
                        str(drg.get("drg_code") or "DRG"),
                        drg.get("description"),
                    )
                ],
                "text": drg.get("description") or str(drg.get("drg_code") or "DRG"),
            },
        }
        if diagnosis_entries and (j - 1) <= len(diagnosis_entries):
            item["diagnosisSequence"] = [j - 1]
        items.append(item)

    claim: dict = {
        "resourceType": "Claim",
        "id": uid,
        "status": "active",
        "type": {
            "coding": [
                _coding("http://terminology.hl7.org/CodeSystem/claim-type", "institutional")
            ]
        },
        "use": "claim",
        "patient": {"reference": _urn(patient_uid)},
        "billablePeriod": {
            "start": _dt(adm["admittime"]),
            **({"end": _dt(adm["dischtime"])} if adm.get("dischtime") else {}),
        },
        "created": _dt(adm.get("dischtime") or adm["admittime"]),
        "provider": _ref(org_uid, BIDMC_NAME),
        "priority": {
            "coding": [
                _coding("http://terminology.hl7.org/CodeSystem/processpriority", "normal")
            ]
        },
        "insurance": [
            {"sequence": 1, "focal": True, "coverage": {"display": insurance}}
        ],
        "item": items,
        "total": {"value": 0.0, "currency": "USD"},
    }
    if diagnosis_entries:
        claim["diagnosis"] = diagnosis_entries
    return claim


def build_eob(
    adm: dict,
    patient_uid: str,
    org_uid: str,
    provider_uid: str | None,
    claim_uid: str,
    enc_uid: str,
    condition_uids: list[str],
) -> dict:
    uid = _uuid("eob", adm["hadm_id"])
    insurance = adm.get("insurance") or "Unknown"
    adm_type_key = (adm.get("admission_type") or "").upper()
    cls_code, _ = _ADMISSION_CLASS.get(adm_type_key, ("IMP", ""))
    snomed_code, snomed_display = _ENCOUNTER_SNOMED[cls_code]
    place_code, place_display = _SERVICE_PLACE[cls_code]
    referral_ref = _urn(provider_uid) if provider_uid else _urn(org_uid)

    contained = [
        {
            "resourceType": "ServiceRequest",
            "id": "referral",
            "status": "completed",
            "intent": "order",
            "subject": {"reference": _urn(patient_uid)},
            "requester": {"reference": referral_ref},
            "performer": [{"reference": referral_ref}],
        },
        {
            "resourceType": "Coverage",
            "id": "coverage",
            "status": "active",
            "type": {"text": insurance},
            "beneficiary": {"reference": _urn(patient_uid)},
            "payor": [{"display": insurance}],
        },
    ]

    diagnosis_entries = [
        {
            "sequence": i + 1,
            "diagnosisReference": {"reference": _urn(cuid)},
            "type": [
                {
                    "coding": [
                        _coding(
                            "http://terminology.hl7.org/CodeSystem/ex-diagnosistype",
                            "principal" if i == 0 else "discharge",
                        )
                    ]
                }
            ],
        }
        for i, cuid in enumerate(condition_uids)
    ]

    care_team: list[dict] = []
    if provider_uid:
        care_team = [
            {
                "sequence": 1,
                "provider": {"reference": _urn(provider_uid)},
                "role": {
                    "coding": [
                        _coding(
                            "http://terminology.hl7.org/CodeSystem/claimcareteamrole",
                            "primary",
                            "Primary Care Practitioner",
                        )
                    ]
                },
            }
        ]

    eob: dict = {
        "resourceType": "ExplanationOfBenefit",
        "id": uid,
        "contained": contained,
        "identifier": [
            {
                "system": "https://bluebutton.cms.gov/resources/variables/clm_id",
                "value": claim_uid,
            },
            {
                "system": "https://bluebutton.cms.gov/resources/identifier/claim-group",
                "value": "99999999999",
            },
        ],
        "status": "active",
        "type": {
            "coding": [
                _coding("http://terminology.hl7.org/CodeSystem/claim-type", "institutional")
            ]
        },
        "use": "claim",
        "patient": {"reference": _urn(patient_uid)},
        "billablePeriod": {
            "start": _dt(adm["admittime"]),
            **({"end": _dt(adm["dischtime"])} if adm.get("dischtime") else {}),
        },
        "created": _dt(adm.get("dischtime") or adm["admittime"]),
        "insurer": {"display": insurance},
        "provider": _ref(provider_uid or org_uid),
        "referral": {"reference": "#referral"},
        "claim": {"reference": _urn(claim_uid)},
        "outcome": "complete",
        "insurance": [
            {
                "focal": True,
                "coverage": {"reference": "#coverage", "display": insurance},
            }
        ],
        "item": [
            {
                "sequence": 1,
                "category": {
                    "coding": [
                        _coding(
                            "https://bluebutton.cms.gov/resources/variables/line_cms_type_srvc_cd",
                            "1",
                            "Medical care",
                        )
                    ]
                },
                "productOrService": {
                    "coding": [_coding("http://snomed.info/sct", snomed_code, snomed_display)],
                    "text": snomed_display,
                },
                "servicedPeriod": {
                    "start": _dt(adm["admittime"]),
                    **({"end": _dt(adm["dischtime"])} if adm.get("dischtime") else {}),
                },
                "locationCodeableConcept": {
                    "coding": [
                        _coding(
                            "http://terminology.hl7.org/CodeSystem/ex-serviceplace",
                            place_code,
                            place_display,
                        )
                    ]
                },
                "encounter": [{"reference": _urn(enc_uid)}],
            }
        ],
        "total": [
            {
                "category": {
                    "coding": [
                        _coding(
                            "http://terminology.hl7.org/CodeSystem/adjudication",
                            "submitted",
                            "Submitted Amount",
                        )
                    ],
                    "text": "Submitted Amount",
                },
                "amount": {"value": 0.0, "currency": "USD"},
            }
        ],
        "payment": {"amount": {"value": 0.0, "currency": "USD"}},
    }
    if care_team:
        eob["careTeam"] = care_team
    if diagnosis_entries:
        eob["diagnosis"] = diagnosis_entries
    return eob


# ── bundle builder ────────────────────────────────────────────────────────────


def build_bundle(entries: list[dict]) -> dict:
    return {
        "resourceType": "Bundle",
        "type": "transaction",
        "entry": entries,
    }


# ── per-patient pipeline ──────────────────────────────────────────────────────


def convert_patient(cur, subject_id: int, output_dir: Path) -> int:
    entries: list[dict] = []
    _seen_ids: set[str] = set()

    def add(resource: dict):
        rid = resource.get("id")
        if rid and rid in _seen_ids:
            return
        if rid:
            _seen_ids.add(rid)
        entries.append(_entry(resource))

    patient_uid = _uuid("patient", subject_id)

    # Organization (BIDMC) — one per bundle
    add(build_organization())

    # Patient
    cur.execute("SELECT * FROM hosp.patients WHERE subject_id = %s", (subject_id,))
    pat_row = cur.fetchone()
    if pat_row is None:
        return 0

    cur.execute(
        "SELECT * FROM hosp.admissions WHERE subject_id = %s ORDER BY admittime DESC LIMIT 1",
        (subject_id,),
    )
    latest_admission = cur.fetchone()

    add(build_patient(pat_row, latest_admission))

    # Practitioners — collect all distinct provider IDs for this patient
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
    provider_rows = cur.fetchall()
    provider_uids: dict[str, str] = {}
    for p in provider_rows:
        pid = p["provider_id"]
        uid = _uuid("practitioner", pid)
        provider_uids[pid] = uid
        add(build_practitioner(pid))

    # Hospital encounters
    cur.execute(
        "SELECT * FROM hosp.admissions WHERE subject_id = %s ORDER BY admittime",
        (subject_id,),
    )
    admissions = cur.fetchall()
    hosp_enc_uids: dict[int, str] = {}
    for adm in admissions:
        p_uid = provider_uids.get(adm.get("admit_provider_id") or "")
        enc = build_encounter_hosp(adm, patient_uid, BIDMC_UUID, p_uid)
        hosp_enc_uids[adm["hadm_id"]] = enc["id"]
        add(enc)

    # ICU encounters
    cur.execute(
        "SELECT * FROM icu.icustays WHERE subject_id = %s ORDER BY intime",
        (subject_id,),
    )
    icu_enc_uids: dict[int, str] = {}
    for icu in cur.fetchall():
        hosp_uid = hosp_enc_uids.get(icu["hadm_id"])
        if not hosp_uid:
            continue
        enc = build_encounter_icu(icu, patient_uid, hosp_uid)
        icu_enc_uids[icu["stay_id"]] = enc["id"]
        add(enc)

    # Conditions — tracked per admission for Claim building
    cur.execute(
        """
        SELECT d.*, i.long_title, a.admittime
        FROM hosp.diagnoses_icd d
        LEFT JOIN hosp.d_icd_diagnoses i ON d.icd_code = i.icd_code AND d.icd_version = i.icd_version
        LEFT JOIN hosp.admissions a ON d.hadm_id = a.hadm_id
        WHERE d.subject_id = %s
        ORDER BY d.hadm_id, d.seq_num
        """,
        (subject_id,),
    )
    conditions_per_hadm: dict[int, list[str]] = defaultdict(list)
    for row in cur.fetchall():
        enc_uid = hosp_enc_uids.get(row["hadm_id"])
        if enc_uid:
            cond = build_condition(row, patient_uid, enc_uid)
            conditions_per_hadm[row["hadm_id"]].append(cond["id"])
            add(cond)

    # DRG codes per admission for Claim line items
    cur.execute(
        "SELECT * FROM hosp.drgcodes WHERE subject_id = %s ORDER BY hadm_id",
        (subject_id,),
    )
    drg_per_hadm: dict[int, list] = defaultdict(list)
    for row in cur.fetchall():
        drg_per_hadm[row["hadm_id"]].append(row)

    # Claims + ExplanationOfBenefits — one per hospital encounter
    for adm in admissions:
        hadm_id = adm["hadm_id"]
        enc_uid = hosp_enc_uids[hadm_id]
        cond_uids = list(conditions_per_hadm.get(hadm_id, []))
        drg_rows = list(drg_per_hadm.get(hadm_id, []))
        p_uid = provider_uids.get(adm.get("admit_provider_id") or "")
        claim = build_claim(adm, patient_uid, BIDMC_UUID, enc_uid, cond_uids, drg_rows)
        add(claim)
        add(build_eob(adm, patient_uid, BIDMC_UUID, p_uid, claim["id"], enc_uid, cond_uids))

    # Procedures
    cur.execute(
        """
        SELECT p.*, i.long_title
        FROM hosp.procedures_icd p
        LEFT JOIN hosp.d_icd_procedures i ON p.icd_code = i.icd_code AND p.icd_version = i.icd_version
        WHERE p.subject_id = %s
        ORDER BY p.hadm_id, p.seq_num
        """,
        (subject_id,),
    )
    for row in cur.fetchall():
        enc_uid = hosp_enc_uids.get(row["hadm_id"])
        if enc_uid:
            add(build_procedure(row, patient_uid, enc_uid))

    # Lab observations — capped per patient to limit bundle size on full dataset
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
    for row in cur.fetchall():
        enc_uid = hosp_enc_uids.get(row["hadm_id"]) if row.get("hadm_id") else None
        add(build_lab_observation(row, patient_uid, enc_uid))

    # Chart observations (vitals only) — capped per patient to limit bundle size
    chart_item_ids = list(_CHART_LOINC.keys())
    cur.execute(
        f"""
        SELECT c.*, d.label
        FROM icu.chartevents c
        LEFT JOIN icu.d_items d ON c.itemid = d.itemid
        WHERE c.subject_id = %s AND c.itemid IN ({','.join('%s' for _ in chart_item_ids)})
        ORDER BY c.charttime DESC
        LIMIT 2000
        """,
        (subject_id, *chart_item_ids),
    )
    for row in cur.fetchall():
        enc_uid = icu_enc_uids.get(row["stay_id"])
        if enc_uid:
            add(build_chart_observation(row, patient_uid, enc_uid))

    # ICU caregivers
    cur.execute(
        """
        SELECT DISTINCT caregiver_id FROM icu.datetimeevents
        WHERE subject_id = %s AND caregiver_id IS NOT NULL
        UNION
        SELECT DISTINCT caregiver_id FROM icu.inputevents
        WHERE subject_id = %s AND caregiver_id IS NOT NULL
        UNION
        SELECT DISTINCT caregiver_id FROM icu.outputevents
        WHERE subject_id = %s AND caregiver_id IS NOT NULL
        """,
        (subject_id, subject_id, subject_id),
    )
    for row in cur.fetchall():
        add(build_icu_caregiver(row))

    # ICU datetime observations — capped per patient
    cur.execute(
        """
        SELECT de.*, d.label
        FROM icu.datetimeevents de
        LEFT JOIN icu.d_items d ON de.itemid = d.itemid
        WHERE de.subject_id = %s
        ORDER BY de.charttime DESC
        LIMIT 500
        """,
        (subject_id,),
    )
    for row in cur.fetchall():
        enc_uid = icu_enc_uids.get(row["stay_id"])
        if enc_uid:
            add(build_datetime_observation(row, patient_uid, enc_uid))

    # ICU output observations — capped per patient
    cur.execute(
        """
        SELECT oe.*, d.label
        FROM icu.outputevents oe
        LEFT JOIN icu.d_items d ON oe.itemid = d.itemid
        WHERE oe.subject_id = %s
        ORDER BY oe.charttime DESC
        LIMIT 500
        """,
        (subject_id,),
    )
    for row in cur.fetchall():
        enc_uid = icu_enc_uids.get(row["stay_id"])
        if enc_uid:
            add(build_output_observation(row, patient_uid, enc_uid))

    # ICU input events — capped per patient
    cur.execute(
        """
        SELECT ie.*, d.label
        FROM icu.inputevents ie
        LEFT JOIN icu.d_items d ON ie.itemid = d.itemid
        WHERE ie.subject_id = %s
        ORDER BY ie.starttime DESC
        LIMIT 2000
        """,
        (subject_id,),
    )
    for row in cur.fetchall():
        enc_uid = icu_enc_uids.get(row["stay_id"])
        if enc_uid:
            add(build_input_event(row, patient_uid, enc_uid))

    # ICU ingredient events — capped per patient
    cur.execute(
        """
        SELECT ige.*, d.label
        FROM icu.ingredientevents ige
        LEFT JOIN icu.d_items d ON ige.itemid = d.itemid
        WHERE ige.subject_id = %s
        ORDER BY ige.starttime DESC
        LIMIT 2000
        """,
        (subject_id,),
    )
    for row in cur.fetchall():
        enc_uid = icu_enc_uids.get(row["stay_id"])
        if enc_uid:
            add(build_ingredient_event(row, patient_uid, enc_uid))

    # Medication requests
    cur.execute(
        "SELECT * FROM hosp.prescriptions WHERE subject_id = %s",
        (subject_id,),
    )
    for row in cur.fetchall():
        enc_uid = hosp_enc_uids.get(row["hadm_id"])
        if enc_uid:
            add(build_medication_request(row, patient_uid, enc_uid))

    # OMR observations
    cur.execute(
        "SELECT * FROM hosp.omr WHERE subject_id = %s ORDER BY chartdate, seq_num",
        (subject_id,),
    )
    for row in cur.fetchall():
        add(build_omr_observation(row, patient_uid))

    # Microbiology — DiagnosticReport + Observations
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
        for resource in build_diagnostic_report(group_list, patient_uid, enc_uid):
            add(resource)

    # ED encounters
    cur.execute("SELECT * FROM ed.edstays WHERE subject_id = %s ORDER BY intime", (subject_id,))
    ed_enc_uids: dict[int, str] = {}
    for row in cur.fetchall():
        hosp_uid = hosp_enc_uids.get(row["hadm_id"]) if row.get("hadm_id") else None
        enc = build_encounter_ed(row, patient_uid, hosp_uid)
        ed_enc_uids[row["stay_id"]] = enc["id"]
        add(enc)

    # ED triage observations
    cur.execute("SELECT * FROM ed.triage WHERE subject_id = %s", (subject_id,))
    for row in cur.fetchall():
        enc_uid = ed_enc_uids.get(row["stay_id"])
        if enc_uid:
            for obs in build_triage_observations(row, patient_uid, enc_uid):
                add(obs)

    # ED vitalsign observations
    cur.execute("SELECT * FROM ed.vitalsign WHERE subject_id = %s ORDER BY stay_id, charttime", (subject_id,))
    for row in cur.fetchall():
        enc_uid = ed_enc_uids.get(row["stay_id"])
        if enc_uid:
            for obs in build_ed_vitalsign_observations(row, patient_uid, enc_uid):
                add(obs)

    # ED conditions
    cur.execute("SELECT * FROM ed.diagnosis WHERE subject_id = %s ORDER BY stay_id, seq_num", (subject_id,))
    for row in cur.fetchall():
        enc_uid = ed_enc_uids.get(row["stay_id"])
        if enc_uid:
            add(build_ed_condition(row, patient_uid, enc_uid))

    # ED medication reconciliation
    cur.execute("SELECT * FROM ed.medrecon WHERE subject_id = %s ORDER BY stay_id, charttime", (subject_id,))
    for row in cur.fetchall():
        enc_uid = ed_enc_uids.get(row["stay_id"])
        if enc_uid:
            add(build_ed_medrecon(row, patient_uid, enc_uid))

    # ED pyxis dispenses
    cur.execute("SELECT * FROM ed.pyxis WHERE subject_id = %s ORDER BY stay_id, charttime", (subject_id,))
    for row in cur.fetchall():
        enc_uid = ed_enc_uids.get(row["stay_id"])
        if enc_uid:
            add(build_ed_pyxis(row, patient_uid, enc_uid))

    # Discharge summaries (MIMIC-IV-Note) — most recent 20 per patient
    cur.execute(
        "SELECT * FROM note.discharge WHERE subject_id = %s ORDER BY charttime DESC NULLS LAST LIMIT 20",
        (subject_id,),
    )
    for row in cur.fetchall():
        enc_uid = hosp_enc_uids.get(row["hadm_id"]) if row.get("hadm_id") else None
        cur2 = cur.connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        cur2.execute("SELECT * FROM note.discharge_detail WHERE note_id = %s ORDER BY field_ordinal", (row["note_id"],))
        detail = cur2.fetchall()
        cur2.close()
        add(build_document_reference(row, patient_uid, enc_uid, detail_rows=list(detail)))

    # Radiology notes (MIMIC-IV-Note) — most recent 20 per patient
    cur.execute(
        "SELECT * FROM note.radiology WHERE subject_id = %s ORDER BY charttime DESC NULLS LAST LIMIT 20",
        (subject_id,),
    )
    for row in cur.fetchall():
        enc_uid = hosp_enc_uids.get(row["hadm_id"]) if row.get("hadm_id") else None
        cur2 = cur.connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        cur2.execute("SELECT * FROM note.radiology_detail WHERE note_id = %s ORDER BY field_ordinal", (row["note_id"],))
        detail = cur2.fetchall()
        cur2.close()
        add(build_document_reference(row, patient_uid, enc_uid, detail_rows=list(detail)))

    bundle = build_bundle(entries)
    out_path = output_dir / f"{subject_id}.json"
    out_path.write_text(json.dumps(_sanitize_for_json(bundle), default=str, indent=2), encoding="utf-8")
    return len(entries)


# ── main ──────────────────────────────────────────────────────────────────────


def convert(
    dsn: str = DSN,
    output_dir: Path = OUTPUT_DIR,
    limit: int | None = None,
    offset: int = 0,
    subject_ids: list[int] | None = None,
    random_sample: bool = True,
):
    output_dir.mkdir(parents=True, exist_ok=True)
    conn = psycopg2.connect(dsn)
    conn.set_session(readonly=True, autocommit=True)
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

    if subject_ids is not None:
        sids = subject_ids
    else:
        effective_limit = limit if limit is not None else (100 if random_sample else None)
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
    print(f"Converting {total:,} patients → {output_dir.resolve()}/\n")
    total_entries = 0
    for i, sid in enumerate(sids, 1):
        n = convert_patient(cur, sid, output_dir)
        total_entries += n
        print(f"  [{i:{width}d}/{total}] subject {sid:>10}  {n:5d} entries  →  {sid}.json")

    cur.close()
    conn.close()
    print(f"\nDone. {total:,} bundles, {total_entries:,} total entries.")


if __name__ == "__main__":
    convert()
