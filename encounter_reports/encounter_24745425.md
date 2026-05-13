# Encounter Report — HADM 24745425

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 24745425 |
| Subject ID | 10038992 |
| Patient Sex | M |
| Patient Anchor Age (at anchor year) | 70 |
| Anchor Year | 2185 |
| Admission Time | 2187-07-29 01:05:00 |
| Discharge Time | 2187-08-03 17:02:00 |
| Admission Type | SURGICAL SAME DAY ADMISSION |
| Admission Location | PHYSICIAN REFERRAL |
| Discharge Location | SKILLED NURSING FACILITY |
| Insurance | Medicare |
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
| APR | 163 | CARDIAC VALVE PROCEDURES W/O AMI OR COMPLEX PDX | 3.0 | 3.0 |
| HCFA | 220 | CARDIAC VALVE & OTH MAJ CARDIOTHORACIC PROC W/O CARD CATH W CC | N/A | N/A |

### Primary Diagnosis (seq_num = 1)

- **ICD-10 I082**: Rheumatic disorders of both aortic and tricuspid valves

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2187-07-29 01:06:12 | N/A | CSURG |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-10 `I082`: Rheumatic disorders of both aortic and tricuspid valves
- (seq 2) ICD-10 `I428`: Other cardiomyopathies
- (seq 3) ICD-10 `D696`: Thrombocytopenia, unspecified
- (seq 4) ICD-10 `I272`: Other secondary pulmonary hypertension
- (seq 5) ICD-10 `I130`: Hypertensive heart and chronic kidney disease with heart failure and stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-10 | `I082` | Rheumatic disorders of both aortic and tricuspid valves |
| 2 | ICD-10 | `I428` | Other cardiomyopathies |
| 3 | ICD-10 | `D696` | Thrombocytopenia, unspecified |
| 4 | ICD-10 | `I272` | Other secondary pulmonary hypertension |
| 5 | ICD-10 | `I130` | Hypertensive heart and chronic kidney disease with heart failure and stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease |
| 6 | ICD-10 | `N183` | Chronic kidney disease, stage 3 (moderate) |
| 7 | ICD-10 | `I5022` | Chronic systolic (congestive) heart failure |
| 8 | ICD-10 | `I471` | Supraventricular tachycardia |
| 9 | ICD-10 | `D62` | Acute posthemorrhagic anemia |
| 10 | ICD-10 | `J449` | Chronic obstructive pulmonary disease, unspecified |
| 11 | ICD-10 | `E785` | Hyperlipidemia, unspecified |
| 12 | ICD-10 | `G4733` | Obstructive sleep apnea (adult) (pediatric) |
| 13 | ICD-10 | `M109` | Gout, unspecified |
| 14 | ICD-10 | `E039` | Hypothyroidism, unspecified |
| 15 | ICD-10 | `E669` | Obesity, unspecified |
| 16 | ICD-10 | `Z87891` | Personal history of nicotine dependence |
| 17 | ICD-10 | `Z6829` | Body mass index (BMI) 29.0-29.9, adult |

## 5. ICU Stays

| Stay ID | First Care Unit | Last Care Unit | ICU Admit | ICU Discharge | LOS (days) |
|---|---|---|---|---|---|
| 37127068 | Cardiac Vascular Intensive Care Unit (CVICU) | Cardiac Vascular Intensive Care Unit (CVICU) | 2187-07-29 09:41:11 | 2187-07-30 13:42:51 | 1.17 |

## 6. Escalation / Severity Indicators

The following critical conditions or interventions were detected:

- **Arterial Line** (ICU procedure event)
- **Invasive Mechanical Ventilation** (ICU procedure event)

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2187-07-29 | ICD-10 | `02RF08Z` | Replacement of Aortic Valve with Zooplastic Tissue, Open Approach |
| 2 | 2187-07-29 | ICD-10 | `5A1221Z` | Performance of Cardiac Output, Continuous |

### ICU Procedure Events (from `icu/procedureevents.csv.gz`)

- Invasive Ventilation (category: 2-Ventilation, started: 2187-07-29 11:45:00, status: FinishedRunning)
- 16 Gauge (category: Access Lines - Peripheral, started: 2187-07-29 11:50:00, status: FinishedRunning)
- PA Catheter (category: Access Lines - Invasive, started: 2187-07-29 11:50:00, status: FinishedRunning)
- MAC (category: Access Lines - Invasive, started: 2187-07-29 11:50:00, status: FinishedRunning)
- Arterial Line (category: Access Lines - Invasive, started: 2187-07-29 11:50:00, status: FinishedRunning)
- EKG (category: 4-Procedures, started: 2187-07-29 12:47:00, status: FinishedRunning)
- Chest X-Ray (category: 5-Imaging, started: 2187-07-29 14:55:00, status: FinishedRunning)
- Extubation (category: 1-Intubation/Extubation, started: 2187-07-29 18:15:00, status: FinishedRunning)
- Chest Tube Removed (category: 4-Procedures, started: 2187-07-30 10:00:00, status: FinishedRunning)
- 22 Gauge (category: Access Lines - Peripheral, started: 2187-07-30 11:04:00, status: FinishedRunning)

## 8. Critical Findings (Charted Events)

- **Ventilator Type** (first noted: 2187-07-29 11:00:00)
- **Ventilator Mode (Hamilton)** (first noted: 2187-07-29 11:00:00)
- **Ventilator Tank #2** (first noted: 2187-07-29 11:00:00)
- **Known difficult intubation** (first noted: 2187-07-29 11:00:00)
- **Code Status.** (first noted: 2187-07-29 12:19:00)
- **Temporary Pacemaker Mode** (first noted: 2187-07-29 12:00:00)
- **Temporary Pacemaker Type** (first noted: 2187-07-29 12:00:00)
- **Temporary Pacemaker Wire Condition** (first noted: 2187-07-29 12:00:00)

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2187-07-29 01:05:00 | Admission | Admitted from PHYSICIAN REFERRAL (SURGICAL SAME DAY ADMISSION) |
| 2187-07-29 09:41:11 | ICU Admission | Cardiac Vascular Intensive Care Unit (CVICU) (LOS: 1.2 days) |
| 2187-07-29 09:41:11 | Transfer | → Cardiac Vascular Intensive Care Unit (CVICU) (transfer) |
| 2187-07-30 13:42:51 | Transfer | → Cardiac Surgery (transfer) |
| 2187-08-03 17:02:00 | Discharge | To SKILLED NURSING FACILITY |

## 10. Missing / Ambiguous Data

- No ED registration time — admission may not have gone through ED.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
