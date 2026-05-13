# Encounter Report — HADM 28236161

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 28236161 |
| Subject ID | 10015860 |
| Patient Sex | M |
| Patient Anchor Age (at anchor year) | 53 |
| Anchor Year | 2186 |
| Admission Time | 2187-09-15 18:49:00 |
| Discharge Time | 2187-09-19 14:50:00 |
| Admission Type | EW EMER. |
| Admission Location | EMERGENCY ROOM |
| Discharge Location | HOME HEALTH CARE |
| Insurance | Other |
| Language | ENGLISH |
| Marital Status | SINGLE |
| Race/Ethnicity | WHITE |
| ED Registration | 2187-09-15 14:14:00 |
| ED Departure | 2187-09-15 20:49:00 |
| In-Hospital Mortality | No |
| Date of Death (overall) | N/A |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| HCFA | 571 | SKIN DEBRIDEMENT W CC | N/A | N/A |
| APR | 380 | SKIN ULCERS | 2.0 | 1.0 |

### Primary Diagnosis (seq_num = 1)

- **ICD-9 70715**: Ulcer of other part of foot

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2187-09-15 18:49:53 | N/A | SURG |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-9 `70715`: Ulcer of other part of foot
- (seq 2) ICD-9 `6827`: Cellulitis and abscess of foot, except toes
- (seq 3) ICD-9 `25000`: Diabetes mellitus without mention of complication, type II or unspecified type, not stated as uncontrolled
- (seq 4) ICD-9 `4019`: Unspecified essential hypertension
- (seq 5) ICD-9 `2720`: Pure hypercholesterolemia

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-9 | `70715` | Ulcer of other part of foot |
| 2 | ICD-9 | `6827` | Cellulitis and abscess of foot, except toes |
| 3 | ICD-9 | `25000` | Diabetes mellitus without mention of complication, type II or unspecified type, not stated as uncontrolled |
| 4 | ICD-9 | `4019` | Unspecified essential hypertension |
| 5 | ICD-9 | `2720` | Pure hypercholesterolemia |
| 6 | ICD-9 | `V1582` | Personal history of tobacco use |

## 5. ICU Stays

_No ICU stay recorded for this admission._

## 6. Escalation / Severity Indicators

_No escalation indicators detected from ICD codes or ICU procedure events._

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2187-09-15 | ICD-9 | `8622` | Excisional debridement of wound, infection, or burn |


## 8. Critical Findings (Charted Events)

_No critical chart events detected._

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2187-09-15 14:14:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2187-09-15 14:14:00 | Transfer | → Emergency Department (ED) |
| 2187-09-15 18:49:00 | Admission | Admitted from EMERGENCY ROOM (EW EMER.) |
| 2187-09-15 20:49:00 | ED Departure | Left Emergency Dept. |
| 2187-09-19 14:50:00 | Discharge | To HOME HEALTH CARE |

## 10. Missing / Ambiguous Data

- No ICU stay — patient managed on floor/step-down only.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
