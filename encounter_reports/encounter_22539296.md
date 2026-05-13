# Encounter Report — HADM 22539296

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 22539296 |
| Subject ID | 10012853 |
| Patient Sex | F |
| Patient Anchor Age (at anchor year) | 91 |
| Anchor Year | 2175 |
| Admission Time | 2176-06-06 18:09:00 |
| Discharge Time | 2176-06-08 18:30:00 |
| Admission Type | EW EMER. |
| Admission Location | EMERGENCY ROOM |
| Discharge Location | HOME |
| Insurance | Medicare |
| Language | ENGLISH |
| Marital Status | WIDOWED |
| Race/Ethnicity | BLACK/AFRICAN AMERICAN |
| ED Registration | 2176-06-06 13:33:00 |
| ED Departure | 2176-06-06 20:18:00 |
| In-Hospital Mortality | No |
| Date of Death (overall) | N/A |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| HCFA | 684 | RENAL FAILURE W/O CC/MCC | N/A | N/A |

### Primary Diagnosis (seq_num = 1)

- **ICD-9 5849**: Acute kidney failure, unspecified

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2176-06-06 18:09:39 | N/A | MED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-9 `5849`: Acute kidney failure, unspecified
- (seq 2) ICD-9 `42731`: Atrial fibrillation
- (seq 3) ICD-9 `25000`: Diabetes mellitus without mention of complication, type II or unspecified type, not stated as uncontrolled
- (seq 4) ICD-9 `59654`: Neurogenic bladder NOS
- (seq 5) ICD-9 `2411`: Nontoxic multinodular goiter

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-9 | `5849` | Acute kidney failure, unspecified |
| 2 | ICD-9 | `42731` | Atrial fibrillation |
| 3 | ICD-9 | `25000` | Diabetes mellitus without mention of complication, type II or unspecified type, not stated as uncontrolled |
| 4 | ICD-9 | `59654` | Neurogenic bladder NOS |
| 5 | ICD-9 | `2411` | Nontoxic multinodular goiter |
| 6 | ICD-9 | `27651` | Dehydration |
| 7 | ICD-9 | `2809` | Iron deficiency anemia, unspecified |
| 8 | ICD-9 | `2724` | Other and unspecified hyperlipidemia |
| 9 | ICD-9 | `27800` | Obesity, unspecified |
| 10 | ICD-9 | `5589` | Other and unspecified noninfectious gastroenteritis and colitis |
| 11 | ICD-9 | `40390` | Hypertensive chronic kidney disease, unspecified, with chronic kidney disease stage I through stage IV, or unspecified |
| 12 | ICD-9 | `5853` | Chronic kidney disease, Stage III (moderate) |
| 13 | ICD-9 | `7919` | Other nonspecific findings on examination of urine |
| 14 | ICD-9 | `4439` | Peripheral vascular disease, unspecified |
| 15 | ICD-9 | `4414` | Abdominal aneurysm without mention of rupture |
| 16 | ICD-9 | `73300` | Osteoporosis, unspecified |
| 17 | ICD-9 | `3051` | Tobacco use disorder |
| 18 | ICD-9 | `V8521` | Body Mass Index 25.0-25.9, adult |
| 19 | ICD-9 | `V5866` | Long-term (current) use of aspirin |
| 20 | ICD-9 | `V1255` | Personal history of pulmonary embolism |
| 21 | ICD-9 | `V5861` | Long-term (current) use of anticoagulants |
| 22 | ICD-9 | `V1254` | Personal history of transient ischemic attack (TIA), and cerebral infarction without residual deficits |

## 5. ICU Stays

_No ICU stay recorded for this admission._

## 6. Escalation / Severity Indicators

The following critical conditions or interventions were detected:

- **Acute Kidney Injury** (ICD diagnosis)

## 7. Procedures and Interventions

_No ICD-coded procedures recorded._


## 8. Critical Findings (Charted Events)

_No critical chart events detected._

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2176-06-06 13:33:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2176-06-06 13:33:00 | Transfer | → Emergency Department (ED) |
| 2176-06-06 18:09:00 | Admission | Admitted from EMERGENCY ROOM (EW EMER.) |
| 2176-06-06 20:18:00 | ED Departure | Left Emergency Dept. |
| 2176-06-08 18:30:00 | Discharge | To HOME |

## 10. Missing / Ambiguous Data

- No procedure ICD codes — procedures may not have been coded or were minor.
- No ICU stay — patient managed on floor/step-down only.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
