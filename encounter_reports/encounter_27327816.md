# Encounter Report — HADM 27327816

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 27327816 |
| Subject ID | 10025463 |
| Patient Sex | M |
| Patient Anchor Age (at anchor year) | 66 |
| Anchor Year | 2136 |
| Admission Time | 2136-10-31 07:15:00 |
| Discharge Time | 2136-11-02 16:50:00 |
| Admission Type | DIRECT EMER. |
| Admission Location | PHYSICIAN REFERRAL |
| Discharge Location | HOME |
| Insurance | Other |
| Language | ENGLISH |
| Marital Status | MARRIED |
| Race/Ethnicity | WHITE |
| ED Registration | N/A |
| ED Departure | N/A |
| In-Hospital Mortality | No |
| Date of Death (overall) | 2137-10-09 |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| APR | 175 | PERCUTANEOUS CORONARY INTERVENTION W/O AMI | 1.0 | 1.0 |
| HCFA | 251 | PERC CARDIOVASC PROC W/O CORONARY ARTERY STENT W/O MCC | N/A | N/A |

### Primary Diagnosis (seq_num = 1)

- **ICD-9 42731**: Atrial fibrillation

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2136-10-31 16:13:42 | N/A | CMED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-9 `42731`: Atrial fibrillation
- (seq 2) ICD-9 `4019`: Unspecified essential hypertension
- (seq 3) ICD-9 `2724`: Other and unspecified hyperlipidemia
- (seq 4) ICD-9 `56210`: Diverticulosis of colon (without mention of hemorrhage)
- (seq 5) ICD-9 `V1582`: Personal history of tobacco use

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-9 | `42731` | Atrial fibrillation |
| 2 | ICD-9 | `4019` | Unspecified essential hypertension |
| 3 | ICD-9 | `2724` | Other and unspecified hyperlipidemia |
| 4 | ICD-9 | `56210` | Diverticulosis of colon (without mention of hemorrhage) |
| 5 | ICD-9 | `V1582` | Personal history of tobacco use |

## 5. ICU Stays

_No ICU stay recorded for this admission._

## 6. Escalation / Severity Indicators

_No escalation indicators detected from ICD codes or ICU procedure events._

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2136-10-31 | ICD-9 | `3734` | Excision or destruction of other lesion or tissue of heart, endovascular approach |
| 2 | 2136-10-31 | ICD-9 | `3727` | Cardiac mapping |
| 3 | 2136-10-31 | ICD-9 | `3726` | Catheter based invasive electrophysiologic testing |
| 4 | 2136-10-31 | ICD-9 | `9962` | Other electric countershock of heart |


## 8. Critical Findings (Charted Events)

_No critical chart events detected._

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2136-10-31 07:15:00 | Admission | Admitted from PHYSICIAN REFERRAL (DIRECT EMER.) |
| 2136-11-02 16:50:00 | Discharge | To HOME |

## 10. Missing / Ambiguous Data

- No ED registration time — admission may not have gone through ED.
- No ICU stay — patient managed on floor/step-down only.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
