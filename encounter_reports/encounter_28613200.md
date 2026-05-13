# Encounter Report — HADM 28613200

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 28613200 |
| Subject ID | 10015860 |
| Patient Sex | M |
| Patient Anchor Age (at anchor year) | 53 |
| Anchor Year | 2186 |
| Admission Time | 2188-03-29 14:14:00 |
| Discharge Time | 2188-04-02 16:30:00 |
| Admission Type | DIRECT EMER. |
| Admission Location | CLINIC REFERRAL |
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
| APR | 314 | FOOT & TOE PROCEDURES | 2.0 | 2.0 |
| HCFA | 629 | OTHER ENDOCRINE, NUTRIT & METAB O.R. PROC W CC | N/A | N/A |

### Primary Diagnosis (seq_num = 1)

- **ICD-9 25080**: Diabetes with other specified manifestations, type II or unspecified type, not stated as uncontrolled

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2188-03-29 14:14:58 | N/A | SURG |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-9 `25080`: Diabetes with other specified manifestations, type II or unspecified type, not stated as uncontrolled
- (seq 2) ICD-9 `70715`: Ulcer of other part of foot
- (seq 3) ICD-9 `73027`: Unspecified osteomyelitis, ankle and foot
- (seq 4) ICD-9 `25060`: Diabetes with neurological manifestations, type II or unspecified type, not stated as uncontrolled
- (seq 5) ICD-9 `V5867`: Long-term (current) use of insulin

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-9 | `25080` | Diabetes with other specified manifestations, type II or unspecified type, not stated as uncontrolled |
| 2 | ICD-9 | `70715` | Ulcer of other part of foot |
| 3 | ICD-9 | `73027` | Unspecified osteomyelitis, ankle and foot |
| 4 | ICD-9 | `25060` | Diabetes with neurological manifestations, type II or unspecified type, not stated as uncontrolled |
| 5 | ICD-9 | `V5867` | Long-term (current) use of insulin |
| 6 | ICD-9 | `7318` | Other bone involvement in diseases classified elsewhere |
| 7 | ICD-9 | `4019` | Unspecified essential hypertension |
| 8 | ICD-9 | `53081` | Esophageal reflux |

## 5. ICU Stays

_No ICU stay recorded for this admission._

## 6. Escalation / Severity Indicators

_No escalation indicators detected from ICD codes or ICU procedure events._

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2188-03-31 | ICD-9 | `7788` | Other partial ostectomy, tarsals and metatarsals |


## 8. Critical Findings (Charted Events)

_No critical chart events detected._

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2188-03-29 14:14:00 | Admission | Admitted from CLINIC REFERRAL (DIRECT EMER.) |
| 2188-04-02 16:30:00 | Discharge | To HOME HEALTH CARE |

## 10. Missing / Ambiguous Data

- No ED registration time — admission may not have gone through ED.
- No ICU stay — patient managed on floor/step-down only.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
