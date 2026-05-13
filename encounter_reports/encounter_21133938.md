# Encounter Report — HADM 21133938

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 21133938 |
| Subject ID | 10023117 |
| Patient Sex | M |
| Patient Anchor Age (at anchor year) | 53 |
| Anchor Year | 2170 |
| Admission Time | 2175-03-20 23:29:00 |
| Discharge Time | 2175-03-29 16:00:00 |
| Admission Type | OBSERVATION ADMIT |
| Admission Location | TRANSFER FROM HOSPITAL |
| Discharge Location | HOME |
| Insurance | Medicare |
| Language | ENGLISH |
| Marital Status | WIDOWED |
| Race/Ethnicity | WHITE |
| ED Registration | N/A |
| ED Departure | N/A |
| In-Hospital Mortality | No |
| Date of Death (overall) | 2175-07-20 |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| APR | 196 | CARDIAC ARREST & SHOCK | 4.0 | 4.0 |
| HCFA | 291 | HEART FAILURE & SHOCK W MCC | N/A | N/A |

### Primary Diagnosis (seq_num = 1)

- **ICD-10 R570**: Cardiogenic shock

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2175-03-20 23:29:26 | N/A | CMED |
| 2175-03-21 03:21:01 | CMED | MED |
| 2175-03-21 07:37:45 | MED | CMED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-10 `R570`: Cardiogenic shock
- (seq 2) ICD-10 `K7200`: Acute and subacute hepatic failure without coma
- (seq 3) ICD-10 `J9601`: Acute respiratory failure with hypoxia
- (seq 4) ICD-10 `R34`: Anuria and oliguria
- (seq 5) ICD-10 `N179`: Acute kidney failure, unspecified

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-10 | `R570` | Cardiogenic shock |
| 2 | ICD-10 | `K7200` | Acute and subacute hepatic failure without coma |
| 3 | ICD-10 | `J9601` | Acute respiratory failure with hypoxia |
| 4 | ICD-10 | `R34` | Anuria and oliguria |
| 5 | ICD-10 | `N179` | Acute kidney failure, unspecified |
| 6 | ICD-10 | `K2270` | Barrett's esophagus without dysplasia |
| 7 | ICD-10 | `F200` | Paranoid schizophrenia |
| 8 | ICD-10 | `E874` | Mixed disorder of acid-base balance |
| 9 | ICD-10 | `I82622` | Acute embolism and thrombosis of deep veins of left upper extremity |
| 10 | ICD-10 | `D689` | Coagulation defect, unspecified |
| 11 | ICD-10 | `I420` | Dilated cardiomyopathy |
| 12 | ICD-10 | `I272` | Other secondary pulmonary hypertension |
| 13 | ICD-10 | `I340` | Nonrheumatic mitral (valve) insufficiency |
| 14 | ICD-10 | `I071` | Rheumatic tricuspid insufficiency |
| 15 | ICD-10 | `I129` | Hypertensive chronic kidney disease with stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease |
| 16 | ICD-10 | `N189` | Chronic kidney disease, unspecified |
| 17 | ICD-10 | `Z87891` | Personal history of nicotine dependence |
| 18 | ICD-10 | `F329` | Major depressive disorder, single episode, unspecified |
| 19 | ICD-10 | `E785` | Hyperlipidemia, unspecified |
| 20 | ICD-10 | `K219` | Gastro-esophageal reflux disease without esophagitis |
| 21 | ICD-10 | `D649` | Anemia, unspecified |
| 22 | ICD-10 | `Z4502` | Encounter for adjustment and management of automatic implantable cardiac defibrillator |
| 23 | ICD-10 | `R112` | Nausea with vomiting, unspecified |
| 24 | ICD-10 | `M109` | Gout, unspecified |
| 25 | ICD-10 | `R319` | Hematuria, unspecified |
| 26 | ICD-10 | `T8089XA` | Other complications following infusion, transfusion and therapeutic injection, initial encounter |
| 27 | ICD-10 | `E875` | Hyperkalemia |
| 28 | ICD-10 | `R002` | Palpitations |
| 29 | ICD-10 | `Z85528` | Personal history of other malignant neoplasm of kidney |
| 30 | ICD-10 | `Z905` | Acquired absence of kidney |

