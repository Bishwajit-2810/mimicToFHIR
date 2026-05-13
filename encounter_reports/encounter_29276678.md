# Encounter Report — HADM 29276678

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 29276678 |
| Subject ID | 10035631 |
| Patient Sex | M |
| Patient Anchor Age (at anchor year) | 63 |
| Anchor Year | 2112 |
| Admission Time | 2116-02-27 20:55:00 |
| Discharge Time | 2116-03-12 07:45:00 |
| Admission Type | OBSERVATION ADMIT |
| Admission Location | EMERGENCY ROOM |
| Discharge Location | DIED |
| Insurance | Other |
| Language | ENGLISH |
| Marital Status | MARRIED |
| Race/Ethnicity | WHITE |
| ED Registration | 2116-02-27 15:33:00 |
| ED Departure | 2116-02-27 22:03:00 |
| In-Hospital Mortality | YES — Death time: 2116-03-12 07:45:00 |
| Date of Death (overall) | 2116-03-12 |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| APR | 130 | RESPIRATORY SYSTEM DIAGNOSIS W VENTILATOR SUPPORT 96+ HOURS | 4.0 | 4.0 |
| HCFA | 207 | RESPIRATORY SYSTEM DIAGNOSIS W VENTILATOR SUPPORT >96 HOURS | N/A | N/A |

### Primary Diagnosis (seq_num = 1)

- **ICD-10 J9601**: Acute respiratory failure with hypoxia

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2116-02-27 20:56:27 | N/A | OMED |
| 2116-02-29 10:01:37 | OMED | MED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-10 `J9601`: Acute respiratory failure with hypoxia
- (seq 2) ICD-10 `E883`: Tumor lysis syndrome
- (seq 3) ICD-10 `R6520`: Severe sepsis without septic shock
- (seq 4) ICD-10 `A419`: Sepsis, unspecified organism
- (seq 5) ICD-10 `B441`: Other pulmonary aspergillosis

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-10 | `J9601` | Acute respiratory failure with hypoxia |
| 2 | ICD-10 | `E883` | Tumor lysis syndrome |
| 3 | ICD-10 | `R6520` | Severe sepsis without septic shock |
| 4 | ICD-10 | `A419` | Sepsis, unspecified organism |
| 5 | ICD-10 | `B441` | Other pulmonary aspergillosis |
| 6 | ICD-10 | `J90` | Pleural effusion, not elsewhere classified |
| 7 | ICD-10 | `B59` | Pneumocystosis |
| 8 | ICD-10 | `E872` | Acidosis |
| 9 | ICD-10 | `J159` | Unspecified bacterial pneumonia |
| 10 | ICD-10 | `D89813` | Graft-versus-host disease, unspecified |
| 11 | ICD-10 | `Z9484` | Stem cells transplant status |
| 12 | ICD-10 | `C92Z0` | Other myeloid leukemia not having achieved remission |
| 13 | ICD-10 | `J9811` | Atelectasis |
| 14 | ICD-10 | `N179` | Acute kidney failure, unspecified |
| 15 | ICD-10 | `E871` | Hypo-osmolality and hyponatremia |
| 16 | ICD-10 | `I248` | Other forms of acute ischemic heart disease |
| 17 | ICD-10 | `R042` | Hemoptysis |
| 18 | ICD-10 | `D689` | Coagulation defect, unspecified |
| 19 | ICD-10 | `D709` | Neutropenia, unspecified |
| 20 | ICD-10 | `R5081` | Fever presenting with conditions classified elsewhere |
| 21 | ICD-10 | `E860` | Dehydration |
| 22 | ICD-10 | `E875` | Hyperkalemia |
| 23 | ICD-10 | `G893` | Neoplasm related pain (acute) (chronic) |
| 24 | ICD-10 | `I4891` | Unspecified atrial fibrillation |
| 25 | ICD-10 | `D6959` | Other secondary thrombocytopenia |
| 26 | ICD-10 | `D630` | Anemia in neoplastic disease |
| 27 | ICD-10 | `H1133` | Conjunctival hemorrhage, bilateral |
| 28 | ICD-10 | `T451X5A` | Adverse effect of antineoplastic and immunosuppressive drugs, initial encounter |
| 29 | ICD-10 | `Z66` | Do not resuscitate |
| 30 | ICD-10 | `Z515` | Encounter for palliative care |
| 31 | ICD-10 | `Z781` | Physical restraint status |
| 32 | ICD-10 | `Z006` | Encounter for examination for normal comparison and control in clinical research program |
| 33 | ICD-10 | `Z853` | Personal history of malignant neoplasm of breast |
| 34 | ICD-10 | `Z9012` | Acquired absence of left breast and nipple |
| 35 | ICD-10 | `Z87891` | Personal history of nicotine dependence |
| 36 | ICD-10 | `Y92230` | Patient room in hospital as the place of occurrence of the external cause |

## 5. ICU Stays

| Stay ID | First Care Unit | Last Care Unit | ICU Admit | ICU Discharge | LOS (days) |
|---|---|---|---|---|---|
| 30932571 | Medical/Surgical Intensive Care Unit (MICU/SICU) | Medical/Surgical Intensive Care Unit (MICU/SICU) | 2116-02-28 18:43:20 | 2116-03-10 06:35:04 | 10.49 |

## 6. Escalation / Severity Indicators

The following critical conditions or interventions were detected:

