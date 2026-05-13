# Encounter Report — HADM 22380825

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 22380825 |
| Subject ID | 10002930 |
| Patient Sex | F |
| Patient Anchor Age (at anchor year) | 48 |
| Anchor Year | 2193 |
| Admission Time | 2193-08-05 06:18:00 |
| Discharge Time | 2193-08-05 11:44:00 |
| Admission Type | EU OBSERVATION |
| Admission Location | EMERGENCY ROOM |
| Discharge Location | N/A |
| Insurance | Medicare |
| Language | ENGLISH |
| Marital Status | SINGLE |
| Race/Ethnicity | BLACK/AFRICAN AMERICAN |
| ED Registration | 2193-08-05 05:04:00 |
| ED Departure | 2193-08-05 12:00:00 |
| In-Hospital Mortality | No |
| Date of Death (overall) | 2201-12-24 |

## 2. Hospital Visit Reason

### Primary Diagnosis (seq_num = 1)

- **ICD-9 311**: Depressive disorder, not elsewhere classified

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2193-08-05 06:19:32 | N/A | MED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-9 `311`: Depressive disorder, not elsewhere classified
- (seq 2) ICD-9 `V08`: Asymptomatic human immunodeficiency virus [HIV] infection status
- (seq 3) ICD-9 `3559`: Mononeuritis of unspecified site
- (seq 4) ICD-9 `V620`: Unemployment
- (seq 5) ICD-9 `30001`: Panic disorder without agoraphobia

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-9 | `311` | Depressive disorder, not elsewhere classified |
| 2 | ICD-9 | `V08` | Asymptomatic human immunodeficiency virus [HIV] infection status |
| 3 | ICD-9 | `3559` | Mononeuritis of unspecified site |
| 4 | ICD-9 | `V620` | Unemployment |
| 5 | ICD-9 | `30001` | Panic disorder without agoraphobia |
| 6 | ICD-9 | `V1552` | Personal history of traumatic brain injury |
| 7 | ICD-9 | `30500` | Alcohol abuse, unspecified |
| 8 | ICD-9 | `30560` | Cocaine abuse, unspecified |

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
| 2193-08-05 05:04:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2193-08-05 05:04:00 | Transfer | → Emergency Department (ED) |
| 2193-08-05 06:18:00 | Admission | Admitted from EMERGENCY ROOM (EU OBSERVATION) |
| 2193-08-05 11:44:00 | Discharge | To N/A |
| 2193-08-05 12:00:00 | ED Departure | Left Emergency Dept. |

## 10. Missing / Ambiguous Data

- Discharge location not recorded.
- No procedure ICD codes — procedures may not have been coded or were minor.
- No ICU stay — patient managed on floor/step-down only.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
