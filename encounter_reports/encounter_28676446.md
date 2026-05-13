# Encounter Report — HADM 28676446

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 28676446 |
| Subject ID | 10002428 |
| Patient Sex | F |
| Patient Anchor Age (at anchor year) | 80 |
| Anchor Year | 2155 |
| Admission Time | 2157-07-16 04:09:00 |
| Discharge Time | 2157-07-18 16:49:00 |
| Admission Type | EU OBSERVATION |
| Admission Location | EMERGENCY ROOM |
| Discharge Location | N/A |
| Insurance | Medicare |
| Language | ENGLISH |
| Marital Status | WIDOWED |
| Race/Ethnicity | WHITE |
| ED Registration | 2157-07-16 01:50:00 |
| ED Departure | 2157-07-16 09:51:00 |
| In-Hospital Mortality | No |
| Date of Death (overall) | N/A |

## 2. Hospital Visit Reason

### Primary Diagnosis (seq_num = 1)

- **ICD-9 82009**: Other closed transcervical fracture of neck of femur

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2157-07-16 04:11:33 | N/A | ORTHO |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-9 `82009`: Other closed transcervical fracture of neck of femur
- (seq 2) ICD-9 `E8859`: Fall from other slipping, tripping, or stumbling
- (seq 3) ICD-9 `4019`: Unspecified essential hypertension
- (seq 4) ICD-9 `V1261`: Personal history of pneumonia (recurrent)
- (seq 5) ICD-9 `4240`: Mitral valve disorders

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-9 | `82009` | Other closed transcervical fracture of neck of femur |
| 2 | ICD-9 | `E8859` | Fall from other slipping, tripping, or stumbling |
| 3 | ICD-9 | `4019` | Unspecified essential hypertension |
| 4 | ICD-9 | `V1261` | Personal history of pneumonia (recurrent) |
| 5 | ICD-9 | `4240` | Mitral valve disorders |
| 6 | ICD-9 | `7102` | Sicca syndrome |
| 7 | ICD-9 | `2724` | Other and unspecified hyperlipidemia |
| 8 | ICD-9 | `2469` | Unspecified disorder of thyroid |
| 9 | ICD-9 | `V441` | Gastrostomy status |

## 5. ICU Stays

_No ICU stay recorded for this admission._

## 6. Escalation / Severity Indicators

_No escalation indicators detected from ICD codes or ICU procedure events._

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2157-07-16 | ICD-9 | `7915` | Closed reduction of fracture with internal fixation, femur |


## 8. Critical Findings (Charted Events)

_No critical chart events detected._

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2157-07-16 01:50:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2157-07-16 01:50:00 | Transfer | → Emergency Department (ED) |
| 2157-07-16 04:09:00 | Admission | Admitted from EMERGENCY ROOM (EU OBSERVATION) |
| 2157-07-16 04:12:01 | Transfer | → Med/Surg/GYN (transfer) |
| 2157-07-16 04:35:09 | Transfer | → Discharge Lounge (transfer) |
| 2157-07-16 06:03:28 | Transfer | → Neurology (transfer) |
| 2157-07-16 06:17:53 | Transfer | → Discharge Lounge (transfer) |
| 2157-07-16 09:19:00 | Transfer | → Neurology (transfer) |
| 2157-07-16 09:51:00 | ED Departure | Left Emergency Dept. |
| 2157-07-18 16:49:00 | Discharge | To N/A |

## 10. Missing / Ambiguous Data

- Discharge location not recorded.
- No ICU stay — patient managed on floor/step-down only.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
