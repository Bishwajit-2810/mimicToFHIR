# Encounter Report — HADM 26793610

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 26793610 |
| Subject ID | 10039708 |
| Patient Sex | F |
| Patient Anchor Age (at anchor year) | 46 |
| Anchor Year | 2138 |
| Admission Time | 2140-09-25 04:17:00 |
| Discharge Time | 2140-09-26 17:40:00 |
| Admission Type | OBSERVATION ADMIT |
| Admission Location | EMERGENCY ROOM |
| Discharge Location | HOME |
| Insurance | Other |
| Language | ENGLISH |
| Marital Status | SINGLE |
| Race/Ethnicity | BLACK/AFRICAN AMERICAN |
| ED Registration | 2140-09-24 21:17:00 |
| ED Departure | 2140-09-25 05:57:00 |
| In-Hospital Mortality | No |
| Date of Death (overall) | N/A |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| HCFA | 683 | RENAL FAILURE W CC | N/A | N/A |

### Primary Diagnosis (seq_num = 1)

- **ICD-10 N179**: Acute kidney failure, unspecified

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2140-09-25 04:18:09 | N/A | MED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-10 `N179`: Acute kidney failure, unspecified
- (seq 2) ICD-10 `E872`: Acidosis
- (seq 3) ICD-10 `I959`: Hypotension, unspecified
- (seq 4) ICD-10 `N183`: Chronic kidney disease, stage 3 (moderate)
- (seq 5) ICD-10 `I129`: Hypertensive chronic kidney disease with stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-10 | `N179` | Acute kidney failure, unspecified |
| 2 | ICD-10 | `E872` | Acidosis |
| 3 | ICD-10 | `I959` | Hypotension, unspecified |
| 4 | ICD-10 | `N183` | Chronic kidney disease, stage 3 (moderate) |
| 5 | ICD-10 | `I129` | Hypertensive chronic kidney disease with stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease |
| 6 | ICD-10 | `F1020` | Alcohol dependence, uncomplicated |
| 7 | ICD-10 | `E039` | Hypothyroidism, unspecified |
| 8 | ICD-10 | `D539` | Nutritional anemia, unspecified |
| 9 | ICD-10 | `F17210` | Nicotine dependence, cigarettes, uncomplicated |
| 10 | ICD-10 | `R740` | Nonspecific elevation of levels of transaminase and lactic acid dehydrogenase [LDH] |

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
| 2140-09-24 21:17:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2140-09-24 21:17:00 | Transfer | → Emergency Department (ED) |
| 2140-09-25 04:17:00 | Admission | Admitted from EMERGENCY ROOM (OBSERVATION ADMIT) |
| 2140-09-25 05:57:00 | ED Departure | Left Emergency Dept. |
| 2140-09-26 17:40:00 | Discharge | To HOME |

## 10. Missing / Ambiguous Data

- No procedure ICD codes — procedures may not have been coded or were minor.
- No ICU stay — patient managed on floor/step-down only.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
