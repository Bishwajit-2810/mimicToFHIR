# Encounter Report — HADM 27617929

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 27617929 |
| Subject ID | 10037975 |
| Patient Sex | M |
| Patient Anchor Age (at anchor year) | 60 |
| Anchor Year | 2185 |
| Admission Time | 2185-01-17 19:11:00 |
| Discharge Time | 2185-01-22 14:25:00 |
| Admission Type | URGENT |
| Admission Location | TRANSFER FROM HOSPITAL |
| Discharge Location | DIED |
| Insurance | Medicare |
| Language | ENGLISH |
| Marital Status | MARRIED |
| Race/Ethnicity | UNKNOWN |
| ED Registration | N/A |
| ED Departure | N/A |
| In-Hospital Mortality | YES — Death time: 2185-01-22 14:25:00 |
| Date of Death (overall) | 2185-01-22 |

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
| 2185-01-17 19:12:12 | N/A | MED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-9 `03849`: Other septicemia due to gram-negative organisms
- (seq 2) ICD-9 `51881`: Acute respiratory failure
- (seq 3) ICD-9 `5845`: Acute kidney failure with lesion of tubular necrosis
- (seq 4) ICD-9 `78552`: Septic shock
- (seq 5) ICD-9 `4820`: Pneumonia due to Klebsiella pneumoniae

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-9 | `03849` | Other septicemia due to gram-negative organisms |
| 2 | ICD-9 | `51881` | Acute respiratory failure |
| 3 | ICD-9 | `5845` | Acute kidney failure with lesion of tubular necrosis |
| 4 | ICD-9 | `78552` | Septic shock |
| 5 | ICD-9 | `4820` | Pneumonia due to Klebsiella pneumoniae |
| 6 | ICD-9 | `28749` | Other secondary thrombocytopenia |
| 7 | ICD-9 | `2760` | Hyperosmolality and/or hypernatremia |
| 8 | ICD-9 | `2762` | Acidosis |
| 9 | ICD-9 | `5559` | Regional enteritis of unspecified site |
| 10 | ICD-9 | `99592` | Severe sepsis |
| 11 | ICD-9 | `496` | Chronic airway obstruction, not elsewhere classified |
| 12 | ICD-9 | `41401` | Coronary atherosclerosis of native coronary artery |
| 13 | ICD-9 | `5859` | Chronic kidney disease, unspecified |
| 14 | ICD-9 | `42731` | Atrial fibrillation |
| 15 | ICD-9 | `3051` | Tobacco use disorder |
| 16 | ICD-9 | `V1254` | Personal history of transient ischemic attack (TIA), and cerebral infarction without residual deficits |
| 17 | ICD-9 | `V667` | Encounter for palliative care |
| 18 | ICD-9 | `V4986` | Do not resuscitate status |
| 19 | ICD-9 | `7823` | Edema |
| 20 | ICD-9 | `3569` | Unspecified hereditary and idiopathic peripheral neuropathy |
| 21 | ICD-9 | `V090` | Infection with microorganisms resistant to penicillins |
| 22 | ICD-9 | `2859` | Anemia, unspecified |

## 5. ICU Stays

| Stay ID | First Care Unit | Last Care Unit | ICU Admit | ICU Discharge | LOS (days) |
|---|---|---|---|---|---|
| 39061571 | Medical Intensive Care Unit (MICU) | Medical Intensive Care Unit (MICU) | 2185-01-17 19:12:12 | 2185-01-22 16:16:52 | 4.88 |

## 6. Escalation / Severity Indicators

The following critical conditions or interventions were detected:

- **Acute Kidney Injury** (ICD diagnosis)
- **Arterial Line** (ICU procedure event)
- **Invasive Mechanical Ventilation** (ICU procedure event)
- **Pneumonia** (ICD diagnosis)
- **Respiratory Failure** (ICD diagnosis)
- **Sepsis** (ICD diagnosis)
- **Shock** (ICD diagnosis)

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2185-01-17 | ICD-9 | `9672` | Continuous invasive mechanical ventilation for 96 consecutive hours or more |
| 2 | 2185-01-18 | ICD-9 | `966` | Enteral infusion of concentrated nutritional substances |
| 3 | 2185-01-17 | ICD-9 | `3891` | Arterial catheterization |

### ICU Procedure Events (from `icu/procedureevents.csv.gz`)

- Invasive Ventilation (category: 2-Ventilation, started: 2185-01-17 19:15:00, status: FinishedRunning)
- 20 Gauge (category: Access Lines - Peripheral, started: 2185-01-17 19:40:00, status: Stopped)
- PICC Line (category: Access Lines - Invasive, started: 2185-01-17 19:41:00, status: Stopped)
- 22 Gauge (category: Access Lines - Peripheral, started: 2185-01-17 19:41:00, status: Stopped)
- Arterial Line (category: Access Lines - Invasive, started: 2185-01-17 21:20:00, status: FinishedRunning)
- Multi Lumen (category: Access Lines - Invasive, started: 2185-01-18 15:30:00, status: FinishedRunning)
- NEOB notified (category: 7-Communication, started: 2185-01-22 15:00:00, status: FinishedRunning)

## 8. Critical Findings (Charted Events)

- **Ventilator Type** (first noted: 2185-01-17 19:00:00)
- **Ventilator Tank #1** (first noted: 2185-01-18 00:00:00)
- **Ventilator Tank #2** (first noted: 2185-01-18 00:00:00)
- **Known difficult intubation** (first noted: 2185-01-17 19:00:00)
- **Code Status.** (first noted: 2185-01-20 05:44:00)

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2185-01-17 19:11:00 | Admission | Admitted from TRANSFER FROM HOSPITAL (URGENT) |
| 2185-01-17 19:12:12 | ICU Admission | Medical Intensive Care Unit (MICU) (LOS: 4.9 days) |
| 2185-01-22 14:25:00 | **IN-HOSPITAL DEATH** | |
| 2185-01-22 14:25:00 | Discharge | To DIED |

## 10. Missing / Ambiguous Data

- No ED registration time — admission may not have gone through ED.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
