# Encounter Report — HADM 24717014

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 24717014 |
| Subject ID | 10024043 |
| Patient Sex | M |
| Patient Anchor Age (at anchor year) | 67 |
| Anchor Year | 2117 |
| Admission Time | 2117-04-11 20:46:00 |
| Discharge Time | 2117-04-16 18:55:00 |
| Admission Type | EW EMER. |
| Admission Location | EMERGENCY ROOM |
| Discharge Location | HOME HEALTH CARE |
| Insurance | Medicare |
| Language | ENGLISH |
| Marital Status | SINGLE |
| Race/Ethnicity | BLACK/AFRICAN AMERICAN |
| ED Registration | 2117-04-11 17:23:00 |
| ED Departure | 2117-04-11 22:05:00 |
| In-Hospital Mortality | No |
| Date of Death (overall) | 2117-06-26 |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| APR | 42 | DEGENERATIVE NERVOUS SYSTEM DISORDERS EXC MULT SCLEROSIS | 3.0 | 3.0 |
| HCFA | 57 | DEGENERATIVE NERVOUS SYSTEM DISORDERS W/O MCC | N/A | N/A |

### Primary Diagnosis (seq_num = 1)

- **ICD-9 33520**: Amyotrophic lateral sclerosis

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2117-04-11 20:46:55 | N/A | NMED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-9 `33520`: Amyotrophic lateral sclerosis
- (seq 2) ICD-9 `2536`: Other disorders of neurohypophysis
- (seq 3) ICD-9 `5859`: Chronic kidney disease, unspecified
- (seq 4) ICD-9 `40390`: Hypertensive chronic kidney disease, unspecified, with chronic kidney disease stage I through stage IV, or unspecified
- (seq 5) ICD-9 `53081`: Esophageal reflux

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-9 | `33520` | Amyotrophic lateral sclerosis |
| 2 | ICD-9 | `2536` | Other disorders of neurohypophysis |
| 3 | ICD-9 | `5859` | Chronic kidney disease, unspecified |
| 4 | ICD-9 | `40390` | Hypertensive chronic kidney disease, unspecified, with chronic kidney disease stage I through stage IV, or unspecified |
| 5 | ICD-9 | `53081` | Esophageal reflux |
| 6 | ICD-9 | `72402` | Spinal stenosis, lumbar region, without neurogenic claudication |
| 7 | ICD-9 | `25000` | Diabetes mellitus without mention of complication, type II or unspecified type, not stated as uncontrolled |
| 8 | ICD-9 | `34690` | Migraine, unspecified, without mention of intractable migraine without mention of status migrainosus |
| 9 | ICD-9 | `V1083` | Personal history of other malignant neoplasm of skin |
| 10 | ICD-9 | `V1272` | Personal history of colonic polyps |
| 11 | ICD-9 | `V1582` | Personal history of tobacco use |
| 12 | ICD-9 | `V1202` | Personal history of poliomyelitis |
| 13 | ICD-9 | `V113` | Personal history of alcoholism |
| 14 | ICD-9 | `V454` | Arthrodesis status |

## 5. ICU Stays

| Stay ID | First Care Unit | Last Care Unit | ICU Admit | ICU Discharge | LOS (days) |
|---|---|---|---|---|---|
| 32374504 | Surgical Intensive Care Unit (SICU) | Surgical Intensive Care Unit (SICU) | 2117-04-11 22:05:00 | 2117-04-14 14:36:11 | 2.69 |

## 6. Escalation / Severity Indicators

The following critical conditions or interventions were detected:

- **Non-Invasive Ventilation (NIV/BiPAP)** (ICU procedure event)

## 7. Procedures and Interventions

_No ICD-coded procedures recorded._

### ICU Procedure Events (from `icu/procedureevents.csv.gz`)

- Non-invasive Ventilation (category: 2-Ventilation, started: 2117-04-11 21:57:00, status: FinishedRunning)
- 18 Gauge (category: Access Lines - Peripheral, started: 2117-04-11 22:00:00, status: FinishedRunning)
- CT scan (category: 5-Imaging, started: 2117-04-13 14:00:00, status: FinishedRunning)

## 8. Critical Findings (Charted Events)

- **Ventilator Mode** (first noted: 2117-04-11 22:00:00)
- **Code Status** (first noted: 2117-04-13 06:30:00)
- **Dialysis patient** (first noted: 2117-04-11 21:27:00)

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2117-04-11 17:23:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2117-04-11 17:23:00 | Transfer | → Emergency Department (ED) |
| 2117-04-11 20:46:00 | Admission | Admitted from EMERGENCY ROOM (EW EMER.) |
| 2117-04-11 22:05:00 | ED Departure | Left Emergency Dept. |
| 2117-04-11 22:05:00 | ICU Admission | Surgical Intensive Care Unit (SICU) (LOS: 2.7 days) |
| 2117-04-14 14:36:11 | Transfer | → Neurology (transfer) |
| 2117-04-14 16:29:38 | Transfer | → PACU (transfer) |
| 2117-04-14 16:29:58 | Transfer | → Neurology (transfer) |
| 2117-04-16 18:55:00 | Discharge | To HOME HEALTH CARE |

## 10. Missing / Ambiguous Data

- No procedure ICD codes — procedures may not have been coded or were minor.

## 11. Manual Review Recommendation

**This encounter is flagged for manual review:**

- ICU stay present but no ICD procedures coded.
