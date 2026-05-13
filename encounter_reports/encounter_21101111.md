# Encounter Report — HADM 21101111

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 21101111 |
| Subject ID | 10018845 |
| Patient Sex | M |
| Patient Anchor Age (at anchor year) | 91 |
| Anchor Year | 2184 |
| Admission Time | 2184-10-08 02:28:00 |
| Discharge Time | 2184-10-11 17:00:00 |
| Admission Type | EW EMER. |
| Admission Location | EMERGENCY ROOM |
| Discharge Location | REHAB |
| Insurance | Other |
| Language | ENGLISH |
| Marital Status | MARRIED |
| Race/Ethnicity | WHITE |
| ED Registration | 2184-10-07 22:35:00 |
| ED Departure | 2184-10-08 04:09:00 |
| In-Hospital Mortality | No |
| Date of Death (overall) | 2184-11-22 |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| APR | 20 | CRANIOTOMY FOR TRAUMA | 1.0 | 2.0 |
| HCFA | 26 | CRANIOTOMY & ENDOVASCULAR INTRACRANIAL PROCEDURES W CC | N/A | N/A |

### Primary Diagnosis (seq_num = 1)

- **ICD-9 85220**: Subdural hemorrhage following injury without mention of open intracranial wound, unspecified state of consciousness

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2184-10-08 02:29:52 | N/A | NSURG |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-9 `85220`: Subdural hemorrhage following injury without mention of open intracranial wound, unspecified state of consciousness
- (seq 2) ICD-9 `40391`: Hypertensive chronic kidney disease, unspecified, with chronic kidney disease stage V or end stage renal disease
- (seq 3) ICD-9 `5855`: Chronic kidney disease, Stage V
- (seq 4) ICD-9 `7843`: Aphasia
- (seq 5) ICD-9 `E8889`: Unspecified fall

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-9 | `85220` | Subdural hemorrhage following injury without mention of open intracranial wound, unspecified state of consciousness |
| 2 | ICD-9 | `40391` | Hypertensive chronic kidney disease, unspecified, with chronic kidney disease stage V or end stage renal disease |
| 3 | ICD-9 | `5855` | Chronic kidney disease, Stage V |
| 4 | ICD-9 | `7843` | Aphasia |
| 5 | ICD-9 | `E8889` | Unspecified fall |
| 6 | ICD-9 | `E8490` | Home accidents |
| 7 | ICD-9 | `78451` | Dysarthria |
| 8 | ICD-9 | `2724` | Other and unspecified hyperlipidemia |
| 9 | ICD-9 | `78830` | Urinary incontinence, unspecified |
| 10 | ICD-9 | `78194` | Facial weakness |
| 11 | ICD-9 | `V4365` | Knee joint replacement |
| 12 | ICD-9 | `41401` | Coronary atherosclerosis of native coronary artery |

## 5. ICU Stays

| Stay ID | First Care Unit | Last Care Unit | ICU Admit | ICU Discharge | LOS (days) |
|---|---|---|---|---|---|
| 36427705 | Surgical Intensive Care Unit (SICU) | Surgical Intensive Care Unit (SICU) | 2184-10-08 04:09:00 | 2184-10-09 15:55:53 | 1.49 |

## 6. Escalation / Severity Indicators

The following critical conditions or interventions were detected:

- **Arterial Line** (ICU procedure event)

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2184-10-08 | ICD-9 | `0124` | Other craniotomy |

### ICU Procedure Events (from `icu/procedureevents.csv.gz`)

- 20 Gauge (category: Access Lines - Peripheral, started: 2184-10-08 04:35:00, status: FinishedRunning)
- Ultrasound (category: 5-Imaging, started: 2184-10-08 11:00:00, status: FinishedRunning)
- Family updated by RN (category: 7-Communication, started: 2184-10-08 11:45:00, status: FinishedRunning)
- EKG (category: 4-Procedures, started: 2184-10-08 12:50:00, status: FinishedRunning)
- Transthoracic Echo (category: 5-Imaging, started: 2184-10-08 13:00:00, status: FinishedRunning)
- 16 Gauge (category: Access Lines - Peripheral, started: 2184-10-08 17:30:00, status: FinishedRunning)
- Arterial Line (category: Access Lines - Invasive, started: 2184-10-08 17:30:00, status: FinishedRunning)
- CT scan (category: 5-Imaging, started: 2184-10-08 20:00:00, status: FinishedRunning)

## 8. Critical Findings (Charted Events)

- **Dialysis patient** (first noted: 2184-10-08 06:16:00)

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2184-10-07 22:35:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2184-10-07 22:35:00 | Transfer | → Emergency Department (ED) |
| 2184-10-08 02:28:00 | Admission | Admitted from EMERGENCY ROOM (EW EMER.) |
| 2184-10-08 04:09:00 | ED Departure | Left Emergency Dept. |
| 2184-10-08 04:09:00 | ICU Admission | Surgical Intensive Care Unit (SICU) (LOS: 1.5 days) |
| 2184-10-09 15:55:53 | Transfer | → Neurology (transfer) |
| 2184-10-11 17:00:00 | Discharge | To REHAB |

## 10. Missing / Ambiguous Data

- No obvious missing critical fields detected.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
