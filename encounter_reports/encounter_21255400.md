# Encounter Report — HADM 21255400

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 21255400 |
| Subject ID | 10004422 |
| Patient Sex | M |
| Patient Anchor Age (at anchor year) | 78 |
| Anchor Year | 2111 |
| Admission Time | 2111-01-15 14:55:00 |
| Discharge Time | 2111-01-25 15:00:00 |
| Admission Type | EW EMER. |
| Admission Location | PROCEDURE SITE |
| Discharge Location | HOME HEALTH CARE |
| Insurance | Medicare |
| Language | ENGLISH |
| Marital Status | WIDOWED |
| Race/Ethnicity | WHITE |
| ED Registration | N/A |
| ED Departure | N/A |
| In-Hospital Mortality | No |
| Date of Death (overall) | N/A |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| APR | 165 | CORONARY BYPASS W AMI OR COMPLEX PDX | 3.0 | 2.0 |
| HCFA | 234 | CORONARY BYPASS W CARDIAC CATH W/O MCC | N/A | N/A |

### Primary Diagnosis (seq_num = 1)

- **ICD-9 41401**: Coronary atherosclerosis of native coronary artery

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2111-01-15 14:55:58 | N/A | CMED |
| 2111-01-17 09:45:02 | CMED | CSURG |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-9 `41401`: Coronary atherosclerosis of native coronary artery
- (seq 2) ICD-9 `4111`: Intermediate coronary syndrome
- (seq 3) ICD-9 `99811`: Hemorrhage complicating a procedure
- (seq 4) ICD-9 `9971`: Cardiac complications, not elsewhere classified
- (seq 5) ICD-9 `2910`: Alcohol withdrawal delirium

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-9 | `41401` | Coronary atherosclerosis of native coronary artery |
| 2 | ICD-9 | `4111` | Intermediate coronary syndrome |
| 3 | ICD-9 | `99811` | Hemorrhage complicating a procedure |
| 4 | ICD-9 | `9971` | Cardiac complications, not elsewhere classified |
| 5 | ICD-9 | `2910` | Alcohol withdrawal delirium |
| 6 | ICD-9 | `V4582` | Percutaneous transluminal coronary angioplasty status |
| 7 | ICD-9 | `2724` | Other and unspecified hyperlipidemia |
| 8 | ICD-9 | `4019` | Unspecified essential hypertension |
| 9 | ICD-9 | `V1582` | Personal history of tobacco use |
| 10 | ICD-9 | `E8782` | Surgical operation with anastomosis, bypass, or graft, with natural or artificial tissues used as implant causing abnormal patient reaction, or later complication, without mention of misadventure at time of operation |
| 11 | ICD-9 | `71941` | Pain in joint, shoulder region |
| 12 | ICD-9 | `E8844` | Accidental fall from bed |
| 13 | ICD-9 | `E8497` | Accidents occurring in residential institution |
| 14 | ICD-9 | `42731` | Atrial fibrillation |
| 15 | ICD-9 | `30390` | Other and unspecified alcohol dependence, unspecified |
| 16 | ICD-9 | `45182` | Phlebitis and thrombophlebitis of superficial veins of upper extremities |

## 5. ICU Stays

| Stay ID | First Care Unit | Last Care Unit | ICU Admit | ICU Discharge | LOS (days) |
|---|---|---|---|---|---|
| 32155744 | Cardiac Vascular Intensive Care Unit (CVICU) | Cardiac Vascular Intensive Care Unit (CVICU) | 2111-01-17 09:44:50 | 2111-01-23 18:18:46 | 6.36 |

## 6. Escalation / Severity Indicators

The following critical conditions or interventions were detected:

- **Arterial Line** (ICU procedure event)
- **Invasive Mechanical Ventilation** (ICU procedure event)

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2111-01-17 | ICD-9 | `3615` | Single internal mammary-coronary artery bypass |
| 2 | 2111-01-15 | ICD-9 | `3722` | Left heart cardiac catheterization |
| 3 | 2111-01-17 | ICD-9 | `3613` | (Aorto)coronary bypass of three coronary arteries |
| 4 | 2111-01-17 | ICD-9 | `3961` | Extracorporeal circulation auxiliary to open heart surgery |
| 5 | 2111-01-15 | ICD-9 | `8856` | Coronary arteriography using two catheters |

### ICU Procedure Events (from `icu/procedureevents.csv.gz`)

- Invasive Ventilation (category: 2-Ventilation, started: 2111-01-17 14:58:00, status: FinishedRunning)
- Nasal Swab (category: 6-Cultures, started: 2111-01-17 14:58:00, status: FinishedRunning)
- OR Received (category: 3-Significant Events, started: 2111-01-17 14:58:00, status: FinishedRunning)
- Multi Lumen (category: Access Lines - Invasive, started: 2111-01-17 15:00:00, status: FinishedRunning)
- 18 Gauge (category: Access Lines - Peripheral, started: 2111-01-17 15:00:00, status: FinishedRunning)
- Arterial Line (category: Access Lines - Invasive, started: 2111-01-17 15:00:00, status: FinishedRunning)
- EKG (category: 4-Procedures, started: 2111-01-17 16:03:00, status: FinishedRunning)
- Chest Tube Removed (category: 4-Procedures, started: 2111-01-19 16:30:00, status: FinishedRunning)
- Chest X-Ray (category: 5-Imaging, started: 2111-01-19 17:00:00, status: FinishedRunning)
- Unplanned Line/Catheter Removal (Patient Initiated) (category: 3-Significant Events, started: 2111-01-20 00:00:00, status: FinishedRunning)
- Family updated by RN (category: 7-Communication, started: 2111-01-20 13:54:00, status: FinishedRunning)
- Temporary Pacemaker Wires Discontinued (category: 4-Procedures, started: 2111-01-20 15:10:00, status: FinishedRunning)
- Urine Culture (category: 6-Cultures, started: 2111-01-20 16:46:00, status: FinishedRunning)
- 20 Gauge (category: Access Lines - Peripheral, started: 2111-01-22 12:00:00, status: FinishedRunning)

## 8. Critical Findings (Charted Events)

- **Ventilator Mode** (first noted: 2111-01-17 14:00:00)
- **Ventilator Type** (first noted: 2111-01-17 14:00:00)
- **Code Status** (first noted: 2111-01-20 06:06:00)
- **Seizure Activity** (first noted: 2111-01-18 08:10:00)
- **Seizure** (first noted: 2111-01-21 13:54:00)
- **Temporary Pacemaker Rate** (first noted: 2111-01-17 15:30:00)
- **Temporary Pacemaker Wires Venticular** (first noted: 2111-01-17 15:30:00)
- **Temporary Pacemaker Wire Condition** (first noted: 2111-01-17 15:30:00)
- **Dialysis patient** (first noted: 2111-01-17 11:52:00)

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2111-01-15 14:55:00 | Admission | Admitted from PROCEDURE SITE (EW EMER.) |
| 2111-01-17 09:44:50 | ICU Admission | Cardiac Vascular Intensive Care Unit (CVICU) (LOS: 6.4 days) |
| 2111-01-17 09:44:50 | Transfer | → Cardiac Vascular Intensive Care Unit (CVICU) (transfer) |
| 2111-01-23 18:18:46 | Transfer | → Cardiac Surgery (transfer) |
| 2111-01-25 15:00:00 | Discharge | To HOME HEALTH CARE |

## 10. Missing / Ambiguous Data

- No ED registration time — admission may not have gone through ED.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
