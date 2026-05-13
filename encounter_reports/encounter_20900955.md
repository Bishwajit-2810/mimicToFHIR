# Encounter Report — HADM 20900955

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 20900955 |
| Subject ID | 10014354 |
| Patient Sex | M |
| Patient Anchor Age (at anchor year) | 60 |
| Anchor Year | 2146 |
| Admission Time | 2149-03-04 23:14:00 |
| Discharge Time | 2149-03-05 14:59:00 |
| Admission Type | EU OBSERVATION |
| Admission Location | WALK-IN/SELF REFERRAL |
| Discharge Location | N/A |
| Insurance | Other |
| Language | ENGLISH |
| Marital Status | SINGLE |
| Race/Ethnicity | WHITE |
| ED Registration | 2149-03-04 20:24:00 |
| ED Departure | 2149-03-05 14:59:00 |
| In-Hospital Mortality | No |
| Date of Death (overall) | N/A |

## 2. Hospital Visit Reason

### Primary Diagnosis (seq_num = 1)

- **ICD-10 R410**: Disorientation, unspecified

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2149-03-04 23:15:10 | N/A | MED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-10 `R410`: Disorientation, unspecified
- (seq 2) ICD-10 `R51`: Headache
- (seq 3) ICD-10 `M533`: Sacrococcygeal disorders, not elsewhere classified
- (seq 4) ICD-10 `M25512`: Pain in left shoulder
- (seq 5) ICD-10 `E119`: Type 2 diabetes mellitus without complications

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-10 | `R410` | Disorientation, unspecified |
| 2 | ICD-10 | `R51` | Headache |
| 3 | ICD-10 | `M533` | Sacrococcygeal disorders, not elsewhere classified |
| 4 | ICD-10 | `M25512` | Pain in left shoulder |
| 5 | ICD-10 | `E119` | Type 2 diabetes mellitus without complications |
| 6 | ICD-10 | `C9110` | Chronic lymphocytic leukemia of B-cell type not having achieved remission |
| 7 | ICD-10 | `I110` | Hypertensive heart disease with heart failure |
| 8 | ICD-10 | `I509` | Heart failure, unspecified |
| 9 | ICD-10 | `Z8673` | Personal history of transient ischemic attack (TIA), and cerebral infarction without residual deficits |
| 10 | ICD-10 | `Z950` | Presence of cardiac pacemaker |
| 11 | ICD-10 | `E785` | Hyperlipidemia, unspecified |
| 12 | ICD-10 | `I4891` | Unspecified atrial fibrillation |
| 13 | ICD-10 | `Z7902` | Long term (current) use of antithrombotics/antiplatelets |
| 14 | ICD-10 | `Z794` | Long term (current) use of insulin |

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
| 2149-03-04 20:24:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2149-03-04 20:24:00 | Transfer | → Emergency Department (ED) |
| 2149-03-04 23:14:00 | Admission | Admitted from WALK-IN/SELF REFERRAL (EU OBSERVATION) |
| 2149-03-05 14:59:00 | Discharge | To N/A |
| 2149-03-05 14:59:00 | ED Departure | Left Emergency Dept. |

## 10. Missing / Ambiguous Data

- Discharge location not recorded.
- No procedure ICD codes — procedures may not have been coded or were minor.
- No ICU stay — patient managed on floor/step-down only.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
