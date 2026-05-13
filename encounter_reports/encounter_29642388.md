# Encounter Report — HADM 29642388

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 29642388 |
| Subject ID | 10022281 |
| Patient Sex | M |
| Patient Anchor Age (at anchor year) | 84 |
| Anchor Year | 2125 |
| Admission Time | 2125-06-17 04:11:00 |
| Discharge Time | 2125-06-19 15:25:00 |
| Admission Type | EW EMER. |
| Admission Location | EMERGENCY ROOM |
| Discharge Location | HOME |
| Insurance | Other |
| Language | ENGLISH |
| Marital Status | MARRIED |
| Race/Ethnicity | OTHER |
| ED Registration | 2125-06-16 20:32:00 |
| ED Departure | 2125-06-17 05:14:00 |
| In-Hospital Mortality | No |
| Date of Death (overall) | N/A |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| HCFA | 301 | PERIPHERAL VASCULAR DISORDERS W/O CC/MCC | N/A | N/A |
| APR | 197 | PERIPHERAL & OTHER VASCULAR DISORDERS | 2.0 | 3.0 |

### Primary Diagnosis (seq_num = 1)

- **ICD-9 44102**: Dissection of aorta, abdominal

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2125-06-17 04:12:54 | N/A | VSURG |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-9 `44102`: Dissection of aorta, abdominal
- (seq 2) ICD-9 `4019`: Unspecified essential hypertension
- (seq 3) ICD-9 `71535`: Osteoarthrosis, localized, not specified whether primary or secondary, pelvic region and thigh
- (seq 4) ICD-9 `25000`: Diabetes mellitus without mention of complication, type II or unspecified type, not stated as uncontrolled
- (seq 5) ICD-9 `2720`: Pure hypercholesterolemia

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-9 | `44102` | Dissection of aorta, abdominal |
| 2 | ICD-9 | `4019` | Unspecified essential hypertension |
| 3 | ICD-9 | `71535` | Osteoarthrosis, localized, not specified whether primary or secondary, pelvic region and thigh |
| 4 | ICD-9 | `25000` | Diabetes mellitus without mention of complication, type II or unspecified type, not stated as uncontrolled |
| 5 | ICD-9 | `2720` | Pure hypercholesterolemia |
| 6 | ICD-9 | `41401` | Coronary atherosclerosis of native coronary artery |
| 7 | ICD-9 | `V1582` | Personal history of tobacco use |
| 8 | ICD-9 | `V5867` | Long-term (current) use of insulin |

## 5. ICU Stays

| Stay ID | First Care Unit | Last Care Unit | ICU Admit | ICU Discharge | LOS (days) |
|---|---|---|---|---|---|
| 30585761 | Cardiac Vascular Intensive Care Unit (CVICU) | Cardiac Vascular Intensive Care Unit (CVICU) | 2125-06-17 04:12:54 | 2125-06-18 14:55:55 | 1.45 |

## 6. Escalation / Severity Indicators

The following critical conditions or interventions were detected:

- **Arterial Line** (ICU procedure event)

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2125-06-17 | ICD-9 | `3891` | Arterial catheterization |

### ICU Procedure Events (from `icu/procedureevents.csv.gz`)

- 18 Gauge (category: Access Lines - Peripheral, started: 2125-06-17 05:06:00, status: FinishedRunning)
- Arterial Line (category: Access Lines - Invasive, started: 2125-06-17 06:24:00, status: FinishedRunning)

## 8. Critical Findings (Charted Events)

- **Dialysis patient** (first noted: 2125-06-17 05:06:00)

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2125-06-16 20:32:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2125-06-16 20:32:00 | Transfer | → Emergency Department (ED) |
| 2125-06-17 04:11:00 | Admission | Admitted from EMERGENCY ROOM (EW EMER.) |
| 2125-06-17 04:12:54 | ICU Admission | Cardiac Vascular Intensive Care Unit (CVICU) (LOS: 1.4 days) |
| 2125-06-17 05:12:07 | Transfer | → Cardiac Vascular Intensive Care Unit (CVICU) (transfer) |
| 2125-06-17 05:14:00 | ED Departure | Left Emergency Dept. |
| 2125-06-18 14:55:55 | Transfer | → Vascular (transfer) |
| 2125-06-18 15:44:46 | Transfer | → Vascular (transfer) |
| 2125-06-19 15:25:00 | Discharge | To HOME |

## 10. Missing / Ambiguous Data

- No obvious missing critical fields detected.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
