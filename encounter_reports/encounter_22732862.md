# Encounter Report — HADM 22732862

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 22732862 |
| Subject ID | 10035631 |
| Patient Sex | M |
| Patient Anchor Age (at anchor year) | 63 |
| Anchor Year | 2112 |
| Admission Time | 2112-11-10 15:55:00 |
| Discharge Time | 2112-11-20 16:20:00 |
| Admission Type | DIRECT EMER. |
| Admission Location | CLINIC REFERRAL |
| Discharge Location | HOME |
| Insurance | Other |
| Language | ENGLISH |
| Marital Status | MARRIED |
| Race/Ethnicity | UNKNOWN |
| ED Registration | N/A |
| ED Departure | N/A |
| In-Hospital Mortality | No |
| Date of Death (overall) | 2116-03-12 |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| HCFA | 314 | OTHER CIRCULATORY SYSTEM DIAGNOSES W MCC | N/A | N/A |
| APR | 721 | POST-OPERATIVE, POST-TRAUMATIC, OTHER DEVICE INFECTIONS | 4.0 | 3.0 |

### Primary Diagnosis (seq_num = 1)

- **ICD-9 99933**: Local infection due to central venous catheter

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2112-11-10 15:57:50 | N/A | OMED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-9 `99933`: Local infection due to central venous catheter
- (seq 2) ICD-9 `4846`: Pneumonia in aspergillosis
- (seq 3) ICD-9 `1173`: Aspergillosis
- (seq 4) ICD-9 `20500`: Acute myeloid leukemia, without mention of having achieved remission
- (seq 5) ICD-9 `28419`: Other pancytopenia

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-9 | `99933` | Local infection due to central venous catheter |
| 2 | ICD-9 | `4846` | Pneumonia in aspergillosis |
| 3 | ICD-9 | `1173` | Aspergillosis |
| 4 | ICD-9 | `20500` | Acute myeloid leukemia, without mention of having achieved remission |
| 5 | ICD-9 | `28419` | Other pancytopenia |
| 6 | ICD-9 | `6822` | Cellulitis and abscess of trunk |
| 7 | ICD-9 | `E8798` | Other specified procedures as the cause of abnormal reaction of patient, or of later complication, without mention of misadventure at time of procedure |
| 8 | ICD-9 | `V1582` | Personal history of tobacco use |
| 9 | ICD-9 | `V707` | Examination of participant in clinical trial |

## 5. ICU Stays

_No ICU stay recorded for this admission._

## 6. Escalation / Severity Indicators

The following critical conditions or interventions were detected:

- **Pneumonia** (ICD diagnosis)

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2112-11-14 | ICD-9 | `9749` | Removal of other device from thorax |
| 2 | 2112-11-15 | ICD-9 | `3324` | Closed [endoscopic] biopsy of bronchus |


## 8. Critical Findings (Charted Events)

_No critical chart events detected._

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2112-11-10 15:55:00 | Admission | Admitted from CLINIC REFERRAL (DIRECT EMER.) |
| 2112-11-11 18:39:01 | Transfer | → Hematology/Oncology (transfer) |
| 2112-11-14 19:20:53 | Transfer | → Hematology/Oncology (transfer) |
| 2112-11-15 19:48:29 | Transfer | → Hematology/Oncology (transfer) |
| 2112-11-20 16:20:00 | Discharge | To HOME |

## 10. Missing / Ambiguous Data

- No ED registration time — admission may not have gone through ED.
- No ICU stay — patient managed on floor/step-down only.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
