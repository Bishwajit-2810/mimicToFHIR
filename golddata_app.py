#!/usr/bin/env python3
"""
golddata_app.py — GoldData FHIR Dashboard (FastAPI)

Runs completely independently from app.py on its own port (default 8096).
Does NOT import from app.py or any existing pipeline module.

Provides:
  GET  /api/standard/patients          — list patients with standard_fhir bundles
  GET  /api/standard/patients/{id}     — parsed standard_fhir bundle
  GET  /api/golddata/patients          — list patients with golddata_fhir bundles
  GET  /api/golddata/patients/{id}     — parsed golddata_fhir bundle
  GET  /api/compare/{id}               — both parsed bundles side-by-side
  GET  /api/status                     — bundle counts + pipeline status
  POST /api/run/standard               — trigger standard pipeline (background)
  POST /api/run/golddata               — trigger golddata pipeline (background)
  GET  /api/run/status                 — running pipeline status

Static SPA: static_golddata/index.html

Start:
    uvicorn golddata_app:app --host 0.0.0.0 --port 8096 --reload
"""

import json
import os
import re
import subprocess
import sys
import time
from datetime import datetime
from functools import lru_cache
from pathlib import Path
from typing import Any

from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI(title="GoldData FHIR Dashboard")

STANDARD_BUNDLES_DIR = Path("fhir_bundles")
GOLDDATA_BUNDLES_DIR = Path("golddata_fhir_bundles")
STATIC_DIR = Path("static_golddata")

# ── Pipeline run tracking (in-memory) ────────────────────────────────────────

_running_processes: dict[str, dict] = {}  # pipeline_name → {proc, started, log_lines}


# ── LOINC / vital mappings (duplicated from app.py to stay isolated) ──────────

VITAL_LOINC = {
    "8867-4": "Heart Rate",
    "8480-6": "Systolic BP",
    "8462-4": "Diastolic BP",
    "9279-1": "Respiratory Rate",
    "8310-5": "Temperature",
    "59408-5": "SpO2",
    "29463-7": "Weight",
    "8302-2": "Height",
}

VITAL_ICONS = {
    "Heart Rate": "fa-heart-pulse",
    "Systolic BP": "fa-gauge-high",
    "Diastolic BP": "fa-gauge",
    "Respiratory Rate": "fa-lungs",
    "Temperature": "fa-thermometer-half",
    "SpO2": "fa-percent",
    "Weight": "fa-weight-scale",
    "Height": "fa-ruler-vertical",
}

VITAL_NORMAL = {
    "Heart Rate": (60, 100),
    "Systolic BP": (90, 140),
    "Diastolic BP": (60, 90),
    "Respiratory Rate": (12, 20),
    "Temperature": (97.0, 99.5),
    "SpO2": (95, 100),
    "Weight": None,
    "Height": None,
}


# ── Helpers ───────────────────────────────────────────────────────────────────


def fmt_dt(raw: str | None) -> str | None:
    if not raw:
        return None
    try:
        s = re.sub(r"[+-]\d{2}:\d{2}$", "", raw).replace("Z", "")
        dt = datetime.fromisoformat(s)
        return dt.strftime("%Y-%m-%d %H:%M") if "T" in s else s
    except Exception:
        return raw


def concept_text(obj: dict) -> str:
    if not obj:
        return ""
    if obj.get("text"):
        return obj["text"]
    for c in obj.get("coding", []):
        if c.get("display"):
            return c["display"]
        if c.get("code"):
            return c["code"]
    return ""


# ── Per-resource parsers ──────────────────────────────────────────────────────


