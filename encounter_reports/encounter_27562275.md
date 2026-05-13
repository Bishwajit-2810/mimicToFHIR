# Encounter Report — HADM 27562275

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 27562275 |
| Subject ID | 10014354 |
| Patient Sex | M |
| Patient Anchor Age (at anchor year) | 60 |
| Anchor Year | 2146 |
| Admission Time | 2148-07-18 02:31:00 |
| Discharge Time | 2148-07-20 17:47:00 |
| Admission Type | DIRECT EMER. |
| Admission Location | PHYSICIAN REFERRAL |
| Discharge Location | HOME HEALTH CARE |
| Insurance | Other |
| Language | ENGLISH |
| Marital Status | SINGLE |
| Race/Ethnicity | WHITE |
| ED Registration | 2148-07-17 20:36:00 |
| ED Departure | 2148-07-18 04:46:00 |
| In-Hospital Mortality | No |
| Date of Death (overall) | N/A |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| APR | 207 | OTHER CIRCULATORY SYSTEM DIAGNOSES | 2.0 | 2.0 |
| HCFA | 315 | OTHER CIRCULATORY SYSTEM DIAGNOSES W CC | N/A | N/A |

### Primary Diagnosis (seq_num = 1)

- **ICD-10 I319**: Disease of pericardium, unspecified

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2148-07-18 02:32:39 | N/A | CMED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-10 `I319`: Disease of pericardium, unspecified
- (seq 2) ICD-10 `E871`: Hypo-osmolality and hyponatremia
- (seq 3) ICD-10 `C9110`: Chronic lymphocytic leukemia of B-cell type not having achieved remission
- (seq 4) ICD-10 `I110`: Hypertensive heart disease with heart failure
- (seq 5) ICD-10 `I5032`: Chronic diastolic (congestive) heart failure

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-10 | `I319` | Disease of pericardium, unspecified |
| 2 | ICD-10 | `E871` | Hypo-osmolality and hyponatremia |
| 3 | ICD-10 | `C9110` | Chronic lymphocytic leukemia of B-cell type not having achieved remission |
| 4 | ICD-10 | `I110` | Hypertensive heart disease with heart failure |
| 5 | ICD-10 | `I5032` | Chronic diastolic (congestive) heart failure |
| 6 | ICD-10 | `I2510` | Atherosclerotic heart disease of native coronary artery without angina pectoris |
| 7 | ICD-10 | `Z955` | Presence of coronary angioplasty implant and graft |
| 8 | ICD-10 | `Z7901` | Long term (current) use of anticoagulants |
| 9 | ICD-10 | `E785` | Hyperlipidemia, unspecified |
| 10 | ICD-10 | `E039` | Hypothyroidism, unspecified |
| 11 | ICD-10 | `E119` | Type 2 diabetes mellitus without complications |
| 12 | ICD-10 | `Z794` | Long term (current) use of insulin |
| 13 | ICD-10 | `G4733` | Obstructive sleep apnea (adult) (pediatric) |
| 14 | ICD-10 | `F259` | Schizoaffective disorder, unspecified |
| 15 | ICD-10 | `E875` | Hyperkalemia |
| 16 | ICD-10 | `E1165` | Type 2 diabetes mellitus with hyperglycemia |
| 17 | ICD-10 | `I480` | Paroxysmal atrial fibrillation |
| 18 | ICD-10 | `E669` | Obesity, unspecified |
| 19 | ICD-10 | `Z6837` | Body mass index (BMI) 37.0-37.9, adult |

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
| 2148-07-17 20:36:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2148-07-17 20:36:00 | Transfer | → Emergency Department (ED) |
| 2148-07-18 02:31:00 | Admission | Admitted from PHYSICIAN REFERRAL (DIRECT EMER.) |
| 2148-07-18 04:46:00 | ED Departure | Left Emergency Dept. |
| 2148-07-19 19:11:24 | Transfer | → Medicine/Cardiology (transfer) |
| 2148-07-20 17:47:00 | Discharge | To HOME HEALTH CARE |

## 10. Missing / Ambiguous Data

- No procedure ICD codes — procedures may not have been coded or were minor.
- No ICU stay — patient managed on floor/step-down only.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
