# Encounter Report — HADM 20044587

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 20044587 |
| Subject ID | 10023771 |
| Patient Sex | M |
| Patient Anchor Age (at anchor year) | 70 |
| Anchor Year | 2113 |
| Admission Time | 2113-08-25 07:15:00 |
| Discharge Time | 2113-08-30 14:15:00 |
| Admission Type | ELECTIVE |
| Admission Location | PHYSICIAN REFERRAL |
| Discharge Location | SKILLED NURSING FACILITY |
| Insurance | Medicare |
| Language | ENGLISH |
| Marital Status | MARRIED |
| Race/Ethnicity | WHITE |
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

- **ICD-9 41401**: Coronary atherosclerosis of native coronary artery

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2113-08-25 03:17:43 | N/A | CSURG |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-9 `41401`: Coronary atherosclerosis of native coronary artery
- (seq 2) ICD-9 `20300`: Multiple myeloma, without mention of having achieved remission
- (seq 3) ICD-9 `99811`: Hemorrhage complicating a procedure
- (seq 4) ICD-9 `V8741`: Personal history of antineoplastic chemotherapy
- (seq 5) ICD-9 `2724`: Other and unspecified hyperlipidemia

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-9 | `41401` | Coronary atherosclerosis of native coronary artery |
| 2 | ICD-9 | `20300` | Multiple myeloma, without mention of having achieved remission |
| 3 | ICD-9 | `99811` | Hemorrhage complicating a procedure |
| 4 | ICD-9 | `V8741` | Personal history of antineoplastic chemotherapy |
| 5 | ICD-9 | `2724` | Other and unspecified hyperlipidemia |
| 6 | ICD-9 | `4019` | Unspecified essential hypertension |
| 7 | ICD-9 | `E8782` | Surgical operation with anastomosis, bypass, or graft, with natural or artificial tissues used as implant causing abnormal patient reaction, or later complication, without mention of misadventure at time of operation |
| 8 | ICD-9 | `42731` | Atrial fibrillation |

## 5. ICU Stays

| Stay ID | First Care Unit | Last Care Unit | ICU Admit | ICU Discharge | LOS (days) |
|---|---|---|---|---|---|
| 33177122 | Cardiac Vascular Intensive Care Unit (CVICU) | Cardiac Vascular Intensive Care Unit (CVICU) | 2113-08-25 09:32:41 | 2113-08-27 16:27:53 | 2.29 |

## 6. Escalation / Severity Indicators

The following critical conditions or interventions were detected:

- **Arterial Line** (ICU procedure event)
- **Invasive Mechanical Ventilation** (ICU procedure event)

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2113-08-25 | ICD-9 | `3615` | Single internal mammary-coronary artery bypass |
| 2 | 2113-08-25 | ICD-9 | `3613` | (Aorto)coronary bypass of three coronary arteries |
| 3 | 2113-08-25 | ICD-9 | `3961` | Extracorporeal circulation auxiliary to open heart surgery |

### ICU Procedure Events (from `icu/procedureevents.csv.gz`)

- Invasive Ventilation (category: 2-Ventilation, started: 2113-08-25 12:30:00, status: FinishedRunning)
- Nasal Swab (category: 6-Cultures, started: 2113-08-25 12:30:00, status: FinishedRunning)
- OR Received (category: 3-Significant Events, started: 2113-08-25 12:30:00, status: FinishedRunning)
- Arterial Line (category: Access Lines - Invasive, started: 2113-08-25 12:36:00, status: FinishedRunning)
- Multi Lumen (category: Access Lines - Invasive, started: 2113-08-25 12:37:00, status: FinishedRunning)
- 16 Gauge (category: Access Lines - Peripheral, started: 2113-08-25 12:37:00, status: FinishedRunning)
- EKG (category: 4-Procedures, started: 2113-08-25 14:03:00, status: FinishedRunning)
- Chest X-Ray (category: 5-Imaging, started: 2113-08-25 20:29:00, status: FinishedRunning)
- Extubation (category: 1-Intubation/Extubation, started: 2113-08-26 07:33:00, status: FinishedRunning)

## 8. Critical Findings (Charted Events)

- **Ventilator Tank #2** (first noted: 2113-08-25 12:00:00)
- **Ventilator Type** (first noted: 2113-08-25 12:00:00)
- **Ventilator Tank #1** (first noted: 2113-08-25 12:00:00)
- **Code Status** (first noted: 2113-08-25 10:07:00)
- **Temporary Pacemaker Rate** (first noted: 2113-08-26 00:00:00)
- **Temporary Pacemaker Wires Atrial** (first noted: 2113-08-26 00:00:00)
- **Temporary Pacemaker Wire Condition** (first noted: 2113-08-26 00:00:00)

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2113-08-25 07:15:00 | Admission | Admitted from PHYSICIAN REFERRAL (ELECTIVE) |
| 2113-08-25 09:32:41 | ICU Admission | Cardiac Vascular Intensive Care Unit (CVICU) (LOS: 2.3 days) |
| 2113-08-25 09:32:41 | Transfer | → Cardiac Vascular Intensive Care Unit (CVICU) (transfer) |
| 2113-08-27 16:27:53 | Transfer | → Cardiac Surgery (transfer) |
| 2113-08-30 14:15:00 | Discharge | To SKILLED NURSING FACILITY |

## 10. Missing / Ambiguous Data

- No ED registration time — admission may not have gone through ED.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
