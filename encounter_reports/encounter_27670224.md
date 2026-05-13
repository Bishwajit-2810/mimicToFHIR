# Encounter Report — HADM 27670224

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 27670224 |
| Subject ID | 10015860 |
| Patient Sex | M |
| Patient Anchor Age (at anchor year) | 53 |
| Anchor Year | 2186 |
| Admission Time | 2187-12-14 15:48:00 |
| Discharge Time | 2187-12-16 14:38:00 |
| Admission Type | EU OBSERVATION |
| Admission Location | EMERGENCY ROOM |
| Discharge Location | N/A |
| Insurance | Other |
| Language | ENGLISH |
| Marital Status | SINGLE |
| Race/Ethnicity | WHITE |
| ED Registration | 2187-12-14 12:49:00 |
| ED Departure | 2187-12-14 17:48:00 |
| In-Hospital Mortality | No |
| Date of Death (overall) | N/A |

## 2. Hospital Visit Reason

### Primary Diagnosis (seq_num = 1)

- **ICD-9 6827**: Cellulitis and abscess of foot, except toes

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2187-12-14 15:48:46 | N/A | MED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-9 `6827`: Cellulitis and abscess of foot, except toes
- (seq 2) ICD-9 `70715`: Ulcer of other part of foot
- (seq 3) ICD-9 `2761`: Hyposmolality and/or hyponatremia
- (seq 4) ICD-9 `40390`: Hypertensive chronic kidney disease, unspecified, with chronic kidney disease stage I through stage IV, or unspecified
- (seq 5) ICD-9 `5859`: Chronic kidney disease, unspecified

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-9 | `6827` | Cellulitis and abscess of foot, except toes |
| 2 | ICD-9 | `70715` | Ulcer of other part of foot |
| 3 | ICD-9 | `2761` | Hyposmolality and/or hyponatremia |
| 4 | ICD-9 | `40390` | Hypertensive chronic kidney disease, unspecified, with chronic kidney disease stage I through stage IV, or unspecified |
| 5 | ICD-9 | `5859` | Chronic kidney disease, unspecified |
| 6 | ICD-9 | `25062` | Diabetes with neurological manifestations, type II or unspecified type, uncontrolled |
| 7 | ICD-9 | `3572` | Polyneuropathy in diabetes |
| 8 | ICD-9 | `2720` | Pure hypercholesterolemia |
| 9 | ICD-9 | `27800` | Obesity, unspecified |
| 10 | ICD-9 | `30503` | Alcohol abuse, in remission |
| 11 | ICD-9 | `V1581` | Personal history of noncompliance with medical treatment, presenting hazards to health |
| 12 | ICD-9 | `V5866` | Long-term (current) use of aspirin |
| 13 | ICD-9 | `V5867` | Long-term (current) use of insulin |
| 14 | ICD-9 | `V707` | Examination of participant in clinical trial |

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
| 2187-12-14 12:49:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2187-12-14 12:49:00 | Transfer | → Emergency Department (ED) |
| 2187-12-14 15:48:00 | Admission | Admitted from EMERGENCY ROOM (EU OBSERVATION) |
| 2187-12-14 17:48:00 | ED Departure | Left Emergency Dept. |
| 2187-12-16 14:38:00 | Discharge | To N/A |

## 10. Missing / Ambiguous Data

- Discharge location not recorded.
- No procedure ICD codes — procedures may not have been coded or were minor.
- No ICU stay — patient managed on floor/step-down only.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
