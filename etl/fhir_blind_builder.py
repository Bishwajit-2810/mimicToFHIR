#!/usr/bin/env python3
"""
Standalone FHIR R4 resource builders for the FHIR (Blinded) pipeline.

Completely independent from mimic_to_bundle.py:
  - Different UUID namespace prevents ID collisions with standard fhir bundles.
  - Every resource gets a meta.tag marking it as "fhir_blind".
  - Helpers are duplicated here intentionally so this module never imports from
    the existing pipeline and cannot break it.

Builders provided:
  Patient, Organization, Practitioner
  Encounter          — hosp (build_encounter_hosp), ICU (build_encounter_icu),
                       ED (build_encounter_ed)
  Observation        — lab (build_lab_observation), chart/vitals (build_chart_observation),
                       ICU procedure (build_icu_procedure_observation), OMR (build_omr_observation),
                       ED triage (build_triage_observations), ED vitalsign (build_ed_vitalsign_observations),
                       ICU datetime (build_datetime_observation), ICU output (build_output_observation)
  Procedure          — ICD (build_procedure)
  Condition          — hosp ICD (build_condition), ED (build_ed_condition)
  MedicationRequest  — prescriptions (build_medication_request)
  MedicationAdministration — ICU input events (build_input_event),
                              ICU ingredient events (build_ingredient_event)
  MedicationStatement — ED medrecon (build_ed_medrecon)
  MedicationDispense — ED Pyxis (build_ed_pyxis)
  DiagnosticReport   — microbiology (build_diagnostic_report)
  DocumentReference  — notes with detail extensions (build_document_reference)
  Claim, ExplanationOfBenefit — DRG-based (build_claim, build_eob)
  Practitioner (ICU caregiver) — build_icu_caregiver

BLINDING RULE (applied in fhir_blind_gen.py, not here):
  Condition, Procedure, MedicationRequest, MedicationStatement, MedicationDispense,
  MedicationAdministration (inputevents, ingredientevents), and
  DocumentReference are excluded for the latest hospital encounter (latest_hadm)
  and latest ED stay (latest_ed_stay). All prior encounters have full data.
  Testing variant (include_notes=True) adds back latest-encounter notes.

Called exclusively by fhir_blind_gen.py.
"""

import base64
import math
import re
import uuid
from datetime import date, datetime
from typing import Any

_RANGE_RE = re.compile(r"^(\d*\.?\d+)\s*-\s*(\d*\.?\d+)$")

# ── UUID namespace — distinct from standard pipeline's namespace ───────────────
# Standard pipeline uses: 6ba7b810-9dad-11d1-80b4-00c04fd430c8 (DNS root)
# FHIR (Blinded) uses a v5 child derived from that root to stay deterministic but separate.
_NS_SEED = uuid.UUID("6ba7b810-9dad-11d1-80b4-00c04fd430c8")
_NS = uuid.uuid5(_NS_SEED, "fhir-blind-pipeline")

BIDMC_UUID = str(uuid.uuid5(_NS, "fhir_blind::org::BIDMC"))
BIDMC_NAME = "Beth Israel Deaconess Medical Center"

# Source tag applied to every resource meta
_FHIR_BLIND_TAG = {
    "system": "http://mimic.mit.edu/fhir/tag/pipeline",
    "code": "fhir_blind",
    "display": "FHIR (Blinded) — latest encounter diagnoses & treatments excluded",
}


# ── Low-level helpers ─────────────────────────────────────────────────────────


def _uuid(*keys: Any) -> str:
    return str(uuid.uuid5(_NS, "fhir_blind::" + "::".join(str(k) for k in keys)))


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
    q: dict[str, Any] = {}
    numeric = _numeric_value(value)
    if numeric is not None:
        q["value"] = numeric
    if unit:
        q["unit"] = unit
    if system:
        q["system"] = system
    return q



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


def _dt(v: Any) -> str | None:
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


def _meta() -> dict:
    return {"tag": [_FHIR_BLIND_TAG]}


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


# ── OMB race / ethnicity / language / marital maps ────────────────────────────

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

# LOINC codes for common ICU chart items
CHART_LOINC: dict[int, str] = {
    220045: "8867-4",   # Heart Rate
    220050: "8480-6",   # Systolic BP
    220051: "8462-4",   # Diastolic BP
    220052: "8478-0",   # Mean BP
    220210: "9279-1",   # Respiratory Rate
    223761: "8310-5",   # Temperature °F
    223762: "8310-5",   # Temperature °C
    220277: "2708-6",   # SpO2
    226253: "29463-7",  # Weight
}

