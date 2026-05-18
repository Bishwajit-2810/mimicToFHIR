# How to Run — MIMIC-IV Clinical Platform

## Architecture

```text
┌───────────────────────────┐  ┌───────────────────────────┐  ┌───────────────────────────┐
│  Full Pipeline            │  │  GoldData Pipeline        │  │  Testing Pipeline         │
│                           │  │                           │  │                           │
│  Container: mimic_pg_     │  │  Container: mimic_pg_     │  │  Container: mimic_pg_     │
│            standard       │  │            golddata       │  │            testing        │
│  DB port : 5433           │  │  DB port : 5434           │  │  DB port : 5435           │
│  Output  : fhir_bundles/  │  │  Output  : golddata_fhir_ │  │  Output  : testing/       │
│  Dashboard: port 8095     │  │            bundles/       │  │  Dashboard: port 8097     │
│                           │  │  Dashboard: port 8096     │  │                           │
│  Conditions    ✓          │  │  Conditions    ✗          │  │  Conditions    ✗          │
│  Medications   ✓          │  │  Medications   ✗          │  │  Medications   ✗          │
│  Notes         ✓          │  │  Notes         ✗          │  │  Notes         ✓          │
│  Vitals/Labs   ✓          │  │  Vitals/Labs   ✓          │  │  Vitals/Labs   ✓          │
└───────────────────────────┘  └───────────────────────────┘  └───────────────────────────┘
```

All three dashboards share the same `static/` UI. The difference is entirely in
the JSON bundles each pipeline generates. A coloured dataset banner at the top of
each dashboard identifies which pipeline is active and which resource types are
included.

---

## Prerequisites

| Requirement             | Version / Notes                                           |
| ----------------------- | --------------------------------------------------------- |
| Docker + Docker Compose | any recent version                                        |
| Python                  | 3.12+                                                     |
| Python packages         | `pip install psycopg2-binary fastapi "uvicorn[standard]"` |

---

## Quick Start — All Three Pipelines

Run all of the following in sequence. Each step must complete before the next.

Data is read from `dataset/` inside the project root — no path flags needed.

```bash
# ── Step 1: Start all three database containers ────────────────────────────
docker compose up -d
docker compose ps    # wait until all three show "healthy"

# ── Step 2: Load data into the standard container (port 5433) ──────────────
python main.py load

# ── Step 3: Load data into the golddata container (port 5434) ──────────────
python main.py load \
  --dsn "host=localhost port=5434 dbname=mimiciv user=mimic password=mimic"

# ── Step 4: Load data into the testing container (port 5435) ───────────────
python main.py load \
  --dsn "host=localhost port=5435 dbname=mimiciv user=mimic password=mimic"

# ── Step 5: Generate Full FHIR bundles ─────────────────────────────────────
python main.py bundle
# Output → fhir_bundles/  (random 20 patients by default)

# ── Step 6: Generate GoldData FHIR bundles ─────────────────────────────────
python main.py golddata
# Output → golddata_fhir_bundles/  (random 20 patients by default)

# ── Step 7: Generate Testing FHIR bundles ──────────────────────────────────
python main.py testing
# Output → testing/  (random 20 patients by default)

# ── Step 8: Start all three dashboards (three separate terminals) ───────────
uvicorn web.app:app          --host 0.0.0.0 --port 8095 --reload
uvicorn web.golddata_app:app --host 0.0.0.0 --port 8096 --reload
uvicorn web.testing_app:app  --host 0.0.0.0 --port 8097 --reload
```

| URL                     | Pipeline | Conditions | Medications | Notes |
| ----------------------- | -------- | :--------: | :---------: | :---: |
| <http://localhost:8095> | Full     | ✓          | ✓           | ✓     |
| <http://localhost:8096> | GoldData | ✗          | ✗           | ✗     |
| <http://localhost:8097> | Testing  | ✗          | ✗           | ✓     |

---

## Containers Reference

### Starting / stopping

