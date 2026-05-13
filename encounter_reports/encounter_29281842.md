# Encounter Report — HADM 29281842

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 29281842 |
| Subject ID | 10016742 |
| Patient Sex | F |
| Patient Anchor Age (at anchor year) | 58 |
| Anchor Year | 2178 |
| Admission Time | 2178-07-03 21:13:00 |
| Discharge Time | 2178-07-08 20:20:00 |
| Admission Type | EW EMER. |
| Admission Location | EMERGENCY ROOM |
| Discharge Location | SKILLED NURSING FACILITY |
| Insurance | Medicaid |
| Language | ENGLISH |
| Marital Status | SINGLE |
| Race/Ethnicity | BLACK/AFRICAN AMERICAN |
| ED Registration | 2178-07-03 17:39:00 |
| ED Departure | 2178-07-03 22:45:00 |
| In-Hospital Mortality | No |
| Date of Death (overall) | N/A |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| APR | 130 | RESPIRATORY SYSTEM DIAGNOSIS W VENTILATOR SUPPORT 96+ HOURS | 4.0 | 4.0 |
| HCFA | 207 | RESPIRATORY SYSTEM DIAGNOSIS W VENTILATOR SUPPORT >96 HOURS | N/A | N/A |

### Primary Diagnosis (seq_num = 1)

- **ICD-10 J95851**: Ventilator associated pneumonia

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2178-07-03 21:13:51 | N/A | MED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-10 `J95851`: Ventilator associated pneumonia
- (seq 2) ICD-10 `I214`: Non-ST elevation (NSTEMI) myocardial infarction
- (seq 3) ICD-10 `G9340`: Encephalopathy, unspecified
- (seq 4) ICD-10 `G1221`: Amyotrophic lateral sclerosis
- (seq 5) ICD-10 `N179`: Acute kidney failure, unspecified

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-10 | `J95851` | Ventilator associated pneumonia |
| 2 | ICD-10 | `I214` | Non-ST elevation (NSTEMI) myocardial infarction |
| 3 | ICD-10 | `G9340` | Encephalopathy, unspecified |
| 4 | ICD-10 | `G1221` | Amyotrophic lateral sclerosis |
| 5 | ICD-10 | `N179` | Acute kidney failure, unspecified |
| 6 | ICD-10 | `N10` | Acute pyelonephritis |
| 7 | ICD-10 | `E873` | Alkalosis |
| 8 | ICD-10 | `D721` | Eosinophilia |
| 9 | ICD-10 | `J9610` | Chronic respiratory failure, unspecified whether with hypoxia or hypercapnia |
| 10 | ICD-10 | `Z9911` | Dependence on respirator [ventilator] status |
| 11 | ICD-10 | `N390` | Urinary tract infection, site not specified |
| 12 | ICD-10 | `B965` | Pseudomonas (aeruginosa) (mallei) (pseudomallei) as the cause of diseases classified elsewhere |
| 13 | ICD-10 | `Z430` | Encounter for attention to tracheostomy |
| 14 | ICD-10 | `Z4689` | Encounter for fitting and adjustment of other specified devices |
| 15 | ICD-10 | `Z931` | Gastrostomy status |
| 16 | ICD-10 | `E119` | Type 2 diabetes mellitus without complications |
| 17 | ICD-10 | `B9620` | Unspecified Escherichia coli [E. coli] as the cause of diseases classified elsewhere |
| 18 | ICD-10 | `Z7982` | Long term (current) use of aspirin |
| 19 | ICD-10 | `N141` | Nephropathy induced by other drugs, medicaments and biological substances |
| 20 | ICD-10 | `T360X5A` | Adverse effect of penicillins, initial encounter |
| 21 | ICD-10 | `Y92230` | Patient room in hospital as the place of occurrence of the external cause |
| 22 | ICD-10 | `F259` | Schizoaffective disorder, unspecified |
| 23 | ICD-10 | `Z6829` | Body mass index (BMI) 29.0-29.9, adult |
| 24 | ICD-10 | `Z781` | Physical restraint status |
| 25 | ICD-10 | `G40909` | Epilepsy, unspecified, not intractable, without status epilepticus |

## 5. ICU Stays

| Stay ID | First Care Unit | Last Care Unit | ICU Admit | ICU Discharge | LOS (days) |
|---|---|---|---|---|---|
| 37057036 | Surgical Intensive Care Unit (SICU) | Surgical Intensive Care Unit (SICU) | 2178-07-03 22:45:00 | 2178-07-08 20:34:44 | 4.91 |

## 6. Escalation / Severity Indicators

The following critical conditions or interventions were detected:

- **Acute Kidney Injury** (ICD diagnosis)
- **Invasive Mechanical Ventilation** (ICU procedure event)
- **Respiratory Failure** (ICD diagnosis)

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2178-07-03 | ICD-10 | `5A1955Z` | Respiratory Ventilation, Greater than 96 Consecutive Hours |
| 2 | 2178-07-07 | ICD-10 | `02HV33Z` | Insertion of Infusion Device into Superior Vena Cava, Percutaneous Approach |

### ICU Procedure Events (from `icu/procedureevents.csv.gz`)

- Invasive Ventilation (category: 2-Ventilation, started: 2178-07-03 23:00:00, status: FinishedRunning)
- 20 Gauge (category: Access Lines - Peripheral, started: 2178-07-04 00:00:00, status: FinishedRunning)
- Foley Catheter (category: GI/GU, started: 2178-07-04 00:00:00, status: FinishedRunning)
- 18 Gauge (category: Access Lines - Peripheral, started: 2178-07-04 01:10:00, status: FinishedRunning)
- Blood Cultured (category: 6-Cultures, started: 2178-07-06 12:30:00, status: FinishedRunning)
- Urine Culture (category: 6-Cultures, started: 2178-07-06 12:35:00, status: FinishedRunning)
- Wound Culture (category: 6-Cultures, started: 2178-07-06 17:00:00, status: FinishedRunning)
- PICC Line (category: Access Lines - Invasive, started: 2178-07-07 12:00:00, status: FinishedRunning)

## 8. Critical Findings (Charted Events)

- **Ventilator Type** (first noted: 2178-07-03 23:09:00)
- **Ventilator Mode (Hamilton)** (first noted: 2178-07-03 23:10:00)
- **Ventilator Tank #2** (first noted: 2178-07-04 04:00:00)
- **Code Status** (first noted: 2178-07-07 00:39:00)

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2178-07-03 17:39:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2178-07-03 17:39:00 | Transfer | → Emergency Department (ED) |
| 2178-07-03 21:13:00 | Admission | Admitted from EMERGENCY ROOM (EW EMER.) |
| 2178-07-03 22:45:00 | ED Departure | Left Emergency Dept. |
| 2178-07-03 22:45:00 | ICU Admission | Surgical Intensive Care Unit (SICU) (LOS: 4.9 days) |
| 2178-07-08 20:20:00 | Discharge | To SKILLED NURSING FACILITY |

## 10. Missing / Ambiguous Data

- No obvious missing critical fields detected.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