- **Acute Kidney Injury** (ICD diagnosis)
- **Arterial Line** (ICU procedure event)
- **Endotracheal Intubation** (ICU procedure event)
- **Invasive Mechanical Ventilation** (ICU procedure event)
- **Pneumonia** (ICD diagnosis)
- **Renal Replacement Therapy / Dialysis** (ICU procedure event)
- **Respiratory Failure** (ICD diagnosis)
- **Sepsis** (ICD diagnosis)

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2116-02-29 | ICD-10 | `5A1955Z` | Respiratory Ventilation, Greater than 96 Consecutive Hours |
| 2 | 2116-02-29 | ICD-10 | `0BH17EZ` | Insertion of Endotracheal Airway into Trachea, Via Natural or Artificial Opening |
| 3 | 2116-02-29 | ICD-10 | `3E04305` | Introduction of Other Antineoplastic into Central Vein, Percutaneous Approach |
| 4 | 2116-02-29 | ICD-10 | `6A551Z3` | Pheresis of Plasma, Multiple |
| 5 | 2116-03-02 | ICD-10 | `0B968ZX` | Drainage of Right Lower Lobe Bronchus, Via Natural or Artificial Opening Endoscopic, Diagnostic |
| 6 | 2116-03-04 | ICD-10 | `5A1D00Z` | Performance of Urinary Filtration, Single |
| 7 | 2116-03-02 | ICD-10 | `3E0G76Z` | Introduction of Nutritional Substance into Upper GI, Via Natural or Artificial Opening |
| 8 | 2116-03-07 | ICD-10 | `0HB7XZX` | Excision of Abdomen Skin, External Approach, Diagnostic |

### ICU Procedure Events (from `icu/procedureevents.csv.gz`)

- PICC Line (category: Access Lines - Invasive, started: 2116-02-28 18:54:00, status: FinishedRunning)
- Pheresis Catheter (category: Access Lines - Invasive, started: 2116-02-29 04:15:00, status: FinishedRunning)
- Plasma Pheresis. (category: 4-Procedures, started: 2116-02-29 08:00:00, status: FinishedRunning)
- Intubation (category: 1-Intubation/Extubation, started: 2116-02-29 16:03:00, status: FinishedRunning)
- Invasive Ventilation (category: 2-Ventilation, started: 2116-02-29 16:12:00, status: FinishedRunning)
- Arterial Line (category: Access Lines - Invasive, started: 2116-02-29 21:36:00, status: FinishedRunning)
- Foley Catheter (category: GI/GU, started: 2116-02-29 23:28:00, status: FinishedRunning)
- 20 Gauge (category: Access Lines - Peripheral, started: 2116-03-02 03:36:00, status: FinishedRunning)
- Bronchoscopy (category: 4-Procedures, started: 2116-03-02 15:00:00, status: FinishedRunning)
- Chest X-Ray (category: 5-Imaging, started: 2116-03-03 08:35:00, status: FinishedRunning)
- Blood Cultured (category: 6-Cultures, started: 2116-03-03 10:00:00, status: FinishedRunning)
- Urine Culture (category: 6-Cultures, started: 2116-03-03 10:00:00, status: FinishedRunning)
- Stool Culture (category: 6-Cultures, started: 2116-03-04 12:41:00, status: FinishedRunning)
- Dialysis - CRRT (category: Dialysis, started: 2116-03-04 14:42:00, status: FinishedRunning)
- Ultrasound (category: 5-Imaging, started: 2116-03-04 16:06:00, status: FinishedRunning)
- Transthoracic Echo (category: 5-Imaging, started: 2116-03-05 20:00:00, status: FinishedRunning)
- EKG (category: 4-Procedures, started: 2116-03-07 11:00:00, status: FinishedRunning)
- CRRT Filter Change (category: Dialysis, started: 2116-03-07 15:01:00, status: FinishedRunning)
- Cardioversion/Defibrillation (category: 3-Significant Events, started: 2116-03-07 20:45:00, status: FinishedRunning)

## 8. Critical Findings (Charted Events)

- **Ventilator Tank #1** (first noted: 2116-03-03 12:00:00)
- **Ventilator Mode (Hamilton)** (first noted: 2116-02-29 16:00:00)
- **Ventilator Tank #2** (first noted: 2116-03-03 12:00:00)
- **Known difficult intubation** (first noted: 2116-02-29 16:00:00)
- **Code Status** (first noted: 2116-03-04 09:37:00)

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2116-02-27 15:33:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2116-02-27 15:33:00 | Transfer | → Emergency Department (ED) |
| 2116-02-27 20:55:00 | Admission | Admitted from EMERGENCY ROOM (OBSERVATION ADMIT) |
| 2116-02-27 22:03:00 | ED Departure | Left Emergency Dept. |
| 2116-02-28 18:43:20 | ICU Admission | Medical/Surgical Intensive Care Unit (MICU/SICU) (LOS: 10.5 days) |
| 2116-02-28 18:43:20 | Transfer | → Medical/Surgical Intensive Care Unit (MICU/SICU) (transfer) |
| 2116-03-03 15:16:46 | Transfer | → Medical/Surgical Intensive Care Unit (MICU/SICU) (transfer) |
| 2116-03-10 06:35:04 | Transfer | → Hematology/Oncology (transfer) |
| 2116-03-12 07:45:00 | **IN-HOSPITAL DEATH** | |
| 2116-03-12 07:45:00 | Discharge | To DIED |

## 10. Missing / Ambiguous Data

- No obvious missing critical fields detected.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