```bash
# Start all three containers
docker compose up -d

# Start a single container
docker compose up -d db_standard
docker compose up -d db_golddata
docker compose up -d db_testing

# Check health
docker compose ps

# Stop (data preserved in Docker volumes)
docker compose down

# Stop and delete all data (full reset — requires reloading)
docker compose down -v
```

### Connection details

| Container            | Host      | Port | Database | User  | Password |
| -------------------- | --------- | ---- | -------- | ----- | -------- |
| `mimic_pg_standard`  | localhost | 5433 | mimiciv  | mimic | mimic    |
| `mimic_pg_golddata`  | localhost | 5434 | mimiciv  | mimic | mimic    |
| `mimic_pg_testing`   | localhost | 5435 | mimiciv  | mimic | mimic    |

### Connect with psql

```bash
docker exec -it mimic_pg_standard psql -U mimic -d mimiciv
docker exec -it mimic_pg_golddata  psql -U mimic -d mimiciv
docker exec -it mimic_pg_testing   psql -U mimic -d mimiciv
```

---

## Full FHIR Pipeline (port 8095)

Uses `mimic_pg_standard` on port 5433.

### Full — load data

```bash
python main.py load
```

Reads `dataset/hosp/`, `dataset/icu/`, and `dataset/note/` by default.
Safe to re-run — truncates tables before loading.

### Full — generate bundles

```bash
python main.py bundle
```

Output → `fhir_bundles/` — one JSON file per patient. Defaults to **20 random patients**.

```bash
# Change the count
python main.py bundle --limit 50

# Sequential ordering instead of random
python main.py bundle --no-random --limit 100

# Specific patients
python main.py bundle --subject-ids 10000032,10000084
```

Each bundle contains: `Patient`, `Practitioner`, `Encounter` (hospital + ICU),
`Condition`, `Procedure`, `Observation` (vitals + labs + ICU events + OMR),
`MedicationRequest`, `DiagnosticReport`, `DocumentReference` (discharge + radiology).

### Full — start dashboard

```bash
uvicorn web.app:app --host 0.0.0.0 --port 8095 --reload
```

---

## GoldData FHIR Pipeline (port 8096)

Uses `mimic_pg_golddata` on port 5434.

The GoldData pipeline produces **fully blind** bundles: **all** ICD diagnoses,
medications, and clinical notes are removed from every encounter.

### GoldData — load data

```bash
python main.py load \
  --dsn "host=localhost port=5434 dbname=mimiciv user=mimic password=mimic"
```

Reads the same `dataset/` directory as the standard pipeline.

### GoldData — generate bundles

```bash
python main.py golddata
```

Defaults to **20 random patients**. Override as needed:

```bash
# More patients
python main.py golddata --limit 50

# Sequential ordering
python main.py golddata --no-random --limit 100

# Specific patients
python main.py golddata --subject-ids 10000032,10000084
```

Or directly:

```bash
python -m etl.golddata_fhir_gen
```

**Test a single patient:**

```bash
python -m etl.golddata_fhir_gen --patient 10000032
```

**Custom DSN or output:**

```bash
python -m etl.golddata_fhir_gen \
  --dsn "host=myhost port=5434 dbname=mimiciv user=mimic password=mimic" \
  --output /custom/path/golddata_bundles
```

### GoldData — start dashboard

```bash
uvicorn web.golddata_app:app --host 0.0.0.0 --port 8096 --reload
```

---

## Testing FHIR Pipeline (port 8097)

Uses `mimic_pg_testing` on port 5435.

The Testing pipeline is identical to GoldData **plus** clinical notes
(`DocumentReference` — discharge summaries and radiology reports). This allows
evaluation of note-based models while keeping diagnoses and medications blind.

### Testing — load data

```bash
python main.py load \
  --dsn "host=localhost port=5435 dbname=mimiciv user=mimic password=mimic"
```

Reads the same `dataset/` directory as the other two pipelines.

### Testing — generate bundles

```bash
python main.py testing
```

Defaults to **20 random patients**. Override as needed:

```bash
# More patients
python main.py testing --limit 50

# Sequential ordering
python main.py testing --no-random --limit 100

# Specific patients
python main.py testing --subject-ids 10000032,10000084
```

