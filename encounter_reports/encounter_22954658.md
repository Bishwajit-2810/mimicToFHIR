# Encounter Report — HADM 22954658

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 22954658 |
| Subject ID | 10007058 |
| Patient Sex | M |
| Patient Anchor Age (at anchor year) | 48 |
| Anchor Year | 2167 |
| Admission Time | 2167-11-07 19:05:00 |
| Discharge Time | 2167-11-11 14:23:00 |
| Admission Type | EW EMER. |
| Admission Location | EMERGENCY ROOM |
| Discharge Location | HOME |
| Insurance | Other |
| Language | ENGLISH |
| Marital Status | MARRIED |
| Race/Ethnicity | WHITE |
| ED Registration | 2167-11-07 17:57:00 |
| ED Departure | 2167-11-07 20:22:00 |
| In-Hospital Mortality | No |
| Date of Death (overall) | N/A |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| APR | 174 | PERCUTANEOUS CORONARY INTERVENTION W AMI | 3.0 | 3.0 |
| HCFA | 250 | PERC CARDIOVASC PROC W/O CORONARY ARTERY STENT W MCC | N/A | N/A |

### Primary Diagnosis (seq_num = 1)

- **ICD-10 I214**: Non-ST elevation (NSTEMI) myocardial infarction

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2167-11-07 19:05:47 | N/A | VSURG |
| 2167-11-08 13:01:54 | VSURG | CMED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-10 `I214`: Non-ST elevation (NSTEMI) myocardial infarction
- (seq 2) ICD-10 `I7102`: Dissection of abdominal aorta
- (seq 3) ICD-10 `K219`: Gastro-esophageal reflux disease without esophagitis
- (seq 4) ICD-10 `Z23`: Encounter for immunization
- (seq 5) ICD-10 `Z7902`: Long term (current) use of antithrombotics/antiplatelets

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-10 | `I214` | Non-ST elevation (NSTEMI) myocardial infarction |
| 2 | ICD-10 | `I7102` | Dissection of abdominal aorta |
| 3 | ICD-10 | `K219` | Gastro-esophageal reflux disease without esophagitis |
| 4 | ICD-10 | `Z23` | Encounter for immunization |
| 5 | ICD-10 | `Z7902` | Long term (current) use of antithrombotics/antiplatelets |
| 6 | ICD-10 | `Z7982` | Long term (current) use of aspirin |

## 5. ICU Stays

| Stay ID | First Care Unit | Last Care Unit | ICU Admit | ICU Discharge | LOS (days) |
|---|---|---|---|---|---|
| 32506122 | Cardiac Vascular Intensive Care Unit (CVICU) | Cardiac Vascular Intensive Care Unit (CVICU) | 2167-11-07 20:22:00 | 2167-11-09 20:55:04 | 2.02 |

## 6. Escalation / Severity Indicators

_No escalation indicators detected from ICD codes or ICU procedure events._

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2167-11-08 | ICD-10 | `02C03ZZ` | Extirpation of Matter from Coronary Artery, One Artery, Percutaneous Approach |
| 2 | 2167-11-08 | ICD-10 | `B211YZZ` | Fluoroscopy of Multiple Coronary Arteries using Other Contrast |

### ICU Procedure Events (from `icu/procedureevents.csv.gz`)

- 18 Gauge (category: Access Lines - Peripheral, started: 2167-11-07 20:00:00, status: FinishedRunning)
- 20 Gauge (category: Access Lines - Peripheral, started: 2167-11-07 21:00:00, status: FinishedRunning)
- CT scan (category: 5-Imaging, started: 2167-11-07 22:00:00, status: FinishedRunning)
- Nasal Swab (category: 6-Cultures, started: 2167-11-07 23:30:00, status: FinishedRunning)
- EKG (category: 4-Procedures, started: 2167-11-08 04:00:00, status: FinishedRunning)
- Transthoracic Echo (category: 5-Imaging, started: 2167-11-08 08:42:00, status: FinishedRunning)
- Cardiac Cath (category: 4-Procedures, started: 2167-11-08 11:00:00, status: FinishedRunning)
- Family updated by RN (category: 7-Communication, started: 2167-11-09 08:30:00, status: FinishedRunning)
- Family updated by MD (category: 7-Communication, started: 2167-11-09 10:00:00, status: FinishedRunning)

## 8. Critical Findings (Charted Events)

_No critical chart events detected._

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2167-11-07 17:57:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2167-11-07 17:57:00 | Transfer | → Emergency Department (ED) |
| 2167-11-07 19:05:00 | Admission | Admitted from EMERGENCY ROOM (EW EMER.) |
| 2167-11-07 20:22:00 | ED Departure | Left Emergency Dept. |
| 2167-11-07 20:22:00 | ICU Admission | Cardiac Vascular Intensive Care Unit (CVICU) (LOS: 2.0 days) |
| 2167-11-09 20:55:04 | Transfer | → Medicine/Cardiology (transfer) |
| 2167-11-11 14:23:00 | Discharge | To HOME |

## 10. Missing / Ambiguous Data

- No obvious missing critical fields detected.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