def _demographics(patient: dict, all_encounters: list) -> dict:
    if not patient:
        return {}

    race = ethnicity = birth_sex = anchor_year = "Unknown"
    latest_hadm = None

    for ext in patient.get("extension", []):
        url = ext.get("url", "")
        if "us-core-race" in url:
            for n in ext.get("extension", []):
                if n.get("url") == "text":
                    race = n.get("valueString", race)
        elif "us-core-ethnicity" in url:
            for n in ext.get("extension", []):
                if n.get("url") == "text":
                    ethnicity = n.get("valueString", ethnicity)
        elif "us-core-birthsex" in url:
            birth_sex = ext.get("valueCode", birth_sex)
        elif "anchor-year-group" in url:
            anchor_year = ext.get("valueString", anchor_year)
        elif "golddata-latest-encounter" in url:
            latest_hadm = ext.get("valueString")

    subject_id = next(
        (
            i.get("value", "")
            for i in patient.get("identifier", [])
            if "patient" in i.get("system", "")
        ),
        "",
    )

    birth_date = patient.get("birthDate", "")
    deceased = patient.get("deceasedDateTime", "")

    age = None
    if birth_date and all_encounters:
        dates = [
            e.get("period", {}).get("start", "")
            for e in all_encounters
            if e.get("period", {}).get("start")
        ]
        if dates:
            latest = max(dates)
            try:
                bd = datetime.strptime(birth_date, "%Y-%m-%d")
                ed = datetime.fromisoformat(re.sub(r"[+-]\d{2}:\d{2}$", "", latest))
                age = (ed - bd).days // 365
            except Exception:
                pass

    marital = concept_text(patient.get("maritalStatus", {}))
    langs = [
        concept_text(c.get("language", {}))
        for c in patient.get("communication", [])
        if c.get("language")
    ]

    return {
        "subjectId": subject_id,
        "gender": patient.get("gender", "unknown").capitalize(),
        "birthDate": birth_date,
        "age": age,
        "deceased": fmt_dt(deceased) if deceased else None,
        "race": race,
        "ethnicity": ethnicity,
        "birthSex": birth_sex,
        "maritalStatus": marital,
        "language": ", ".join(langs) or "Unknown",
        "anchorYear": anchor_year,
        "goldataLatestHadm": latest_hadm,
    }


def _parse_vital_obs(obs: dict) -> dict | None:
    loinc = next(
        (
            c.get("code")
            for c in obs.get("code", {}).get("coding", [])
            if "loinc" in c.get("system", "").lower()
        ),
        None,
    )
    name = VITAL_LOINC.get(loinc or "", "")
    if not name:
        return None
    qty = obs.get("valueQuantity", {})
    val = qty.get("value") if qty else obs.get("valueString")
    if val is None:
        return None
    unit = qty.get("unit", "")
    eff = obs.get("effectiveDateTime", "")
    nr = VITAL_NORMAL.get(name)
    status = "normal"
    if nr and isinstance(val, (int, float)):
        status = "normal" if nr[0] <= val <= nr[1] else "abnormal"
    return {
        "name": name,
        "value": val,
        "unit": unit,
        "raw": eff,
        "time": fmt_dt(eff),
        "icon": VITAL_ICONS.get(name, "fa-stethoscope"),
        "status": status,
        "normalRange": nr,
        "encounterRef": obs.get("encounter", {}).get("reference", ""),
    }


def _vitals(obs_list: list) -> list:
    latest: dict[str, dict] = {}
    for obs in obs_list:
        parsed = _parse_vital_obs(obs)
        if parsed is None:
            continue
        name = parsed["name"]
        if name not in latest or parsed["raw"] > latest[name]["raw"]:
            latest[name] = parsed
    return sorted(latest.values(), key=lambda x: x["name"])


def _vitals_by_encounter(obs_list: list) -> dict[str, list]:
    groups: dict[str, list] = {}
    for obs in obs_list:
        parsed = _parse_vital_obs(obs)
        if parsed is None:
            continue
        enc = parsed["encounterRef"]
        groups.setdefault(enc, []).append(parsed)
    for enc in groups:
        groups[enc].sort(key=lambda x: x["name"])
    return groups


