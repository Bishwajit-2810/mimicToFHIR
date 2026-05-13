# Encounter Report — HADM 23251352

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 23251352 |
| Subject ID | 10004457 |
| Patient Sex | M |
| Patient Anchor Age (at anchor year) | 65 |
| Anchor Year | 2140 |
| Admission Time | 2141-12-17 11:00:00 |
| Discharge Time | 2141-12-21 15:56:00 |
| Admission Type | SURGICAL SAME DAY ADMISSION |
| Admission Location | PHYSICIAN REFERRAL |
| Discharge Location | REHAB |
| Insurance | Medicare |
| Language | ENGLISH |
| Marital Status | SINGLE |
| Race/Ethnicity | OTHER |
| ED Registration | N/A |
| ED Departure | N/A |
| In-Hospital Mortality | No |
| Date of Death (overall) | N/A |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| HCFA | 221 | CARDIAC VALVE & OTH MAJ CARDIOTHORACIC PROC W/O CARD CATH W/O CC/MCC | N/A | N/A |
| APR | 163 | CARDIAC VALVE PROCEDURES W/O AMI OR COMPLEX PDX | 2.0 | 2.0 |

### Primary Diagnosis (seq_num = 1)

- **ICD-9 3968**: Multiple involvement of mitral and aortic valves

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2141-12-17 02:40:01 | N/A | CSURG |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-9 `3968`: Multiple involvement of mitral and aortic valves
- (seq 2) ICD-9 `41401`: Coronary atherosclerosis of native coronary artery
- (seq 3) ICD-9 `V4582`: Percutaneous transluminal coronary angioplasty status
- (seq 4) ICD-9 `4142`: Chronic total occlusion of coronary artery
- (seq 5) ICD-9 `V1046`: Personal history of malignant neoplasm of prostate

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-9 | `3968` | Multiple involvement of mitral and aortic valves |
| 2 | ICD-9 | `41401` | Coronary atherosclerosis of native coronary artery |
| 3 | ICD-9 | `V4582` | Percutaneous transluminal coronary angioplasty status |
| 4 | ICD-9 | `4142` | Chronic total occlusion of coronary artery |
| 5 | ICD-9 | `V1046` | Personal history of malignant neoplasm of prostate |
| 6 | ICD-9 | `V1079` | Personal history of other lymphatic and hematopoietic neoplasms |
| 7 | ICD-9 | `2724` | Other and unspecified hyperlipidemia |
| 8 | ICD-9 | `V8741` | Personal history of antineoplastic chemotherapy |
| 9 | ICD-9 | `V153` | Personal history of irradiation, presenting hazards to health |
| 10 | ICD-9 | `V1582` | Personal history of tobacco use |
| 11 | ICD-9 | `49390` | Asthma, unspecified type, unspecified |

## 5. ICU Stays

| Stay ID | First Care Unit | Last Care Unit | ICU Admit | ICU Discharge | LOS (days) |
|---|---|---|---|---|---|
| 31494479 | Cardiac Vascular Intensive Care Unit (CVICU) | Cardiac Vascular Intensive Care Unit (CVICU) | 2141-12-17 10:24:25 | 2141-12-18 14:16:17 | 1.16 |

## 6. Escalation / Severity Indicators

The following critical conditions or interventions were detected:

- **Arterial Line** (ICU procedure event)
- **Invasive Mechanical Ventilation** (ICU procedure event)

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2141-12-17 | ICD-9 | `3521` | Open and other replacement of aortic valve with tissue graft |
| 2 | 2141-12-17 | ICD-9 | `3611` | (Aorto)coronary bypass of one coronary artery |
| 3 | 2141-12-17 | ICD-9 | `3961` | Extracorporeal circulation auxiliary to open heart surgery |

### ICU Procedure Events (from `icu/procedureevents.csv.gz`)

- Invasive Ventilation (category: 2-Ventilation, started: 2141-12-17 14:25:00, status: FinishedRunning)
- Cordis/Introducer (category: Access Lines - Invasive, started: 2141-12-17 14:25:00, status: FinishedRunning)
- CCO PAC (category: Access Lines - Invasive, started: 2141-12-17 14:25:00, status: FinishedRunning)
- 16 Gauge (category: Access Lines - Peripheral, started: 2141-12-17 14:25:00, status: FinishedRunning)
- OR Received (category: 3-Significant Events, started: 2141-12-17 14:25:00, status: FinishedRunning)
- Arterial Line (category: Access Lines - Invasive, started: 2141-12-17 14:25:00, status: FinishedRunning)
- EKG (category: 4-Procedures, started: 2141-12-17 14:36:00, status: FinishedRunning)
- Nasal Swab (category: 6-Cultures, started: 2141-12-17 14:36:00, status: FinishedRunning)
- Chest X-Ray (category: 5-Imaging, started: 2141-12-17 15:43:00, status: FinishedRunning)
- Extubation (category: 1-Intubation/Extubation, started: 2141-12-17 18:04:00, status: FinishedRunning)
- Chest Tube Removed (category: 4-Procedures, started: 2141-12-18 09:30:00, status: FinishedRunning)

## 8. Critical Findings (Charted Events)

- **Ventilator Mode** (first noted: 2141-12-17 14:25:00)
- **Ventilator Type** (first noted: 2141-12-17 14:27:00)
- **Known difficult intubation** (first noted: 2141-12-17 14:27:00)
- **Code Status** (first noted: 2141-12-17 12:18:00)
- **Temporary Pacemaker Wires Atrial** (first noted: 2141-12-17 15:00:00)
- **Temporary Pacemaker Type** (first noted: 2141-12-17 15:00:00)
- **Temporary Pacemaker Mode** (first noted: 2141-12-17 15:00:00)

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2141-12-17 10:24:25 | ICU Admission | Cardiac Vascular Intensive Care Unit (CVICU) (LOS: 1.2 days) |
| 2141-12-17 10:24:25 | Transfer | → Cardiac Vascular Intensive Care Unit (CVICU) (transfer) |
| 2141-12-17 11:00:00 | Admission | Admitted from PHYSICIAN REFERRAL (SURGICAL SAME DAY ADMISSION) |
| 2141-12-18 14:16:17 | Transfer | → Cardiac Surgery (transfer) |
| 2141-12-19 10:38:45 | Transfer | → Cardiac Surgery (transfer) |
| 2141-12-21 15:56:00 | Discharge | To REHAB |

## 10. Missing / Ambiguous Data

- No ED registration time — admission may not have gone through ED.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
