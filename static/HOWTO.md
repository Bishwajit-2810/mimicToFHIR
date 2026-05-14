# Clinical Dashboard — How to Use

This guide covers running the dashboards and navigating the patient data.

## Starting the Dashboards

From the project root:

```bash
# Standard dashboard — full clinical data (port 8095)
uvicorn web.app:app --host 0.0.0.0 --port 8095 --reload

# GoldData dashboard — latest-encounter diagnoses withheld (port 8096)
uvicorn web.golddata_app:app --host 0.0.0.0 --port 8096 --reload
```

| URL                     | Data                                           |
| ----------------------- | ---------------------------------------------- |
| <http://localhost:8095> | Full data — all diagnoses and medications      |
| <http://localhost:8096> | Latest encounter is diagnosis/treatment-blind  |

`fhir_bundles/` is already included in the repository so the standard dashboard
works immediately without running any ETL.

Press **Ctrl + C** to stop the server.

> **Tip:** Add `--reload` only during development — it restarts the server on
> file changes but uses more resources.

---

## Optional: Use a Different Port

```bash
# Check what is using port 8095
fuser 8095/tcp

# Kill it, or pick another port
uvicorn web.app:app --host 0.0.0.0 --port 8097
```

---

## Selecting a Patient

The **Select Patient** dropdown in the top-right header lists all 100 demo
patients by their MIMIC-IV subject ID. Choose any patient to load their full
clinical record.

The patient info bar below the header shows a quick summary:

| Field          | Description                                              |
| -------------- | -------------------------------------------------------- |
| Patient ID     | MIMIC-IV subject identifier                              |
| Gender & Age   | Sex and approximate age at time of most recent encounter |
| Race           | Self-reported race (de-identified)                       |
| MRN            | Medical record number (same as subject ID here)          |
| Deceased badge | Shown in red if a death date is recorded                 |

> **Note:** All dates in MIMIC-IV are shifted forward by a random offset per
> patient to protect privacy. Relative time between events is preserved;
> absolute years are not real.

---

## Dashboard Sections

The dashboard is divided into four tabs. Click any tab to switch views.

---

### Tab 1 — Patient Overview

A full snapshot of the patient's current clinical status.

#### Demographics

Key demographic fields pulled from the FHIR `Patient` resource:

- Subject ID, gender, birth date, approximate age
- Race, ethnicity, birth sex, marital status, language
- Anchor year group (the real-world decade the data belongs to)
- Deceased date (if applicable)

#### Vitals

Displays the **most recent recorded value** for each vital sign type:

| Vital            | LOINC Code | Normal Range   |
| ---------------- | ---------- | -------------- |
| Heart Rate       | 8867-4     | 60 – 100 bpm   |
| Systolic BP      | 8480-6     | 90 – 140 mmHg  |
| Diastolic BP     | 8462-4     | 60 – 90 mmHg   |
| Respiratory Rate | 9279-1     | 12 – 20 /min   |
| Temperature      | 8310-5     | 97.0 – 99.5 °F |
| SpO2             | 59408-5    | 95 – 100 %     |
| Weight           | 29463-7    | —              |
| Height           | 8302-2     | —              |

Cards are coloured **blue** for normal and **red** for out-of-range values.

#### Allergies

This dataset does not include `AllergyIntolerance` resources. The section
notes "No known allergies recorded."

#### Current Medications

Lists all `MedicationRequest` resources for the patient, deduplicated by drug
name. Shows dose, route, and prescription period.

#### Past Medical History

All `Condition` resources coded with ICD-9 or ICD-10, with clinical status
(active / resolved).

#### Suggested Tests

Microbiology and other diagnostic orders from `DiagnosticReport` resources,
sorted by most recent first.

#### Lab Report Values

A searchable table of all laboratory `Observation` results (most recent value
per test):

- **Result** — numeric value and unit
- **Flag** — `↑` high, `↓` low, `!` abnormal (shown in red/blue)
- **Ref Range** — reference interval when available
- **Date** — date/time of the result

Use the **Filter…** input in the section header to search by test name.

---

### Tab 2 — Chief Complaint

The primary reason for the patient's **most recent** hospital encounter.

- The chief complaint is derived from the primary ICD-coded condition linked
  to the most recent encounter.
- **Admission Details** — encounter type, admit/discharge dates, admit source,
  discharge disposition, insurance.
- **Associated Diagnoses** — all conditions linked to that same encounter.

---

### Tab 3 — Diagnosis & Treatment

A validation view for reviewing the clinical picture and planned care.

#### Suggested Diagnoses

All `Condition` resources ranked in the order they appear in the FHIR bundle
(which mirrors the ICD sequence number from the source data). Each entry shows:

- Full condition name
- ICD code and code system (ICD-9 or ICD-10)
- Clinical status badge

#### Treatment & Medications

Full medication list with drug name, dose, and route.

#### Procedures Performed

All `Procedure` resources with ICD code descriptions and performed dates.

---

### Tab 4 — Encounters

A complete timeline of all hospital visits, sorted most-recent first.

Each **hospital encounter** is a collapsible card. Click anywhere on the header
row to expand or collapse it.

Expanded view shows:

| Field                 | Description                                      |
| --------------------- | ------------------------------------------------ |
| Admit Source          | Where the patient came from (e.g., ED, transfer) |
| Discharge Disposition | Where the patient went on discharge              |
| Insurance             | Payer type recorded at admission                 |

**ICU stays** are nested inside their parent hospital encounter as blue
sub-cards, showing the care unit, admission/discharge times, and length of
stay in days.

---

## API Endpoints

The dashboard is backed by a FastAPI service. You can query the API directly
while the server is running:

| Endpoint                 | Description                                   |
| ------------------------ | --------------------------------------------- |
| `GET /api/patients`      | List of all patient IDs                       |
| `GET /api/patients/{id}` | Full structured clinical data for one patient |
| `GET /`                  | Serves the dashboard (index.html)             |
| `GET /static/{file}`     | Static assets (JS, CSS, this file)            |

Example:

```bash
curl http://localhost:8095/api/patients/10000032 | python3 -m json.tool | head -60
```

The GoldData dashboard (port 8096) adds a `golddata` key to each patient
response containing `blindedHadm` and `excludedConditions`.

---

## Performance Notes

- Parsed bundles are cached in memory (LRU, 15 patients). Switching between
  recently viewed patients is instant.
- The first load of a patient parses their full FHIR bundle (~2.75 MB average).
  Expect ~0.5–1 s on first open.
- The server reads the static JSON files in `fhir_bundles/` directly — no
  running database required.
