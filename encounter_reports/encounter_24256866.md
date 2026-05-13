# Encounter Report — HADM 24256866

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 24256866 |
| Subject ID | 10037861 |
| Patient Sex | M |
| Patient Anchor Age (at anchor year) | 77 |
| Anchor Year | 2115 |
| Admission Time | 2115-10-09 20:28:00 |
| Discharge Time | 2115-10-18 16:50:00 |
| Admission Type | URGENT |
| Admission Location | TRANSFER FROM HOSPITAL |
| Discharge Location | HOME HEALTH CARE |
| Insurance | Medicare |
| Language | ENGLISH |
| Marital Status | MARRIED |
| Race/Ethnicity | UNKNOWN |
| ED Registration | N/A |
| ED Departure | N/A |
| In-Hospital Mortality | No |
| Date of Death (overall) | 2117-03-24 |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| APR | 191 | CARDIAC CATHETERIZATION FOR CORONARY ARTERY DISEASE | 3.0 | 3.0 |
| HCFA | 287 | CIRCULATORY DISORDERS EXCEPT AMI, W CARD CATH W/O MCC | N/A | N/A |

### Primary Diagnosis (seq_num = 1)

- **ICD-9 42823**: Acute on chronic systolic heart failure

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2115-10-09 20:29:28 | N/A | CMED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-9 `42823`: Acute on chronic systolic heart failure
- (seq 2) ICD-9 `5849`: Acute kidney failure, unspecified
- (seq 3) ICD-9 `2760`: Hyperosmolality and/or hypernatremia
- (seq 4) ICD-9 `4589`: Hypotension, unspecified
- (seq 5) ICD-9 `2763`: Alkalosis

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-9 | `42823` | Acute on chronic systolic heart failure |
| 2 | ICD-9 | `5849` | Acute kidney failure, unspecified |
| 3 | ICD-9 | `2760` | Hyperosmolality and/or hypernatremia |
| 4 | ICD-9 | `4589` | Hypotension, unspecified |
| 5 | ICD-9 | `2763` | Alkalosis |
| 6 | ICD-9 | `4168` | Other chronic pulmonary heart diseases |
| 7 | ICD-9 | `2875` | Thrombocytopenia, unspecified |
| 8 | ICD-9 | `5990` | Urinary tract infection, site not specified |
| 9 | ICD-9 | `5693` | Hemorrhage of rectum and anus |
| 10 | ICD-9 | `4280` | Congestive heart failure, unspecified |
| 11 | ICD-9 | `412` | Old myocardial infarction |
| 12 | ICD-9 | `4148` | Other specified forms of chronic ischemic heart disease |
| 13 | ICD-9 | `41400` | Coronary atherosclerosis of unspecified type of vessel, native or graft |
| 14 | ICD-9 | `42731` | Atrial fibrillation |
| 15 | ICD-9 | `40390` | Hypertensive chronic kidney disease, unspecified, with chronic kidney disease stage I through stage IV, or unspecified |
| 16 | ICD-9 | `5853` | Chronic kidney disease, Stage III (moderate) |
| 17 | ICD-9 | `2724` | Other and unspecified hyperlipidemia |
| 18 | ICD-9 | `25000` | Diabetes mellitus without mention of complication, type II or unspecified type, not stated as uncontrolled |
| 19 | ICD-9 | `59970` | Hematuria, unspecified |
| 20 | ICD-9 | `E9444` | Other diuretics causing adverse effects in therapeutic use |
| 21 | ICD-9 | `5920` | Calculus of kidney |
| 22 | ICD-9 | `0417` | Pseudomonas infection in conditions classified elsewhere and of unspecified site |
| 23 | ICD-9 | `V1582` | Personal history of tobacco use |
| 24 | ICD-9 | `V4582` | Percutaneous transluminal coronary angioplasty status |
| 25 | ICD-9 | `V5861` | Long-term (current) use of anticoagulants |

## 5. ICU Stays

_No ICU stay recorded for this admission._

## 6. Escalation / Severity Indicators

The following critical conditions or interventions were detected:

- **Acute Kidney Injury** (ICD diagnosis)

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2115-10-14 | ICD-9 | `3721` | Right heart cardiac catheterization |


## 8. Critical Findings (Charted Events)

_No critical chart events detected._

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2115-10-09 20:28:00 | Admission | Admitted from TRANSFER FROM HOSPITAL (URGENT) |
| 2115-10-14 00:24:03 | Transfer | → Medicine/Cardiology (transfer) |
| 2115-10-15 17:28:00 | Transfer | → Medicine/Cardiology (transfer) |
| 2115-10-18 16:50:00 | Discharge | To HOME HEALTH CARE |

## 10. Missing / Ambiguous Data

- No ED registration time — admission may not have gone through ED.
- No ICU stay — patient managed on floor/step-down only.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
