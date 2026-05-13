# Encounter Report — HADM 21322534

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 21322534 |
| Subject ID | 10010471 |
| Patient Sex | F |
| Patient Anchor Age (at anchor year) | 89 |
| Anchor Year | 2155 |
| Admission Time | 2155-05-08 17:05:00 |
| Discharge Time | 2155-05-10 18:55:00 |
| Admission Type | OBSERVATION ADMIT |
| Admission Location | EMERGENCY ROOM |
| Discharge Location | HOME |
| Insurance | Medicare |
| Language | ENGLISH |
| Marital Status | WIDOWED |
| Race/Ethnicity | WHITE |
| ED Registration | 2155-05-08 13:48:00 |
| ED Departure | 2155-05-08 18:16:00 |
| In-Hospital Mortality | No |
| Date of Death (overall) | 2155-12-07 |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| APR | 201 | CARDIAC ARRHYTHMIA & CONDUCTION DISORDERS | 3.0 | 3.0 |
| HCFA | 308 | CARDIAC ARRHYTHMIA & CONDUCTION DISORDERS W MCC | N/A | N/A |

### Primary Diagnosis (seq_num = 1)

- **ICD-10 I4891**: Unspecified atrial fibrillation

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2155-05-08 17:06:17 | N/A | MED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-10 `I4891`: Unspecified atrial fibrillation
- (seq 2) ICD-10 `N186`: End stage renal disease
- (seq 3) ICD-10 `J189`: Pneumonia, unspecified organism
- (seq 4) ICD-10 `Z7682`: Awaiting organ transplant status
- (seq 5) ICD-10 `I248`: Other forms of acute ischemic heart disease

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-10 | `I4891` | Unspecified atrial fibrillation |
| 2 | ICD-10 | `N186` | End stage renal disease |
| 3 | ICD-10 | `J189` | Pneumonia, unspecified organism |
| 4 | ICD-10 | `Z7682` | Awaiting organ transplant status |
| 5 | ICD-10 | `I248` | Other forms of acute ischemic heart disease |
| 6 | ICD-10 | `J449` | Chronic obstructive pulmonary disease, unspecified |
| 7 | ICD-10 | `Z992` | Dependence on renal dialysis |
| 8 | ICD-10 | `I2510` | Atherosclerotic heart disease of native coronary artery without angina pectoris |
| 9 | ICD-10 | `I350` | Nonrheumatic aortic (valve) stenosis |
| 10 | ICD-10 | `I340` | Nonrheumatic mitral (valve) insufficiency |
| 11 | ICD-10 | `D631` | Anemia in chronic kidney disease |
| 12 | ICD-10 | `E039` | Hypothyroidism, unspecified |
| 13 | ICD-10 | `M5489` | Other dorsalgia |
| 14 | ICD-10 | `M25512` | Pain in left shoulder |
| 15 | ICD-10 | `Z79891` | Long term (current) use of opiate analgesic |
| 16 | ICD-10 | `G8929` | Other chronic pain |

## 5. ICU Stays

_No ICU stay recorded for this admission._

## 6. Escalation / Severity Indicators

The following critical conditions or interventions were detected:

- **Pneumonia** (ICD diagnosis)

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2155-05-09 | ICD-10 | `5A1D60Z` | Performance of Urinary Filtration, Multiple |


## 8. Critical Findings (Charted Events)

_No critical chart events detected._

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2155-05-08 13:48:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2155-05-08 13:48:00 | Transfer | → Emergency Department (ED) |
| 2155-05-08 17:05:00 | Admission | Admitted from EMERGENCY ROOM (OBSERVATION ADMIT) |
| 2155-05-08 18:16:00 | ED Departure | Left Emergency Dept. |
| 2155-05-09 23:34:11 | Transfer | → Medicine (transfer) |
| 2155-05-10 18:55:00 | Discharge | To HOME |

## 10. Missing / Ambiguous Data

- No ICU stay — patient managed on floor/step-down only.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
