# Encounter Report — HADM 21390688

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 21390688 |
| Subject ID | 10039997 |
| Patient Sex | F |
| Patient Anchor Age (at anchor year) | 67 |
| Anchor Year | 2134 |
| Admission Time | 2135-11-07 02:42:00 |
| Discharge Time | 2135-11-07 06:27:00 |
| Admission Type | EU OBSERVATION |
| Admission Location | EMERGENCY ROOM |
| Discharge Location | N/A |
| Insurance | Medicare |
| Language | ENGLISH |
| Marital Status | WIDOWED |
| Race/Ethnicity | BLACK/AFRICAN AMERICAN |
| ED Registration | 2135-11-06 21:44:00 |
| ED Departure | 2135-11-07 06:27:00 |
| In-Hospital Mortality | No |
| Date of Death (overall) | N/A |

## 2. Hospital Visit Reason

### Primary Diagnosis (seq_num = 1)

- **ICD-10 F309**: Manic episode, unspecified

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2135-11-07 02:42:35 | N/A | MED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-10 `F309`: Manic episode, unspecified
- (seq 2) ICD-10 `F17210`: Nicotine dependence, cigarettes, uncomplicated
- (seq 3) ICD-10 `I10`: Essential (primary) hypertension
- (seq 4) ICD-10 `I69354`: Hemiplegia and hemiparesis following cerebral infarction affecting left non-dominant side
- (seq 5) ICD-10 `F4310`: Post-traumatic stress disorder, unspecified

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-10 | `F309` | Manic episode, unspecified |
| 2 | ICD-10 | `F17210` | Nicotine dependence, cigarettes, uncomplicated |
| 3 | ICD-10 | `I10` | Essential (primary) hypertension |
| 4 | ICD-10 | `I69354` | Hemiplegia and hemiparesis following cerebral infarction affecting left non-dominant side |
| 5 | ICD-10 | `F4310` | Post-traumatic stress disorder, unspecified |

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
| 2135-11-06 21:44:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2135-11-06 21:44:00 | Transfer | → Emergency Department (ED) |
| 2135-11-07 02:42:00 | Admission | Admitted from EMERGENCY ROOM (EU OBSERVATION) |
| 2135-11-07 06:27:00 | Discharge | To N/A |
| 2135-11-07 06:27:00 | ED Departure | Left Emergency Dept. |

## 10. Missing / Ambiguous Data

- Discharge location not recorded.
- No procedure ICD codes — procedures may not have been coded or were minor.
- No ICU stay — patient managed on floor/step-down only.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
