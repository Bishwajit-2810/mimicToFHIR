# Encounter Report — HADM 24357615

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 24357615 |
| Subject ID | 10014354 |
| Patient Sex | M |
| Patient Anchor Age (at anchor year) | 60 |
| Anchor Year | 2146 |
| Admission Time | 2150-05-09 16:09:00 |
| Discharge Time | 2150-05-10 15:59:00 |
| Admission Type | EW EMER. |
| Admission Location | PHYSICIAN REFERRAL |
| Discharge Location | HOME HEALTH CARE |
| Insurance | Other |
| Language | ENGLISH |
| Marital Status | SINGLE |
| Race/Ethnicity | WHITE |
| ED Registration | 2150-05-08 22:30:00 |
| ED Departure | 2150-05-09 19:09:00 |
| In-Hospital Mortality | No |
| Date of Death (overall) | N/A |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| HCFA | 392 | ESOPHAGITIS, GASTROENT & MISC DIGEST DISORDERS W/O MCC | N/A | N/A |
| APR | 251 | ABDOMINAL PAIN | 3.0 | 2.0 |

### Primary Diagnosis (seq_num = 1)

- **ICD-10 R1030**: Lower abdominal pain, unspecified

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2150-05-09 16:10:21 | N/A | OMED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-10 `R1030`: Lower abdominal pain, unspecified
- (seq 2) ICD-10 `C9110`: Chronic lymphocytic leukemia of B-cell type not having achieved remission
- (seq 3) ICD-10 `I69354`: Hemiplegia and hemiparesis following cerebral infarction affecting left non-dominant side
- (seq 4) ICD-10 `F323`: Major depressive disorder, single episode, severe with psychotic features
- (seq 5) ICD-10 `R339`: Retention of urine, unspecified

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-10 | `R1030` | Lower abdominal pain, unspecified |
| 2 | ICD-10 | `C9110` | Chronic lymphocytic leukemia of B-cell type not having achieved remission |
| 3 | ICD-10 | `I69354` | Hemiplegia and hemiparesis following cerebral infarction affecting left non-dominant side |
| 4 | ICD-10 | `F323` | Major depressive disorder, single episode, severe with psychotic features |
| 5 | ICD-10 | `R339` | Retention of urine, unspecified |
| 6 | ICD-10 | `I495` | Sick sinus syndrome |
| 7 | ICD-10 | `D696` | Thrombocytopenia, unspecified |
| 8 | ICD-10 | `E039` | Hypothyroidism, unspecified |
| 9 | ICD-10 | `I480` | Paroxysmal atrial fibrillation |
| 10 | ICD-10 | `Z7901` | Long term (current) use of anticoagulants |
| 11 | ICD-10 | `Z950` | Presence of cardiac pacemaker |
| 12 | ICD-10 | `M109` | Gout, unspecified |
| 13 | ICD-10 | `D638` | Anemia in other chronic diseases classified elsewhere |
| 14 | ICD-10 | `E1142` | Type 2 diabetes mellitus with diabetic polyneuropathy |
| 15 | ICD-10 | `Z794` | Long term (current) use of insulin |
| 16 | ICD-10 | `I2510` | Atherosclerotic heart disease of native coronary artery without angina pectoris |
| 17 | ICD-10 | `E785` | Hyperlipidemia, unspecified |
| 18 | ICD-10 | `G4733` | Obstructive sleep apnea (adult) (pediatric) |
| 19 | ICD-10 | `M1990` | Unspecified osteoarthritis, unspecified site |
| 20 | ICD-10 | `R600` | Localized edema |
| 21 | ICD-10 | `E669` | Obesity, unspecified |
| 22 | ICD-10 | `G8929` | Other chronic pain |
| 23 | ICD-10 | `M549` | Dorsalgia, unspecified |
| 24 | ICD-10 | `R509` | Fever, unspecified |
| 25 | ICD-10 | `Z6837` | Body mass index (BMI) 37.0-37.9, adult |
| 26 | ICD-10 | `Z955` | Presence of coronary angioplasty implant and graft |
| 27 | ICD-10 | `Z8547` | Personal history of malignant neoplasm of testis |
| 28 | ICD-10 | `Z9884` | Bariatric surgery status |

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
| 2150-05-08 22:30:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2150-05-08 22:30:00 | Transfer | → Emergency Department (ED) |
| 2150-05-09 16:09:00 | Admission | Admitted from PHYSICIAN REFERRAL (EW EMER.) |
| 2150-05-09 19:09:00 | ED Departure | Left Emergency Dept. |
| 2150-05-10 15:59:00 | Discharge | To HOME HEALTH CARE |

## 10. Missing / Ambiguous Data

- No procedure ICD codes — procedures may not have been coded or were minor.
- No ICU stay — patient managed on floor/step-down only.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
