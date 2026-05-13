# Encounter Report — HADM 20297618

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 20297618 |
| Subject ID | 10019385 |
| Patient Sex | M |
| Patient Anchor Age (at anchor year) | 44 |
| Anchor Year | 2180 |
| Admission Time | 2180-02-15 20:28:00 |
| Discharge Time | 2180-02-25 13:45:00 |
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

- **ICD-10 I25110**: Atherosclerotic heart disease of native coronary artery with unstable angina pectoris

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2180-02-15 20:28:58 | N/A | CMED |
| 2180-02-21 08:34:20 | CMED | CSURG |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-10 `I25110`: Atherosclerotic heart disease of native coronary artery with unstable angina pectoris
- (seq 2) ICD-10 `E669`: Obesity, unspecified
- (seq 3) ICD-10 `E785`: Hyperlipidemia, unspecified
- (seq 4) ICD-10 `Z955`: Presence of coronary angioplasty implant and graft
- (seq 5) ICD-10 `F17200`: Nicotine dependence, unspecified, uncomplicated

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-10 | `I25110` | Atherosclerotic heart disease of native coronary artery with unstable angina pectoris |
| 2 | ICD-10 | `E669` | Obesity, unspecified |
| 3 | ICD-10 | `E785` | Hyperlipidemia, unspecified |
| 4 | ICD-10 | `Z955` | Presence of coronary angioplasty implant and graft |
| 5 | ICD-10 | `F17200` | Nicotine dependence, unspecified, uncomplicated |
| 6 | ICD-10 | `Z6832` | Body mass index (BMI) 32.0-32.9, adult |
| 7 | ICD-10 | `F419` | Anxiety disorder, unspecified |
| 8 | ICD-10 | `Z7902` | Long term (current) use of antithrombotics/antiplatelets |
| 9 | ICD-10 | `Z8249` | Family history of ischemic heart disease and other diseases of the circulatory system |

## 5. ICU Stays

| Stay ID | First Care Unit | Last Care Unit | ICU Admit | ICU Discharge | LOS (days) |
|---|---|---|---|---|---|
| 39268883 | Cardiac Vascular Intensive Care Unit (CVICU) | Cardiac Vascular Intensive Care Unit (CVICU) | 2180-02-21 08:34:06 | 2180-02-22 16:05:14 | 1.31 |

## 6. Escalation / Severity Indicators

The following critical conditions or interventions were detected:

- **Arterial Line** (ICU procedure event)
- **Invasive Mechanical Ventilation** (ICU procedure event)

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2180-02-21 | ICD-10 | `02100Z9` | Bypass Coronary Artery, One Artery from Left Internal Mammary, Open Approach |
| 2 | 2180-02-21 | ICD-10 | `5A1221Z` | Performance of Cardiac Output, Continuous |

### ICU Procedure Events (from `icu/procedureevents.csv.gz`)

- Invasive Ventilation (category: 2-Ventilation, started: 2180-02-21 10:55:00, status: FinishedRunning)
- OR Received (category: 3-Significant Events, started: 2180-02-21 10:55:00, status: FinishedRunning)
- Arterial Line (category: Access Lines - Invasive, started: 2180-02-21 11:03:00, status: FinishedRunning)
- Multi Lumen (category: Access Lines - Invasive, started: 2180-02-21 11:04:00, status: FinishedRunning)
- 16 Gauge (category: Access Lines - Peripheral, started: 2180-02-21 11:04:00, status: FinishedRunning)
- 22 Gauge (category: Access Lines - Peripheral, started: 2180-02-21 11:05:00, status: FinishedRunning)
- Foley Catheter (category: GI/GU, started: 2180-02-21 12:10:00, status: FinishedRunning)
- EKG (category: 4-Procedures, started: 2180-02-21 15:19:00, status: FinishedRunning)
- Family updated by RN (category: 7-Communication, started: 2180-02-21 18:55:00, status: FinishedRunning)
- Chest Tube Removed (category: 4-Procedures, started: 2180-02-22 10:10:00, status: FinishedRunning)
- Chest X-Ray (category: 5-Imaging, started: 2180-02-22 10:30:00, status: FinishedRunning)

## 8. Critical Findings (Charted Events)

- **Ventilator Mode (Hamilton)** (first noted: 2180-02-21 11:00:00)
- **Ventilator Tank #2** (first noted: 2180-02-21 11:00:00)
- **Ventilator Type** (first noted: 2180-02-21 11:00:00)
- **Known difficult intubation** (first noted: 2180-02-21 11:00:00)
- **Code Status** (first noted: 2180-02-21 13:40:00)
- **Seizure Activity** (first noted: 2180-02-22 08:22:00)
- **Temporary Pacemaker Mode** (first noted: 2180-02-21 12:00:00)
- **Temporary Pacemaker Rate** (first noted: 2180-02-21 12:00:00)
- **Temporary Pacemaker Wires Venticular** (first noted: 2180-02-21 12:00:00)

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2180-02-15 20:28:00 | Admission | Admitted from TRANSFER FROM HOSPITAL (URGENT) |
| 2180-02-20 20:58:42 | Transfer | → Medicine/Cardiology (transfer) |
| 2180-02-21 06:34:21 | Transfer | → PACU (transfer) |
| 2180-02-21 08:34:06 | ICU Admission | Cardiac Vascular Intensive Care Unit (CVICU) (LOS: 1.3 days) |
| 2180-02-21 08:34:06 | Transfer | → Cardiac Vascular Intensive Care Unit (CVICU) (transfer) |
| 2180-02-22 16:05:14 | Transfer | → Cardiac Surgery (transfer) |
| 2180-02-25 13:45:00 | Discharge | To HOME HEALTH CARE |

## 10. Missing / Ambiguous Data

- No ED registration time — admission may not have gone through ED.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
