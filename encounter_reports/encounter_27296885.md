# Encounter Report — HADM 27296885

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 27296885 |
| Subject ID | 10003400 |
| Patient Sex | F |
| Patient Anchor Age (at anchor year) | 72 |
| Anchor Year | 2134 |
| Admission Time | 2136-12-31 21:40:00 |
| Discharge Time | 2137-01-03 17:05:00 |
| Admission Type | EW EMER. |
| Admission Location | EMERGENCY ROOM |
| Discharge Location | SKILLED NURSING FACILITY |
| Insurance | Medicare |
| Language | ENGLISH |
| Marital Status | MARRIED |
| Race/Ethnicity | BLACK/AFRICAN AMERICAN |
| ED Registration | 2136-12-31 13:41:00 |
| ED Departure | 2137-01-01 00:35:00 |
| In-Hospital Mortality | No |
| Date of Death (overall) | 2137-09-02 |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| HCFA | 71 | NONSPECIFIC CEREBROVASCULAR DISORDERS W CC | N/A | N/A |
| APR | 52 | ALTERATION IN CONSCIOUSNESS | 3.0 | 2.0 |

### Primary Diagnosis (seq_num = 1)

- **ICD-9 34839**: Other encephalopathy

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2136-12-31 21:41:25 | N/A | MED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-9 `34839`: Other encephalopathy
- (seq 2) ICD-9 `20300`: Multiple myeloma, without mention of having achieved remission
- (seq 3) ICD-9 `1543`: Malignant neoplasm of anus, unspecified site
- (seq 4) ICD-9 `42731`: Atrial fibrillation
- (seq 5) ICD-9 `27800`: Obesity, unspecified

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-9 | `34839` | Other encephalopathy |
| 2 | ICD-9 | `20300` | Multiple myeloma, without mention of having achieved remission |
| 3 | ICD-9 | `1543` | Malignant neoplasm of anus, unspecified site |
| 4 | ICD-9 | `42731` | Atrial fibrillation |
| 5 | ICD-9 | `27800` | Obesity, unspecified |
| 6 | ICD-9 | `V8531` | Body Mass Index 31.0-31.9, adult |
| 7 | ICD-9 | `71536` | Osteoarthrosis, localized, not specified whether primary or secondary, lower leg |
| 8 | ICD-9 | `40390` | Hypertensive chronic kidney disease, unspecified, with chronic kidney disease stage I through stage IV, or unspecified |
| 9 | ICD-9 | `5853` | Chronic kidney disease, Stage III (moderate) |
| 10 | ICD-9 | `V5861` | Long-term (current) use of anticoagulants |

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
| 2136-12-31 13:41:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2136-12-31 13:41:00 | Transfer | → Emergency Department (ED) |
| 2136-12-31 21:40:00 | Admission | Admitted from EMERGENCY ROOM (EW EMER.) |
| 2137-01-01 00:35:00 | ED Departure | Left Emergency Dept. |
| 2137-01-01 19:04:37 | Transfer | → Medicine (transfer) |
| 2137-01-03 17:05:00 | Discharge | To SKILLED NURSING FACILITY |

## 10. Missing / Ambiguous Data

- No procedure ICD codes — procedures may not have been coded or were minor.
- No ICU stay — patient managed on floor/step-down only.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
