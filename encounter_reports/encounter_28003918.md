# Encounter Report — HADM 28003918

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 28003918 |
| Subject ID | 10019003 |
| Patient Sex | F |
| Patient Anchor Age (at anchor year) | 65 |
| Anchor Year | 2148 |
| Admission Time | 2148-12-21 07:15:00 |
| Discharge Time | 2148-12-24 17:10:00 |
| Admission Type | ELECTIVE |
| Admission Location | PHYSICIAN REFERRAL |
| Discharge Location | HOME |
| Insurance | Medicare |
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
| HCFA | 743 | UTERINE & ADNEXA PROC FOR NON-MALIGNANCY W/O CC/MCC | N/A | N/A |
| APR | 513 | UTERINE & ADNEXA PROCEDURES FOR NON-MALIGNANCY EXCEPT LEIOMYOMA | 2.0 | 1.0 |

### Primary Diagnosis (seq_num = 1)

- **ICD-9 6202**: Other and unspecified ovarian cyst

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2148-12-21 03:32:53 | N/A | GYN |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-9 `6202`: Other and unspecified ovarian cyst
- (seq 2) ICD-9 `25000`: Diabetes mellitus without mention of complication, type II or unspecified type, not stated as uncontrolled
- (seq 3) ICD-9 `4019`: Unspecified essential hypertension
- (seq 4) ICD-9 `2724`: Other and unspecified hyperlipidemia
- (seq 5) ICD-9 `4928`: Other emphysema

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-9 | `6202` | Other and unspecified ovarian cyst |
| 2 | ICD-9 | `25000` | Diabetes mellitus without mention of complication, type II or unspecified type, not stated as uncontrolled |
| 3 | ICD-9 | `4019` | Unspecified essential hypertension |
| 4 | ICD-9 | `2724` | Other and unspecified hyperlipidemia |
| 5 | ICD-9 | `4928` | Other emphysema |
| 6 | ICD-9 | `311` | Depressive disorder, not elsewhere classified |
| 7 | ICD-9 | `V103` | Personal history of malignant neoplasm of breast |

## 5. ICU Stays

_No ICU stay recorded for this admission._

## 6. Escalation / Severity Indicators

_No escalation indicators detected from ICD codes or ICU procedure events._

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2148-12-21 | ICD-9 | `6563` | Laparoscopic removal of both ovaries and tubes at same operative episode |
| 2 | 2148-12-21 | ICD-9 | `6841` | Laparoscopic total abdominal hysterectomy |
| 3 | 2148-12-21 | ICD-9 | `5732` | Other cystoscopy |


## 8. Critical Findings (Charted Events)

_No critical chart events detected._

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2148-12-21 07:15:00 | Admission | Admitted from PHYSICIAN REFERRAL (ELECTIVE) |
| 2148-12-21 17:43:31 | Transfer | → Med/Surg/GYN (transfer) |
| 2148-12-24 17:10:00 | Discharge | To HOME |

## 10. Missing / Ambiguous Data

- No ED registration time — admission may not have gone through ED.
- No ICU stay — patient managed on floor/step-down only.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
