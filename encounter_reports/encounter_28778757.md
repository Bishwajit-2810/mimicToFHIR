# Encounter Report — HADM 28778757

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 28778757 |
| Subject ID | 10020306 |
| Patient Sex | F |
| Patient Anchor Age (at anchor year) | 74 |
| Anchor Year | 2129 |
| Admission Time | 2129-10-29 08:00:00 |
| Discharge Time | 2129-10-30 13:20:00 |
| Admission Type | AMBULATORY OBSERVATION |
| Admission Location | PACU |
| Discharge Location | N/A |
| Insurance | Medicare |
| Language | ENGLISH |
| Marital Status | SINGLE |
| Race/Ethnicity | BLACK/AFRICAN AMERICAN |
| ED Registration | N/A |
| ED Departure | N/A |
| In-Hospital Mortality | No |
| Date of Death (overall) | N/A |

## 2. Hospital Visit Reason

### Primary Diagnosis (seq_num = 1)

- **ICD-9 1741**: Malignant neoplasm of central portion of female breast

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2129-10-29 15:12:26 | N/A | SURG |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-9 `1741`: Malignant neoplasm of central portion of female breast
- (seq 2) ICD-9 `4019`: Unspecified essential hypertension
- (seq 3) ICD-9 `25000`: Diabetes mellitus without mention of complication, type II or unspecified type, not stated as uncontrolled
- (seq 4) ICD-9 `41400`: Coronary atherosclerosis of unspecified type of vessel, native or graft
- (seq 5) ICD-9 `4149`: Chronic ischemic heart disease, unspecified

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-9 | `1741` | Malignant neoplasm of central portion of female breast |
| 2 | ICD-9 | `4019` | Unspecified essential hypertension |
| 3 | ICD-9 | `25000` | Diabetes mellitus without mention of complication, type II or unspecified type, not stated as uncontrolled |
| 4 | ICD-9 | `41400` | Coronary atherosclerosis of unspecified type of vessel, native or graft |
| 5 | ICD-9 | `4149` | Chronic ischemic heart disease, unspecified |
| 6 | ICD-9 | `412` | Old myocardial infarction |
| 7 | ICD-9 | `32723` | Obstructive sleep apnea (adult)(pediatric) |
| 8 | ICD-9 | `2724` | Other and unspecified hyperlipidemia |
| 9 | ICD-9 | `53081` | Esophageal reflux |
| 10 | ICD-9 | `V103` | Personal history of malignant neoplasm of breast |
| 11 | ICD-9 | `V1254` | Personal history of transient ischemic attack (TIA), and cerebral infarction without residual deficits |
| 12 | ICD-9 | `V163` | Family history of malignant neoplasm of breast |
| 13 | ICD-9 | `V4571` | Acquired absence of breast and nipple |

## 5. ICU Stays

_No ICU stay recorded for this admission._

## 6. Escalation / Severity Indicators

_No escalation indicators detected from ICD codes or ICU procedure events._

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2129-10-29 | ICD-9 | `8541` | Unilateral simple mastectomy |
| 2 | 2129-10-29 | ICD-9 | `4023` | Excision of axillary lymph node |


## 8. Critical Findings (Charted Events)

_No critical chart events detected._

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2129-10-29 08:00:00 | Admission | Admitted from PACU (AMBULATORY OBSERVATION) |
| 2129-10-30 13:20:00 | Discharge | To N/A |

## 10. Missing / Ambiguous Data

- No ED registration time — admission may not have gone through ED.
- Discharge location not recorded.
- No ICU stay — patient managed on floor/step-down only.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
