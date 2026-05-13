# Encounter Report — HADM 21216581

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 21216581 |
| Subject ID | 10004457 |
| Patient Sex | M |
| Patient Anchor Age (at anchor year) | 65 |
| Anchor Year | 2140 |
| Admission Time | 2143-03-09 11:10:00 |
| Discharge Time | 2143-03-10 11:35:00 |
| Admission Type | AMBULATORY OBSERVATION |
| Admission Location | PROCEDURE SITE |
| Discharge Location | N/A |
| Insurance | Medicare |
| Language | ENGLISH |
| Marital Status | DIVORCED |
| Race/Ethnicity | WHITE |
| ED Registration | N/A |
| ED Departure | N/A |
| In-Hospital Mortality | No |
| Date of Death (overall) | N/A |

## 2. Hospital Visit Reason

### Primary Diagnosis (seq_num = 1)

- **ICD-9 42732**: Atrial flutter

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2143-03-09 11:11:33 | N/A | CMED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-9 `42732`: Atrial flutter
- (seq 2) ICD-9 `41400`: Coronary atherosclerosis of unspecified type of vessel, native or graft
- (seq 3) ICD-9 `20190`: Hodgkin's disease, unspecified type, unspecified site, extranodal and solid organ sites
- (seq 4) ICD-9 `V1254`: Personal history of transient ischemic attack (TIA), and cerebral infarction without residual deficits
- (seq 5) ICD-9 `V4581`: Aortocoronary bypass status

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-9 | `42732` | Atrial flutter |
| 2 | ICD-9 | `41400` | Coronary atherosclerosis of unspecified type of vessel, native or graft |
| 3 | ICD-9 | `20190` | Hodgkin's disease, unspecified type, unspecified site, extranodal and solid organ sites |
| 4 | ICD-9 | `V1254` | Personal history of transient ischemic attack (TIA), and cerebral infarction without residual deficits |
| 5 | ICD-9 | `V4581` | Aortocoronary bypass status |
| 6 | ICD-9 | `V4582` | Percutaneous transluminal coronary angioplasty status |
| 7 | ICD-9 | `V5861` | Long-term (current) use of anticoagulants |
| 8 | ICD-9 | `V5866` | Long-term (current) use of aspirin |
| 9 | ICD-9 | `V1046` | Personal history of malignant neoplasm of prostate |
| 10 | ICD-9 | `V422` | Heart valve replaced by transplant |

## 5. ICU Stays

_No ICU stay recorded for this admission._

## 6. Escalation / Severity Indicators

_No escalation indicators detected from ICD codes or ICU procedure events._

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2143-03-09 | ICD-9 | `3734` | Excision or destruction of other lesion or tissue of heart, endovascular approach |
| 2 | 2143-03-09 | ICD-9 | `3727` | Cardiac mapping |


## 8. Critical Findings (Charted Events)

_No critical chart events detected._

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2143-03-09 11:10:00 | Admission | Admitted from PROCEDURE SITE (AMBULATORY OBSERVATION) |
| 2143-03-09 16:25:33 | Transfer | → Medicine/Cardiology (transfer) |
| 2143-03-10 11:35:00 | Discharge | To N/A |

## 10. Missing / Ambiguous Data

- No ED registration time — admission may not have gone through ED.
- Discharge location not recorded.
- No ICU stay — patient managed on floor/step-down only.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
