# Encounter Report — HADM 29780751

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 29780751 |
| Subject ID | 10014354 |
| Patient Sex | M |
| Patient Anchor Age (at anchor year) | 60 |
| Anchor Year | 2146 |
| Admission Time | 2147-11-26 00:39:00 |
| Discharge Time | 2147-11-30 16:54:00 |
| Admission Type | OBSERVATION ADMIT |
| Admission Location | EMERGENCY ROOM |
| Discharge Location | HOME HEALTH CARE |
| Insurance | Other |
| Language | ENGLISH |
| Marital Status | SINGLE |
| Race/Ethnicity | WHITE |
| ED Registration | 2147-11-25 19:39:00 |
| ED Departure | 2147-11-26 01:30:00 |
| In-Hospital Mortality | No |
| Date of Death (overall) | N/A |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| HCFA | 866 | VIRAL ILLNESS W/O MCC | N/A | N/A |
| APR | 723 | VIRAL ILLNESS | 3.0 | 2.0 |

### Primary Diagnosis (seq_num = 1)

- **ICD-10 B348**: Other viral infections of unspecified site

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2147-11-26 00:40:17 | N/A | OMED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-10 `B348`: Other viral infections of unspecified site
- (seq 2) ICD-10 `C9110`: Chronic lymphocytic leukemia of B-cell type not having achieved remission
- (seq 3) ICD-10 `E1136`: Type 2 diabetes mellitus with diabetic cataract
- (seq 4) ICD-10 `D6481`: Anemia due to antineoplastic chemotherapy
- (seq 5) ICD-10 `E871`: Hypo-osmolality and hyponatremia

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-10 | `B348` | Other viral infections of unspecified site |
| 2 | ICD-10 | `C9110` | Chronic lymphocytic leukemia of B-cell type not having achieved remission |
| 3 | ICD-10 | `E1136` | Type 2 diabetes mellitus with diabetic cataract |
| 4 | ICD-10 | `D6481` | Anemia due to antineoplastic chemotherapy |
| 5 | ICD-10 | `E871` | Hypo-osmolality and hyponatremia |
| 6 | ICD-10 | `C6292` | Malignant neoplasm of left testis, unspecified whether descended or undescended |
| 7 | ICD-10 | `E785` | Hyperlipidemia, unspecified |
| 8 | ICD-10 | `I2510` | Atherosclerotic heart disease of native coronary artery without angina pectoris |
| 9 | ICD-10 | `Z955` | Presence of coronary angioplasty implant and graft |
| 10 | ICD-10 | `Z8673` | Personal history of transient ischemic attack (TIA), and cerebral infarction without residual deficits |
| 11 | ICD-10 | `I10` | Essential (primary) hypertension |
| 12 | ICD-10 | `Z9884` | Bariatric surgery status |
| 13 | ICD-10 | `E039` | Hypothyroidism, unspecified |
| 14 | ICD-10 | `G8929` | Other chronic pain |
| 15 | ICD-10 | `F329` | Major depressive disorder, single episode, unspecified |
| 16 | ICD-10 | `F419` | Anxiety disorder, unspecified |
| 17 | ICD-10 | `H409` | Unspecified glaucoma |
| 18 | ICD-10 | `Z794` | Long term (current) use of insulin |
| 19 | ICD-10 | `Z950` | Presence of cardiac pacemaker |
| 20 | ICD-10 | `R002` | Palpitations |
| 21 | ICD-10 | `M7989` | Other specified soft tissue disorders |
| 22 | ICD-10 | `E669` | Obesity, unspecified |
| 23 | ICD-10 | `Z6834` | Body mass index (BMI) 34.0-34.9, adult |

## 5. ICU Stays

_No ICU stay recorded for this admission._

## 6. Escalation / Severity Indicators

_No escalation indicators detected from ICD codes or ICU procedure events._

## 7. Procedures and Interventions

_No ICD-coded procedures recorded._


## 8. Critical Findings (Charted Events)

_No critical chart events detected._

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2147-11-25 19:39:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2147-11-25 19:39:00 | Transfer | → Emergency Department (ED) |
| 2147-11-26 00:39:00 | Admission | Admitted from EMERGENCY ROOM (OBSERVATION ADMIT) |
| 2147-11-26 01:30:00 | ED Departure | Left Emergency Dept. |
| 2147-11-30 16:54:00 | Discharge | To HOME HEALTH CARE |

## 10. Missing / Ambiguous Data

- No procedure ICD codes — procedures may not have been coded or were minor.
- No ICU stay — patient managed on floor/step-down only.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
