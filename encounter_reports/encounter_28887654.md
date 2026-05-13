# Encounter Report — HADM 28887654

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 28887654 |
| Subject ID | 10023117 |
| Patient Sex | M |
| Patient Anchor Age (at anchor year) | 53 |
| Anchor Year | 2170 |
| Admission Time | 2174-12-16 13:25:00 |
| Discharge Time | 2174-12-20 10:27:00 |
| Admission Type | DIRECT EMER. |
| Admission Location | PHYSICIAN REFERRAL |
| Discharge Location | HOME |
| Insurance | Medicare |
| Language | ENGLISH |
| Marital Status | WIDOWED |
| Race/Ethnicity | WHITE |
| ED Registration | N/A |
| ED Departure | N/A |
| In-Hospital Mortality | No |
| Date of Death (overall) | 2175-07-20 |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| APR | 194 | HEART FAILURE | 2.0 | 2.0 |
| HCFA | 292 | HEART FAILURE & SHOCK W CC | N/A | N/A |

### Primary Diagnosis (seq_num = 1)

- **ICD-10 I5023**: Acute on chronic systolic (congestive) heart failure

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2174-12-16 13:25:48 | N/A | CMED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-10 `I5023`: Acute on chronic systolic (congestive) heart failure
- (seq 2) ICD-10 `I427`: Cardiomyopathy due to drug and external agent
- (seq 3) ICD-10 `I272`: Other secondary pulmonary hypertension
- (seq 4) ICD-10 `F200`: Paranoid schizophrenia
- (seq 5) ICD-10 `T43505S`: Adverse effect of unspecified antipsychotics and neuroleptics, sequela

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-10 | `I5023` | Acute on chronic systolic (congestive) heart failure |
| 2 | ICD-10 | `I427` | Cardiomyopathy due to drug and external agent |
| 3 | ICD-10 | `I272` | Other secondary pulmonary hypertension |
| 4 | ICD-10 | `F200` | Paranoid schizophrenia |
| 5 | ICD-10 | `T43505S` | Adverse effect of unspecified antipsychotics and neuroleptics, sequela |
| 6 | ICD-10 | `I081` | Rheumatic disorders of both mitral and tricuspid valves |
| 7 | ICD-10 | `I129` | Hypertensive chronic kidney disease with stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease |
| 8 | ICD-10 | `N189` | Chronic kidney disease, unspecified |
| 9 | ICD-10 | `Z87891` | Personal history of nicotine dependence |
| 10 | ICD-10 | `Z95810` | Presence of automatic (implantable) cardiac defibrillator |
| 11 | ICD-10 | `F329` | Major depressive disorder, single episode, unspecified |
| 12 | ICD-10 | `E785` | Hyperlipidemia, unspecified |
| 13 | ICD-10 | `Z85528` | Personal history of other malignant neoplasm of kidney |
| 14 | ICD-10 | `K219` | Gastro-esophageal reflux disease without esophagitis |
| 15 | ICD-10 | `K2270` | Barrett's esophagus without dysplasia |
| 16 | ICD-10 | `Z8249` | Family history of ischemic heart disease and other diseases of the circulatory system |
| 17 | ICD-10 | `F419` | Anxiety disorder, unspecified |
| 18 | ICD-10 | `D649` | Anemia, unspecified |

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
| 2174-12-16 13:25:00 | Admission | Admitted from PHYSICIAN REFERRAL (DIRECT EMER.) |
| 2174-12-20 10:27:00 | Discharge | To HOME |

## 10. Missing / Ambiguous Data

- No ED registration time — admission may not have gone through ED.
- No procedure ICD codes — procedures may not have been coded or were minor.
- No ICU stay — patient managed on floor/step-down only.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
