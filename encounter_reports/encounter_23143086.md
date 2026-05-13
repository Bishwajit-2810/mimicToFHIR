# Encounter Report — HADM 23143086

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 23143086 |
| Subject ID | 10020740 |
| Patient Sex | M |
| Patient Anchor Age (at anchor year) | 56 |
| Anchor Year | 2150 |
| Admission Time | 2151-01-15 15:25:00 |
| Discharge Time | 2151-01-16 02:38:00 |
| Admission Type | EU OBSERVATION |
| Admission Location | EMERGENCY ROOM |
| Discharge Location | N/A |
| Insurance | Other |
| Language | ENGLISH |
| Marital Status | SINGLE |
| Race/Ethnicity | WHITE |
| ED Registration | 2151-01-15 11:47:00 |
| ED Departure | 2151-01-16 02:38:00 |
| In-Hospital Mortality | No |
| Date of Death (overall) | N/A |

## 2. Hospital Visit Reason

### Primary Diagnosis (seq_num = 1)

- **ICD-9 29574**: Schizoaffective disorder, chronic with acute exacerbation

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2151-01-15 15:26:40 | N/A | MED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-9 `29574`: Schizoaffective disorder, chronic with acute exacerbation
- (seq 2) ICD-9 `25000`: Diabetes mellitus without mention of complication, type II or unspecified type, not stated as uncontrolled
- (seq 3) ICD-9 `V5867`: Long-term (current) use of insulin

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-9 | `29574` | Schizoaffective disorder, chronic with acute exacerbation |
| 2 | ICD-9 | `25000` | Diabetes mellitus without mention of complication, type II or unspecified type, not stated as uncontrolled |
| 3 | ICD-9 | `V5867` | Long-term (current) use of insulin |

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
| 2151-01-15 11:47:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2151-01-15 11:47:00 | Transfer | → Emergency Department (ED) |
| 2151-01-15 15:25:00 | Admission | Admitted from EMERGENCY ROOM (EU OBSERVATION) |
| 2151-01-16 02:38:00 | Discharge | To N/A |
| 2151-01-16 02:38:00 | ED Departure | Left Emergency Dept. |

## 10. Missing / Ambiguous Data

- Discharge location not recorded.
- No procedure ICD codes — procedures may not have been coded or were minor.
- No ICU stay — patient managed on floor/step-down only.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