def _parse_lab_obs(obs: dict) -> dict | None:
    name = concept_text(obs.get("code", {}))
    if not name:
        return None
    qty = obs.get("valueQuantity", {})
    val = qty.get("value") if qty else obs.get("valueString", "")
    unit = qty.get("unit", "") if qty else ""
    flag = next(
        (
            c.get("code", "")
            for i in obs.get("interpretation", [])
            for c in i.get("coding", [])
        ),
        "",
    )
    rr = obs.get("referenceRange", [{}])[0] if obs.get("referenceRange") else {}
    ref_lo = rr.get("low", {}).get("value") if rr else None
    ref_hi = rr.get("high", {}).get("value") if rr else None
    eff = obs.get("effectiveDateTime", "")
    return {
        "name": name,
        "value": val,
        "unit": unit,
        "flag": flag,
        "refLow": ref_lo,
        "refHigh": ref_hi,
        "time": fmt_dt(eff),
        "rawDt": eff,
        "encounterRef": obs.get("encounter", {}).get("reference", ""),
    }


def _labs(obs_list: list) -> list:
    seen: dict[str, dict] = {}
    for obs in obs_list:
        parsed = _parse_lab_obs(obs)
        if parsed is None:
            continue
        name = parsed["name"]
        if name not in seen or parsed["rawDt"] > seen[name]["rawDt"]:
            seen[name] = parsed
    return sorted(seen.values(), key=lambda x: x["name"])


def _labs_by_encounter(obs_list: list) -> dict[str, list]:
    groups: dict[str, list] = {}
    for obs in obs_list:
        parsed = _parse_lab_obs(obs)
        if parsed is None:
            continue
        enc = parsed["encounterRef"]
        groups.setdefault(enc, []).append(parsed)
    for enc in groups:
        groups[enc].sort(key=lambda x: x["name"])
    return groups


def _conditions(conds: list) -> list:
    out = []
    for c in conds:
        code_obj = c.get("code", {})
        name = concept_text(code_obj)
        icd = next((cd.get("code", "") for cd in code_obj.get("coding", [])), "")
        sys_raw = next((cd.get("system", "") for cd in code_obj.get("coding", [])), "")
        icd_sys = (
            "ICD-10" if "icd-10" in sys_raw else ("ICD-9" if "icd-9" in sys_raw else "")
        )
        status = next(
            (
                cd.get("code", "")
                for s in [c.get("clinicalStatus", {})]
                for cd in s.get("coding", [])
            ),
            "",
        )
        out.append(
            {
                "name": name,
                "code": icd,
                "codeSystem": icd_sys,
                "status": status,
                "encounterRef": c.get("encounter", {}).get("reference", ""),
            }
        )
    return out


def _medications(meds: list) -> list:
    seen: dict[str, dict] = {}
    for m in meds:
        name = concept_text(m.get("medicationCodeableConcept", {}))
        if not name or name in seen:
            continue
        dosages = m.get("dosageInstruction", [{}])
        d = dosages[0] if dosages else {}
        route = concept_text(d.get("route", {}))
        dose_val = next(
            (
                f"{dr.get('doseQuantity', {}).get('value', '')} "
                f"{dr.get('doseQuantity', {}).get('unit', '')}".strip()
                for dr in d.get("doseAndRate", [])
                if dr.get("doseQuantity", {}).get("value") is not None
            ),
            "",
        )
        period = m.get("dispenseRequest", {}).get("validityPeriod", {})
        seen[name] = {
            "name": name,
            "status": m.get("status", ""),
            "dose": dose_val,
            "route": route,
            "start": fmt_dt(period.get("start")),
            "end": fmt_dt(period.get("end")),
            "encounterRef": m.get("encounter", {}).get("reference", ""),
        }
    return sorted(seen.values(), key=lambda x: x["name"])


