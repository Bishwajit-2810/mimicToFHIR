# Encounter Report — HADM 27089790

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 27089790 |
| Subject ID | 10012552 |
| Patient Sex | M |
| Patient Anchor Age (at anchor year) | 78 |
| Anchor Year | 2140 |
| Admission Time | 2140-03-22 17:18:00 |
| Discharge Time | 2140-03-30 14:10:00 |
| Admission Type | URGENT |
| Admission Location | TRANSFER FROM HOSPITAL |
| Discharge Location | HOME HEALTH CARE |
| Insurance | Medicare |
| Language | ENGLISH |
| Marital Status | MARRIED |
| Race/Ethnicity | UNKNOWN |
| ED Registration | N/A |
| ED Departure | N/A |
| In-Hospital Mortality | No |
| Date of Death (overall) | N/A |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| APR | 166 | CORONARY BYPASS W/O AMI OR COMPLEX PDX | 2.0 | 2.0 |
| HCFA | 236 | CORONARY BYPASS W/O CARDIAC CATH W/O MCC | N/A | N/A |

### Primary Diagnosis (seq_num = 1)

- **ICD-9 41071**: Subendocardial infarction, initial episode of care

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2140-03-22 17:19:37 | N/A | CSURG |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-9 `41071`: Subendocardial infarction, initial episode of care
- (seq 2) ICD-9 `2724`: Other and unspecified hyperlipidemia
- (seq 3) ICD-9 `41401`: Coronary atherosclerosis of native coronary artery
- (seq 4) ICD-9 `4019`: Unspecified essential hypertension
- (seq 5) ICD-9 `53081`: Esophageal reflux

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-9 | `41071` | Subendocardial infarction, initial episode of care |
| 2 | ICD-9 | `2724` | Other and unspecified hyperlipidemia |
| 3 | ICD-9 | `41401` | Coronary atherosclerosis of native coronary artery |
| 4 | ICD-9 | `4019` | Unspecified essential hypertension |
| 5 | ICD-9 | `53081` | Esophageal reflux |
| 6 | ICD-9 | `V1005` | Personal history of malignant neoplasm of large intestine |
| 7 | ICD-9 | `V8741` | Personal history of antineoplastic chemotherapy |
| 8 | ICD-9 | `V707` | Examination of participant in clinical trial |

## 5. ICU Stays

| Stay ID | First Care Unit | Last Care Unit | ICU Admit | ICU Discharge | LOS (days) |
|---|---|---|---|---|---|
| 33383124 | Cardiac Vascular Intensive Care Unit (CVICU) | Cardiac Vascular Intensive Care Unit (CVICU) | 2140-03-25 14:37:26 | 2140-03-28 18:25:54 | 3.16 |

## 6. Escalation / Severity Indicators

The following critical conditions or interventions were detected:

- **Arterial Line** (ICU procedure event)
- **Invasive Mechanical Ventilation** (ICU procedure event)

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2140-03-25 | ICD-9 | `3615` | Single internal mammary-coronary artery bypass |
| 2 | 2140-03-25 | ICD-9 | `3612` | (Aorto)coronary bypass of two coronary arteries |
| 3 | 2140-03-25 | ICD-9 | `3961` | Extracorporeal circulation auxiliary to open heart surgery |

### ICU Procedure Events (from `icu/procedureevents.csv.gz`)

- OR Received (category: 3-Significant Events, started: 2140-03-25 17:34:00, status: FinishedRunning)
- Invasive Ventilation (category: 2-Ventilation, started: 2140-03-25 17:35:00, status: FinishedRunning)
- Cordis/Introducer (category: Access Lines - Invasive, started: 2140-03-25 17:35:00, status: FinishedRunning)
- Arterial Line (category: Access Lines - Invasive, started: 2140-03-25 17:36:00, status: FinishedRunning)
- PA Catheter (category: Access Lines - Invasive, started: 2140-03-25 17:45:00, status: FinishedRunning)
- 20 Gauge (category: Access Lines - Peripheral, started: 2140-03-25 17:46:00, status: FinishedRunning)
- 18 Gauge (category: Access Lines - Peripheral, started: 2140-03-25 17:48:00, status: FinishedRunning)
- EKG (category: 4-Procedures, started: 2140-03-25 18:01:00, status: FinishedRunning)
- Extubation (category: 1-Intubation/Extubation, started: 2140-03-26 00:20:00, status: FinishedRunning)
- Chest Tube Removed (category: 4-Procedures, started: 2140-03-27 09:31:00, status: FinishedRunning)
- Chest X-Ray (category: 5-Imaging, started: 2140-03-27 12:21:00, status: FinishedRunning)
- Temporary Pacemaker Wires Discontinued (category: 4-Procedures, started: 2140-03-28 08:00:00, status: FinishedRunning)

## 8. Critical Findings (Charted Events)

- **Ventilator Type** (first noted: 2140-03-25 00:00:00)
- **Ventilator Mode** (first noted: 2140-03-25 00:00:00)
- **Ventilator Tank #1** (first noted: 2140-03-25 20:00:00)
- **Known difficult intubation** (first noted: 2140-03-25 20:31:00)
- **Temporary Pacemaker Wires Venticular** (first noted: 2140-03-25 17:59:00)
- **Temporary Pacemaker Wire Condition** (first noted: 2140-03-25 17:59:00)
- **Temporary Pacemaker Rate** (first noted: 2140-03-25 18:30:00)

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2140-03-22 17:18:00 | Admission | Admitted from TRANSFER FROM HOSPITAL (URGENT) |
| 2140-03-25 11:11:08 | Transfer | → PACU (transfer) |
| 2140-03-25 14:37:26 | ICU Admission | Cardiac Vascular Intensive Care Unit (CVICU) (LOS: 3.2 days) |
| 2140-03-25 14:37:26 | Transfer | → Cardiac Vascular Intensive Care Unit (CVICU) (transfer) |
| 2140-03-26 18:36:23 | Transfer | → Cardiac Vascular Intensive Care Unit (CVICU) (transfer) |
| 2140-03-28 18:25:54 | Transfer | → Cardiac Surgery (transfer) |
| 2140-03-30 14:10:00 | Discharge | To HOME HEALTH CARE |

## 10. Missing / Ambiguous Data

- No ED registration time — admission may not have gone through ED.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
