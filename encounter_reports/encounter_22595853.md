# Encounter Report — HADM 22595853

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 22595853 |
| Subject ID | 10000032 |
| Patient Sex | F |
| Patient Anchor Age (at anchor year) | 52 |
| Anchor Year | 2180 |
| Admission Time | 2180-05-06 22:23:00 |
| Discharge Time | 2180-05-07 17:15:00 |
| Admission Type | URGENT |
| Admission Location | TRANSFER FROM HOSPITAL |
| Discharge Location | HOME |
| Insurance | Other |
| Language | ENGLISH |
| Marital Status | WIDOWED |
| Race/Ethnicity | WHITE |
| ED Registration | 2180-05-06 19:17:00 |
| ED Departure | 2180-05-06 23:30:00 |
| In-Hospital Mortality | No |
| Date of Death (overall) | 2180-09-09 |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| APR | 283 | OTHER DISORDERS OF THE LIVER | 2.0 | 2.0 |
| HCFA | 442 | DISORDERS OF LIVER EXCEPT MALIG,CIRR,ALC HEPA W CC | N/A | N/A |

### Primary Diagnosis (seq_num = 1)

- **ICD-9 5723**: Portal hypertension

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2180-05-06 22:24:57 | N/A | MED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-9 `5723`: Portal hypertension
- (seq 2) ICD-9 `78959`: Other ascites
- (seq 3) ICD-9 `5715`: Cirrhosis of liver without mention of alcohol
- (seq 4) ICD-9 `07070`: Unspecified viral hepatitis C without hepatic coma
- (seq 5) ICD-9 `496`: Chronic airway obstruction, not elsewhere classified

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-9 | `5723` | Portal hypertension |
| 2 | ICD-9 | `78959` | Other ascites |
| 3 | ICD-9 | `5715` | Cirrhosis of liver without mention of alcohol |
| 4 | ICD-9 | `07070` | Unspecified viral hepatitis C without hepatic coma |
| 5 | ICD-9 | `496` | Chronic airway obstruction, not elsewhere classified |
| 6 | ICD-9 | `29680` | Bipolar disorder, unspecified |
| 7 | ICD-9 | `30981` | Posttraumatic stress disorder |
| 8 | ICD-9 | `V1582` | Personal history of tobacco use |

## 5. ICU Stays

_No ICU stay recorded for this admission._

## 6. Escalation / Severity Indicators

The following critical conditions or interventions were detected:

- **Liver Failure** (ICD diagnosis)

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2180-05-07 | ICD-9 | `5491` | Percutaneous abdominal drainage |


## 8. Critical Findings (Charted Events)

_No critical chart events detected._

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2180-05-06 19:17:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2180-05-06 19:17:00 | Transfer | → Emergency Department (ED) |
| 2180-05-06 22:23:00 | Admission | Admitted from TRANSFER FROM HOSPITAL (URGENT) |
| 2180-05-06 23:30:00 | ED Departure | Left Emergency Dept. |
| 2180-05-07 17:15:00 | Discharge | To HOME |

## 10. Missing / Ambiguous Data

- No ICU stay — patient managed on floor/step-down only.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
