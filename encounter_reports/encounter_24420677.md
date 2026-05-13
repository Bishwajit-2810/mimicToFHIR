# Encounter Report — HADM 24420677

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 24420677 |
| Subject ID | 10015931 |
| Patient Sex | M |
| Patient Anchor Age (at anchor year) | 87 |
| Anchor Year | 2176 |
| Admission Time | 2176-12-16 23:31:00 |
| Discharge Time | 2176-12-31 17:35:00 |
| Admission Type | OBSERVATION ADMIT |
| Admission Location | EMERGENCY ROOM |
| Discharge Location | HOME HEALTH CARE |
| Insurance | Medicare |
| Language | ENGLISH |
| Marital Status | MARRIED |
| Race/Ethnicity | WHITE |
| ED Registration | 2176-12-16 18:24:00 |
| ED Departure | 2176-12-17 01:07:00 |
| In-Hospital Mortality | No |
| Date of Death (overall) | 2177-03-29 |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| APR | 194 | HEART FAILURE | 3.0 | 4.0 |
| HCFA | 291 | HEART FAILURE & SHOCK W MCC | N/A | N/A |

### Primary Diagnosis (seq_num = 1)

- **ICD-10 I5023**: Acute on chronic systolic (congestive) heart failure

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2176-12-16 23:32:32 | N/A | CMED |
| 2176-12-22 16:24:53 | CMED | MED |
| 2176-12-22 19:04:51 | MED | CMED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-10 `I5023`: Acute on chronic systolic (congestive) heart failure
- (seq 2) ICD-10 `R571`: Hypovolemic shock
- (seq 3) ICD-10 `N184`: Chronic kidney disease, stage 4 (severe)
- (seq 4) ICD-10 `J90`: Pleural effusion, not elsewhere classified
- (seq 5) ICD-10 `D696`: Thrombocytopenia, unspecified

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-10 | `I5023` | Acute on chronic systolic (congestive) heart failure |
| 2 | ICD-10 | `R571` | Hypovolemic shock |
| 3 | ICD-10 | `N184` | Chronic kidney disease, stage 4 (severe) |
| 4 | ICD-10 | `J90` | Pleural effusion, not elsewhere classified |
| 5 | ICD-10 | `D696` | Thrombocytopenia, unspecified |
| 6 | ICD-10 | `E1122` | Type 2 diabetes mellitus with diabetic chronic kidney disease |
| 7 | ICD-10 | `I272` | Other secondary pulmonary hypertension |
| 8 | ICD-10 | `E11649` | Type 2 diabetes mellitus with hypoglycemia without coma |
| 9 | ICD-10 | `Q6432` | Congenital stricture of urethra |
| 10 | ICD-10 | `L03116` | Cellulitis of left lower limb |
| 11 | ICD-10 | `N390` | Urinary tract infection, site not specified |
| 12 | ICD-10 | `I4891` | Unspecified atrial fibrillation |
| 13 | ICD-10 | `I129` | Hypertensive chronic kidney disease with stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease |
| 14 | ICD-10 | `Z794` | Long term (current) use of insulin |
| 15 | ICD-10 | `J449` | Chronic obstructive pulmonary disease, unspecified |
| 16 | ICD-10 | `E785` | Hyperlipidemia, unspecified |
| 17 | ICD-10 | `N400` | Benign prostatic hyperplasia without lower urinary tract symptoms |
| 18 | ICD-10 | `M7981` | Nontraumatic hematoma of soft tissue |
| 19 | ICD-10 | `T45515A` | Adverse effect of anticoagulants, initial encounter |
| 20 | ICD-10 | `Y92230` | Patient room in hospital as the place of occurrence of the external cause |
| 21 | ICD-10 | `H3530` | Unspecified macular degeneration |
| 22 | ICD-10 | `R5381` | Other malaise |
| 23 | ICD-10 | `Z7902` | Long term (current) use of antithrombotics/antiplatelets |
| 24 | ICD-10 | `F4329` | Adjustment disorder with other symptoms |
| 25 | ICD-10 | `F1021` | Alcohol dependence, in remission |
| 26 | ICD-10 | `B9689` | Other specified bacterial agents as the cause of diseases classified elsewhere |
| 27 | ICD-10 | `R0902` | Hypoxemia |

## 5. ICU Stays

| Stay ID | First Care Unit | Last Care Unit | ICU Admit | ICU Discharge | LOS (days) |
|---|---|---|---|---|---|
| 38137964 | Medical Intensive Care Unit (MICU) | Medical Intensive Care Unit (MICU) | 2176-12-22 16:24:33 | 2176-12-23 20:14:53 | 1.16 |

## 6. Escalation / Severity Indicators

The following critical conditions or interventions were detected:

- **Shock** (ICD diagnosis)

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2176-12-22 | ICD-10 | `02HV33Z` | Insertion of Infusion Device into Superior Vena Cava, Percutaneous Approach |

### ICU Procedure Events (from `icu/procedureevents.csv.gz`)

- 22 Gauge (category: Access Lines - Peripheral, started: 2176-12-22 16:30:00, status: FinishedRunning)
- 20 Gauge (category: Access Lines - Peripheral, started: 2176-12-22 16:30:00, status: FinishedRunning)
- PICC Line (category: Access Lines - Invasive, started: 2176-12-22 19:57:00, status: FinishedRunning)

## 8. Critical Findings (Charted Events)

- **Code Status** (first noted: 2176-12-22 17:47:00)
- **Dialysis patient** (first noted: 2176-12-22 17:49:00)

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2176-12-16 18:24:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2176-12-16 18:24:00 | Transfer | → Emergency Department (ED) |
| 2176-12-16 23:31:00 | Admission | Admitted from EMERGENCY ROOM (OBSERVATION ADMIT) |
| 2176-12-17 01:07:00 | ED Departure | Left Emergency Dept. |
| 2176-12-22 16:24:33 | ICU Admission | Medical Intensive Care Unit (MICU) (LOS: 1.2 days) |
| 2176-12-22 16:24:33 | Transfer | → Medical Intensive Care Unit (MICU) (transfer) |
| 2176-12-23 20:14:53 | Transfer | → Medicine/Cardiology (transfer) |
| 2176-12-31 17:35:00 | Discharge | To HOME HEALTH CARE |

## 10. Missing / Ambiguous Data

- No obvious missing critical fields detected.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
