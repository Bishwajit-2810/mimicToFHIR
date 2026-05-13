# How to Run — MIMIC-IV Clinical Platform

## Prerequisites

| Requirement             | Version / Install                      |
| ----------------------- | -------------------------------------- |
| Docker + Docker Compose | any recent version                     |
| Python                  | 3.12+                                  |
| Python dependencies     | `pip install -e .` or see below        |

```bash
pip install psycopg2-binary fastapi "uvicorn[standard]"
```

---

## Option A — Dashboard only (no ETL needed)

The `fhir_bundles/` directory is already populated in this repository.
You can run the dashboard immediately without Docker or PostgreSQL:

```bash
uvicorn app:app --host 0.0.0.0 --port 8095 --reload
```

Open <http://localhost:8095>, select a patient from the dropdown, and
explore their full clinical record across all dashboard tabs.

---

## Option B — Full ETL Pipeline

### Step 1 — Start PostgreSQL

```bash
docker compose up -d
```

Starts a PostgreSQL 16 container on **port 5433**.

Verify it is healthy:

```bash
docker compose ps
```

Expected output:

```text
NAME       STATUS                   PORTS
mimic_pg   Up (healthy)   0.0.0.0:5433->5432/tcp
```

Connection details:

| Setting  | Value     |
| -------- | --------- |
| Host     | localhost |
| Port     | 5433      |
| Database | mimiciv   |
| User     | mimic     |
| Password | mimic     |

Connect with psql:

```bash
docker exec -it mimic_pg psql -U mimic -d mimiciv
```

---

### Step 2 — Load the data

```bash
python main.py load
```

Streams all 35 gzipped CSV files into PostgreSQL via `COPY`.
Loads ~1.4 million rows across 31 tables (`hosp` and `icu` schemas).
Takes about 30 seconds.

Expected output:

```text
Connected to database.
  Loading hosp.provider ... 40508 rows
  Loading hosp.patients ... 100 rows
  Loading hosp.admissions ... 275 rows
  ...
Done. 1398500 total rows loaded.
```

Running the loader multiple times is safe — it truncates tables before loading.

---

### Step 3 — Generate FHIR bundles

Two output formats are available.

#### Transaction Bundles (recommended)

One JSON file per patient. Each is a FHIR R4 `Bundle` (type `transaction`)
with `urn:uuid:` references and `POST` request entries — compatible with
Synthea-style FHIR servers.

```bash
python main.py bundle
```

Output goes to `fhir_bundles/` — 100 files, one per patient.

Each bundle contains these resource types:

| Resource            | Source table(s)                                      |
| ------------------- | ---------------------------------------------------- |
| `Patient`           | `hosp.patients` + `hosp.admissions`                  |
| `Organization`      | BIDMC placeholder                                    |
| `Practitioner`      | `hosp.provider`                                      |
| `Encounter`         | `hosp.admissions` (hospital) + `icu.icustays` (ICU)  |
| `Condition`         | `hosp.diagnoses_icd`                                 |
| `Procedure`         | `hosp.procedures_icd`                                |
| `Observation`       | `hosp.labevents`, `icu.chartevents`, `hosp.omr`      |
| `MedicationRequest` | `hosp.prescriptions`                                 |
| `DiagnosticReport`  | `hosp.microbiologyevents`                            |

#### Flat NDJSON

One `.ndjson` file per resource type — useful for bulk ingestion into FHIR
servers that accept streaming NDJSON.

```bash
python main.py convert
```

Output goes to `fhir_output/`:

```text
fhir_output/
├── Condition.ndjson           4,506 resources
├── DiagnosticReport.ndjson    1,336 resources
├── Encounter.ndjson             415 resources
├── MedicationRequest.ndjson  18,087 resources
├── Observation.ndjson        176,511 resources
├── Patient.ndjson               100 resources
└── Procedure.ndjson             722 resources
```

---

### Step 4 — Run the dashboard

```bash
uvicorn app:app --host 0.0.0.0 --port 8095 --reload
```

---

## Custom DSN or output directory

Both `bundle` and `convert` accept optional flags:

```bash
# Custom connection string
python main.py bundle --dsn "host=myhost port=5433 dbname=mimiciv user=mimic password=mimic"

# Custom output directory
python main.py bundle --output /path/to/output
python main.py convert --output /path/to/output
```

Or export `MIMIC_DSN` once to avoid repeating it:

```bash
export MIMIC_DSN="host=localhost port=5433 dbname=mimiciv user=mimic password=mimic"
python main.py bundle
python main.py convert
```

---

## Stop and reset

```bash
# Stop the container (data preserved in Docker volume)
docker compose down

# Stop and delete all data (full reset)
docker compose down -v
```

After a full reset, repeat from Step 1.

---

## Troubleshooting

### Port 5432 already in use

The compose file maps to host port 5433 to avoid conflicts with a local
PostgreSQL instance. If 5433 is also taken, change the left side in
`docker-compose.yml`:

```yaml
ports:
  - "5434:5432"
```

Then update the DSN accordingly.

### `psycopg2` not found

```bash
pip install psycopg2-binary
```

### Container not ready yet

The loader retries automatically. If it still fails after a few seconds, run:

```bash
docker compose ps   # check health status
docker compose logs # check for startup errors
```

### Dashboard shows no data

Ensure `fhir_bundles/` contains `.json` files. If you ran a full reset,
re-run `python main.py bundle` to regenerate them.
