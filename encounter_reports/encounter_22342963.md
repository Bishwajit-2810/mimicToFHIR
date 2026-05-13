# Encounter Report — HADM 22342963

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 22342963 |
| Subject ID | 10022017 |
| Patient Sex | M |
| Patient Anchor Age (at anchor year) | 59 |
| Anchor Year | 2189 |
| Admission Time | 2189-09-10 00:00:00 |
| Discharge Time | 2189-09-16 15:00:00 |
| Admission Type | SURGICAL SAME DAY ADMISSION |
| Admission Location | PHYSICIAN REFERRAL |
| Discharge Location | HOME HEALTH CARE |
| Insurance | Other |
| Language | ENGLISH |
| Marital Status | SINGLE |
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
| HCFA | 235 | CORONARY BYPASS W/O CARDIAC CATH W MCC | N/A | N/A |

### Primary Diagnosis (seq_num = 1)

- **ICD-10 I2510**: Atherosclerotic heart disease of native coronary artery without angina pectoris

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2189-09-10 06:52:51 | N/A | CSURG |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-10 `I2510`: Atherosclerotic heart disease of native coronary artery without angina pectoris
- (seq 2) ICD-10 `J810`: Acute pulmonary edema
- (seq 3) ICD-10 `I959`: Hypotension, unspecified
- (seq 4) ICD-10 `K5190`: Ulcerative colitis, unspecified, without complications
- (seq 5) ICD-10 `I4891`: Unspecified atrial fibrillation

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-10 | `I2510` | Atherosclerotic heart disease of native coronary artery without angina pectoris |
| 2 | ICD-10 | `J810` | Acute pulmonary edema |
| 3 | ICD-10 | `I959` | Hypotension, unspecified |
| 4 | ICD-10 | `K5190` | Ulcerative colitis, unspecified, without complications |
| 5 | ICD-10 | `I4891` | Unspecified atrial fibrillation |
| 6 | ICD-10 | `D62` | Acute posthemorrhagic anemia |
| 7 | ICD-10 | `I9789` | Other postprocedural complications and disorders of the circulatory system, not elsewhere classified |
| 8 | ICD-10 | `I255` | Ischemic cardiomyopathy |
| 9 | ICD-10 | `Z933` | Colostomy status |
| 10 | ICD-10 | `R0902` | Hypoxemia |
| 11 | ICD-10 | `E119` | Type 2 diabetes mellitus without complications |
| 12 | ICD-10 | `E785` | Hyperlipidemia, unspecified |
| 13 | ICD-10 | `G4700` | Insomnia, unspecified |
| 14 | ICD-10 | `Y832` | Surgical operation with anastomosis, bypass or graft as the cause of abnormal reaction of the patient, or of later complication, without mention of misadventure at the time of the procedure |
| 15 | ICD-10 | `Y92230` | Patient room in hospital as the place of occurrence of the external cause |

## 5. ICU Stays

| Stay ID | First Care Unit | Last Care Unit | ICU Admit | ICU Discharge | LOS (days) |
|---|---|---|---|---|---|
| 39497668 | Cardiac Vascular Intensive Care Unit (CVICU) | Cardiac Vascular Intensive Care Unit (CVICU) | 2189-09-10 10:05:24 | 2189-09-14 21:27:28 | 4.47 |

## 6. Escalation / Severity Indicators

The following critical conditions or interventions were detected:

- **Arterial Line** (ICU procedure event)
- **Invasive Mechanical Ventilation** (ICU procedure event)
- **Non-Invasive Ventilation (NIV/BiPAP)** (ICU procedure event)

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2189-09-10 | ICD-10 | `02100Z9` | Bypass Coronary Artery, One Artery from Left Internal Mammary, Open Approach |
| 2 | 2189-09-10 | ICD-10 | `021209W` | Bypass Coronary Artery, Three Arteries from Aorta with Autologous Venous Tissue, Open Approach |
| 3 | 2189-09-10 | ICD-10 | `06BQ4ZZ` | Excision of Left Saphenous Vein, Percutaneous Endoscopic Approach |
| 4 | 2189-09-10 | ICD-10 | `5A1221Z` | Performance of Cardiac Output, Continuous |

### ICU Procedure Events (from `icu/procedureevents.csv.gz`)

- Invasive Ventilation (category: 2-Ventilation, started: 2189-09-10 12:20:00, status: FinishedRunning)
- OR Received (category: 3-Significant Events, started: 2189-09-10 12:26:00, status: FinishedRunning)
- CCO PAC (category: Access Lines - Invasive, started: 2189-09-10 13:07:00, status: FinishedRunning)
- 18 Gauge (category: Access Lines - Peripheral, started: 2189-09-10 13:07:00, status: FinishedRunning)
- Arterial Line (category: Access Lines - Invasive, started: 2189-09-10 13:07:00, status: FinishedRunning)
- Cordis/Introducer (category: Access Lines - Invasive, started: 2189-09-10 13:08:00, status: FinishedRunning)
- Foley Catheter (category: GI/GU, started: 2189-09-10 13:08:00, status: FinishedRunning)
- EKG (category: 4-Procedures, started: 2189-09-10 15:05:00, status: FinishedRunning)
- Extubation (category: 1-Intubation/Extubation, started: 2189-09-10 16:24:00, status: FinishedRunning)
- Chest Tube Removed (category: 4-Procedures, started: 2189-09-12 08:30:00, status: FinishedRunning)
- Chest X-Ray (category: 5-Imaging, started: 2189-09-12 10:30:00, status: FinishedRunning)
- Non-invasive Ventilation (category: 2-Ventilation, started: 2189-09-12 14:10:00, status: FinishedRunning)
- Urine Culture (category: 6-Cultures, started: 2189-09-13 08:30:00, status: FinishedRunning)
- Temporary Pacemaker Wires Discontinued (category: 4-Procedures, started: 2189-09-13 10:00:00, status: FinishedRunning)
- 20 Gauge (category: Access Lines - Peripheral, started: 2189-09-14 11:57:00, status: FinishedRunning)
- 22 Gauge (category: Access Lines - Peripheral, started: 2189-09-14 12:02:00, status: FinishedRunning)

## 8. Critical Findings (Charted Events)

- **Ventilator Mode** (first noted: 2189-09-10 12:00:00)
- **Ventilator Type** (first noted: 2189-09-10 12:00:00)
- **Ventilator Mode (Hamilton)** (first noted: 2189-09-12 14:00:00)
- **Known difficult intubation** (first noted: 2189-09-10 12:00:00)
- **Code Status** (first noted: 2189-09-10 11:13:00)
- **Temporary Pacemaker Rate** (first noted: 2189-09-10 13:26:00)
- **Temporary Pacemaker Wire Condition** (first noted: 2189-09-10 13:26:00)
- **Temporary Pacemaker Wires Venticular** (first noted: 2189-09-10 13:26:00)

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2189-09-10 00:00:00 | Admission | Admitted from PHYSICIAN REFERRAL (SURGICAL SAME DAY ADMISSION) |
| 2189-09-10 10:05:24 | ICU Admission | Cardiac Vascular Intensive Care Unit (CVICU) (LOS: 4.5 days) |
| 2189-09-10 10:05:24 | Transfer | → Cardiac Vascular Intensive Care Unit (CVICU) (transfer) |
| 2189-09-14 21:27:28 | Transfer | → Cardiac Surgery (transfer) |
| 2189-09-16 15:00:00 | Discharge | To HOME HEALTH CARE |

## 10. Missing / Ambiguous Data

- No ED registration time — admission may not have gone through ED.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