Or directly:

```bash
python -m etl.testing_gen
```

**Test a single patient:**

```bash
python -m etl.testing_gen --patient 10000032
```

### Testing — start dashboard

```bash
uvicorn web.testing_app:app --host 0.0.0.0 --port 8097 --reload
```

---

## Environment Variables

| Variable          | Used by                    | Default                              |
| ----------------- | -------------------------- | ------------------------------------ |
| `MIMIC_DSN`       | `main.py load`, `bundle`   | `host=localhost port=5433 …`         |
| `GOLDDATA_DSN`    | `main.py golddata`         | `host=localhost port=5434 …`         |
| `TESTING_DSN`     | `main.py testing`          | `host=localhost port=5435 …`         |
| `GOLDDATA_OUT`    | `etl/golddata_fhir_gen.py` | `golddata_fhir_bundles`              |
| `TESTING_OUT`     | `etl/testing_gen.py`       | `testing`                            |
| `MIMIC_DATA_DIR`  | `main.py load`             | `dataset/`                           |
| `MIMIC_NOTE_DIR`  | `main.py load`             | `dataset/note/`                      |

---

## What Each Bundle Contains

| Resource type          | Full (`fhir_bundles/`) | GoldData | Testing |
| ---------------------- | :--------------------: | :------: | :-----: |
| `Patient`              | ✓                      | ✓        | ✓       |
| `Encounter` (hospital) | ✓                      | ✓        | ✓       |
| `Encounter` (ICU)      | ✓                      | ✓        | ✓       |
| `Condition`            | ✓                      | **✗**    | **✗**   |
| `MedicationRequest`    | ✓                      | **✗**    | **✗**   |
| `Procedure`            | ✓                      | ✓        | ✓       |
| `Observation` (labs)   | ✓                      | ✓        | ✓       |
| `Observation` (vitals) | ✓                      | ✓        | ✓       |
| `DiagnosticReport`     | ✓                      | ✓        | ✓       |
| `Practitioner`         | ✓                      | ✓        | ✓       |
| `DocumentReference`    | ✓                      | **✗**    | ✓       |

---

## Generating Output Files

All output directories are safe to regenerate at any time — files are overwritten.

### `fhir_bundles/` — Full FHIR bundles

```bash
python main.py bundle
```

### `golddata_fhir_bundles/` — Blind bundles (no diagnoses, no meds, no notes)

```bash
python main.py golddata
```

### `testing/` — Blind + notes bundles (no diagnoses, no meds, WITH notes)

```bash
python main.py testing
```

### `fhir_output/` — Flat NDJSON (bulk ingestion format)

```bash
python main.py convert
```

One `.ndjson` file per resource type (e.g. `Patient.ndjson`, `Condition.ndjson`).
Useful for bulk ingestion into FHIR servers or analytics pipelines.

---

## Troubleshooting

### Connection refused on port 5433, 5434, or 5435

```bash
docker compose up -d
docker compose ps    # check health status
docker compose logs  # check for startup errors
```

### Port already in use (dashboard)

```bash
# Check what is using the port
fuser 8095/tcp

# Start on a different port
uvicorn web.app:app --host 0.0.0.0 --port 9095
```

### `psycopg2` not found

```bash
pip install psycopg2-binary
```

### Dashboard shows no data

Check that the relevant bundles directory contains `.json` files:

```bash
ls fhir_bundles/           # for port 8095
ls golddata_fhir_bundles/  # for port 8096
ls testing/                # for port 8097
```

If empty, run the corresponding generation step above.

### Full reset

```bash
docker compose down -v    # delete all volumes and data
docker compose up -d      # fresh containers (re-runs schema DDL)
docker compose ps         # wait until all three are healthy

# Reload all three databases (all read from dataset/ by default)
python main.py load
python main.py load --dsn "host=localhost port=5434 dbname=mimiciv user=mimic password=mimic"
python main.py load --dsn "host=localhost port=5435 dbname=mimiciv user=mimic password=mimic"
```
