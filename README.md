# MIMIC-IV Clinical Database Platform

A full-stack clinical data platform built on
[MIMIC-IV v3.1](https://physionet.org/content/mimiciv/3.1/) and
[MIMIC-IV-Note v2.2](https://physionet.org/content/mimic-iv-note/2.2/).

It loads de-identified patient records into PostgreSQL, converts them to FHIR R4
transaction bundles, and serves them through three independent web dashboards.

---

## Three Pipelines

| Pipeline | Output dir | Port | Conditions | Medications | Notes | Vitals / Labs |
|---|---|---|:---:|:---:|:---:|:---:|
| `main.py bundle` | `fhir_bundles/` | 8095 | ✅ | ✅ | ✅ | ✅ |
| `main.py golddata` | `golddata_fhir_bundles/` | 8096 | ❌ | ❌ | ❌ | ✅ |
| `main.py testing` | `testing/` | 8097 | ❌ | ❌ | ✅ | ✅ |

**Full** — complete clinical record for every encounter.  
**GoldData** — fully blind: all ICD diagnoses and medications removed from all encounters.  
**Testing** — same blind as GoldData but with discharge summaries and radiology reports included.

---

## Dataset overview

| Module | Tables | Key content |
|---|---|---|
| `hosp` | 22 | Admissions, diagnoses, labs, medications, microbiology, orders, OMR |
| `icu` | 9 | ICU stays, chart events, inputs/outputs, procedure events |
| `note` | 2 | Discharge summaries (`note.discharge`) · Radiology reports (`note.radiology`) |

**Full dataset:** 364K patients · 5.7 GB compressed.

---

## Three independent databases

| Container | Port | DSN env var | Used by |
|---|---|---|---|
| `mimic_pg_standard` | 5433 | `MIMIC_DSN` | `main.py load` + `main.py bundle` |
| `mimic_pg_golddata` | 5434 | `GOLDDATA_DSN` | `main.py load` + `main.py golddata` |
| `mimic_pg_testing` | 5435 | `TESTING_DSN` | `main.py load` + `main.py testing` |

---

## Prerequisites

- Docker + Docker Compose
- Python 3.12+

```bash
pip install psycopg2-binary fastapi "uvicorn[standard]"
```

---

## Quick start — all three pipelines

### 1. Start the containers

```bash
docker compose up -d
docker compose ps    # wait until all three show healthy
```

### 2. Load MIMIC-IV data into each database

Data is read from `dataset/` inside the project (hosp, icu, note subdirectories).
No `--data-dir` or `--note-dir` flags are needed when using the default layout.

```bash
# Standard (port 5433) — reads dataset/ by default
python main.py load

# GoldData (port 5434)
python main.py load \
  --dsn "host=localhost port=5434 dbname=mimiciv user=mimic password=mimic"

# Testing (port 5435)
python main.py load \
  --dsn "host=localhost port=5435 dbname=mimiciv user=mimic password=mimic"
```

To load from a different location, pass `--data-dir` and `--note-dir` explicitly:

```bash
python main.py load \
  --data-dir /path/to/mimiciv/3.1 \
  --note-dir /path/to/mimic-iv-note/2.2/note
```

### 3. Generate FHIR bundles

By default each pipeline selects **20 random patients**. Use `--limit` to change
the count or `--no-random` for sequential ordering.

```bash
python main.py bundle    # → fhir_bundles/          (random 20 patients)
python main.py golddata  # → golddata_fhir_bundles/  (random 20 patients)
python main.py testing   # → testing/                (random 20 patients)
```

### 4. Run the dashboards

```bash
uvicorn web.app:app          --host 0.0.0.0 --port 8095 --reload
uvicorn web.golddata_app:app --host 0.0.0.0 --port 8096 --reload
uvicorn web.testing_app:app  --host 0.0.0.0 --port 8097 --reload
```

---

## CLI reference

```
python main.py <subcommand> [options]

Subcommands:
  load      Load MIMIC-IV CSV.gz files into PostgreSQL
  convert   PostgreSQL → flat FHIR NDJSON (one file per resource type)
  bundle    Full pipeline  → fhir_bundles/
  golddata  Blind pipeline → golddata_fhir_bundles/  (no Dx, no Meds, no Notes)
  testing   Blind + notes  → testing/                (no Dx, no Meds, WITH Notes)

Common batch options (bundle / golddata / testing):
  --dsn              Override PostgreSQL DSN
  --output           Override output directory
  --limit N          Number of patients to process (default: 20 when --random)
  --offset N         Skip the first N patients (only applies with --no-random)
  --subject-ids      Comma-separated list of specific subject IDs
  --random           Random patient sample, default ON  (use --no-random for sequential)

load-specific options:
  --data-dir     Root dir containing hosp/ and icu/ (default: dataset/)
  --note-dir     Note dir containing discharge.csv.gz / radiology.csv.gz (default: dataset/note/)
```

---

## FHIR resource mappings

| MIMIC-IV source | FHIR R4 resource | bundle | golddata | testing |
|---|---|:---:|:---:|:---:|
| `hosp.patients` | `Patient` | ✓ | ✓ | ✓ |
| `hosp.admissions` | `Encounter` (hospital) | ✓ | ✓ | ✓ |
| `icu.icustays` | `Encounter` (ICU) | ✓ | ✓ | ✓ |
| `hosp.diagnoses_icd` | `Condition` | ✓ | **excluded** | **excluded** |
| `hosp.prescriptions` | `MedicationRequest` | ✓ | **excluded** | **excluded** |
| `hosp.procedures_icd` | `Procedure` | ✓ | ✓ | ✓ |
| `hosp.labevents` | `Observation` (laboratory) | ✓ | ✓ | ✓ |
| `icu.chartevents` | `Observation` (vital-signs) | ✓ | ✓ | ✓ |
| `icu.procedureevents` | `Observation` (procedure) | ✓ | ✓ | ✓ |
| `hosp.omr` | `Observation` (survey) | ✓ | ✓ | ✓ |
| `hosp.microbiologyevents` | `DiagnosticReport` + `Observation` | ✓ | ✓ | ✓ |
| `hosp.provider` | `Practitioner` | ✓ | ✓ | ✓ |
| `note.discharge` | `DocumentReference` | ✓ | **excluded** | ✓ |
| `note.radiology` | `DocumentReference` | ✓ | **excluded** | ✓ |

> **Patient cap:** 20 random patients by default — override with `--limit N` or `--no-random`.  
> **Lab cap:** 500 most-recent lab events per patient.  
> **Note cap:** 20 most-recent notes per type (discharge / radiology) per patient.

---

## Dashboard UI — tabs

All three dashboards share the same `static/` UI. A coloured **dataset banner**
at the top identifies which pipeline is active and which resources are included.

| Tab | Contents |
|---|---|
| **Patient Overview** | Demographics · Vitals (colour-coded) · Medications · Past medical history · Tests · Lab table |
| **Chief Complaint** | Primary reason for most recent visit · Admission details · Linked diagnoses |
| **Diagnosis & Treatment** | Ranked ICD conditions · Medications · Procedures performed |
| **Encounters** | Collapsible timeline of all hospital visits with nested ICU stays · per-encounter vitals, labs, notes |
| **Clinical Notes** | Discharge summaries · Radiology reports · Searchable full text |

Conditions and Medications tabs show "No data recorded" for GoldData and Testing bundles — this is correct and expected, not an error.

---

## Output directories

| Directory | Pipeline | Contents |
|---|---|---|
| `fhir_bundles/` | bundle | One JSON per patient — full clinical data |
| `golddata_fhir_bundles/` | golddata | One JSON per patient — no Dx, no Meds, no Notes |
| `testing/` | testing | One JSON per patient — no Dx, no Meds, WITH Notes |
| `fhir_output/` | convert | Flat NDJSON per resource type (optional) |

---

## Environment variables

| Variable | Default | Used by |
|---|---|---|
| `MIMIC_DSN` | `host=localhost port=5433 dbname=mimiciv user=mimic password=mimic` | load, bundle, convert |
| `GOLDDATA_DSN` | `host=localhost port=5434 dbname=mimiciv user=mimic password=mimic` | golddata pipeline |
| `TESTING_DSN` | `host=localhost port=5435 dbname=mimiciv user=mimic password=mimic` | testing pipeline |
| `MIMIC_DATA_DIR` | `dataset/` | load — hosp/ and icu/ parent directory |
| `MIMIC_NOTE_DIR` | `dataset/note/` | load — note CSV directory |
| `GOLDDATA_OUT` | `golddata_fhir_bundles` | golddata output directory |
| `TESTING_OUT` | `testing` | testing output directory |

---

## Project structure

```
.
├── main.py                      # CLI entry point
├── docker-compose.yml           # Three PostgreSQL 16 containers (5433 / 5434 / 5435)
├── pyproject.toml
│
├── etl/
│   ├── load_mimic.py            # CSV.gz → PostgreSQL loader (all three DBs)
│   ├── mimic_to_bundle.py       # Full pipeline — all resources including notes
│   ├── mimic_to_fhir.py         # Flat NDJSON per resource type (optional)
│   ├── golddata_fhir_gen.py     # Blind pipeline — no Dx / no Meds, optional notes
│   ├── golddata_builder.py      # FHIR builders for golddata/testing (isolated UUID namespace)
│   └── testing_gen.py           # Testing pipeline — calls golddata with include_notes=True
│
├── web/
│   ├── parser.py                # Shared FHIR bundle → API response parser
│   ├── app.py                   # Full dashboard      (port 8095, fhir_bundles/)
│   ├── golddata_app.py          # GoldData dashboard  (port 8096, golddata_fhir_bundles/)
│   └── testing_app.py           # Testing dashboard   (port 8097, testing/)
│
├── static/                      # Shared UI (served by all three apps)
│   ├── index.html
│   ├── app.js
│   └── style.css
│
├── sql/
│   └── 01_schema.sql            # DDL for all tables (hosp + icu + note schemas)
│
├── fhir_bundles/                # Full FHIR bundles
├── golddata_fhir_bundles/       # GoldData bundles
├── testing/                     # Testing bundles
└── fhir_output/                 # Flat NDJSON (optional)
```

---

## Stopping / resetting

```bash
# Stop containers (data preserved)
docker compose down

# Full reset — deletes all loaded data
docker compose down -v
```

---

## Data source

This project uses:

- [MIMIC-IV v3.1](https://physionet.org/content/mimiciv/3.1/) — requires PhysioNet credentialing
- [MIMIC-IV-Note v2.2](https://physionet.org/content/mimic-iv-note/2.2/) — requires PhysioNet credentialing
