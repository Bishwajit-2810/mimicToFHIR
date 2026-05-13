# Encounter Report — HADM 29974575

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 29974575 |
| Subject ID | 10020944 |
| Patient Sex | M |
| Patient Anchor Age (at anchor year) | 72 |
| Anchor Year | 2131 |
| Admission Time | 2131-02-27 15:34:00 |
| Discharge Time | 2131-03-13 17:01:00 |
| Admission Type | EW EMER. |
| Admission Location | EMERGENCY ROOM |
| Discharge Location | SKILLED NURSING FACILITY |
| Insurance | Medicare |
| Language | ENGLISH |
| Marital Status | N/A |
| Race/Ethnicity | UNKNOWN |
| ED Registration | 2131-02-27 13:16:00 |
| ED Departure | 2131-02-27 16:40:00 |
| In-Hospital Mortality | No |
| Date of Death (overall) | 2131-04-28 |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| APR | 720 | SEPTICEMIA & DISSEMINATED INFECTIONS | 4.0 | 4.0 |
| HCFA | 870 | SEPTICEMIA OR SEVERE SEPSIS W MV 96+ HOURS | N/A | N/A |

### Primary Diagnosis (seq_num = 1)

- **ICD-9 03849**: Other septicemia due to gram-negative organisms

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2131-02-27 15:35:01 | N/A | MED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-9 `03849`: Other septicemia due to gram-negative organisms
- (seq 2) ICD-9 `51881`: Acute respiratory failure
- (seq 3) ICD-9 `78552`: Septic shock
- (seq 4) ICD-9 `4820`: Pneumonia due to Klebsiella pneumoniae
- (seq 5) ICD-9 `34982`: Toxic encephalopathy

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-9 | `03849` | Other septicemia due to gram-negative organisms |
| 2 | ICD-9 | `51881` | Acute respiratory failure |
| 3 | ICD-9 | `78552` | Septic shock |
| 4 | ICD-9 | `4820` | Pneumonia due to Klebsiella pneumoniae |
| 5 | ICD-9 | `34982` | Toxic encephalopathy |
| 6 | ICD-9 | `20210` | Mycosis fungoides, unspecified site, extranodal and solid organ sites |
| 7 | ICD-9 | `78039` | Other convulsions |
| 8 | ICD-9 | `5849` | Acute kidney failure, unspecified |
| 9 | ICD-9 | `1540` | Malignant neoplasm of rectosigmoid junction |
| 10 | ICD-9 | `73010` | Chronic osteomyelitis, site unspecified |
| 11 | ICD-9 | `5789` | Hemorrhage of gastrointestinal tract, unspecified |
| 12 | ICD-9 | `5180` | Pulmonary collapse |
| 13 | ICD-9 | `2762` | Acidosis |
| 14 | ICD-9 | `5990` | Urinary tract infection, site not specified |
| 15 | ICD-9 | `496` | Chronic airway obstruction, not elsewhere classified |
| 16 | ICD-9 | `3575` | Alcoholic polyneuropathy |
| 17 | ICD-9 | `5712` | Alcoholic cirrhosis of liver |
| 18 | ICD-9 | `5989` | Urethral stricture, unspecified |
| 19 | ICD-9 | `51889` | Other diseases of lung, not elsewhere classified |
| 20 | ICD-9 | `99592` | Severe sepsis |
| 21 | ICD-9 | `4168` | Other chronic pulmonary heart diseases |
| 22 | ICD-9 | `2767` | Hyperpotassemia |
| 23 | ICD-9 | `2449` | Unspecified acquired hypothyroidism |
| 24 | ICD-9 | `5859` | Chronic kidney disease, unspecified |
| 25 | ICD-9 | `40390` | Hypertensive chronic kidney disease, unspecified, with chronic kidney disease stage I through stage IV, or unspecified |
| 26 | ICD-9 | `53550` | Unspecified gastritis and gastroduodenitis, without mention of hemorrhage |
| 27 | ICD-9 | `78791` | Diarrhea |
| 28 | ICD-9 | `3489` | Unspecified condition of brain |
| 29 | ICD-9 | `7810` | Abnormal involuntary movements |
| 30 | ICD-9 | `V1255` | Personal history of pulmonary embolism |
| 31 | ICD-9 | `V5861` | Long-term (current) use of anticoagulants |
| 32 | ICD-9 | `V1582` | Personal history of tobacco use |
| 33 | ICD-9 | `75261` | Hypospadias |

## 5. ICU Stays

