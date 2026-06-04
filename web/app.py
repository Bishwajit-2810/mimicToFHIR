from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pathlib import Path
from functools import lru_cache
import json

from etl.mimic_to_bundle import build_patient_bundle, _sanitize_for_json
from .db import connect, dict_cursor, list_subject_ids, patient_count
from .parser import parse_bundle

app = FastAPI(title="MIMIC-IV Clinical Dashboard")

STATIC_DIR = Path("static")

_DATASET_INFO = {
    "mode": "full",
    "label": "Full Clinical Data",
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


@lru_cache(maxsize=64)
def _patient_data(patient_id: str) -> dict:
    """Build a patient's full FHIR bundle live from PostgreSQL and parse it.

    The in-memory bundle is round-tripped through ``_sanitize_for_json`` +
    ``json`` so it is byte-for-byte what the file pipeline would have written,
    guaranteeing the UI sees identical data.
    """
    try:
        sid = int(patient_id)
    except ValueError:
        raise FileNotFoundError(patient_id)

    conn = connect()
    try:
        cur = dict_cursor(conn)
        bundle = build_patient_bundle(cur, sid)
        cur.close()
    finally:
        conn.close()

    if bundle is None:
        raise FileNotFoundError(patient_id)

    bundle = json.loads(json.dumps(_sanitize_for_json(bundle), default=str))
    return parse_bundle(bundle)


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
        return _patient_data(patient_id)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail=f"Patient {patient_id} not found")


app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")


@app.get("/")
def root():
    return FileResponse(str(STATIC_DIR / "index.html"))


@app.get("/favicon.ico", include_in_schema=False)
def favicon():
    return FileResponse(str(STATIC_DIR / "favicon.svg"), media_type="image/svg+xml")
