# Encounter Report — HADM 27553957

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 27553957 |
| Subject ID | 10040025 |
| Patient Sex | F |
| Patient Anchor Age (at anchor year) | 64 |
| Anchor Year | 2143 |
| Admission Time | 2145-07-24 19:00:00 |
| Discharge Time | 2145-07-31 14:12:00 |
| Admission Type | EW EMER. |
| Admission Location | EMERGENCY ROOM |
| Discharge Location | HOME |
| Insurance | Other |
| Language | ENGLISH |
| Marital Status | DIVORCED |
| Race/Ethnicity | WHITE |
| ED Registration | 2145-07-24 11:30:00 |
| ED Departure | 2145-07-24 20:32:00 |
| In-Hospital Mortality | No |
| Date of Death (overall) | 2148-02-07 |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| APR | 201 | CARDIAC ARRHYTHMIA & CONDUCTION DISORDERS | 3.0 | 3.0 |
| HCFA | 308 | CARDIAC ARRHYTHMIA & CONDUCTION DISORDERS W MCC | N/A | N/A |

### Primary Diagnosis (seq_num = 1)

- **ICD-9 42731**: Atrial fibrillation

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2145-07-24 19:00:51 | N/A | CMED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-9 `42731`: Atrial fibrillation
- (seq 2) ICD-9 `5849`: Acute kidney failure, unspecified
- (seq 3) ICD-9 `36230`: Retinal vascular occlusion, unspecified
- (seq 4) ICD-9 `25040`: Diabetes with renal manifestations, type II or unspecified type, not stated as uncontrolled
- (seq 5) ICD-9 `4280`: Congestive heart failure, unspecified

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-9 | `42731` | Atrial fibrillation |
| 2 | ICD-9 | `5849` | Acute kidney failure, unspecified |
| 3 | ICD-9 | `36230` | Retinal vascular occlusion, unspecified |
| 4 | ICD-9 | `25040` | Diabetes with renal manifestations, type II or unspecified type, not stated as uncontrolled |
| 5 | ICD-9 | `4280` | Congestive heart failure, unspecified |
| 6 | ICD-9 | `412` | Old myocardial infarction |
| 7 | ICD-9 | `41401` | Coronary atherosclerosis of native coronary artery |
| 8 | ICD-9 | `40390` | Hypertensive chronic kidney disease, unspecified, with chronic kidney disease stage I through stage IV, or unspecified |
| 9 | ICD-9 | `5853` | Chronic kidney disease, Stage III (moderate) |
| 10 | ICD-9 | `2724` | Other and unspecified hyperlipidemia |
| 11 | ICD-9 | `2749` | Gout, unspecified |
| 12 | ICD-9 | `27800` | Obesity, unspecified |
| 13 | ICD-9 | `2859` | Anemia, unspecified |
| 14 | ICD-9 | `311` | Depressive disorder, not elsewhere classified |
| 15 | ICD-9 | `71940` | Pain in joint, site unspecified |
| 16 | ICD-9 | `33829` | Other chronic pain |
| 17 | ICD-9 | `V5861` | Long-term (current) use of anticoagulants |
| 18 | ICD-9 | `V5867` | Long-term (current) use of insulin |
| 19 | ICD-9 | `V4582` | Percutaneous transluminal coronary angioplasty status |
| 20 | ICD-9 | `V1582` | Personal history of tobacco use |
| 21 | ICD-9 | `V8537` | Body Mass Index 37.0-37.9, adult |
| 22 | ICD-9 | `E9320` | Adrenal cortical steroids causing adverse effects in therapeutic use |
| 23 | ICD-9 | `E9444` | Other diuretics causing adverse effects in therapeutic use |
| 24 | ICD-9 | `V0179` | Contact with or exposure to other viral diseases |

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
| 2145-07-24 11:30:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2145-07-24 11:30:00 | Transfer | → Emergency Department (ED) |
| 2145-07-24 19:00:00 | Admission | Admitted from EMERGENCY ROOM (EW EMER.) |
| 2145-07-24 20:32:00 | ED Departure | Left Emergency Dept. |
| 2145-07-26 20:40:37 | Transfer | → Medicine/Cardiology (transfer) |
| 2145-07-31 14:12:00 | Discharge | To HOME |

## 10. Missing / Ambiguous Data

- No procedure ICD codes — procedures may not have been coded or were minor.
- No ICU stay — patient managed on floor/step-down only.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
