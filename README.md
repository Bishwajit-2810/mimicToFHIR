# MIMIC-IV Clinical Database Demo v2.2

A full-stack clinical data platform built on the
[MIMIC-IV demo dataset](https://physionet.org/content/mimic-iv-demo/2.2/).
It loads de-identified patient records into PostgreSQL, converts them to FHIR R4,
and serves them through a web-based clinical dashboard.

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

## What's included

### ETL Pipeline (`main.py`)

Loads MIMIC-IV CSV data into PostgreSQL and converts it to FHIR R4.

| Command                  | Output                                                           |
| ------------------------ | ---------------------------------------------------------------- |
| `python main.py load`    | Loads all CSV.gz files into PostgreSQL                           |
| `python main.py bundle`  | One FHIR transaction bundle (JSON) per patient → `fhir_bundles/` |
| `python main.py convert` | Flat NDJSON per resource type → `fhir_output/`                   |

### Clinical Dashboard (`app.py`)

A FastAPI single-page application that reads the pre-built FHIR bundles and
serves a clinical-grade dashboard. **No database required** — works directly
from the `fhir_bundles/` JSON files.

---

## Prerequisites

- Docker + Docker Compose *(only needed for the ETL pipeline)*
- Python 3.12+

```bash
pip install psycopg2-binary fastapi "uvicorn[standard]"
```

---

## Quick start — Clinical Dashboard

`fhir_bundles/` is already populated in this repo. Skip the ETL steps and
start the dashboard directly:

```bash
uvicorn app:app --host 0.0.0.0 --port 8095 --reload
```

Open <http://localhost:8095> in your browser and select a patient from the
dropdown.

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
python main.py bundle    # patient-scoped transaction bundles → fhir_bundles/
python main.py convert   # flat NDJSON per resource type     → fhir_output/
```

### 4. Run the dashboard

```bash
uvicorn app:app --host 0.0.0.0 --port 8095 --reload
```

---

## Dashboard tabs

| Tab                       | Contents                                                                                       |
| ------------------------- | ---------------------------------------------------------------------------------------------- |
| **Patient Overview**      | Demographics · Vitals (colour-coded) · Medications · Past medical history · Tests · Lab values |
| **Chief Complaint**       | Primary reason for most recent visit · Admission details · Associated diagnoses                |
| **Diagnosis & Treatment** | Ranked ICD-coded condition list · Prescribed medications · Procedures performed                |
| **Encounters**            | Collapsible accordion of all hospital encounters, each showing:                                |
|                           | • Chief complaint / reason for that encounter                                                  |
|                           | • Attending provider (de-identified)                                                           |
|                           | • Auto-generated Clinical Summary (diagnoses, meds, labs, procedures, vitals, discharge)       |
|                           | • Full per-encounter data: diagnoses, medications, vitals, labs, procedures, reports           |
|                           | • Nested ICU stays with location, dates, and LOS                                               |

---

## FHIR resource mappings

| MIMIC-IV source           | FHIR R4 resource                   | Notes                                                      |
| ------------------------- | ---------------------------------- | ---------------------------------------------------------- |
| `hosp.patients`           | `Patient`                          | Gender, deceased date, anchor age/year-group as extensions |
| `hosp.admissions`         | `Encounter` (hospital)             | Admission/discharge times, location, race extension        |
| `icu.icustays`            | `Encounter` (ICU)                  | `partOf` hospital encounter, LOS extension                 |
| `hosp.diagnoses_icd`      | `Condition`                        | ICD-9/10 coded, linked to encounter                        |
| `hosp.procedures_icd`     | `Procedure`                        | ICD-9/10 coded, linked to encounter                        |
| `hosp.labevents`          | `Observation` (laboratory)         | Numeric + string values, reference ranges, flags           |
| `icu.chartevents`         | `Observation` (vital-signs)        | Common vitals mapped to LOINC; others use MIMIC item codes |
| `hosp.prescriptions`      | `MedicationRequest`                | NDC code, dose, route, validity period                     |
| `hosp.microbiologyevents` | `DiagnosticReport` + `Observation` | Grouped by specimen; organism and interpretation           |
| `hosp.omr`                | `Observation` (survey)             | Outpatient measurements (BP, BMI, weight, etc.)            |
| `hosp.provider`           | `Practitioner`                     | De-identified provider IDs (e.g. `P60CC5`)                 |

---

## Project structure

```text
.
├── app.py                  # FastAPI clinical dashboard (reads fhir_bundles/)
├── main.py                 # CLI entry point (load / bundle / convert)
├── load_mimic.py           # CSV → PostgreSQL loader
├── mimic_to_bundle.py      # PostgreSQL → FHIR transaction bundles
├── mimic_to_fhir.py        # PostgreSQL → FHIR flat NDJSON
├── docker-compose.yml      # PostgreSQL 16 container
├── pyproject.toml          # Project metadata and dependencies
├── demo_subject_id.csv     # The 100 demo patient IDs
├── sql/
│   └── 01_schema.sql       # DDL for all 31 tables
├── static/
│   ├── index.html          # Single-page dashboard shell
│   ├── app.js              # Vanilla JS — data fetch, render, tab logic
│   └── style.css           # Custom component styles (dark theme)
├── fhir_bundles/           # Pre-built FHIR bundles (100 × patient JSON)
├── fhir_output/            # Flat NDJSON output (generated by convert)
├── hosp/                   # Source CSV.gz files (hosp module)
└── icu/                    # Source CSV.gz files (icu module)
```

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
