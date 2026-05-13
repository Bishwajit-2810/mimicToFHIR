# Encounter Report — HADM 29802992

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 29802992 |
| Subject ID | 10037928 |
| Patient Sex | F |
| Patient Anchor Age (at anchor year) | 78 |
| Anchor Year | 2175 |
| Admission Time | 2179-07-25 00:06:00 |
| Discharge Time | 2179-07-28 15:54:00 |
| Admission Type | EW EMER. |
| Admission Location | EMERGENCY ROOM |
| Discharge Location | HOME HEALTH CARE |
| Insurance | Medicare |
| Language | ? |
| Marital Status | WIDOWED |
| Race/Ethnicity | HISPANIC/LATINO - CUBAN |
| ED Registration | 2179-07-24 18:21:00 |
| ED Departure | 2179-07-25 01:17:00 |
| In-Hospital Mortality | No |
| Date of Death (overall) | N/A |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| HCFA | 682 | RENAL FAILURE W MCC | N/A | N/A |

### Primary Diagnosis (seq_num = 1)

- **ICD-9 5849**: Acute kidney failure, unspecified

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2179-07-25 00:07:48 | N/A | MED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-9 `5849`: Acute kidney failure, unspecified
- (seq 2) ICD-9 `34982`: Toxic encephalopathy
- (seq 3) ICD-9 `5990`: Urinary tract infection, site not specified
- (seq 4) ICD-9 `2761`: Hyposmolality and/or hyponatremia
- (seq 5) ICD-9 `25002`: Diabetes mellitus without mention of complication, type II or unspecified type, uncontrolled

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-9 | `5849` | Acute kidney failure, unspecified |
| 2 | ICD-9 | `34982` | Toxic encephalopathy |
| 3 | ICD-9 | `5990` | Urinary tract infection, site not specified |
| 4 | ICD-9 | `2761` | Hyposmolality and/or hyponatremia |
| 5 | ICD-9 | `25002` | Diabetes mellitus without mention of complication, type II or unspecified type, uncontrolled |
| 6 | ICD-9 | `40390` | Hypertensive chronic kidney disease, unspecified, with chronic kidney disease stage I through stage IV, or unspecified |
| 7 | ICD-9 | `42789` | Other specified cardiac dysrhythmias |
| 8 | ICD-9 | `78791` | Diarrhea |
| 9 | ICD-9 | `27652` | Hypovolemia |
| 10 | ICD-9 | `V4986` | Do not resuscitate status |
| 11 | ICD-9 | `30000` | Anxiety state, unspecified |
| 12 | ICD-9 | `53081` | Esophageal reflux |
| 13 | ICD-9 | `311` | Depressive disorder, not elsewhere classified |
| 14 | ICD-9 | `2724` | Other and unspecified hyperlipidemia |
| 15 | ICD-9 | `23871` | Essential thrombocythemia |
| 16 | ICD-9 | `59969` | Urinary obstruction, not elsewhere classified |
| 17 | ICD-9 | `78830` | Urinary incontinence, unspecified |
| 18 | ICD-9 | `04149` | Other and unspecified Escherichia coli [E. coli] |
| 19 | ICD-9 | `2809` | Iron deficiency anemia, unspecified |
| 20 | ICD-9 | `33829` | Other chronic pain |
| 21 | ICD-9 | `7245` | Backache, unspecified |
| 22 | ICD-9 | `5859` | Chronic kidney disease, unspecified |
| 23 | ICD-9 | `V1001` | Personal history of malignant neoplasm of tongue |
| 24 | ICD-9 | `V5867` | Long-term (current) use of insulin |
| 25 | ICD-9 | `V1581` | Personal history of noncompliance with medical treatment, presenting hazards to health |
| 26 | ICD-9 | `V1302` | Personal history, urinary (tract) infection |

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
| 2179-07-24 18:21:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2179-07-24 18:21:00 | Transfer | → Emergency Department (ED) |
| 2179-07-25 00:06:00 | Admission | Admitted from EMERGENCY ROOM (EW EMER.) |
| 2179-07-25 01:17:00 | ED Departure | Left Emergency Dept. |
| 2179-07-28 15:54:00 | Discharge | To HOME HEALTH CARE |

## 10. Missing / Ambiguous Data

- No procedure ICD codes — procedures may not have been coded or were minor.
- No ICU stay — patient managed on floor/step-down only.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
