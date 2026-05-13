# Encounter Report — HADM 20764029

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 20764029 |
| Subject ID | 10029484 |
| Patient Sex | M |
| Patient Anchor Age (at anchor year) | 64 |
| Anchor Year | 2160 |
| Admission Time | 2160-11-08 04:16:00 |
| Discharge Time | 2160-11-11 11:40:00 |
| Admission Type | EW EMER. |
| Admission Location | EMERGENCY ROOM |
| Discharge Location | HOME |
| Insurance | Other |
| Language | ENGLISH |
| Marital Status | SINGLE |
| Race/Ethnicity | WHITE |
| ED Registration | 2160-11-07 19:15:00 |
| ED Departure | 2160-11-08 05:23:00 |
| In-Hospital Mortality | No |
| Date of Death (overall) | N/A |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| APR | 249 | OTHER GASTROENTERITIS, NAUSEA & VOMITING | 3.0 | 2.0 |
| HCFA | 391 | ESOPHAGITIS, GASTROENT & MISC DIGEST DISORDERS W MCC | N/A | N/A |

### Primary Diagnosis (seq_num = 1)

- **ICD-9 0088**: Intestinal infection due to other organism, not elsewhere classified

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2160-11-08 04:16:40 | N/A | MED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-9 `0088`: Intestinal infection due to other organism, not elsewhere classified
- (seq 2) ICD-9 `25012`: Diabetes with ketoacidosis, type II or unspecified type, uncontrolled
- (seq 3) ICD-9 `5849`: Acute kidney failure, unspecified
- (seq 4) ICD-9 `27651`: Dehydration
- (seq 5) ICD-9 `7802`: Syncope and collapse

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-9 | `0088` | Intestinal infection due to other organism, not elsewhere classified |
| 2 | ICD-9 | `25012` | Diabetes with ketoacidosis, type II or unspecified type, uncontrolled |
| 3 | ICD-9 | `5849` | Acute kidney failure, unspecified |
| 4 | ICD-9 | `27651` | Dehydration |
| 5 | ICD-9 | `7802` | Syncope and collapse |
| 6 | ICD-9 | `41400` | Coronary atherosclerosis of unspecified type of vessel, native or graft |
| 7 | ICD-9 | `V4582` | Percutaneous transluminal coronary angioplasty status |
| 8 | ICD-9 | `4019` | Unspecified essential hypertension |
| 9 | ICD-9 | `2724` | Other and unspecified hyperlipidemia |
| 10 | ICD-9 | `7245` | Backache, unspecified |

## 5. ICU Stays

| Stay ID | First Care Unit | Last Care Unit | ICU Admit | ICU Discharge | LOS (days) |
|---|---|---|---|---|---|
| 35396193 | Medical Intensive Care Unit (MICU) | Medical Intensive Care Unit (MICU) | 2160-11-08 05:23:00 | 2160-11-08 21:04:55 | 0.65 |

## 6. Escalation / Severity Indicators

The following critical conditions or interventions were detected:

- **Acute Kidney Injury** (ICD diagnosis)

## 7. Procedures and Interventions

_No ICD-coded procedures recorded._

### ICU Procedure Events (from `icu/procedureevents.csv.gz`)

- 20 Gauge (category: Access Lines - Peripheral, started: 2160-11-08 05:20:00, status: FinishedRunning)
- 18 Gauge (category: Access Lines - Peripheral, started: 2160-11-08 05:20:00, status: FinishedRunning)

## 8. Critical Findings (Charted Events)

- **Code Status** (first noted: 2160-11-08 05:39:00)
- **Dialysis patient** (first noted: 2160-11-08 04:57:00)

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2160-11-07 19:15:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2160-11-07 19:15:00 | Transfer | → Emergency Department (ED) |
| 2160-11-08 04:16:00 | Admission | Admitted from EMERGENCY ROOM (EW EMER.) |
| 2160-11-08 05:23:00 | ED Departure | Left Emergency Dept. |
| 2160-11-08 05:23:00 | ICU Admission | Medical Intensive Care Unit (MICU) (LOS: 0.7 days) |
| 2160-11-08 21:04:55 | Transfer | → Medicine (transfer) |
| 2160-11-11 11:40:00 | Discharge | To HOME |

## 10. Missing / Ambiguous Data

- No procedure ICD codes — procedures may not have been coded or were minor.

## 11. Manual Review Recommendation

**This encounter is flagged for manual review:**

- ICU stay present but no ICD procedures coded.
