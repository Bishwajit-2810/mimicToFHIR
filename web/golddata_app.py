"""
golddata_app.py — GoldData FHIR Dashboard

Serves the blinded ("gold") view on port 8096 using the same static/ UI as app.py.
Both dashboards now read live from the `mimic_pg` Docker PostgreSQL database
instead of pre-generated JSON files:

  Port 8095  →  web.app          full clinical data        (PostgreSQL → bundle live)
  Port 8096  →  web.golddata_app blinded latest encounter  (PostgreSQL → bundle live)

Start:
    uvicorn web.golddata_app:app --host 0.0.0.0 --port 8096 --reload
"""

import json
import subprocess
import sys
from datetime import datetime
from functools import lru_cache
from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles

from etl.golddata_fhir_gen import build_patient_bundle as build_gold_bundle
from etl.mimic_to_bundle import build_patient_bundle as build_full_bundle, _sanitize_for_json
from .db import connect, dict_cursor, list_subject_ids, patient_count
from .parser import parse_bundle, concept_text

app = FastAPI(title="GoldData FHIR Dashboard")

STATIC_DIR = Path("static")

_running: dict[str, dict] = {}

_DATASET_INFO = {
    "mode": "golddata",
    "label": "Gold Data (Blind)",
    "description": "Blind dataset — latest encounter: no diagnoses, no procedures, no medications, no clinical notes",
    "includes": {
        "conditions": False,
        "medications": False,
        "notes": False,
        "vitals": True,
        "labs": True,
        "procedures": False,
        "encounters": True,
    },
    "color": "#f59e0b",
    "icon": "fa-eye-slash",
}


def _blinded_hadm(bundle: dict) -> int | None:
    for ext in bundle.get("meta", {}).get("extension", []):
        if "golddata-blinded-hadm" in ext.get("url", ""):
            return ext.get("valueInteger")
    return None


def _excluded_conditions(std_bundle: dict) -> list[dict]:
    """Return ALL conditions from the standard bundle (gold excludes all, not just latest)."""
    excluded = []
    for entry in std_bundle.get("entry", []):
        r = entry.get("resource", {})
        if r.get("resourceType") != "Condition":
            continue
        code_obj = r.get("code", {})
        icd = next((cd.get("code", "") for cd in code_obj.get("coding", [])), "")
        sys_raw = next((cd.get("system", "") for cd in code_obj.get("coding", [])), "")
        icd_sys = "ICD-10" if "icd-10" in sys_raw else ("ICD-9" if "icd-9" in sys_raw else "")
        excluded.append({"name": concept_text(code_obj), "code": icd, "codeSystem": icd_sys})
    return excluded


def _sanitized(bundle: dict) -> dict:
    """Round-trip a bundle so it matches what the file pipeline would have written."""
    return json.loads(json.dumps(_sanitize_for_json(bundle), default=str))


@lru_cache(maxsize=64)
def _gold_bundle(patient_id: str) -> dict:
    try:
        sid = int(patient_id)
    except ValueError:
        raise FileNotFoundError(patient_id)
    conn = connect()
    try:
        cur = dict_cursor(conn)
        bundle, _ = build_gold_bundle(cur, sid, include_notes=False)
        cur.close()
    finally:
        conn.close()
    if bundle is None:
        raise FileNotFoundError(patient_id)
    return _sanitized(bundle)


@lru_cache(maxsize=64)
def _std_bundle(patient_id: str) -> dict:
    try:
        sid = int(patient_id)
    except ValueError:
        raise FileNotFoundError(patient_id)
    conn = connect()
    try:
        cur = dict_cursor(conn)
        bundle = build_full_bundle(cur, sid)
        cur.close()
    finally:
        conn.close()
    if bundle is None:
        raise FileNotFoundError(patient_id)
    return _sanitized(bundle)


def _pipeline_status(name: str) -> dict:
    info = _running.get(name)
    if info is None:
        return {"name": name, "state": "idle", "returncode": None, "log": []}
    rc = info["proc"].poll()
    state = "idle" if rc is not None else "running"
    return {"name": name, "state": state, "returncode": rc,
            "started": info["started"], "log": info.get("log", [])}


def _run_pipeline(name: str, cmd: list[str]) -> dict:
    existing = _running.get(name)
    if existing and existing["proc"].poll() is None:
        return {"started": False, "reason": f"{name} pipeline already running"}
    proc = subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True,
    )
    _running[name] = {"proc": proc, "started": datetime.utcnow().isoformat(), "log": []}
    return {"started": True, "pid": proc.pid}


@app.get("/api/info")
def api_info():
    try:
        count = patient_count()
    except Exception:
        count = 0
    return {**_DATASET_INFO, "bundleCount": count}


@app.get("/api/patients")
def list_patients():
    try:
        return {"patients": list_subject_ids()}
    except Exception:
        return {"patients": []}


@app.get("/api/patients/{patient_id}")
def get_patient(patient_id: str):
    try:
        bundle = _gold_bundle(patient_id)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail=f"Patient {patient_id} not found")
    result = parse_bundle(bundle)

    result["golddata"] = {
        "blindedHadm": _blinded_hadm(bundle),
        "pipelineTag": "golddata_fhir",
    }
    try:
        result["golddata"]["excludedConditions"] = _excluded_conditions(_std_bundle(patient_id))
    except Exception:
        result["golddata"]["excludedConditions"] = []

    return result


@app.get("/api/status")
def api_status():
    try:
        count = patient_count()
    except Exception:
        count = 0
    return {
        "golddata_fhir": {"source": "postgres", "patientCount": count},
        "standard_fhir": {"source": "postgres", "patientCount": count},
        "pipelines": {
            "standard": _pipeline_status("standard"),
            "golddata": _pipeline_status("golddata"),
        },
    }


@app.post("/api/run/standard")
def run_standard():
    result = _run_pipeline("standard", [sys.executable, "main.py", "bundle"])
    if not result["started"]:
        raise HTTPException(status_code=409, detail=result["reason"])
    return result


@app.post("/api/run/golddata")
def run_golddata():
    result = _run_pipeline("golddata", [sys.executable, "-m", "etl.golddata_fhir_gen"])
    if not result["started"]:
        raise HTTPException(status_code=409, detail=result["reason"])
    return result


@app.get("/api/run/status")
def run_status():
    for name, info in _running.items():
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
    return {"standard": _pipeline_status("standard"), "golddata": _pipeline_status("golddata")}


app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")


@app.get("/")
def root():
    index = STATIC_DIR / "index.html"
    if not index.exists():
        return JSONResponse({"error": "static/index.html not found"}, status_code=503)
    return FileResponse(str(index))


@app.get("/favicon.ico", include_in_schema=False)
def favicon():
    svg = STATIC_DIR / "favicon.svg"
    if svg.exists():
        return FileResponse(str(svg), media_type="image/svg+xml")
    raise HTTPException(status_code=404)
