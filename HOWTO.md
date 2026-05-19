# How to Run — MIMIC-IV Clinical Platform

## Architecture

```text
┌────────────────────────────────────────────────────────────────────┐
│  Single PostgreSQL container: mimic_pg  (port 5433)                │
│  Shared by all three pipelines — load data once                    │
│  Schemas: hosp (22 tables) · icu (9) · ed (6) · note (4)          │
└────────────────────────────────────────────────────────────────────┘
         │                    │                    │
         ▼                    ▼                    ▼
┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐
│  Full Pipeline  │  │ GoldData Pipeline│  │Testing Pipeline │
│  fhir_bundles/  │  │golddata_fhir_   │  │  testing/       │
│  port 8095      │  │bundles/         │  │  port 8097      │
│                 │  │port 8096        │  │                 │
│  All encounters │  │Prior encounters │  │Prior encounters │
│  Conditions  ✓  │  │Conditions  ✓    │  │Conditions  ✓    │
│  Medications ✓  │  │Medications ✓    │  │Medications ✓    │
│  Notes       ✓  │  │Notes       ✓    │  │Notes       ✓    │
│                 │  │                 │  │                 │
│  Latest encounter│  │Latest encounter │  │Latest encounter │
│  Conditions  ✓  │  │Conditions  ✗    │  │Conditions  ✗    │
│  Medications ✓  │  │Medications ✗    │  │Medications ✗    │
│  Notes       ✓  │  │Notes       ✗    │  │Notes       ✓    │
│  Vitals/Labs ✓  │  │Vitals/Labs ✓    │  │Vitals/Labs ✓    │
└─────────────────┘  └─────────────────┘  └─────────────────┘
```

**Blinding applies only to the most recent encounter** — the latest hospital
admission (`latest_hadm`) and latest ED stay (`latest_ed_stay`). All prior
encounters retain their full data including diagnoses and medications.

---

## Prerequisites

| Requirement             | Version / Notes                                           |
| ----------------------- | --------------------------------------------------------- |
| Docker + Docker Compose | any recent version                                        |
| Python                  | 3.12+                                                     |
| Python packages         | `pip install psycopg2-binary fastapi "uvicorn[standard]"` |

---

## Quick Start

```bash
# ── Step 1: Start the database container ───────────────────────────────────
docker compose up -d
docker compose ps    # wait until it shows "healthy"

# ── Step 2: Load data (once — all pipelines share the same DB) ─────────────
python main.py load

# ── Step 3: Create indexes (required for fast queries) ─────────────────────
python main.py reindex
# Takes 10–30 minutes on the full dataset. Safe to skip on the demo dataset.

# ── Step 4: Generate all three bundle sets from the same 5 random patients ──
python main.py all
# Output:
#   fhir_bundles/              ← Full (all data, no blinding)
#   golddata_fhir_bundles/     ← Latest encounter blinded (no Dx, no Meds, no Notes)
#   testing/                   ← Latest encounter blinded + notes restored

# ── Step 5: Start dashboards (three separate terminals) ────────────────────
uvicorn web.app:app          --host 0.0.0.0 --port 8095 --reload
uvicorn web.golddata_app:app --host 0.0.0.0 --port 8096 --reload
uvicorn web.testing_app:app  --host 0.0.0.0 --port 8097 --reload
```

| URL                     | Pipeline | Latest Conditions | Latest Meds | Notes |
| ----------------------- | -------- | :---------------: | :---------: | :---: |
| <http://localhost:8095> | Full     | ✓                 | ✓           | ✓     |
| <http://localhost:8096> | GoldData | ✗                 | ✗           | ✗     |
| <http://localhost:8097> | Testing  | ✗                 | ✗           | ✓     |

---

## Container Reference

### Starting / stopping

```bash
docker compose up -d      # start
docker compose ps         # check health
docker compose down       # stop (data preserved)
docker compose down -v    # stop and delete all data (full reset)
```

### Connection details

| Container  | Host      | Port | Database | User  | Password |
| ---------- | --------- | ---- | -------- | ----- | -------- |
| `mimic_pg` | localhost | 5433 | mimiciv  | mimic | mimic    |

### Connect with psql

```bash
docker exec -it mimic_pg psql -U mimic -d mimiciv
```

---

## `python main.py all` — Shared Patient Selection

`all` picks N random patients **once** from the database and passes the same list
to all three generators. This guarantees identical patient cohorts across
`fhir_bundles/`, `golddata_fhir_bundles/`, and `testing/`.

```bash
# Default: 5 random patients
python main.py all

# Custom count
python main.py all --limit 50

# Specific patients (skips random selection)
python main.py all --subject-ids 10000032,10000084
```

---

## Individual Pipeline Commands

### Load data

```bash
python main.py load
```

Reads `dataset/hosp/`, `dataset/icu/`, `dataset/ed/`, and `dataset/note/` by default.
Safe to re-run — truncates tables before reloading. Use `--tables` to reload specific tables only.

```bash
# Reload only prescriptions and emar
python main.py load --tables prescriptions,emar
```

### Create indexes

```bash
python main.py reindex
```

Creates `subject_id` indexes on all 38 queried tables. Run once after the initial
load. Skips existing indexes (safe to re-run). Critical for the full dataset —
without indexes, per-patient queries on `icu.chartevents` (432M rows) are very slow.

### Full FHIR bundles

```bash
python main.py bundle                        # 20 random patients (default)
python main.py bundle --limit 50
python main.py bundle --no-random --limit 100
python main.py bundle --subject-ids 10000032,10000084
```

Output → `fhir_bundles/` — all resources, no blinding.

