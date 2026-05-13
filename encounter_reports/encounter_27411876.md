# Encounter Report — HADM 27411876

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 27411876 |
| Subject ID | 10004733 |
| Patient Sex | M |
| Patient Anchor Age (at anchor year) | 51 |
| Anchor Year | 2174 |
| Admission Time | 2174-12-04 11:28:00 |
| Discharge Time | 2174-12-27 14:00:00 |
| Admission Type | URGENT |
| Admission Location | TRANSFER FROM HOSPITAL |
| Discharge Location | HOME HEALTH CARE |
| Insurance | Medicaid |
| Language | ENGLISH |
| Marital Status | SINGLE |
| Race/Ethnicity | UNKNOWN |
| ED Registration | N/A |
| ED Departure | N/A |
| In-Hospital Mortality | No |
| Date of Death (overall) | N/A |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| APR | 52 | ALTERATION IN CONSCIOUSNESS | 4.0 | 4.0 |
| HCFA | 70 | NONSPECIFIC CEREBROVASCULAR DISORDERS W MCC | N/A | N/A |

### Primary Diagnosis (seq_num = 1)

- **ICD-9 34839**: Other encephalopathy

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2174-12-04 11:28:24 | N/A | MED |
| 2174-12-14 08:03:11 | MED | NMED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-9 `34839`: Other encephalopathy
- (seq 2) ICD-9 `43491`: Cerebral artery occlusion, unspecified with cerebral infarction
- (seq 3) ICD-9 `5070`: Pneumonitis due to inhalation of food or vomitus
- (seq 4) ICD-9 `48249`: Other Staphylococcus pneumonia
- (seq 5) ICD-9 `5829`: Chronic glomerulonephritis with unspecified pathological lesion in kidney

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-9 | `34839` | Other encephalopathy |
| 2 | ICD-9 | `43491` | Cerebral artery occlusion, unspecified with cerebral infarction |
| 3 | ICD-9 | `5070` | Pneumonitis due to inhalation of food or vomitus |
| 4 | ICD-9 | `48249` | Other Staphylococcus pneumonia |
| 5 | ICD-9 | `5829` | Chronic glomerulonephritis with unspecified pathological lesion in kidney |
| 6 | ICD-9 | `78722` | Dysphagia, oropharyngeal phase |
| 7 | ICD-9 | `5849` | Acute kidney failure, unspecified |
| 8 | ICD-9 | `99731` | Ventilator associated pneumonia |
| 9 | ICD-9 | `7907` | Bacteremia |
| 10 | ICD-9 | `40300` | Hypertensive chronic kidney disease, malignant, with chronic kidney disease stage I through stage IV, or unspecified |
| 11 | ICD-9 | `5781` | Blood in stool |
| 12 | ICD-9 | `2760` | Hyperosmolality and/or hypernatremia |
| 13 | ICD-9 | `34290` | Hemiplegia, unspecified, affecting unspecified side |
| 14 | ICD-9 | `5859` | Chronic kidney disease, unspecified |
| 15 | ICD-9 | `7904` | Nonspecific elevation of levels of transaminase or lactic acid dehydrogenase [LDH] |
| 16 | ICD-9 | `0416` | Proteus (mirabilis) (morganii) infection in conditions classified elsewhere and of unspecified site |
| 17 | ICD-9 | `45829` | Other iatrogenic hypotension |
| 18 | ICD-9 | `E9383` | Intravenous anesthetics causing adverse effects in therapeutic use |
| 19 | ICD-9 | `3129` | Unspecified disturbance of conduct |
| 20 | ICD-9 | `7850` | Tachycardia, unspecified |
| 21 | ICD-9 | `V4987` | Physical restraints status |
| 22 | ICD-9 | `56210` | Diverticulosis of colon (without mention of hemorrhage) |
| 23 | ICD-9 | `78052` | Insomnia, unspecified |
| 24 | ICD-9 | `28529` | Anemia of other chronic disease |
| 25 | ICD-9 | `28521` | Anemia in chronic kidney disease |
| 26 | ICD-9 | `4739` | Unspecified sinusitis (chronic) |
| 27 | ICD-9 | `E8798` | Other specified procedures as the cause of abnormal reaction of patient, or of later complication, without mention of misadventure at time of procedure |
| 28 | ICD-9 | `30590` | Other, mixed, or unspecified drug abuse, unspecified |
| 29 | ICD-9 | `30390` | Other and unspecified alcohol dependence, unspecified |
| 30 | ICD-9 | `30000` | Anxiety state, unspecified |

