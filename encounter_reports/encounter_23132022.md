# Encounter Report — HADM 23132022

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 23132022 |
| Subject ID | 10014354 |
| Patient Sex | M |
| Patient Anchor Age (at anchor year) | 60 |
| Anchor Year | 2146 |
| Admission Time | 2148-06-24 15:22:00 |
| Discharge Time | 2148-06-28 13:54:00 |
| Admission Type | OBSERVATION ADMIT |
| Admission Location | PHYSICIAN REFERRAL |
| Discharge Location | HOME |
| Insurance | Other |
| Language | ENGLISH |
| Marital Status | SINGLE |
| Race/Ethnicity | WHITE |
| ED Registration | 2148-06-24 09:22:00 |
| ED Departure | 2148-06-24 16:12:00 |
| In-Hospital Mortality | No |
| Date of Death (overall) | N/A |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| APR | 207 | OTHER CIRCULATORY SYSTEM DIAGNOSES | 3.0 | 2.0 |
| HCFA | 315 | OTHER CIRCULATORY SYSTEM DIAGNOSES W CC | N/A | N/A |

### Primary Diagnosis (seq_num = 1)

- **ICD-10 I309**: Acute pericarditis, unspecified

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2148-06-24 15:22:45 | N/A | CMED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-10 `I309`: Acute pericarditis, unspecified
- (seq 2) ICD-10 `C9110`: Chronic lymphocytic leukemia of B-cell type not having achieved remission
- (seq 3) ICD-10 `N179`: Acute kidney failure, unspecified
- (seq 4) ICD-10 `E1142`: Type 2 diabetes mellitus with diabetic polyneuropathy
- (seq 5) ICD-10 `I480`: Paroxysmal atrial fibrillation

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-10 | `I309` | Acute pericarditis, unspecified |
| 2 | ICD-10 | `C9110` | Chronic lymphocytic leukemia of B-cell type not having achieved remission |
| 3 | ICD-10 | `N179` | Acute kidney failure, unspecified |
| 4 | ICD-10 | `E1142` | Type 2 diabetes mellitus with diabetic polyneuropathy |
| 5 | ICD-10 | `I480` | Paroxysmal atrial fibrillation |
| 6 | ICD-10 | `E860` | Dehydration |
| 7 | ICD-10 | `E871` | Hypo-osmolality and hyponatremia |
| 8 | ICD-10 | `G4733` | Obstructive sleep apnea (adult) (pediatric) |
| 9 | ICD-10 | `E039` | Hypothyroidism, unspecified |
| 10 | ICD-10 | `G8929` | Other chronic pain |
| 11 | ICD-10 | `I2510` | Atherosclerotic heart disease of native coronary artery without angina pectoris |
| 12 | ICD-10 | `Z955` | Presence of coronary angioplasty implant and graft |
| 13 | ICD-10 | `Z7984` | Long term (current) use of oral hypoglycemic drugs |
| 14 | ICD-10 | `I10` | Essential (primary) hypertension |
| 15 | ICD-10 | `Z7901` | Long term (current) use of anticoagulants |
| 16 | ICD-10 | `E785` | Hyperlipidemia, unspecified |
| 17 | ICD-10 | `G4700` | Insomnia, unspecified |
| 18 | ICD-10 | `Z6836` | Body mass index (BMI) 36.0-36.9, adult |
| 19 | ICD-10 | `Z9884` | Bariatric surgery status |
| 20 | ICD-10 | `F419` | Anxiety disorder, unspecified |
| 21 | ICD-10 | `F329` | Major depressive disorder, single episode, unspecified |
| 22 | ICD-10 | `E669` | Obesity, unspecified |

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
| 2148-06-24 09:22:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2148-06-24 09:22:00 | Transfer | → Emergency Department (ED) |
| 2148-06-24 15:22:00 | Admission | Admitted from PHYSICIAN REFERRAL (OBSERVATION ADMIT) |
| 2148-06-24 16:12:00 | ED Departure | Left Emergency Dept. |
| 2148-06-28 13:54:00 | Discharge | To HOME |

## 10. Missing / Ambiguous Data

- No procedure ICD codes — procedures may not have been coded or were minor.
- No ICU stay — patient managed on floor/step-down only.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
