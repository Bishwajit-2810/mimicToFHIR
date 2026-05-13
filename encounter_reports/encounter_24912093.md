# Encounter Report — HADM 24912093

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 24912093 |
| Subject ID | 10035631 |
| Patient Sex | M |
| Patient Anchor Age (at anchor year) | 63 |
| Anchor Year | 2112 |
| Admission Time | 2112-10-22 00:00:00 |
| Discharge Time | 2112-10-28 12:16:00 |
| Admission Type | ELECTIVE |
| Admission Location | PHYSICIAN REFERRAL |
| Discharge Location | HOME HEALTH CARE |
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
| HCFA | 839 | CHEMO W ACUTE LEUKEMIA AS SDX W/O CC/MCC | N/A | N/A |

### Primary Diagnosis (seq_num = 1)

- **ICD-9 V5811**: Encounter for antineoplastic chemotherapy

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2112-10-22 14:14:40 | N/A | OMED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-9 `V5811`: Encounter for antineoplastic chemotherapy
- (seq 2) ICD-9 `20501`: Acute myeloid leukemia, in remission
- (seq 3) ICD-9 `V707`: Examination of participant in clinical trial
- (seq 4) ICD-9 `V1582`: Personal history of tobacco use
- (seq 5) ICD-9 `7905`: Other nonspecific abnormal serum enzyme levels

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-9 | `V5811` | Encounter for antineoplastic chemotherapy |
| 2 | ICD-9 | `20501` | Acute myeloid leukemia, in remission |
| 3 | ICD-9 | `V707` | Examination of participant in clinical trial |
| 4 | ICD-9 | `V1582` | Personal history of tobacco use |
| 5 | ICD-9 | `7905` | Other nonspecific abnormal serum enzyme levels |

## 5. ICU Stays

_No ICU stay recorded for this admission._

## 6. Escalation / Severity Indicators

_No escalation indicators detected from ICD codes or ICU procedure events._

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2112-10-22 | ICD-9 | `9925` | Injection or infusion of cancer chemotherapeutic substance |
| 2 | 2112-10-22 | ICD-9 | `3897` | Central venous catheter placement with guidance |


## 8. Critical Findings (Charted Events)

_No critical chart events detected._

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2112-10-22 00:00:00 | Admission | Admitted from PHYSICIAN REFERRAL (ELECTIVE) |
| 2112-10-28 12:16:00 | Discharge | To HOME HEALTH CARE |

## 10. Missing / Ambiguous Data

- No ED registration time — admission may not have gone through ED.
- No ICU stay — patient managed on floor/step-down only.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
