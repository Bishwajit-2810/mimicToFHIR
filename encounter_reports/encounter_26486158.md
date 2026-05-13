# Encounter Report — HADM 26486158

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 26486158 |
| Subject ID | 10014354 |
| Patient Sex | M |
| Patient Anchor Age (at anchor year) | 60 |
| Anchor Year | 2146 |
| Admission Time | 2148-08-22 15:18:00 |
| Discharge Time | 2148-09-08 12:00:00 |
| Admission Type | OBSERVATION ADMIT |
| Admission Location | CLINIC REFERRAL |
| Discharge Location | HOME HEALTH CARE |
| Insurance | Other |
| Language | ENGLISH |
| Marital Status | SINGLE |
| Race/Ethnicity | WHITE |
| ED Registration | N/A |
| ED Departure | N/A |
| In-Hospital Mortality | No |
| Date of Death (overall) | N/A |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| HCFA | 846 | CHEMOTHERAPY W/O ACUTE LEUKEMIA AS SECONDARY DIAGNOSIS W MCC | N/A | N/A |
| APR | 696 | OTHER CHEMOTHERAPY | 3.0 | 3.0 |

### Primary Diagnosis (seq_num = 1)

- **ICD-10 Z5111**: Encounter for antineoplastic chemotherapy

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2148-08-22 15:20:17 | N/A | OMED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-10 `Z5111`: Encounter for antineoplastic chemotherapy
- (seq 2) ICD-10 `I5023`: Acute on chronic systolic (congestive) heart failure
- (seq 3) ICD-10 `N179`: Acute kidney failure, unspecified
- (seq 4) ICD-10 `C9110`: Chronic lymphocytic leukemia of B-cell type not having achieved remission
- (seq 5) ICD-10 `E222`: Syndrome of inappropriate secretion of antidiuretic hormone

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-10 | `Z5111` | Encounter for antineoplastic chemotherapy |
| 2 | ICD-10 | `I5023` | Acute on chronic systolic (congestive) heart failure |
| 3 | ICD-10 | `N179` | Acute kidney failure, unspecified |
| 4 | ICD-10 | `C9110` | Chronic lymphocytic leukemia of B-cell type not having achieved remission |
| 5 | ICD-10 | `E222` | Syndrome of inappropriate secretion of antidiuretic hormone |
| 6 | ICD-10 | `D630` | Anemia in neoplastic disease |
| 7 | ICD-10 | `C6290` | Malignant neoplasm of unspecified testis, unspecified whether descended or undescended |
| 8 | ICD-10 | `F05` | Delirium due to known physiological condition |
| 9 | ICD-10 | `E1142` | Type 2 diabetes mellitus with diabetic polyneuropathy |
| 10 | ICD-10 | `I4891` | Unspecified atrial fibrillation |
| 11 | ICD-10 | `I110` | Hypertensive heart disease with heart failure |
| 12 | ICD-10 | `F259` | Schizoaffective disorder, unspecified |
| 13 | ICD-10 | `I2510` | Atherosclerotic heart disease of native coronary artery without angina pectoris |
| 14 | ICD-10 | `E039` | Hypothyroidism, unspecified |
| 15 | ICD-10 | `E785` | Hyperlipidemia, unspecified |
| 16 | ICD-10 | `Z955` | Presence of coronary angioplasty implant and graft |
| 17 | ICD-10 | `G4733` | Obstructive sleep apnea (adult) (pediatric) |
| 18 | ICD-10 | `Z7901` | Long term (current) use of anticoagulants |
| 19 | ICD-10 | `Z794` | Long term (current) use of insulin |
| 20 | ICD-10 | `Z45018` | Encounter for adjustment and management of other part of cardiac pacemaker |
| 21 | ICD-10 | `R509` | Fever, unspecified |
| 22 | ICD-10 | `G8929` | Other chronic pain |
| 23 | ICD-10 | `I493` | Ventricular premature depolarization |
| 24 | ICD-10 | `E875` | Hyperkalemia |
| 25 | ICD-10 | `M7989` | Other specified soft tissue disorders |

## 5. ICU Stays

_No ICU stay recorded for this admission._

## 6. Escalation / Severity Indicators

The following critical conditions or interventions were detected:

- **Acute Kidney Injury** (ICD diagnosis)

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2148-09-01 | ICD-10 | `3E04305` | Introduction of Other Antineoplastic into Central Vein, Percutaneous Approach |


## 8. Critical Findings (Charted Events)

_No critical chart events detected._

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2148-08-22 15:18:00 | Admission | Admitted from CLINIC REFERRAL (OBSERVATION ADMIT) |
| 2148-08-28 20:44:35 | Transfer | → Hematology/Oncology Intermediate (transfer) |
| 2148-08-29 20:28:05 | Transfer | → Hematology/Oncology Intermediate (transfer) |
| 2148-09-08 12:00:00 | Discharge | To HOME HEALTH CARE |

## 10. Missing / Ambiguous Data

- No ED registration time — admission may not have gone through ED.
- No ICU stay — patient managed on floor/step-down only.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