def _encounters(encs: list) -> list:
    hospital, icu = [], []
    for e in encs:
        cls = e.get("class", {}).get("code", "")
        period = e.get("period", {})
        types = e.get("type", [])
        locs = e.get("location", [])
        hosp_info = e.get("hospitalization", {})
        exts = {x.get("url"): x for x in e.get("extension", [])}
        ins = exts.get("insurance", {}).get("valueString", "") if "insurance" in str(exts) else ""
        # Resolve insurance extension URL (may vary)
        for url_key, ext_val in exts.items():
            if "insurance" in url_key:
                ins = ext_val.get("valueString", "")
                break
        los = None
        blinded = False
        for url_key, ext_val in exts.items():
            if "los" in url_key:
                los = ext_val.get("valueDecimal")
            if "golddata-blinded" in url_key:
                blinded = ext_val.get("valueBoolean", False)

        row = {
            "id": "urn:uuid:" + e.get("id", ""),
            "cls": cls,
            "type": concept_text(types[0]) if types else "",
            "status": e.get("status", ""),
            "start": fmt_dt(period.get("start")),
            "end": fmt_dt(period.get("end")),
            "rawStart": period.get("start", ""),
            "location": locs[0].get("location", {}).get("display", "") if locs else "",
            "admitSource": concept_text(hosp_info.get("admitSource", {})),
            "dischDisp": concept_text(hosp_info.get("dischargeDisposition", {})),
            "insurance": ins,
            "los": round(los, 2) if los is not None else None,
            "partOf": e.get("partOf", {}).get("reference", ""),
            "children": [],
            "participantRefs": [
                p.get("individual", {}).get("reference", "")
                for p in e.get("participant", [])
            ],
            "blinded": blinded,
        }

        if row["partOf"]:
            icu.append(row)
        else:
            hospital.append(row)

    by_id = {h["id"]: h for h in hospital}
    for i in icu:
        parent = by_id.get(i["partOf"])
        if parent is not None:
            parent["children"].append(i)
        else:
            hospital.append(i)

    hospital.sort(key=lambda x: x["rawStart"], reverse=True)
    return hospital


def _diagnostic_reports(rpts: list) -> list:
    out = []
    for r in rpts:
        cats = r.get("category", [])
        out.append(
            {
                "name": concept_text(r.get("code", {})),
                "category": concept_text(cats[0]) if cats else "",
                "time": fmt_dt(r.get("effectiveDateTime")),
                "status": r.get("status", ""),
                "encounterRef": r.get("encounter", {}).get("reference", ""),
            }
        )
    out.sort(key=lambda x: x.get("time") or "", reverse=True)
    return out


def _procedures(procs: list) -> list:
    out = []
    for p in procs:
        out.append(
            {
                "name": concept_text(p.get("code", {})),
                "time": fmt_dt(p.get("performedDateTime")),
                "status": p.get("status", ""),
                "encounterRef": p.get("encounter", {}).get("reference", ""),
            }
        )
    out.sort(key=lambda x: x.get("time") or "", reverse=True)
    return out


def _practitioners(pract_list: list) -> dict:
    result = {}
    for p in pract_list:
        uid = "urn:uuid:" + p.get("id", "")
        names = p.get("name", [{}])
        n = names[0] if names else {}
        given = " ".join(n.get("given", []))
        family = n.get("family", "")
        full = f"{given} {family}".strip()
        ident = next(
            (i.get("value", "") for i in p.get("identifier", [])),
            "",
        )
        result[uid] = {"name": full, "providerId": ident}
    return result


def _bundle_meta_tags(bundle: dict) -> list[str]:
    """Extract pipeline tags from bundle meta."""
    return [
        t.get("code", "")
        for t in bundle.get("meta", {}).get("tag", [])
    ]


def _blinded_hadm(bundle: dict) -> int | None:
    """Extract the blinded hadm_id from bundle meta extensions."""
    for ext in bundle.get("meta", {}).get("extension", []):
        if "golddata-blinded-hadm" in ext.get("url", ""):
            return ext.get("valueInteger")
    return None


# ── Bundle parser ─────────────────────────────────────────────────────────────


