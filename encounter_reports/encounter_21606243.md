# Encounter Report — HADM 21606243

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 21606243 |
| Subject ID | 10031404 |
| Patient Sex | F |
| Patient Anchor Age (at anchor year) | 82 |
| Anchor Year | 2113 |
| Admission Time | 2113-08-04 18:46:00 |
| Discharge Time | 2113-08-06 20:57:00 |
| Admission Type | URGENT |
| Admission Location | TRANSFER FROM HOSPITAL |
| Discharge Location | HOME |
| Insurance | Other |
| Language | ENGLISH |
| Marital Status | WIDOWED |
| Race/Ethnicity | WHITE |
| ED Registration | N/A |
| ED Departure | N/A |
| In-Hospital Mortality | No |
| Date of Death (overall) | N/A |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| APR | 207 | OTHER CIRCULATORY SYSTEM DIAGNOSES | 3.0 | 3.0 |
| HCFA | 315 | OTHER CIRCULATORY SYSTEM DIAGNOSES W CC | N/A | N/A |

### Primary Diagnosis (seq_num = 1)

- **ICD-10 I308**: Other forms of acute pericarditis

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2113-08-04 18:47:42 | N/A | CMED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-10 `I308`: Other forms of acute pericarditis
- (seq 2) ICD-10 `J90`: Pleural effusion, not elsewhere classified
- (seq 3) ICD-10 `N179`: Acute kidney failure, unspecified
- (seq 4) ICD-10 `E871`: Hypo-osmolality and hyponatremia
- (seq 5) ICD-10 `E860`: Dehydration

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-10 | `I308` | Other forms of acute pericarditis |
| 2 | ICD-10 | `J90` | Pleural effusion, not elsewhere classified |
| 3 | ICD-10 | `N179` | Acute kidney failure, unspecified |
| 4 | ICD-10 | `E871` | Hypo-osmolality and hyponatremia |
| 5 | ICD-10 | `E860` | Dehydration |
| 6 | ICD-10 | `I9589` | Other hypotension |
| 7 | ICD-10 | `J9811` | Atelectasis |
| 8 | ICD-10 | `R000` | Tachycardia, unspecified |
| 9 | ICD-10 | `I10` | Essential (primary) hypertension |
| 10 | ICD-10 | `E785` | Hyperlipidemia, unspecified |
| 11 | ICD-10 | `Z8781` | Personal history of (healed) traumatic fracture |
| 12 | ICD-10 | `L930` | Discoid lupus erythematosus |
| 13 | ICD-10 | `R002` | Palpitations |
| 14 | ICD-10 | `Z8639` | Personal history of other endocrine, nutritional and metabolic disease |
| 15 | ICD-10 | `Z87891` | Personal history of nicotine dependence |

## 5. ICU Stays

| Stay ID | First Care Unit | Last Care Unit | ICU Admit | ICU Discharge | LOS (days) |
|---|---|---|---|---|---|
| 35544374 | Coronary Care Unit (CCU) | Coronary Care Unit (CCU) | 2113-08-04 18:47:42 | 2113-08-05 23:45:02 | 1.21 |

## 6. Escalation / Severity Indicators

The following critical conditions or interventions were detected:

- **Acute Kidney Injury** (ICD diagnosis)

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2113-08-04 | ICD-10 | `0W9D3ZZ` | Drainage of Pericardial Cavity, Percutaneous Approach |

### ICU Procedure Events (from `icu/procedureevents.csv.gz`)

- 18 Gauge (category: Access Lines - Peripheral, started: 2113-08-04 21:44:00, status: FinishedRunning)
- Family updated by RN (category: 7-Communication, started: 2113-08-05 14:10:00, status: FinishedRunning)
- Pericardial Drain Removed (category: 4-Procedures, started: 2113-08-05 14:10:00, status: FinishedRunning)

## 8. Critical Findings (Charted Events)

- **Code Status** (first noted: 2113-08-04 21:32:00)
- **Dialysis patient** (first noted: 2113-08-05 03:07:00)

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2113-08-04 18:46:00 | Admission | Admitted from TRANSFER FROM HOSPITAL (URGENT) |
| 2113-08-04 18:47:42 | ICU Admission | Coronary Care Unit (CCU) (LOS: 1.2 days) |
| 2113-08-05 23:45:02 | Transfer | → Vascular (transfer) |
| 2113-08-06 20:57:00 | Discharge | To HOME |

## 10. Missing / Ambiguous Data

- No ED registration time — admission may not have gone through ED.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
