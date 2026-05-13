# MIMIC-IV Clinical Database Demo v2.2

A full-stack clinical data platform built on the
[MIMIC-IV demo dataset](https://physionet.org/content/mimic-iv-demo/2.2/).
It loads de-identified patient records into PostgreSQL, converts them to FHIR R4,
and serves them through two independent web dashboards.

> **Note on clinical notes:** The MIMIC-IV demo dataset explicitly excludes
> free-text clinical notes. The dashboard synthesizes a structured "Clinical
> Summary" per encounter from coded FHIR data (diagnoses, medications, labs,
> procedures, vitals) instead.

---

## Dataset overview

| Module | Tables | Key content                                                    |
| ------ | ------ | -------------------------------------------------------------- |
| `hosp` | 22     | Admissions, diagnoses, labs, medications, microbiology, orders |
| `icu`  | 9      | ICU stays, chart events, inputs/outputs, procedures            |

**Demo size:** 100 patients · 275 admissions · 140 ICU stays · ~1.4 M rows total.

---

## Pipelines

This project contains two fully independent FHIR generation pipelines.
They share the same PostgreSQL source but produce separate output directories,
use different UUID namespaces, and run on separate ports.

### `standard_fhir` pipeline

Generates complete FHIR R4 bundles — all resources included for all encounters.

| Command                  | Output                                                           |
| ------------------------ | ---------------------------------------------------------------- |
| `python main.py load`    | Loads all CSV.gz files into PostgreSQL                           |
| `python main.py bundle`  | One FHIR transaction bundle per patient → `fhir_bundles/`        |
| `python main.py convert` | Flat NDJSON per resource type → `fhir_output/`                   |

Dashboard: `app.py` → <http://localhost:8095>

### `golddata_fhir` pipeline

Generates diagnosis-blind FHIR R4 bundles suitable for model evaluation and
clinical decision support benchmarking. For each patient's **latest (most
recent) encounter**, the following are intentionally withheld:

- `Condition` resources (ICD diagnoses)
- Discharge disposition from the `Encounter` resource

Everything else is included for **all encounters** — vitals, labs, ICU
chartevents, ICU procedure events, medications administered, ICD-coded
procedures performed, and microbiology reports.

Historical (non-latest) encounters retain their complete data including diagnoses.

| Command                         | Output                                                                 |
| ------------------------------- | ---------------------------------------------------------------------- |
| `python golddata_fhir_gen.py`   | One golddata bundle per patient → `golddata_fhir_bundles/`             |
| `python golddata_fhir_gen.py --patient <id>` | Single-patient test run                               |

Dashboard: `golddata_app.py` → <http://localhost:8096>

---

## Prerequisites

- Docker + Docker Compose *(only needed for the ETL pipeline)*
- Python 3.12+

```bash
pip install psycopg2-binary fastapi "uvicorn[standard]"
```

---

## Quick start — Standard Dashboard

`fhir_bundles/` is already populated in this repo. Skip the ETL steps and
start the dashboard directly:

```bash
uvicorn app:app --host 0.0.0.0 --port 8095 --reload
```

Open <http://localhost:8095> and select a patient from the dropdown.

---

## Quick start — GoldData Dashboard

After running `python golddata_fhir_gen.py` (requires PostgreSQL):

```bash
uvicorn golddata_app:app --host 0.0.0.0 --port 8096 --reload
```

Open <http://localhost:8096> to access the GoldData FHIR Dashboard with three
view modes: **GoldData**, **Standard**, and **Compare**.

---

## Quick start — Full ETL Pipeline

### 1. Start PostgreSQL

```bash
docker compose up -d
```

Starts a PostgreSQL 16 container on **port 5433**.

| Setting  | Value     |
| -------- | --------- |
| Host     | localhost |
| Port     | 5433      |
| Database | mimiciv   |
| User     | mimic     |
| Password | mimic     |

### 2. Load the data

```bash
python main.py load
```

Streams all gzipped CSVs into PostgreSQL via `COPY`. Takes ~30 seconds.

