# Encounter Report — HADM 22205327

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 22205327 |
| Subject ID | 10029291 |
| Patient Sex | F |
| Patient Anchor Age (at anchor year) | 50 |
| Anchor Year | 2123 |
| Admission Time | 2123-02-20 01:59:00 |
| Discharge Time | 2123-03-10 15:30:00 |
| Admission Type | EW EMER. |
| Admission Location | EMERGENCY ROOM |
| Discharge Location | HOME HEALTH CARE |
| Insurance | Medicare |
| Language | ENGLISH |
| Marital Status | DIVORCED |
| Race/Ethnicity | WHITE |
| ED Registration | 2123-02-19 23:57:00 |
| ED Departure | 2123-02-20 04:13:00 |
| In-Hospital Mortality | No |
| Date of Death (overall) | N/A |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| APR | 130 | RESPIRATORY SYSTEM DIAGNOSIS W VENTILATOR SUPPORT 96+ HOURS | 4.0 | 4.0 |
| HCFA | 207 | RESPIRATORY SYSTEM DIAGNOSIS W VENTILATOR SUPPORT >96 HOURS | N/A | N/A |

### Primary Diagnosis (seq_num = 1)

- **ICD-10 I2602**: Saddle embolus of pulmonary artery with acute cor pulmonale

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2123-02-20 02:00:12 | N/A | CMED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-10 `I2602`: Saddle embolus of pulmonary artery with acute cor pulmonale
- (seq 2) ICD-10 `K7201`: Acute and subacute hepatic failure with coma
- (seq 3) ICD-10 `N170`: Acute kidney failure with tubular necrosis
- (seq 4) ICD-10 `R578`: Other shock
- (seq 5) ICD-10 `G92`: Toxic encephalopathy

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-10 | `I2602` | Saddle embolus of pulmonary artery with acute cor pulmonale |
| 2 | ICD-10 | `K7201` | Acute and subacute hepatic failure with coma |
| 3 | ICD-10 | `N170` | Acute kidney failure with tubular necrosis |
| 4 | ICD-10 | `R578` | Other shock |
| 5 | ICD-10 | `G92` | Toxic encephalopathy |
| 6 | ICD-10 | `A047` | Enterocolitis due to Clostridium difficile |
| 7 | ICD-10 | `F5001` | Anorexia nervosa, restricting type |
| 8 | ICD-10 | `J9601` | Acute respiratory failure with hypoxia |
| 9 | ICD-10 | `E1142` | Type 2 diabetes mellitus with diabetic polyneuropathy |
| 10 | ICD-10 | `E11621` | Type 2 diabetes mellitus with foot ulcer |
| 11 | ICD-10 | `Z794` | Long term (current) use of insulin |
| 12 | ICD-10 | `F4310` | Post-traumatic stress disorder, unspecified |
| 13 | ICD-10 | `F39` | Unspecified mood [affective] disorder |
| 14 | ICD-10 | `F28` | Other psychotic disorder not due to a substance or known physiological condition |
| 15 | ICD-10 | `F514` | Sleep terrors [night terrors] |
| 16 | ICD-10 | `F603` | Borderline personality disorder |
| 17 | ICD-10 | `K219` | Gastro-esophageal reflux disease without esophagitis |
| 18 | ICD-10 | `J449` | Chronic obstructive pulmonary disease, unspecified |
| 19 | ICD-10 | `Z720` | Tobacco use |
| 20 | ICD-10 | `E785` | Hyperlipidemia, unspecified |
| 21 | ICD-10 | `E038` | Other specified hypothyroidism |
| 22 | ICD-10 | `I129` | Hypertensive chronic kidney disease with stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease |
| 23 | ICD-10 | `N189` | Chronic kidney disease, unspecified |
| 24 | ICD-10 | `N141` | Nephropathy induced by other drugs, medicaments and biological substances |
| 25 | ICD-10 | `T508X5A` | Adverse effect of diagnostic agents, initial encounter |
| 26 | ICD-10 | `Y92238` | Other place in hospital as the place of occurrence of the external cause |
| 27 | ICD-10 | `E876` | Hypokalemia |
| 28 | ICD-10 | `Z915` | Personal history of self-harm |
| 29 | ICD-10 | `F1220` | Cannabis dependence, uncomplicated |
| 30 | ICD-10 | `T4275XA` | Adverse effect of unspecified antiepileptic and sedative-hypnotic drugs, initial encounter |
| 31 | ICD-10 | `Y92230` | Patient room in hospital as the place of occurrence of the external cause |
| 32 | ICD-10 | `F319` | Bipolar disorder, unspecified |
| 33 | ICD-10 | `I4581` | Long QT syndrome |
| 34 | ICD-10 | `K047` | Periapical abscess without sinus |
| 35 | ICD-10 | `B954` | Other streptococcus as the cause of diseases classified elsewhere |
| 36 | ICD-10 | `Z1639` | Resistance to other specified antimicrobial drug |
| 37 | ICD-10 | `R1312` | Dysphagia, oropharyngeal phase |
| 38 | ICD-10 | `T17920A` | Food in respiratory tract, part unspecified causing asphyxiation, initial encounter |
| 39 | ICD-10 | `R490` | Dysphonia |

