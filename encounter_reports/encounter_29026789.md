# Encounter Report — HADM 29026789

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 29026789 |
| Subject ID | 10038999 |
| Patient Sex | M |
| Patient Anchor Age (at anchor year) | 45 |
| Anchor Year | 2131 |
| Admission Time | 2132-05-17 23:32:00 |
| Discharge Time | 2132-05-23 13:01:00 |
| Admission Type | EW EMER. |
| Admission Location | TRANSFER FROM HOSPITAL |
| Discharge Location | REHAB |
| Insurance | Medicare |
| Language | ENGLISH |
| Marital Status | SINGLE |
| Race/Ethnicity | WHITE |
| ED Registration | 2132-05-17 19:56:00 |
| ED Departure | 2132-05-18 01:36:00 |
| In-Hospital Mortality | No |
| Date of Death (overall) | N/A |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| HCFA | 494 | LOWER EXTREM & HUMER PROC EXCEPT HIP,FOOT,FEMUR W/O CC/MCC | N/A | N/A |
| APR | 313 | KNEE & LOWER LEG PROCEDURES EXCEPT FOOT | 1.0 | 1.0 |

### Primary Diagnosis (seq_num = 1)

- **ICD-10 S82251A**: Displaced comminuted fracture of shaft of right tibia, initial encounter for closed fracture

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2132-05-17 23:33:51 | N/A | ORTHO |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-10 `S82251A`: Displaced comminuted fracture of shaft of right tibia, initial encounter for closed fracture
- (seq 2) ICD-10 `F09`: Unspecified mental disorder due to known physiological condition
- (seq 3) ICD-10 `G40909`: Epilepsy, unspecified, not intractable, without status epilepticus
- (seq 4) ICD-10 `H548`: Legal blindness, as defined in USA
- (seq 5) ICD-10 `W1830XA`: Fall on same level, unspecified, initial encounter

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-10 | `S82251A` | Displaced comminuted fracture of shaft of right tibia, initial encounter for closed fracture |
| 2 | ICD-10 | `F09` | Unspecified mental disorder due to known physiological condition |
| 3 | ICD-10 | `G40909` | Epilepsy, unspecified, not intractable, without status epilepticus |
| 4 | ICD-10 | `H548` | Legal blindness, as defined in USA |
| 5 | ICD-10 | `W1830XA` | Fall on same level, unspecified, initial encounter |
| 6 | ICD-10 | `Y92199` | Unspecified place in other specified residential institution as the place of occurrence of the external cause |

## 5. ICU Stays

_No ICU stay recorded for this admission._

## 6. Escalation / Severity Indicators

_No escalation indicators detected from ICD codes or ICU procedure events._

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2132-05-18 | ICD-10 | `0QSG06Z` | Reposition Right Tibia with Intramedullary Internal Fixation Device, Open Approach |


## 8. Critical Findings (Charted Events)

_No critical chart events detected._

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2132-05-17 19:56:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2132-05-17 19:56:00 | Transfer | → Emergency Department (ED) |
| 2132-05-17 23:32:00 | Admission | Admitted from TRANSFER FROM HOSPITAL (EW EMER.) |
| 2132-05-18 01:36:00 | ED Departure | Left Emergency Dept. |
| 2132-05-18 03:25:04 | Transfer | → Med/Surg/Trauma (transfer) |
| 2132-05-23 13:01:00 | Discharge | To REHAB |

## 10. Missing / Ambiguous Data

- No ICU stay — patient managed on floor/step-down only.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
