# Clinical Dashboard — How to Use

This guide covers running the dashboards and navigating the patient data.

## Starting the Dashboards

From the project root:

```bash
# Full dashboard — complete clinical data (port 8095)
uvicorn web.app:app --host 0.0.0.0 --port 8095 --reload

# GoldData dashboard — latest encounter blinded: no diagnoses, no procedures, no medications, no notes (port 8096)
uvicorn web.golddata_app:app --host 0.0.0.0 --port 8096 --reload

# Testing dashboard — latest encounter blinded + notes restored (port 8097)
uvicorn web.testing_app:app --host 0.0.0.0 --port 8097 --reload
```

| URL                     | Pipeline | Latest Conditions | Latest Meds | Notes |
| ----------------------- | -------- | :---------------: | :---------: | :---: |
| <http://localhost:8095> | Full     | ✓                 | ✓           | ✓     |
| <http://localhost:8096> | GoldData | ✗                 | ✗           | ✗     |
| <http://localhost:8097> | Testing  | ✗                 | ✗           | ✓     |

**Blinding applies only to the most recent encounter.** Prior encounters always
include full diagnoses, medications, and notes on all three dashboards.

Press **Ctrl + C** to stop the server.

> **Tip:** Add `--reload` only during development — it restarts the server on
> file changes but uses more resources.

---

## Dataset Banner

A coloured banner appears below the patient info bar on every page. It identifies
which pipeline is active and shows inclusion chips for each resource type:

- **Blue banner** — Full pipeline (all data, no blinding)
- **Amber banner** — GoldData pipeline (latest encounter blinded: vitals/labs only; no conditions, procedures, medications, or notes)
- **Green banner** — Testing pipeline (latest encounter blinded + clinical notes)

Each chip is green when that resource type is included for the latest encounter,
or grey with strikethrough when excluded. Conditions, Procedures, and Medications
chips will show as excluded on the GoldData and Testing dashboards — this is
correct and expected for the most recent visit.

---

## Selecting a Patient

The **Select Patient** dropdown in the top-right header lists all available
patients by their MIMIC-IV subject ID. By default the pipelines load random
patients — rerun `python main.py all` to get a different cohort, or pass cohort
filters (e.g. `python main.py all --gender male --service medicine`) to extract a
targeted subset into `filtered/<slug>/`. See the project README for the full
list of filter flags.

The patient info bar shows a quick summary:

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

## Dashboard Tabs

The dashboard has five tabs. Click any tab to switch views.

---

### Tab 1 — Patient Overview

A snapshot of the patient's current clinical status.

**Demographics** — subject ID, gender, birth date, age, race, ethnicity, birth
sex, marital status, language, anchor year group, deceased date.

**Vitals** — most recent recorded value for each vital sign type, colour-coded
blue (normal) or red (out-of-range):

| Vital            | LOINC   | Normal Range   |
| ---------------- | ------- | -------------- |
| Heart Rate       | 8867-4  | 60 – 100 bpm   |
| Systolic BP      | 8480-6  | 90 – 140 mmHg  |
| Diastolic BP     | 8462-4  | 60 – 90 mmHg   |
| Mean BP          | 8478-0  | 70 – 100 mmHg  |
| Respiratory Rate | 9279-1  | 12 – 20 /min   |
| Temperature      | 8310-5  | 97.0 – 99.5 °F |
| SpO2             | 59408-5 | 95 – 100 %     |
| Weight           | 29463-7 | —              |
| Height           | 8302-2  | —              |

**Current Medications** — all `MedicationRequest` resources for prior encounters,
deduplicated by drug name with dose and route. Shows "No data recorded" for the
latest encounter on GoldData and Testing dashboards.

**Past Medical History** — all `Condition` resources with ICD-9/10 codes and
clinical status. Latest encounter conditions are excluded on GoldData and Testing.

**Suggested Tests** — microbiology and diagnostic orders from `DiagnosticReport`
resources, sorted by most recent first.

**Lab Report Values** — searchable table of all laboratory `Observation` results.
Use the **Filter…** input to search by test name.

---

### Tab 2 — Chief Complaint

The primary reason for the patient's **most recent** hospital encounter.

- Chief complaint derived from the primary ICD-coded condition for the encounter.
- **Admission Details** — encounter type, admit/discharge dates, admit source,
  discharge disposition, insurance.
- **Associated Diagnoses** — all conditions linked to that encounter.

Shows "No data recorded" on GoldData and Testing dashboards — the latest
encounter's conditions are blinded.

---

### Tab 3 — Diagnosis & Treatment

**Suggested Diagnoses** — all `Condition` resources in ICD sequence order.
Each entry shows the condition name, ICD code, and clinical status badge.
Latest encounter diagnoses are absent on GoldData and Testing.

**Treatment & Medications** — full medication list with drug name, dose, and route.
Latest encounter prescriptions are absent on GoldData and Testing.

**Procedures Performed** — all `Procedure` resources with ICD descriptions and dates.
Latest encounter procedures are absent on GoldData and Testing (prior encounter procedures are shown).

---

### Tab 4 — Encounters

A timeline of all hospital, ICU, and ED visits, sorted most-recent first.

Each **hospital encounter** is a collapsible card. Click the header to expand it.
Expanded view shows admit source, discharge disposition, insurance, and ICU stays.

**ICU stays** appear as nested blue sub-cards inside their parent hospital
encounter, showing care unit, admission/discharge times, and length of stay.

**ED stays** appear as separate orange cards showing arrival/departure times,
triage information, and ED vitals.

Each encounter card also contains:

- A vitals summary for that specific encounter
- Lab results recorded during that encounter
- Clinical notes (discharge summary + radiology reports) — shown for prior
  encounters on all pipelines; for the latest encounter only on Full and Testing

The **Synthesized clinical note** box at the bottom of each encounter card is
built entirely from the FHIR resources in the bundle (vitals, labs, procedures,
microbiology). It is generated locally from parsed data — not stored text. On
Full and Testing bundles where real `DocumentReference` resources are present,
a "Real notes available" badge appears and the actual notes are shown below.

---

### Tab 5 — Clinical Notes

Full text of all `DocumentReference` resources for the patient:

- **Discharge Summary** (LOINC 18842-5) — the attending's discharge note
- **Radiology Report** (LOINC 18726-0) — imaging interpretation notes

Each note shows the encounter date, author (provider ID), and full text with
section-level detail extensions where available. Notes are searchable using the
**Search notes…** input.

This tab shows notes for all prior encounters on all three dashboards. For the
latest encounter, notes appear on Full and Testing but are excluded on GoldData.

---

## API Endpoints

The dashboard is backed by a FastAPI service you can query directly:

| Endpoint                 | Description                                   |
| ------------------------ | --------------------------------------------- |
| `GET /api/info`          | Dataset metadata and bundle count             |
| `GET /api/patients`      | List of all patient IDs                       |
| `GET /api/patients/{id}` | Full structured clinical data for one patient |
| `GET /`                  | Serves the dashboard (index.html)             |

Example:

```bash
curl http://localhost:8095/api/patients/10000032 | python3 -m json.tool | head -60
curl http://localhost:8095/api/info
```

---

## Performance Notes

- Parsed bundles are cached in memory (LRU, 15–20 patients per dashboard). Switching between
  recently viewed patients is instant.
- The first load of a patient parses their full FHIR bundle from disk.
- No running database is required — dashboards read static JSON files only.
