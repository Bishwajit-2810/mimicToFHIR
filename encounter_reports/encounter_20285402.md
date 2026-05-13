# Encounter Report — HADM 20285402

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 20285402 |
| Subject ID | 10007795 |
| Patient Sex | F |
| Patient Anchor Age (at anchor year) | 53 |
| Anchor Year | 2136 |
| Admission Time | 2136-08-04 22:16:00 |
| Discharge Time | 2136-08-11 19:20:00 |
| Admission Type | EW EMER. |
| Admission Location | EMERGENCY ROOM |
| Discharge Location | HOME HEALTH CARE |
| Insurance | Medicare |
| Language | ENGLISH |
| Marital Status | SINGLE |
| Race/Ethnicity | WHITE |
| ED Registration | 2136-08-04 16:26:00 |
| ED Departure | 2136-08-05 00:17:00 |
| In-Hospital Mortality | No |
| Date of Death (overall) | N/A |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| HCFA | 372 | MAJOR GASTROINTESTINAL DISORDERS & PERITONEAL INFECTIONS W CC | N/A | N/A |
| APR | 248 | MAJOR GASTROINTESTINAL & PERITONEAL INFECTIONS | 3.0 | 1.0 |

### Primary Diagnosis (seq_num = 1)

- **ICD-9 00845**: Intestinal infection due to Clostridium difficile

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2136-08-04 22:17:10 | N/A | SURG |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-9 `00845`: Intestinal infection due to Clostridium difficile
- (seq 2) ICD-9 `5772`: Cyst and pseudocyst of pancreas
- (seq 3) ICD-9 `7907`: Bacteremia
- (seq 4) ICD-9 `1179`: Other and unspecified mycoses
- (seq 5) ICD-9 `45385`: Acute venous embolism and thrombosis of subclavian veins

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-9 | `00845` | Intestinal infection due to Clostridium difficile |
| 2 | ICD-9 | `5772` | Cyst and pseudocyst of pancreas |
| 3 | ICD-9 | `7907` | Bacteremia |
| 4 | ICD-9 | `1179` | Other and unspecified mycoses |
| 5 | ICD-9 | `45385` | Acute venous embolism and thrombosis of subclavian veins |
| 6 | ICD-9 | `04109` | Streptococcus infection in conditions classified elsewhere and of unspecified site, other streptococcus |
| 7 | ICD-9 | `27651` | Dehydration |
| 8 | ICD-9 | `4019` | Unspecified essential hypertension |
| 9 | ICD-9 | `2720` | Pure hypercholesterolemia |
| 10 | ICD-9 | `25000` | Diabetes mellitus without mention of complication, type II or unspecified type, not stated as uncontrolled |
| 11 | ICD-9 | `28529` | Anemia of other chronic disease |
| 12 | ICD-9 | `V103` | Personal history of malignant neoplasm of breast |
| 13 | ICD-9 | `V443` | Colostomy status |
| 14 | ICD-9 | `3051` | Tobacco use disorder |

## 5. ICU Stays

_No ICU stay recorded for this admission._

## 6. Escalation / Severity Indicators

_No escalation indicators detected from ICD codes or ICU procedure events._

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2136-08-10 | ICD-9 | `3897` | Central venous catheter placement with guidance |
| 2 | 2136-08-06 | ICD-9 | `966` | Enteral infusion of concentrated nutritional substances |
| 3 | 2136-08-09 | ICD-9 | `3897` | Central venous catheter placement with guidance |


## 8. Critical Findings (Charted Events)

_No critical chart events detected._

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2136-08-04 16:26:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2136-08-04 16:26:00 | Transfer | → Emergency Department (ED) |
| 2136-08-04 22:16:00 | Admission | Admitted from EMERGENCY ROOM (EW EMER.) |
| 2136-08-05 00:17:00 | ED Departure | Left Emergency Dept. |
| 2136-08-05 14:08:12 | Transfer | → Med/Surg (transfer) |
| 2136-08-11 19:20:00 | Discharge | To HOME HEALTH CARE |

## 10. Missing / Ambiguous Data

- No ICU stay — patient managed on floor/step-down only.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