### GoldData FHIR bundles

```bash
python main.py golddata
python main.py golddata --limit 50
python main.py golddata --subject-ids 10000032,10000084
```

Output → `golddata_fhir_bundles/` — latest encounter is blinded: no `Condition`,
no `MedicationRequest`, no `MedicationStatement` (ED), no `MedicationDispense` (ED),
no `MedicationAdministration` (ICU), no `DocumentReference`. All prior encounters
are fully included.

### Testing FHIR bundles

```bash
python main.py testing
python main.py testing --limit 50
python main.py testing --subject-ids 10000032,10000084
```

Output → `testing/` — same as GoldData but latest encounter's `DocumentReference`
(discharge notes + radiology) is restored. Designed for LLM evaluation where notes
are the input and diagnoses/medications are the labels to predict.

### Start dashboards

```bash
uvicorn web.app:app          --host 0.0.0.0 --port 8095 --reload
uvicorn web.golddata_app:app --host 0.0.0.0 --port 8096 --reload
uvicorn web.testing_app:app  --host 0.0.0.0 --port 8097 --reload
```

---

## Environment Variables

| Variable         | Default                                                         |
| ---------------- | --------------------------------------------------------------- |
| `MIMIC_DSN`      | `host=localhost port=5433 dbname=mimiciv user=mimic password=mimic` |
| `MIMIC_DATA_DIR` | `dataset/`                                                      |
| `MIMIC_NOTE_DIR` | `dataset/note/`                                                 |
| `GOLDDATA_OUT`   | `golddata_fhir_bundles`                                         |
| `TESTING_OUT`    | `testing`                                                       |

---

## What Each Bundle Contains

| Resource type | Source | Full | GoldData | Testing |
| --- | --- | :---: | :---: | :---: |
| `Patient` | hosp.patients | ✓ | ✓ | ✓ |
| `Encounter` (hospital) | hosp.admissions | ✓ | ✓ | ✓ |
| `Encounter` (ICU) | icu.icustays | ✓ | ✓ | ✓ |
| `Encounter` (ED) | ed.edstays | ✓ | ✓ | ✓ |
| `Condition` (hospital) | hosp.diagnoses_icd | ✓ | prior ✓ / latest ✗ | prior ✓ / latest ✗ |
| `Condition` (ED) | ed.diagnosis | ✓ | prior ✓ / latest ✗ | prior ✓ / latest ✗ |
| `MedicationRequest` | hosp.prescriptions | ✓ | prior ✓ / latest ✗ | prior ✓ / latest ✗ |
| `MedicationStatement` | ed.medrecon | ✓ | prior ✓ / latest ✗ | prior ✓ / latest ✗ |
| `MedicationDispense` | ed.pyxis | ✓ | prior ✓ / latest ✗ | prior ✓ / latest ✗ |
| `MedicationAdministration` | icu.inputevents | ✓ | prior ✓ / latest ✗ | prior ✓ / latest ✗ |
| `MedicationAdministration` | icu.ingredientevents | ✓ | prior ✓ / latest ✗ | prior ✓ / latest ✗ |
| `Procedure` | hosp.procedures_icd | ✓ | ✓ | ✓ |
| `Observation` (labs) | hosp.labevents | ✓ | ✓ | ✓ |
| `Observation` (ICU vitals) | icu.chartevents | ✓ | ✓ | ✓ |
| `Observation` (ICU procedure) | icu.procedureevents | ✓ | ✓ | ✓ |
| `Observation` (ICU datetime) | icu.datetimeevents | ✓ | ✓ | ✓ |
| `Observation` (ICU output) | icu.outputevents | ✓ | ✓ | ✓ |
| `Observation` (OMR survey) | hosp.omr | ✓ | ✓ | ✓ |
| `Observation` (ED triage) | ed.triage | ✓ | ✓ | ✓ |
| `Observation` (ED vitals) | ed.vitalsign | ✓ | ✓ | ✓ |
| `DiagnosticReport` | hosp.microbiologyevents | ✓ | ✓ | ✓ |
| `Claim` + `ExplanationOfBenefit` | hosp.drgcodes | ✓ | ✓ | ✓ |
| `Practitioner` | hosp.provider | ✓ | ✓ | ✓ |
| `Practitioner` (ICU caregiver) | icu.caregivers | ✓ | ✓ | ✓ |
| `DocumentReference` (discharge) | note.discharge | ✓ | prior ✓ / latest ✗ | ✓ |
| `DocumentReference` (radiology) | note.radiology | ✓ | prior ✓ / latest ✗ | ✓ |

---

## Troubleshooting

### Connection refused on port 5433

```bash
docker compose up -d
docker compose ps    # check health status
docker compose logs  # check for startup errors
```

### Port already in use (dashboard)

```bash
fuser 8095/tcp
uvicorn web.app:app --host 0.0.0.0 --port 9095   # use a different port
```

### `psycopg2` not found

```bash
pip install psycopg2-binary
```

### Dashboard shows no data

```bash
ls fhir_bundles/           # for port 8095
ls golddata_fhir_bundles/  # for port 8096
ls testing/                # for port 8097
```

If empty, run `python main.py all`.

### Slow bundle generation

Run `python main.py reindex` if you haven't already. Without subject_id indexes
the full dataset queries are extremely slow.

### Full reset

```bash
docker compose down -v    # delete volume and data
docker compose up -d      # fresh container (re-runs schema DDL)
docker compose ps         # wait until healthy
python main.py load       # reload data
python main.py reindex    # recreate indexes
python main.py all        # regenerate all bundles
```
