# Encounter Report — HADM 24490144

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 24490144 |
| Subject ID | 10021118 |
| Patient Sex | M |
| Patient Anchor Age (at anchor year) | 62 |
| Anchor Year | 2161 |
| Admission Time | 2161-11-15 20:10:00 |
| Discharge Time | 2161-11-23 16:00:00 |
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
| APR | 166 | CORONARY BYPASS W/O AMI OR COMPLEX PDX | 3.0 | 2.0 |
| HCFA | 235 | CORONARY BYPASS W/O CARDIAC CATH W MCC | N/A | N/A |

### Primary Diagnosis (seq_num = 1)

- **ICD-10 I2510**: Atherosclerotic heart disease of native coronary artery without angina pectoris

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2161-11-15 20:10:55 | N/A | CMED |
| 2161-11-19 10:04:18 | CMED | CSURG |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-10 `I2510`: Atherosclerotic heart disease of native coronary artery without angina pectoris
- (seq 2) ICD-10 `I214`: Non-ST elevation (NSTEMI) myocardial infarction
- (seq 3) ICD-10 `D62`: Acute posthemorrhagic anemia
- (seq 4) ICD-10 `I10`: Essential (primary) hypertension
- (seq 5) ICD-10 `J45909`: Unspecified asthma, uncomplicated

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-10 | `I2510` | Atherosclerotic heart disease of native coronary artery without angina pectoris |
| 2 | ICD-10 | `I214` | Non-ST elevation (NSTEMI) myocardial infarction |
| 3 | ICD-10 | `D62` | Acute posthemorrhagic anemia |
| 4 | ICD-10 | `I10` | Essential (primary) hypertension |
| 5 | ICD-10 | `J45909` | Unspecified asthma, uncomplicated |
| 6 | ICD-10 | `E669` | Obesity, unspecified |
| 7 | ICD-10 | `F419` | Anxiety disorder, unspecified |
| 8 | ICD-10 | `G4700` | Insomnia, unspecified |
| 9 | ICD-10 | `Z87891` | Personal history of nicotine dependence |
| 10 | ICD-10 | `Z8249` | Family history of ischemic heart disease and other diseases of the circulatory system |
| 11 | ICD-10 | `Z7982` | Long term (current) use of aspirin |
| 12 | ICD-10 | `Z6835` | Body mass index (BMI) 35.0-35.9, adult |

## 5. ICU Stays

| Stay ID | First Care Unit | Last Care Unit | ICU Admit | ICU Discharge | LOS (days) |
|---|---|---|---|---|---|
| 36558922 | Cardiac Vascular Intensive Care Unit (CVICU) | Cardiac Vascular Intensive Care Unit (CVICU) | 2161-11-19 10:04:04 | 2161-11-20 21:45:42 | 1.49 |

## 6. Escalation / Severity Indicators

The following critical conditions or interventions were detected:

- **Arterial Line** (ICU procedure event)
- **Invasive Mechanical Ventilation** (ICU procedure event)

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2161-11-19 | ICD-10 | `02100Z9` | Bypass Coronary Artery, One Artery from Left Internal Mammary, Open Approach |
| 2 | 2161-11-19 | ICD-10 | `02110Z3` | Bypass Coronary Artery, Two Arteries from Coronary Artery, Open Approach |
| 3 | 2161-11-19 | ICD-10 | `06BP4ZZ` | Excision of Right Saphenous Vein, Percutaneous Endoscopic Approach |
| 4 | 2161-11-19 | ICD-10 | `5A1221Z` | Performance of Cardiac Output, Continuous |

### ICU Procedure Events (from `icu/procedureevents.csv.gz`)

- OR Received (category: 3-Significant Events, started: 2161-11-19 12:08:00, status: FinishedRunning)
- Invasive Ventilation (category: 2-Ventilation, started: 2161-11-19 12:10:00, status: FinishedRunning)
- Arterial Line (category: Access Lines - Invasive, started: 2161-11-19 12:13:00, status: FinishedRunning)
- Multi Lumen (category: Access Lines - Invasive, started: 2161-11-19 12:14:00, status: FinishedRunning)
- 18 Gauge (category: Access Lines - Peripheral, started: 2161-11-19 12:15:00, status: FinishedRunning)
- 20 Gauge (category: Access Lines - Peripheral, started: 2161-11-19 12:16:00, status: FinishedRunning)
- EKG (category: 4-Procedures, started: 2161-11-19 13:58:00, status: FinishedRunning)
- Extubation (category: 1-Intubation/Extubation, started: 2161-11-19 16:21:00, status: FinishedRunning)
- Family updated by RN (category: 7-Communication, started: 2161-11-20 09:00:00, status: FinishedRunning)
- Chest Tube Removed (category: 4-Procedures, started: 2161-11-20 09:15:00, status: FinishedRunning)
- Chest X-Ray (category: 5-Imaging, started: 2161-11-20 09:45:00, status: FinishedRunning)

## 8. Critical Findings (Charted Events)

- **Ventilator Mode** (first noted: 2161-11-19 12:00:00)
- **Ventilator Tank #1** (first noted: 2161-11-19 12:14:00)
- **Ventilator Type** (first noted: 2161-11-19 12:14:00)
- **Code Status** (first noted: 2161-11-19 23:05:00)
- **Temporary Pacemaker Wire Condition** (first noted: 2161-11-19 13:00:00)
- **Temporary Pacemaker Rate** (first noted: 2161-11-19 13:00:00)
- **Temporary Pacemaker Wires Venticular** (first noted: 2161-11-19 13:00:00)

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2161-11-15 20:10:00 | Admission | Admitted from TRANSFER FROM HOSPITAL (URGENT) |
| 2161-11-16 19:53:20 | Transfer | → Medicine/Cardiology (transfer) |
| 2161-11-19 07:16:15 | Transfer | → PACU (transfer) |
| 2161-11-19 10:04:04 | ICU Admission | Cardiac Vascular Intensive Care Unit (CVICU) (LOS: 1.5 days) |
| 2161-11-19 10:04:04 | Transfer | → Cardiac Vascular Intensive Care Unit (CVICU) (transfer) |
| 2161-11-20 21:45:42 | Transfer | → Cardiac Surgery (transfer) |
| 2161-11-23 16:00:00 | Discharge | To HOME HEALTH CARE |

## 10. Missing / Ambiguous Data

- No ED registration time — admission may not have gone through ED.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
