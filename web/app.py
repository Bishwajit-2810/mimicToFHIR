from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pathlib import Path
from functools import lru_cache
import json

from .parser import parse_bundle

app = FastAPI(title="MIMIC-IV Clinical Dashboard")

BUNDLES_DIR = Path("fhir_bundles")
STATIC_DIR = Path("static")

_DATASET_INFO = {
    "mode": "full",
    "label": "FHIR",
    "description": "Complete clinical record — diagnoses, medications, notes, vitals, labs",
    "includes": {
        "conditions": True,
        "medications": True,
        "notes": True,
        "vitals": True,
        "labs": True,
        "procedures": True,
        "encounters": True,
    },
    "color": "#3b82f6",
    "icon": "fa-hospital-user",
}


@lru_cache(maxsize=15)
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
    ids = sorted(p.stem for p in BUNDLES_DIR.glob("*.json"))
    return {"patients": ids}


@app.get("/api/patients/{patient_id}")
def get_patient(patient_id: str):
    try:
        bundle = _read_bundle(patient_id)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail=f"Patient {patient_id} not found")
    return parse_bundle(bundle)


app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")


@app.get("/")
def root():
    return FileResponse(str(STATIC_DIR / "index.html"))


@app.get("/favicon.ico", include_in_schema=False)
def favicon():
    return FileResponse(str(STATIC_DIR / "favicon.svg"), media_type="image/svg+xml")
