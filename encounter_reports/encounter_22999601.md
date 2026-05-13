# Encounter Report — HADM 22999601

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 22999601 |
| Subject ID | 10039708 |
| Patient Sex | F |
| Patient Anchor Age (at anchor year) | 46 |
| Anchor Year | 2138 |
| Admission Time | 2142-05-15 17:14:00 |
| Discharge Time | 2142-05-15 18:21:00 |
| Admission Type | DIRECT OBSERVATION |
| Admission Location | PHYSICIAN REFERRAL |
| Discharge Location | N/A |
| Insurance | Other |
| Language | ENGLISH |
| Marital Status | SINGLE |
| Race/Ethnicity | BLACK/AFRICAN AMERICAN |
| ED Registration | 2142-05-15 10:47:00 |
| ED Departure | 2142-05-15 18:21:00 |
| In-Hospital Mortality | No |
| Date of Death (overall) | N/A |

## 2. Hospital Visit Reason

### Primary Diagnosis (seq_num = 1)

- **ICD-10 T8242XA**: Displacement of vascular dialysis catheter, initial encounter

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2142-05-15 17:15:02 | N/A | MED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-10 `T8242XA`: Displacement of vascular dialysis catheter, initial encounter
- (seq 2) ICD-10 `I120`: Hypertensive chronic kidney disease with stage 5 chronic kidney disease or end stage renal disease
- (seq 3) ICD-10 `N186`: End stage renal disease
- (seq 4) ICD-10 `Z992`: Dependence on renal dialysis
- (seq 5) ICD-10 `F17200`: Nicotine dependence, unspecified, uncomplicated

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-10 | `T8242XA` | Displacement of vascular dialysis catheter, initial encounter |
| 2 | ICD-10 | `I120` | Hypertensive chronic kidney disease with stage 5 chronic kidney disease or end stage renal disease |
| 3 | ICD-10 | `N186` | End stage renal disease |
| 4 | ICD-10 | `Z992` | Dependence on renal dialysis |
| 5 | ICD-10 | `F17200` | Nicotine dependence, unspecified, uncomplicated |
| 6 | ICD-10 | `Y828` | Other medical devices associated with adverse incidents |
| 7 | ICD-10 | `Y929` | Unspecified place or not applicable |
| 8 | ICD-10 | `K7460` | Unspecified cirrhosis of liver |

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
| 2142-05-15 10:47:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2142-05-15 10:47:00 | Transfer | → Emergency Department (ED) |
| 2142-05-15 17:14:00 | Admission | Admitted from PHYSICIAN REFERRAL (DIRECT OBSERVATION) |
| 2142-05-15 18:21:00 | Discharge | To N/A |
| 2142-05-15 18:21:00 | ED Departure | Left Emergency Dept. |

## 10. Missing / Ambiguous Data

- Discharge location not recorded.
- No procedure ICD codes — procedures may not have been coded or were minor.
- No ICU stay — patient managed on floor/step-down only.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
