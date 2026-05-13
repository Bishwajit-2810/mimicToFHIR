# Encounter Report — HADM 29839885

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 29839885 |
| Subject ID | 10023117 |
| Patient Sex | M |
| Patient Anchor Age (at anchor year) | 53 |
| Anchor Year | 2170 |
| Admission Time | 2170-10-08 07:15:00 |
| Discharge Time | 2170-10-09 16:30:00 |
| Admission Type | SURGICAL SAME DAY ADMISSION |
| Admission Location | PHYSICIAN REFERRAL |
| Discharge Location | HOME HEALTH CARE |
| Insurance | Medicare |
| Language | ENGLISH |
| Marital Status | WIDOWED |
| Race/Ethnicity | WHITE |
| ED Registration | N/A |
| ED Departure | N/A |
| In-Hospital Mortality | No |
| Date of Death (overall) | 2175-07-20 |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| HCFA | 227 | CARDIAC DEFIBRILLATOR IMPLANT W/O CARDIAC CATH W/O MCC | N/A | N/A |
| APR | 161 | CARDIAC DEFIBRILLATOR & HEART ASSIST IMPLANT | 1.0 | 2.0 |

### Primary Diagnosis (seq_num = 1)

- **ICD-9 99604**: Mechanical complication of automatic implantable cardiac defibrillator

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2170-10-08 00:41:32 | N/A | CMED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-9 `99604`: Mechanical complication of automatic implantable cardiac defibrillator
- (seq 2) ICD-9 `42822`: Chronic systolic heart failure
- (seq 3) ICD-9 `4254`: Other primary cardiomyopathies
- (seq 4) ICD-9 `E8798`: Other specified procedures as the cause of abnormal reaction of patient, or of later complication, without mention of misadventure at time of procedure
- (seq 5) ICD-9 `E8498`: Accidents occurring in other specified places

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-9 | `99604` | Mechanical complication of automatic implantable cardiac defibrillator |
| 2 | ICD-9 | `42822` | Chronic systolic heart failure |
| 3 | ICD-9 | `4254` | Other primary cardiomyopathies |
| 4 | ICD-9 | `E8798` | Other specified procedures as the cause of abnormal reaction of patient, or of later complication, without mention of misadventure at time of procedure |
| 5 | ICD-9 | `E8498` | Accidents occurring in other specified places |
| 6 | ICD-9 | `4280` | Congestive heart failure, unspecified |
| 7 | ICD-9 | `27800` | Obesity, unspecified |

## 5. ICU Stays

_No ICU stay recorded for this admission._

## 6. Escalation / Severity Indicators

_No escalation indicators detected from ICD codes or ICU procedure events._

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2170-10-08 | ICD-9 | `0051` | Implantation of cardiac resynchronization defibrillator, total system [CRT-D] |


## 8. Critical Findings (Charted Events)

_No critical chart events detected._

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2170-10-08 07:15:00 | Admission | Admitted from PHYSICIAN REFERRAL (SURGICAL SAME DAY ADMISSION) |
| 2170-10-08 16:48:44 | Transfer | → Medicine/Cardiology (transfer) |
| 2170-10-09 16:30:00 | Discharge | To HOME HEALTH CARE |

## 10. Missing / Ambiguous Data

- No ED registration time — admission may not have gone through ED.
- No ICU stay — patient managed on floor/step-down only.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
