# Encounter Report — HADM 24225421

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 24225421 |
| Subject ID | 10037928 |
| Patient Sex | F |
| Patient Anchor Age (at anchor year) | 78 |
| Anchor Year | 2175 |
| Admission Time | 2178-09-28 23:05:00 |
| Discharge Time | 2178-10-02 17:13:00 |
| Admission Type | EW EMER. |
| Admission Location | EMERGENCY ROOM |
| Discharge Location | HOME |
| Insurance | Medicare |
| Language | ? |
| Marital Status | WIDOWED |
| Race/Ethnicity | HISPANIC/LATINO - CUBAN |
| ED Registration | 2178-09-28 20:29:00 |
| ED Departure | 2178-09-29 00:43:00 |
| In-Hospital Mortality | No |
| Date of Death (overall) | N/A |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| HCFA | 155 | OTHER EAR, NOSE, MOUTH & THROAT DIAGNOSES W CC | N/A | N/A |
| APR | 115 | OTHER EAR, NOSE, MOUTH,THROAT & CRANIAL/FACIAL DIAGNOSES | 3.0 | 3.0 |

### Primary Diagnosis (seq_num = 1)

- **ICD-9 38010**: Infective otitis externa, unspecified

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2178-09-28 23:06:20 | N/A | MED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-9 `38010`: Infective otitis externa, unspecified
- (seq 2) ICD-9 `5990`: Urinary tract infection, site not specified
- (seq 3) ICD-9 `5849`: Acute kidney failure, unspecified
- (seq 4) ICD-9 `25000`: Diabetes mellitus without mention of complication, type II or unspecified type, not stated as uncontrolled
- (seq 5) ICD-9 `27652`: Hypovolemia

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-9 | `38010` | Infective otitis externa, unspecified |
| 2 | ICD-9 | `5990` | Urinary tract infection, site not specified |
| 3 | ICD-9 | `5849` | Acute kidney failure, unspecified |
| 4 | ICD-9 | `25000` | Diabetes mellitus without mention of complication, type II or unspecified type, not stated as uncontrolled |
| 5 | ICD-9 | `27652` | Hypovolemia |
| 6 | ICD-9 | `2761` | Hyposmolality and/or hyponatremia |
| 7 | ICD-9 | `2724` | Other and unspecified hyperlipidemia |
| 8 | ICD-9 | `04149` | Other and unspecified Escherichia coli [E. coli] |
| 9 | ICD-9 | `V5867` | Long-term (current) use of insulin |
| 10 | ICD-9 | `4019` | Unspecified essential hypertension |
| 11 | ICD-9 | `311` | Depressive disorder, not elsewhere classified |
| 12 | ICD-9 | `53081` | Esophageal reflux |
| 13 | ICD-9 | `V1001` | Personal history of malignant neoplasm of tongue |
| 14 | ICD-9 | `30000` | Anxiety state, unspecified |
| 15 | ICD-9 | `2859` | Anemia, unspecified |
| 16 | ICD-9 | `78830` | Urinary incontinence, unspecified |
| 17 | ICD-9 | `38531` | Cholesteatoma of attic |

## 5. ICU Stays

_No ICU stay recorded for this admission._

## 6. Escalation / Severity Indicators

The following critical conditions or interventions were detected:

- **Acute Kidney Injury** (ICD diagnosis)

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2178-09-29 | ICD-9 | `2911` | Pharyngoscopy |
| 2 | 2178-09-29 | ICD-9 | `9652` | Irrigation of ear |
| 3 | 2178-09-29 | ICD-9 | `2219` | Other diagnostic procedures on nasal sinuses |


## 8. Critical Findings (Charted Events)

_No critical chart events detected._

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2178-09-28 20:29:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2178-09-28 20:29:00 | Transfer | → Emergency Department (ED) |
| 2178-09-28 23:05:00 | Admission | Admitted from EMERGENCY ROOM (EW EMER.) |
| 2178-09-29 00:43:00 | ED Departure | Left Emergency Dept. |
| 2178-10-02 17:13:00 | Discharge | To HOME |

## 10. Missing / Ambiguous Data

- No ICU stay — patient managed on floor/step-down only.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
