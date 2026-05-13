# Encounter Report — HADM 22580999

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 22580999 |
| Subject ID | 10035185 |
| Patient Sex | M |
| Patient Anchor Age (at anchor year) | 70 |
| Anchor Year | 2120 |
| Admission Time | 2120-05-12 12:53:00 |
| Discharge Time | 2120-05-17 16:00:00 |
| Admission Type | URGENT |
| Admission Location | TRANSFER FROM HOSPITAL |
| Discharge Location | HOME HEALTH CARE |
| Insurance | Other |
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
| APR | 166 | CORONARY BYPASS W/O AMI OR COMPLEX PDX | 2.0 | 1.0 |
| HCFA | 236 | CORONARY BYPASS W/O CARDIAC CATH W/O MCC | N/A | N/A |

### Primary Diagnosis (seq_num = 1)

- **ICD-9 41401**: Coronary atherosclerosis of native coronary artery

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2120-05-12 12:54:35 | N/A | CSURG |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-9 `41401`: Coronary atherosclerosis of native coronary artery
- (seq 2) ICD-9 `25002`: Diabetes mellitus without mention of complication, type II or unspecified type, uncontrolled
- (seq 3) ICD-9 `4139`: Other and unspecified angina pectoris
- (seq 4) ICD-9 `2724`: Other and unspecified hyperlipidemia
- (seq 5) ICD-9 `27800`: Obesity, unspecified

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-9 | `41401` | Coronary atherosclerosis of native coronary artery |
| 2 | ICD-9 | `25002` | Diabetes mellitus without mention of complication, type II or unspecified type, uncontrolled |
| 3 | ICD-9 | `4139` | Other and unspecified angina pectoris |
| 4 | ICD-9 | `2724` | Other and unspecified hyperlipidemia |
| 5 | ICD-9 | `27800` | Obesity, unspecified |
| 6 | ICD-9 | `V5867` | Long-term (current) use of insulin |
| 7 | ICD-9 | `71696` | Arthropathy, unspecified, lower leg |
| 8 | ICD-9 | `V1083` | Personal history of other malignant neoplasm of skin |
| 9 | ICD-9 | `3899` | Unspecified hearing loss |
| 10 | ICD-9 | `V707` | Examination of participant in clinical trial |
| 11 | ICD-9 | `V8532` | Body Mass Index 32.0-32.9, adult |

## 5. ICU Stays

| Stay ID | First Care Unit | Last Care Unit | ICU Admit | ICU Discharge | LOS (days) |
|---|---|---|---|---|---|
| 39084876 | Cardiac Vascular Intensive Care Unit (CVICU) | Cardiac Vascular Intensive Care Unit (CVICU) | 2120-05-13 14:27:34 | 2120-05-14 16:28:21 | 1.08 |

## 6. Escalation / Severity Indicators

The following critical conditions or interventions were detected:

- **Arterial Line** (ICU procedure event)
- **Invasive Mechanical Ventilation** (ICU procedure event)

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2120-05-13 | ICD-9 | `3613` | (Aorto)coronary bypass of three coronary arteries |
| 2 | 2120-05-13 | ICD-9 | `3615` | Single internal mammary-coronary artery bypass |
| 3 | 2120-05-13 | ICD-9 | `3961` | Extracorporeal circulation auxiliary to open heart surgery |

### ICU Procedure Events (from `icu/procedureevents.csv.gz`)

- Invasive Ventilation (category: 2-Ventilation, started: 2120-05-13 17:26:00, status: FinishedRunning)
- Multi Lumen (category: Access Lines - Invasive, started: 2120-05-13 17:26:00, status: FinishedRunning)
- 20 Gauge (category: Access Lines - Peripheral, started: 2120-05-13 17:26:00, status: FinishedRunning)
- 16 Gauge (category: Access Lines - Peripheral, started: 2120-05-13 17:26:00, status: FinishedRunning)
- OR Received (category: 3-Significant Events, started: 2120-05-13 17:26:00, status: FinishedRunning)
- Arterial Line (category: Access Lines - Invasive, started: 2120-05-13 17:26:00, status: FinishedRunning)
- Nasal Swab (category: 6-Cultures, started: 2120-05-13 17:40:00, status: FinishedRunning)
- Chest X-Ray (category: 5-Imaging, started: 2120-05-13 17:45:00, status: FinishedRunning)
- Extubation (category: 1-Intubation/Extubation, started: 2120-05-13 19:53:00, status: FinishedRunning)
- EKG (category: 4-Procedures, started: 2120-05-13 21:40:00, status: FinishedRunning)

## 8. Critical Findings (Charted Events)

- **Ventilator Tank #2** (first noted: 2120-05-13 17:00:00)
- **Ventilator Type** (first noted: 2120-05-13 17:00:00)
- **Ventilator Tank #1** (first noted: 2120-05-13 17:00:00)
- **Known difficult intubation** (first noted: 2120-05-13 17:00:00)
- **Code Status** (first noted: 2120-05-13 16:36:00)
- **Temporary Pacemaker Mode** (first noted: 2120-05-13 17:30:00)
- **Temporary Pacemaker Wires Venticular** (first noted: 2120-05-13 17:30:00)
- **Temporary Pacemaker Rate** (first noted: 2120-05-13 18:38:00)

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2120-05-12 12:53:00 | Admission | Admitted from TRANSFER FROM HOSPITAL (URGENT) |
| 2120-05-13 12:37:12 | Transfer | → PACU (transfer) |
| 2120-05-13 14:27:34 | ICU Admission | Cardiac Vascular Intensive Care Unit (CVICU) (LOS: 1.1 days) |
| 2120-05-13 14:27:34 | Transfer | → Cardiac Vascular Intensive Care Unit (CVICU) (transfer) |
| 2120-05-14 16:28:21 | Transfer | → Cardiac Surgery (transfer) |
| 2120-05-17 16:00:00 | Discharge | To HOME HEALTH CARE |

## 10. Missing / Ambiguous Data

- No ED registration time — admission may not have gone through ED.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