| Stay ID | First Care Unit | Last Care Unit | ICU Admit | ICU Discharge | LOS (days) |
|---|---|---|---|---|---|
| 30757476 | Medical Intensive Care Unit (MICU) | Medical Intensive Care Unit (MICU) | 2131-02-27 16:40:00 | 2131-03-08 18:30:38 | 9.08 |

## 6. Escalation / Severity Indicators

The following critical conditions or interventions were detected:

- **Acute Kidney Injury** (ICD diagnosis)
- **Arterial Line** (ICU procedure event)
- **Endotracheal Intubation** (ICU procedure event)
- **Invasive Mechanical Ventilation** (ICU procedure event)
- **Pneumonia** (ICD diagnosis)
- **Respiratory Failure** (ICD diagnosis)
- **Sepsis** (ICD diagnosis)
- **Shock** (ICD diagnosis)

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2131-02-27 | ICD-9 | `9672` | Continuous invasive mechanical ventilation for 96 consecutive hours or more |
| 2 | 2131-02-27 | ICD-9 | `9604` | Insertion of endotracheal tube |
| 3 | 2131-02-27 | ICD-9 | `3893` | Venous catheterization, not elsewhere classified |
| 4 | 2131-02-27 | ICD-9 | `3323` | Other bronchoscopy |
| 5 | 2131-03-03 | ICD-9 | `3891` | Arterial catheterization |

### ICU Procedure Events (from `icu/procedureevents.csv.gz`)

- Multi Lumen (category: Access Lines - Invasive, started: 2131-02-27 17:30:00, status: FinishedRunning)
- 18 Gauge (category: Access Lines - Peripheral, started: 2131-02-27 17:30:00, status: FinishedRunning)
- Bronchoscopy (category: 4-Procedures, started: 2131-02-27 19:00:00, status: FinishedRunning)
- Sputum Culture (category: 6-Cultures, started: 2131-02-27 20:00:00, status: FinishedRunning)
- Urine Culture (category: 6-Cultures, started: 2131-02-28 00:00:00, status: FinishedRunning)
- Rectal Swab (category: 6-Cultures, started: 2131-02-28 04:42:00, status: FinishedRunning)
- CT scan (category: 5-Imaging, started: 2131-03-01 21:05:00, status: FinishedRunning)
- EEG (category: 4-Procedures, started: 2131-03-02 00:15:00, status: FinishedRunning)
- Chest X-Ray (category: 5-Imaging, started: 2131-03-02 00:20:00, status: FinishedRunning)
- 20 Gauge (category: Access Lines - Peripheral, started: 2131-03-02 01:00:00, status: FinishedRunning)
- Magnetic Resonance Imaging (category: 5-Imaging, started: 2131-03-02 01:45:00, status: FinishedRunning)
- PICC Line (category: Access Lines - Invasive, started: 2131-03-02 17:08:00, status: FinishedRunning)
- Arterial Line (category: Access Lines - Invasive, started: 2131-03-03 07:00:00, status: FinishedRunning)
- Unplanned Extubation (patient-initiated) (category: 1-Intubation/Extubation, started: 2131-03-03 19:54:00, status: FinishedRunning)
- Invasive Ventilation (category: 2-Ventilation, started: 2131-03-03 20:11:00, status: FinishedRunning)
- Intubation (category: 1-Intubation/Extubation, started: 2131-03-03 20:11:00, status: FinishedRunning)

## 8. Critical Findings (Charted Events)

- **Ventilator Type** (first noted: 2131-02-27 17:30:00)
- **Ventilator Tank #1** (first noted: 2131-02-27 17:30:00)
- **Ventilator Mode** (first noted: 2131-02-27 17:30:00)
- **Known difficult intubation** (first noted: 2131-02-27 17:00:00)
- **Code Status** (first noted: 2131-03-07 07:06:00)
- **Seizure Activity** (first noted: 2131-02-27 17:30:00)

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2131-02-27 13:16:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2131-02-27 13:16:00 | Transfer | → Emergency Department (ED) |
| 2131-02-27 15:34:00 | Admission | Admitted from EMERGENCY ROOM (EW EMER.) |
| 2131-02-27 16:40:00 | ED Departure | Left Emergency Dept. |
| 2131-02-27 16:40:00 | ICU Admission | Medical Intensive Care Unit (MICU) (LOS: 9.1 days) |
| 2131-03-08 18:30:38 | Transfer | → Medicine (transfer) |
| 2131-03-13 17:01:00 | Discharge | To SKILLED NURSING FACILITY |

## 10. Missing / Ambiguous Data

- No obvious missing critical fields detected.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
