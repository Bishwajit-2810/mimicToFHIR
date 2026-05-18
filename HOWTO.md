# How to Run — MIMIC-IV Clinical Platform

## Architecture

```text
┌─────────────────────────────────────────────────────────────────────┐
│  Single PostgreSQL container: mimic_pg  (port 5432)                 │
│  Shared by all three pipelines — load data once                     │
└─────────────────────────────────────────────────────────────────────┘
         │                    │                    │
         ▼                    ▼                    ▼
┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐
│  Full Pipeline  │  │ GoldData Pipeline│  │Testing Pipeline │
│  fhir_bundles/  │  │golddata_fhir_   │  │  testing/       │
│  port 8095      │  │bundles/         │  │  port 8097      │
│                 │  │port 8096        │  │                 │
│  Conditions  ✓  │  │Conditions  ✗    │  │Conditions  ✗    │
│  Medications ✓  │  │Medications ✗    │  │Medications ✗    │
│  Notes       ✓  │  │Notes       ✗    │  │Notes       ✓    │
│  Vitals/Labs ✓  │  │Vitals/Labs ✓    │  │Vitals/Labs ✓    │
└─────────────────┘  └─────────────────┘  └─────────────────┘
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

## Quick Start

```bash
# ── Step 1: Start the database container ───────────────────────────────────
docker compose up -d
docker compose ps    # wait until it shows "healthy"

# ── Step 2: Load data (once — all pipelines share the same DB) ─────────────
python main.py load

# ── Step 3: Generate all three bundle sets from the same 20 random patients ─
python main.py all
# Output:
#   fhir_bundles/              ← Full (conditions + meds + notes)
#   golddata_fhir_bundles/     ← Blind (no conditions, no meds, no notes)
#   testing/                   ← Blind + notes

# ── Step 4: Start dashboards (three separate terminals) ────────────────────
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

## `python main.py all` — Shared patient selection

`all` picks N random patients **once** from the database and passes the same list
to all three generators. This guarantees identical patient cohorts across
`fhir_bundles/`, `golddata_fhir_bundles/`, and `testing/`.

```bash
# Default: 20 random patients
python main.py all

# Custom count
python main.py all --limit 50
```

---

## Individual pipeline commands

### Load data

```bash
python main.py load
```

Reads `dataset/hosp/`, `dataset/icu/`, and `dataset/note/` by default.
Safe to re-run — truncates tables before loading.

### Full FHIR bundles

```bash
python main.py bundle                        # 20 random patients (default)
python main.py bundle --limit 50             # more patients
python main.py bundle --no-random --limit 100
python main.py bundle --subject-ids 10000032,10000084
```

Output → `fhir_bundles/` — contains: `Patient`, `Practitioner`, `Encounter`,
`Condition`, `Procedure`, `Observation`, `MedicationRequest`, `DiagnosticReport`,
`DocumentReference`.

### GoldData FHIR bundles

```bash
python main.py golddata
python main.py golddata --limit 50
python main.py golddata --subject-ids 10000032,10000084
```

Output → `golddata_fhir_bundles/` — same as Full minus `Condition`,
`MedicationRequest`, and `DocumentReference`.

### Testing FHIR bundles

```bash
python main.py testing
python main.py testing --limit 50
python main.py testing --subject-ids 10000032,10000084
```

Output → `testing/` — same as GoldData plus `DocumentReference` (notes).

### Start dashboards

```bash
uvicorn web.app:app          --host 0.0.0.0 --port 8095 --reload
uvicorn web.golddata_app:app --host 0.0.0.0 --port 8096 --reload
uvicorn web.testing_app:app  --host 0.0.0.0 --port 8097 --reload
```

---

## Environment Variables

| Variable         | Default                                      |
| ---------------- | -------------------------------------------- |
| `MIMIC_DSN`      | `host=localhost port=5433 dbname=mimiciv …`  |
| `GOLDDATA_OUT`   | `golddata_fhir_bundles`                      |
| `TESTING_OUT`    | `testing`                                    |
| `MIMIC_DATA_DIR` | `dataset/`                                   |
| `MIMIC_NOTE_DIR` | `dataset/note/`                              |

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

### Full reset

```bash
docker compose down -v    # delete volume and data
docker compose up -d      # fresh container (re-runs schema DDL)
docker compose ps         # wait until healthy
python main.py load       # reload data
python main.py all        # regenerate all bundles
```