def parse_bundle(bundle: dict) -> dict:
    resources: dict[str, list] = {
        "Patient": [],
        "Encounter": [],
        "Condition": [],
        "ObsLab": [],
        "ObsVital": [],
        "ObsOther": [],
        "MedicationRequest": [],
        "DiagnosticReport": [],
        "Procedure": [],
        "Practitioner": [],
    }

    for entry in bundle.get("entry", []):
        r = entry.get("resource", {})
        rt = r.get("resourceType", "")
        if rt == "Patient":
            resources["Patient"].append(r)
        elif rt == "Encounter":
            resources["Encounter"].append(r)
        elif rt == "Condition":
            resources["Condition"].append(r)
        elif rt == "Observation":
            cats = {
                cd.get("code", "")
                for cat in r.get("category", [])
                for cd in cat.get("coding", [])
            }
            if "laboratory" in cats:
                resources["ObsLab"].append(r)
            elif "vital-signs" in cats:
                resources["ObsVital"].append(r)
            else:
                resources["ObsOther"].append(r)
        elif rt == "MedicationRequest":
            resources["MedicationRequest"].append(r)
        elif rt == "DiagnosticReport":
            resources["DiagnosticReport"].append(r)
        elif rt == "Procedure":
            resources["Procedure"].append(r)
        elif rt == "Practitioner":
            resources["Practitioner"].append(r)

    patient = resources["Patient"][0] if resources["Patient"] else {}
    raw_encs = resources["Encounter"]

    demo = _demographics(patient, raw_encs)
    encs = _encounters(raw_encs)
    conds = _conditions(resources["Condition"])
    meds = _medications(resources["MedicationRequest"])
    vitals = _vitals(resources["ObsVital"])
    labs = _labs(resources["ObsLab"])
    reports = _diagnostic_reports(resources["DiagnosticReport"])
    procs = _procedures(resources["Procedure"])
    prac_lookup = _practitioners(resources["Practitioner"])
    vitals_by_enc = _vitals_by_encounter(resources["ObsVital"])
    labs_by_enc = _labs_by_encounter(resources["ObsLab"])

    for enc in encs:
        eid = enc["id"]
        own_vitals = vitals_by_enc.get(eid, [])
        if not own_vitals:
            child_vitals: list = []
            for child in enc.get("children", []):
                child_vitals.extend(vitals_by_enc.get(child["id"], []))
            own_vitals = sorted(child_vitals, key=lambda x: x["name"])

        enc_conds = [c for c in conds if c.get("encounterRef") == eid]
        enc_meds = [m for m in meds if m.get("encounterRef") == eid]
        enc_procs = [p for p in procs if p.get("encounterRef") == eid]
        enc_rpts = [r for r in reports if r.get("encounterRef") == eid]
        enc_labs = labs_by_enc.get(eid, [])

        chief_complaint = enc_conds[0]["name"] if enc_conds else None
        providers = [
            prac_lookup[ref]
            for ref in enc.get("participantRefs", [])
            if ref in prac_lookup
        ]

        enc["encounterData"] = {
            "chiefComplaint": chief_complaint,
            "providers": providers,
            "conditions": enc_conds,
            "medications": enc_meds,
            "procedures": enc_procs,
            "diagnosticReports": enc_rpts,
            "vitals": own_vitals,
            "labs": enc_labs,
        }

    chief = "Not recorded"
    if encs and conds:
        recent_id = encs[0]["id"]
        primary = next(
            (c for c in conds if c["encounterRef"] == recent_id),
            conds[0] if conds else None,
        )
        if primary:
            chief = primary["name"]

    pipeline_tags = _bundle_meta_tags(bundle)
    blinded_hadm = _blinded_hadm(bundle)

    return {
        "demographics": demo,
        "vitals": vitals,
        "conditions": conds,
        "medications": meds,
        "labs": labs,
        "diagnosticReports": reports,
        "procedures": procs,
        "encounters": encs,
        "chiefComplaint": chief,
        "pipelineTags": pipeline_tags,
        "blindedHadm": blinded_hadm,
        "resourceCounts": {
            "encounters": len(resources["Encounter"]),
            "conditions": len(resources["Condition"]),
            "observations": len(resources["ObsLab"]) + len(resources["ObsVital"]) + len(resources["ObsOther"]),
            "medications": len(resources["MedicationRequest"]),
            "procedures": len(resources["Procedure"]),
            "diagnosticReports": len(resources["DiagnosticReport"]),
        },
    }


