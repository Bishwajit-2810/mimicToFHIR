# Encounter Report — HADM 22675517

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 22675517 |
| Subject ID | 10013049 |
| Patient Sex | M |
| Patient Anchor Age (at anchor year) | 52 |
| Anchor Year | 2114 |
| Admission Time | 2114-06-20 10:15:00 |
| Discharge Time | 2114-06-24 16:45:00 |
| Admission Type | ELECTIVE |
| Admission Location | PHYSICIAN REFERRAL |
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
| HCFA | 230 | OTHER CARDIOTHORACIC PROCEDURES W/O CC/MCC | N/A | N/A |
| APR | 167 | OTHER CARDIOTHORACIC & THORACIC VASCULAR PROCEDURES | 1.0 | 1.0 |

### Primary Diagnosis (seq_num = 1)

- **ICD-9 2127**: Benign neoplasm of heart

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2114-06-20 02:41:44 | N/A | CSURG |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-9 `2127`: Benign neoplasm of heart
- (seq 2) ICD-9 `4556`: Unspecified hemorrhoids without mention of complication
- (seq 3) ICD-9 `53550`: Unspecified gastritis and gastroduodenitis, without mention of hemorrhage
- (seq 4) ICD-9 `V1272`: Personal history of colonic polyps
- (seq 5) ICD-9 `V173`: Family history of ischemic heart disease

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-9 | `2127` | Benign neoplasm of heart |
| 2 | ICD-9 | `4556` | Unspecified hemorrhoids without mention of complication |
| 3 | ICD-9 | `53550` | Unspecified gastritis and gastroduodenitis, without mention of hemorrhage |
| 4 | ICD-9 | `V1272` | Personal history of colonic polyps |
| 5 | ICD-9 | `V173` | Family history of ischemic heart disease |

## 5. ICU Stays

| Stay ID | First Care Unit | Last Care Unit | ICU Admit | ICU Discharge | LOS (days) |
|---|---|---|---|---|---|
| 35679826 | Cardiac Vascular Intensive Care Unit (CVICU) | Cardiac Vascular Intensive Care Unit (CVICU) | 2114-06-20 09:32:58 | 2114-06-21 13:47:44 | 1.18 |

## 6. Escalation / Severity Indicators

The following critical conditions or interventions were detected:

- **Arterial Line** (ICU procedure event)
- **Invasive Mechanical Ventilation** (ICU procedure event)

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2114-06-20 | ICD-9 | `3733` | Excision or destruction of other lesion or tissue of heart, open approach |
| 2 | 2114-06-20 | ICD-9 | `3561` | Repair of atrial septal defect with tissue graft |
| 3 | 2114-06-20 | ICD-9 | `3961` | Extracorporeal circulation auxiliary to open heart surgery |

### ICU Procedure Events (from `icu/procedureevents.csv.gz`)

- Invasive Ventilation (category: 2-Ventilation, started: 2114-06-20 10:55:00, status: FinishedRunning)
- Multi Lumen (category: Access Lines - Invasive, started: 2114-06-20 10:55:00, status: FinishedRunning)
- 18 Gauge (category: Access Lines - Peripheral, started: 2114-06-20 10:55:00, status: FinishedRunning)
- OR Received (category: 3-Significant Events, started: 2114-06-20 10:55:00, status: FinishedRunning)
- Arterial Line (category: Access Lines - Invasive, started: 2114-06-20 10:55:00, status: FinishedRunning)
- Nasal Swab (category: 6-Cultures, started: 2114-06-20 11:00:00, status: FinishedRunning)
- Chest X-Ray (category: 5-Imaging, started: 2114-06-20 11:27:00, status: FinishedRunning)
- Extubation (category: 1-Intubation/Extubation, started: 2114-06-20 13:15:00, status: FinishedRunning)
- EKG (category: 4-Procedures, started: 2114-06-21 05:56:00, status: FinishedRunning)
- 20 Gauge (category: Access Lines - Peripheral, started: 2114-06-21 07:30:00, status: FinishedRunning)
- Chest Tube Removed (category: 4-Procedures, started: 2114-06-21 08:46:00, status: FinishedRunning)

## 8. Critical Findings (Charted Events)

- **Ventilator Tank #2** (first noted: 2114-06-20 10:00:00)
- **Ventilator Tank #1** (first noted: 2114-06-20 10:00:00)
- **Ventilator Type** (first noted: 2114-06-20 10:00:00)
- **Known difficult intubation** (first noted: 2114-06-20 10:00:00)
- **Code Status** (first noted: 2114-06-20 10:07:00)
- **Temporary Pacemaker Wire Condition** (first noted: 2114-06-20 11:00:00)
- **Temporary Pacemaker Mode** (first noted: 2114-06-20 11:00:00)
- **Temporary Pacemaker Wires Venticular** (first noted: 2114-06-20 11:00:00)

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2114-06-20 09:32:58 | ICU Admission | Cardiac Vascular Intensive Care Unit (CVICU) (LOS: 1.2 days) |
| 2114-06-20 09:32:58 | Transfer | → Cardiac Vascular Intensive Care Unit (CVICU) (transfer) |
| 2114-06-20 10:15:00 | Admission | Admitted from PHYSICIAN REFERRAL (ELECTIVE) |
| 2114-06-21 13:47:44 | Transfer | → Cardiac Surgery (transfer) |
| 2114-06-24 16:45:00 | Discharge | To HOME HEALTH CARE |

## 10. Missing / Ambiguous Data

- No ED registration time — admission may not have gone through ED.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
