# Encounter Report — HADM 22196214

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 22196214 |
| Subject ID | 10010867 |
| Patient Sex | F |
| Patient Anchor Age (at anchor year) | 28 |
| Anchor Year | 2147 |
| Admission Time | 2148-03-07 23:30:00 |
| Discharge Time | 2148-03-13 15:50:00 |
| Admission Type | OBSERVATION ADMIT |
| Admission Location | EMERGENCY ROOM |
| Discharge Location | REHAB |
| Insurance | Other |
| Language | ENGLISH |
| Marital Status | DIVORCED |
| Race/Ethnicity | WHITE - BRAZILIAN |
| ED Registration | 2148-03-07 18:21:00 |
| ED Departure | 2148-03-08 00:50:00 |
| In-Hospital Mortality | No |
| Date of Death (overall) | N/A |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| HCFA | 188 | PLEURAL EFFUSION W/O CC/MCC | N/A | N/A |
| APR | 143 | OTHER RESPIRATORY DIAGNOSES EXCEPT SIGNS, SYMPTOMS & MINOR DIAGNOSES | 2.0 | 1.0 |

### Primary Diagnosis (seq_num = 1)

- **ICD-10 J90**: Pleural effusion, not elsewhere classified

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2148-03-07 23:31:05 | N/A | TRAUM |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-10 `J90`: Pleural effusion, not elsewhere classified
- (seq 2) ICD-10 `I272`: Other secondary pulmonary hypertension
- (seq 3) ICD-10 `M25511`: Pain in right shoulder
- (seq 4) ICD-10 `Z981`: Arthrodesis status
- (seq 5) ICD-10 `Z87820`: Personal history of traumatic brain injury

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-10 | `J90` | Pleural effusion, not elsewhere classified |
| 2 | ICD-10 | `I272` | Other secondary pulmonary hypertension |
| 3 | ICD-10 | `M25511` | Pain in right shoulder |
| 4 | ICD-10 | `Z981` | Arthrodesis status |
| 5 | ICD-10 | `Z87820` | Personal history of traumatic brain injury |
| 6 | ICD-10 | `V8609XS` | Driver of other special all-terrain or other off-road motor vehicle injured in traffic accident, sequela |
| 7 | ICD-10 | `Y92488` | Other paved roadways as the place of occurrence of the external cause |
| 8 | ICD-10 | `J45909` | Unspecified asthma, uncomplicated |
| 9 | ICD-10 | `E041` | Nontoxic single thyroid nodule |
| 10 | ICD-10 | `G43909` | Migraine, unspecified, not intractable, without status migrainosus |
| 11 | ICD-10 | `F1210` | Cannabis abuse, uncomplicated |

## 5. ICU Stays

_No ICU stay recorded for this admission._

## 6. Escalation / Severity Indicators

_No escalation indicators detected from ICD codes or ICU procedure events._

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2148-03-09 | ICD-10 | `0W9930Z` | Drainage of Right Pleural Cavity with Drainage Device, Percutaneous Approach |


## 8. Critical Findings (Charted Events)

_No critical chart events detected._

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2148-03-07 18:21:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2148-03-07 18:21:00 | Transfer | → Emergency Department (ED) |
| 2148-03-07 23:30:00 | Admission | Admitted from EMERGENCY ROOM (OBSERVATION ADMIT) |
| 2148-03-08 00:50:00 | ED Departure | Left Emergency Dept. |
| 2148-03-13 15:50:00 | Discharge | To REHAB |

## 10. Missing / Ambiguous Data

- No ICU stay — patient managed on floor/step-down only.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