# ── Bundle file caches ────────────────────────────────────────────────────────


@lru_cache(maxsize=20)
def _read_standard_bundle(patient_id: str) -> dict:
    path = STANDARD_BUNDLES_DIR / f"{patient_id}.json"
    if not path.exists():
        raise FileNotFoundError(patient_id)
    with open(path) as f:
        return json.load(f)


@lru_cache(maxsize=20)
def _read_golddata_bundle(patient_id: str) -> dict:
    path = GOLDDATA_BUNDLES_DIR / f"{patient_id}.json"
    if not path.exists():
        raise FileNotFoundError(patient_id)
    with open(path) as f:
        return json.load(f)


# ── Pipeline runner ───────────────────────────────────────────────────────────


def _pipeline_status(name: str) -> dict:
    info = _running_processes.get(name)
    if info is None:
        return {"name": name, "state": "idle", "returncode": None, "log": []}
    proc: subprocess.Popen = info["proc"]
    rc = proc.poll()
    state = "idle" if rc is not None else "running"
    return {
        "name": name,
        "state": state,
        "returncode": rc,
        "started": info["started"],
        "log": info.get("log", []),
    }


def _run_pipeline(name: str, script: str) -> dict:
    existing = _running_processes.get(name)
    if existing and existing["proc"].poll() is None:
        return {"started": False, "reason": f"{name} pipeline is already running"}

    proc = subprocess.Popen(
        [sys.executable, script],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
    )
    _running_processes[name] = {
        "proc": proc,
        "started": datetime.utcnow().isoformat(),
        "log": [],
    }
    return {"started": True, "pid": proc.pid}


# ── API routes ────────────────────────────────────────────────────────────────


@app.get("/api/status")
def api_status():
    std_count = len(list(STANDARD_BUNDLES_DIR.glob("*.json"))) if STANDARD_BUNDLES_DIR.exists() else 0
    gold_count = len(list(GOLDDATA_BUNDLES_DIR.glob("*.json"))) if GOLDDATA_BUNDLES_DIR.exists() else 0
    return {
        "standard_fhir": {
            "dir": str(STANDARD_BUNDLES_DIR),
            "exists": STANDARD_BUNDLES_DIR.exists(),
            "bundleCount": std_count,
        },
        "golddata_fhir": {
            "dir": str(GOLDDATA_BUNDLES_DIR),
            "exists": GOLDDATA_BUNDLES_DIR.exists(),
            "bundleCount": gold_count,
        },
        "pipelines": {
            "standard": _pipeline_status("standard"),
            "golddata": _pipeline_status("golddata"),
        },
    }


@app.get("/api/standard/patients")
def list_standard_patients():
    if not STANDARD_BUNDLES_DIR.exists():
        return {"patients": [], "source": "standard_fhir", "bundleDir": str(STANDARD_BUNDLES_DIR)}
    ids = sorted(p.stem for p in STANDARD_BUNDLES_DIR.glob("*.json"))
    return {"patients": ids, "source": "standard_fhir", "bundleDir": str(STANDARD_BUNDLES_DIR)}


@app.get("/api/standard/patients/{patient_id}")
def get_standard_patient(patient_id: str):
    try:
        bundle = _read_standard_bundle(patient_id)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail=f"Standard patient {patient_id} not found")
    result = parse_bundle(bundle)
    result["source"] = "standard_fhir"
    return result


@app.get("/api/golddata/patients")
def list_golddata_patients():
    if not GOLDDATA_BUNDLES_DIR.exists():
        return {"patients": [], "source": "golddata_fhir", "bundleDir": str(GOLDDATA_BUNDLES_DIR)}
    ids = sorted(p.stem for p in GOLDDATA_BUNDLES_DIR.glob("*.json"))
    return {"patients": ids, "source": "golddata_fhir", "bundleDir": str(GOLDDATA_BUNDLES_DIR)}


