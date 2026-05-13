# Encounter Report — HADM 20457729

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 20457729 |
| Subject ID | 10012853 |
| Patient Sex | F |
| Patient Anchor Age (at anchor year) | 91 |
| Anchor Year | 2175 |
| Admission Time | 2177-11-03 09:30:00 |
| Discharge Time | 2177-11-04 15:06:00 |
| Admission Type | DIRECT OBSERVATION |
| Admission Location | PHYSICIAN REFERRAL |
| Discharge Location | N/A |
| Insurance | Medicare |
| Language | ENGLISH |
| Marital Status | WIDOWED |
| Race/Ethnicity | BLACK/AFRICAN AMERICAN |
| ED Registration | N/A |
| ED Departure | N/A |
| In-Hospital Mortality | No |
| Date of Death (overall) | N/A |

## 2. Hospital Visit Reason

### Primary Diagnosis (seq_num = 1)

- **ICD-10 C73**: Malignant neoplasm of thyroid gland

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2177-11-03 16:25:34 | N/A | SURG |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-10 `C73`: Malignant neoplasm of thyroid gland
- (seq 2) ICD-10 `N319`: Neuromuscular dysfunction of bladder, unspecified
- (seq 3) ICD-10 `I480`: Paroxysmal atrial fibrillation
- (seq 4) ICD-10 `Z7902`: Long term (current) use of antithrombotics/antiplatelets
- (seq 5) ICD-10 `I340`: Nonrheumatic mitral (valve) insufficiency

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-10 | `C73` | Malignant neoplasm of thyroid gland |
| 2 | ICD-10 | `N319` | Neuromuscular dysfunction of bladder, unspecified |
| 3 | ICD-10 | `I480` | Paroxysmal atrial fibrillation |
| 4 | ICD-10 | `Z7902` | Long term (current) use of antithrombotics/antiplatelets |
| 5 | ICD-10 | `I340` | Nonrheumatic mitral (valve) insufficiency |
| 6 | ICD-10 | `I272` | Other secondary pulmonary hypertension |
| 7 | ICD-10 | `I10` | Essential (primary) hypertension |
| 8 | ICD-10 | `E785` | Hyperlipidemia, unspecified |
| 9 | ICD-10 | `E119` | Type 2 diabetes mellitus without complications |
| 10 | ICD-10 | `J449` | Chronic obstructive pulmonary disease, unspecified |
| 11 | ICD-10 | `F17210` | Nicotine dependence, cigarettes, uncomplicated |
| 12 | ICD-10 | `I739` | Peripheral vascular disease, unspecified |
| 13 | ICD-10 | `Z95820` | Peripheral vascular angioplasty status with implants and grafts |
| 14 | ICD-10 | `Z8673` | Personal history of transient ischemic attack (TIA), and cerebral infarction without residual deficits |
| 15 | ICD-10 | `Z86718` | Personal history of other venous thrombosis and embolism |
| 16 | ICD-10 | `Z86711` | Personal history of pulmonary embolism |

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
| 2177-11-03 09:30:00 | Admission | Admitted from PHYSICIAN REFERRAL (DIRECT OBSERVATION) |
| 2177-11-04 15:06:00 | Discharge | To N/A |

## 10. Missing / Ambiguous Data

- No ED registration time — admission may not have gone through ED.
- Discharge location not recorded.
- No procedure ICD codes — procedures may not have been coded or were minor.
- No ICU stay — patient managed on floor/step-down only.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
