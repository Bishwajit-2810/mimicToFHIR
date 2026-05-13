# Encounter Report — HADM 22484749

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 22484749 |
| Subject ID | 10039997 |
| Patient Sex | F |
| Patient Anchor Age (at anchor year) | 67 |
| Anchor Year | 2134 |
| Admission Time | 2137-03-15 22:08:00 |
| Discharge Time | 2137-03-18 16:34:00 |
| Admission Type | OBSERVATION ADMIT |
| Admission Location | PHYSICIAN REFERRAL |
| Discharge Location | REHAB |
| Insurance | Medicare |
| Language | ENGLISH |
| Marital Status | WIDOWED |
| Race/Ethnicity | BLACK/AFRICAN AMERICAN |
| ED Registration | 2137-03-15 15:27:00 |
| ED Departure | 2137-03-16 00:11:00 |
| In-Hospital Mortality | No |
| Date of Death (overall) | N/A |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| APR | 45 | CVA & PRECEREBRAL OCCLUSION W INFARCT | 2.0 | 2.0 |
| HCFA | 65 | INTRACRANIAL HEMORRHAGE OR CEREBRAL INFARCTION W CC OR TPA IN 24 HRS | N/A | N/A |

### Primary Diagnosis (seq_num = 1)

- **ICD-10 I6340**: Cerebral infarction due to embolism of unspecified cerebral artery

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2137-03-15 22:08:46 | N/A | NMED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-10 `I6340`: Cerebral infarction due to embolism of unspecified cerebral artery
- (seq 2) ICD-10 `I69354`: Hemiplegia and hemiparesis following cerebral infarction affecting left non-dominant side
- (seq 3) ICD-10 `D696`: Thrombocytopenia, unspecified
- (seq 4) ICD-10 `I480`: Paroxysmal atrial fibrillation
- (seq 5) ICD-10 `G8191`: Hemiplegia, unspecified affecting right dominant side

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-10 | `I6340` | Cerebral infarction due to embolism of unspecified cerebral artery |
| 2 | ICD-10 | `I69354` | Hemiplegia and hemiparesis following cerebral infarction affecting left non-dominant side |
| 3 | ICD-10 | `D696` | Thrombocytopenia, unspecified |
| 4 | ICD-10 | `I480` | Paroxysmal atrial fibrillation |
| 5 | ICD-10 | `G8191` | Hemiplegia, unspecified affecting right dominant side |
| 6 | ICD-10 | `I129` | Hypertensive chronic kidney disease with stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease |
| 7 | ICD-10 | `I69392` | Facial weakness following cerebral infarction |
| 8 | ICD-10 | `N189` | Chronic kidney disease, unspecified |
| 9 | ICD-10 | `I69893` | Ataxia following other cerebrovascular disease |
| 10 | ICD-10 | `E785` | Hyperlipidemia, unspecified |
| 11 | ICD-10 | `D72819` | Decreased white blood cell count, unspecified |
| 12 | ICD-10 | `R2681` | Unsteadiness on feet |
| 13 | ICD-10 | `F17210` | Nicotine dependence, cigarettes, uncomplicated |
| 14 | ICD-10 | `F329` | Major depressive disorder, single episode, unspecified |
| 15 | ICD-10 | `Z9181` | History of falling |

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
| 2137-03-15 15:27:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2137-03-15 15:27:00 | Transfer | → Emergency Department (ED) |
| 2137-03-15 22:08:00 | Admission | Admitted from PHYSICIAN REFERRAL (OBSERVATION ADMIT) |
| 2137-03-15 22:20:19 | Transfer | → Medicine/Cardiology (transfer) |
| 2137-03-16 00:11:00 | ED Departure | Left Emergency Dept. |
| 2137-03-18 16:34:00 | Discharge | To REHAB |

## 10. Missing / Ambiguous Data

- No procedure ICD codes — procedures may not have been coded or were minor.
- No ICU stay — patient managed on floor/step-down only.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