## 5. ICU Stays

| Stay ID | First Care Unit | Last Care Unit | ICU Admit | ICU Discharge | LOS (days) |
|---|---|---|---|---|---|
| 38554095 | Medical Intensive Care Unit (MICU) | Coronary Care Unit (CCU) | 2175-03-21 03:20:53 | 2175-03-27 17:52:59 | 6.61 |

## 6. Escalation / Severity Indicators

The following critical conditions or interventions were detected:

- **Acute Kidney Injury** (ICD diagnosis)
- **Arterial Line** (ICU procedure event)
- **Invasive Mechanical Ventilation** (ICU procedure event)
- **Liver Failure** (ICD diagnosis)
- **Respiratory Failure** (ICD diagnosis)
- **Shock** (ICD diagnosis)

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2175-03-21 | ICD-10 | `5A1945Z` | Respiratory Ventilation, 24-96 Consecutive Hours |
| 2 | 2175-03-21 | ICD-10 | `0BH18EZ` | Insertion of Endotracheal Airway into Trachea, Via Natural or Artificial Opening Endoscopic |
| 3 | 2175-03-21 | ICD-10 | `02HP32Z` | Insertion of Monitoring Device into Pulmonary Trunk, Percutaneous Approach |
| 4 | 2175-03-21 | ICD-10 | `4A133B3` | Monitoring of Arterial Pressure, Pulmonary, Percutaneous Approach |
| 5 | 2175-03-21 | ICD-10 | `4A1239Z` | Monitoring of Cardiac Output, Percutaneous Approach |

### ICU Procedure Events (from `icu/procedureevents.csv.gz`)

- 20 Gauge (category: Access Lines - Peripheral, started: 2175-03-21 03:34:00, status: FinishedRunning)
- Invasive Ventilation (category: 2-Ventilation, started: 2175-03-21 03:37:00, status: FinishedRunning)
- PA Catheter (category: Access Lines - Invasive, started: 2175-03-21 05:42:00, status: FinishedRunning)
- Cordis/Introducer (category: Access Lines - Invasive, started: 2175-03-22 00:00:00, status: FinishedRunning)
- Arterial Line (category: Access Lines - Invasive, started: 2175-03-22 00:00:00, status: FinishedRunning)
- Chest X-Ray (category: 5-Imaging, started: 2175-03-22 08:00:00, status: FinishedRunning)
- Transthoracic Echo (category: 5-Imaging, started: 2175-03-22 09:16:00, status: FinishedRunning)
- Pan Culture (category: 6-Cultures, started: 2175-03-22 09:16:00, status: FinishedRunning)
- Extubation (category: 1-Intubation/Extubation, started: 2175-03-22 12:45:00, status: FinishedRunning)
- 22 Gauge (category: Access Lines - Peripheral, started: 2175-03-25 18:40:00, status: FinishedRunning)

## 8. Critical Findings (Charted Events)

- **Ventilator Mode** (first noted: 2175-03-21 04:00:00)
- **Ventilator Type** (first noted: 2175-03-21 04:00:00)
- **Ventilator Tank #1** (first noted: 2175-03-21 19:00:00)
- **Known difficult intubation** (first noted: 2175-03-21 04:00:00)
- **Code Status** (first noted: 2175-03-25 17:52:00)
- **Dialysis patient** (first noted: 2175-03-23 07:30:00)

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2175-03-20 23:29:00 | Admission | Admitted from TRANSFER FROM HOSPITAL (OBSERVATION ADMIT) |
| 2175-03-21 03:20:53 | ICU Admission | Medical Intensive Care Unit (MICU) (LOS: 6.6 days) |
| 2175-03-21 03:20:53 | Transfer | → Medical Intensive Care Unit (MICU) (transfer) |
| 2175-03-21 20:47:36 | Transfer | → Coronary Care Unit (CCU) (transfer) |
| 2175-03-27 17:52:59 | Transfer | → Medicine/Cardiology (transfer) |
| 2175-03-29 16:00:00 | Discharge | To HOME |

## 10. Missing / Ambiguous Data

- No ED registration time — admission may not have gone through ED.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
