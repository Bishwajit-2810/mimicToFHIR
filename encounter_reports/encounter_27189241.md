# Encounter Report — HADM 27189241

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 27189241 |
| Subject ID | 10038999 |
| Patient Sex | M |
| Patient Anchor Age (at anchor year) | 45 |
| Anchor Year | 2131 |
| Admission Time | 2131-05-22 21:49:00 |
| Discharge Time | 2131-06-04 13:43:00 |
| Admission Type | OBSERVATION ADMIT |
| Admission Location | EMERGENCY ROOM |
| Discharge Location | HOME |
| Insurance | Medicare |
| Language | ENGLISH |
| Marital Status | SINGLE |
| Race/Ethnicity | WHITE |
| ED Registration | 2131-05-22 20:33:00 |
| ED Departure | 2131-05-22 21:28:00 |
| In-Hospital Mortality | No |
| Date of Death (overall) | N/A |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| APR | 130 | RESPIRATORY SYSTEM DIAGNOSIS W VENTILATOR SUPPORT 96+ HOURS | 4.0 | 4.0 |
| HCFA | 207 | RESPIRATORY SYSTEM DIAGNOSIS W VENTILATOR SUPPORT >96 HOURS | N/A | N/A |

### Primary Diagnosis (seq_num = 1)

- **ICD-10 J189**: Pneumonia, unspecified organism

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2131-05-22 21:50:33 | N/A | CMED |
| 2131-05-31 17:55:18 | CMED | MED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-10 `J189`: Pneumonia, unspecified organism
- (seq 2) ICD-10 `R570`: Cardiogenic shock
- (seq 3) ICD-10 `I314`: Cardiac tamponade
- (seq 4) ICD-10 `J918`: Pleural effusion in other conditions classified elsewhere
- (seq 5) ICD-10 `D688`: Other specified coagulation defects

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-10 | `J189` | Pneumonia, unspecified organism |
| 2 | ICD-10 | `R570` | Cardiogenic shock |
| 3 | ICD-10 | `I314` | Cardiac tamponade |
| 4 | ICD-10 | `J918` | Pleural effusion in other conditions classified elsewhere |
| 5 | ICD-10 | `D688` | Other specified coagulation defects |
| 6 | ICD-10 | `E46` | Unspecified protein-calorie malnutrition |
| 7 | ICD-10 | `J9691` | Respiratory failure, unspecified with hypoxia |
| 8 | ICD-10 | `I313` | Pericardial effusion (noninflammatory) |
| 9 | ICD-10 | `J9811` | Atelectasis |
| 10 | ICD-10 | `I319` | Disease of pericardium, unspecified |
| 11 | ICD-10 | `G40909` | Epilepsy, unspecified, not intractable, without status epilepticus |
| 12 | ICD-10 | `H540` | Blindness, both eyes |
| 13 | ICD-10 | `R21` | Rash and other nonspecific skin eruption |
| 14 | ICD-10 | `I509` | Heart failure, unspecified |
| 15 | ICD-10 | `D649` | Anemia, unspecified |
| 16 | ICD-10 | `E875` | Hyperkalemia |
| 17 | ICD-10 | `R001` | Bradycardia, unspecified |

## 5. ICU Stays

| Stay ID | First Care Unit | Last Care Unit | ICU Admit | ICU Discharge | LOS (days) |
|---|---|---|---|---|---|
| 39711498 | Coronary Care Unit (CCU) | Coronary Care Unit (CCU) | 2131-05-22 21:50:33 | 2131-05-31 17:55:04 | 8.84 |

## 6. Escalation / Severity Indicators

The following critical conditions or interventions were detected:

