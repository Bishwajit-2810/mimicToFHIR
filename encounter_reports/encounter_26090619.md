# Encounter Report — HADM 26090619

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 26090619 |
| Subject ID | 10003400 |
| Patient Sex | F |
| Patient Anchor Age (at anchor year) | 72 |
| Anchor Year | 2134 |
| Admission Time | 2134-06-06 02:25:00 |
| Discharge Time | 2134-06-07 15:05:00 |
| Admission Type | EW EMER. |
| Admission Location | EMERGENCY ROOM |
| Discharge Location | HOME HEALTH CARE |
| Insurance | Medicare |
| Language | ENGLISH |
| Marital Status | MARRIED |
| Race/Ethnicity | BLACK/AFRICAN AMERICAN |
| ED Registration | 2134-06-05 21:42:00 |
| ED Departure | 2134-06-06 03:44:00 |
| In-Hospital Mortality | No |
| Date of Death (overall) | 2137-09-02 |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| APR | 468 | OTHER KIDNEY & URINARY TRACT DIAGNOSES, SIGNS & SYMPTOMS | 1.0 | 2.0 |
| HCFA | 696 | KIDNEY & URINARY TRACT SIGNS & SYMPTOMS W/O MCC | N/A | N/A |

### Primary Diagnosis (seq_num = 1)

- **ICD-9 59972**: Microscopic hematuria

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2134-06-06 02:26:44 | N/A | MED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-9 `59972`: Microscopic hematuria
- (seq 2) ICD-9 `20300`: Multiple myeloma, without mention of having achieved remission
- (seq 3) ICD-9 `E9342`: Anticoagulants causing adverse effects in therapeutic use
- (seq 4) ICD-9 `42731`: Atrial fibrillation
- (seq 5) ICD-9 `4019`: Unspecified essential hypertension

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-9 | `59972` | Microscopic hematuria |
| 2 | ICD-9 | `20300` | Multiple myeloma, without mention of having achieved remission |
| 3 | ICD-9 | `E9342` | Anticoagulants causing adverse effects in therapeutic use |
| 4 | ICD-9 | `42731` | Atrial fibrillation |
| 5 | ICD-9 | `4019` | Unspecified essential hypertension |
| 6 | ICD-9 | `27800` | Obesity, unspecified |
| 7 | ICD-9 | `V5861` | Long-term (current) use of anticoagulants |
| 8 | ICD-9 | `7919` | Other nonspecific findings on examination of urine |

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
| 2134-06-05 21:42:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2134-06-05 21:42:00 | Transfer | → Emergency Department (ED) |
| 2134-06-06 02:25:00 | Admission | Admitted from EMERGENCY ROOM (EW EMER.) |
| 2134-06-06 03:44:00 | ED Departure | Left Emergency Dept. |
| 2134-06-07 15:05:00 | Discharge | To HOME HEALTH CARE |

## 10. Missing / Ambiguous Data

- No procedure ICD codes — procedures may not have been coded or were minor.
- No ICU stay — patient managed on floor/step-down only.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
