# Encounter Report — HADM 20626031

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 20626031 |
| Subject ID | 10005817 |
| Patient Sex | M |
| Patient Anchor Age (at anchor year) | 66 |
| Anchor Year | 2132 |
| Admission Time | 2132-12-12 01:43:00 |
| Discharge Time | 2132-12-20 15:04:00 |
| Admission Type | URGENT |
| Admission Location | TRANSFER FROM HOSPITAL |
| Discharge Location | HOME HEALTH CARE |
| Insurance | Medicare |
| Language | ENGLISH |
| Marital Status | MARRIED |
| Race/Ethnicity | WHITE |
| ED Registration | N/A |
| ED Departure | N/A |
| In-Hospital Mortality | No |
| Date of Death (overall) | 2135-01-19 |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| APR | 166 | CORONARY BYPASS W/O AMI OR COMPLEX PDX | 2.0 | 2.0 |
| HCFA | 236 | CORONARY BYPASS W/O CARDIAC CATH W/O MCC | N/A | N/A |

### Primary Diagnosis (seq_num = 1)

- **ICD-9 41071**: Subendocardial infarction, initial episode of care

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2132-12-12 01:44:24 | N/A | SURG |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-9 `41071`: Subendocardial infarction, initial episode of care
- (seq 2) ICD-9 `4280`: Congestive heart failure, unspecified
- (seq 3) ICD-9 `42731`: Atrial fibrillation
- (seq 4) ICD-9 `42732`: Atrial flutter
- (seq 5) ICD-9 `5990`: Urinary tract infection, site not specified

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-9 | `41071` | Subendocardial infarction, initial episode of care |
| 2 | ICD-9 | `4280` | Congestive heart failure, unspecified |
| 3 | ICD-9 | `42731` | Atrial fibrillation |
| 4 | ICD-9 | `42732` | Atrial flutter |
| 5 | ICD-9 | `5990` | Urinary tract infection, site not specified |
| 6 | ICD-9 | `25000` | Diabetes mellitus without mention of complication, type II or unspecified type, not stated as uncontrolled |
| 7 | ICD-9 | `04110` | Staphylococcus infection in conditions classified elsewhere and of unspecified site, staphylococcus, unspecified |
| 8 | ICD-9 | `41401` | Coronary atherosclerosis of native coronary artery |
| 9 | ICD-9 | `V707` | Examination of participant in clinical trial |
| 10 | ICD-9 | `V5866` | Long-term (current) use of aspirin |
| 11 | ICD-9 | `V4582` | Percutaneous transluminal coronary angioplasty status |
| 12 | ICD-9 | `496` | Chronic airway obstruction, not elsewhere classified |
| 13 | ICD-9 | `V5863` | Long-term (current) use of antiplatelet/antithrombotic |
| 14 | ICD-9 | `4019` | Unspecified essential hypertension |
| 15 | ICD-9 | `V1006` | Personal history of malignant neoplasm of rectum, rectosigmoid junction, and anus |
| 16 | ICD-9 | `30981` | Posttraumatic stress disorder |
| 17 | ICD-9 | `V153` | Personal history of irradiation, presenting hazards to health |
| 18 | ICD-9 | `V8741` | Personal history of antineoplastic chemotherapy |
| 19 | ICD-9 | `7847` | Epistaxis |
| 20 | ICD-9 | `3051` | Tobacco use disorder |
| 21 | ICD-9 | `27800` | Obesity, unspecified |
| 22 | ICD-9 | `V8531` | Body Mass Index 31.0-31.9, adult |
| 23 | ICD-9 | `4400` | Atherosclerosis of aorta |
| 24 | ICD-9 | `4240` | Mitral valve disorders |
| 25 | ICD-9 | `71690` | Arthropathy, unspecified, site unspecified |
| 26 | ICD-9 | `2859` | Anemia, unspecified |

## 5. ICU Stays

| Stay ID | First Care Unit | Last Care Unit | ICU Admit | ICU Discharge | LOS (days) |
|---|---|---|---|---|---|
| 32604416 | Cardiac Vascular Intensive Care Unit (CVICU) | Cardiac Vascular Intensive Care Unit (CVICU) | 2132-12-15 09:29:01 | 2132-12-17 18:06:07 | 2.36 |

## 6. Escalation / Severity Indicators

The following critical conditions or interventions were detected:

- **Arterial Line** (ICU procedure event)
- **Invasive Mechanical Ventilation** (ICU procedure event)

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2132-12-15 | ICD-9 | `3612` | (Aorto)coronary bypass of two coronary arteries |
| 2 | 2132-12-15 | ICD-9 | `3615` | Single internal mammary-coronary artery bypass |
| 3 | 2132-12-15 | ICD-9 | `3961` | Extracorporeal circulation auxiliary to open heart surgery |

### ICU Procedure Events (from `icu/procedureevents.csv.gz`)

- Invasive Ventilation (category: 2-Ventilation, started: 2132-12-15 14:10:00, status: FinishedRunning)
- OR Received (category: 3-Significant Events, started: 2132-12-15 14:10:00, status: FinishedRunning)
- Cordis/Introducer (category: Access Lines - Invasive, started: 2132-12-15 14:13:00, status: FinishedRunning)
- PA Catheter (category: Access Lines - Invasive, started: 2132-12-15 14:13:00, status: FinishedRunning)
- Arterial Line (category: Access Lines - Invasive, started: 2132-12-15 14:13:00, status: FinishedRunning)
- 22 Gauge (category: Access Lines - Peripheral, started: 2132-12-15 14:20:00, status: FinishedRunning)
- 16 Gauge (category: Access Lines - Peripheral, started: 2132-12-15 14:20:00, status: FinishedRunning)
- Chest X-Ray (category: 5-Imaging, started: 2132-12-15 14:30:00, status: FinishedRunning)
- Nasal Swab (category: 6-Cultures, started: 2132-12-15 14:40:00, status: FinishedRunning)
- EKG (category: 4-Procedures, started: 2132-12-15 14:41:00, status: FinishedRunning)
- Extubation (category: 1-Intubation/Extubation, started: 2132-12-15 19:00:00, status: FinishedRunning)
- Chest Tube Removed (category: 4-Procedures, started: 2132-12-17 09:00:00, status: FinishedRunning)
- Multi Lumen (category: Access Lines - Invasive, started: 2132-12-17 17:12:00, status: FinishedRunning)

## 8. Critical Findings (Charted Events)

- **Ventilator Type** (first noted: 2132-12-15 14:00:00)
- **Ventilator Mode** (first noted: 2132-12-15 14:00:00)
- **Known difficult intubation** (first noted: 2132-12-15 14:00:00)
- **Temporary Pacemaker Mode** (first noted: 2132-12-15 14:30:00)
- **Temporary Pacemaker Rate** (first noted: 2132-12-15 14:30:00)
- **Temporary Pacemaker Type** (first noted: 2132-12-15 14:30:00)

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2132-12-12 01:43:00 | Admission | Admitted from TRANSFER FROM HOSPITAL (URGENT) |
| 2132-12-15 09:29:01 | ICU Admission | Cardiac Vascular Intensive Care Unit (CVICU) (LOS: 2.4 days) |
| 2132-12-15 09:29:01 | Transfer | → Cardiac Vascular Intensive Care Unit (CVICU) (transfer) |
| 2132-12-17 18:06:07 | Transfer | → Cardiac Surgery (transfer) |
| 2132-12-20 15:04:00 | Discharge | To HOME HEALTH CARE |

## 10. Missing / Ambiguous Data

- No ED registration time — admission may not have gone through ED.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
