# Encounter Report — HADM 20572787

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 20572787 |
| Subject ID | 10039708 |
| Patient Sex | F |
| Patient Anchor Age (at anchor year) | 46 |
| Anchor Year | 2138 |
| Admission Time | 2138-10-30 23:30:00 |
| Discharge Time | 2138-11-06 23:30:00 |
| Admission Type | EW EMER. |
| Admission Location | EMERGENCY ROOM |
| Discharge Location | AGAINST ADVICE |
| Insurance | Other |
| Language | ENGLISH |
| Marital Status | SINGLE |
| Race/Ethnicity | BLACK/AFRICAN AMERICAN |
| ED Registration | 2138-10-30 17:27:00 |
| ED Departure | 2138-10-31 00:19:00 |
| In-Hospital Mortality | No |
| Date of Death (overall) | N/A |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| APR | 421 | MALNUTRITION, FAILURE TO THRIVE & OTHER NUTRITIONAL DISORDERS | 2.0 | 1.0 |
| HCFA | 641 | MISC DISORDERS OF NUTRITION,METABOLISM,FLUIDS/ELECTROLYTES W/O MCC | N/A | N/A |

### Primary Diagnosis (seq_num = 1)

- **ICD-9 2651**: Other and unspecified manifestations of thiamine deficiency

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2138-10-30 23:31:22 | N/A | MED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-9 `2651`: Other and unspecified manifestations of thiamine deficiency
- (seq 2) ICD-9 `3575`: Alcoholic polyneuropathy
- (seq 3) ICD-9 `2449`: Unspecified acquired hypothyroidism
- (seq 4) ICD-9 `3051`: Tobacco use disorder
- (seq 5) ICD-9 `4019`: Unspecified essential hypertension

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-9 | `2651` | Other and unspecified manifestations of thiamine deficiency |
| 2 | ICD-9 | `3575` | Alcoholic polyneuropathy |
| 3 | ICD-9 | `2449` | Unspecified acquired hypothyroidism |
| 4 | ICD-9 | `3051` | Tobacco use disorder |
| 5 | ICD-9 | `4019` | Unspecified essential hypertension |
| 6 | ICD-9 | `V4586` | Bariatric surgery status |
| 7 | ICD-9 | `30391` | Other and unspecified alcohol dependence, continuous |
| 8 | ICD-9 | `49390` | Asthma, unspecified type, unspecified |
| 9 | ICD-9 | `2859` | Anemia, unspecified |
| 10 | ICD-9 | `2662` | Other B-complex deficiencies |
| 11 | ICD-9 | `2749` | Gout, unspecified |

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
| 2138-10-30 17:27:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2138-10-30 17:27:00 | Transfer | → Emergency Department (ED) |
| 2138-10-30 23:30:00 | Admission | Admitted from EMERGENCY ROOM (EW EMER.) |
| 2138-10-31 00:19:00 | ED Departure | Left Emergency Dept. |
| 2138-11-06 23:30:00 | Discharge | To AGAINST ADVICE |

## 10. Missing / Ambiguous Data

- No procedure ICD codes — procedures may not have been coded or were minor.
- No ICU stay — patient managed on floor/step-down only.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
