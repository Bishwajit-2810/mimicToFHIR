# Encounter Report — HADM 24244087

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 24244087 |
| Subject ID | 10023117 |
| Patient Sex | M |
| Patient Anchor Age (at anchor year) | 53 |
| Anchor Year | 2170 |
| Admission Time | 2174-06-07 23:25:00 |
| Discharge Time | 2174-06-12 15:55:00 |
| Admission Type | URGENT |
| Admission Location | TRANSFER FROM HOSPITAL |
| Discharge Location | HOME |
| Insurance | Medicare |
| Language | ENGLISH |
| Marital Status | WIDOWED |
| Race/Ethnicity | WHITE |
| ED Registration | 2174-06-07 16:24:00 |
| ED Departure | 2174-06-08 01:02:00 |
| In-Hospital Mortality | No |
| Date of Death (overall) | 2175-07-20 |

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
| 2174-06-07 23:26:35 | N/A | MED |
| 2174-06-08 00:11:34 | MED | CMED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-9 `5849`: Acute kidney failure, unspecified
- (seq 2) ICD-9 `42823`: Acute on chronic systolic heart failure
- (seq 3) ICD-9 `4271`: Paroxysmal ventricular tachycardia
- (seq 4) ICD-9 `4254`: Other primary cardiomyopathies
- (seq 5) ICD-9 `78959`: Other ascites

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-9 | `5849` | Acute kidney failure, unspecified |
| 2 | ICD-9 | `42823` | Acute on chronic systolic heart failure |
| 3 | ICD-9 | `4271` | Paroxysmal ventricular tachycardia |
| 4 | ICD-9 | `4254` | Other primary cardiomyopathies |
| 5 | ICD-9 | `78959` | Other ascites |
| 6 | ICD-9 | `7530` | Renal agenesis and dysgenesis |
| 7 | ICD-9 | `2761` | Hyposmolality and/or hyponatremia |
| 8 | ICD-9 | `40491` | Hypertensive heart and chronic kidney disease, unspecified, with heart failure and with chronic kidney disease stage I through stage IV, or unspecified |
| 9 | ICD-9 | `29530` | Paranoid type schizophrenia, unspecified |
| 10 | ICD-9 | `4168` | Other chronic pulmonary heart diseases |
| 11 | ICD-9 | `4280` | Congestive heart failure, unspecified |
| 12 | ICD-9 | `5859` | Chronic kidney disease, unspecified |
| 13 | ICD-9 | `2800` | Iron deficiency anemia secondary to blood loss (chronic) |
| 14 | ICD-9 | `4240` | Mitral valve disorders |
| 15 | ICD-9 | `53085` | Barrett's esophagus |
| 16 | ICD-9 | `311` | Depressive disorder, not elsewhere classified |
| 17 | ICD-9 | `2724` | Other and unspecified hyperlipidemia |
| 18 | ICD-9 | `27800` | Obesity, unspecified |
| 19 | ICD-9 | `53081` | Esophageal reflux |
| 20 | ICD-9 | `3970` | Diseases of tricuspid valve |
| 21 | ICD-9 | `5730` | Chronic passive congestion of liver |
| 22 | ICD-9 | `28860` | Leukocytosis, unspecified |
| 23 | ICD-9 | `V5866` | Long-term (current) use of aspirin |
| 24 | ICD-9 | `V1052` | Personal history of malignant neoplasm of kidney |
| 25 | ICD-9 | `V8523` | Body Mass Index 27.0-27.9, adult |
| 26 | ICD-9 | `V1582` | Personal history of tobacco use |
| 27 | ICD-9 | `V5331` | Fitting and adjustment of cardiac pacemaker |

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
| 2174-06-07 16:24:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2174-06-07 16:24:00 | Transfer | → Emergency Department (ED) |
| 2174-06-07 23:25:00 | Admission | Admitted from TRANSFER FROM HOSPITAL (URGENT) |
| 2174-06-08 01:02:00 | ED Departure | Left Emergency Dept. |
| 2174-06-12 15:55:00 | Discharge | To HOME |

## 10. Missing / Ambiguous Data

- No procedure ICD codes — procedures may not have been coded or were minor.
- No ICU stay — patient managed on floor/step-down only.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
