# Encounter Report — HADM 20790339

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 20790339 |
| Subject ID | 10015860 |
| Patient Sex | M |
| Patient Anchor Age (at anchor year) | 53 |
| Anchor Year | 2186 |
| Admission Time | 2189-05-23 02:14:00 |
| Discharge Time | 2189-05-25 14:45:00 |
| Admission Type | EW EMER. |
| Admission Location | EMERGENCY ROOM |
| Discharge Location | HOME HEALTH CARE |
| Insurance | Other |
| Language | ENGLISH |
| Marital Status | SINGLE |
| Race/Ethnicity | WHITE |
| ED Registration | 2189-05-22 23:18:00 |
| ED Departure | 2189-05-23 03:38:00 |
| In-Hospital Mortality | No |
| Date of Death (overall) | N/A |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| HCFA | 854 | INFECTIOUS & PARASITIC DISEASES W O.R. PROCEDURE W CC | N/A | N/A |
| APR | 720 | SEPTICEMIA & DISSEMINATED INFECTIONS | 3.0 | 2.0 |

### Primary Diagnosis (seq_num = 1)

- **ICD-9 0389**: Unspecified septicemia

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2189-05-23 02:16:04 | N/A | MED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-9 `0389`: Unspecified septicemia
- (seq 2) ICD-9 `5849`: Acute kidney failure, unspecified
- (seq 3) ICD-9 `25082`: Diabetes with other specified manifestations, type II or unspecified type, uncontrolled
- (seq 4) ICD-9 `25062`: Diabetes with neurological manifestations, type II or unspecified type, uncontrolled
- (seq 5) ICD-9 `5853`: Chronic kidney disease, Stage III (moderate)

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-9 | `0389` | Unspecified septicemia |
| 2 | ICD-9 | `5849` | Acute kidney failure, unspecified |
| 3 | ICD-9 | `25082` | Diabetes with other specified manifestations, type II or unspecified type, uncontrolled |
| 4 | ICD-9 | `25062` | Diabetes with neurological manifestations, type II or unspecified type, uncontrolled |
| 5 | ICD-9 | `5853` | Chronic kidney disease, Stage III (moderate) |
| 6 | ICD-9 | `2761` | Hyposmolality and/or hyponatremia |
| 7 | ICD-9 | `V0481` | Need for prophylactic vaccination and inoculation against influenza |
| 8 | ICD-9 | `70715` | Ulcer of other part of foot |
| 9 | ICD-9 | `V5867` | Long-term (current) use of insulin |
| 10 | ICD-9 | `3572` | Polyneuropathy in diabetes |
| 11 | ICD-9 | `40390` | Hypertensive chronic kidney disease, unspecified, with chronic kidney disease stage I through stage IV, or unspecified |
| 12 | ICD-9 | `2720` | Pure hypercholesterolemia |
| 13 | ICD-9 | `99591` | Sepsis |
| 14 | ICD-9 | `V4972` | Other toe(s) amputation status |
| 15 | ICD-9 | `V5866` | Long-term (current) use of aspirin |
| 16 | ICD-9 | `78701` | Nausea with vomiting |
| 17 | ICD-9 | `42789` | Other specified cardiac dysrhythmias |
| 18 | ICD-9 | `2767` | Hyperpotassemia |

## 5. ICU Stays

_No ICU stay recorded for this admission._

## 6. Escalation / Severity Indicators

The following critical conditions or interventions were detected:

- **Acute Kidney Injury** (ICD diagnosis)
- **Sepsis** (ICD diagnosis)

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2189-05-23 | ICD-9 | `8622` | Excisional debridement of wound, infection, or burn |


## 8. Critical Findings (Charted Events)

_No critical chart events detected._

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2189-05-22 23:18:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2189-05-22 23:18:00 | Transfer | → Emergency Department (ED) |
| 2189-05-23 02:14:00 | Admission | Admitted from EMERGENCY ROOM (EW EMER.) |
| 2189-05-23 03:38:00 | ED Departure | Left Emergency Dept. |
| 2189-05-25 14:45:00 | Discharge | To HOME HEALTH CARE |

## 10. Missing / Ambiguous Data

- No ICU stay — patient managed on floor/step-down only.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