## 5. ICU Stays

| Stay ID | First Care Unit | Last Care Unit | ICU Admit | ICU Discharge | LOS (days) |
|---|---|---|---|---|---|
| 36059427 | Coronary Care Unit (CCU) | Coronary Care Unit (CCU) | 2123-02-20 04:13:00 | 2123-02-26 12:03:56 | 6.33 |
| 35146796 | Coronary Care Unit (CCU) | Coronary Care Unit (CCU) | 2123-02-26 12:12:32 | 2123-03-04 23:36:14 | 6.47 |

## 6. Escalation / Severity Indicators

The following critical conditions or interventions were detected:

- **Acute Kidney Injury** (ICD diagnosis)
- **Arterial Line** (ICU procedure event)
- **Invasive Mechanical Ventilation** (ICU procedure event)
- **Liver Failure** (ICD diagnosis)
- **Non-Invasive Ventilation (NIV/BiPAP)** (ICU procedure event)
- **Renal Replacement Therapy / Dialysis** (ICU procedure event)
- **Respiratory Failure** (ICD diagnosis)
- **Shock** (ICD diagnosis)

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2123-02-20 | ICD-10 | `3E04317` | Introduction of Other Thrombolytic into Central Vein, Percutaneous Approach |
| 2 | 2123-02-20 | ICD-10 | `5A1955Z` | Respiratory Ventilation, Greater than 96 Consecutive Hours |
| 3 | 2123-02-20 | ICD-10 | `0BH17EZ` | Insertion of Endotracheal Airway into Trachea, Via Natural or Artificial Opening |
| 4 | 2123-02-20 | ICD-10 | `02HV33Z` | Insertion of Infusion Device into Superior Vena Cava, Percutaneous Approach |
| 5 | 2123-02-20 | ICD-10 | `B548ZZA` | Ultrasonography of Superior Vena Cava, Guidance |
| 6 | 2123-02-24 | ICD-10 | `02HV33Z` | Insertion of Infusion Device into Superior Vena Cava, Percutaneous Approach |
| 7 | 2123-02-24 | ICD-10 | `B548ZZA` | Ultrasonography of Superior Vena Cava, Guidance |
| 8 | 2123-02-24 | ICD-10 | `5A1D60Z` | Performance of Urinary Filtration, Multiple |
| 9 | 2123-02-24 | ICD-10 | `3E0G76Z` | Introduction of Nutritional Substance into Upper GI, Via Natural or Artificial Opening |
| 10 | 2123-02-24 | ICD-10 | `0CJS8ZZ` | Inspection of Larynx, Via Natural or Artificial Opening Endoscopic |

