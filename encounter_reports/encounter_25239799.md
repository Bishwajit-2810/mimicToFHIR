# Encounter Report — HADM 25239799

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 25239799 |
| Subject ID | 10005348 |
| Patient Sex | M |
| Patient Anchor Age (at anchor year) | 76 |
| Anchor Year | 2128 |
| Admission Time | 2130-10-26 17:03:00 |
| Discharge Time | 2130-11-02 16:00:00 |
| Admission Type | EW EMER. |
| Admission Location | PROCEDURE SITE |
| Discharge Location | SKILLED NURSING FACILITY |
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
| HCFA | 217 | CARDIAC VALVE & OTH MAJ CARDIOTHORACIC PROC W CARD CATH W CC | N/A | N/A |
| APR | 162 | CARDIAC VALVE PROCEDURES W AMI OR COMPLEX PDX | 3.0 | 2.0 |

### Primary Diagnosis (seq_num = 1)

- **ICD-9 4241**: Aortic valve disorders

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2130-10-26 17:04:03 | N/A | CMED |
| 2130-10-27 12:06:16 | CMED | CSURG |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-9 `4241`: Aortic valve disorders
- (seq 2) ICD-9 `42612`: Mobitz (type) II atrioventricular block
- (seq 3) ICD-9 `5119`: Unspecified pleural effusion
- (seq 4) ICD-9 `2662`: Other B-complex deficiencies
- (seq 5) ICD-9 `42731`: Atrial fibrillation

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-9 | `4241` | Aortic valve disorders |
| 2 | ICD-9 | `42612` | Mobitz (type) II atrioventricular block |
| 3 | ICD-9 | `5119` | Unspecified pleural effusion |
| 4 | ICD-9 | `2662` | Other B-complex deficiencies |
| 5 | ICD-9 | `42731` | Atrial fibrillation |
| 6 | ICD-9 | `2875` | Thrombocytopenia, unspecified |
| 7 | ICD-9 | `5180` | Pulmonary collapse |
| 8 | ICD-9 | `9971` | Cardiac complications, not elsewhere classified |
| 9 | ICD-9 | `41401` | Coronary atherosclerosis of native coronary artery |
| 10 | ICD-9 | `4019` | Unspecified essential hypertension |
| 11 | ICD-9 | `71594` | Osteoarthrosis, unspecified whether generalized or localized, hand |
| 12 | ICD-9 | `311` | Depressive disorder, not elsewhere classified |
| 13 | ICD-9 | `2724` | Other and unspecified hyperlipidemia |
| 14 | ICD-9 | `2809` | Iron deficiency anemia, unspecified |
| 15 | ICD-9 | `4580` | Orthostatic hypotension |
| 16 | ICD-9 | `3659` | Unspecified glaucoma |
| 17 | ICD-9 | `4400` | Atherosclerosis of aorta |
| 18 | ICD-9 | `7224` | Degeneration of cervical intervertebral disc |
| 19 | ICD-9 | `72252` | Degeneration of lumbar or lumbosacral intervertebral disc |
| 20 | ICD-9 | `E8781` | Surgical operation with implant of artificial internal device causing abnormal patient reaction, or later complication,without mention of misadventure at time of operation |
| 21 | ICD-9 | `V707` | Examination of participant in clinical trial |
| 22 | ICD-9 | `V1046` | Personal history of malignant neoplasm of prostate |
| 23 | ICD-9 | `V1011` | Personal history of malignant neoplasm of bronchus and lung |
| 24 | ICD-9 | `V1083` | Personal history of other malignant neoplasm of skin |
| 25 | ICD-9 | `V173` | Family history of ischemic heart disease |
| 26 | ICD-9 | `V1582` | Personal history of tobacco use |
| 27 | ICD-9 | `V4582` | Percutaneous transluminal coronary angioplasty status |
| 28 | ICD-9 | `V113` | Personal history of alcoholism |

## 5. ICU Stays

