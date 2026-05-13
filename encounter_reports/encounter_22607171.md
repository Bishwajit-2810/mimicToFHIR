# Encounter Report — HADM 22607171

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 22607171 |
| Subject ID | 10015860 |
| Patient Sex | M |
| Patient Anchor Age (at anchor year) | 53 |
| Anchor Year | 2186 |
| Admission Time | 2190-05-15 08:16:00 |
| Discharge Time | 2190-05-16 15:44:00 |
| Admission Type | EU OBSERVATION |
| Admission Location | EMERGENCY ROOM |
| Discharge Location | N/A |
| Insurance | Other |
| Language | ENGLISH |
| Marital Status | SINGLE |
| Race/Ethnicity | WHITE |
| ED Registration | 2190-05-14 17:11:00 |
| ED Departure | 2190-05-15 10:00:00 |
| In-Hospital Mortality | No |
| Date of Death (overall) | N/A |

## 2. Hospital Visit Reason

### Primary Diagnosis (seq_num = 1)

- **ICD-10 E1165**: Type 2 diabetes mellitus with hyperglycemia

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2190-05-15 08:17:29 | N/A | MED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-10 `E1165`: Type 2 diabetes mellitus with hyperglycemia
- (seq 2) ICD-10 `E1121`: Type 2 diabetes mellitus with diabetic nephropathy
- (seq 3) ICD-10 `E11621`: Type 2 diabetes mellitus with foot ulcer
- (seq 4) ICD-10 `L97519`: Non-pressure chronic ulcer of other part of right foot with unspecified severity
- (seq 5) ICD-10 `E1140`: Type 2 diabetes mellitus with diabetic neuropathy, unspecified

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-10 | `E1165` | Type 2 diabetes mellitus with hyperglycemia |
| 2 | ICD-10 | `E1121` | Type 2 diabetes mellitus with diabetic nephropathy |
| 3 | ICD-10 | `E11621` | Type 2 diabetes mellitus with foot ulcer |
| 4 | ICD-10 | `L97519` | Non-pressure chronic ulcer of other part of right foot with unspecified severity |
| 5 | ICD-10 | `E1140` | Type 2 diabetes mellitus with diabetic neuropathy, unspecified |
| 6 | ICD-10 | `Z794` | Long term (current) use of insulin |
| 7 | ICD-10 | `N179` | Acute kidney failure, unspecified |
| 8 | ICD-10 | `I129` | Hypertensive chronic kidney disease with stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease |
| 9 | ICD-10 | `N183` | Chronic kidney disease, stage 3 (moderate) |
| 10 | ICD-10 | `E780` | Pure hypercholesterolemia |
| 11 | ICD-10 | `Z87891` | Personal history of nicotine dependence |

## 5. ICU Stays

_No ICU stay recorded for this admission._

## 6. Escalation / Severity Indicators

The following critical conditions or interventions were detected:

- **Acute Kidney Injury** (ICD diagnosis)

## 7. Procedures and Interventions

_No ICD-coded procedures recorded._


## 8. Critical Findings (Charted Events)

_No critical chart events detected._

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2190-05-14 17:11:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2190-05-14 17:11:00 | Transfer | → Emergency Department (ED) |
| 2190-05-15 08:16:00 | Admission | Admitted from EMERGENCY ROOM (EU OBSERVATION) |
| 2190-05-15 10:00:00 | ED Departure | Left Emergency Dept. |
| 2190-05-16 15:44:00 | Discharge | To N/A |

## 10. Missing / Ambiguous Data

- Discharge location not recorded.
- No procedure ICD codes — procedures may not have been coded or were minor.
- No ICU stay — patient managed on floor/step-down only.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
