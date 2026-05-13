# Encounter Report — HADM 29366372

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 29366372 |
| Subject ID | 10018423 |
| Patient Sex | M |
| Patient Anchor Age (at anchor year) | 37 |
| Anchor Year | 2162 |
| Admission Time | 2167-05-03 21:24:00 |
| Discharge Time | 2167-05-11 12:57:00 |
| Admission Type | EW EMER. |
| Admission Location | EMERGENCY ROOM |
| Discharge Location | HOME HEALTH CARE |
| Insurance | Other |
| Language | ENGLISH |
| Marital Status | MARRIED |
| Race/Ethnicity | WHITE |
| ED Registration | 2167-05-03 15:18:00 |
| ED Departure | 2167-05-03 22:50:00 |
| In-Hospital Mortality | No |
| Date of Death (overall) | N/A |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| APR | 165 | CORONARY BYPASS W AMI OR COMPLEX PDX | 2.0 | 1.0 |
| HCFA | 234 | CORONARY BYPASS W CARDIAC CATH W/O MCC | N/A | N/A |

### Primary Diagnosis (seq_num = 1)

- **ICD-10 I25110**: Atherosclerotic heart disease of native coronary artery with unstable angina pectoris

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2167-05-03 21:25:46 | N/A | CMED |
| 2167-05-05 13:00:29 | CMED | CSURG |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-10 `I25110`: Atherosclerotic heart disease of native coronary artery with unstable angina pectoris
- (seq 2) ICD-10 `I2582`: Chronic total occlusion of coronary artery
- (seq 3) ICD-10 `D62`: Acute posthemorrhagic anemia
- (seq 4) ICD-10 `I10`: Essential (primary) hypertension
- (seq 5) ICD-10 `E780`: Pure hypercholesterolemia

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-10 | `I25110` | Atherosclerotic heart disease of native coronary artery with unstable angina pectoris |
| 2 | ICD-10 | `I2582` | Chronic total occlusion of coronary artery |
| 3 | ICD-10 | `D62` | Acute posthemorrhagic anemia |
| 4 | ICD-10 | `I10` | Essential (primary) hypertension |
| 5 | ICD-10 | `E780` | Pure hypercholesterolemia |
| 6 | ICD-10 | `K219` | Gastro-esophageal reflux disease without esophagitis |
| 7 | ICD-10 | `E669` | Obesity, unspecified |
| 8 | ICD-10 | `Z6838` | Body mass index (BMI) 38.0-38.9, adult |
| 9 | ICD-10 | `Z8249` | Family history of ischemic heart disease and other diseases of the circulatory system |

## 5. ICU Stays

| Stay ID | First Care Unit | Last Care Unit | ICU Admit | ICU Discharge | LOS (days) |
|---|---|---|---|---|---|
| 30665396 | Cardiac Vascular Intensive Care Unit (CVICU) | Cardiac Vascular Intensive Care Unit (CVICU) | 2167-05-05 12:54:06 | 2167-05-06 18:40:10 | 1.24 |

## 6. Escalation / Severity Indicators

The following critical conditions or interventions were detected:

- **Arterial Line** (ICU procedure event)
- **Invasive Mechanical Ventilation** (ICU procedure event)

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2167-05-05 | ICD-10 | `02100A9` | Bypass Coronary Artery, One Artery from Left Internal Mammary with Autologous Arterial Tissue, Open Approach |
| 2 | 2167-05-04 | ICD-10 | `4A023N7` | Measurement of Cardiac Sampling and Pressure, Left Heart, Percutaneous Approach |
| 3 | 2167-05-05 | ICD-10 | `021009W` | Bypass Coronary Artery, One Artery from Aorta with Autologous Venous Tissue, Open Approach |
| 4 | 2167-05-05 | ICD-10 | `02100A8` | Bypass Coronary Artery, One Artery from Right Internal Mammary with Autologous Arterial Tissue, Open Approach |
| 5 | 2167-05-05 | ICD-10 | `06BP4ZZ` | Excision of Right Saphenous Vein, Percutaneous Endoscopic Approach |
| 6 | 2167-05-05 | ICD-10 | `03B14ZZ` | Excision of Left Internal Mammary Artery, Percutaneous Endoscopic Approach |
| 7 | 2167-05-05 | ICD-10 | `03B04ZZ` | Excision of Right Internal Mammary Artery, Percutaneous Endoscopic Approach |
| 8 | 2167-05-04 | ICD-10 | `B2111ZZ` | Fluoroscopy of Multiple Coronary Arteries using Low Osmolar Contrast |
| 9 | 2167-05-05 | ICD-10 | `5A1221Z` | Performance of Cardiac Output, Continuous |
| 10 | 2167-05-05 | ICD-10 | `3E080GC` | Introduction of Other Therapeutic Substance into Heart, Open Approach |

### ICU Procedure Events (from `icu/procedureevents.csv.gz`)

- OR Received (category: 3-Significant Events, started: 2167-05-05 19:14:00, status: FinishedRunning)
- Invasive Ventilation (category: 2-Ventilation, started: 2167-05-05 19:15:00, status: FinishedRunning)
- Arterial Line (category: Access Lines - Invasive, started: 2167-05-05 20:27:00, status: FinishedRunning)
- Multi Lumen (category: Access Lines - Invasive, started: 2167-05-05 20:28:00, status: FinishedRunning)
- 20 Gauge (category: Access Lines - Peripheral, started: 2167-05-05 20:28:00, status: FinishedRunning)
- 18 Gauge (category: Access Lines - Peripheral, started: 2167-05-05 20:28:00, status: FinishedRunning)
- Extubation (category: 1-Intubation/Extubation, started: 2167-05-06 05:56:00, status: FinishedRunning)
- Chest Tube Removed (category: 4-Procedures, started: 2167-05-06 09:24:00, status: FinishedRunning)
- Chest X-Ray (category: 5-Imaging, started: 2167-05-06 09:55:00, status: FinishedRunning)

## 8. Critical Findings (Charted Events)

- **Ventilator Type** (first noted: 2167-05-05 19:15:00)
- **Ventilator Mode** (first noted: 2167-05-05 19:10:00)
- **Ventilator Tank #1** (first noted: 2167-05-06 04:00:00)
- **Known difficult intubation** (first noted: 2167-05-05 19:15:00)
- **Temporary Pacemaker Wires Atrial** (first noted: 2167-05-06 00:32:00)
- **Temporary Pacemaker Type** (first noted: 2167-05-06 00:32:00)
- **Temporary Pacemaker Rate** (first noted: 2167-05-06 08:00:00)

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2167-05-03 15:18:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2167-05-03 15:18:00 | Transfer | → Emergency Department (ED) |
| 2167-05-03 21:24:00 | Admission | Admitted from EMERGENCY ROOM (EW EMER.) |
| 2167-05-03 22:50:00 | ED Departure | Left Emergency Dept. |
| 2167-05-05 11:04:21 | Transfer | → PACU (transfer) |
| 2167-05-05 12:54:06 | ICU Admission | Cardiac Vascular Intensive Care Unit (CVICU) (LOS: 1.2 days) |
| 2167-05-05 12:54:06 | Transfer | → Cardiac Vascular Intensive Care Unit (CVICU) (transfer) |
| 2167-05-06 18:40:10 | Transfer | → Cardiac Surgery (transfer) |
| 2167-05-08 17:29:09 | Transfer | → Cardiac Surgery (transfer) |
| 2167-05-11 12:57:00 | Discharge | To HOME HEALTH CARE |

## 10. Missing / Ambiguous Data

- No obvious missing critical fields detected.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
