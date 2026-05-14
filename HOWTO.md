# How to Run — MIMIC-IV Clinical Platform

## Architecture

```text
┌─────────────────────────────────┐   ┌─────────────────────────────────┐
│  Standard FHIR Pipeline         │   │  GoldData FHIR Pipeline         │
│                                 │   │                                 │
│  Container : mimic_pg_standard  │   │  Container : mimic_pg_golddata  │
│  Port      : 5433               │   │  Port      : 5434               │
│  Script    : python main.py     │   │  Script    : golddata_fhir_gen  │
│  Output    : fhir_bundles/      │   │  Output    : golddata_fhir_bundles/│
│  Dashboard : port 8095 (app.py) │   │  Dashboard : port 8096          │
│                                 │   │                                 │
│  Full clinical data             │   │  Latest-encounter diagnoses and │
│  All diagnoses included         │   │  medications intentionally      │
│                                 │   │  excluded from JSON bundles     │
└─────────────────────────────────┘   └─────────────────────────────────┘
```

Both dashboards use the same `static/` UI. The difference is purely in the
data: the GoldData JSON bundles never contain `Condition` resources or
`MedicationRequest` resources for the patient's most recent hospital encounter.

---

## Prerequisites

| Requirement             | Version / Notes                                           |
| ----------------------- | --------------------------------------------------------- |
| Docker + Docker Compose | any recent version                                        |
| Python                  | 3.12+                                                     |
| Python packages         | `pip install psycopg2-binary fastapi "uvicorn[standard]"` |

---

## Quick Start — Both Pipelines

Run all of the following in sequence. Each step must complete before the next.

```bash
# ── Step 1: Start both database containers ─────────────────────────────────
docker compose up -d

# Wait until both are healthy (~10 seconds):
docker compose ps

# ── Step 2: Load MIMIC-IV data into the standard container (port 5433) ─────
python main.py load

# ── Step 3: Load MIMIC-IV data into the golddata container (port 5434) ─────
MIMIC_DSN="host=localhost port=5434 dbname=mimiciv user=mimic password=mimic" \
  python main.py load

# ── Step 4: Generate standard FHIR bundles ─────────────────────────────────
python main.py bundle
# Output → fhir_bundles/  (100 files, full clinical data)

# ── Step 5: Generate GoldData FHIR bundles ─────────────────────────────────
python -m etl.golddata_fhir_gen
# Output → golddata_fhir_bundles/  (100 files, latest-encounter dx+meds excluded)

# ── Step 6: Start both dashboards (two separate terminals) ─────────────────
uvicorn web.app:app           --host 0.0.0.0 --port 8095 --reload   # standard
uvicorn web.golddata_app:app  --host 0.0.0.0 --port 8096 --reload   # golddata
```

| URL                     | Pipeline | What it shows                                  |
| ----------------------- | -------- | ---------------------------------------------- |
| <http://localhost:8095> | Standard | Full data — all diagnoses and medications      |
| <http://localhost:8096> | GoldData | Latest encounter is diagnosis/treatment-blind  |

---

## Standard Dashboard Only (no GoldData needed)

`fhir_bundles/` is already included in the repository. You can run the
standard dashboard immediately without Docker:

```bash
uvicorn web.app:app --host 0.0.0.0 --port 8095 --reload
```

Open <http://localhost:8095> and select a patient.

---

## Containers Reference

### Starting / stopping

```bash
# Start both containers
docker compose up -d

# Start only one container
docker compose up -d db_standard
docker compose up -d db_golddata

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

### Connect with psql

```bash
# Standard container
docker exec -it mimic_pg_standard psql -U mimic -d mimiciv

# GoldData container
docker exec -it mimic_pg_golddata psql -U mimic -d mimiciv
```

---

## Standard FHIR Pipeline (port 8095)

Uses `mimic_pg_standard` on port 5433.

### Load data

```bash
python main.py load
```

Expected output:

```text
Connected to database.
  Loading hosp.provider ... 40508 rows
  Loading hosp.patients ... 100 rows
  ...
Done. 1398500 total rows loaded.
```

Safe to re-run — truncates tables before loading.

### Generate bundles

```bash
python main.py bundle
```

Output → `fhir_bundles/` — 100 JSON files, one per patient.

Each bundle contains: `Patient`, `Organization`, `Practitioner`, `Encounter`,
`Condition`, `Procedure`, `Observation` (vitals + labs), `MedicationRequest`,
`DiagnosticReport`.

### Run dashboard

```bash
uvicorn web.app:app --host 0.0.0.0 --port 8095 --reload
```

---

## GoldData FHIR Pipeline (port 8096)

Uses `mimic_pg_golddata` on port 5434.

The GoldData pipeline generates **diagnosis-and-treatment-blind** FHIR bundles
for model evaluation. For each patient's most-recent hospital encounter, the
following are **never written into the JSON file**:

- `Condition` resources — ICD-9/10 diagnoses
- `MedicationRequest` resources — medications prescribed during that encounter
- `dischargeDisposition` — outcome signal on the `Encounter` resource

All other data is present for every encounter including the latest:
vitals, lab results, ICU chart events, ICU procedure events, ICD-coded
procedures performed, microbiology reports.

Historical encounters (all encounters except the latest) retain complete data.

### Load data into the golddata container

```bash
MIMIC_DSN="host=localhost port=5434 dbname=mimiciv user=mimic password=mimic" \
  python main.py load
