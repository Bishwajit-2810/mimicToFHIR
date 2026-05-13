# Encounter Report — HADM 25166559

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 25166559 |
| Subject ID | 10026406 |
| Patient Sex | M |
| Patient Anchor Age (at anchor year) | 45 |
| Anchor Year | 2129 |
| Admission Time | 2133-03-01 19:30:00 |
| Discharge Time | 2133-03-04 17:05:00 |
| Admission Type | EU OBSERVATION |
| Admission Location | WALK-IN/SELF REFERRAL |
| Discharge Location | N/A |
| Insurance | Other |
| Language | ENGLISH |
| Marital Status | DIVORCED |
| Race/Ethnicity | WHITE |
| ED Registration | 2133-03-01 16:42:00 |
| ED Departure | 2133-03-04 17:05:00 |
| In-Hospital Mortality | No |
| Date of Death (overall) | N/A |

## 2. Hospital Visit Reason

### Primary Diagnosis (seq_num = 1)

- **ICD-10 F10229**: Alcohol dependence with intoxication, unspecified

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2133-03-01 19:31:03 | N/A | MED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-10 `F10229`: Alcohol dependence with intoxication, unspecified
- (seq 2) ICD-10 `F10239`: Alcohol dependence with withdrawal, unspecified
- (seq 3) ICD-10 `F39`: Unspecified mood [affective] disorder
- (seq 4) ICD-10 `F17210`: Nicotine dependence, cigarettes, uncomplicated
- (seq 5) ICD-10 `Z590`: Homelessness

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-10 | `F10229` | Alcohol dependence with intoxication, unspecified |
| 2 | ICD-10 | `F10239` | Alcohol dependence with withdrawal, unspecified |
| 3 | ICD-10 | `F39` | Unspecified mood [affective] disorder |
| 4 | ICD-10 | `F17210` | Nicotine dependence, cigarettes, uncomplicated |
| 5 | ICD-10 | `Z590` | Homelessness |
| 6 | ICD-10 | `F419` | Anxiety disorder, unspecified |
| 7 | ICD-10 | `Z915` | Personal history of self-harm |

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
| 2133-03-01 16:42:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2133-03-01 16:42:00 | Transfer | → Emergency Department (ED) |
| 2133-03-01 19:30:00 | Admission | Admitted from WALK-IN/SELF REFERRAL (EU OBSERVATION) |
| 2133-03-04 17:05:00 | Discharge | To N/A |
| 2133-03-04 17:05:00 | ED Departure | Left Emergency Dept. |

## 10. Missing / Ambiguous Data

- Discharge location not recorded.
- No procedure ICD codes — procedures may not have been coded or were minor.
- No ICU stay — patient managed on floor/step-down only.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
