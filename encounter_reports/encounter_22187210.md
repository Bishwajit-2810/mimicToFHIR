# Encounter Report — HADM 22187210

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 22187210 |
| Subject ID | 10004235 |
| Patient Sex | M |
| Patient Anchor Age (at anchor year) | 47 |
| Anchor Year | 2196 |
| Admission Time | 2196-06-20 21:11:00 |
| Discharge Time | 2196-06-22 13:30:00 |
| Admission Type | DIRECT EMER. |
| Admission Location | PHYSICIAN REFERRAL |
| Discharge Location | HOME HEALTH CARE |
| Insurance | Medicaid |
| Language | ENGLISH |
| Marital Status | SINGLE |
| Race/Ethnicity | BLACK/CAPE VERDEAN |
| ED Registration | N/A |
| ED Departure | N/A |
| In-Hospital Mortality | No |
| Date of Death (overall) | N/A |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| HCFA | 864 | FEVER | N/A | N/A |
| APR | 722 | FEVER | 2.0 | 1.0 |

### Primary Diagnosis (seq_num = 1)

- **ICD-9 78062**: Postprocedural fever

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2196-06-20 21:12:18 | N/A | SURG |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-9 `78062`: Postprocedural fever
- (seq 2) ICD-9 `V1253`: Personal history of sudden cardiac arrest
- (seq 3) ICD-9 `29900`: Autistic disorder, current or active state
- (seq 4) ICD-9 `4019`: Unspecified essential hypertension
- (seq 5) ICD-9 `V5861`: Long-term (current) use of anticoagulants

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-9 | `78062` | Postprocedural fever |
| 2 | ICD-9 | `V1253` | Personal history of sudden cardiac arrest |
| 3 | ICD-9 | `29900` | Autistic disorder, current or active state |
| 4 | ICD-9 | `4019` | Unspecified essential hypertension |
| 5 | ICD-9 | `V5861` | Long-term (current) use of anticoagulants |
| 6 | ICD-9 | `42731` | Atrial fibrillation |

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
| 2196-06-20 21:11:00 | Admission | Admitted from PHYSICIAN REFERRAL (DIRECT EMER.) |
| 2196-06-21 17:54:26 | Transfer | → Transplant (transfer) |
| 2196-06-22 13:30:00 | Discharge | To HOME HEALTH CARE |

## 10. Missing / Ambiguous Data

- No ED registration time — admission may not have gone through ED.
- No procedure ICD codes — procedures may not have been coded or were minor.
- No ICU stay — patient managed on floor/step-down only.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
