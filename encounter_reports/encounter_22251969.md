# Encounter Report — HADM 22251969

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 22251969 |
| Subject ID | 10040025 |
| Patient Sex | F |
| Patient Anchor Age (at anchor year) | 64 |
| Anchor Year | 2143 |
| Admission Time | 2147-08-03 02:58:00 |
| Discharge Time | 2147-08-06 16:50:00 |
| Admission Type | OBSERVATION ADMIT |
| Admission Location | EMERGENCY ROOM |
| Discharge Location | HOME |
| Insurance | Other |
| Language | ENGLISH |
| Marital Status | DIVORCED |
| Race/Ethnicity | WHITE |
| ED Registration | 2147-08-02 18:14:00 |
| ED Departure | 2147-08-03 02:41:00 |
| In-Hospital Mortality | No |
| Date of Death (overall) | 2148-02-07 |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| HCFA | 683 | RENAL FAILURE W CC | N/A | N/A |

### Primary Diagnosis (seq_num = 1)

- **ICD-10 N170**: Acute kidney failure with tubular necrosis

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2147-08-03 03:01:07 | N/A | MED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-10 `N170`: Acute kidney failure with tubular necrosis
- (seq 2) ICD-10 `I130`: Hypertensive heart and chronic kidney disease with heart failure and stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease
- (seq 3) ICD-10 `E1122`: Type 2 diabetes mellitus with diabetic chronic kidney disease
- (seq 4) ICD-10 `I5032`: Chronic diastolic (congestive) heart failure
- (seq 5) ICD-10 `I4891`: Unspecified atrial fibrillation

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-10 | `N170` | Acute kidney failure with tubular necrosis |
| 2 | ICD-10 | `I130` | Hypertensive heart and chronic kidney disease with heart failure and stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease |
| 3 | ICD-10 | `E1122` | Type 2 diabetes mellitus with diabetic chronic kidney disease |
| 4 | ICD-10 | `I5032` | Chronic diastolic (congestive) heart failure |
| 5 | ICD-10 | `I4891` | Unspecified atrial fibrillation |
| 6 | ICD-10 | `E860` | Dehydration |
| 7 | ICD-10 | `E871` | Hypo-osmolality and hyponatremia |
| 8 | ICD-10 | `I701` | Atherosclerosis of renal artery |
| 9 | ICD-10 | `F329` | Major depressive disorder, single episode, unspecified |
| 10 | ICD-10 | `T501X5A` | Adverse effect of loop [high-ceiling] diuretics, initial encounter |
| 11 | ICD-10 | `T465X5A` | Adverse effect of other antihypertensive drugs, initial encounter |
| 12 | ICD-10 | `Y929` | Unspecified place or not applicable |
| 13 | ICD-10 | `Z794` | Long term (current) use of insulin |
| 14 | ICD-10 | `N184` | Chronic kidney disease, stage 4 (severe) |
| 15 | ICD-10 | `G8929` | Other chronic pain |
| 16 | ICD-10 | `I2510` | Atherosclerotic heart disease of native coronary artery without angina pectoris |
| 17 | ICD-10 | `Z955` | Presence of coronary angioplasty implant and graft |
| 18 | ICD-10 | `Z7901` | Long term (current) use of anticoagulants |
| 19 | ICD-10 | `D649` | Anemia, unspecified |
| 20 | ICD-10 | `E785` | Hyperlipidemia, unspecified |
| 21 | ICD-10 | `E039` | Hypothyroidism, unspecified |
| 22 | ICD-10 | `I252` | Old myocardial infarction |
| 23 | ICD-10 | `E669` | Obesity, unspecified |
| 24 | ICD-10 | `Z87891` | Personal history of nicotine dependence |
| 25 | ICD-10 | `R791` | Abnormal coagulation profile |
| 26 | ICD-10 | `T45515A` | Adverse effect of anticoagulants, initial encounter |
| 27 | ICD-10 | `M109` | Gout, unspecified |
| 28 | ICD-10 | `Z6833` | Body mass index (BMI) 33.0-33.9, adult |
| 29 | ICD-10 | `F419` | Anxiety disorder, unspecified |

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
| 2147-08-02 18:14:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2147-08-02 18:14:00 | Transfer | → Emergency Department (ED) |
| 2147-08-03 02:41:00 | ED Departure | Left Emergency Dept. |
| 2147-08-03 02:58:00 | Admission | Admitted from EMERGENCY ROOM (OBSERVATION ADMIT) |
| 2147-08-04 20:48:04 | Transfer | → Transplant (transfer) |
| 2147-08-04 21:18:33 | Transfer | → Transplant (transfer) |
| 2147-08-05 15:54:21 | Transfer | → Transplant (transfer) |
| 2147-08-06 16:50:00 | Discharge | To HOME |

## 10. Missing / Ambiguous Data

- No procedure ICD codes — procedures may not have been coded or were minor.
- No ICU stay — patient managed on floor/step-down only.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
