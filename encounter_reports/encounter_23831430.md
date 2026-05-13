# Encounter Report — HADM 23831430

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 23831430 |
| Subject ID | 10020740 |
| Patient Sex | M |
| Patient Anchor Age (at anchor year) | 56 |
| Anchor Year | 2150 |
| Admission Time | 2150-03-11 15:34:00 |
| Discharge Time | 2150-04-25 13:50:00 |
| Admission Type | URGENT |
| Admission Location | TRANSFER FROM HOSPITAL |
| Discharge Location | SKILLED NURSING FACILITY |
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
| APR | 720 | SEPTICEMIA & DISSEMINATED INFECTIONS | 4.0 | 3.0 |
| HCFA | 871 | SEPTICEMIA OR SEVERE SEPSIS W/O MV 96+ HOURS W MCC | N/A | N/A |

### Primary Diagnosis (seq_num = 1)

- **ICD-9 03842**: Septicemia due to escherichia coli [E. coli]

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2150-03-11 15:34:56 | N/A | MED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-9 `03842`: Septicemia due to escherichia coli [E. coli]
- (seq 2) ICD-9 `5770`: Acute pancreatitis
- (seq 3) ICD-9 `51881`: Acute respiratory failure
- (seq 4) ICD-9 `5070`: Pneumonitis due to inhalation of food or vomitus
- (seq 5) ICD-9 `5849`: Acute kidney failure, unspecified

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-9 | `03842` | Septicemia due to escherichia coli [E. coli] |
| 2 | ICD-9 | `5770` | Acute pancreatitis |
| 3 | ICD-9 | `51881` | Acute respiratory failure |
| 4 | ICD-9 | `5070` | Pneumonitis due to inhalation of food or vomitus |
| 5 | ICD-9 | `5849` | Acute kidney failure, unspecified |
| 6 | ICD-9 | `2639` | Unspecified protein-calorie malnutrition |
| 7 | ICD-9 | `2760` | Hyperosmolality and/or hypernatremia |
| 8 | ICD-9 | `5772` | Cyst and pseudocyst of pancreas |
| 9 | ICD-9 | `29520` | Catatonic type schizophrenia, unspecified |
| 10 | ICD-9 | `5723` | Portal hypertension |
| 11 | ICD-9 | `4592` | Compression of vein |
| 12 | ICD-9 | `99591` | Sepsis |
| 13 | ICD-9 | `25000` | Diabetes mellitus without mention of complication, type II or unspecified type, not stated as uncontrolled |
| 14 | ICD-9 | `49390` | Asthma, unspecified type, unspecified |
| 15 | ICD-9 | `32723` | Obstructive sleep apnea (adult)(pediatric) |
| 16 | ICD-9 | `2724` | Other and unspecified hyperlipidemia |
| 17 | ICD-9 | `9331` | Foreign body in larynx |
| 18 | ICD-9 | `E912` | Inhalation and ingestion of other object causing obstruction of respiratory tract or suffocation |
| 19 | ICD-9 | `E8497` | Accidents occurring in residential institution |
| 20 | ICD-9 | `2875` | Thrombocytopenia, unspecified |
| 21 | ICD-9 | `2859` | Anemia, unspecified |
| 22 | ICD-9 | `78009` | Other alteration of consciousness |
| 23 | ICD-9 | `78820` | Retention of urine, unspecified |
| 24 | ICD-9 | `78720` | Dysphagia, unspecified |

## 5. ICU Stays

| Stay ID | First Care Unit | Last Care Unit | ICU Admit | ICU Discharge | LOS (days) |
|---|---|---|---|---|---|
| 35026312 | Medical/Surgical Intensive Care Unit (MICU/SICU) | Medical/Surgical Intensive Care Unit (MICU/SICU) | 2150-03-11 15:34:56 | 2150-03-19 02:17:47 | 7.45 |
| 35044342 | Medical/Surgical Intensive Care Unit (MICU/SICU) | Medical/Surgical Intensive Care Unit (MICU/SICU) | 2150-03-19 04:41:33 | 2150-03-23 20:49:33 | 4.67 |
| 35889503 | Medical Intensive Care Unit (MICU) | Medical Intensive Care Unit (MICU) | 2150-03-25 18:22:56 | 2150-03-28 22:20:47 | 3.17 |
| 31077365 | Medical Intensive Care Unit (MICU) | Medical Intensive Care Unit (MICU) | 2150-03-30 07:57:10 | 2150-04-04 10:58:43 | 5.13 |

## 6. Escalation / Severity Indicators

The following critical conditions or interventions were detected:

