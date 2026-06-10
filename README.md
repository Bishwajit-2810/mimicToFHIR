# MIMIC-IV Clinical Database Platform

A full-stack clinical data platform built on
[MIMIC-IV v3.1](https://physionet.org/content/mimiciv/3.1/) and
[MIMIC-IV-Note v2.2](https://physionet.org/content/mimic-iv-note/2.2/).

Loads de-identified patient records into PostgreSQL, converts them to FHIR R4
transaction bundles, and serves them through two independent web dashboards.

---

## Two Pipelines

| Pipeline           | Output dir               | Port |      Conditions      |      Procedures      |     Medications      |        Notes         | Vitals / Labs |
| ------------------ | ------------------------ | ---- | :------------------: | :------------------: | :------------------: | :------------------: | :-----------: |
| `main.py bundle`   | `golddata_fhir_bundles/`          | 8095 |        ✅ all        |        ✅ all        |        ✅ all        |        ✅ all        |      ✅       |
| `main.py golddata` | `fhir_bundles/` | 8096 | prior ✅ + latest ❌ | prior ✅ + latest ❌ | prior ✅ + latest ❌ | prior ✅ + latest ❌ |      ✅       |

**Gold Data** — complete clinical record for every encounter, no blinding.  
**FHIR (Blind)** — latest hospital encounter and latest ED stay are blinded: ICD diagnoses, procedures, medications, and notes removed from the most recent visit only. All prior encounters remain intact.

---

## Dataset Overview

| Module | Tables | Key content                                                                          |
| ------ | ------ | ------------------------------------------------------------------------------------ |
| `hosp` | 22     | Admissions, diagnoses, labs, medications, microbiology, orders, OMR                  |
| `icu`  | 9      | ICU stays, chart events, inputs/outputs, datetime events, procedure events           |
| `ed`   | 6      | ED stays, triage, vital signs, diagnoses, medication reconciliation, Pyxis dispenses |
| `note` | 4      | Discharge summaries + detail · Radiology reports + detail                            |

**Full dataset:** 364K patients · 5.7 GB compressed · ~50 GB uncompressed.  
**Demo dataset:** 100 patients · included in `dataset/`.

### Dataset Directory Layout

```text
dataset/
├── ed/
│   ├── diagnosis.csv.gz
│   ├── edstays.csv.gz
│   ├── medrecon.csv.gz
│   ├── pyxis.csv.gz
│   ├── triage.csv.gz
│   └── vitalsign.csv.gz
├── hosp/
│   ├── admissions.csv.gz
│   ├── d_hcpcs.csv.gz
│   ├── d_icd_diagnoses.csv.gz
│   ├── d_icd_procedures.csv.gz
│   ├── d_labitems.csv.gz
│   ├── diagnoses_icd.csv.gz
│   ├── drgcodes.csv.gz
│   ├── emar.csv.gz
│   ├── emar_detail.csv.gz
│   ├── hcpcsevents.csv.gz
│   ├── labevents.csv.gz
│   ├── microbiologyevents.csv.gz
│   ├── omr.csv.gz
│   ├── patients.csv.gz
│   ├── pharmacy.csv.gz
│   ├── poe.csv.gz
│   ├── poe_detail.csv.gz
│   ├── prescriptions.csv.gz
│   ├── procedures_icd.csv.gz
│   ├── provider.csv.gz
│   ├── services.csv.gz
│   └── transfers.csv.gz
├── icu/
│   ├── caregiver.csv.gz
│   ├── chartevents.csv.gz
│   ├── d_items.csv.gz
│   ├── datetimeevents.csv.gz
│   ├── icustays.csv.gz
│   ├── ingredientevents.csv.gz
│   ├── inputevents.csv.gz
│   ├── outputevents.csv.gz
│   └── procedureevents.csv.gz
└── note/
    ├── discharge.csv.gz
    ├── discharge_detail.csv.gz
    ├── radiology.csv.gz
    └── radiology_detail.csv.gz
```

---

## Single Database

Both pipelines share one PostgreSQL container. Load data once.

| Container  | Port | Default DSN                                                         |
| ---------- | ---- | ------------------------------------------------------------------- |
| `mimic_pg` | 5433 | `host=localhost port=5433 dbname=mimiciv user=mimic password=mimic` |

---

## Prerequisites

- Docker + Docker Compose
- Python 3.12+

```bash
pip install psycopg2-binary fastapi "uvicorn[standard]"
```

---

## Quick Start — Both Pipelines

### 1. Start the container

```bash
docker compose up -d
docker compose ps    # wait until healthy
```

### 2. Load MIMIC-IV data

Reads `dataset/` by default (hosp/, icu/, ed/, note/ subdirectories).

```bash
python main.py load
```

To load from a custom path:

```bash
python main.py load \
  --data-dir /path/to/mimiciv \
  --note-dir /path/to/mimic-iv-note/note
```

### 3. Create indexes (run once after loading)

Required for acceptable query performance — especially important for the full
dataset where `icu.chartevents` has 432 million rows.

```bash
python main.py reindex
```

### 4. Generate FHIR bundles

```bash
# Both pipelines on the same 100 random patients (recommended)
python main.py all

# Or individually (100 random patients each by default)
python main.py bundle    # → golddata_fhir_bundles/
python main.py golddata  # → fhir_bundles/

# Extract a filtered cohort into its own folder under filtered/
python main.py all --gender male --service medicine
#   → filtered/gender-male_service-med/{fhir,golddata}/
```

### 5. Run the dashboards

```bash
uvicorn web.app:app          --host 0.0.0.0 --port 8095 --reload
uvicorn web.golddata_app:app --host 0.0.0.0 --port 8096 --reload
```

---

## CLI Reference

See [ARGUMENTS.md](ARGUMENTS.md) for the full argument reference and run recipes.

```
python main.py <subcommand> [options]

Subcommands:
  load      Load MIMIC-IV CSV.gz files into PostgreSQL
  reindex   Create subject_id indexes after loading (run once — makes queries fast)
  convert   PostgreSQL → flat FHIR NDJSON (one file per resource type)
  bundle    Gold Data pipeline → golddata_fhir_bundles/
  golddata  Blind pipeline → fhir_bundles/  (latest encounter: no Dx/Meds/Notes)
  all       Run both on the same random patients (recommended)

Common batch options (bundle / golddata / all):
  --dsn              Override PostgreSQL DSN
  --output           Override output directory
  --limit N          Number of patients (default: 100)
  --offset N         Skip first N patients (sequential mode only)
  --subject-ids      Comma-separated list of specific subject IDs
  --random           Random patient sample, default ON (use --no-random for sequential)

Cohort filters (bundle / golddata / all) — extract a subset into filtered/<slug>/:
  --gender male|female      hosp.patients.gender
  --min-age / --max-age     hosp.patients.anchor_age (inclusive range)
  --anchor-year YYYY        hosp.patients.anchor_year (exact)
  --anchor-year-group TEXT  hosp.patients.anchor_year_group (substring)
  --deceased                patients with a recorded date of death
  --race TEXT               hosp.admissions.race (substring)
  --ethnicity TEXT          hosp.admissions.race (substring, e.g. hispanic)
  --language TEXT           hosp.admissions.language (substring)
  --marital-status TEXT     hosp.admissions.marital_status (substring)
  --service CODE|name       hosp.services.curr_service (MED or "medicine")
  --admission-type TEXT     hosp.admissions.admission_type (substring)
  --admit-source TEXT       hosp.admissions.admission_location (substring)
  --discharge-location TEXT hosp.admissions.discharge_location (substring)
  --insurance TEXT          hosp.admissions.insurance (substring)
  --expired                 patients with an in-hospital death
  (filters combine with AND; output → filtered/<slug>/, e.g. filtered/gender-male_service-med/)

load-specific options:
  --data-dir     Root dir containing hosp/, icu/, ed/ (default: dataset/)
  --note-dir     Note dir with discharge.csv.gz / radiology.csv.gz (default: dataset/note/)
  --tables       Comma-separated table names to reload only (e.g. prescriptions,emar)
```

---

## FHIR Resource Mappings

| MIMIC-IV source                       | FHIR R4 resource                   | bundle |      golddata      |
| ------------------------------------- | ---------------------------------- | :----: | :----------------: |
| `hosp.patients`                       | `Patient`                          |   ✓    |         ✓          |
| `hosp.admissions`                     | `Encounter` (hospital)             |   ✓    |         ✓          |
| `icu.icustays`                        | `Encounter` (ICU)                  |   ✓    |         ✓          |
| `ed.edstays`                          | `Encounter` (ED)                   |   ✓    |         ✓          |
| `hosp.diagnoses_icd`                  | `Condition` (hospital)             |   ✓    | prior ✓ + latest ✗ |
| `ed.diagnosis`                        | `Condition` (ED)                   |   ✓    | prior ✓ + latest ✗ |
| `hosp.prescriptions`                  | `MedicationRequest`                |   ✓    | prior ✓ + latest ✗ |
| `ed.medrecon`                         | `MedicationStatement` (ED)         |   ✓    | prior ✓ + latest ✗ |
| `ed.pyxis`                            | `MedicationDispense` (ED)          |   ✓    | prior ✓ + latest ✗ |
| `icu.inputevents`                     | `MedicationAdministration` (ICU)   |   ✓    | prior ✓ + latest ✗ |
| `icu.ingredientevents`                | `MedicationAdministration` (ICU)   |   ✓    | prior ✓ + latest ✗ |
| `hosp.procedures_icd`                 | `Procedure`                        |   ✓    | prior ✓ + latest ✗ |
| `hosp.labevents`                      | `Observation` (laboratory)         |   ✓    |         ✓          |
| `icu.chartevents`                     | `Observation` (vital-signs)        |   ✓    |         ✓          |
| `icu.procedureevents`                 | `Observation` (ICU procedure)      |   ✓    |         ✓          |
| `icu.datetimeevents`                  | `Observation` (ICU datetime)       |   ✓    |         ✓          |
| `icu.outputevents`                    | `Observation` (ICU output)         |   ✓    |         ✓          |
| `hosp.omr`                            | `Observation` (survey)             |   ✓    |         ✓          |
| `ed.triage`                           | `Observation` (ED triage)          |   ✓    |         ✓          |
| `ed.vitalsign`                        | `Observation` (ED vitals)          |   ✓    |         ✓          |
| `hosp.microbiologyevents`             | `DiagnosticReport` + `Observation` |   ✓    |         ✓          |
| `hosp.drgcodes`                       | `Claim` + `ExplanationOfBenefit`   |   ✓    |         ✓          |
| `hosp.provider`                       | `Practitioner`                     |   ✓    |         ✓          |
| `icu.caregivers`                      | `Practitioner` (ICU)               |   ✓    |         ✓          |
| `note.discharge` + `discharge_detail` | `DocumentReference` (discharge)    |   ✓    | prior ✓ + latest ✗ |
| `note.radiology` + `radiology_detail` | `DocumentReference` (radiology)    |   ✓    | prior ✓ + latest ✗ |

> **"latest" blinding** applies to the most recent hospital admission (`latest_hadm`) and
> the most recent ED stay (`latest_ed_stay`). All prior encounters are always included.  
> **Lab cap:** 500 most-recent lab events per patient.  
> **Note cap:** 20 most-recent notes per type (discharge + radiology) per patient.
>
> **Per-patient caps** (apply to both `bundle` and `golddata` pipelines):
>
> | Resource                                            | Cap  |
> | --------------------------------------------------- | ---- |
> | `hosp.labevents` → `Observation`                    | 500  |
> | `icu.chartevents` (vitals) → `Observation`          | 2000 |
> | `icu.procedureevents` → `Observation`               | 500  |
> | `icu.datetimeevents` → `Observation`                | 500  |
> | `icu.outputevents` → `Observation`                  | 500  |
> | `icu.inputevents` → `MedicationAdministration`      | 2000 |
> | `icu.ingredientevents` → `MedicationAdministration` | 2000 |
> | `note.discharge` → `DocumentReference`              | 20   |
> | `note.radiology` → `DocumentReference`              | 20   |
>
> Each cap selects the most-recent rows per patient (ORDER BY time DESC LIMIT N).
> Caps keep bundle size manageable on the full dataset where `icu.chartevents`
> alone has 432 M rows.

---

## Dashboard UI — Tabs

Both dashboards share the same `static/` UI. A coloured dataset banner at
the top identifies which pipeline is active and which resources are included.

| Tab                       | Contents                                                                                      |
| ------------------------- | --------------------------------------------------------------------------------------------- |
| **Patient Overview**      | Demographics · Vitals (colour-coded) · Medications · Past medical history · Tests · Lab table |
| **Chief Complaint**       | Primary reason for most recent visit · Admission details · Linked diagnoses                   |
| **Diagnosis & Treatment** | Ranked ICD conditions · Medications · Procedures performed                                    |
| **Encounters**            | Collapsible timeline of all hospital + ICU + ED visits · per-encounter vitals, labs, notes    |
| **Clinical Notes**        | Discharge summaries · Radiology reports · Searchable full text                                |

Conditions and Medications sections show "No data recorded" for the latest
encounter on FHIR (Blind) bundles — this is correct and expected.

---

## Output Directories

| Directory                | Pipeline | Contents                                               |
| ------------------------ | -------- | ------------------------------------------------------ |
| `golddata_fhir_bundles/`          | bundle   | One JSON per patient — full clinical data, no blinding |
| `fhir_bundles/` | golddata | One JSON per patient — latest encounter blinded        |
| `fhir_output/`           | convert  | Flat NDJSON per resource type (optional)               |
| `filtered/<slug>/`       | filtered | Cohort extract — `fhir/` + `golddata/` subfolders      |

---

## Environment Variables

| Variable         | Default                                                             | Used by                                  |
| ---------------- | ------------------------------------------------------------------- | ---------------------------------------- |
| `MIMIC_DSN`      | `host=localhost port=5433 dbname=mimiciv user=mimic password=mimic` | all pipelines                            |
| `MIMIC_DATA_DIR` | `dataset/`                                                          | load — hosp/, icu/, ed/ parent directory |
| `MIMIC_NOTE_DIR` | `dataset/note/`                                                     | load — note CSV directory                |
| `GOLDDATA_OUT`   | `fhir_bundles`                                             | golddata output directory                |

---

## Project Structure

```
.
├── main.py                      # CLI entry point
├── docker-compose.yml           # Single PostgreSQL 16 container (port 5433, perf-tuned)
├── pyproject.toml
│
├── etl/
│   ├── load_mimic.py            # CSV.gz → PostgreSQL loader (hosp + icu + ed + note)
│   ├── mimic_to_bundle.py       # Gold Data pipeline — all resources, no blinding
│   ├── mimic_to_fhir.py         # Flat NDJSON per resource type (optional)
│   ├── golddata_fhir_gen.py     # Blind pipeline — latest encounter blinded
│   └── golddata_builder.py      # FHIR builders for golddata (isolated UUID namespace)
│
├── web/
│   ├── parser.py                # Shared FHIR bundle → API response parser
│   ├── app.py                   # Gold Data dashboard  (port 8095, golddata_fhir_bundles/)
│   └── golddata_app.py          # FHIR (Blind) dashboard  (port 8096, fhir_bundles/)
│
├── static/                      # Shared UI (served by both apps)
│   ├── index.html
│   ├── app.js
│   └── style.css
│
├── sql/
│   ├── 01_schema.sql            # DDL for all tables (hosp + icu + ed + note schemas)
│   └── 02_indexes.sql           # subject_id indexes — run via `python main.py reindex`
│
├── golddata_fhir_bundles/       # Gold Data — full clinical bundles
├── fhir_bundles/       # FHIR (Blind) bundles (latest encounter blinded)
└── fhir_output/                 # Flat NDJSON (optional)
```

---

## Performance Notes (Full Dataset)

The full MIMIC-IV dataset has 888 million rows. Key tables:

| Table              | Rows  | Notes                                             |
| ------------------ | ----- | ------------------------------------------------- |
| `icu.chartevents`  | 432 M | Composite index on `(subject_id, itemid)`         |
| `hosp.labevents`   | 158 M | Composite index on `(subject_id, charttime DESC)` |
| `hosp.emar_detail` | 54 M  | Index on `subject_id`                             |

Always run `python main.py reindex` after loading. Without indexes, generating
one patient bundle can take several minutes instead of milliseconds.

The `docker-compose.yml` includes PostgreSQL performance tuning parameters
(`shared_buffers=4GB`, `fsync=off`, `wal_level=minimal`) optimised for
bulk loading. Do not use `fsync=off` in production.

---

## Stopping / Resetting

```bash
# Stop containers (data preserved)
docker compose down

# Full reset — deletes all loaded data
docker compose down -v
```

---

## Data Sources

- [MIMIC-IV v3.1](https://physionet.org/content/mimiciv/3.1/) — requires PhysioNet credentialing
- [MIMIC-IV-Note v2.2](https://physionet.org/content/mimic-iv-note/2.2/) — requires PhysioNet credentialing
