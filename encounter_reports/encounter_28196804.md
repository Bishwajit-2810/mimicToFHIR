# Encounter Report — HADM 28196804

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 28196804 |
| Subject ID | 10015860 |
| Patient Sex | M |
| Patient Anchor Age (at anchor year) | 53 |
| Anchor Year | 2186 |
| Admission Time | 2193-11-23 19:15:00 |
| Discharge Time | 2193-11-27 21:58:00 |
| Admission Type | OBSERVATION ADMIT |
| Admission Location | WALK-IN/SELF REFERRAL |
| Discharge Location | SKILLED NURSING FACILITY |
| Insurance | Other |
| Language | ENGLISH |
| Marital Status | SINGLE |
| Race/Ethnicity | WHITE |
| ED Registration | 2193-11-23 12:38:00 |
| ED Departure | 2193-11-23 20:59:00 |
| In-Hospital Mortality | No |
| Date of Death (overall) | N/A |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| HCFA | 252 | OTHER VASCULAR PROCEDURES W MCC | N/A | N/A |
| APR | 182 | OTHER PERIPHERAL VASCULAR PROCEDURES | 2.0 | 2.0 |

### Primary Diagnosis (seq_num = 1)

- **ICD-10 T82868A**: Thrombosis due to vascular prosthetic devices, implants and grafts, initial encounter

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2193-11-23 19:16:36 | N/A | MED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-10 `T82868A`: Thrombosis due to vascular prosthetic devices, implants and grafts, initial encounter
- (seq 2) ICD-10 `N186`: End stage renal disease
- (seq 3) ICD-10 `I120`: Hypertensive chronic kidney disease with stage 5 chronic kidney disease or end stage renal disease
- (seq 4) ICD-10 `L03114`: Cellulitis of left upper limb
- (seq 5) ICD-10 `E11621`: Type 2 diabetes mellitus with foot ulcer

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-10 | `T82868A` | Thrombosis due to vascular prosthetic devices, implants and grafts, initial encounter |
| 2 | ICD-10 | `N186` | End stage renal disease |
| 3 | ICD-10 | `I120` | Hypertensive chronic kidney disease with stage 5 chronic kidney disease or end stage renal disease |
| 4 | ICD-10 | `L03114` | Cellulitis of left upper limb |
| 5 | ICD-10 | `E11621` | Type 2 diabetes mellitus with foot ulcer |
| 6 | ICD-10 | `L97511` | Non-pressure chronic ulcer of other part of right foot limited to breakdown of skin |
| 7 | ICD-10 | `Y713` | Surgical instruments, materials and cardiovascular devices (including sutures) associated with adverse incidents |
| 8 | ICD-10 | `E1122` | Type 2 diabetes mellitus with diabetic chronic kidney disease |
| 9 | ICD-10 | `L281` | Prurigo nodularis |
| 10 | ICD-10 | `E785` | Hyperlipidemia, unspecified |
| 11 | ICD-10 | `F419` | Anxiety disorder, unspecified |
| 12 | ICD-10 | `K219` | Gastro-esophageal reflux disease without esophagitis |
| 13 | ICD-10 | `Z992` | Dependence on renal dialysis |
| 14 | ICD-10 | `Z794` | Long term (current) use of insulin |
| 15 | ICD-10 | `D631` | Anemia in chronic kidney disease |
| 16 | ICD-10 | `Z89431` | Acquired absence of right foot |
| 17 | ICD-10 | `F1021` | Alcohol dependence, in remission |
| 18 | ICD-10 | `Z87891` | Personal history of nicotine dependence |
| 19 | ICD-10 | `Z95820` | Peripheral vascular angioplasty status with implants and grafts |
| 20 | ICD-10 | `Z85828` | Personal history of other malignant neoplasm of skin |

## 5. ICU Stays

_No ICU stay recorded for this admission._

## 6. Escalation / Severity Indicators

_No escalation indicators detected from ICD codes or ICU procedure events._

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2193-11-27 | ICD-10 | `057A3ZZ` | Dilation of Left Brachial Vein, Percutaneous Approach |
| 2 | 2193-11-27 | ICD-10 | `057F3ZZ` | Dilation of Left Cephalic Vein, Percutaneous Approach |
| 3 | 2193-11-27 | ICD-10 | `B51W1ZZ` | Fluoroscopy of Dialysis Shunt/Fistula using Low Osmolar Contrast |
| 4 | 2193-11-24 | ICD-10 | `5A1D70Z` | Performance of Urinary Filtration, Intermittent, Less than 6 Hours Per Day |


## 8. Critical Findings (Charted Events)

_No critical chart events detected._

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2193-11-23 12:38:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2193-11-23 12:38:00 | Transfer | → Emergency Department (ED) |
| 2193-11-23 19:15:00 | Admission | Admitted from WALK-IN/SELF REFERRAL (OBSERVATION ADMIT) |
| 2193-11-23 20:12:47 | Transfer | → Medicine (transfer) |
| 2193-11-23 20:59:00 | ED Departure | Left Emergency Dept. |
| 2193-11-27 21:58:00 | Discharge | To SKILLED NURSING FACILITY |

## 10. Missing / Ambiguous Data

- No ICU stay — patient managed on floor/step-down only.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
