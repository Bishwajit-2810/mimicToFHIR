# Encounter Report — HADM 27505812

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 27505812 |
| Subject ID | 10011398 |
| Patient Sex | M |
| Patient Anchor Age (at anchor year) | 67 |
| Anchor Year | 2146 |
| Admission Time | 2146-12-15 07:15:00 |
| Discharge Time | 2146-12-19 13:37:00 |
| Admission Type | SURGICAL SAME DAY ADMISSION |
| Admission Location | PHYSICIAN REFERRAL |
| Discharge Location | HOME HEALTH CARE |
| Insurance | Other |
| Language | ENGLISH |
| Marital Status | MARRIED |
| Race/Ethnicity | HISPANIC OR LATINO |
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

- **ICD-9 41401**: Coronary atherosclerosis of native coronary artery

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2146-12-15 04:53:55 | N/A | CSURG |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-9 `41401`: Coronary atherosclerosis of native coronary artery
- (seq 2) ICD-9 `4239`: Unspecified disease of pericardium
- (seq 3) ICD-9 `4111`: Intermediate coronary syndrome
- (seq 4) ICD-9 `4019`: Unspecified essential hypertension
- (seq 5) ICD-9 `2724`: Other and unspecified hyperlipidemia

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-9 | `41401` | Coronary atherosclerosis of native coronary artery |
| 2 | ICD-9 | `4239` | Unspecified disease of pericardium |
| 3 | ICD-9 | `4111` | Intermediate coronary syndrome |
| 4 | ICD-9 | `4019` | Unspecified essential hypertension |
| 5 | ICD-9 | `2724` | Other and unspecified hyperlipidemia |
| 6 | ICD-9 | `5641` | Irritable bowel syndrome |
| 7 | ICD-9 | `4779` | Allergic rhinitis, cause unspecified |
| 8 | ICD-9 | `60000` | Hypertrophy (benign) of prostate without urinary obstruction and other lower urinary tract symptom (LUTS) |
| 9 | ICD-9 | `V1301` | Personal history of urinary calculi |
| 10 | ICD-9 | `V1272` | Personal history of colonic polyps |

## 5. ICU Stays

| Stay ID | First Care Unit | Last Care Unit | ICU Admit | ICU Discharge | LOS (days) |
|---|---|---|---|---|---|
| 37648963 | Cardiac Vascular Intensive Care Unit (CVICU) | Cardiac Vascular Intensive Care Unit (CVICU) | 2146-12-15 09:54:58 | 2146-12-16 10:53:06 | 1.04 |

## 6. Escalation / Severity Indicators

The following critical conditions or interventions were detected:

- **Arterial Line** (ICU procedure event)

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2146-12-15 | ICD-9 | `3614` | (Aorto)coronary bypass of four or more coronary arteries |
| 2 | 2146-12-15 | ICD-9 | `3615` | Single internal mammary-coronary artery bypass |
| 3 | 2146-12-15 | ICD-9 | `3961` | Extracorporeal circulation auxiliary to open heart surgery |

### ICU Procedure Events (from `icu/procedureevents.csv.gz`)

- OR Received (category: 3-Significant Events, started: 2146-12-15 12:30:00, status: FinishedRunning)
- Chest X-Ray (category: 5-Imaging, started: 2146-12-15 12:40:00, status: FinishedRunning)
- Arterial Line (category: Access Lines - Invasive, started: 2146-12-15 12:46:00, status: FinishedRunning)
- Cordis/Introducer (category: Access Lines - Invasive, started: 2146-12-15 12:47:00, status: FinishedRunning)
- PA Catheter (category: Access Lines - Invasive, started: 2146-12-15 12:47:00, status: FinishedRunning)
- 16 Gauge (category: Access Lines - Peripheral, started: 2146-12-15 12:48:00, status: FinishedRunning)
- Family updated by RN (category: 7-Communication, started: 2146-12-15 13:24:00, status: FinishedRunning)
- Extubation (category: 1-Intubation/Extubation, started: 2146-12-15 15:20:00, status: FinishedRunning)
- EKG (category: 4-Procedures, started: 2146-12-16 03:00:00, status: FinishedRunning)
- 20 Gauge (category: Access Lines - Peripheral, started: 2146-12-16 08:00:00, status: FinishedRunning)

## 8. Critical Findings (Charted Events)

- **Ventilator Tank #1** (first noted: 2146-12-15 10:46:00)
- **Ventilator Mode** (first noted: 2146-12-15 12:30:00)
- **Ventilator Tank #2** (first noted: 2146-12-15 10:46:00)
- **Code Status** (first noted: 2146-12-15 19:26:00)
- **Temporary Pacemaker Wire Condition** (first noted: 2146-12-15 12:58:00)
- **Temporary Pacemaker Wires Venticular** (first noted: 2146-12-15 12:58:00)
- **Temporary Pacemaker Wires Atrial** (first noted: 2146-12-15 12:58:00)

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2146-12-15 07:15:00 | Admission | Admitted from PHYSICIAN REFERRAL (SURGICAL SAME DAY ADMISSION) |
| 2146-12-15 09:54:58 | ICU Admission | Cardiac Vascular Intensive Care Unit (CVICU) (LOS: 1.0 days) |
| 2146-12-15 09:54:58 | Transfer | → Cardiac Vascular Intensive Care Unit (CVICU) (transfer) |
| 2146-12-16 10:53:06 | Transfer | → Cardiac Surgery (transfer) |
| 2146-12-19 13:37:00 | Discharge | To HOME HEALTH CARE |

## 10. Missing / Ambiguous Data

- No ED registration time — admission may not have gone through ED.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
