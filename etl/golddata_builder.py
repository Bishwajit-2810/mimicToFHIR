#!/usr/bin/env python3
"""
Standalone FHIR R4 resource builders for the golddata pipeline.

Completely independent from mimic_to_bundle.py:
  - Different UUID namespace prevents ID collisions with standard fhir bundles.
  - Every resource gets a meta.tag marking it as "golddata_fhir".
  - Helpers are duplicated here intentionally so this module never imports from
    the existing pipeline and cannot break it.

Golddata bundles blind the latest encounter: Condition (diagnoses) and
MedicationRequest (treatments) are excluded; Observation (vitals, labs, OMR),
DiagnosticReport, Procedure, and Encounter metadata are fully retained.

Called exclusively by golddata_fhir_gen.py.
"""

import re
import uuid
from datetime import date, datetime
from typing import Any

# ── UUID namespace — distinct from standard pipeline's namespace ───────────────
# Standard pipeline uses: 6ba7b810-9dad-11d1-80b4-00c04fd430c8 (DNS root)
# Golddata uses a v5 child derived from that root to stay deterministic but separate.
_NS_SEED = uuid.UUID("6ba7b810-9dad-11d1-80b4-00c04fd430c8")
_NS = uuid.uuid5(_NS_SEED, "golddata-fhir-pipeline")

BIDMC_UUID = str(uuid.uuid5(_NS, "golddata::org::BIDMC"))
BIDMC_NAME = "Beth Israel Deaconess Medical Center"

_RANGE_RE = re.compile(r"^(\d*\.?\d+)-(\d*\.?\d+)$")

# Source tag applied to every resource meta
_GOLDDATA_TAG = {
    "system": "http://mimic.mit.edu/fhir/tag/pipeline",
    "code": "golddata_fhir",
    "display": "GoldData FHIR — diagnosis & treatment blind, latest encounter",
}


# ── Low-level helpers ─────────────────────────────────────────────────────────


def _uuid(*keys: Any) -> str:
    return str(uuid.uuid5(_NS, "golddata::" + "::".join(str(k) for k in keys)))


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
    q: dict[str, Any] = {"value": _numeric_value(value)}
    if unit:
        q["unit"] = unit
    if system:
        q["system"] = system
    return q


def _dose_and_rate(dose_value: Any, dose_unit: str | None) -> dict | None:
    if dose_value is None or not dose_unit:
        return None
    if isinstance(dose_value, str):
        stripped = dose_value.strip()
        m = _RANGE_RE.match(stripped)
        if m:
            return {
                "doseRange": {
                    "low": _quantity(m.group(1), dose_unit, "http://unitsofmeasure.org"),
                    "high": _quantity(m.group(2), dose_unit, "http://unitsofmeasure.org"),
                }
            }
        dose_value = stripped
    return {"doseQuantity": _quantity(dose_value, dose_unit, "http://unitsofmeasure.org")}


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
    return {"tag": [_GOLDDATA_TAG]}


def _entry(resource: dict) -> dict:
    uid = resource["id"]
    return {
        "fullUrl": _urn(uid),
        "resource": resource,
        "request": {"method": "POST", "url": resource["resourceType"]},
    }


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
    # Mark which hadm_id is the "blinded" latest encounter so consumers know
    if admission:
        extensions.append(
            {
                "url": "http://mimic.mit.edu/fhir/StructureDefinition/golddata-latest-encounter",
                "valueString": str(admission.get("hadm_id", "")),
            }
        )

    patient: dict = {
        "resourceType": "Patient",
        "id": uid,
        "meta": _meta(),
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
    is_latest: bool = False,
) -> dict:
    uid = _uuid("encounter-hosp", row["hadm_id"])
    r: dict = {
        "resourceType": "Encounter",
        "id": uid,
        "meta": _meta(),
        "status": "finished",
        "class": _coding(
            "http://terminology.hl7.org/CodeSystem/v3-ActCode",
            "IMP",
            "inpatient encounter",
        ),
        "type": [
            {
                "coding": [
                    _coding(
                        "http://snomed.info/sct",
                        "11429006",
                        row.get("admission_type", "Inpatient"),
                    )
                ],
                "text": row.get("admission_type", "Inpatient"),
            }
        ],
        "subject": _ref(patient_uid),
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

    # For the latest encounter we intentionally omit discharge disposition/diagnosis
    # to prevent outcome leakage.
    if not is_latest:
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

    extensions: list[dict] = []
    if row.get("insurance"):
        extensions.append(
            {
                "url": "http://mimic.mit.edu/fhir/StructureDefinition/insurance",
                "valueString": row["insurance"],
            }
        )
    if is_latest:
        extensions.append(
            {
                "url": "http://mimic.mit.edu/fhir/StructureDefinition/golddata-blinded",
                "valueBoolean": True,
            }
        )
    if extensions:
        r["extension"] = extensions

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
        "extension": [
            {
                "url": "http://mimic.mit.edu/fhir/StructureDefinition/los",
                "valueDecimal": (
                    round(float(row["los"]), 4) if row.get("los") else None
                ),
            }
        ],
    }


def build_condition(row: dict, patient_uid: str, enc_uid: str) -> dict:
    """Build a Condition for HISTORICAL encounters only. Never called for latest."""
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
        **(
            {"onsetDateTime": _dt(row.get("admittime"))} if row.get("admittime") else {}
        ),
        **({"recordedDate": _dt(row.get("admittime"))} if row.get("admittime") else {}),
    }


def build_procedure(row: dict, patient_uid: str, enc_uid: str) -> dict:
    """Procedures performed — included for all encounters including latest."""
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


def build_lab_observation(row: dict, patient_uid: str, enc_uid: str | None) -> dict:
    uid = _uuid("lab", row["labevent_id"])
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
            "coding": [
                _coding("http://loinc.org", str(row["itemid"]), row.get("label"))
            ],
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
        "code": {"coding": coding, "text": row.get("label")},
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
            "effectiveDateTime": _dt(row.get("charttime") or row.get("chartdate")),
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
        "effectiveDateTime": _dt(first.get("charttime") or first.get("chartdate")),
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
        "effectiveDateTime": _dt(row["chartdate"]),
        "valueString": str(row["result_value"]),
    }


def build_bundle(entries: list[dict], latest_hadm_id: int | None = None) -> dict:
    bundle: dict = {
        "resourceType": "Bundle",
        "type": "transaction",
        "meta": {
            "tag": [_GOLDDATA_TAG],
        },
        "entry": entries,
    }
    if latest_hadm_id is not None:
        bundle["meta"]["extension"] = [
            {
                "url": "http://mimic.mit.edu/fhir/StructureDefinition/golddata-blinded-hadm",
                "valueInteger": latest_hadm_id,
            }
        ]
    return bundle
