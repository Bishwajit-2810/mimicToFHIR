# Encounter Report — HADM 26352758

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 26352758 |
| Subject ID | 10015860 |
| Patient Sex | M |
| Patient Anchor Age (at anchor year) | 53 |
| Anchor Year | 2186 |
| Admission Time | 2192-09-24 09:19:00 |
| Discharge Time | 2192-09-28 19:52:00 |
| Admission Type | URGENT |
| Admission Location | TRANSFER FROM SKILLED NURSING FACILITY |
| Discharge Location | SKILLED NURSING FACILITY |
| Insurance | Other |
| Language | ENGLISH |
| Marital Status | SINGLE |
| Race/Ethnicity | WHITE |
| ED Registration | 2192-09-23 22:43:00 |
| ED Departure | 2192-09-24 09:38:00 |
| In-Hospital Mortality | No |
| Date of Death (overall) | N/A |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| APR | 308 | HIP & FEMUR FRACTURE REPAIR | 2.0 | 2.0 |
| HCFA | 480 | HIP & FEMUR PROCEDURES EXCEPT MAJOR JOINT W MCC | N/A | N/A |

### Primary Diagnosis (seq_num = 1)

- **ICD-10 S72145A**: Nondisplaced intertrochanteric fracture of left femur, initial encounter for closed fracture

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2192-09-24 09:20:21 | N/A | ORTHO |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-10 `S72145A`: Nondisplaced intertrochanteric fracture of left femur, initial encounter for closed fracture
- (seq 2) ICD-10 `W010XXA`: Fall on same level from slipping, tripping and stumbling without subsequent striking against object, initial encounter
- (seq 3) ICD-10 `Y92121`: Bathroom in nursing home as the place of occurrence of the external cause
- (seq 4) ICD-10 `I120`: Hypertensive chronic kidney disease with stage 5 chronic kidney disease or end stage renal disease
- (seq 5) ICD-10 `N186`: End stage renal disease

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-10 | `S72145A` | Nondisplaced intertrochanteric fracture of left femur, initial encounter for closed fracture |
| 2 | ICD-10 | `W010XXA` | Fall on same level from slipping, tripping and stumbling without subsequent striking against object, initial encounter |
| 3 | ICD-10 | `Y92121` | Bathroom in nursing home as the place of occurrence of the external cause |
| 4 | ICD-10 | `I120` | Hypertensive chronic kidney disease with stage 5 chronic kidney disease or end stage renal disease |
| 5 | ICD-10 | `N186` | End stage renal disease |
| 6 | ICD-10 | `E1122` | Type 2 diabetes mellitus with diabetic chronic kidney disease |
| 7 | ICD-10 | `E1142` | Type 2 diabetes mellitus with diabetic polyneuropathy |
| 8 | ICD-10 | `D62` | Acute posthemorrhagic anemia |
| 9 | ICD-10 | `E1151` | Type 2 diabetes mellitus with diabetic peripheral angiopathy without gangrene |
| 10 | ICD-10 | `D631` | Anemia in chronic kidney disease |
| 11 | ICD-10 | `E7800` | Pure hypercholesterolemia, unspecified |
| 12 | ICD-10 | `Z992` | Dependence on renal dialysis |
| 13 | ICD-10 | `Z794` | Long term (current) use of insulin |
| 14 | ICD-10 | `Z89421` | Acquired absence of other right toe(s) |
| 15 | ICD-10 | `Z87891` | Personal history of nicotine dependence |

## 5. ICU Stays

_No ICU stay recorded for this admission._

## 6. Escalation / Severity Indicators

_No escalation indicators detected from ICD codes or ICU procedure events._

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2192-09-24 | ICD-10 | `0QH736Z` | Insertion of Intramedullary Internal Fixation Device into Left Upper Femur, Percutaneous Approach |
| 2 | 2192-09-25 | ICD-10 | `5A1D70Z` | Performance of Urinary Filtration, Intermittent, Less than 6 Hours Per Day |


## 8. Critical Findings (Charted Events)

_No critical chart events detected._

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2192-09-23 22:43:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2192-09-23 22:43:00 | Transfer | → Emergency Department (ED) |
| 2192-09-24 09:19:00 | Admission | Admitted from TRANSFER FROM SKILLED NURSING FACILITY (URGENT) |
| 2192-09-24 09:38:00 | ED Departure | Left Emergency Dept. |
| 2192-09-24 16:53:36 | Transfer | → Surgery/Trauma (transfer) |
| 2192-09-27 21:11:59 | Transfer | → Surgery/Trauma (transfer) |
| 2192-09-28 19:52:00 | Discharge | To SKILLED NURSING FACILITY |

## 10. Missing / Ambiguous Data

- No ICU stay — patient managed on floor/step-down only.

## 11. Manual Review Recommendation

**This encounter is flagged for manual review:**

- Urgent/Emergency admission but no clear escalation indicator found.