### ICU Procedure Events (from `icu/procedureevents.csv.gz`)

- Invasive Ventilation (category: 2-Ventilation, started: 2123-02-20 04:30:00, status: FinishedRunning)
- 18 Gauge (category: Access Lines - Peripheral, started: 2123-02-20 04:41:00, status: FinishedRunning)
- Arterial Line (category: Access Lines - Invasive, started: 2123-02-20 04:43:00, status: FinishedRunning)
- Multi Lumen (category: Access Lines - Invasive, started: 2123-02-20 19:30:00, status: FinishedRunning)
- Sputum Culture (category: 6-Cultures, started: 2123-02-22 00:00:00, status: FinishedRunning)
- Blood Cultured (category: 6-Cultures, started: 2123-02-22 00:15:00, status: FinishedRunning)
- Urine Culture (category: 6-Cultures, started: 2123-02-22 00:35:00, status: FinishedRunning)
- CT scan (category: 5-Imaging, started: 2123-02-23 13:05:00, status: FinishedRunning)
- Family meeting held (category: 7-Communication, started: 2123-02-23 14:00:00, status: FinishedRunning)
- Dialysis Catheter (category: Access Lines - Invasive, started: 2123-02-24 15:30:00, status: FinishedRunning)
- Chest X-Ray (category: 5-Imaging, started: 2123-02-24 16:00:00, status: FinishedRunning)
- Hemodialysis (category: 4-Procedures, started: 2123-02-25 09:24:00, status: FinishedRunning)
- Extubation (category: 1-Intubation/Extubation, started: 2123-02-25 15:30:00, status: FinishedRunning)
- Non-invasive Ventilation (category: 2-Ventilation, started: 2123-02-25 15:50:00, status: FinishedRunning)
- 22 Gauge (category: Access Lines - Peripheral, started: 2123-03-03 16:15:00, status: FinishedRunning)
- 20 Gauge (category: Access Lines - Peripheral, started: 2123-03-03 16:15:00, status: FinishedRunning)

## 8. Critical Findings (Charted Events)

- **Ventilator Type** (first noted: 2123-02-20 05:00:00)
- **Ventilator Mode (Hamilton)** (first noted: 2123-02-20 05:00:00)
- **Ventilator Tank #2** (first noted: 2123-02-22 07:00:00)
- **Known difficult intubation** (first noted: 2123-02-20 05:00:00)
- **Code Status** (first noted: 2123-02-20 04:29:00)
- **Dialysis Catheter Type** (first noted: 2123-02-24 15:30:00)
- **Dialysis Catheter Placement Confirmed by X-ray** (first noted: 2123-02-24 15:30:00)
- **Dialysis Catheter placed in outside facility** (first noted: 2123-02-24 15:30:00)

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2123-02-19 23:57:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2123-02-19 23:57:00 | Transfer | → Emergency Department (ED) |
| 2123-02-20 01:59:00 | Admission | Admitted from EMERGENCY ROOM (EW EMER.) |
| 2123-02-20 04:13:00 | ED Departure | Left Emergency Dept. |
| 2123-02-20 04:13:00 | ICU Admission | Coronary Care Unit (CCU) (LOS: 6.3 days) |
| 2123-02-26 12:03:56 | Transfer | → Medicine/Cardiology (transfer) |
| 2123-02-26 12:12:32 | ICU Admission | Coronary Care Unit (CCU) (LOS: 6.5 days) |
| 2123-02-26 12:12:32 | Transfer | → Coronary Care Unit (CCU) (transfer) |
| 2123-03-04 23:36:14 | Transfer | → Cardiac Surgery (transfer) |
| 2123-03-10 15:30:00 | Discharge | To HOME HEALTH CARE |

## 10. Missing / Ambiguous Data

- No obvious missing critical fields detected.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
