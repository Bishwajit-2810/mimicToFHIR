# Encounter Report — HADM 27259207

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 27259207 |
| Subject ID | 10040025 |
| Patient Sex | F |
| Patient Anchor Age (at anchor year) | 64 |
| Anchor Year | 2143 |
| Admission Time | 2147-12-04 20:48:00 |
| Discharge Time | 2147-12-18 16:43:00 |
| Admission Type | OBSERVATION ADMIT |
| Admission Location | EMERGENCY ROOM |
| Discharge Location | SKILLED NURSING FACILITY |
| Insurance | Other |
| Language | ENGLISH |
| Marital Status | DIVORCED |
| Race/Ethnicity | WHITE |
| ED Registration | 2147-12-04 13:11:00 |
| ED Departure | 2147-12-05 02:28:00 |
| In-Hospital Mortality | No |
| Date of Death (overall) | 2148-02-07 |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| APR | 951 | MODERATELY EXTENSIVE PROCEDURE UNRELATED TO PRINCIPAL DIAGNOSIS | 3.0 | 2.0 |
| HCFA | 982 | EXTENSIVE O.R. PROCEDURE UNRELATED TO PRINCIPAL DIAGNOSIS W CC | N/A | N/A |

### Primary Diagnosis (seq_num = 1)

- **ICD-10 E11621**: Type 2 diabetes mellitus with foot ulcer

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2147-12-04 20:49:51 | N/A | VSURG |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-10 `E11621`: Type 2 diabetes mellitus with foot ulcer
- (seq 2) ICD-10 `I70262`: Atherosclerosis of native arteries of extremities with gangrene, left leg
- (seq 3) ICD-10 `L97523`: Non-pressure chronic ulcer of other part of left foot with necrosis of muscle
- (seq 4) ICD-10 `L97429`: Non-pressure chronic ulcer of left heel and midfoot with unspecified severity
- (seq 5) ICD-10 `L97419`: Non-pressure chronic ulcer of right heel and midfoot with unspecified severity

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-10 | `E11621` | Type 2 diabetes mellitus with foot ulcer |
| 2 | ICD-10 | `I70262` | Atherosclerosis of native arteries of extremities with gangrene, left leg |
| 3 | ICD-10 | `L97523` | Non-pressure chronic ulcer of other part of left foot with necrosis of muscle |
| 4 | ICD-10 | `L97429` | Non-pressure chronic ulcer of left heel and midfoot with unspecified severity |
| 5 | ICD-10 | `L97419` | Non-pressure chronic ulcer of right heel and midfoot with unspecified severity |
| 6 | ICD-10 | `E11622` | Type 2 diabetes mellitus with other skin ulcer |
| 7 | ICD-10 | `L97229` | Non-pressure chronic ulcer of left calf with unspecified severity |
| 8 | ICD-10 | `E1152` | Type 2 diabetes mellitus with diabetic peripheral angiopathy with gangrene |
| 9 | ICD-10 | `E11628` | Type 2 diabetes mellitus with other skin complications |
| 10 | ICD-10 | `L03116` | Cellulitis of left lower limb |
| 11 | ICD-10 | `B965` | Pseudomonas (aeruginosa) (mallei) (pseudomallei) as the cause of diseases classified elsewhere |
| 12 | ICD-10 | `I130` | Hypertensive heart and chronic kidney disease with heart failure and stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease |
| 13 | ICD-10 | `I5022` | Chronic systolic (congestive) heart failure |
| 14 | ICD-10 | `E1122` | Type 2 diabetes mellitus with diabetic chronic kidney disease |
| 15 | ICD-10 | `I4891` | Unspecified atrial fibrillation |
| 16 | ICD-10 | `N183` | Chronic kidney disease, stage 3 (moderate) |
| 17 | ICD-10 | `E785` | Hyperlipidemia, unspecified |
| 18 | ICD-10 | `E039` | Hypothyroidism, unspecified |
| 19 | ICD-10 | `I2510` | Atherosclerotic heart disease of native coronary artery without angina pectoris |
| 20 | ICD-10 | `E669` | Obesity, unspecified |
| 21 | ICD-10 | `Z6832` | Body mass index (BMI) 32.0-32.9, adult |
| 22 | ICD-10 | `M109` | Gout, unspecified |
| 23 | ICD-10 | `D649` | Anemia, unspecified |
| 24 | ICD-10 | `F329` | Major depressive disorder, single episode, unspecified |
| 25 | ICD-10 | `E11649` | Type 2 diabetes mellitus with hypoglycemia without coma |
| 26 | ICD-10 | `I252` | Old myocardial infarction |
| 27 | ICD-10 | `Z955` | Presence of coronary angioplasty implant and graft |
| 28 | ICD-10 | `Z7902` | Long term (current) use of antithrombotics/antiplatelets |
| 29 | ICD-10 | `Z794` | Long term (current) use of insulin |
| 30 | ICD-10 | `Z87891` | Personal history of nicotine dependence |

## 5. ICU Stays

_No ICU stay recorded for this admission._

## 6. Escalation / Severity Indicators

_No escalation indicators detected from ICD codes or ICU procedure events._

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2147-12-04 | ICD-10 | `0LBW0ZZ` | Excision of Left Foot Tendon, Open Approach |
| 2 | 2147-12-17 | ICD-10 | `B410ZZZ` | Fluoroscopy of Abdominal Aorta |
| 3 | 2147-12-17 | ICD-10 | `B41GYZZ` | Fluoroscopy of Left Lower Extremity Arteries using Other Contrast |


## 8. Critical Findings (Charted Events)

_No critical chart events detected._

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2147-12-04 13:11:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2147-12-04 13:11:00 | Transfer | → Emergency Department (ED) |
| 2147-12-04 20:48:00 | Admission | Admitted from EMERGENCY ROOM (OBSERVATION ADMIT) |
| 2147-12-05 02:28:00 | ED Departure | Left Emergency Dept. |
| 2147-12-18 16:43:00 | Discharge | To SKILLED NURSING FACILITY |

## 10. Missing / Ambiguous Data

- No ICU stay — patient managed on floor/step-down only.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
