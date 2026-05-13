# Encounter Report — HADM 29483621

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 29483621 |
| Subject ID | 10003400 |
| Patient Sex | F |
| Patient Anchor Age (at anchor year) | 72 |
| Anchor Year | 2134 |
| Admission Time | 2136-11-04 20:43:00 |
| Discharge Time | 2136-11-12 17:40:00 |
| Admission Type | EW EMER. |
| Admission Location | EMERGENCY ROOM |
| Discharge Location | SKILLED NURSING FACILITY |
| Insurance | Medicare |
| Language | ENGLISH |
| Marital Status | MARRIED |
| Race/Ethnicity | BLACK/AFRICAN AMERICAN |
| ED Registration | 2136-11-04 16:08:00 |
| ED Departure | 2136-11-04 22:12:00 |
| In-Hospital Mortality | No |
| Date of Death (overall) | 2137-09-02 |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| HCFA | 374 | DIGESTIVE MALIGNANCY W MCC | N/A | N/A |
| APR | 240 | DIGESTIVE MALIGNANCY | 3.0 | 3.0 |

### Primary Diagnosis (seq_num = 1)

- **ICD-9 1548**: Malignant neoplasm of other sites of rectum, rectosigmoid junction, and anus

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2136-11-04 20:43:36 | N/A | MED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-9 `1548`: Malignant neoplasm of other sites of rectum, rectosigmoid junction, and anus
- (seq 2) ICD-9 `28412`: Other drug-induced pancytopenia
- (seq 3) ICD-9 `20300`: Multiple myeloma, without mention of having achieved remission
- (seq 4) ICD-9 `4589`: Hypotension, unspecified
- (seq 5) ICD-9 `42731`: Atrial fibrillation

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-9 | `1548` | Malignant neoplasm of other sites of rectum, rectosigmoid junction, and anus |
| 2 | ICD-9 | `28412` | Other drug-induced pancytopenia |
| 3 | ICD-9 | `20300` | Multiple myeloma, without mention of having achieved remission |
| 4 | ICD-9 | `4589` | Hypotension, unspecified |
| 5 | ICD-9 | `42731` | Atrial fibrillation |
| 6 | ICD-9 | `5853` | Chronic kidney disease, Stage III (moderate) |
| 7 | ICD-9 | `2851` | Acute posthemorrhagic anemia |
| 8 | ICD-9 | `V5861` | Long-term (current) use of anticoagulants |
| 9 | ICD-9 | `27800` | Obesity, unspecified |
| 10 | ICD-9 | `40390` | Hypertensive chronic kidney disease, unspecified, with chronic kidney disease stage I through stage IV, or unspecified |
| 11 | ICD-9 | `7919` | Other nonspecific findings on examination of urine |
| 12 | ICD-9 | `71596` | Osteoarthrosis, unspecified whether generalized or localized, lower leg |
| 13 | ICD-9 | `56210` | Diverticulosis of colon (without mention of hemorrhage) |
| 14 | ICD-9 | `V8532` | Body Mass Index 32.0-32.9, adult |
| 15 | ICD-9 | `56400` | Constipation, unspecified |
| 16 | ICD-9 | `E9478` | Other drugs and medicinal substances causing adverse effects in therapeutic use |
| 17 | ICD-9 | `E8490` | Home accidents |

## 5. ICU Stays

_No ICU stay recorded for this admission._

## 6. Escalation / Severity Indicators

_No escalation indicators detected from ICD codes or ICU procedure events._

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2136-11-07 | ICD-9 | `4923` | Biopsy of anus |
| 2 | 2136-11-11 | ICD-9 | `4523` | Colonoscopy |


## 8. Critical Findings (Charted Events)

_No critical chart events detected._

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2136-11-04 16:08:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2136-11-04 16:08:00 | Transfer | → Emergency Department (ED) |
| 2136-11-04 20:43:00 | Admission | Admitted from EMERGENCY ROOM (EW EMER.) |
| 2136-11-04 22:12:00 | ED Departure | Left Emergency Dept. |
| 2136-11-10 21:15:15 | Transfer | → Medicine (transfer) |
| 2136-11-12 17:40:00 | Discharge | To SKILLED NURSING FACILITY |

## 10. Missing / Ambiguous Data

- No ICU stay — patient managed on floor/step-down only.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
