# Encounter Report — HADM 26369609

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 26369609 |
| Subject ID | 10012853 |
| Patient Sex | F |
| Patient Anchor Age (at anchor year) | 91 |
| Anchor Year | 2175 |
| Admission Time | 2175-04-05 15:36:00 |
| Discharge Time | 2175-04-10 16:55:00 |
| Admission Type | EW EMER. |
| Admission Location | EMERGENCY ROOM |
| Discharge Location | HOME |
| Insurance | Other |
| Language | ENGLISH |
| Marital Status | WIDOWED |
| Race/Ethnicity | BLACK/AFRICAN AMERICAN |
| ED Registration | 2175-04-05 06:22:00 |
| ED Departure | 2175-04-05 17:10:00 |
| In-Hospital Mortality | No |
| Date of Death (overall) | N/A |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| APR | 194 | HEART FAILURE | 1.0 | 2.0 |
| HCFA | 315 | OTHER CIRCULATORY SYSTEM DIAGNOSES W CC | N/A | N/A |

### Primary Diagnosis (seq_num = 1)

- **ICD-9 4150**: Acute cor pulmonale

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2175-04-05 15:36:27 | N/A | CMED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-9 `4150`: Acute cor pulmonale
- (seq 2) ICD-9 `5990`: Urinary tract infection, site not specified
- (seq 3) ICD-9 `5119`: Unspecified pleural effusion
- (seq 4) ICD-9 `4280`: Congestive heart failure, unspecified
- (seq 5) ICD-9 `0413`: Friedländer's bacillus infection in conditions classified elsewhere and of unspecified site

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-9 | `4150` | Acute cor pulmonale |
| 2 | ICD-9 | `5990` | Urinary tract infection, site not specified |
| 3 | ICD-9 | `5119` | Unspecified pleural effusion |
| 4 | ICD-9 | `4280` | Congestive heart failure, unspecified |
| 5 | ICD-9 | `0413` | Friedländer's bacillus infection in conditions classified elsewhere and of unspecified site |
| 6 | ICD-9 | `27669` | Other fluid overload |
| 7 | ICD-9 | `5853` | Chronic kidney disease, Stage III (moderate) |
| 8 | ICD-9 | `25000` | Diabetes mellitus without mention of complication, type II or unspecified type, not stated as uncontrolled |
| 9 | ICD-9 | `42731` | Atrial fibrillation |
| 10 | ICD-9 | `7842` | Swelling, mass, or lump in head and neck |
| 11 | ICD-9 | `2411` | Nontoxic multinodular goiter |
| 12 | ICD-9 | `2724` | Other and unspecified hyperlipidemia |
| 13 | ICD-9 | `7804` | Dizziness and giddiness |
| 14 | ICD-9 | `40390` | Hypertensive chronic kidney disease, unspecified, with chronic kidney disease stage I through stage IV, or unspecified |
| 15 | ICD-9 | `V5861` | Long-term (current) use of anticoagulants |
| 16 | ICD-9 | `4439` | Peripheral vascular disease, unspecified |

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
| 2175-04-05 06:22:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2175-04-05 06:22:00 | Transfer | → Emergency Department (ED) |
| 2175-04-05 15:36:00 | Admission | Admitted from EMERGENCY ROOM (EW EMER.) |
| 2175-04-05 17:10:00 | ED Departure | Left Emergency Dept. |
| 2175-04-10 16:55:00 | Discharge | To HOME |

## 10. Missing / Ambiguous Data

- No procedure ICD codes — procedures may not have been coded or were minor.
- No ICU stay — patient managed on floor/step-down only.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
