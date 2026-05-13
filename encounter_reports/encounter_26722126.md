# Encounter Report — HADM 26722126

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 26722126 |
| Subject ID | 10014354 |
| Patient Sex | M |
| Patient Anchor Age (at anchor year) | 60 |
| Anchor Year | 2146 |
| Admission Time | 2146-11-09 01:53:00 |
| Discharge Time | 2146-11-09 13:13:00 |
| Admission Type | EU OBSERVATION |
| Admission Location | EMERGENCY ROOM |
| Discharge Location | N/A |
| Insurance | Other |
| Language | ENGLISH |
| Marital Status | MARRIED |
| Race/Ethnicity | WHITE |
| ED Registration | 2146-11-08 21:24:00 |
| ED Departure | 2146-11-09 13:13:00 |
| In-Hospital Mortality | No |
| Date of Death (overall) | N/A |

## 2. Hospital Visit Reason

### Primary Diagnosis (seq_num = 1)

- **ICD-10 R079**: Chest pain, unspecified

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2146-11-09 01:54:30 | N/A | MED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-10 `R079`: Chest pain, unspecified
- (seq 2) ICD-10 `C9110`: Chronic lymphocytic leukemia of B-cell type not having achieved remission
- (seq 3) ICD-10 `I272`: Other secondary pulmonary hypertension
- (seq 4) ICD-10 `R001`: Bradycardia, unspecified
- (seq 5) ICD-10 `E785`: Hyperlipidemia, unspecified

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-10 | `R079` | Chest pain, unspecified |
| 2 | ICD-10 | `C9110` | Chronic lymphocytic leukemia of B-cell type not having achieved remission |
| 3 | ICD-10 | `I272` | Other secondary pulmonary hypertension |
| 4 | ICD-10 | `R001` | Bradycardia, unspecified |
| 5 | ICD-10 | `E785` | Hyperlipidemia, unspecified |
| 6 | ICD-10 | `E119` | Type 2 diabetes mellitus without complications |
| 7 | ICD-10 | `E780` | Pure hypercholesterolemia |
| 8 | ICD-10 | `Z950` | Presence of cardiac pacemaker |
| 9 | ICD-10 | `Z8673` | Personal history of transient ischemic attack (TIA), and cerebral infarction without residual deficits |
| 10 | ICD-10 | `Z9049` | Acquired absence of other specified parts of digestive tract |

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
| 2146-11-08 21:24:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2146-11-08 21:24:00 | Transfer | → Emergency Department (ED) |
| 2146-11-09 01:53:00 | Admission | Admitted from EMERGENCY ROOM (EU OBSERVATION) |
| 2146-11-09 13:13:00 | Discharge | To N/A |
| 2146-11-09 13:13:00 | ED Departure | Left Emergency Dept. |

## 10. Missing / Ambiguous Data

- Discharge location not recorded.
- No procedure ICD codes — procedures may not have been coded or were minor.
- No ICU stay — patient managed on floor/step-down only.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