### 3. Generate FHIR bundles

```bash
# Standard pipeline
python main.py bundle    # → fhir_bundles/
python main.py convert   # → fhir_output/  (optional flat NDJSON)

# GoldData pipeline
python golddata_fhir_gen.py   # → golddata_fhir_bundles/
```

### 4. Run the dashboards

```bash
# Standard dashboard (port 8095) — existing, unchanged
uvicorn app:app --host 0.0.0.0 --port 8095 --reload

# GoldData dashboard (port 8096) — new, isolated
uvicorn golddata_app:app --host 0.0.0.0 --port 8096 --reload
```

Both dashboards can run simultaneously.

---

## Standard dashboard tabs (`app.py`, port 8095)

| Tab                       | Contents                                                                                       |
| ------------------------- | ---------------------------------------------------------------------------------------------- |
| **Patient Overview**      | Demographics · Vitals (colour-coded) · Medications · Past medical history · Tests · Lab values |
| **Chief Complaint**       | Primary reason for most recent visit · Admission details · Associated diagnoses                |
| **Diagnosis & Treatment** | Ranked ICD-coded condition list · Prescribed medications · Procedures performed                |
| **Encounters**            | Collapsible accordion of all hospital encounters with nested ICU stays                         |

## GoldData dashboard tabs (`golddata_app.py`, port 8096)

| Mode / Tab              | Contents                                                                                      |
| ----------------------- | --------------------------------------------------------------------------------------------- |
| **GoldData mode**       | Diagnosis-blind view — clearly labelled; shows blinded encounter `hadm_id`                    |
| → Overview              | Demographics · Exclusion summary card · Latest vitals · Medications · Historical conditions   |
| → Vitals & Labs         | Full vital sign grid · Complete lab table with filter                                         |
| → Meds & Procedures     | All medications administered · All procedures performed                                       |
| → Encounters            | All encounters; latest is flagged `dx-blind` with amber border                                |
| **Standard mode**       | Full `standard_fhir` data — all diagnoses included                                            |
| → Overview / Diagnoses / Vitals & Labs / Encounters | Standard clinical view                                |
| **Compare mode**        | Side-by-side summary · Condition diff (excluded vs shared) · Vitals comparison                |
| Pipeline status bar     | Bundle counts · Run buttons · Live log for both pipelines                                     |

---

## FHIR resource mappings

Both pipelines produce the same resource types. The golddata pipeline adds
`meta.tag: golddata_fhir` to every resource and embeds the blinded `hadm_id`
in `Bundle.meta.extension`.

| MIMIC-IV source           | FHIR R4 resource                   | standard_fhir | golddata_fhir (latest enc) |
| ------------------------- | ---------------------------------- | :-----------: | :------------------------: |
| `hosp.patients`           | `Patient`                          | ✓             | ✓ + blinded-encounter ext  |
| `hosp.admissions`         | `Encounter` (hospital)             | ✓             | ✓ (no discharge dispo)     |
| `icu.icustays`            | `Encounter` (ICU)                  | ✓             | ✓                          |
| `hosp.diagnoses_icd`      | `Condition`                        | ✓             | **excluded** for latest    |
| `hosp.procedures_icd`     | `Procedure`                        | ✓             | ✓                          |
| `hosp.labevents`          | `Observation` (laboratory)         | ✓             | ✓                          |
| `icu.chartevents`         | `Observation` (vital-signs)        | ✓             | ✓                          |
| `icu.procedureevents`     | `Observation` (procedure)          | —             | ✓ (ICU procedure events)   |
| `hosp.prescriptions`      | `MedicationRequest`                | ✓             | ✓                          |
| `hosp.microbiologyevents` | `DiagnosticReport` + `Observation` | ✓             | ✓                          |
| `hosp.omr`                | `Observation` (survey)             | ✓             | ✓                          |
| `hosp.provider`           | `Practitioner`                     | ✓             | ✓                          |

---

## Output directories

