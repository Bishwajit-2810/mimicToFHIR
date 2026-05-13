# Encounter Report — HADM 25926192

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 25926192 |
| Subject ID | 10009628 |
| Patient Sex | M |
| Patient Anchor Age (at anchor year) | 58 |
| Anchor Year | 2153 |
| Admission Time | 2153-09-17 17:08:00 |
| Discharge Time | 2153-09-25 13:20:00 |
| Admission Type | URGENT |
| Admission Location | TRANSFER FROM HOSPITAL |
| Discharge Location | HOME HEALTH CARE |
| Insurance | Medicaid |
| Language | ? |
| Marital Status | MARRIED |
| Race/Ethnicity | HISPANIC/LATINO - PUERTO RICAN |
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
| 2153-09-17 17:08:47 | N/A | CSURG |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-9 `41401`: Coronary atherosclerosis of native coronary artery
- (seq 2) ICD-9 `4142`: Chronic total occlusion of coronary artery
- (seq 3) ICD-9 `42731`: Atrial fibrillation
- (seq 4) ICD-9 `25050`: Diabetes with ophthalmic manifestations, type II or unspecified type, not stated as uncontrolled
- (seq 5) ICD-9 `36201`: Background diabetic retinopathy

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-9 | `41401` | Coronary atherosclerosis of native coronary artery |
| 2 | ICD-9 | `4142` | Chronic total occlusion of coronary artery |
| 3 | ICD-9 | `42731` | Atrial fibrillation |
| 4 | ICD-9 | `25050` | Diabetes with ophthalmic manifestations, type II or unspecified type, not stated as uncontrolled |
| 5 | ICD-9 | `36201` | Background diabetic retinopathy |
| 6 | ICD-9 | `V5867` | Long-term (current) use of insulin |
| 7 | ICD-9 | `2859` | Anemia, unspecified |
| 8 | ICD-9 | `2724` | Other and unspecified hyperlipidemia |

## 5. ICU Stays

| Stay ID | First Care Unit | Last Care Unit | ICU Admit | ICU Discharge | LOS (days) |
|---|---|---|---|---|---|
| 35258379 | Cardiac Vascular Intensive Care Unit (CVICU) | Cardiac Vascular Intensive Care Unit (CVICU) | 2153-09-19 09:54:49 | 2153-09-21 16:39:06 | 2.28 |

## 6. Escalation / Severity Indicators

The following critical conditions or interventions were detected:

- **Arterial Line** (ICU procedure event)
- **Invasive Mechanical Ventilation** (ICU procedure event)

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2153-09-19 | ICD-9 | `3614` | (Aorto)coronary bypass of four or more coronary arteries |
| 2 | 2153-09-19 | ICD-9 | `3615` | Single internal mammary-coronary artery bypass |
| 3 | 2153-09-19 | ICD-9 | `3961` | Extracorporeal circulation auxiliary to open heart surgery |

### ICU Procedure Events (from `icu/procedureevents.csv.gz`)

- Invasive Ventilation (category: 2-Ventilation, started: 2153-09-19 13:45:00, status: FinishedRunning)
- OR Received (category: 3-Significant Events, started: 2153-09-19 13:45:00, status: FinishedRunning)
- Multi Lumen (category: Access Lines - Invasive, started: 2153-09-19 14:00:00, status: FinishedRunning)
- 20 Gauge (category: Access Lines - Peripheral, started: 2153-09-19 14:00:00, status: FinishedRunning)
- 16 Gauge (category: Access Lines - Peripheral, started: 2153-09-19 14:00:00, status: FinishedRunning)
- Nasal Swab (category: 6-Cultures, started: 2153-09-19 14:00:00, status: FinishedRunning)
- Chest X-Ray (category: 5-Imaging, started: 2153-09-19 14:00:00, status: FinishedRunning)
- Arterial Line (category: Access Lines - Invasive, started: 2153-09-19 14:00:00, status: FinishedRunning)
- EKG (category: 4-Procedures, started: 2153-09-19 14:26:00, status: FinishedRunning)
- Extubation (category: 1-Intubation/Extubation, started: 2153-09-19 18:18:00, status: FinishedRunning)
- Temporary Pacemaker Wires Discontinued (category: 4-Procedures, started: 2153-09-21 09:15:00, status: FinishedRunning)
- Chest Tube Removed (category: 4-Procedures, started: 2153-09-21 09:20:00, status: FinishedRunning)
- Urine Culture (category: 6-Cultures, started: 2153-09-21 11:01:00, status: FinishedRunning)

## 8. Critical Findings (Charted Events)

- **Ventilator Mode** (first noted: 2153-09-19 14:00:00)
- **Ventilator Tank #1** (first noted: 2153-09-19 14:00:00)
- **Ventilator Tank #2** (first noted: 2153-09-19 14:00:00)
- **Code Status** (first noted: 2153-09-20 12:33:00)
- **Temporary Pacemaker Wire Condition** (first noted: 2153-09-19 14:00:00)
- **Temporary Pacemaker Type** (first noted: 2153-09-19 14:00:00)
- **Temporary Pacemaker Mode** (first noted: 2153-09-19 14:00:00)
- **Dialysis patient** (first noted: 2153-09-19 12:14:00)

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2153-09-17 17:08:00 | Admission | Admitted from TRANSFER FROM HOSPITAL (URGENT) |
| 2153-09-19 09:54:49 | ICU Admission | Cardiac Vascular Intensive Care Unit (CVICU) (LOS: 2.3 days) |
| 2153-09-19 09:54:49 | Transfer | → Cardiac Vascular Intensive Care Unit (CVICU) (transfer) |
| 2153-09-21 16:39:06 | Transfer | → Cardiac Surgery (transfer) |
| 2153-09-25 13:20:00 | Discharge | To HOME HEALTH CARE |

## 10. Missing / Ambiguous Data

- No ED registration time — admission may not have gone through ED.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
