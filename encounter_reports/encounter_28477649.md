# Encounter Report — HADM 28477649

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 28477649 |
| Subject ID | 10002930 |
| Patient Sex | F |
| Patient Anchor Age (at anchor year) | 48 |
| Anchor Year | 2193 |
| Admission Time | 2197-04-07 06:56:00 |
| Discharge Time | 2197-04-08 19:37:00 |
| Admission Type | EU OBSERVATION |
| Admission Location | EMERGENCY ROOM |
| Discharge Location | N/A |
| Insurance | Medicare |
| Language | ENGLISH |
| Marital Status | SINGLE |
| Race/Ethnicity | BLACK/AFRICAN AMERICAN |
| ED Registration | 2197-04-07 03:20:00 |
| ED Departure | 2197-04-08 20:14:00 |
| In-Hospital Mortality | No |
| Date of Death (overall) | 2201-12-24 |

## 2. Hospital Visit Reason

### Primary Diagnosis (seq_num = 1)

- **ICD-9 2989**: Unspecified psychosis

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2197-04-07 06:56:40 | N/A | MED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-9 `2989`: Unspecified psychosis
- (seq 2) ICD-9 `V6284`: Suicidal ideation
- (seq 3) ICD-9 `07070`: Unspecified viral hepatitis C without hepatic coma
- (seq 4) ICD-9 `V08`: Asymptomatic human immunodeficiency virus [HIV] infection status
- (seq 5) ICD-9 `V1552`: Personal history of traumatic brain injury

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-9 | `2989` | Unspecified psychosis |
| 2 | ICD-9 | `V6284` | Suicidal ideation |
| 3 | ICD-9 | `07070` | Unspecified viral hepatitis C without hepatic coma |
| 4 | ICD-9 | `V08` | Asymptomatic human immunodeficiency virus [HIV] infection status |
| 5 | ICD-9 | `V1552` | Personal history of traumatic brain injury |
| 6 | ICD-9 | `30500` | Alcohol abuse, unspecified |
| 7 | ICD-9 | `30560` | Cocaine abuse, unspecified |

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
| 2197-04-07 03:20:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2197-04-07 03:20:00 | Transfer | → Emergency Department (ED) |
| 2197-04-07 06:56:00 | Admission | Admitted from EMERGENCY ROOM (EU OBSERVATION) |
| 2197-04-08 19:37:00 | Discharge | To N/A |
| 2197-04-08 20:14:00 | ED Departure | Left Emergency Dept. |

## 10. Missing / Ambiguous Data

- Discharge location not recorded.
- No procedure ICD codes — procedures may not have been coded or were minor.
- No ICU stay — patient managed on floor/step-down only.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
