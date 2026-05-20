"""
testing_app.py — Testing FHIR Dashboard

Serves testing/ bundles on port 8097.
Bundles contain: encounters, vitals, labs, procedures, microbiology, OMR, clinical notes.
Bundles EXCLUDE: Condition (diagnoses), MedicationRequest (treatments).

  Port 8095 → web.app          fhir_bundles/          (full clinical data)
  Port 8096 → web.golddata_app golddata_fhir_bundles/  (blind: no Dx/Tx/notes)
  Port 8097 → web.testing_app  testing/               (blind + notes)

Start:
    uvicorn web.testing_app:app --host 0.0.0.0 --port 8097 --reload
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

from .parser import parse_bundle

app = FastAPI(title="Testing FHIR Dashboard")

BUNDLES_DIR = Path("testing")
STATIC_DIR = Path("static")

_DATASET_INFO = {
    "mode": "testing",
    "label": "Testing",
    "description": "Blind dataset with clinical notes — latest encounter: no diagnoses, no procedures, no medications",
    "includes": {
        "conditions": False,
        "medications": False,
        "notes": True,
        "vitals": True,
        "labs": True,
        "procedures": False,
        "encounters": True,
    },
    "color": "#34d399",
    "icon": "fa-flask",
}


_running: dict[str, dict] = {}


def _run_testing() -> dict:
    info = _running.get("testing")
    if info and info["proc"].poll() is None:
        return {"started": False, "reason": "testing pipeline already running"}
    proc = subprocess.Popen(
        [sys.executable, "-m", "etl.testing_gen"],
        stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True,
    )
    _running["testing"] = {"proc": proc, "started": datetime.utcnow().isoformat(), "log": []}
    return {"started": True, "pid": proc.pid}


def _pipeline_status() -> dict:
    info = _running.get("testing")
    if info is None:
        return {"name": "testing", "state": "idle", "returncode": None, "log": []}
    rc = info["proc"].poll()
    return {
        "name": "testing",
        "state": "idle" if rc is not None else "running",
        "returncode": rc,
        "started": info["started"],
        "log": info.get("log", []),
    }


@lru_cache(maxsize=20)
def _read_bundle(patient_id: str) -> dict:
    path = BUNDLES_DIR / f"{patient_id}.json"
    if not path.exists():
        raise FileNotFoundError(patient_id)
    with open(path) as f:
        return json.load(f)


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
    return parse_bundle(bundle)


@app.post("/api/run/testing")
def run_testing():
    result = _run_testing()
    if not result["started"]:
        raise HTTPException(status_code=409, detail=result["reason"])
    _read_bundle.cache_clear()
    return result


@app.get("/api/run/status")
def run_status():
    info = _running.get("testing")
    if info and info["proc"].poll() is None and info["proc"].stdout:
        try:
            line = info["proc"].stdout.readline()
            if line:
                info["log"].append(line.rstrip())
                if len(info["log"]) > 200:
                    info["log"] = info["log"][-200:]
        except Exception:
            pass
    return _pipeline_status()


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
