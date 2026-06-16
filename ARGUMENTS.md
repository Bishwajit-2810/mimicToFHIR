# CLI Arguments & How to Run

Complete reference for `python main.py` — every subcommand, every flag, and the
cohort-filter options that carve a patient subset into its own folder.

```bash
python main.py <subcommand> [options]
```

| Subcommand | What it does                                                           | Default output                             |
| ---------- | ---------------------------------------------------------------------- | ------------------------------------------ |
| `load`     | Load MIMIC-IV CSV.gz files into PostgreSQL                             | (database)                                 |
| `reindex`  | Create `subject_id` indexes (run once after load — makes queries fast) | (database)                                 |
| `convert`  | PostgreSQL → flat FHIR R4 NDJSON (one file per resource type)          | `fhir_output/`                             |
| `bundle`   | FHIR pipeline → one FHIR bundle JSON per patient                       | `fhir_bundles/`                            |
| `fhir_blind` | Blind pipeline (latest encounter has no Dx / Meds / Notes)             | `fhir_blind_bundles/`                   |
| `all`      | Run `bundle` + `fhir_blind` on the **same** patients (recommended)       | `fhir_bundles/` + `fhir_blind_bundles/` |

---

## Batch options (`bundle` / `fhir_blind` / `all`)

| Flag                       | Default               | Meaning                                              |
| -------------------------- | --------------------- | ---------------------------------------------------- |
| `--dsn DSN`                | `$MIMIC_DSN` or local | Override the PostgreSQL connection string            |
| `--output DIR`             | per-pipeline          | Override the output directory                        |
| `--limit N`                | `10000` (random)      | Max patients to process                              |
| `--offset N`               | `0`                   | Skip the first N patients (sequential mode only)     |
| `--subject-ids a,b,c`      | —                     | Process specific subject IDs; skips random selection |
| `--random` / `--no-random` | `--random`            | Random sample vs. sequential by `subject_id`         |

> `all` always picks its patient set **once** and feeds the same list to both
> pipelines, so the FHIR and FHIR (Blinded) outputs cover identical patients.

---

## Cohort filters (`bundle` / `fhir_blind` / `all`)

Pass one or more of these to extract only the matching patients. Output is
redirected to a self-describing folder under `filtered/`:

```
filtered/<slug>/
├── fhir/        ← full clinical bundles  (from the bundle pipeline)
└── fhir_blind/  ← blinded bundles        (from the fhir_blind pipeline)
```

`<slug>` is built from the active filters, e.g. `gender-male_service-med`.
Running the `all` command produces **both** subfolders for the same patients;
running `bundle` or `fhir_blind` alone produces just the one it owns.

All filters combine with **AND**. A patient is selected when _any_ of their
admissions / services satisfy the admission/service-level filters (the exported
bundle still contains the patient's full history).

### Demographics

| Flag                       | Column                            | Match                       |
| -------------------------- | --------------------------------- | --------------------------- |
| `--gender male\|female`    | `hosp.patients.gender`            | exact (M/F)                 |
| `--min-age N`              | `hosp.patients.anchor_age`        | `>= N`                      |
| `--max-age N`              | `hosp.patients.anchor_age`        | `<= N`                      |
| `--anchor-year YYYY`       | `hosp.patients.anchor_year`       | exact                       |
| `--anchor-year-group TEXT` | `hosp.patients.anchor_year_group` | substring (e.g. `2011`)     |
| `--deceased`               | `hosp.patients.dod`               | has a date of death         |
| `--race TEXT`              | `hosp.admissions.race`            | substring                   |
| `--ethnicity TEXT`         | `hosp.admissions.race`            | substring (e.g. `hispanic`) |
| `--language TEXT`          | `hosp.admissions.language`        | substring                   |
| `--marital-status TEXT`    | `hosp.admissions.marital_status`  | substring                   |

### Encounter

| Flag                        | Column                                 | Match                             |
| --------------------------- | -------------------------------------- | --------------------------------- |
| `--service CODE\|name`      | `hosp.services.curr_service`           | code (`MED`) or name (`medicine`) |
| `--admission-type TEXT`     | `hosp.admissions.admission_type`       | substring                         |
| `--admit-source TEXT`       | `hosp.admissions.admission_location`   | substring                         |
| `--discharge-location TEXT` | `hosp.admissions.discharge_location`   | substring                         |
| `--insurance TEXT`          | `hosp.admissions.insurance`            | substring                         |
| `--expired`                 | `hosp.admissions.hospital_expire_flag` | in-hospital death (`= 1`)         |

> Text filters are case-insensitive substring matches, so `--insurance medicare`
> matches `Medicare` and `--admit-source emergency` matches `EMERGENCY ROOM`.

### Service codes

`CMED` (Cardiac Medicine), `CSURG` (Cardiac Surgery), `DENT` (Dentistry),
`ENT` (Ear, Nose & Throat), `EYE` (Ophthalmology), `GU` (Genitourinary),
`GYN` (Gynecology), `MED` (Medicine), `NB`/`NBB` (Newborn), `NMED` (Neurology),
`NSURG` (Neurosurgery), `OBS` (Obstetrics), `OMED` (Oncology),
`ORTHO` (Orthopedics), `PSURG` (Plastic Surgery), `PSYCH` (Psychiatry),
`SURG` (Surgery), `TRAUM` (Trauma), `TSURG` (Thoracic Surgery),
`VSURG` (Vascular Surgery).

---

## `load` options

| Flag             | Default         | Meaning                                                  |
| ---------------- | --------------- | -------------------------------------------------------- |
| `--dsn DSN`      | local           | PostgreSQL connection string                             |
| `--data-dir DIR` | `dataset/`      | Root dir containing `hosp/`, `icu/`, `ed/`               |
| `--note-dir DIR` | `dataset/note/` | Dir with `discharge.csv.gz` / `radiology.csv.gz`         |
| `--tables a,b`   | all             | Reload only the named tables (e.g. `prescriptions,emar`) |

---

## How to run

### One-time setup

```bash
# 1. Start the PostgreSQL container
docker compose up -d

# 2. Load the MIMIC-IV CSVs
python main.py load

# 3. Build indexes (once — makes everything below fast)
python main.py reindex
```

### Generate bundles

```bash
# Both pipelines, same 100 random patients
python main.py all --limit 100

# Just one pipeline
python main.py bundle --limit 50
python main.py fhir_blind --limit 50

# Specific patients
python main.py all --subject-ids 10000032,10000084
```

### Filtered cohorts

```bash
# All male patients → filtered/gender-male/{fhir,fhir_blind}/
python main.py all --gender male

# Male patients on the Medicine service
python main.py all --gender male --service medicine
#   → filtered/gender-male_service-med/{fhir,fhir_blind}/

# Female, age 65+, Medicare, admitted via the ER, capped at 500
python main.py all --gender female --min-age 65 --insurance medicare \
                   --admit-source emergency --limit 500

# Filters work on individual pipelines too
python main.py bundle   --gender male --service medicine   # → .../fhir/
python main.py fhir_blind --deceased --language english      # → .../fhir_blind/
```

### Run the dashboards

```bash
uvicorn web.app:app          --host 0.0.0.0 --port 8095 --reload  # full
uvicorn web.fhir_blind_app:app --host 0.0.0.0 --port 8096 --reload  # blind
```
