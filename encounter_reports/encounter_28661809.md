# Encounter Report — HADM 28661809

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 28661809 |
| Subject ID | 10005817 |
| Patient Sex | M |
| Patient Anchor Age (at anchor year) | 66 |
| Anchor Year | 2132 |
| Admission Time | 2135-01-03 21:54:00 |
| Discharge Time | 2135-01-19 18:36:00 |
| Admission Type | OBSERVATION ADMIT |
| Admission Location | TRANSFER FROM HOSPITAL |
| Discharge Location | DIED |
| Insurance | Medicare |
| Language | ENGLISH |
| Marital Status | MARRIED |
| Race/Ethnicity | WHITE |
| ED Registration | N/A |
| ED Departure | N/A |
| In-Hospital Mortality | YES — Death time: 2135-01-19 18:36:00 |
| Date of Death (overall) | 2135-01-19 |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| APR | 130 | RESPIRATORY SYSTEM DIAGNOSIS W VENTILATOR SUPPORT 96+ HOURS | 3.0 | 3.0 |
| HCFA | 207 | RESPIRATORY SYSTEM DIAGNOSIS W VENTILATOR SUPPORT >96 HOURS | N/A | N/A |

### Primary Diagnosis (seq_num = 1)

- **ICD-10 J9621**: Acute and chronic respiratory failure with hypoxia

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2135-01-03 21:55:32 | N/A | OMED |
| 2135-01-04 19:27:00 | OMED | MED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-10 `J9621`: Acute and chronic respiratory failure with hypoxia
- (seq 2) ICD-10 `J910`: Malignant pleural effusion
- (seq 3) ICD-10 `J189`: Pneumonia, unspecified organism
- (seq 4) ICD-10 `N170`: Acute kidney failure with tubular necrosis
- (seq 5) ICD-10 `E883`: Tumor lysis syndrome

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-10 | `J9621` | Acute and chronic respiratory failure with hypoxia |
| 2 | ICD-10 | `J910` | Malignant pleural effusion |
| 3 | ICD-10 | `J189` | Pneumonia, unspecified organism |
| 4 | ICD-10 | `N170` | Acute kidney failure with tubular necrosis |
| 5 | ICD-10 | `E883` | Tumor lysis syndrome |
| 6 | ICD-10 | `I82412` | Acute embolism and thrombosis of left femoral vein |
| 7 | ICD-10 | `C7B8` | Other secondary neuroendocrine tumors |
| 8 | ICD-10 | `I5022` | Chronic systolic (congestive) heart failure |
| 9 | ICD-10 | `I871` | Compression of vein |
| 10 | ICD-10 | `C7A8` | Other malignant neuroendocrine tumors |
| 11 | ICD-10 | `J449` | Chronic obstructive pulmonary disease, unspecified |
| 12 | ICD-10 | `I2510` | Atherosclerotic heart disease of native coronary artery without angina pectoris |
| 13 | ICD-10 | `F17210` | Nicotine dependence, cigarettes, uncomplicated |
| 14 | ICD-10 | `Z951` | Presence of aortocoronary bypass graft |
| 15 | ICD-10 | `Z955` | Presence of coronary angioplasty implant and graft |
| 16 | ICD-10 | `E119` | Type 2 diabetes mellitus without complications |
| 17 | ICD-10 | `Z85048` | Personal history of other malignant neoplasm of rectum, rectosigmoid junction, and anus |
| 18 | ICD-10 | `F4310` | Post-traumatic stress disorder, unspecified |
| 19 | ICD-10 | `I4891` | Unspecified atrial fibrillation |
| 20 | ICD-10 | `Z515` | Encounter for palliative care |
| 21 | ICD-10 | `I129` | Hypertensive chronic kidney disease with stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease |
| 22 | ICD-10 | `N189` | Chronic kidney disease, unspecified |
| 23 | ICD-10 | `R410` | Disorientation, unspecified |
| 24 | ICD-10 | `Z9981` | Dependence on supplemental oxygen |
| 25 | ICD-10 | `Z7902` | Long term (current) use of antithrombotics/antiplatelets |

## 5. ICU Stays

| Stay ID | First Care Unit | Last Care Unit | ICU Admit | ICU Discharge | LOS (days) |
|---|---|---|---|---|---|
| 31316840 | Medical Intensive Care Unit (MICU) | Medical/Surgical Intensive Care Unit (MICU/SICU) | 2135-01-03 21:55:32 | 2135-01-19 21:16:23 | 15.97 |

## 6. Escalation / Severity Indicators

The following critical conditions or interventions were detected:

