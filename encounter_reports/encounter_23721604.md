# Encounter Report — HADM 23721604

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 23721604 |
| Subject ID | 10037928 |
| Patient Sex | F |
| Patient Anchor Age (at anchor year) | 78 |
| Anchor Year | 2175 |
| Admission Time | 2179-03-27 18:27:00 |
| Discharge Time | 2179-04-04 19:40:00 |
| Admission Type | EW EMER. |
| Admission Location | EMERGENCY ROOM |
| Discharge Location | HOME HEALTH CARE |
| Insurance | Medicare |
| Language | ? |
| Marital Status | WIDOWED |
| Race/Ethnicity | HISPANIC/LATINO - CUBAN |
| ED Registration | 2179-03-27 14:15:00 |
| ED Departure | 2179-03-27 19:48:00 |
| In-Hospital Mortality | No |
| Date of Death (overall) | N/A |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| APR | 248 | MAJOR GASTROINTESTINAL & PERITONEAL INFECTIONS | 4.0 | 3.0 |
| HCFA | 371 | MAJOR GASTROINTESTINAL DISORDERS & PERITONEAL INFECTIONS W MCC | N/A | N/A |

### Primary Diagnosis (seq_num = 1)

- **ICD-9 00845**: Intestinal infection due to Clostridium difficile

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2179-03-27 18:28:18 | N/A | MED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-9 `00845`: Intestinal infection due to Clostridium difficile
- (seq 2) ICD-9 `4870`: Influenza with pneumonia
- (seq 3) ICD-9 `5849`: Acute kidney failure, unspecified
- (seq 4) ICD-9 `2763`: Alkalosis
- (seq 5) ICD-9 `99931`: Other and unspecified infection due to central venous catheter

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-9 | `00845` | Intestinal infection due to Clostridium difficile |
| 2 | ICD-9 | `4870` | Influenza with pneumonia |
| 3 | ICD-9 | `5849` | Acute kidney failure, unspecified |
| 4 | ICD-9 | `2763` | Alkalosis |
| 5 | ICD-9 | `99931` | Other and unspecified infection due to central venous catheter |
| 6 | ICD-9 | `25002` | Diabetes mellitus without mention of complication, type II or unspecified type, uncontrolled |
| 7 | ICD-9 | `1121` | Candidiasis of vulva and vagina |
| 8 | ICD-9 | `7245` | Backache, unspecified |
| 9 | ICD-9 | `6824` | Cellulitis and abscess of hand, except fingers and thumb |
| 10 | ICD-9 | `2809` | Iron deficiency anemia, unspecified |
| 11 | ICD-9 | `53081` | Esophageal reflux |
| 12 | ICD-9 | `33829` | Other chronic pain |
| 13 | ICD-9 | `78052` | Insomnia, unspecified |
| 14 | ICD-9 | `4019` | Unspecified essential hypertension |
| 15 | ICD-9 | `2724` | Other and unspecified hyperlipidemia |
| 16 | ICD-9 | `311` | Depressive disorder, not elsewhere classified |
| 17 | ICD-9 | `30000` | Anxiety state, unspecified |
| 18 | ICD-9 | `E8798` | Other specified procedures as the cause of abnormal reaction of patient, or of later complication, without mention of misadventure at time of procedure |
| 19 | ICD-9 | `E8497` | Accidents occurring in residential institution |
| 20 | ICD-9 | `V5867` | Long-term (current) use of insulin |
| 21 | ICD-9 | `V1302` | Personal history, urinary (tract) infection |
| 22 | ICD-9 | `V1001` | Personal history of malignant neoplasm of tongue |

## 5. ICU Stays

_No ICU stay recorded for this admission._

## 6. Escalation / Severity Indicators

The following critical conditions or interventions were detected:

- **Acute Kidney Injury** (ICD diagnosis)

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2179-04-03 | ICD-9 | `3324` | Closed [endoscopic] biopsy of bronchus |


## 8. Critical Findings (Charted Events)

_No critical chart events detected._

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2179-03-27 14:15:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2179-03-27 14:15:00 | Transfer | → Emergency Department (ED) |
| 2179-03-27 18:27:00 | Admission | Admitted from EMERGENCY ROOM (EW EMER.) |
| 2179-03-27 19:48:00 | ED Departure | Left Emergency Dept. |
| 2179-03-31 17:23:05 | Transfer | → Med/Surg (transfer) |
| 2179-04-04 19:40:00 | Discharge | To HOME HEALTH CARE |

## 10. Missing / Ambiguous Data

- No ICU stay — patient managed on floor/step-down only.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
