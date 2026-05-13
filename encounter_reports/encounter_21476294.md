# Encounter Report — HADM 21476294

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 21476294 |
| Subject ID | 10035631 |
| Patient Sex | M |
| Patient Anchor Age (at anchor year) | 63 |
| Anchor Year | 2112 |
| Admission Time | 2115-11-08 13:54:00 |
| Discharge Time | 2115-12-08 17:31:00 |
| Admission Type | OBSERVATION ADMIT |
| Admission Location | EMERGENCY ROOM |
| Discharge Location | HOME |
| Insurance | Other |
| Language | ENGLISH |
| Marital Status | MARRIED |
| Race/Ethnicity | WHITE |
| ED Registration | 2115-11-08 12:02:00 |
| ED Departure | 2115-11-08 15:43:00 |
| In-Hospital Mortality | No |
| Date of Death (overall) | 2116-03-12 |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| HCFA | 840 | LYMPHOMA & NON-ACUTE LEUKEMIA W MCC | N/A | N/A |
| APR | 690 | ACUTE LEUKEMIA | 4.0 | 3.0 |

### Primary Diagnosis (seq_num = 1)

- **ICD-10 C92Z2**: Other myeloid leukemia, in relapse

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2115-11-08 13:55:43 | N/A | OMED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-10 `C92Z2`: Other myeloid leukemia, in relapse
- (seq 2) ICD-10 `J810`: Acute pulmonary edema
- (seq 3) ICD-10 `Z9484`: Stem cells transplant status
- (seq 4) ICD-10 `D709`: Neutropenia, unspecified
- (seq 5) ICD-10 `K521`: Toxic gastroenteritis and colitis

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-10 | `C92Z2` | Other myeloid leukemia, in relapse |
| 2 | ICD-10 | `J810` | Acute pulmonary edema |
| 3 | ICD-10 | `Z9484` | Stem cells transplant status |
| 4 | ICD-10 | `D709` | Neutropenia, unspecified |
| 5 | ICD-10 | `K521` | Toxic gastroenteritis and colitis |
| 6 | ICD-10 | `D696` | Thrombocytopenia, unspecified |
| 7 | ICD-10 | `E871` | Hypo-osmolality and hyponatremia |
| 8 | ICD-10 | `I951` | Orthostatic hypotension |
| 9 | ICD-10 | `R5081` | Fever presenting with conditions classified elsewhere |
| 10 | ICD-10 | `R0789` | Other chest pain |
| 11 | ICD-10 | `G893` | Neoplasm related pain (acute) (chronic) |
| 12 | ICD-10 | `Z853` | Personal history of malignant neoplasm of breast |
| 13 | ICD-10 | `Z79810` | Long term (current) use of selective estrogen receptor modulators (SERMs) |
| 14 | ICD-10 | `Z9012` | Acquired absence of left breast and nipple |
| 15 | ICD-10 | `Z87891` | Personal history of nicotine dependence |
| 16 | ICD-10 | `G44209` | Tension-type headache, unspecified, not intractable |
| 17 | ICD-10 | `R740` | Nonspecific elevation of levels of transaminase and lactic acid dehydrogenase [LDH] |
| 18 | ICD-10 | `T361X5A` | Adverse effect of cephalosporins and other beta-lactam antibiotics, initial encounter |
| 19 | ICD-10 | `Y92230` | Patient room in hospital as the place of occurrence of the external cause |
| 20 | ICD-10 | `Z792` | Long term (current) use of antibiotics |
| 21 | ICD-10 | `Z20828` | Contact with and (suspected) exposure to other viral communicable diseases |
| 22 | ICD-10 | `R634` | Abnormal weight loss |
| 23 | ICD-10 | `Z6826` | Body mass index (BMI) 26.0-26.9, adult |
| 24 | ICD-10 | `M545` | Low back pain |

## 5. ICU Stays

_No ICU stay recorded for this admission._

## 6. Escalation / Severity Indicators

_No escalation indicators detected from ICD codes or ICU procedure events._

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2115-11-10 | ICD-10 | `3E04305` | Introduction of Other Antineoplastic into Central Vein, Percutaneous Approach |
| 2 | 2115-11-08 | ICD-10 | `07DR3ZX` | Extraction of Iliac Bone Marrow, Percutaneous Approach, Diagnostic |
| 3 | 2115-11-09 | ICD-10 | `02HV33Z` | Insertion of Infusion Device into Superior Vena Cava, Percutaneous Approach |


## 8. Critical Findings (Charted Events)

_No critical chart events detected._

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2115-11-08 12:02:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2115-11-08 12:02:00 | Transfer | → Emergency Department (ED) |
| 2115-11-08 13:54:00 | Admission | Admitted from EMERGENCY ROOM (OBSERVATION ADMIT) |
| 2115-11-08 15:43:00 | ED Departure | Left Emergency Dept. |
| 2115-12-02 11:18:28 | Transfer | → Hematology/Oncology (transfer) |
| 2115-12-08 17:31:00 | Discharge | To HOME |

## 10. Missing / Ambiguous Data

- No ICU stay — patient managed on floor/step-down only.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
