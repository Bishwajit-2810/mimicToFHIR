# Encounter Report — HADM 27125816

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 27125816 |
| Subject ID | 10040025 |
| Patient Sex | F |
| Patient Anchor Age (at anchor year) | 64 |
| Anchor Year | 2143 |
| Admission Time | 2143-03-18 12:34:00 |
| Discharge Time | 2143-03-19 12:00:00 |
| Admission Type | AMBULATORY OBSERVATION |
| Admission Location | PROCEDURE SITE |
| Discharge Location | N/A |
| Insurance | Other |
| Language | ENGLISH |
| Marital Status | DIVORCED |
| Race/Ethnicity | WHITE |
| ED Registration | N/A |
| ED Departure | N/A |
| In-Hospital Mortality | No |
| Date of Death (overall) | 2148-02-07 |

## 2. Hospital Visit Reason

### Primary Diagnosis (seq_num = 1)

- **ICD-9 40390**: Hypertensive chronic kidney disease, unspecified, with chronic kidney disease stage I through stage IV, or unspecified

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2143-03-18 12:34:29 | N/A | CMED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-9 `40390`: Hypertensive chronic kidney disease, unspecified, with chronic kidney disease stage I through stage IV, or unspecified
- (seq 2) ICD-9 `4473`: Hyperplasia of renal artery
- (seq 3) ICD-9 `42830`: Diastolic heart failure, unspecified
- (seq 4) ICD-9 `4280`: Congestive heart failure, unspecified
- (seq 5) ICD-9 `25000`: Diabetes mellitus without mention of complication, type II or unspecified type, not stated as uncontrolled

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-9 | `40390` | Hypertensive chronic kidney disease, unspecified, with chronic kidney disease stage I through stage IV, or unspecified |
| 2 | ICD-9 | `4473` | Hyperplasia of renal artery |
| 3 | ICD-9 | `42830` | Diastolic heart failure, unspecified |
| 4 | ICD-9 | `4280` | Congestive heart failure, unspecified |
| 5 | ICD-9 | `25000` | Diabetes mellitus without mention of complication, type II or unspecified type, not stated as uncontrolled |
| 6 | ICD-9 | `2449` | Unspecified acquired hypothyroidism |
| 7 | ICD-9 | `412` | Old myocardial infarction |
| 8 | ICD-9 | `V4582` | Percutaneous transluminal coronary angioplasty status |
| 9 | ICD-9 | `5859` | Chronic kidney disease, unspecified |

## 5. ICU Stays

_No ICU stay recorded for this admission._

## 6. Escalation / Severity Indicators

_No escalation indicators detected from ICD codes or ICU procedure events._

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2143-03-18 | ICD-9 | `8845` | Arteriography of renal arteries |
| 2 | 2143-03-18 | ICD-9 | `0069` | Intravascular pressure measurement, other specified and unspecified vessels |


## 8. Critical Findings (Charted Events)

_No critical chart events detected._

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2143-03-18 12:34:00 | Admission | Admitted from PROCEDURE SITE (AMBULATORY OBSERVATION) |
| 2143-03-19 12:00:00 | Discharge | To N/A |

## 10. Missing / Ambiguous Data

- No ED registration time — admission may not have gone through ED.
- Discharge location not recorded.
- No ICU stay — patient managed on floor/step-down only.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
