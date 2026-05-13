# Encounter Report — HADM 27496788

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 27496788 |
| Subject ID | 10035631 |
| Patient Sex | M |
| Patient Anchor Age (at anchor year) | 63 |
| Anchor Year | 2112 |
| Admission Time | 2113-08-26 17:07:00 |
| Discharge Time | 2113-08-29 15:18:00 |
| Admission Type | DIRECT EMER. |
| Admission Location | CLINIC REFERRAL |
| Discharge Location | HOME |
| Insurance | Other |
| Language | ENGLISH |
| Marital Status | MARRIED |
| Race/Ethnicity | WHITE |
| ED Registration | N/A |
| ED Departure | N/A |
| In-Hospital Mortality | No |
| Date of Death (overall) | 2116-03-12 |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| APR | 144 | RESPIRATORY SIGNS, SYMPTOMS & MINOR DIAGNOSES | 4.0 | 3.0 |
| HCFA | 166 | OTHER RESP SYSTEM O.R. PROCEDURES W MCC | N/A | N/A |

### Primary Diagnosis (seq_num = 1)

- **ICD-9 78609**: Other respiratory abnormalities

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2113-08-26 17:08:00 | N/A | OMED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-9 `78609`: Other respiratory abnormalities
- (seq 2) ICD-9 `486`: Pneumonia, organism unspecified
- (seq 3) ICD-9 `1173`: Aspergillosis
- (seq 4) ICD-9 `20500`: Acute myeloid leukemia, without mention of having achieved remission
- (seq 5) ICD-9 `V4281`: Bone marrow replaced by transplant

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-9 | `78609` | Other respiratory abnormalities |
| 2 | ICD-9 | `486` | Pneumonia, organism unspecified |
| 3 | ICD-9 | `1173` | Aspergillosis |
| 4 | ICD-9 | `20500` | Acute myeloid leukemia, without mention of having achieved remission |
| 5 | ICD-9 | `V4281` | Bone marrow replaced by transplant |
| 6 | ICD-9 | `1629` | Malignant neoplasm of bronchus and lung, unspecified |
| 7 | ICD-9 | `78605` | Shortness of breath |
| 8 | ICD-9 | `V4571` | Acquired absence of breast and nipple |
| 9 | ICD-9 | `V1582` | Personal history of tobacco use |
| 10 | ICD-9 | `V8739` | Contact with and (suspected) exposure to other potentially hazardous substances |
| 11 | ICD-9 | `7904` | Nonspecific elevation of levels of transaminase or lactic acid dehydrogenase [LDH] |
| 12 | ICD-9 | `V161` | Family history of malignant neoplasm of trachea, bronchus, and lung |
| 13 | ICD-9 | `V160` | Family history of malignant neoplasm of gastrointestinal tract |
| 14 | ICD-9 | `V707` | Examination of participant in clinical trial |

## 5. ICU Stays

_No ICU stay recorded for this admission._

## 6. Escalation / Severity Indicators

The following critical conditions or interventions were detected:

- **Pneumonia** (ICD diagnosis)

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2113-08-28 | ICD-9 | `3327` | Closed endoscopic biopsy of lung |
| 2 | 2113-08-28 | ICD-9 | `3324` | Closed [endoscopic] biopsy of bronchus |


## 8. Critical Findings (Charted Events)

_No critical chart events detected._

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2113-08-26 17:07:00 | Admission | Admitted from CLINIC REFERRAL (DIRECT EMER.) |
| 2113-08-29 15:18:00 | Discharge | To HOME |

## 10. Missing / Ambiguous Data

- No ED registration time — admission may not have gone through ED.
- No ICU stay — patient managed on floor/step-down only.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
