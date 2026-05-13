# Encounter Report — HADM 20611796

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 20611796 |
| Subject ID | 10019385 |
| Patient Sex | M |
| Patient Anchor Age (at anchor year) | 44 |
| Anchor Year | 2180 |
| Admission Time | 2180-03-04 01:16:00 |
| Discharge Time | 2180-03-06 18:32:00 |
| Admission Type | OBSERVATION ADMIT |
| Admission Location | EMERGENCY ROOM |
| Discharge Location | HOME HEALTH CARE |
| Insurance | Other |
| Language | ENGLISH |
| Marital Status | MARRIED |
| Race/Ethnicity | WHITE |
| ED Registration | 2180-03-03 20:26:00 |
| ED Departure | 2180-03-04 02:24:00 |
| In-Hospital Mortality | No |
| Date of Death (overall) | N/A |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| HCFA | 303 | ATHEROSCLEROSIS W/O MCC | N/A | N/A |
| APR | 198 | ANGINA PECTORIS & CORONARY ATHEROSCLEROSIS | 1.0 | 1.0 |

### Primary Diagnosis (seq_num = 1)

- **ICD-10 I25119**: Atherosclerotic heart disease of native coronary artery with unspecified angina pectoris

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2180-03-04 01:16:56 | N/A | CMED |
| 2180-03-04 10:37:37 | CMED | CSURG |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-10 `I25119`: Atherosclerotic heart disease of native coronary artery with unspecified angina pectoris
- (seq 2) ICD-10 `E785`: Hyperlipidemia, unspecified
- (seq 3) ICD-10 `F17210`: Nicotine dependence, cigarettes, uncomplicated
- (seq 4) ICD-10 `Z8249`: Family history of ischemic heart disease and other diseases of the circulatory system
- (seq 5) ICD-10 `Z951`: Presence of aortocoronary bypass graft

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-10 | `I25119` | Atherosclerotic heart disease of native coronary artery with unspecified angina pectoris |
| 2 | ICD-10 | `E785` | Hyperlipidemia, unspecified |
| 3 | ICD-10 | `F17210` | Nicotine dependence, cigarettes, uncomplicated |
| 4 | ICD-10 | `Z8249` | Family history of ischemic heart disease and other diseases of the circulatory system |
| 5 | ICD-10 | `Z951` | Presence of aortocoronary bypass graft |
| 6 | ICD-10 | `Z955` | Presence of coronary angioplasty implant and graft |
| 7 | ICD-10 | `K219` | Gastro-esophageal reflux disease without esophagitis |

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
| 2180-03-03 20:26:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2180-03-03 20:26:00 | Transfer | → Emergency Department (ED) |
| 2180-03-04 01:16:00 | Admission | Admitted from EMERGENCY ROOM (OBSERVATION ADMIT) |
| 2180-03-04 02:24:00 | ED Departure | Left Emergency Dept. |
| 2180-03-06 18:32:00 | Discharge | To HOME HEALTH CARE |

## 10. Missing / Ambiguous Data

- No procedure ICD codes — procedures may not have been coded or were minor.
- No ICU stay — patient managed on floor/step-down only.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
