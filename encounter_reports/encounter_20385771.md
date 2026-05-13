# Encounter Report — HADM 20385771

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 20385771 |
| Subject ID | 10035631 |
| Patient Sex | M |
| Patient Anchor Age (at anchor year) | 63 |
| Anchor Year | 2112 |
| Admission Time | 2112-12-04 00:00:00 |
| Discharge Time | 2112-12-27 16:24:00 |
| Admission Type | ELECTIVE |
| Admission Location | PHYSICIAN REFERRAL |
| Discharge Location | HOME HEALTH CARE |
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
| HCFA | 14 | ALLOGENEIC BONE MARROW TRANSPLANT | N/A | N/A |

### Primary Diagnosis (seq_num = 1)

- **ICD-9 20500**: Acute myeloid leukemia, without mention of having achieved remission

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2112-12-04 10:34:31 | N/A | OMED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-9 `20500`: Acute myeloid leukemia, without mention of having achieved remission
- (seq 2) ICD-9 `4846`: Pneumonia in aspergillosis
- (seq 3) ICD-9 `1173`: Aspergillosis
- (seq 4) ICD-9 `28411`: Antineoplastic chemotherapy induced pancytopenia
- (seq 5) ICD-9 `99931`: Other and unspecified infection due to central venous catheter

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-9 | `20500` | Acute myeloid leukemia, without mention of having achieved remission |
| 2 | ICD-9 | `4846` | Pneumonia in aspergillosis |
| 3 | ICD-9 | `1173` | Aspergillosis |
| 4 | ICD-9 | `28411` | Antineoplastic chemotherapy induced pancytopenia |
| 5 | ICD-9 | `99931` | Other and unspecified infection due to central venous catheter |
| 6 | ICD-9 | `2768` | Hypopotassemia |
| 7 | ICD-9 | `E9331` | Antineoplastic and immunosuppressive drugs causing adverse effects in therapeutic use |
| 8 | ICD-9 | `78791` | Diarrhea |
| 9 | ICD-9 | `2752` | Disorders of magnesium metabolism |
| 10 | ICD-9 | `V707` | Examination of participant in clinical trial |
| 11 | ICD-9 | `45182` | Phlebitis and thrombophlebitis of superficial veins of upper extremities |
| 12 | ICD-9 | `7830` | Anorexia |
| 13 | ICD-9 | `E8798` | Other specified procedures as the cause of abnormal reaction of patient, or of later complication, without mention of misadventure at time of procedure |
| 14 | ICD-9 | `V1582` | Personal history of tobacco use |
| 15 | ICD-9 | `4019` | Unspecified essential hypertension |
| 16 | ICD-9 | `78702` | Nausea alone |
| 17 | ICD-9 | `E8497` | Accidents occurring in residential institution |
| 18 | ICD-9 | `V141` | Personal history of allergy to other antibiotic agent |

## 5. ICU Stays

_No ICU stay recorded for this admission._

## 6. Escalation / Severity Indicators

The following critical conditions or interventions were detected:

- **Pneumonia** (ICD diagnosis)

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2112-12-11 | ICD-9 | `4105` | Allogeneic hematopoietic stem cell transpant without purging |
| 2 | 2112-12-11 | ICD-9 | `0091` | Transplant from live related donor |
| 3 | 2112-12-04 | ICD-9 | `3897` | Central venous catheter placement with guidance |


## 8. Critical Findings (Charted Events)

_No critical chart events detected._

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2112-12-04 00:00:00 | Admission | Admitted from PHYSICIAN REFERRAL (ELECTIVE) |
| 2112-12-27 16:24:00 | Discharge | To HOME HEALTH CARE |

## 10. Missing / Ambiguous Data

- No ED registration time — admission may not have gone through ED.
- No ICU stay — patient managed on floor/step-down only.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
