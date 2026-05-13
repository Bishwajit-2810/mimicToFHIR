# Encounter Report — HADM 28157142

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 28157142 |
| Subject ID | 10015931 |
| Patient Sex | M |
| Patient Anchor Age (at anchor year) | 87 |
| Anchor Year | 2176 |
| Admission Time | 2176-11-14 18:02:00 |
| Discharge Time | 2176-11-27 13:30:00 |
| Admission Type | OBSERVATION ADMIT |
| Admission Location | EMERGENCY ROOM |
| Discharge Location | SKILLED NURSING FACILITY |
| Insurance | Medicare |
| Language | ENGLISH |
| Marital Status | MARRIED |
| Race/Ethnicity | WHITE |
| ED Registration | 2176-11-14 02:27:00 |
| ED Departure | 2176-11-14 19:51:00 |
| In-Hospital Mortality | No |
| Date of Death (overall) | 2177-03-29 |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| HCFA | 266 | ENDOVASCULAR CARDIAC VALVE REPLACEMENT W MCC | N/A | N/A |
| APR | 175 | PERCUTANEOUS CORONARY INTERVENTION W/O AMI | 4.0 | 3.0 |

### Primary Diagnosis (seq_num = 1)

- **ICD-10 I350**: Nonrheumatic aortic (valve) stenosis

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2176-11-14 18:02:50 | N/A | CMED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-10 `I350`: Nonrheumatic aortic (valve) stenosis
- (seq 2) ICD-10 `I5023`: Acute on chronic systolic (congestive) heart failure
- (seq 3) ICD-10 `R34`: Anuria and oliguria
- (seq 4) ICD-10 `N179`: Acute kidney failure, unspecified
- (seq 5) ICD-10 `E872`: Acidosis

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-10 | `I350` | Nonrheumatic aortic (valve) stenosis |
| 2 | ICD-10 | `I5023` | Acute on chronic systolic (congestive) heart failure |
| 3 | ICD-10 | `R34` | Anuria and oliguria |
| 4 | ICD-10 | `N179` | Acute kidney failure, unspecified |
| 5 | ICD-10 | `E872` | Acidosis |
| 6 | ICD-10 | `N390` | Urinary tract infection, site not specified |
| 7 | ICD-10 | `E871` | Hypo-osmolality and hyponatremia |
| 8 | ICD-10 | `T81718A` | Complication of other artery following a procedure, not elsewhere classified, initial encounter |
| 9 | ICD-10 | `I482` | Chronic atrial fibrillation |
| 10 | ICD-10 | `Z7901` | Long term (current) use of anticoagulants |
| 11 | ICD-10 | `Y831` | Surgical operation with implant of artificial internal device as the cause of abnormal reaction of the patient, or of later complication, without mention of misadventure at the time of the procedure |
| 12 | ICD-10 | `Y92239` | Unspecified place in hospital as the place of occurrence of the external cause |
| 13 | ICD-10 | `I724` | Aneurysm of artery of lower extremity |
| 14 | ICD-10 | `J449` | Chronic obstructive pulmonary disease, unspecified |
| 15 | ICD-10 | `E785` | Hyperlipidemia, unspecified |
| 16 | ICD-10 | `E1122` | Type 2 diabetes mellitus with diabetic chronic kidney disease |
| 17 | ICD-10 | `I129` | Hypertensive chronic kidney disease with stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease |
| 18 | ICD-10 | `N183` | Chronic kidney disease, stage 3 (moderate) |
| 19 | ICD-10 | `I272` | Other secondary pulmonary hypertension |
| 20 | ICD-10 | `Z794` | Long term (current) use of insulin |
| 21 | ICD-10 | `E875` | Hyperkalemia |
| 22 | ICD-10 | `Z006` | Encounter for examination for normal comparison and control in clinical research program |
| 23 | ICD-10 | `B964` | Proteus (mirabilis) (morganii) as the cause of diseases classified elsewhere |
| 24 | ICD-10 | `M109` | Gout, unspecified |
| 25 | ICD-10 | `L723` | Sebaceous cyst |
| 26 | ICD-10 | `D702` | Other drug-induced agranulocytosis |
| 27 | ICD-10 | `T370X5A` | Adverse effect of sulfonamides, initial encounter |
| 28 | ICD-10 | `N401` | Benign prostatic hyperplasia with lower urinary tract symptoms |
| 29 | ICD-10 | `R3911` | Hesitancy of micturition |
| 30 | ICD-10 | `R339` | Retention of urine, unspecified |

## 5. ICU Stays

| Stay ID | First Care Unit | Last Care Unit | ICU Admit | ICU Discharge | LOS (days) |
|---|---|---|---|---|---|
| 39544395 | Coronary Care Unit (CCU) | Coronary Care Unit (CCU) | 2176-11-19 14:24:52 | 2176-11-20 19:18:13 | 1.20 |

## 6. Escalation / Severity Indicators

The following critical conditions or interventions were detected:

- **Acute Kidney Injury** (ICD diagnosis)
- **Arterial Line** (ICU procedure event)

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2176-11-19 | ICD-10 | `02RF38Z` | Replacement of Aortic Valve with Zooplastic Tissue, Percutaneous Approach |
| 2 | 2176-11-21 | ICD-10 | `3E053GC` | Introduction of Other Therapeutic Substance into Peripheral Artery, Percutaneous Approach |

### ICU Procedure Events (from `icu/procedureevents.csv.gz`)

- 20 Gauge (category: Access Lines - Peripheral, started: 2176-11-19 17:00:00, status: FinishedRunning)
- 16 Gauge (category: Access Lines - Peripheral, started: 2176-11-19 17:00:00, status: FinishedRunning)
- Arterial Line (category: Access Lines - Invasive, started: 2176-11-19 17:06:00, status: FinishedRunning)
- Foley Catheter (category: GI/GU, started: 2176-11-19 19:30:00, status: FinishedRunning)

## 8. Critical Findings (Charted Events)

- **Code Status** (first noted: 2176-11-19 14:53:00)
- **Dialysis patient** (first noted: 2176-11-19 18:07:00)

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2176-11-14 02:27:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2176-11-14 02:27:00 | Transfer | → Emergency Department (ED) |
| 2176-11-14 18:02:00 | Admission | Admitted from EMERGENCY ROOM (OBSERVATION ADMIT) |
| 2176-11-14 19:51:00 | ED Departure | Left Emergency Dept. |
| 2176-11-19 14:24:52 | ICU Admission | Coronary Care Unit (CCU) (LOS: 1.2 days) |
| 2176-11-19 14:24:52 | Transfer | → Coronary Care Unit (CCU) (transfer) |
| 2176-11-20 19:18:13 | Transfer | → Medicine/Cardiology (transfer) |
| 2176-11-27 13:30:00 | Discharge | To SKILLED NURSING FACILITY |

## 10. Missing / Ambiguous Data

- No obvious missing critical fields detected.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
