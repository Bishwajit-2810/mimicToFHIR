# Encounter Report — HADM 22390287

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 22390287 |
| Subject ID | 10003400 |
| Patient Sex | F |
| Patient Anchor Age (at anchor year) | 72 |
| Anchor Year | 2134 |
| Admission Time | 2137-02-07 19:42:00 |
| Discharge Time | 2137-02-18 18:30:00 |
| Admission Type | EW EMER. |
| Admission Location | EMERGENCY ROOM |
| Discharge Location | SKILLED NURSING FACILITY |
| Insurance | Medicare |
| Language | ENGLISH |
| Marital Status | MARRIED |
| Race/Ethnicity | BLACK/AFRICAN AMERICAN |
| ED Registration | 2137-02-07 13:06:00 |
| ED Departure | 2137-02-07 21:44:00 |
| In-Hospital Mortality | No |
| Date of Death (overall) | 2137-09-02 |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| HCFA | 375 | DIGESTIVE MALIGNANCY W CC | N/A | N/A |
| APR | 240 | DIGESTIVE MALIGNANCY | 3.0 | 2.0 |

### Primary Diagnosis (seq_num = 1)

- **ICD-9 1541**: Malignant neoplasm of rectum

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2137-02-07 19:42:51 | N/A | OMED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-9 `1541`: Malignant neoplasm of rectum
- (seq 2) ICD-9 `5693`: Hemorrhage of rectum and anus
- (seq 3) ICD-9 `20300`: Multiple myeloma, without mention of having achieved remission
- (seq 4) ICD-9 `2753`: Disorders of phosphorus metabolism
- (seq 5) ICD-9 `42731`: Atrial fibrillation

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-9 | `1541` | Malignant neoplasm of rectum |
| 2 | ICD-9 | `5693` | Hemorrhage of rectum and anus |
| 3 | ICD-9 | `20300` | Multiple myeloma, without mention of having achieved remission |
| 4 | ICD-9 | `2753` | Disorders of phosphorus metabolism |
| 5 | ICD-9 | `42731` | Atrial fibrillation |
| 6 | ICD-9 | `5921` | Calculus of ureter |
| 7 | ICD-9 | `E9342` | Anticoagulants causing adverse effects in therapeutic use |
| 8 | ICD-9 | `3383` | Neoplasm related pain (acute) (chronic) |
| 9 | ICD-9 | `56942` | Anal or rectal pain |
| 10 | ICD-9 | `2800` | Iron deficiency anemia secondary to blood loss (chronic) |
| 11 | ICD-9 | `V8741` | Personal history of antineoplastic chemotherapy |
| 12 | ICD-9 | `40390` | Hypertensive chronic kidney disease, unspecified, with chronic kidney disease stage I through stage IV, or unspecified |
| 13 | ICD-9 | `5853` | Chronic kidney disease, Stage III (moderate) |
| 14 | ICD-9 | `V1351` | Personal history of pathologic fracture |
| 15 | ICD-9 | `V446` | Other artificial opening of urinary tract status |

## 5. ICU Stays

_No ICU stay recorded for this admission._

## 6. Escalation / Severity Indicators

_No escalation indicators detected from ICD codes or ICU procedure events._

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2137-02-11 | ICD-9 | `9229` | Other radiotherapeutic procedure |


## 8. Critical Findings (Charted Events)

_No critical chart events detected._

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2137-02-07 13:06:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2137-02-07 13:06:00 | Transfer | → Emergency Department (ED) |
| 2137-02-07 19:42:00 | Admission | Admitted from EMERGENCY ROOM (EW EMER.) |
| 2137-02-07 21:44:00 | ED Departure | Left Emergency Dept. |
| 2137-02-09 21:41:52 | Transfer | → Hematology/Oncology (transfer) |
| 2137-02-10 22:03:22 | Transfer | → Hematology/Oncology (transfer) |
| 2137-02-18 18:30:00 | Discharge | To SKILLED NURSING FACILITY |

## 10. Missing / Ambiguous Data

- No ICU stay — patient managed on floor/step-down only.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
