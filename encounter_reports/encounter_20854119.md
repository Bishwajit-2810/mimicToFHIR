# Encounter Report — HADM 20854119

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 20854119 |
| Subject ID | 10015860 |
| Patient Sex | M |
| Patient Anchor Age (at anchor year) | 53 |
| Anchor Year | 2186 |
| Admission Time | 2188-08-06 00:49:00 |
| Discharge Time | 2188-08-12 17:49:00 |
| Admission Type | EW EMER. |
| Admission Location | EMERGENCY ROOM |
| Discharge Location | HOME HEALTH CARE |
| Insurance | Other |
| Language | ENGLISH |
| Marital Status | SINGLE |
| Race/Ethnicity | WHITE |
| ED Registration | 2188-08-05 20:36:00 |
| ED Departure | 2188-08-06 03:24:00 |
| In-Hospital Mortality | No |
| Date of Death (overall) | N/A |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| HCFA | 628 | OTHER ENDOCRINE, NUTRIT & METAB O.R. PROC W MCC | N/A | N/A |
| APR | 320 | OTHER MUSCULOSKELETAL SYSTEM & CONNECTIVE TISSUE PROCEDURES | 3.0 | 3.0 |

### Primary Diagnosis (seq_num = 1)

- **ICD-9 25082**: Diabetes with other specified manifestations, type II or unspecified type, uncontrolled

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2188-08-06 00:49:59 | N/A | MED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-9 `25082`: Diabetes with other specified manifestations, type II or unspecified type, uncontrolled
- (seq 2) ICD-9 `0380`: Streptococcal septicemia
- (seq 3) ICD-9 `99591`: Sepsis
- (seq 4) ICD-9 `25062`: Diabetes with neurological manifestations, type II or unspecified type, uncontrolled
- (seq 5) ICD-9 `70715`: Ulcer of other part of foot

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-9 | `25082` | Diabetes with other specified manifestations, type II or unspecified type, uncontrolled |
| 2 | ICD-9 | `0380` | Streptococcal septicemia |
| 3 | ICD-9 | `99591` | Sepsis |
| 4 | ICD-9 | `25062` | Diabetes with neurological manifestations, type II or unspecified type, uncontrolled |
| 5 | ICD-9 | `70715` | Ulcer of other part of foot |
| 6 | ICD-9 | `73027` | Unspecified osteomyelitis, ankle and foot |
| 7 | ICD-9 | `7318` | Other bone involvement in diseases classified elsewhere |
| 8 | ICD-9 | `5849` | Acute kidney failure, unspecified |
| 9 | ICD-9 | `5853` | Chronic kidney disease, Stage III (moderate) |
| 10 | ICD-9 | `04111` | Methicillin susceptible Staphylococcus aureus in conditions classified elsewhere and of unspecified site |
| 11 | ICD-9 | `40390` | Hypertensive chronic kidney disease, unspecified, with chronic kidney disease stage I through stage IV, or unspecified |
| 12 | ICD-9 | `2859` | Anemia, unspecified |
| 13 | ICD-9 | `27800` | Obesity, unspecified |
| 14 | ICD-9 | `2720` | Pure hypercholesterolemia |
| 15 | ICD-9 | `V5866` | Long-term (current) use of aspirin |
| 16 | ICD-9 | `V0481` | Need for prophylactic vaccination and inoculation against influenza |
| 17 | ICD-9 | `V180` | Family history of diabetes mellitus |

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
| 1 | 2188-08-07 | ICD-9 | `7769` | Local excision of lesion or tissue of bone, other bones |
| 2 | 2188-08-09 | ICD-9 | `7769` | Local excision of lesion or tissue of bone, other bones |
| 3 | 2188-08-05 | ICD-9 | `8604` | Other incision with drainage of skin and subcutaneous tissue |
| 4 | 2188-08-12 | ICD-9 | `3893` | Venous catheterization, not elsewhere classified |


## 8. Critical Findings (Charted Events)

_No critical chart events detected._

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2188-08-05 20:36:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2188-08-05 20:36:00 | Transfer | → Emergency Department (ED) |
| 2188-08-06 00:49:00 | Admission | Admitted from EMERGENCY ROOM (EW EMER.) |
| 2188-08-06 03:24:00 | ED Departure | Left Emergency Dept. |
| 2188-08-10 16:33:00 | Transfer | → Medicine (transfer) |
| 2188-08-12 17:49:00 | Discharge | To HOME HEALTH CARE |

## 10. Missing / Ambiguous Data

- No ICU stay — patient managed on floor/step-down only.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
