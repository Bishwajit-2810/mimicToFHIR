# Encounter Report — HADM 25933959

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 25933959 |
| Subject ID | 10040025 |
| Patient Sex | F |
| Patient Anchor Age (at anchor year) | 64 |
| Anchor Year | 2143 |
| Admission Time | 2147-12-29 19:36:00 |
| Discharge Time | 2148-01-09 17:38:00 |
| Admission Type | ELECTIVE |
| Admission Location | PHYSICIAN REFERRAL |
| Discharge Location | SKILLED NURSING FACILITY |
| Insurance | Other |
| Language | ENGLISH |
| Marital Status | DIVORCED |
| Race/Ethnicity | WHITE |
| ED Registration | N/A |
| ED Departure | N/A |
| In-Hospital Mortality | No |
| Date of Death (overall) | 2148-02-07 |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| APR | 364 | OTHER SKIN, SUBCUTANEOUS TISSUE & RELATED PROCEDURES | 2.0 | 2.0 |
| HCFA | 629 | OTHER ENDOCRINE, NUTRIT & METAB O.R. PROC W CC | N/A | N/A |

### Primary Diagnosis (seq_num = 1)

- **ICD-10 E11621**: Type 2 diabetes mellitus with foot ulcer

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2147-12-29 19:37:01 | N/A | VSURG |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-10 `E11621`: Type 2 diabetes mellitus with foot ulcer
- (seq 2) ICD-10 `L03116`: Cellulitis of left lower limb
- (seq 3) ICD-10 `L97529`: Non-pressure chronic ulcer of other part of left foot with unspecified severity
- (seq 4) ICD-10 `E1122`: Type 2 diabetes mellitus with diabetic chronic kidney disease
- (seq 5) ICD-10 `I130`: Hypertensive heart and chronic kidney disease with heart failure and stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-10 | `E11621` | Type 2 diabetes mellitus with foot ulcer |
| 2 | ICD-10 | `L03116` | Cellulitis of left lower limb |
| 3 | ICD-10 | `L97529` | Non-pressure chronic ulcer of other part of left foot with unspecified severity |
| 4 | ICD-10 | `E1122` | Type 2 diabetes mellitus with diabetic chronic kidney disease |
| 5 | ICD-10 | `I130` | Hypertensive heart and chronic kidney disease with heart failure and stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease |
| 6 | ICD-10 | `I509` | Heart failure, unspecified |
| 7 | ICD-10 | `Z794` | Long term (current) use of insulin |
| 8 | ICD-10 | `I7789` | Other specified disorders of arteries and arterioles |
| 9 | ICD-10 | `E11649` | Type 2 diabetes mellitus with hypoglycemia without coma |
| 10 | ICD-10 | `N183` | Chronic kidney disease, stage 3 (moderate) |
| 11 | ICD-10 | `Z87891` | Personal history of nicotine dependence |
| 12 | ICD-10 | `E785` | Hyperlipidemia, unspecified |
| 13 | ICD-10 | `E039` | Hypothyroidism, unspecified |
| 14 | ICD-10 | `I2510` | Atherosclerotic heart disease of native coronary artery without angina pectoris |
| 15 | ICD-10 | `Z955` | Presence of coronary angioplasty implant and graft |
| 16 | ICD-10 | `I252` | Old myocardial infarction |
| 17 | ICD-10 | `Z7902` | Long term (current) use of antithrombotics/antiplatelets |
| 18 | ICD-10 | `E669` | Obesity, unspecified |
| 19 | ICD-10 | `Z6830` | Body mass index (BMI) 30.0-30.9, adult |
| 20 | ICD-10 | `M109` | Gout, unspecified |
| 21 | ICD-10 | `D649` | Anemia, unspecified |
| 22 | ICD-10 | `F329` | Major depressive disorder, single episode, unspecified |
| 23 | ICD-10 | `I701` | Atherosclerosis of renal artery |
| 24 | ICD-10 | `I4891` | Unspecified atrial fibrillation |

## 5. ICU Stays

_No ICU stay recorded for this admission._

## 6. Escalation / Severity Indicators

_No escalation indicators detected from ICD codes or ICU procedure events._

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2147-12-30 | ICD-10 | `041L09L` | Bypass Left Femoral Artery to Popliteal Artery with Autologous Venous Tissue, Open Approach |
| 2 | 2147-12-30 | ICD-10 | `06BQ0ZZ` | Excision of Left Saphenous Vein, Open Approach |
| 3 | 2147-12-30 | ICD-10 | `0LBW0ZZ` | Excision of Left Foot Tendon, Open Approach |


## 8. Critical Findings (Charted Events)

_No critical chart events detected._

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2147-12-29 19:36:00 | Admission | Admitted from PHYSICIAN REFERRAL (ELECTIVE) |
| 2147-12-30 07:54:34 | Transfer | → Vascular (transfer) |
| 2147-12-30 16:08:24 | Transfer | → Vascular (transfer) |
| 2148-01-06 15:07:44 | Transfer | → Vascular (transfer) |
| 2148-01-09 17:38:00 | Discharge | To SKILLED NURSING FACILITY |

## 10. Missing / Ambiguous Data

- No ED registration time — admission may not have gone through ED.
- No ICU stay — patient managed on floor/step-down only.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