```

### Generate GoldData bundles

```bash
python -m etl.golddata_fhir_gen
```

Expected output:

```text
GoldData FHIR Generator
  DSN        : host=localhost port=5434 dbname=mimiciv user=mimic password=mimic
  Output     : /path/to/golddata_fhir_bundles/
  Mode       : exclude diagnoses for each patient's latest encounter

Processing 100 patients → golddata_fhir_bundles/

  [  1/100]  subject  10000032   entries  latest_hadm=29079034  → 10000032.json
  ...

Done. 100/100 bundles.
```

**Test a single patient first:**

```bash
python -m etl.golddata_fhir_gen --patient 10000032
```

**Custom DSN or output directory:**

```bash
python -m etl.golddata_fhir_gen --dsn "host=myhost port=5434 dbname=mimiciv user=mimic password=mimic"
python -m etl.golddata_fhir_gen --output /custom/path/golddata_bundles
```

**Environment variables (alternative to flags):**

```bash
export GOLDDATA_DSN="host=localhost port=5434 dbname=mimiciv user=mimic password=mimic"
export GOLDDATA_OUT="golddata_fhir_bundles"
python -m etl.golddata_fhir_gen
```

### Start the GoldData dashboard

```bash
uvicorn web.golddata_app:app --host 0.0.0.0 --port 8096 --reload
```

Open <http://localhost:8096>.

---

## Environment Variables

| Variable      | Used by                  | Default                                   |
| ------------- | ------------------------ | ----------------------------------------- |
| `MIMIC_DSN`   | `main.py load`           | `host=localhost port=5433 ...`            |
| `GOLDDATA_DSN`| `etl/golddata_fhir_gen.py`   | `host=localhost port=5434 ...`            |
| `GOLDDATA_OUT`| `etl/golddata_fhir_gen.py`   | `golddata_fhir_bundles`                   |

---

## What Makes a GoldData Bundle Different

For the blinded (latest) encounter the JSON bundle contains:

| Resource type                       | Standard bundle | GoldData bundle |
| ----------------------------------- | --------------- | --------------- |
| `Condition`                         | ✓ included      | ✗ absent        |
| `MedicationRequest`                 | ✓ included      | ✗ absent        |
| `dischargeDisposition` on Encounter | ✓ included      | ✗ absent        |
| `Observation` (vitals + labs)       | ✓ included      | ✓ included      |
| `Procedure`                         | ✓ included      | ✓ included      |
| `DiagnosticReport`                  | ✓ included      | ✓ included      |

Historical encounters (all encounters before the latest) are identical in both
pipelines — full data including diagnoses and medications.

---

## Generating Output Files

All three output directories are produced by separate commands. Generation is
safe to re-run at any time — files are overwritten.

### `fhir_bundles/` — Standard FHIR transaction bundles

Requires: standard container running (`mimic_pg_standard`, port 5433) and data loaded.

```bash
python main.py bundle
```

- Output: `fhir_bundles/` — 100 JSON files, one per patient
- Each file is a FHIR R4 transaction bundle containing: `Patient`, `Organization`,
  `Practitioner`, `Encounter` (hospital + ICU), `Condition`, `Procedure`,
  `Observation` (vitals + labs + ICU events + OMR), `MedicationRequest`,
  `DiagnosticReport`
- All encounters included, all diagnoses and medications present

### `golddata_fhir_bundles/` — Diagnosis-blind FHIR bundles

Requires: golddata container running (`mimic_pg_golddata`, port 5434) and data loaded.

```bash
python -m etl.golddata_fhir_gen
```

- Output: `golddata_fhir_bundles/` — 100 JSON files, one per patient
- Identical structure to standard bundles **except** for each patient's latest encounter:
  - `Condition` resources are **absent** (ICD diagnoses withheld)
  - `MedicationRequest` resources are **absent** (prescriptions withheld)
  - `dischargeDisposition` field is **absent** (outcome signal withheld)
- Vitals, labs, procedures, microbiology, and ICU data are fully present for all encounters
- Historical encounters retain complete data including diagnoses and medications

Test a single patient before running all 100:

```bash
python -m etl.golddata_fhir_gen --patient 10000032
```

### `fhir_output/` — Flat NDJSON (bulk ingestion format)

Requires: standard container running and data loaded.

```bash
python main.py convert
```

- Output: `fhir_output/` — one `.ndjson` file per resource type (e.g. `Patient.ndjson`, `Condition.ndjson`)
- Useful for bulk ingestion into FHIR servers or analytics pipelines
- Derived from the same data as `fhir_bundles/`

---

## Troubleshooting

### Connection refused on port 5433 or 5434

The relevant container is not running.

```bash
docker compose up -d
docker compose ps    # check health status
docker compose logs  # check for startup errors
```

### Port already in use

Change the left-hand port in `docker-compose.yml` and update your DSN:

```yaml
# e.g. move standard to 5435
ports:
  - "5435:5432"
```

### `psycopg2` not found

```bash
pip install psycopg2-binary
```

### Dashboard shows no data

Ensure the relevant bundles directory contains `.json` files:

```bash
ls fhir_bundles/           # for port 8095
ls golddata_fhir_bundles/  # for port 8096
```

If empty, run the corresponding generation step above.

### Full reset

```bash
docker compose down -v    # delete all volumes and data
docker compose up -d      # fresh containers
python main.py load       # reload standard
MIMIC_DSN="host=localhost port=5434 dbname=mimiciv user=mimic password=mimic" \
  python main.py load     # reload golddata
```
