# Encounter Report — HADM 24982426

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 24982426 |
| Subject ID | 10002495 |
| Patient Sex | M |
| Patient Anchor Age (at anchor year) | 81 |
| Anchor Year | 2141 |
| Admission Time | 2141-05-22 20:17:00 |
| Discharge Time | 2141-05-29 17:41:00 |
| Admission Type | URGENT |
| Admission Location | TRANSFER FROM HOSPITAL |
| Discharge Location | SKILLED NURSING FACILITY |
| Insurance | Medicare |
| Language | ENGLISH |
| Marital Status | MARRIED |
| Race/Ethnicity | UNKNOWN |
| ED Registration | N/A |
| ED Departure | N/A |
| In-Hospital Mortality | No |
| Date of Death (overall) | N/A |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| HCFA | 270 | OTHER MAJOR CARDIOVASCULAR PROCEDURES W MCC | N/A | N/A |
| APR | 174 | PERCUTANEOUS CORONARY INTERVENTION W AMI | 4.0 | 4.0 |

### Primary Diagnosis (seq_num = 1)

- **ICD-10 I214**: Non-ST elevation (NSTEMI) myocardial infarction

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2141-05-22 20:18:01 | N/A | CMED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-10 `I214`: Non-ST elevation (NSTEMI) myocardial infarction
- (seq 2) ICD-10 `R570`: Cardiogenic shock
- (seq 3) ICD-10 `I509`: Heart failure, unspecified
- (seq 4) ICD-10 `R578`: Other shock
- (seq 5) ICD-10 `A047`: Enterocolitis due to Clostridium difficile

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-10 | `I214` | Non-ST elevation (NSTEMI) myocardial infarction |
| 2 | ICD-10 | `R570` | Cardiogenic shock |
| 3 | ICD-10 | `I509` | Heart failure, unspecified |
| 4 | ICD-10 | `R578` | Other shock |
| 5 | ICD-10 | `A047` | Enterocolitis due to Clostridium difficile |
| 6 | ICD-10 | `N179` | Acute kidney failure, unspecified |
| 7 | ICD-10 | `S3730XA` | Unspecified injury of urethra, initial encounter |
| 8 | ICD-10 | `I2510` | Atherosclerotic heart disease of native coronary artery without angina pectoris |
| 9 | ICD-10 | `E118` | Type 2 diabetes mellitus with unspecified complications |
| 10 | ICD-10 | `X58XXXA` | Exposure to other specified factors, initial encounter |
| 11 | ICD-10 | `Y92239` | Unspecified place in hospital as the place of occurrence of the external cause |
| 12 | ICD-10 | `I10` | Essential (primary) hypertension |
| 13 | ICD-10 | `E785` | Hyperlipidemia, unspecified |
| 14 | ICD-10 | `T45515A` | Adverse effect of anticoagulants, initial encounter |
| 15 | ICD-10 | `Z86718` | Personal history of other venous thrombosis and embolism |
| 16 | ICD-10 | `Z7901` | Long term (current) use of anticoagulants |
| 17 | ICD-10 | `R310` | Gross hematuria |
| 18 | ICD-10 | `Z7902` | Long term (current) use of antithrombotics/antiplatelets |
| 19 | ICD-10 | `I480` | Paroxysmal atrial fibrillation |
| 20 | ICD-10 | `Z23` | Encounter for immunization |
| 21 | ICD-10 | `K2960` | Other gastritis without bleeding |
| 22 | ICD-10 | `B9681` | Helicobacter pylori [H. pylori] as the cause of diseases classified elsewhere |
| 23 | ICD-10 | `Z87891` | Personal history of nicotine dependence |
| 24 | ICD-10 | `I252` | Old myocardial infarction |
| 25 | ICD-10 | `R410` | Disorientation, unspecified |
| 26 | ICD-10 | `K219` | Gastro-esophageal reflux disease without esophagitis |

## 5. ICU Stays