- **Acute Kidney Injury** (ICD diagnosis)
- **Endotracheal Intubation** (ICU procedure event)
- **Invasive Mechanical Ventilation** (ICU procedure event)
- **Liver Failure** (ICD diagnosis)
- **Respiratory Failure** (ICD diagnosis)
- **Sepsis** (ICD diagnosis)

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2150-03-11 | ICD-9 | `9671` | Continuous invasive mechanical ventilation for less than 96 consecutive hours |
| 2 | 2150-03-11 | ICD-9 | `9915` | Parenteral infusion of concentrated nutritional substances |
| 3 | 2150-03-12 | ICD-9 | `966` | Enteral infusion of concentrated nutritional substances |
| 4 | 2150-03-19 | ICD-9 | `9604` | Insertion of endotracheal tube |
| 5 | 2150-03-19 | ICD-9 | `9671` | Continuous invasive mechanical ventilation for less than 96 consecutive hours |
| 6 | 2150-03-27 | ICD-9 | `9427` | Other electroshock therapy |
| 7 | 2150-04-01 | ICD-9 | `9427` | Other electroshock therapy |
| 8 | 2150-04-03 | ICD-9 | `9427` | Other electroshock therapy |
| 9 | 2150-04-06 | ICD-9 | `9427` | Other electroshock therapy |
| 10 | 2150-04-14 | ICD-9 | `9427` | Other electroshock therapy |
| 11 | 2150-04-17 | ICD-9 | `9427` | Other electroshock therapy |
| 12 | 2150-04-20 | ICD-9 | `9427` | Other electroshock therapy |
| 13 | 2150-04-24 | ICD-9 | `9427` | Other electroshock therapy |
| 14 | 2150-03-26 | ICD-9 | `3897` | Central venous catheter placement with guidance |
| 15 | 2150-03-30 | ICD-9 | `9604` | Insertion of endotracheal tube |
| 16 | 2150-03-30 | ICD-9 | `9671` | Continuous invasive mechanical ventilation for less than 96 consecutive hours |

### ICU Procedure Events (from `icu/procedureevents.csv.gz`)

- Invasive Ventilation (category: 2-Ventilation, started: 2150-03-11 15:45:00, status: FinishedRunning)
- PICC Line (category: Access Lines - Invasive, started: 2150-03-11 16:00:00, status: FinishedRunning)
- Chest X-Ray (category: 5-Imaging, started: 2150-03-11 16:15:00, status: FinishedRunning)
- Blood Cultured (category: 6-Cultures, started: 2150-03-11 16:53:00, status: FinishedRunning)
- Nasal Swab (category: 6-Cultures, started: 2150-03-11 16:53:00, status: FinishedRunning)
- 20 Gauge (category: Access Lines - Peripheral, started: 2150-03-12 22:34:00, status: FinishedRunning)
- CT scan (category: 5-Imaging, started: 2150-03-15 21:30:00, status: FinishedRunning)
- Ultrasound (category: 5-Imaging, started: 2150-03-16 11:14:00, status: FinishedRunning)
- Extubation (category: 1-Intubation/Extubation, started: 2150-03-19 11:05:00, status: FinishedRunning)
- Midline (category: Access Lines - Invasive, started: 2150-03-25 18:49:00, status: FinishedRunning)
- Intubation (category: 1-Intubation/Extubation, started: 2150-03-27 07:44:00, status: FinishedRunning)
- Family updated by RN (category: 7-Communication, started: 2150-03-28 15:13:00, status: FinishedRunning)
- Stool Culture (category: 6-Cultures, started: 2150-04-03 23:00:00, status: FinishedRunning)

## 8. Critical Findings (Charted Events)

- **Ventilator Type** (first noted: 2150-03-11 16:00:00)
- **Ventilator Tank #1** (first noted: 2150-03-11 20:00:00)
- **Ventilator Tank #2** (first noted: 2150-03-11 20:00:00)
- **Known difficult intubation** (first noted: 2150-03-11 20:00:00)
- **Code Status** (first noted: 2150-03-19 05:30:00)
- **Seizure Activity** (first noted: 2150-04-03 07:40:00)

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2150-03-11 15:34:00 | Admission | Admitted from TRANSFER FROM HOSPITAL (URGENT) |
| 2150-03-11 15:34:56 | ICU Admission | Medical/Surgical Intensive Care Unit (MICU/SICU) (LOS: 7.4 days) |
| 2150-03-19 02:17:47 | Transfer | → Medicine (transfer) |
| 2150-03-19 04:41:33 | ICU Admission | Medical/Surgical Intensive Care Unit (MICU/SICU) (LOS: 4.7 days) |
| 2150-03-19 04:41:33 | Transfer | → Medical/Surgical Intensive Care Unit (MICU/SICU) (transfer) |
| 2150-03-23 20:49:33 | Transfer | → Medicine (transfer) |
| 2150-03-25 18:22:56 | ICU Admission | Medical Intensive Care Unit (MICU) (LOS: 3.2 days) |
| 2150-03-25 18:22:56 | Transfer | → Medical Intensive Care Unit (MICU) (transfer) |
| 2150-03-28 22:20:47 | Transfer | → Medicine (transfer) |
| 2150-03-30 07:57:10 | ICU Admission | Medical Intensive Care Unit (MICU) (LOS: 5.1 days) |
| 2150-03-30 07:57:10 | Transfer | → Medical Intensive Care Unit (MICU) (transfer) |
| 2150-04-04 10:58:43 | Transfer | → Neurology (transfer) |
| 2150-04-08 17:48:06 | Transfer | → Medicine (transfer) |
| 2150-04-25 13:50:00 | Discharge | To SKILLED NURSING FACILITY |

## 10. Missing / Ambiguous Data

- No ED registration time — admission may not have gone through ED.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