## 5. ICU Stays

| Stay ID | First Care Unit | Last Care Unit | ICU Admit | ICU Discharge | LOS (days) |
|---|---|---|---|---|---|
| 39635619 | Medical/Surgical Intensive Care Unit (MICU/SICU) | Medical/Surgical Intensive Care Unit (MICU/SICU) | 2174-12-04 11:28:24 | 2174-12-12 20:03:01 | 8.36 |

## 6. Escalation / Severity Indicators

The following critical conditions or interventions were detected:

- **Acute Kidney Injury** (ICD diagnosis)
- **Invasive Mechanical Ventilation** (ICU procedure event)
- **Pneumonia** (ICD diagnosis)

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2174-12-04 | ICD-9 | `9671` | Continuous invasive mechanical ventilation for less than 96 consecutive hours |
| 2 | 2174-12-07 | ICD-9 | `5523` | Closed [percutaneous] [needle] biopsy of kidney |
| 3 | 2174-12-20 | ICD-9 | `4513` | Other endoscopy of small intestine |
| 4 | 2174-12-20 | ICD-9 | `4523` | Colonoscopy |
| 5 | 2174-12-07 | ICD-9 | `3897` | Central venous catheter placement with guidance |
| 6 | 2174-12-07 | ICD-9 | `3322` | Fiber-optic bronchoscopy |
| 7 | 2174-12-10 | ICD-9 | `966` | Enteral infusion of concentrated nutritional substances |

### ICU Procedure Events (from `icu/procedureevents.csv.gz`)

- Multi Lumen (category: Access Lines - Invasive, started: 2174-12-04 12:00:00, status: FinishedRunning)
- Invasive Ventilation (category: 2-Ventilation, started: 2174-12-04 12:25:00, status: FinishedRunning)
- EEG (category: 4-Procedures, started: 2174-12-05 03:05:00, status: FinishedRunning)
- Blood Cultured (category: 6-Cultures, started: 2174-12-05 03:05:00, status: FinishedRunning)
- Transthoracic Echo (category: 5-Imaging, started: 2174-12-05 09:00:00, status: FinishedRunning)
- 18 Gauge (category: Access Lines - Peripheral, started: 2174-12-05 11:00:00, status: FinishedRunning)
- Magnetic Resonance Imaging (category: 5-Imaging, started: 2174-12-05 18:00:00, status: FinishedRunning)
- EKG (category: 4-Procedures, started: 2174-12-05 23:47:00, status: FinishedRunning)
- Chest X-Ray (category: 5-Imaging, started: 2174-12-07 10:28:00, status: FinishedRunning)
- PICC Line (category: Access Lines - Invasive, started: 2174-12-07 11:02:00, status: FinishedRunning)
- Bronchoscopy (category: 4-Procedures, started: 2174-12-07 12:07:00, status: FinishedRunning)
- Extubation (category: 1-Intubation/Extubation, started: 2174-12-07 16:20:00, status: FinishedRunning)

## 8. Critical Findings (Charted Events)

- **Ventilator Mode** (first noted: 2174-12-04 12:00:00)
- **Ventilator Type** (first noted: 2174-12-04 12:00:00)
- **Ventilator Tank #1** (first noted: 2174-12-04 20:00:00)
- **Known difficult intubation** (first noted: 2174-12-04 12:00:00)
- **Code Status** (first noted: 2174-12-08 21:07:00)
- **Dialysis patient** (first noted: 2174-12-04 16:54:00)

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2174-12-04 11:28:00 | Admission | Admitted from TRANSFER FROM HOSPITAL (URGENT) |
| 2174-12-04 11:28:24 | ICU Admission | Medical/Surgical Intensive Care Unit (MICU/SICU) (LOS: 8.4 days) |
| 2174-12-12 20:03:01 | Transfer | → Medicine (transfer) |
| 2174-12-13 17:47:18 | Transfer | → Neurology (transfer) |
| 2174-12-13 22:18:45 | Transfer | → Neurology (transfer) |
| 2174-12-25 15:01:56 | Transfer | → Neurology (transfer) |
| 2174-12-27 14:00:00 | Discharge | To HOME HEALTH CARE |

## 10. Missing / Ambiguous Data

- No ED registration time — admission may not have gone through ED.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
