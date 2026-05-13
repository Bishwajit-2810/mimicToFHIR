# Encounter Report — HADM 29462354

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 29462354 |
| Subject ID | 10035631 |
| Patient Sex | M |
| Patient Anchor Age (at anchor year) | 63 |
| Anchor Year | 2112 |
| Admission Time | 2112-09-17 19:13:00 |
| Discharge Time | 2112-10-17 01:41:00 |
| Admission Type | DIRECT EMER. |
| Admission Location | PHYSICIAN REFERRAL |
| Discharge Location | HOME |
| Insurance | Other |
| Language | ENGLISH |
| Marital Status | MARRIED |
| Race/Ethnicity | UNKNOWN |
| ED Registration | 2112-09-17 18:46:00 |
| ED Departure | 2112-09-17 19:50:00 |
| In-Hospital Mortality | No |
| Date of Death (overall) | 2116-03-12 |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| HCFA | 834 | ACUTE LEUKEMIA W/O MAJOR O.R. PROCEDURE W MCC | N/A | N/A |
| APR | 690 | ACUTE LEUKEMIA | 3.0 | 2.0 |

### Primary Diagnosis (seq_num = 1)

- **ICD-9 20500**: Acute myeloid leukemia, without mention of having achieved remission

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2112-09-17 19:14:01 | N/A | MED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-9 `20500`: Acute myeloid leukemia, without mention of having achieved remission
- (seq 2) ICD-9 `4809`: Viral pneumonia, unspecified
- (seq 3) ICD-9 `28419`: Other pancytopenia
- (seq 4) ICD-9 `5733`: Hepatitis, unspecified
- (seq 5) ICD-9 `7907`: Bacteremia

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-9 | `20500` | Acute myeloid leukemia, without mention of having achieved remission |
| 2 | ICD-9 | `4809` | Viral pneumonia, unspecified |
| 3 | ICD-9 | `28419` | Other pancytopenia |
| 4 | ICD-9 | `5733` | Hepatitis, unspecified |
| 5 | ICD-9 | `7907` | Bacteremia |
| 6 | ICD-9 | `99932` | Bloodstream infection due to central venous catheter |
| 7 | ICD-9 | `V707` | Examination of participant in clinical trial |
| 8 | ICD-9 | `61172` | Lump or mass in breast |
| 9 | ICD-9 | `78061` | Fever presenting with conditions classified elsewhere |
| 10 | ICD-9 | `04109` | Streptococcus infection in conditions classified elsewhere and of unspecified site, other streptococcus |
| 11 | ICD-9 | `E8798` | Other specified procedures as the cause of abnormal reaction of patient, or of later complication, without mention of misadventure at time of procedure |
| 12 | ICD-9 | `V1582` | Personal history of tobacco use |
| 13 | ICD-9 | `3393` | Drug induced headache, not elsewhere classified |
| 14 | ICD-9 | `E9348` | Other agents affecting blood constituents causing adverse effects in therapeutic use |
| 15 | ICD-9 | `E9319` | Other and unspecified anti-infectives causing adverse effects in therapeutic use |
| 16 | ICD-9 | `78791` | Diarrhea |
| 17 | ICD-9 | `V6402` | Vaccination not carried out because of chronic illness or condition |
| 18 | ICD-9 | `28804` | Neutropenia due to infection |

## 5. ICU Stays

_No ICU stay recorded for this admission._

## 6. Escalation / Severity Indicators

The following critical conditions or interventions were detected:

- **Pneumonia** (ICD diagnosis)

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2112-09-20 | ICD-9 | `9925` | Injection or infusion of cancer chemotherapeutic substance |
| 2 | 2112-09-18 | ICD-9 | `4131` | Biopsy of bone marrow |
| 3 | 2112-09-19 | ICD-9 | `3897` | Central venous catheter placement with guidance |
| 4 | 2112-09-20 | ICD-9 | `4131` | Biopsy of bone marrow |
| 5 | 2112-10-17 | ICD-9 | `4131` | Biopsy of bone marrow |


## 8. Critical Findings (Charted Events)

_No critical chart events detected._

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2112-09-17 18:46:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2112-09-17 18:46:00 | Transfer | → Emergency Department (ED) |
| 2112-09-17 19:13:00 | Admission | Admitted from PHYSICIAN REFERRAL (DIRECT EMER.) |
| 2112-09-17 19:50:00 | ED Departure | Left Emergency Dept. |
| 2112-10-04 08:13:45 | Transfer | → Hematology/Oncology (transfer) |
| 2112-10-04 08:14:27 | Transfer | → Hematology/Oncology (transfer) |
| 2112-10-06 15:13:50 | Transfer | → Hematology/Oncology (transfer) |
| 2112-10-17 01:41:00 | Discharge | To HOME |

## 10. Missing / Ambiguous Data

- No ICU stay — patient managed on floor/step-down only.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
