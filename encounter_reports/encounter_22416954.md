# Encounter Report — HADM 22416954

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 22416954 |
| Subject ID | 10015860 |
| Patient Sex | M |
| Patient Anchor Age (at anchor year) | 53 |
| Anchor Year | 2186 |
| Admission Time | 2193-05-03 22:45:00 |
| Discharge Time | 2193-05-05 02:13:00 |
| Admission Type | EU OBSERVATION |
| Admission Location | TRANSFER FROM HOSPITAL |
| Discharge Location | N/A |
| Insurance | Other |
| Language | ENGLISH |
| Marital Status | SINGLE |
| Race/Ethnicity | WHITE |
| ED Registration | 2193-05-03 19:12:00 |
| ED Departure | 2193-05-05 02:13:00 |
| In-Hospital Mortality | No |
| Date of Death (overall) | N/A |

## 2. Hospital Visit Reason

### Primary Diagnosis (seq_num = 1)

- **ICD-10 R2232**: Localized swelling, mass and lump, left upper limb

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2193-05-03 22:48:05 | N/A | MED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-10 `R2232`: Localized swelling, mass and lump, left upper limb
- (seq 2) ICD-10 `R200`: Anesthesia of skin
- (seq 3) ICD-10 `E1122`: Type 2 diabetes mellitus with diabetic chronic kidney disease
- (seq 4) ICD-10 `I120`: Hypertensive chronic kidney disease with stage 5 chronic kidney disease or end stage renal disease
- (seq 5) ICD-10 `N186`: End stage renal disease

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-10 | `R2232` | Localized swelling, mass and lump, left upper limb |
| 2 | ICD-10 | `R200` | Anesthesia of skin |
| 3 | ICD-10 | `E1122` | Type 2 diabetes mellitus with diabetic chronic kidney disease |
| 4 | ICD-10 | `I120` | Hypertensive chronic kidney disease with stage 5 chronic kidney disease or end stage renal disease |
| 5 | ICD-10 | `N186` | End stage renal disease |
| 6 | ICD-10 | `Z992` | Dependence on renal dialysis |
| 7 | ICD-10 | `E1142` | Type 2 diabetes mellitus with diabetic polyneuropathy |
| 8 | ICD-10 | `E1151` | Type 2 diabetes mellitus with diabetic peripheral angiopathy without gangrene |
| 9 | ICD-10 | `E785` | Hyperlipidemia, unspecified |
| 10 | ICD-10 | `D649` | Anemia, unspecified |
| 11 | ICD-10 | `Z87891` | Personal history of nicotine dependence |
| 12 | ICD-10 | `Z794` | Long term (current) use of insulin |
| 13 | ICD-10 | `Z89421` | Acquired absence of other right toe(s) |

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
| 2193-05-03 19:12:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2193-05-03 19:12:00 | Transfer | → Emergency Department (ED) |
| 2193-05-03 22:45:00 | Admission | Admitted from TRANSFER FROM HOSPITAL (EU OBSERVATION) |
| 2193-05-05 02:13:00 | Discharge | To N/A |
| 2193-05-05 02:13:00 | ED Departure | Left Emergency Dept. |

## 10. Missing / Ambiguous Data

- Discharge location not recorded.
- No procedure ICD codes — procedures may not have been coded or were minor.
- No ICU stay — patient managed on floor/step-down only.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
