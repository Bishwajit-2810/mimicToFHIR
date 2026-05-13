# Encounter Report — HADM 26173805

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 26173805 |
| Subject ID | 10014354 |
| Patient Sex | M |
| Patient Anchor Age (at anchor year) | 60 |
| Anchor Year | 2146 |
| Admission Time | 2149-09-17 22:54:00 |
| Discharge Time | 2149-09-18 10:45:00 |
| Admission Type | EU OBSERVATION |
| Admission Location | WALK-IN/SELF REFERRAL |
| Discharge Location | N/A |
| Insurance | Other |
| Language | ENGLISH |
| Marital Status | SINGLE |
| Race/Ethnicity | WHITE |
| ED Registration | 2149-09-17 09:08:00 |
| ED Departure | 2149-09-17 23:55:00 |
| In-Hospital Mortality | No |
| Date of Death (overall) | N/A |

## 2. Hospital Visit Reason

### Primary Diagnosis (seq_num = 1)

- **ICD-10 R61**: Generalized hyperhidrosis

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2149-09-17 22:54:57 | N/A | OMED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-10 `R61`: Generalized hyperhidrosis
- (seq 2) ICD-10 `R638`: Other symptoms and signs concerning food and fluid intake
- (seq 3) ICD-10 `R1013`: Epigastric pain
- (seq 4) ICD-10 `R748`: Abnormal levels of other serum enzymes
- (seq 5) ICD-10 `Z8719`: Personal history of other diseases of the digestive system

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-10 | `R61` | Generalized hyperhidrosis |
| 2 | ICD-10 | `R638` | Other symptoms and signs concerning food and fluid intake |
| 3 | ICD-10 | `R1013` | Epigastric pain |
| 4 | ICD-10 | `R748` | Abnormal levels of other serum enzymes |
| 5 | ICD-10 | `Z8719` | Personal history of other diseases of the digestive system |
| 6 | ICD-10 | `C9110` | Chronic lymphocytic leukemia of B-cell type not having achieved remission |
| 7 | ICD-10 | `E1165` | Type 2 diabetes mellitus with hyperglycemia |
| 8 | ICD-10 | `E1142` | Type 2 diabetes mellitus with diabetic polyneuropathy |
| 9 | ICD-10 | `Z794` | Long term (current) use of insulin |
| 10 | ICD-10 | `E039` | Hypothyroidism, unspecified |
| 11 | ICD-10 | `Z8547` | Personal history of malignant neoplasm of testis |
| 12 | ICD-10 | `I10` | Essential (primary) hypertension |
| 13 | ICD-10 | `E785` | Hyperlipidemia, unspecified |
| 14 | ICD-10 | `G4733` | Obstructive sleep apnea (adult) (pediatric) |
| 15 | ICD-10 | `F323` | Major depressive disorder, single episode, severe with psychotic features |
| 16 | ICD-10 | `F419` | Anxiety disorder, unspecified |
| 17 | ICD-10 | `Z950` | Presence of cardiac pacemaker |
| 18 | ICD-10 | `Z8673` | Personal history of transient ischemic attack (TIA), and cerebral infarction without residual deficits |
| 19 | ICD-10 | `Z7902` | Long term (current) use of antithrombotics/antiplatelets |
| 20 | ICD-10 | `E6601` | Morbid (severe) obesity due to excess calories |
| 21 | ICD-10 | `Z6835` | Body mass index (BMI) 35.0-35.9, adult |

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
| 2149-09-17 09:08:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2149-09-17 09:08:00 | Transfer | → Emergency Department (ED) |
| 2149-09-17 22:54:00 | Admission | Admitted from WALK-IN/SELF REFERRAL (EU OBSERVATION) |
| 2149-09-17 23:55:00 | ED Departure | Left Emergency Dept. |
| 2149-09-18 10:45:00 | Discharge | To N/A |

## 10. Missing / Ambiguous Data

- Discharge location not recorded.
- No procedure ICD codes — procedures may not have been coded or were minor.
- No ICU stay — patient managed on floor/step-down only.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