- **Acute Kidney Injury** (ICD diagnosis)
- **Arterial Line** (ICU procedure event)
- **Endotracheal Intubation** (ICU procedure event)
- **Invasive Mechanical Ventilation** (ICU procedure event)
- **Pneumonia** (ICD diagnosis)

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2135-01-04 | ICD-10 | `0W9930Z` | Drainage of Right Pleural Cavity with Drainage Device, Percutaneous Approach |
| 2 | 2135-01-06 | ICD-10 | `5A1955Z` | Respiratory Ventilation, Greater than 96 Consecutive Hours |
| 3 | 2135-01-06 | ICD-10 | `0BH17EZ` | Insertion of Endotracheal Airway into Trachea, Via Natural or Artificial Opening |
| 4 | 2135-01-07 | ICD-10 | `DW021ZZ` | Beam Radiation of Chest using Photons 1 - 10 MeV |
| 5 | 2135-01-08 | ICD-10 | `02HV33Z` | Insertion of Infusion Device into Superior Vena Cava, Percutaneous Approach |
| 6 | 2135-01-09 | ICD-10 | `0B9B8ZX` | Drainage of Left Lower Lobe Bronchus, Via Natural or Artificial Opening Endoscopic, Diagnostic |

### ICU Procedure Events (from `icu/procedureevents.csv.gz`)

- 22 Gauge (category: Access Lines - Peripheral, started: 2135-01-03 23:04:00, status: FinishedRunning)
- Foley Catheter (category: GI/GU, started: 2135-01-04 12:00:00, status: FinishedRunning)
- 20 Gauge (category: Access Lines - Peripheral, started: 2135-01-04 15:15:00, status: FinishedRunning)
- Intubation (category: 1-Intubation/Extubation, started: 2135-01-06 08:33:00, status: FinishedRunning)
- Invasive Ventilation (category: 2-Ventilation, started: 2135-01-06 08:34:00, status: FinishedRunning)
- Transthoracic Echo (category: 5-Imaging, started: 2135-01-06 15:33:00, status: FinishedRunning)
- PICC Line (category: Access Lines - Invasive, started: 2135-01-08 11:39:00, status: FinishedRunning)
- CT scan (category: 5-Imaging, started: 2135-01-08 20:15:00, status: FinishedRunning)
- Ultrasound (category: 5-Imaging, started: 2135-01-09 14:40:00, status: FinishedRunning)
- Bronchoscopy (category: 4-Procedures, started: 2135-01-09 17:11:00, status: FinishedRunning)
- EKG (category: 4-Procedures, started: 2135-01-10 16:07:00, status: FinishedRunning)
- Multi Lumen (category: Access Lines - Invasive, started: 2135-01-13 18:00:00, status: FinishedRunning)
- Arterial Line (category: Access Lines - Invasive, started: 2135-01-13 18:30:00, status: FinishedRunning)
- Radiation Therapy (category: 4-Procedures, started: 2135-01-15 15:00:00, status: FinishedRunning)
- Urine Culture (category: 6-Cultures, started: 2135-01-15 18:00:00, status: FinishedRunning)
- Thoracentesis (category: 4-Procedures, started: 2135-01-16 14:36:00, status: FinishedRunning)
- Chest X-Ray (category: 5-Imaging, started: 2135-01-17 05:56:00, status: FinishedRunning)
- Cardioversion/Defibrillation (category: 3-Significant Events, started: 2135-01-17 11:50:00, status: FinishedRunning)
- Extubation (category: 1-Intubation/Extubation, started: 2135-01-19 14:00:00, status: FinishedRunning)

## 8. Critical Findings (Charted Events)

- **Ventilator Type** (first noted: 2135-01-06 08:00:00)
- **Ventilator Mode** (first noted: 2135-01-06 22:00:00)
- **Ventilator Tank #1** (first noted: 2135-01-06 20:00:00)
- **Known difficult intubation** (first noted: 2135-01-06 08:00:00)
- **Code Status** (first noted: 2135-01-03 22:02:00)
- **Dialysis patient** (first noted: 2135-01-03 23:15:00)

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2135-01-03 21:54:00 | Admission | Admitted from TRANSFER FROM HOSPITAL (OBSERVATION ADMIT) |
| 2135-01-03 21:55:32 | ICU Admission | Medical Intensive Care Unit (MICU) (LOS: 16.0 days) |
| 2135-01-06 22:14:10 | Transfer | → Medical/Surgical Intensive Care Unit (MICU/SICU) (transfer) |
| 2135-01-19 18:36:00 | **IN-HOSPITAL DEATH** | |
| 2135-01-19 18:36:00 | Discharge | To DIED |

## 10. Missing / Ambiguous Data

- No ED registration time — admission may not have gone through ED.

## 11. Manual Review Recommendation

**This encounter is flagged for manual review:**

- Patient expired in-hospital but cause of death not clearly coded.