- **Arterial Line** (ICU procedure event)
- **Invasive Mechanical Ventilation** (ICU procedure event)
- **Pneumonia** (ICD diagnosis)
- **Respiratory Failure** (ICD diagnosis)
- **Shock** (ICD diagnosis)

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2131-05-29 | ICD-10 | `0W9B3ZZ` | Drainage of Left Pleural Cavity, Percutaneous Approach |
| 2 | 2131-05-22 | ICD-10 | `5A1955Z` | Respiratory Ventilation, Greater than 96 Consecutive Hours |
| 3 | 2131-05-22 | ICD-10 | `0W9D30Z` | Drainage of Pericardial Cavity with Drainage Device, Percutaneous Approach |
| 4 | 2131-05-22 | ICD-10 | `0BH17EZ` | Insertion of Endotracheal Airway into Trachea, Via Natural or Artificial Opening |
| 5 | 2131-05-26 | ICD-10 | `3E0H76Z` | Introduction of Nutritional Substance into Lower GI, Via Natural or Artificial Opening |
| 6 | 2131-05-29 | ICD-10 | `0W9B3ZX` | Drainage of Left Pleural Cavity, Percutaneous Approach, Diagnostic |
| 7 | 2131-05-26 | ICD-10 | `02HV33Z` | Insertion of Infusion Device into Superior Vena Cava, Percutaneous Approach |
| 8 | 2131-05-26 | ICD-10 | `0B988ZX` | Drainage of Left Upper Lobe Bronchus, Via Natural or Artificial Opening Endoscopic, Diagnostic |
| 9 | 2131-05-26 | ICD-10 | `0BB88ZX` | Excision of Left Upper Lobe Bronchus, Via Natural or Artificial Opening Endoscopic, Diagnostic |

### ICU Procedure Events (from `icu/procedureevents.csv.gz`)

- Foley Catheter (category: GI/GU, started: 2131-05-22 21:55:00, status: FinishedRunning)
- Invasive Ventilation (category: 2-Ventilation, started: 2131-05-22 22:39:00, status: FinishedRunning)
- 20 Gauge (category: Access Lines - Peripheral, started: 2131-05-22 22:40:00, status: FinishedRunning)
- EKG (category: 4-Procedures, started: 2131-05-22 22:40:00, status: FinishedRunning)
- 18 Gauge (category: Access Lines - Peripheral, started: 2131-05-22 22:41:00, status: FinishedRunning)
- Arterial Line (category: Access Lines - Invasive, started: 2131-05-24 17:29:00, status: FinishedRunning)
- Chest X-Ray (category: 5-Imaging, started: 2131-05-26 07:32:00, status: FinishedRunning)
- Bronchoscopy (category: 4-Procedures, started: 2131-05-26 08:30:00, status: FinishedRunning)
- Family updated by MD (category: 7-Communication, started: 2131-05-26 15:31:00, status: FinishedRunning)
- Family updated by RN (category: 7-Communication, started: 2131-05-26 15:31:00, status: FinishedRunning)
- Blood Cultured (category: 6-Cultures, started: 2131-05-26 15:31:00, status: FinishedRunning)
- Urine Culture (category: 6-Cultures, started: 2131-05-26 15:31:00, status: FinishedRunning)
- PICC Line (category: Access Lines - Invasive, started: 2131-05-26 18:20:00, status: FinishedRunning)
- Thoracentesis (category: 4-Procedures, started: 2131-05-29 11:16:00, status: FinishedRunning)
- Extubation (category: 1-Intubation/Extubation, started: 2131-05-29 14:59:00, status: FinishedRunning)

## 8. Critical Findings (Charted Events)

- **Ventilator Type** (first noted: 2131-05-22 22:00:00)
- **Ventilator Mode** (first noted: 2131-05-22 22:28:00)
- **Ventilator Tank #2** (first noted: 2131-05-23 00:00:00)
- **Known difficult intubation** (first noted: 2131-05-22 22:00:00)
- **Code Status** (first noted: 2131-05-22 22:37:00)

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2131-05-22 20:33:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2131-05-22 20:33:00 | Transfer | → Emergency Department (ED) |
| 2131-05-22 21:28:00 | ED Departure | Left Emergency Dept. |
| 2131-05-22 21:49:00 | Admission | Admitted from EMERGENCY ROOM (OBSERVATION ADMIT) |
| 2131-05-22 21:50:33 | ICU Admission | Coronary Care Unit (CCU) (LOS: 8.8 days) |
| 2131-05-31 17:55:04 | Transfer | → Med/Surg (transfer) |
| 2131-06-01 10:52:54 | Transfer | → Med/Surg (transfer) |
| 2131-06-04 13:43:00 | Discharge | To HOME |

## 10. Missing / Ambiguous Data

- No obvious missing critical fields detected.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
