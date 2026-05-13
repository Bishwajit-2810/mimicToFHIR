# Encounter Report — HADM 26013492

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 26013492 |
| Subject ID | 10014354 |
| Patient Sex | M |
| Patient Anchor Age (at anchor year) | 60 |
| Anchor Year | 2146 |
| Admission Time | 2147-11-14 22:12:00 |
| Discharge Time | 2147-11-16 15:00:00 |
| Admission Type | EW EMER. |
| Admission Location | EMERGENCY ROOM |
| Discharge Location | HOME HEALTH CARE |
| Insurance | Other |
| Language | ENGLISH |
| Marital Status | SINGLE |
| Race/Ethnicity | WHITE |
| ED Registration | 2147-11-14 18:22:00 |
| ED Departure | 2147-11-14 23:09:00 |
| In-Hospital Mortality | No |
| Date of Death (overall) | N/A |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| HCFA | 683 | RENAL FAILURE W CC | N/A | N/A |

### Primary Diagnosis (seq_num = 1)

- **ICD-10 N179**: Acute kidney failure, unspecified

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2147-11-14 22:14:43 | N/A | OMED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-10 `N179`: Acute kidney failure, unspecified
- (seq 2) ICD-10 `C9110`: Chronic lymphocytic leukemia of B-cell type not having achieved remission
- (seq 3) ICD-10 `E1121`: Type 2 diabetes mellitus with diabetic nephropathy
- (seq 4) ICD-10 `C6212`: Malignant neoplasm of descended left testis
- (seq 5) ICD-10 `E861`: Hypovolemia

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-10 | `N179` | Acute kidney failure, unspecified |
| 2 | ICD-10 | `C9110` | Chronic lymphocytic leukemia of B-cell type not having achieved remission |
| 3 | ICD-10 | `E1121` | Type 2 diabetes mellitus with diabetic nephropathy |
| 4 | ICD-10 | `C6212` | Malignant neoplasm of descended left testis |
| 5 | ICD-10 | `E861` | Hypovolemia |
| 6 | ICD-10 | `I110` | Hypertensive heart disease with heart failure |
| 7 | ICD-10 | `I5032` | Chronic diastolic (congestive) heart failure |
| 8 | ICD-10 | `I480` | Paroxysmal atrial fibrillation |
| 9 | ICD-10 | `I2510` | Atherosclerotic heart disease of native coronary artery without angina pectoris |
| 10 | ICD-10 | `Z955` | Presence of coronary angioplasty implant and graft |
| 11 | ICD-10 | `Z7902` | Long term (current) use of antithrombotics/antiplatelets |
| 12 | ICD-10 | `Z8673` | Personal history of transient ischemic attack (TIA), and cerebral infarction without residual deficits |
| 13 | ICD-10 | `E785` | Hyperlipidemia, unspecified |
| 14 | ICD-10 | `Z9884` | Bariatric surgery status |
| 15 | ICD-10 | `E039` | Hypothyroidism, unspecified |
| 16 | ICD-10 | `F329` | Major depressive disorder, single episode, unspecified |
| 17 | ICD-10 | `F419` | Anxiety disorder, unspecified |
| 18 | ICD-10 | `F449` | Dissociative and conversion disorder, unspecified |
| 19 | ICD-10 | `E1136` | Type 2 diabetes mellitus with diabetic cataract |
| 20 | ICD-10 | `G8929` | Other chronic pain |
| 21 | ICD-10 | `T451X5A` | Adverse effect of antineoplastic and immunosuppressive drugs, initial encounter |
| 22 | ICD-10 | `Y92009` | Unspecified place in unspecified non-institutional (private) residence as the place of occurrence of the external cause |
| 23 | ICD-10 | `T501X5A` | Adverse effect of loop [high-ceiling] diuretics, initial encounter |
| 24 | ICD-10 | `E6601` | Morbid (severe) obesity due to excess calories |
| 25 | ICD-10 | `Z6834` | Body mass index (BMI) 34.0-34.9, adult |
| 26 | ICD-10 | `Z794` | Long term (current) use of insulin |

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
| 2147-11-14 18:22:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2147-11-14 18:22:00 | Transfer | → Emergency Department (ED) |
| 2147-11-14 22:12:00 | Admission | Admitted from EMERGENCY ROOM (EW EMER.) |
| 2147-11-14 23:09:00 | ED Departure | Left Emergency Dept. |
| 2147-11-16 15:00:00 | Discharge | To HOME HEALTH CARE |

## 10. Missing / Ambiguous Data

- No procedure ICD codes — procedures may not have been coded or were minor.
- No ICU stay — patient managed on floor/step-down only.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
