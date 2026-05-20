"""
golddata_app.py — GoldData FHIR Dashboard

Serves golddata_fhir_bundles/ on port 8096 using the same static/ UI as app.py.

  Port 8095  →  web.app          reads fhir_bundles/          (full clinical data)
  Port 8096  →  web.golddata_app reads golddata_fhir_bundles/ (all diagnoses & medications excluded)

Start:
    uvicorn web.golddata_app:app --host 0.0.0.0 --port 8096 --reload
"""

import json
import subprocess
import sys
import uuid
from datetime import datetime
from functools import lru_cache
from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles

from .parser import parse_bundle, concept_text

app = FastAPI(title="GoldData FHIR Dashboard")

BUNDLES_DIR = Path("golddata_fhir_bundles")
STD_BUNDLES_DIR = Path("fhir_bundles")
STATIC_DIR = Path("static")

_STD_NS = uuid.UUID("6ba7b810-9dad-11d1-80b4-00c04fd430c8")

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


@lru_cache(maxsize=20)
def _read_bundle(patient_id: str) -> dict:
    path = BUNDLES_DIR / f"{patient_id}.json"
    if not path.exists():
        raise FileNotFoundError(patient_id)
    with open(path) as f:
        return json.load(f)


@lru_cache(maxsize=20)
def _read_std_bundle(patient_id: str) -> dict:
    path = STD_BUNDLES_DIR / f"{patient_id}.json"
    if not path.exists():
        raise FileNotFoundError(patient_id)
    with open(path) as f:
        return json.load(f)


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
    count = len(list(BUNDLES_DIR.glob("*.json"))) if BUNDLES_DIR.exists() else 0
    return {**_DATASET_INFO, "bundleCount": count}


@app.get("/api/patients")
def list_patients():
    if not BUNDLES_DIR.exists():
        return {"patients": []}
    return {"patients": sorted(p.stem for p in BUNDLES_DIR.glob("*.json"))}


@app.get("/api/patients/{patient_id}")
def get_patient(patient_id: str):
    try:
        bundle = _read_bundle(patient_id)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail=f"Patient {patient_id} not found")
    result = parse_bundle(bundle)

    hadm = _blinded_hadm(bundle)
    result["golddata"] = {
        "blindedHadm": hadm,
        "pipelineTag": "golddata_fhir",
    }
    try:
        std = _read_std_bundle(patient_id)
        result["golddata"]["excludedConditions"] = _excluded_conditions(std)
    except Exception:
        result["golddata"]["excludedConditions"] = []

    return result


@app.get("/api/status")
def api_status():
    gd_count = len(list(BUNDLES_DIR.glob("*.json"))) if BUNDLES_DIR.exists() else 0
    std_count = len(list(STD_BUNDLES_DIR.glob("*.json"))) if STD_BUNDLES_DIR.exists() else 0
    return {
        "golddata_fhir": {"dir": str(BUNDLES_DIR), "bundleCount": gd_count},
        "standard_fhir": {"dir": str(STD_BUNDLES_DIR), "bundleCount": std_count},
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
