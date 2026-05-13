# Encounter Report — HADM 25129047

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 25129047 |
| Subject ID | 10038933 |
| Patient Sex | M |
| Patient Anchor Age (at anchor year) | 34 |
| Anchor Year | 2148 |
| Admission Time | 2148-09-10 12:09:00 |
| Discharge Time | 2148-09-23 12:18:00 |
| Admission Type | EW EMER. |
| Admission Location | EMERGENCY ROOM |
| Discharge Location | REHAB |
| Insurance | Other |
| Language | ENGLISH |
| Marital Status | SINGLE |
| Race/Ethnicity | WHITE |
| ED Registration | 2148-09-10 09:23:00 |
| ED Departure | 2148-09-10 13:19:00 |
| In-Hospital Mortality | No |
| Date of Death (overall) | N/A |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| APR | 951 | MODERATELY EXTENSIVE PROCEDURE UNRELATED TO PRINCIPAL DIAGNOSIS | 4.0 | 3.0 |
| HCFA | 981 | EXTENSIVE O.R. PROCEDURE UNRELATED TO PRINCIPAL DIAGNOSIS W MCC | N/A | N/A |

### Primary Diagnosis (seq_num = 1)

- **ICD-9 85186**: Other and unspecified cerebral laceration and contusion, without mention of open intracranial wound, with loss of consciousness of unspecified duration

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2148-09-10 12:10:02 | N/A | NSURG |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-9 `85186`: Other and unspecified cerebral laceration and contusion, without mention of open intracranial wound, with loss of consciousness of unspecified duration
- (seq 2) ICD-9 `5070`: Pneumonitis due to inhalation of food or vomitus
- (seq 3) ICD-9 `34830`: Encephalopathy, unspecified
- (seq 4) ICD-9 `2910`: Alcohol withdrawal delirium
- (seq 5) ICD-9 `2761`: Hyposmolality and/or hyponatremia

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-9 | `85186` | Other and unspecified cerebral laceration and contusion, without mention of open intracranial wound, with loss of consciousness of unspecified duration |
| 2 | ICD-9 | `5070` | Pneumonitis due to inhalation of food or vomitus |
| 3 | ICD-9 | `34830` | Encephalopathy, unspecified |
| 4 | ICD-9 | `2910` | Alcohol withdrawal delirium |
| 5 | ICD-9 | `2761` | Hyposmolality and/or hyponatremia |
| 6 | ICD-9 | `1120` | Candidiasis of mouth |
| 7 | ICD-9 | `E8809` | Accidental fall on or from other stairs or steps |
| 8 | ICD-9 | `78720` | Dysphagia, unspecified |
| 9 | ICD-9 | `30390` | Other and unspecified alcohol dependence, unspecified |
| 10 | ICD-9 | `25000` | Diabetes mellitus without mention of complication, type II or unspecified type, not stated as uncontrolled |
| 11 | ICD-9 | `4019` | Unspecified essential hypertension |
| 12 | ICD-9 | `78820` | Retention of urine, unspecified |

## 5. ICU Stays

| Stay ID | First Care Unit | Last Care Unit | ICU Admit | ICU Discharge | LOS (days) |
|---|---|---|---|---|---|
| 32166508 | Surgical Intensive Care Unit (SICU) | Surgical Intensive Care Unit (SICU) | 2148-09-10 13:19:00 | 2148-09-15 21:50:29 | 5.36 |

## 6. Escalation / Severity Indicators

The following critical conditions or interventions were detected:

- **Arterial Line** (ICU procedure event)
- **Invasive Mechanical Ventilation** (ICU procedure event)

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2148-09-11 | ICD-9 | `3329` | Other diagnostic procedures on lung or bronchus |
| 2 | 2148-09-20 | ICD-9 | `4311` | Percutaneous [endoscopic] gastrostomy [PEG] |
| 3 | 2148-09-10 | ICD-9 | `9671` | Continuous invasive mechanical ventilation for less than 96 consecutive hours |
| 4 | 2148-09-10 | ICD-9 | `966` | Enteral infusion of concentrated nutritional substances |

### ICU Procedure Events (from `icu/procedureevents.csv.gz`)

- Invasive Ventilation (category: 2-Ventilation, started: 2148-09-10 13:47:00, status: FinishedRunning)
- 18 Gauge (category: Access Lines - Peripheral, started: 2148-09-10 14:41:00, status: FinishedRunning)
- Chest X-Ray (category: 5-Imaging, started: 2148-09-10 18:00:00, status: FinishedRunning)
- 20 Gauge (category: Access Lines - Peripheral, started: 2148-09-10 18:05:00, status: FinishedRunning)
- 16 Gauge (category: Access Lines - Peripheral, started: 2148-09-10 20:51:00, status: FinishedRunning)
- Arterial Line (category: Access Lines - Invasive, started: 2148-09-10 23:00:00, status: FinishedRunning)
- Extubation (category: 1-Intubation/Extubation, started: 2148-09-11 14:00:00, status: FinishedRunning)
- CT scan (category: 5-Imaging, started: 2148-09-12 04:30:00, status: FinishedRunning)
- 22 Gauge (category: Access Lines - Peripheral, started: 2148-09-13 16:31:00, status: FinishedRunning)
- PICC Line (category: Access Lines - Invasive, started: 2148-09-15 09:17:00, status: FinishedRunning)
- Nasal Swab (category: 6-Cultures, started: 2148-09-15 14:59:00, status: FinishedRunning)

## 8. Critical Findings (Charted Events)

- **Ventilator Tank #2** (first noted: 2148-09-10 13:00:00)
- **Ventilator Type** (first noted: 2148-09-10 13:00:00)
- **Ventilator Tank #1** (first noted: 2148-09-10 13:00:00)
- **Known difficult intubation** (first noted: 2148-09-10 13:00:00)
- **Seizure** (first noted: 2148-09-10 20:51:00)
- **Seizure Activity** (first noted: 2148-09-11 08:00:00)

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2148-09-10 09:23:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2148-09-10 09:23:00 | Transfer | → Emergency Department (ED) |
| 2148-09-10 12:09:00 | Admission | Admitted from EMERGENCY ROOM (EW EMER.) |
| 2148-09-10 13:19:00 | ED Departure | Left Emergency Dept. |
| 2148-09-10 13:19:00 | ICU Admission | Surgical Intensive Care Unit (SICU) (LOS: 5.4 days) |
| 2148-09-15 21:50:29 | Transfer | → Neurology (transfer) |
| 2148-09-16 21:48:18 | Transfer | → Neurology (transfer) |
| 2148-09-23 00:06:07 | Transfer | → Neurology (transfer) |
| 2148-09-23 12:18:00 | Discharge | To REHAB |

## 10. Missing / Ambiguous Data

- No obvious missing critical fields detected.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
