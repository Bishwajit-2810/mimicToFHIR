# Encounter Report — HADM 27962747

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 27962747 |
| Subject ID | 10007795 |
| Patient Sex | F |
| Patient Anchor Age (at anchor year) | 53 |
| Anchor Year | 2136 |
| Admission Time | 2136-07-24 17:15:00 |
| Discharge Time | 2136-07-27 14:27:00 |
| Admission Type | DIRECT OBSERVATION |
| Admission Location | PHYSICIAN REFERRAL |
| Discharge Location | N/A |
| Insurance | Medicare |
| Language | ENGLISH |
| Marital Status | SINGLE |
| Race/Ethnicity | WHITE |
| ED Registration | N/A |
| ED Departure | N/A |
| In-Hospital Mortality | No |
| Date of Death (overall) | N/A |

## 2. Hospital Visit Reason

### Primary Diagnosis (seq_num = 1)

- **ICD-9 5772**: Cyst and pseudocyst of pancreas

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2136-07-24 17:16:17 | N/A | SURG |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-9 `5772`: Cyst and pseudocyst of pancreas
- (seq 2) ICD-9 `V443`: Colostomy status
- (seq 3) ICD-9 `78321`: Loss of weight
- (seq 4) ICD-9 `56400`: Constipation, unspecified
- (seq 5) ICD-9 `4019`: Unspecified essential hypertension

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-9 | `5772` | Cyst and pseudocyst of pancreas |
| 2 | ICD-9 | `V443` | Colostomy status |
| 3 | ICD-9 | `78321` | Loss of weight |
| 4 | ICD-9 | `56400` | Constipation, unspecified |
| 5 | ICD-9 | `4019` | Unspecified essential hypertension |
| 6 | ICD-9 | `V1279` | Personal history of other diseases of digestive system |
| 7 | ICD-9 | `25000` | Diabetes mellitus without mention of complication, type II or unspecified type, not stated as uncontrolled |
| 8 | ICD-9 | `28529` | Anemia of other chronic disease |
| 9 | ICD-9 | `V103` | Personal history of malignant neoplasm of breast |
| 10 | ICD-9 | `2720` | Pure hypercholesterolemia |
| 11 | ICD-9 | `V851` | Body Mass Index between 19-24, adult |
| 12 | ICD-9 | `3051` | Tobacco use disorder |

## 5. ICU Stays

_No ICU stay recorded for this admission._

## 6. Escalation / Severity Indicators

_No escalation indicators detected from ICD codes or ICU procedure events._

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2136-07-24 | ICD-9 | `966` | Enteral infusion of concentrated nutritional substances |


## 8. Critical Findings (Charted Events)

_No critical chart events detected._

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2136-07-24 17:15:00 | Admission | Admitted from PHYSICIAN REFERRAL (DIRECT OBSERVATION) |
| 2136-07-25 04:06:33 | Transfer | → Med/Surg (transfer) |
| 2136-07-25 14:38:59 | Transfer | → Med/Surg (transfer) |
| 2136-07-25 14:39:30 | Transfer | → Med/Surg (transfer) |
| 2136-07-27 14:27:00 | Discharge | To N/A |

## 10. Missing / Ambiguous Data

- No ED registration time — admission may not have gone through ED.
- Discharge location not recorded.
- No ICU stay — patient managed on floor/step-down only.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