| Directory                  | Pipeline       | Contents                                   |
| -------------------------- | -------------- | ------------------------------------------ |
| `fhir_bundles/`            | standard_fhir  | 100 × patient JSON (full data)             |
| `fhir_output/`             | standard_fhir  | Flat NDJSON per resource type (optional)   |
| `golddata_fhir_bundles/`   | golddata_fhir  | 100 × patient JSON (diagnosis-blind)       |

---

## Project structure

```text
.
├── app.py                      # Standard dashboard (port 8095, reads fhir_bundles/)
├── main.py                     # Standard pipeline CLI (load / bundle / convert)
├── load_mimic.py               # CSV → PostgreSQL loader
├── mimic_to_bundle.py          # PostgreSQL → standard_fhir transaction bundles
├── mimic_to_fhir.py            # PostgreSQL → standard_fhir flat NDJSON
│
├── golddata_app.py             # GoldData dashboard (port 8096)
├── golddata_fhir_gen.py        # GoldData pipeline CLI
├── golddata_bundle_builder.py  # GoldData FHIR resource builders (isolated)
│
├── docker-compose.yml          # PostgreSQL 16 container
├── pyproject.toml              # Project metadata and dependencies
├── demo_subject_id.csv         # The 100 demo patient IDs
├── sql/
│   └── 01_schema.sql           # DDL for all 31 tables
├── static/                     # Standard dashboard UI (unchanged)
│   ├── index.html
│   ├── app.js
│   └── style.css
├── static_golddata/            # GoldData dashboard UI (new)
│   ├── index.html
│   ├── golddata_app.js
│   └── style.css
├── fhir_bundles/               # standard_fhir bundles (100 × patient JSON)
├── golddata_fhir_bundles/      # golddata_fhir bundles (100 × patient JSON)
├── fhir_output/                # Flat NDJSON (standard_fhir, optional)
├── hosp/                       # Source CSV.gz files (hosp module)
└── icu/                        # Source CSV.gz files (icu module)
```

---

## Environment variables

| Variable       | Used by                    | Default                                       |
| -------------- | -------------------------- | --------------------------------------------- |
| `MIMIC_DSN`    | standard pipeline          | `host=localhost port=5433 dbname=mimiciv ...` |
| `GOLDDATA_DSN` | golddata pipeline (primary)| falls back to `MIMIC_DSN` then built-in       |
| `GOLDDATA_OUT` | golddata pipeline          | `golddata_fhir_bundles`                       |

---

## Useful SQL queries

```sql
-- Patients with ICU stays
SELECT p.subject_id, p.gender, p.anchor_age, i.first_careunit, i.los
FROM hosp.patients p
JOIN icu.icustays i USING (subject_id)
ORDER BY i.los DESC;

-- Top diagnoses
SELECT i.long_title, count(*) AS n
FROM hosp.diagnoses_icd d
JOIN hosp.d_icd_diagnoses i USING (icd_code, icd_version)
GROUP BY i.long_title
ORDER BY n DESC
LIMIT 10;

-- Abnormal lab results
SELECT d.label, l.value, l.valueuom, l.flag
FROM hosp.labevents l
JOIN hosp.d_labitems d USING (itemid)
WHERE l.flag IS NOT NULL
LIMIT 20;

-- Latest encounter per patient (golddata blinded encounter)
SELECT subject_id, hadm_id, admittime
FROM hosp.admissions a
WHERE admittime = (
  SELECT MAX(admittime) FROM hosp.admissions WHERE subject_id = a.subject_id
)
ORDER BY subject_id;
```

---

## Stopping / resetting

```bash
# Stop container (data persists in Docker volume)
docker compose down

# Stop and delete all data
docker compose down -v
```

---

## Data source

This project uses the MIMIC-IV Clinical Database Demo v2.2 from PhysioNet:
<https://doi.org/10.13026/07hj-2a80>

Access to the full MIMIC-IV dataset requires credentialing. The demo subset
(100 patients) is openly available.
