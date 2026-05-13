# Encounter Report — HADM 28543425

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 28543425 |
| Subject ID | 10037928 |
| Patient Sex | F |
| Patient Anchor Age (at anchor year) | 78 |
| Anchor Year | 2175 |
| Admission Time | 2175-10-26 01:31:00 |
| Discharge Time | 2175-10-26 12:48:00 |
| Admission Type | EU OBSERVATION |
| Admission Location | EMERGENCY ROOM |
| Discharge Location | N/A |
| Insurance | Medicare |
| Language | ? |
| Marital Status | SINGLE |
| Race/Ethnicity | HISPANIC OR LATINO |
| ED Registration | 2175-10-25 19:55:00 |
| ED Departure | 2175-10-26 12:48:00 |
| In-Hospital Mortality | No |
| Date of Death (overall) | N/A |

## 2. Hospital Visit Reason

### Primary Diagnosis (seq_num = 1)

- **ICD-9 8052**: Closed fracture of dorsal [thoracic] vertebra without mention of spinal cord injury

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2175-10-26 01:32:33 | N/A | MED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-9 `8052`: Closed fracture of dorsal [thoracic] vertebra without mention of spinal cord injury
- (seq 2) ICD-9 `9243`: Contusion of toe
- (seq 3) ICD-9 `E8889`: Unspecified fall
- (seq 4) ICD-9 `E8490`: Home accidents
- (seq 5) ICD-9 `25000`: Diabetes mellitus without mention of complication, type II or unspecified type, not stated as uncontrolled

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-9 | `8052` | Closed fracture of dorsal [thoracic] vertebra without mention of spinal cord injury |
| 2 | ICD-9 | `9243` | Contusion of toe |
| 3 | ICD-9 | `E8889` | Unspecified fall |
| 4 | ICD-9 | `E8490` | Home accidents |
| 5 | ICD-9 | `25000` | Diabetes mellitus without mention of complication, type II or unspecified type, not stated as uncontrolled |
| 6 | ICD-9 | `4019` | Unspecified essential hypertension |

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
| 2175-10-25 19:55:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2175-10-25 19:55:00 | Transfer | → Emergency Department (ED) |
| 2175-10-26 01:31:00 | Admission | Admitted from EMERGENCY ROOM (EU OBSERVATION) |
| 2175-10-26 12:48:00 | Discharge | To N/A |
| 2175-10-26 12:48:00 | ED Departure | Left Emergency Dept. |

## 10. Missing / Ambiguous Data

- Discharge location not recorded.
- No procedure ICD codes — procedures may not have been coded or were minor.
- No ICU stay — patient managed on floor/step-down only.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
