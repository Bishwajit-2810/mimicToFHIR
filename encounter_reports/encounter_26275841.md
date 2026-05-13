# Encounter Report — HADM 26275841

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 26275841 |
| Subject ID | 10027445 |
| Patient Sex | F |
| Patient Anchor Age (at anchor year) | 48 |
| Anchor Year | 2142 |
| Admission Time | 2142-07-31 00:32:00 |
| Discharge Time | 2142-08-09 17:30:00 |
| Admission Type | EW EMER. |
| Admission Location | EMERGENCY ROOM |
| Discharge Location | HOME HEALTH CARE |
| Insurance | Other |
| Language | ENGLISH |
| Marital Status | WIDOWED |
| Race/Ethnicity | WHITE |
| ED Registration | 2142-07-30 23:33:00 |
| ED Departure | 2142-07-31 01:41:00 |
| In-Hospital Mortality | No |
| Date of Death (overall) | 2146-02-09 |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| APR | 133 | RESPIRATORY FAILURE | 4.0 | 3.0 |
| HCFA | 208 | RESPIRATORY SYSTEM DIAGNOSIS W VENTILATOR SUPPORT <96 HOURS | N/A | N/A |

### Primary Diagnosis (seq_num = 1)

- **ICD-9 51881**: Acute respiratory failure

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2142-07-31 00:33:06 | N/A | MED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-9 `51881`: Acute respiratory failure
- (seq 2) ICD-9 `42833`: Acute on chronic diastolic heart failure
- (seq 3) ICD-9 `2763`: Alkalosis
- (seq 4) ICD-9 `4280`: Congestive heart failure, unspecified
- (seq 5) ICD-9 `515`: Postinflammatory pulmonary fibrosis

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-9 | `51881` | Acute respiratory failure |
| 2 | ICD-9 | `42833` | Acute on chronic diastolic heart failure |
| 3 | ICD-9 | `2763` | Alkalosis |
| 4 | ICD-9 | `4280` | Congestive heart failure, unspecified |
| 5 | ICD-9 | `515` | Postinflammatory pulmonary fibrosis |
| 6 | ICD-9 | `25000` | Diabetes mellitus without mention of complication, type II or unspecified type, not stated as uncontrolled |
| 7 | ICD-9 | `4019` | Unspecified essential hypertension |
| 8 | ICD-9 | `41401` | Coronary atherosclerosis of native coronary artery |
| 9 | ICD-9 | `3004` | Dysthymic disorder |
| 10 | ICD-9 | `4240` | Mitral valve disorders |
| 11 | ICD-9 | `7245` | Backache, unspecified |
| 12 | ICD-9 | `2859` | Anemia, unspecified |

## 5. ICU Stays

| Stay ID | First Care Unit | Last Care Unit | ICU Admit | ICU Discharge | LOS (days) |
|---|---|---|---|---|---|
| 34499716 | Medical Intensive Care Unit (MICU) | Medical Intensive Care Unit (MICU) | 2142-07-31 01:41:00 | 2142-08-03 21:05:58 | 3.81 |

## 6. Escalation / Severity Indicators

The following critical conditions or interventions were detected:

- **Arterial Line** (ICU procedure event)
- **Invasive Mechanical Ventilation** (ICU procedure event)
- **Respiratory Failure** (ICD diagnosis)

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2142-07-31 | ICD-9 | `9671` | Continuous invasive mechanical ventilation for less than 96 consecutive hours |
| 2 | 2142-07-31 | ICD-9 | `9604` | Insertion of endotracheal tube |
| 3 | 2142-07-31 | ICD-9 | `3897` | Central venous catheter placement with guidance |
| 4 | 2142-08-01 | ICD-9 | `966` | Enteral infusion of concentrated nutritional substances |

### ICU Procedure Events (from `icu/procedureevents.csv.gz`)

- Invasive Ventilation (category: 2-Ventilation, started: 2142-07-31 01:54:00, status: FinishedRunning)
- 20 Gauge (category: Access Lines - Peripheral, started: 2142-07-31 06:00:00, status: FinishedRunning)
- Multi Lumen (category: Access Lines - Invasive, started: 2142-07-31 08:18:00, status: FinishedRunning)
- Family updated by RN (category: 7-Communication, started: 2142-07-31 09:23:00, status: FinishedRunning)
- EKG (category: 4-Procedures, started: 2142-07-31 12:21:00, status: FinishedRunning)
- Trans Esophageal Echo (category: 5-Imaging, started: 2142-07-31 14:30:00, status: FinishedRunning)
- Arterial Line (category: Access Lines - Invasive, started: 2142-07-31 19:00:00, status: FinishedRunning)
- Blood Cultured (category: 6-Cultures, started: 2142-08-01 10:12:00, status: FinishedRunning)
- Urine Culture (category: 6-Cultures, started: 2142-08-01 11:22:00, status: FinishedRunning)
- Sputum Culture (category: 6-Cultures, started: 2142-08-01 15:17:00, status: FinishedRunning)
- Extubation (category: 1-Intubation/Extubation, started: 2142-08-02 10:44:00, status: FinishedRunning)
- 18 Gauge (category: Access Lines - Peripheral, started: 2142-08-03 08:00:00, status: FinishedRunning)

## 8. Critical Findings (Charted Events)

- **Ventilator Mode** (first noted: 2142-07-31 01:44:00)
- **Ventilator Type** (first noted: 2142-07-31 01:00:00)
- **Ventilator Tank #2** (first noted: 2142-07-31 01:00:00)
- **Seizure Activity** (first noted: 2142-08-03 08:11:00)

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2142-07-30 23:33:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2142-07-30 23:33:00 | Transfer | → Emergency Department (ED) |
| 2142-07-31 00:32:00 | Admission | Admitted from EMERGENCY ROOM (EW EMER.) |
| 2142-07-31 01:41:00 | ED Departure | Left Emergency Dept. |
| 2142-07-31 01:41:00 | ICU Admission | Medical Intensive Care Unit (MICU) (LOS: 3.8 days) |
| 2142-08-03 21:05:58 | Transfer | → Medicine (transfer) |
| 2142-08-09 17:30:00 | Discharge | To HOME HEALTH CARE |

## 10. Missing / Ambiguous Data

- No obvious missing critical fields detected.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
