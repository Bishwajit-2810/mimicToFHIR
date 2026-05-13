# Encounter Report — HADM 24997044

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 24997044 |
| Subject ID | 10019172 |
| Patient Sex | F |
| Patient Anchor Age (at anchor year) | 63 |
| Anchor Year | 2118 |
| Admission Time | 2118-11-15 14:00:00 |
| Discharge Time | 2118-11-21 18:31:00 |
| Admission Type | ELECTIVE |
| Admission Location | PHYSICIAN REFERRAL |
| Discharge Location | HOME HEALTH CARE |
| Insurance | Other |
| Language | ENGLISH |
| Marital Status | N/A |
| Race/Ethnicity | UNABLE TO OBTAIN |
| ED Registration | N/A |
| ED Departure | N/A |
| In-Hospital Mortality | No |
| Date of Death (overall) | N/A |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| APR | 163 | CARDIAC VALVE PROCEDURES W/O AMI OR COMPLEX PDX | 2.0 | 2.0 |
| HCFA | 220 | CARDIAC VALVE & OTH MAJ CARDIOTHORACIC PROC W/O CARD CATH W CC | N/A | N/A |

### Primary Diagnosis (seq_num = 1)

- **ICD-9 4241**: Aortic valve disorders

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2118-11-15 14:47:26 | N/A | CSURG |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-9 `4241`: Aortic valve disorders
- (seq 2) ICD-9 `4271`: Paroxysmal ventricular tachycardia
- (seq 3) ICD-9 `4019`: Unspecified essential hypertension
- (seq 4) ICD-9 `42731`: Atrial fibrillation
- (seq 5) ICD-9 `71590`: Osteoarthrosis, unspecified whether generalized or localized, site unspecified

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-9 | `4241` | Aortic valve disorders |
| 2 | ICD-9 | `4271` | Paroxysmal ventricular tachycardia |
| 3 | ICD-9 | `4019` | Unspecified essential hypertension |
| 4 | ICD-9 | `42731` | Atrial fibrillation |
| 5 | ICD-9 | `71590` | Osteoarthrosis, unspecified whether generalized or localized, site unspecified |
| 6 | ICD-9 | `3051` | Tobacco use disorder |

## 5. ICU Stays

| Stay ID | First Care Unit | Last Care Unit | ICU Admit | ICU Discharge | LOS (days) |
|---|---|---|---|---|---|
| 32283063 | Cardiac Vascular Intensive Care Unit (CVICU) | Cardiac Vascular Intensive Care Unit (CVICU) | 2118-11-16 09:38:22 | 2118-11-19 20:34:51 | 3.46 |

## 6. Escalation / Severity Indicators

The following critical conditions or interventions were detected:

- **Arterial Line** (ICU procedure event)
- **Invasive Mechanical Ventilation** (ICU procedure event)

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2118-11-16 | ICD-9 | `3522` | Open and other replacement of aortic valve |
| 2 | 2118-11-16 | ICD-9 | `3961` | Extracorporeal circulation auxiliary to open heart surgery |

### ICU Procedure Events (from `icu/procedureevents.csv.gz`)

- Trauma line (category: Access Lines - Invasive, started: 2118-11-16 11:30:00, status: FinishedRunning)
- CCO PAC (category: Access Lines - Invasive, started: 2118-11-16 11:30:00, status: FinishedRunning)
- 20 Gauge (category: Access Lines - Peripheral, started: 2118-11-16 11:30:00, status: FinishedRunning)
- 18 Gauge (category: Access Lines - Peripheral, started: 2118-11-16 11:30:00, status: FinishedRunning)
- OR Received (category: 3-Significant Events, started: 2118-11-16 11:30:00, status: FinishedRunning)
- Arterial Line (category: Access Lines - Invasive, started: 2118-11-16 11:30:00, status: FinishedRunning)
- Invasive Ventilation (category: 2-Ventilation, started: 2118-11-16 11:36:00, status: FinishedRunning)
- Chest X-Ray (category: 5-Imaging, started: 2118-11-16 11:39:00, status: FinishedRunning)
- EKG (category: 4-Procedures, started: 2118-11-16 11:49:00, status: FinishedRunning)
- Extubation (category: 1-Intubation/Extubation, started: 2118-11-16 16:57:00, status: FinishedRunning)
- Chest Tube Removed (category: 4-Procedures, started: 2118-11-17 09:11:00, status: FinishedRunning)
- Temporary Pacemaker Wires Discontinued (category: 4-Procedures, started: 2118-11-19 07:15:00, status: FinishedRunning)

## 8. Critical Findings (Charted Events)

- **Ventilator Type** (first noted: 2118-11-16 12:00:00)
- **Ventilator Mode** (first noted: 2118-11-16 12:00:00)
- **Known difficult intubation** (first noted: 2118-11-16 12:00:00)
- **Code Status** (first noted: 2118-11-16 11:10:00)
- **Seizure Activity** (first noted: 2118-11-16 23:24:00)
- **Temporary Pacemaker Rate** (first noted: 2118-11-16 11:30:00)
- **Temporary Pacemaker Wire Condition** (first noted: 2118-11-16 11:30:00)
- **Temporary Pacemaker Mode** (first noted: 2118-11-16 11:30:00)

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2118-11-15 14:00:00 | Admission | Admitted from PHYSICIAN REFERRAL (ELECTIVE) |
| 2118-11-15 23:04:54 | Transfer | → Medicine/Cardiology (transfer) |
| 2118-11-16 07:08:10 | Transfer | → PACU (transfer) |
| 2118-11-16 09:38:22 | ICU Admission | Cardiac Vascular Intensive Care Unit (CVICU) (LOS: 3.5 days) |
| 2118-11-16 09:38:22 | Transfer | → Cardiac Vascular Intensive Care Unit (CVICU) (transfer) |
| 2118-11-17 18:09:08 | Transfer | → Cardiac Vascular Intensive Care Unit (CVICU) (transfer) |
| 2118-11-18 15:27:34 | Transfer | → Cardiac Vascular Intensive Care Unit (CVICU) (transfer) |
| 2118-11-19 20:34:51 | Transfer | → Cardiac Surgery (transfer) |
| 2118-11-21 18:31:00 | Discharge | To HOME HEALTH CARE |

## 10. Missing / Ambiguous Data

- No ED registration time — admission may not have gone through ED.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
