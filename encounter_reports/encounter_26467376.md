# Encounter Report — HADM 26467376

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 26467376 |
| Subject ID | 10003400 |
| Patient Sex | F |
| Patient Anchor Age (at anchor year) | 72 |
| Anchor Year | 2134 |
| Admission Time | 2136-12-09 14:44:00 |
| Discharge Time | 2136-12-15 16:00:00 |
| Admission Type | EW EMER. |
| Admission Location | EMERGENCY ROOM |
| Discharge Location | SKILLED NURSING FACILITY |
| Insurance | Medicare |
| Language | ENGLISH |
| Marital Status | MARRIED |
| Race/Ethnicity | BLACK/AFRICAN AMERICAN |
| ED Registration | 2136-12-09 13:16:00 |
| ED Departure | 2136-12-09 18:45:00 |
| In-Hospital Mortality | No |
| Date of Death (overall) | 2137-09-02 |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| APR | 201 | CARDIAC ARRHYTHMIA & CONDUCTION DISORDERS | 4.0 | 3.0 |
| HCFA | 308 | CARDIAC ARRHYTHMIA & CONDUCTION DISORDERS W MCC | N/A | N/A |

### Primary Diagnosis (seq_num = 1)

- **ICD-9 42731**: Atrial fibrillation

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2136-12-09 14:45:10 | N/A | MED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-9 `42731`: Atrial fibrillation
- (seq 2) ICD-9 `28412`: Other drug-induced pancytopenia
- (seq 3) ICD-9 `5849`: Acute kidney failure, unspecified
- (seq 4) ICD-9 `00845`: Intestinal infection due to Clostridium difficile
- (seq 5) ICD-9 `20300`: Multiple myeloma, without mention of having achieved remission

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-9 | `42731` | Atrial fibrillation |
| 2 | ICD-9 | `28412` | Other drug-induced pancytopenia |
| 3 | ICD-9 | `5849` | Acute kidney failure, unspecified |
| 4 | ICD-9 | `00845` | Intestinal infection due to Clostridium difficile |
| 5 | ICD-9 | `20300` | Multiple myeloma, without mention of having achieved remission |
| 6 | ICD-9 | `4589` | Hypotension, unspecified |
| 7 | ICD-9 | `2762` | Acidosis |
| 8 | ICD-9 | `2555` | Other adrenal hypofunction |
| 9 | ICD-9 | `42832` | Chronic diastolic heart failure |
| 10 | ICD-9 | `1543` | Malignant neoplasm of anus, unspecified site |
| 11 | ICD-9 | `1122` | Candidiasis of other urogenital sites |
| 12 | ICD-9 | `5934` | Other ureteric obstruction |
| 13 | ICD-9 | `2761` | Hyposmolality and/or hyponatremia |
| 14 | ICD-9 | `4280` | Congestive heart failure, unspecified |
| 15 | ICD-9 | `79092` | Abnormal coagulation profile |
| 16 | ICD-9 | `E9342` | Anticoagulants causing adverse effects in therapeutic use |
| 17 | ICD-9 | `40390` | Hypertensive chronic kidney disease, unspecified, with chronic kidney disease stage I through stage IV, or unspecified |
| 18 | ICD-9 | `5853` | Chronic kidney disease, Stage III (moderate) |
| 19 | ICD-9 | `V5861` | Long-term (current) use of anticoagulants |
| 20 | ICD-9 | `71596` | Osteoarthrosis, unspecified whether generalized or localized, lower leg |
| 21 | ICD-9 | `7905` | Other nonspecific abnormal serum enzyme levels |
| 22 | ICD-9 | `28529` | Anemia of other chronic disease |
| 23 | ICD-9 | `E9478` | Other drugs and medicinal substances causing adverse effects in therapeutic use |
| 24 | ICD-9 | `E8497` | Accidents occurring in residential institution |
| 25 | ICD-9 | `E9320` | Adrenal cortical steroids causing adverse effects in therapeutic use |
| 26 | ICD-9 | `78079` | Other malaise and fatigue |
| 27 | ICD-9 | `2768` | Hypopotassemia |
| 28 | ICD-9 | `27800` | Obesity, unspecified |
| 29 | ICD-9 | `V8532` | Body Mass Index 32.0-32.9, adult |

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
| 2136-12-09 13:16:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2136-12-09 13:16:00 | Transfer | → Emergency Department (ED) |
| 2136-12-09 14:44:00 | Admission | Admitted from EMERGENCY ROOM (EW EMER.) |
| 2136-12-09 17:53:42 | Transfer | → Cardiac Surgery (transfer) |
| 2136-12-09 18:45:00 | ED Departure | Left Emergency Dept. |
| 2136-12-11 17:57:35 | Transfer | → Cardiac Surgery (transfer) |
| 2136-12-15 16:00:00 | Discharge | To SKILLED NURSING FACILITY |

## 10. Missing / Ambiguous Data

- No procedure ICD codes — procedures may not have been coded or were minor.
- No ICU stay — patient managed on floor/step-down only.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
