# Encounter Report — HADM 28335091

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 28335091 |
| Subject ID | 10014354 |
| Patient Sex | M |
| Patient Anchor Age (at anchor year) | 60 |
| Anchor Year | 2146 |
| Admission Time | 2147-04-26 16:44:00 |
| Discharge Time | 2147-04-29 15:30:00 |
| Admission Type | URGENT |
| Admission Location | TRANSFER FROM HOSPITAL |
| Discharge Location | HOME HEALTH CARE |
| Insurance | Other |
| Language | ENGLISH |
| Marital Status | SINGLE |
| Race/Ethnicity | WHITE |
| ED Registration | N/A |
| ED Departure | N/A |
| In-Hospital Mortality | No |
| Date of Death (overall) | N/A |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| APR | 174 | PERCUTANEOUS CORONARY INTERVENTION W AMI | 2.0 | 2.0 |
| HCFA | 247 | PERC CARDIOVASC PROC W DRUG-ELUTING STENT W/O MCC | N/A | N/A |

### Primary Diagnosis (seq_num = 1)

- **ICD-10 I214**: Non-ST elevation (NSTEMI) myocardial infarction

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2147-04-26 16:45:47 | N/A | CMED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-10 `I214`: Non-ST elevation (NSTEMI) myocardial infarction
- (seq 2) ICD-10 `C9110`: Chronic lymphocytic leukemia of B-cell type not having achieved remission
- (seq 3) ICD-10 `E119`: Type 2 diabetes mellitus without complications
- (seq 4) ICD-10 `I10`: Essential (primary) hypertension
- (seq 5) ICD-10 `E785`: Hyperlipidemia, unspecified

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-10 | `I214` | Non-ST elevation (NSTEMI) myocardial infarction |
| 2 | ICD-10 | `C9110` | Chronic lymphocytic leukemia of B-cell type not having achieved remission |
| 3 | ICD-10 | `E119` | Type 2 diabetes mellitus without complications |
| 4 | ICD-10 | `I10` | Essential (primary) hypertension |
| 5 | ICD-10 | `E785` | Hyperlipidemia, unspecified |
| 6 | ICD-10 | `F329` | Major depressive disorder, single episode, unspecified |
| 7 | ICD-10 | `G3184` | Mild cognitive impairment, so stated |
| 8 | ICD-10 | `I2510` | Atherosclerotic heart disease of native coronary artery without angina pectoris |
| 9 | ICD-10 | `G4733` | Obstructive sleep apnea (adult) (pediatric) |
| 10 | ICD-10 | `Z7902` | Long term (current) use of antithrombotics/antiplatelets |
| 11 | ICD-10 | `M719` | Bursopathy, unspecified |

## 5. ICU Stays

_No ICU stay recorded for this admission._

## 6. Escalation / Severity Indicators

_No escalation indicators detected from ICD codes or ICU procedure events._

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2147-04-28 | ICD-10 | `027134Z` | Dilation of Coronary Artery, Two Arteries with Drug-eluting Intraluminal Device, Percutaneous Approach |
| 2 | 2147-04-28 | ICD-10 | `B211YZZ` | Fluoroscopy of Multiple Coronary Arteries using Other Contrast |
| 3 | 2147-04-26 | ICD-10 | `B211YZZ` | Fluoroscopy of Multiple Coronary Arteries using Other Contrast |


## 8. Critical Findings (Charted Events)

_No critical chart events detected._

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2147-04-26 16:44:00 | Admission | Admitted from TRANSFER FROM HOSPITAL (URGENT) |
| 2147-04-26 19:55:10 | Transfer | → Cardiac Surgery (transfer) |
| 2147-04-29 15:30:00 | Discharge | To HOME HEALTH CARE |

## 10. Missing / Ambiguous Data

- No ED registration time — admission may not have gone through ED.
- No ICU stay — patient managed on floor/step-down only.

## 11. Manual Review Recommendation

**This encounter is flagged for manual review:**

- Urgent/Emergency admission but no clear escalation indicator found.
