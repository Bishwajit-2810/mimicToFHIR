# Encounter Report — HADM 28479513

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 28479513 |
| Subject ID | 10018501 |
| Patient Sex | M |
| Patient Anchor Age (at anchor year) | 83 |
| Anchor Year | 2141 |
| Admission Time | 2141-07-30 22:34:00 |
| Discharge Time | 2141-08-05 18:06:00 |
| Admission Type | EW EMER. |
| Admission Location | EMERGENCY ROOM |
| Discharge Location | SKILLED NURSING FACILITY |
| Insurance | Medicare |
| Language | ENGLISH |
| Marital Status | N/A |
| Race/Ethnicity | WHITE |
| ED Registration | 2141-07-30 18:53:00 |
| ED Departure | 2141-07-31 00:01:00 |
| In-Hospital Mortality | No |
| Date of Death (overall) | N/A |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| HCFA | 86 | TRAUMATIC STUPOR & COMA, COMA <1 HR W CC | N/A | N/A |
| APR | 55 | HEAD TRAUMA W COMA >1 HR OR HEMORRHAGE | 2.0 | 1.0 |

### Primary Diagnosis (seq_num = 1)

- **ICD-9 85221**: Subdural hemorrhage following injury without mention of open intracranial wound, with no loss of consciousness

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2141-07-30 22:35:25 | N/A | NSURG |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-9 `85221`: Subdural hemorrhage following injury without mention of open intracranial wound, with no loss of consciousness
- (seq 2) ICD-9 `8054`: Closed fracture of lumbar vertebra without mention of spinal cord injury
- (seq 3) ICD-9 `29181`: Alcohol withdrawal
- (seq 4) ICD-9 `E8150`: Other motor vehicle traffic accident involving collision on the highway injuring driver of motor vehicle other than motorcycle
- (seq 5) ICD-9 `E8495`: Street and highway accidents

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-9 | `85221` | Subdural hemorrhage following injury without mention of open intracranial wound, with no loss of consciousness |
| 2 | ICD-9 | `8054` | Closed fracture of lumbar vertebra without mention of spinal cord injury |
| 3 | ICD-9 | `29181` | Alcohol withdrawal |
| 4 | ICD-9 | `E8150` | Other motor vehicle traffic accident involving collision on the highway injuring driver of motor vehicle other than motorcycle |
| 5 | ICD-9 | `E8495` | Street and highway accidents |
| 6 | ICD-9 | `30391` | Other and unspecified alcohol dependence, continuous |
| 7 | ICD-9 | `4019` | Unspecified essential hypertension |
| 8 | ICD-9 | `53081` | Esophageal reflux |
| 9 | ICD-9 | `2749` | Gout, unspecified |
| 10 | ICD-9 | `V1083` | Personal history of other malignant neoplasm of skin |

## 5. ICU Stays

| Stay ID | First Care Unit | Last Care Unit | ICU Admit | ICU Discharge | LOS (days) |
|---|---|---|---|---|---|
| 35446858 | Trauma SICU (TSICU) | Trauma SICU (TSICU) | 2141-07-31 00:01:00 | 2141-08-01 22:36:21 | 1.94 |

## 6. Escalation / Severity Indicators

_No escalation indicators detected from ICD codes or ICU procedure events._

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2141-08-01 | ICD-9 | `9462` | Alcohol detoxification |

### ICU Procedure Events (from `icu/procedureevents.csv.gz`)

- 18 Gauge (category: Access Lines - Peripheral, started: 2141-07-31 00:29:00, status: FinishedRunning)
- 20 Gauge (category: Access Lines - Peripheral, started: 2141-07-31 01:00:00, status: FinishedRunning)
- CT scan (category: 5-Imaging, started: 2141-07-31 10:45:00, status: FinishedRunning)
- Magnetic Resonance Imaging (category: 5-Imaging, started: 2141-07-31 22:00:00, status: FinishedRunning)

## 8. Critical Findings (Charted Events)

- **Seizure** (first noted: 2141-07-31 15:57:00)
- **Dialysis patient** (first noted: 2141-07-31 07:59:00)

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2141-07-30 18:53:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2141-07-30 18:53:00 | Transfer | → Emergency Department (ED) |
| 2141-07-30 22:34:00 | Admission | Admitted from EMERGENCY ROOM (EW EMER.) |
| 2141-07-31 00:01:00 | ED Departure | Left Emergency Dept. |
| 2141-07-31 00:01:00 | ICU Admission | Trauma SICU (TSICU) (LOS: 1.9 days) |
| 2141-08-01 22:36:21 | Transfer | → Neurology (transfer) |
| 2141-08-05 10:15:00 | Transfer | → Neurology (transfer) |
| 2141-08-05 12:22:41 | Transfer | → Neurology (transfer) |
| 2141-08-05 18:06:00 | Discharge | To SKILLED NURSING FACILITY |

## 10. Missing / Ambiguous Data

- No obvious missing critical fields detected.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