| Stay ID | First Care Unit | Last Care Unit | ICU Admit | ICU Discharge | LOS (days) |
|---|---|---|---|---|---|
| 34629895 | Cardiac Vascular Intensive Care Unit (CVICU) | Cardiac Vascular Intensive Care Unit (CVICU) | 2130-10-27 12:06:00 | 2130-10-29 12:05:02 | 2.00 |

## 6. Escalation / Severity Indicators

The following critical conditions or interventions were detected:

- **Arterial Line** (ICU procedure event)
- **Invasive Mechanical Ventilation** (ICU procedure event)

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2130-10-27 | ICD-9 | `3521` | Open and other replacement of aortic valve with tissue graft |
| 2 | 2130-10-26 | ICD-9 | `3722` | Left heart cardiac catheterization |
| 3 | 2130-10-27 | ICD-9 | `3611` | (Aorto)coronary bypass of one coronary artery |
| 4 | 2130-10-26 | ICD-9 | `8856` | Coronary arteriography using two catheters |
| 5 | 2130-10-27 | ICD-9 | `3961` | Extracorporeal circulation auxiliary to open heart surgery |
| 6 | 2130-10-27 | ICD-9 | `3893` | Venous catheterization, not elsewhere classified |

### ICU Procedure Events (from `icu/procedureevents.csv.gz`)

- Invasive Ventilation (category: 2-Ventilation, started: 2130-10-27 16:45:00, status: FinishedRunning)
- 20 Gauge (category: Access Lines - Peripheral, started: 2130-10-27 17:00:00, status: FinishedRunning)
- 18 Gauge (category: Access Lines - Peripheral, started: 2130-10-27 17:00:00, status: FinishedRunning)
- 14 Gauge (category: Access Lines - Peripheral, started: 2130-10-27 17:00:00, status: FinishedRunning)
- Nasal Swab (category: 6-Cultures, started: 2130-10-27 17:00:00, status: FinishedRunning)
- OR Received (category: 3-Significant Events, started: 2130-10-27 17:00:00, status: FinishedRunning)
- Arterial Line (category: Access Lines - Invasive, started: 2130-10-27 17:00:00, status: FinishedRunning)
- AVA (category: Access Lines - Invasive, started: 2130-10-27 17:05:00, status: FinishedRunning)
- PA Catheter (category: Access Lines - Invasive, started: 2130-10-27 17:06:00, status: FinishedRunning)
- EKG (category: 4-Procedures, started: 2130-10-27 18:00:00, status: FinishedRunning)
- Chest X-Ray (category: 5-Imaging, started: 2130-10-27 21:45:00, status: FinishedRunning)
- Chest Tube Removed (category: 4-Procedures, started: 2130-10-28 10:20:00, status: FinishedRunning)

## 8. Critical Findings (Charted Events)

- **Ventilator Type** (first noted: 2130-10-27 16:00:00)
- **Ventilator Mode** (first noted: 2130-10-27 16:00:00)
- **Ventilator Tank #2** (first noted: 2130-10-27 20:00:00)
- **Known difficult intubation** (first noted: 2130-10-27 16:00:00)
- **Temporary Pacemaker Rate** (first noted: 2130-10-27 17:00:00)
- **Temporary Pacemaker Wires Venticular** (first noted: 2130-10-27 17:00:00)
- **Temporary Pacemaker Wires Atrial** (first noted: 2130-10-27 17:00:00)

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2130-10-26 17:03:00 | Admission | Admitted from PROCEDURE SITE (EW EMER.) |
| 2130-10-27 11:01:08 | Transfer | → Discharge Lounge (transfer) |
| 2130-10-27 12:06:00 | ICU Admission | Cardiac Vascular Intensive Care Unit (CVICU) (LOS: 2.0 days) |
| 2130-10-27 12:06:00 | Transfer | → Cardiac Vascular Intensive Care Unit (CVICU) (transfer) |
| 2130-10-29 12:05:02 | Transfer | → Cardiac Surgery (transfer) |
| 2130-11-02 16:00:00 | Discharge | To SKILLED NURSING FACILITY |

## 10. Missing / Ambiguous Data

- No ED registration time — admission may not have gone through ED.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
