# Encounter Report — HADM 22413744

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 22413744 |
| Subject ID | 10015860 |
| Patient Sex | M |
| Patient Anchor Age (at anchor year) | 53 |
| Anchor Year | 2186 |
| Admission Time | 2191-01-15 01:55:00 |
| Discharge Time | 2191-01-30 17:09:00 |
| Admission Type | OBSERVATION ADMIT |
| Admission Location | EMERGENCY ROOM |
| Discharge Location | SKILLED NURSING FACILITY |
| Insurance | Other |
| Language | ENGLISH |
| Marital Status | SINGLE |
| Race/Ethnicity | WHITE |
| ED Registration | 2191-01-14 21:18:00 |
| ED Departure | 2191-01-15 03:20:00 |
| In-Hospital Mortality | No |
| Date of Death (overall) | N/A |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| HCFA | 872 | SEPTICEMIA OR SEVERE SEPSIS W/O MV >96 HOURS W/O MCC | N/A | N/A |
| APR | 720 | SEPTICEMIA & DISSEMINATED INFECTIONS | 3.0 | 3.0 |

### Primary Diagnosis (seq_num = 1)

- **ICD-10 A408**: Other streptococcal sepsis

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2191-01-15 01:57:34 | N/A | MED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-10 `A408`: Other streptococcal sepsis
- (seq 2) ICD-10 `R6520`: Severe sepsis without septic shock
- (seq 3) ICD-10 `E872`: Acidosis
- (seq 4) ICD-10 `N179`: Acute kidney failure, unspecified
- (seq 5) ICD-10 `N183`: Chronic kidney disease, stage 3 (moderate)

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-10 | `A408` | Other streptococcal sepsis |
| 2 | ICD-10 | `R6520` | Severe sepsis without septic shock |
| 3 | ICD-10 | `E872` | Acidosis |
| 4 | ICD-10 | `N179` | Acute kidney failure, unspecified |
| 5 | ICD-10 | `N183` | Chronic kidney disease, stage 3 (moderate) |
| 6 | ICD-10 | `E1122` | Type 2 diabetes mellitus with diabetic chronic kidney disease |
| 7 | ICD-10 | `B356` | Tinea cruris |
| 8 | ICD-10 | `E871` | Hypo-osmolality and hyponatremia |
| 9 | ICD-10 | `E11621` | Type 2 diabetes mellitus with foot ulcer |
| 10 | ICD-10 | `L97519` | Non-pressure chronic ulcer of other part of right foot with unspecified severity |
| 11 | ICD-10 | `E1165` | Type 2 diabetes mellitus with hyperglycemia |
| 12 | ICD-10 | `Z794` | Long term (current) use of insulin |
| 13 | ICD-10 | `I129` | Hypertensive chronic kidney disease with stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease |
| 14 | ICD-10 | `Z87891` | Personal history of nicotine dependence |
| 15 | ICD-10 | `E1140` | Type 2 diabetes mellitus with diabetic neuropathy, unspecified |
| 16 | ICD-10 | `E875` | Hyperkalemia |
| 17 | ICD-10 | `E8339` | Other disorders of phosphorus metabolism |
| 18 | ICD-10 | `D649` | Anemia, unspecified |
| 19 | ICD-10 | `R5084` | Febrile nonhemolytic transfusion reaction |
| 20 | ICD-10 | `R197` | Diarrhea, unspecified |

## 5. ICU Stays

_No ICU stay recorded for this admission._

## 6. Escalation / Severity Indicators

The following critical conditions or interventions were detected:

- **Acute Kidney Injury** (ICD diagnosis)
- **Sepsis** (ICD diagnosis)

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2191-01-22 | ICD-10 | `0S993ZX` | Drainage of Right Hip Joint, Percutaneous Approach, Diagnostic |


## 8. Critical Findings (Charted Events)

_No critical chart events detected._

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2191-01-14 21:18:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2191-01-14 21:18:00 | Transfer | → Emergency Department (ED) |
| 2191-01-15 01:55:00 | Admission | Admitted from EMERGENCY ROOM (OBSERVATION ADMIT) |
| 2191-01-15 03:20:00 | ED Departure | Left Emergency Dept. |
| 2191-01-30 17:09:00 | Discharge | To SKILLED NURSING FACILITY |

## 10. Missing / Ambiguous Data

- No ICU stay — patient managed on floor/step-down only.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
