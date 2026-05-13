# Encounter Report — HADM 28324362

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 28324362 |
| Subject ID | 10009035 |
| Patient Sex | M |
| Patient Anchor Age (at anchor year) | 28 |
| Anchor Year | 2161 |
| Admission Time | 2161-04-27 07:15:00 |
| Discharge Time | 2161-05-01 13:45:00 |
| Admission Type | ELECTIVE |
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
| APR | 163 | CARDIAC VALVE PROCEDURES W/O AMI OR COMPLEX PDX | 1.0 | 1.0 |
| HCFA | 220 | CARDIAC VALVE & OTH MAJ CARDIOTHORACIC PROC W/O CARD CATH W CC | N/A | N/A |

### Primary Diagnosis (seq_num = 1)

- **ICD-9 4240**: Mitral valve disorders

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2161-04-27 04:47:09 | N/A | CSURG |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-9 `4240`: Mitral valve disorders
- (seq 2) ICD-9 `5121`: Iatrogenic pneumothorax
- (seq 3) ICD-9 `7873`: Flatulence, eructation, and gas pain
- (seq 4) ICD-9 `V4589`: Other postprocedural status

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-9 | `4240` | Mitral valve disorders |
| 2 | ICD-9 | `5121` | Iatrogenic pneumothorax |
| 3 | ICD-9 | `7873` | Flatulence, eructation, and gas pain |
| 4 | ICD-9 | `V4589` | Other postprocedural status |

## 5. ICU Stays

| Stay ID | First Care Unit | Last Care Unit | ICU Admit | ICU Discharge | LOS (days) |
|---|---|---|---|---|---|
| 38507547 | Cardiac Vascular Intensive Care Unit (CVICU) | Cardiac Vascular Intensive Care Unit (CVICU) | 2161-04-27 10:38:12 | 2161-04-28 15:06:17 | 1.19 |

## 6. Escalation / Severity Indicators

The following critical conditions or interventions were detected:

- **Arterial Line** (ICU procedure event)
- **Invasive Mechanical Ventilation** (ICU procedure event)

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2161-04-27 | ICD-9 | `3512` | Open heart valvuloplasty of mitral valve without replacement |
| 2 | 2161-04-27 | ICD-9 | `3961` | Extracorporeal circulation auxiliary to open heart surgery |

### ICU Procedure Events (from `icu/procedureevents.csv.gz`)

- Invasive Ventilation (category: 2-Ventilation, started: 2161-04-27 11:55:00, status: FinishedRunning)
- OR Received (category: 3-Significant Events, started: 2161-04-27 11:55:00, status: FinishedRunning)
- Cordis/Introducer (category: Access Lines - Invasive, started: 2161-04-27 12:12:00, status: FinishedRunning)
- Nasal Swab (category: 6-Cultures, started: 2161-04-27 12:12:00, status: FinishedRunning)
- Chest X-Ray (category: 5-Imaging, started: 2161-04-27 12:12:00, status: FinishedRunning)
- 16 Gauge (category: Access Lines - Peripheral, started: 2161-04-27 12:21:00, status: FinishedRunning)
- PA Catheter (category: Access Lines - Invasive, started: 2161-04-27 12:22:00, status: FinishedRunning)
- Arterial Line (category: Access Lines - Invasive, started: 2161-04-27 12:22:00, status: FinishedRunning)
- Extubation (category: 1-Intubation/Extubation, started: 2161-04-27 13:35:00, status: FinishedRunning)
- EKG (category: 4-Procedures, started: 2161-04-27 13:39:00, status: FinishedRunning)
- Chest Tube Placed (category: 4-Procedures, started: 2161-04-27 16:30:00, status: FinishedRunning)
- 22 Gauge (category: Access Lines - Peripheral, started: 2161-04-28 14:33:00, status: FinishedRunning)

## 8. Critical Findings (Charted Events)

- **Ventilator Type** (first noted: 2161-04-27 12:00:00)
- **Ventilator Mode** (first noted: 2161-04-27 12:00:00)
- **Code Status** (first noted: 2161-04-27 11:08:00)
- **Temporary Pacemaker Type** (first noted: 2161-04-27 16:00:00)
- **Temporary Pacemaker Wires Atrial** (first noted: 2161-04-27 16:00:00)
- **Temporary Pacemaker Wires Venticular** (first noted: 2161-04-27 16:00:00)
- **Dialysis patient** (first noted: 2161-04-27 11:10:00)

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2161-04-27 07:15:00 | Admission | Admitted from PHYSICIAN REFERRAL (ELECTIVE) |
| 2161-04-27 10:38:12 | ICU Admission | Cardiac Vascular Intensive Care Unit (CVICU) (LOS: 1.2 days) |
| 2161-04-27 10:38:12 | Transfer | → Cardiac Vascular Intensive Care Unit (CVICU) (transfer) |
| 2161-04-28 15:06:17 | Transfer | → Cardiac Surgery (transfer) |
| 2161-04-29 15:57:02 | Transfer | → Cardiac Surgery (transfer) |
| 2161-05-01 13:45:00 | Discharge | To HOME HEALTH CARE |

## 10. Missing / Ambiguous Data

- No ED registration time — admission may not have gone through ED.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