@app.get("/api/golddata/patients/{patient_id}")
def get_golddata_patient(patient_id: str):
    try:
        bundle = _read_golddata_bundle(patient_id)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail=f"GoldData patient {patient_id} not found")
    result = parse_bundle(bundle)
    result["source"] = "golddata_fhir"
    return result


@app.get("/api/compare/{patient_id}")
def compare_patient(patient_id: str):
    standard = None
    golddata = None
    standard_error = None
    golddata_error = None

    try:
        bundle = _read_standard_bundle(patient_id)
        standard = parse_bundle(bundle)
        standard["source"] = "standard_fhir"
    except FileNotFoundError:
        standard_error = f"No standard_fhir bundle for patient {patient_id}"
    except Exception as exc:
        standard_error = str(exc)

    try:
        bundle = _read_golddata_bundle(patient_id)
        golddata = parse_bundle(bundle)
        golddata["source"] = "golddata_fhir"
    except FileNotFoundError:
        golddata_error = f"No golddata_fhir bundle for patient {patient_id}"
    except Exception as exc:
        golddata_error = str(exc)

    if standard is None and golddata is None:
        raise HTTPException(
            status_code=404,
            detail=f"Patient {patient_id} not found in either pipeline",
        )

    diff: dict[str, Any] = {}
    if standard and golddata:
        std_conds = {c["code"] for c in standard.get("conditions", []) if c.get("code")}
        gld_conds = {c["code"] for c in golddata.get("conditions", []) if c.get("code")}
        diff["conditionsOnlyInStandard"] = len(std_conds - gld_conds)
        diff["conditionsOnlyInGolddata"] = len(gld_conds - std_conds)
        diff["conditionsInBoth"] = len(std_conds & gld_conds)

        std_rc = standard.get("resourceCounts", {})
        gld_rc = golddata.get("resourceCounts", {})
        diff["resourceCountDiff"] = {
            k: {"standard": std_rc.get(k, 0), "golddata": gld_rc.get(k, 0)}
            for k in set(list(std_rc.keys()) + list(gld_rc.keys()))
        }

    return {
        "patientId": patient_id,
        "standard": standard,
        "golddata": golddata,
        "standardError": standard_error,
        "golddataError": golddata_error,
        "diff": diff,
    }


@app.post("/api/run/standard")
def run_standard_pipeline():
    result = _run_pipeline("standard", "main.py")
    if not result["started"]:
        raise HTTPException(status_code=409, detail=result["reason"])
    _read_standard_bundle.cache_clear()
    return result


@app.post("/api/run/golddata")
def run_golddata_pipeline():
    result = _run_pipeline("golddata", "golddata_fhir_gen.py")
    if not result["started"]:
        raise HTTPException(status_code=409, detail=result["reason"])
    _read_golddata_bundle.cache_clear()
    return result


@app.get("/api/run/status")
def run_status():
    for name, info in _running_processes.items():
        proc = info["proc"]
        if proc.poll() is None and proc.stdout:
            try:
                line = proc.stdout.readline()
                if line:
                    info["log"].append(line.rstrip())
                    if len(info["log"]) > 200:
                        info["log"] = info["log"][-200:]
            except Exception:
                pass
    return {
        "standard": _pipeline_status("standard"),
        "golddata": _pipeline_status("golddata"),
    }


# ── Static files & SPA root ───────────────────────────────────────────────────

if STATIC_DIR.exists():
    app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")


@app.get("/")
def root():
    index = STATIC_DIR / "index.html"
    if not index.exists():
        return JSONResponse(
            {"error": "static_golddata/index.html not found. Run the static file setup."},
            status_code=503,
        )
    return FileResponse(str(index))


@app.get("/favicon.ico", include_in_schema=False)
def favicon():
    svg = Path("static") / "favicon.svg"
    if svg.exists():
        return FileResponse(str(svg), media_type="image/svg+xml")
    raise HTTPException(status_code=404)
