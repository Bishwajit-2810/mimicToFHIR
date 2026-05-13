# Encounter Report — HADM 27984218

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 27984218 |
| Subject ID | 10020640 |
| Patient Sex | F |
| Patient Anchor Age (at anchor year) | 91 |
| Anchor Year | 2153 |
| Admission Time | 2153-02-13 00:22:00 |
| Discharge Time | 2153-02-20 13:52:00 |
| Admission Type | EW EMER. |
| Admission Location | EMERGENCY ROOM |
| Discharge Location | SKILLED NURSING FACILITY |
| Insurance | Other |
| Language | ENGLISH |
| Marital Status | WIDOWED |
| Race/Ethnicity | WHITE |
| ED Registration | 2153-02-12 21:59:00 |
| ED Departure | 2153-02-13 01:38:00 |
| In-Hospital Mortality | No |
| Date of Death (overall) | 2154-02-04 |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| APR | 139 | OTHER PNEUMONIA | 3.0 | 3.0 |
| HCFA | 193 | SIMPLE PNEUMONIA & PLEURISY W MCC | N/A | N/A |

### Primary Diagnosis (seq_num = 1)

- **ICD-9 486**: Pneumonia, organism unspecified

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2153-02-13 00:23:03 | N/A | MED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-9 `486`: Pneumonia, organism unspecified
- (seq 2) ICD-9 `34831`: Metabolic encephalopathy
- (seq 3) ICD-9 `2760`: Hyperosmolality and/or hypernatremia
- (seq 4) ICD-9 `2639`: Unspecified protein-calorie malnutrition
- (seq 5) ICD-9 `29411`: Dementia in conditions classified elsewhere with behavioral disturbance

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-9 | `486` | Pneumonia, organism unspecified |
| 2 | ICD-9 | `34831` | Metabolic encephalopathy |
| 3 | ICD-9 | `2760` | Hyperosmolality and/or hypernatremia |
| 4 | ICD-9 | `2639` | Unspecified protein-calorie malnutrition |
| 5 | ICD-9 | `29411` | Dementia in conditions classified elsewhere with behavioral disturbance |
| 6 | ICD-9 | `2762` | Acidosis |
| 7 | ICD-9 | `3310` | Alzheimer's disease |
| 8 | ICD-9 | `2810` | Pernicious anemia |
| 9 | ICD-9 | `43820` | Late effects of cerebrovascular disease, hemiplegia affecting unspecified side |
| 10 | ICD-9 | `5990` | Urinary tract infection, site not specified |
| 11 | ICD-9 | `V643` | Procedure not carried out for other reasons |
| 12 | ICD-9 | `71590` | Osteoarthrosis, unspecified whether generalized or localized, site unspecified |
| 13 | ICD-9 | `4019` | Unspecified essential hypertension |
| 14 | ICD-9 | `41401` | Coronary atherosclerosis of native coronary artery |
| 15 | ICD-9 | `4439` | Peripheral vascular disease, unspecified |
| 16 | ICD-9 | `78321` | Loss of weight |
| 17 | ICD-9 | `311` | Depressive disorder, not elsewhere classified |
| 18 | ICD-9 | `79902` | Hypoxemia |
| 19 | ICD-9 | `79092` | Abnormal coagulation profile |
| 20 | ICD-9 | `25002` | Diabetes mellitus without mention of complication, type II or unspecified type, uncontrolled |
| 21 | ICD-9 | `2768` | Hypopotassemia |

## 5. ICU Stays

| Stay ID | First Care Unit | Last Care Unit | ICU Admit | ICU Discharge | LOS (days) |
|---|---|---|---|---|---|
| 30849778 | Medical/Surgical Intensive Care Unit (MICU/SICU) | Medical/Surgical Intensive Care Unit (MICU/SICU) | 2153-02-13 01:38:00 | 2153-02-15 15:00:57 | 2.56 |

## 6. Escalation / Severity Indicators

The following critical conditions or interventions were detected:

- **Pneumonia** (ICD diagnosis)

## 7. Procedures and Interventions

_No ICD-coded procedures recorded._

### ICU Procedure Events (from `icu/procedureevents.csv.gz`)

- 18 Gauge (category: Access Lines - Peripheral, started: 2153-02-13 01:58:00, status: FinishedRunning)
- 20 Gauge (category: Access Lines - Peripheral, started: 2153-02-13 02:00:00, status: FinishedRunning)
- 22 Gauge (category: Access Lines - Peripheral, started: 2153-02-13 02:01:00, status: FinishedRunning)
- Family updated by RN (category: 7-Communication, started: 2153-02-14 08:41:00, status: FinishedRunning)
- PICC Line (category: Access Lines - Invasive, started: 2153-02-14 11:00:00, status: FinishedRunning)

## 8. Critical Findings (Charted Events)

- **Code Status** (first noted: 2153-02-13 05:27:00)
- **Seizure Activity** (first noted: 2153-02-13 20:00:00)

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2153-02-12 21:59:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2153-02-12 21:59:00 | Transfer | → Emergency Department (ED) |
| 2153-02-13 00:22:00 | Admission | Admitted from EMERGENCY ROOM (EW EMER.) |
| 2153-02-13 01:38:00 | ED Departure | Left Emergency Dept. |
| 2153-02-13 01:38:00 | ICU Admission | Medical/Surgical Intensive Care Unit (MICU/SICU) (LOS: 2.6 days) |
| 2153-02-15 15:00:57 | Transfer | → Med/Surg/GYN (transfer) |
| 2153-02-20 13:52:00 | Discharge | To SKILLED NURSING FACILITY |

## 10. Missing / Ambiguous Data

- No procedure ICD codes — procedures may not have been coded or were minor.

## 11. Manual Review Recommendation

**This encounter is flagged for manual review:**

- ICU stay present but no ICD procedures coded.
