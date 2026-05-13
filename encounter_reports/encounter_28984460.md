# Encounter Report — HADM 28984460

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 28984460 |
| Subject ID | 10023239 |
| Patient Sex | F |
| Patient Anchor Age (at anchor year) | 29 |
| Anchor Year | 2137 |
| Admission Time | 2140-10-22 22:04:00 |
| Discharge Time | 2140-10-23 17:01:00 |
| Admission Type | EU OBSERVATION |
| Admission Location | PHYSICIAN REFERRAL |
| Discharge Location | N/A |
| Insurance | Other |
| Language | ENGLISH |
| Marital Status | MARRIED |
| Race/Ethnicity | WHITE |
| ED Registration | 2140-10-22 18:05:00 |
| ED Departure | 2140-10-23 17:01:00 |
| In-Hospital Mortality | No |
| Date of Death (overall) | N/A |

## 2. Hospital Visit Reason

### Primary Diagnosis (seq_num = 1)

- **ICD-10 N179**: Acute kidney failure, unspecified

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2140-10-22 22:05:28 | N/A | MED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-10 `N179`: Acute kidney failure, unspecified
- (seq 2) ICD-10 `E1165`: Type 2 diabetes mellitus with hyperglycemia
- (seq 3) ICD-10 `D869`: Sarcoidosis, unspecified
- (seq 4) ICD-10 `E039`: Hypothyroidism, unspecified
- (seq 5) ICD-10 `E871`: Hypo-osmolality and hyponatremia

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-10 | `N179` | Acute kidney failure, unspecified |
| 2 | ICD-10 | `E1165` | Type 2 diabetes mellitus with hyperglycemia |
| 3 | ICD-10 | `D869` | Sarcoidosis, unspecified |
| 4 | ICD-10 | `E039` | Hypothyroidism, unspecified |
| 5 | ICD-10 | `E871` | Hypo-osmolality and hyponatremia |
| 6 | ICD-10 | `E7800` | Pure hypercholesterolemia, unspecified |
| 7 | ICD-10 | `G40909` | Epilepsy, unspecified, not intractable, without status epilepticus |
| 8 | ICD-10 | `Z794` | Long term (current) use of insulin |

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
| 2140-10-22 18:05:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2140-10-22 18:05:00 | Transfer | → Emergency Department (ED) |
| 2140-10-22 22:04:00 | Admission | Admitted from PHYSICIAN REFERRAL (EU OBSERVATION) |
| 2140-10-23 17:01:00 | Discharge | To N/A |
| 2140-10-23 17:01:00 | ED Departure | Left Emergency Dept. |

## 10. Missing / Ambiguous Data

- Discharge location not recorded.
- No procedure ICD codes — procedures may not have been coded or were minor.
- No ICU stay — patient managed on floor/step-down only.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
