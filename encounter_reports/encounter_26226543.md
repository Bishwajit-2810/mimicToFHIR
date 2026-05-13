# Encounter Report — HADM 26226543

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 26226543 |
| Subject ID | 10019003 |
| Patient Sex | F |
| Patient Anchor Age (at anchor year) | 65 |
| Anchor Year | 2148 |
| Admission Time | 2155-10-17 18:01:00 |
| Discharge Time | 2155-11-03 18:00:00 |
| Admission Type | ELECTIVE |
| Admission Location | PHYSICIAN REFERRAL |
| Discharge Location | HOME HEALTH CARE |
| Insurance | Other |
| Language | ENGLISH |
| Marital Status | WIDOWED |
| Race/Ethnicity | WHITE |
| ED Registration | N/A |
| ED Departure | N/A |
| In-Hospital Mortality | No |
| Date of Death (overall) | 2155-12-03 |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| APR | 194 | HEART FAILURE | 3.0 | 4.0 |
| HCFA | 291 | HEART FAILURE & SHOCK W MCC | N/A | N/A |

### Primary Diagnosis (seq_num = 1)

- **ICD-10 I110**: Hypertensive heart disease with heart failure

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2155-10-17 18:02:26 | N/A | OMED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-10 `I110`: Hypertensive heart disease with heart failure
- (seq 2) ICD-10 `J9601`: Acute respiratory failure with hypoxia
- (seq 3) ICD-10 `N390`: Urinary tract infection, site not specified
- (seq 4) ICD-10 `N179`: Acute kidney failure, unspecified
- (seq 5) ICD-10 `I5033`: Acute on chronic diastolic (congestive) heart failure

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-10 | `I110` | Hypertensive heart disease with heart failure |
| 2 | ICD-10 | `J9601` | Acute respiratory failure with hypoxia |
| 3 | ICD-10 | `N390` | Urinary tract infection, site not specified |
| 4 | ICD-10 | `N179` | Acute kidney failure, unspecified |
| 5 | ICD-10 | `I5033` | Acute on chronic diastolic (congestive) heart failure |
| 6 | ICD-10 | `R161` | Splenomegaly, not elsewhere classified |
| 7 | ICD-10 | `D469` | Myelodysplastic syndrome, unspecified |
| 8 | ICD-10 | `J449` | Chronic obstructive pulmonary disease, unspecified |
| 9 | ICD-10 | `E039` | Hypothyroidism, unspecified |
| 10 | ICD-10 | `E119` | Type 2 diabetes mellitus without complications |
| 11 | ICD-10 | `D696` | Thrombocytopenia, unspecified |
| 12 | ICD-10 | `Y842` | Radiological procedure and radiotherapy as the cause of abnormal reaction of the patient, or of later complication, without mention of misadventure at the time of the procedure |
| 13 | ICD-10 | `Z853` | Personal history of malignant neoplasm of breast |
| 14 | ICD-10 | `K7581` | Nonalcoholic steatohepatitis (NASH) |
| 15 | ICD-10 | `E7800` | Pure hypercholesterolemia, unspecified |
| 16 | ICD-10 | `Z87891` | Personal history of nicotine dependence |
| 17 | ICD-10 | `D649` | Anemia, unspecified |
| 18 | ICD-10 | `K219` | Gastro-esophageal reflux disease without esophagitis |
| 19 | ICD-10 | `B009` | Herpesviral infection, unspecified |
| 20 | ICD-10 | `B961` | Klebsiella pneumoniae [K. pneumoniae] as the cause of diseases classified elsewhere |
| 21 | ICD-10 | `Z1611` | Resistance to penicillins |
| 22 | ICD-10 | `E876` | Hypokalemia |
| 23 | ICD-10 | `F329` | Major depressive disorder, single episode, unspecified |
| 24 | ICD-10 | `E790` | Hyperuricemia without signs of inflammatory arthritis and tophaceous disease |
| 25 | ICD-10 | `R109` | Unspecified abdominal pain |

## 5. ICU Stays

_No ICU stay recorded for this admission._

## 6. Escalation / Severity Indicators

The following critical conditions or interventions were detected:

- **Acute Kidney Injury** (ICD diagnosis)
- **Respiratory Failure** (ICD diagnosis)

## 7. Procedures and Interventions

_No ICD-coded procedures recorded._


## 8. Critical Findings (Charted Events)

_No critical chart events detected._

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2155-10-17 18:01:00 | Admission | Admitted from PHYSICIAN REFERRAL (ELECTIVE) |
| 2155-10-18 19:05:30 | Transfer | → Hematology/Oncology Intermediate (transfer) |
| 2155-11-03 18:00:00 | Discharge | To HOME HEALTH CARE |

## 10. Missing / Ambiguous Data

- No ED registration time — admission may not have gone through ED.
- No procedure ICD codes — procedures may not have been coded or were minor.
- No ICU stay — patient managed on floor/step-down only.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
