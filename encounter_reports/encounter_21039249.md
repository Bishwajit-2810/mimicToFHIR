# Encounter Report — HADM 21039249

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 21039249 |
| Subject ID | 10004457 |
| Patient Sex | M |
| Patient Anchor Age (at anchor year) | 65 |
| Anchor Year | 2140 |
| Admission Time | 2140-09-17 13:41:00 |
| Discharge Time | 2140-09-18 12:40:00 |
| Admission Type | AMBULATORY OBSERVATION |
| Admission Location | PROCEDURE SITE |
| Discharge Location | N/A |
| Insurance | Medicare |
| Language | ENGLISH |
| Marital Status | SINGLE |
| Race/Ethnicity | WHITE |
| ED Registration | N/A |
| ED Departure | N/A |
| In-Hospital Mortality | No |
| Date of Death (overall) | N/A |

## 2. Hospital Visit Reason

### Primary Diagnosis (seq_num = 1)

- **ICD-9 41401**: Coronary atherosclerosis of native coronary artery

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2140-09-17 13:41:45 | N/A | CMED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-9 `41401`: Coronary atherosclerosis of native coronary artery
- (seq 2) ICD-9 `2724`: Other and unspecified hyperlipidemia
- (seq 3) ICD-9 `4019`: Unspecified essential hypertension
- (seq 4) ICD-9 `49390`: Asthma, unspecified type, unspecified
- (seq 5) ICD-9 `V1046`: Personal history of malignant neoplasm of prostate

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-9 | `41401` | Coronary atherosclerosis of native coronary artery |
| 2 | ICD-9 | `2724` | Other and unspecified hyperlipidemia |
| 3 | ICD-9 | `4019` | Unspecified essential hypertension |
| 4 | ICD-9 | `49390` | Asthma, unspecified type, unspecified |
| 5 | ICD-9 | `V1046` | Personal history of malignant neoplasm of prostate |
| 6 | ICD-9 | `V1072` | Personal history of hodgkin's disease |
| 7 | ICD-9 | `V153` | Personal history of irradiation, presenting hazards to health |
| 8 | ICD-9 | `V8741` | Personal history of antineoplastic chemotherapy |

## 5. ICU Stays

_No ICU stay recorded for this admission._

## 6. Escalation / Severity Indicators

_No escalation indicators detected from ICD codes or ICU procedure events._

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2140-09-17 | ICD-9 | `0066` | Percutaneous transluminal coronary angioplasty [PTCA] |
| 2 | 2140-09-17 | ICD-9 | `3607` | Insertion of drug-eluting coronary artery stent(s) |
| 3 | 2140-09-17 | ICD-9 | `3722` | Left heart cardiac catheterization |
| 4 | 2140-09-17 | ICD-9 | `0045` | Insertion of one vascular stent |
| 5 | 2140-09-17 | ICD-9 | `0040` | Procedure on single vessel |
| 6 | 2140-09-17 | ICD-9 | `8856` | Coronary arteriography using two catheters |


## 8. Critical Findings (Charted Events)

_No critical chart events detected._

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2140-09-17 13:41:00 | Admission | Admitted from PROCEDURE SITE (AMBULATORY OBSERVATION) |
| 2140-09-18 12:40:00 | Discharge | To N/A |

## 10. Missing / Ambiguous Data

- No ED registration time — admission may not have gone through ED.
- Discharge location not recorded.
- No ICU stay — patient managed on floor/step-down only.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