# LOINC codes for ED triage / vitalsign fields
ED_VITAL_LOINC: dict[str, tuple[str, str, str]] = {
    "temperature": ("8310-5",  "Temperature",              "Cel"),
    "heartrate":   ("8867-4",  "Heart Rate",               "/min"),
    "resprate":    ("9279-1",  "Respiratory Rate",         "/min"),
    "o2sat":       ("2708-6",  "Oxygen Saturation",        "%"),
    "sbp":         ("8480-6",  "Systolic Blood Pressure",  "mm[Hg]"),
    "dbp":         ("8462-4",  "Diastolic Blood Pressure", "mm[Hg]"),
}


# ── Resource builders ─────────────────────────────────────────────────────────


def build_organization() -> dict:
    return {
        "resourceType": "Organization",
        "id": BIDMC_UUID,
        "meta": _meta(),
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
        "meta": _meta(),
        "identifier": [
            {"system": "http://mimic.mit.edu/fhir/provider", "value": provider_id}
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

    extensions.append(
        {
            "url": "http://hl7.org/fhir/us/core/StructureDefinition/us-core-birthsex",
            "valueCode": gender_code,
        }
    )
    extensions.append(
        {
            "url": "http://mimic.mit.edu/fhir/StructureDefinition/anchor-year-group",
            "valueString": row["anchor_year_group"],
        }
    )

    patient: dict = {
        "resourceType": "Patient",
        "id": uid,
        "meta": _meta(),
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
    row: dict,
    patient_uid: str,
    org_uid: str,
    provider_uid: str | None,
    service_code: str | None = None,
    transfer_rows: list[dict] | None = None,
) -> dict:
    uid = _uuid("encounter-hosp", row["hadm_id"])
    adm_type_key = (row.get("admission_type") or "").upper()
    cls_code, cls_display = _ADMISSION_CLASS.get(adm_type_key, ("IMP", "inpatient encounter"))
    snomed_code, snomed_display = _ENCOUNTER_SNOMED[cls_code]
    subject_id = row.get("subject_id", "")
    r: dict = {
        "resourceType": "Encounter",
        "id": uid,
        "meta": _meta(),
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
        "meta": _meta(),
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


def build_procedure(row: dict, patient_uid: str, enc_uid: str) -> dict:
    uid = _uuid("procedure", row["hadm_id"], row["seq_num"])
    return {
        "resourceType": "Procedure",
        "id": uid,
        "meta": _meta(),
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


def build_condition(row: dict, patient_uid: str, enc_uid: str) -> dict:
    uid = _uuid("condition", row["hadm_id"], row["seq_num"])
    return {
        "resourceType": "Condition",
        "id": uid,
        "meta": _meta(),
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
        **({"onsetDateTime": _dt(row.get("admittime"))} if row.get("admittime") else {}),
        **({"recordedDate": _dt(row.get("admittime"))} if row.get("admittime") else {}),
    }


def _dose_and_rate(dose_value: Any, dose_unit: str | None) -> dict | None:
    if dose_value is None or not dose_unit:
        return None
    if isinstance(dose_value, str):
        stripped = dose_value.strip()
        if not stripped:
            return None
        # MIMIC dose strings like "5-10" or "0.5 -1" are ranges — emit doseRange.
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
        "meta": _meta(),
        "status": "completed",
        "intent": "order",
        "medicationCodeableConcept": {"text": row.get("drug") or "Unknown"},
        "subject": _ref(patient_uid),
        "encounter": _ref(enc_uid),
    }
    if row.get("ndc"):
        r["medicationCodeableConcept"]["coding"] = [
            _coding("http://hl7.org/fhir/sid/ndc", row["ndc"], row.get("drug"))
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


def build_encounter_ed(row: dict, patient_uid: str, hosp_uid: str | None) -> dict:
    uid = _uuid("encounter-ed", row["stay_id"])
    r: dict = {
        "resourceType": "Encounter",
        "id": uid,
        "meta": _meta(),
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
    if hosp_uid:
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
    results: list[dict] = []
    for field, (loinc_code, loinc_display, unit) in ED_VITAL_LOINC.items():
        val = row.get(field)
        if val is None:
            continue
        uid = _uuid("triage-obs", row["stay_id"], field)
        obs: dict = {
            "resourceType": "Observation",
            "id": uid,
            "meta": _meta(),
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
                "coding": [_coding("http://loinc.org", loinc_code, loinc_display)],
                "text": loinc_display,
            },
            "subject": _ref(patient_uid),
            "encounter": _ref(enc_uid),
            "valueQuantity": _quantity(val, unit, "http://unitsofmeasure.org"),
        }
        results.append(obs)
    # Chief complaint
    if row.get("chiefcomplaint") is not None:
        uid = _uuid("triage-obs", row["stay_id"], "chiefcomplaint")
        results.append({
            "resourceType": "Observation",
            "id": uid,
            "meta": _meta(),
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
    # Acuity
    if row.get("acuity") is not None:
        uid = _uuid("triage-obs", row["stay_id"], "acuity")
        results.append({
            "resourceType": "Observation",
            "id": uid,
            "meta": _meta(),
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
            "valueQuantity": _quantity(row["acuity"]),
        })
    return results


def build_ed_vitalsign_observations(row: dict, patient_uid: str, enc_uid: str) -> list[dict]:
    results: list[dict] = []
    ts_key = (
        _dt(row["charttime"]).replace(":", "").replace("-", "").replace("T", "")
        if row.get("charttime")
        else "0"
    )
    for field, (loinc_code, loinc_display, unit) in ED_VITAL_LOINC.items():
        val = row.get(field)
        if val is None:
            continue
        uid = _uuid("ed-vital", row["stay_id"], field, ts_key)
        obs: dict = {
            "resourceType": "Observation",
            "id": uid,
            "meta": _meta(),
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
                "coding": [_coding("http://loinc.org", loinc_code, loinc_display)],
                "text": loinc_display,
            },
            "subject": _ref(patient_uid),
            "encounter": _ref(enc_uid),
            "valueQuantity": _quantity(val, unit, "http://unitsofmeasure.org"),
        }
        if row.get("charttime"):
            obs["effectiveDateTime"] = _dt(row["charttime"])
        results.append(obs)
    # Rhythm
    if row.get("rhythm") is not None:
        uid = _uuid("ed-vital", row["stay_id"], "rhythm", ts_key)
        obs_rhythm: dict = {
            "resourceType": "Observation",
            "id": uid,
            "meta": _meta(),
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
            obs_rhythm["effectiveDateTime"] = _dt(row["charttime"])
        results.append(obs_rhythm)
    return results


def build_ed_condition(row: dict, patient_uid: str, enc_uid: str) -> dict:
    uid = _uuid("ed-condition", row["stay_id"], row["seq_num"])
    return {
        "resourceType": "Condition",
        "id": uid,
        "meta": _meta(),
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
    uid = _uuid("ed-medrecon", row["stay_id"], row.get("charttime") or row.get("etc_rn") or 0, row.get("name") or "")
    r: dict = {
        "resourceType": "MedicationStatement",
        "id": uid,
        "meta": _meta(),
        "status": "active",
        "medicationCodeableConcept": {"text": row.get("name") or "Unknown"},
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
    uid = _uuid("ed-pyxis", row["stay_id"], row.get("med_rn") or 0, row.get("charttime") or "")
    r: dict = {
        "resourceType": "MedicationDispense",
        "id": uid,
        "meta": _meta(),
        "status": "completed",
        "medicationCodeableConcept": {"text": row.get("name") or "Unknown"},
        "subject": _ref(patient_uid),
        "context": _ref(enc_uid),
    }
    if row.get("gsn"):
        r["medicationCodeableConcept"]["coding"] = [
            _coding(
                "http://mimic.mit.edu/fhir/CodeSystem/gsn",
                row["gsn"],
                row.get("name"),
            )
        ]
    if row.get("charttime"):
        r["whenHandedOver"] = _dt(row["charttime"])
    return r


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
        "meta": _meta(),
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
        obs["valueQuantity"] = _quantity(
            float(row["valuenum"]),
            row.get("valueuom") or None,
            "http://unitsofmeasure.org",
        )
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
    loinc = CHART_LOINC.get(row["itemid"])
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
        "meta": _meta(),
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


def build_icu_procedure_observation(row: dict, patient_uid: str, enc_uid: str) -> dict:
    """Build an Observation for an ICU procedure event (ventilation, dialysis, etc.)."""
    uid = _uuid("icu-proc", row["stay_id"], row["orderid"])
    return {
        "resourceType": "Observation",
        "id": uid,
        "meta": _meta(),
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
            "text": row.get("label") or str(row.get("itemid", "")),
            "coding": [
                _coding(
                    "http://mimic.mit.edu/fhir/CodeSystem/d-items",
                    str(row.get("itemid", "")),
                    row.get("label"),
                )
            ],
        },
        "subject": _ref(patient_uid),
        "encounter": _ref(enc_uid),
        **({"effectiveDateTime": _dt(row["starttime"])} if row.get("starttime") else {}),
        **(
            {"valueQuantity": _quantity(
                float(row["value"]),
                row.get("valueuom") or None,
                "http://unitsofmeasure.org",
            )}
            if row.get("value") is not None
            else {}
        ),
    }


def build_icu_caregiver(row: dict) -> dict:
    """Build a Practitioner resource from an ICU caregiver row."""
    uid = _uuid("caregiver", row["caregiver_id"])
    return {
        "resourceType": "Practitioner",
        "id": uid,
        "meta": _meta(),
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
        "meta": _meta(),
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
        # Try to detect datetime-like values
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
        "meta": _meta(),
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
        "meta": _meta(),
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
        "meta": _meta(),
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
            "meta": _meta(),
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
            **({"effectiveDateTime": _dt(row.get("charttime") or row.get("chartdate"))}
               if (row.get("charttime") or row.get("chartdate")) else {}),
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
        "meta": _meta(),
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
    uid = _uuid(
        "omr",
        row["subject_id"],
        _dt(row["chartdate"]),
        row["seq_num"],
        row.get("result_name") or "",
    )
    return {
        "resourceType": "Observation",
        "id": uid,
        "meta": _meta(),
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


_NOTE_TYPE_LOINC: dict[str, tuple[str, str]] = {
    "DS":  ("18842-5", "Discharge summary"),
    "AR":  ("18726-0", "Radiology studies (set)"),
    "RR":  ("18726-0", "Radiology studies (set)"),
    "ECG": ("11524-6", "EKG study"),
    "ECH": ("34750-4", "Echocardiography study"),
    "NUR": ("34119-2", "Nursing facility initial assessment note"),
    "PH":  ("47049-6", "Pharmacy note"),
}


def build_document_reference(
    row: dict,
    patient_uid: str,
    enc_uid: str | None,
    detail_rows: list[dict] | None = None,
) -> dict:
    note_type = (row.get("note_type") or "").upper()
    loinc_code, loinc_display = _NOTE_TYPE_LOINC.get(note_type, ("34109-3", "Note"))
    uid = _uuid("docref", row["note_id"])
    text_bytes = (row.get("text") or "").encode("utf-8")
    doc: dict = {
        "resourceType": "DocumentReference",
        "id": uid,
        "meta": _meta(),
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
        doc.setdefault("extension", []).append(
            {
                "url": "http://mimic.mit.edu/fhir/StructureDefinition/note-detail",
                "extension": [
                    {"url": r["field_name"], "valueString": str(r["field_value"])}
                    for r in detail_rows
                    if r.get("field_value")
                ],
            }
        )
    return doc


def build_claim(
    adm: dict,
    patient_uid: str,
    org_uid: str,
    enc_uid: str,
    drg_rows: list[dict],
) -> dict:
    uid = _uuid("claim", adm["hadm_id"])
    insurance = adm.get("insurance") or "Unknown"
    adm_type_key = (adm.get("admission_type") or "").upper()
    cls_code, _ = _ADMISSION_CLASS.get(adm_type_key, ("IMP", ""))
    snomed_code, snomed_display = _ENCOUNTER_SNOMED[cls_code]

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
        items.append(
            {
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
        )

    return {
        "resourceType": "Claim",
        "id": uid,
        "meta": _meta(),
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


def build_eob(
    adm: dict,
    patient_uid: str,
    org_uid: str,
    provider_uid: str | None,
    claim_uid: str,
    enc_uid: str,
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
        "meta": _meta(),
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
    return eob


def build_bundle(entries: list[dict], latest_hadm_id: int | None = None) -> dict:
    bundle: dict = {
        "resourceType": "Bundle",
        "type": "transaction",
        "meta": {
            "tag": [_FHIR_BLIND_TAG],
        },
        "entry": entries,
    }
    if latest_hadm_id is not None:
        bundle["meta"]["extension"] = [
            {
                "url": "http://mimic.mit.edu/fhir/StructureDefinition/fhir-blinded-hadm",
                "valueInteger": latest_hadm_id,
            }
        ]
    return bundle