| Stay ID | First Care Unit | Last Care Unit | ICU Admit | ICU Discharge | LOS (days) |
|---|---|---|---|---|---|
| 36753294 | Coronary Care Unit (CCU) | Coronary Care Unit (CCU) | 2141-05-22 20:18:01 | 2141-05-27 22:24:02 | 5.09 |

## 6. Escalation / Severity Indicators

The following critical conditions or interventions were detected:

- **Acute Kidney Injury** (ICD diagnosis)
- **Non-Invasive Ventilation (NIV/BiPAP)** (ICU procedure event)
- **Shock** (ICD diagnosis)

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2141-05-22 | ICD-10 | `027034Z` | Dilation of Coronary Artery, One Artery with Drug-eluting Intraluminal Device, Percutaneous Approach |
| 2 | 2141-05-23 | ICD-10 | `5A02210` | Assistance with Cardiac Output using Balloon Pump, Continuous |
| 3 | 2141-05-22 | ICD-10 | `4A023N7` | Measurement of Cardiac Sampling and Pressure, Left Heart, Percutaneous Approach |
| 4 | 2141-05-22 | ICD-10 | `B211YZZ` | Fluoroscopy of Multiple Coronary Arteries using Other Contrast |
| 5 | 2141-05-23 | ICD-10 | `4A023N6` | Measurement of Cardiac Sampling and Pressure, Right Heart, Percutaneous Approach |
| 6 | 2141-05-23 | ICD-10 | `B211YZZ` | Fluoroscopy of Multiple Coronary Arteries using Other Contrast |
| 7 | 2141-05-23 | ICD-10 | `3E1K78Z` | Irrigation of Genitourinary Tract using Irrigating Substance, Via Natural or Artificial Opening |

### ICU Procedure Events (from `icu/procedureevents.csv.gz`)

- Foley Catheter (category: GI/GU, started: 2141-05-22 20:18:00, status: FinishedRunning)
- 20 Gauge (category: Access Lines - Peripheral, started: 2141-05-22 20:20:00, status: FinishedRunning)
- 18 Gauge (category: Access Lines - Peripheral, started: 2141-05-22 20:41:00, status: FinishedRunning)
- EKG (category: 4-Procedures, started: 2141-05-23 08:40:00, status: FinishedRunning)
- Transthoracic Echo (category: 5-Imaging, started: 2141-05-23 08:56:00, status: FinishedRunning)
- Non-invasive Ventilation (category: 2-Ventilation, started: 2141-05-23 20:15:00, status: FinishedRunning)
- PA Catheter (category: Access Lines - Invasive, started: 2141-05-23 23:42:00, status: FinishedRunning)
- IABP line (category: Access Lines - Invasive, started: 2141-05-24 01:00:00, status: FinishedRunning)
- Family updated by RN (category: 7-Communication, started: 2141-05-24 10:29:00, status: FinishedRunning)
- Chest X-Ray (category: 5-Imaging, started: 2141-05-24 23:00:00, status: FinishedRunning)
- Family updated by MD (category: 7-Communication, started: 2141-05-25 18:47:00, status: FinishedRunning)

## 8. Critical Findings (Charted Events)

- **Ventilator Type** (first noted: 2141-05-23 20:21:00)
- **Ventilator Mode (Hamilton)** (first noted: 2141-05-23 20:22:00)
- **Dialysis patient** (first noted: 2141-05-22 23:44:00)

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2141-05-22 20:17:00 | Admission | Admitted from TRANSFER FROM HOSPITAL (URGENT) |
| 2141-05-22 20:18:01 | ICU Admission | Coronary Care Unit (CCU) (LOS: 5.1 days) |
| 2141-05-27 22:24:02 | Transfer | → Medicine/Cardiology (transfer) |
| 2141-05-29 17:41:00 | Discharge | To SKILLED NURSING FACILITY |

## 10. Missing / Ambiguous Data

- No ED registration time — admission may not have gone through ED.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
