# Encounter Report — HADM 23473524

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 23473524 |
| Subject ID | 10002428 |
| Patient Sex | F |
| Patient Anchor Age (at anchor year) | 80 |
| Anchor Year | 2155 |
| Admission Time | 2156-05-11 14:49:00 |
| Discharge Time | 2156-05-22 14:16:00 |
| Admission Type | EW EMER. |
| Admission Location | EMERGENCY ROOM |
| Discharge Location | CHRONIC/LONG TERM ACUTE CARE |
| Insurance | Medicare |
| Language | ENGLISH |
| Marital Status | WIDOWED |
| Race/Ethnicity | WHITE |
| ED Registration | 2156-05-11 11:29:00 |
| ED Departure | 2156-05-11 16:53:00 |
| In-Hospital Mortality | No |
| Date of Death (overall) | N/A |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| APR | 720 | SEPTICEMIA & DISSEMINATED INFECTIONS | 4.0 | 4.0 |
| HCFA | 870 | SEPTICEMIA OR SEVERE SEPSIS W MV 96+ HOURS | N/A | N/A |

### Primary Diagnosis (seq_num = 1)

- **ICD-9 03843**: Septicemia due to pseudomonas

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2156-05-11 14:49:34 | N/A | MED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-9 `03843`: Septicemia due to pseudomonas
- (seq 2) ICD-9 `51881`: Acute respiratory failure
- (seq 3) ICD-9 `42843`: Acute on chronic combined systolic and diastolic heart failure
- (seq 4) ICD-9 `5990`: Urinary tract infection, site not specified
- (seq 5) ICD-9 `00845`: Intestinal infection due to Clostridium difficile

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-9 | `03843` | Septicemia due to pseudomonas |
| 2 | ICD-9 | `51881` | Acute respiratory failure |
| 3 | ICD-9 | `42843` | Acute on chronic combined systolic and diastolic heart failure |
| 4 | ICD-9 | `5990` | Urinary tract infection, site not specified |
| 5 | ICD-9 | `00845` | Intestinal infection due to Clostridium difficile |
| 6 | ICD-9 | `99591` | Sepsis |
| 7 | ICD-9 | `4280` | Congestive heart failure, unspecified |
| 8 | ICD-9 | `2859` | Anemia, unspecified |
| 9 | ICD-9 | `53081` | Esophageal reflux |
| 10 | ICD-9 | `6930` | Dermatitis due to drugs and medicines taken internally |
| 11 | ICD-9 | `1123` | Candidiasis of skin and nails |
| 12 | ICD-9 | `73300` | Osteoporosis, unspecified |
| 13 | ICD-9 | `7102` | Sicca syndrome |
| 14 | ICD-9 | `2720` | Pure hypercholesterolemia |
| 15 | ICD-9 | `4019` | Unspecified essential hypertension |
| 16 | ICD-9 | `2449` | Unspecified acquired hypothyroidism |
| 17 | ICD-9 | `4240` | Mitral valve disorders |
| 18 | ICD-9 | `V707` | Examination of participant in clinical trial |

## 5. ICU Stays

| Stay ID | First Care Unit | Last Care Unit | ICU Admit | ICU Discharge | LOS (days) |
|---|---|---|---|---|---|
| 35479615 | Surgical Intensive Care Unit (SICU) | Medical Intensive Care Unit (MICU) | 2156-05-11 14:49:34 | 2156-05-22 14:16:46 | 10.98 |

## 6. Escalation / Severity Indicators

The following critical conditions or interventions were detected:

- **Arterial Line** (ICU procedure event)
- **Invasive Mechanical Ventilation** (ICU procedure event)
- **Respiratory Failure** (ICD diagnosis)
- **Sepsis** (ICD diagnosis)

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2156-05-11 | ICD-9 | `9672` | Continuous invasive mechanical ventilation for 96 consecutive hours or more |
| 2 | 2156-05-11 | ICD-9 | `9604` | Insertion of endotracheal tube |
| 3 | 2156-05-11 | ICD-9 | `3891` | Arterial catheterization |
| 4 | 2156-05-11 | ICD-9 | `3897` | Central venous catheter placement with guidance |

### ICU Procedure Events (from `icu/procedureevents.csv.gz`)

- Invasive Ventilation (category: 2-Ventilation, started: 2156-05-11 16:05:00, status: FinishedRunning)
- 18 Gauge (category: Access Lines - Peripheral, started: 2156-05-11 17:51:00, status: FinishedRunning)
- Arterial Line (category: Access Lines - Invasive, started: 2156-05-11 17:51:00, status: FinishedRunning)
- X-ray (category: 5-Imaging, started: 2156-05-11 17:52:00, status: FinishedRunning)
- Nasal Swab (category: 6-Cultures, started: 2156-05-11 17:52:00, status: FinishedRunning)
- Midline (category: Access Lines - Invasive, started: 2156-05-11 19:19:00, status: FinishedRunning)
- Blood Cultured (category: 6-Cultures, started: 2156-05-13 11:00:00, status: FinishedRunning)
- PICC Line (category: Access Lines - Invasive, started: 2156-05-15 09:00:00, status: FinishedRunning)
- Family updated by RN (category: 7-Communication, started: 2156-05-16 13:00:00, status: FinishedRunning)
- EKG (category: 4-Procedures, started: 2156-05-16 23:33:00, status: FinishedRunning)
- Pan Culture (category: 6-Cultures, started: 2156-05-17 20:45:00, status: FinishedRunning)
- Chest X-Ray (category: 5-Imaging, started: 2156-05-20 03:06:00, status: FinishedRunning)
- Extubation (category: 1-Intubation/Extubation, started: 2156-05-20 10:45:00, status: FinishedRunning)

## 8. Critical Findings (Charted Events)

- **Ventilator Mode** (first noted: 2156-05-11 16:00:00)
- **Ventilator Type** (first noted: 2156-05-11 16:00:00)
- **Ventilator Tank #2** (first noted: 2156-05-11 16:00:00)
- **Known difficult intubation** (first noted: 2156-05-11 20:00:00)

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2156-05-11 11:29:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2156-05-11 11:29:00 | Transfer | → Emergency Department (ED) |
| 2156-05-11 14:49:00 | Admission | Admitted from EMERGENCY ROOM (EW EMER.) |
| 2156-05-11 14:49:34 | ICU Admission | Surgical Intensive Care Unit (SICU) (LOS: 11.0 days) |
| 2156-05-11 14:52:30 | Transfer | → Surgical Intensive Care Unit (SICU) (transfer) |
| 2156-05-11 16:53:00 | ED Departure | Left Emergency Dept. |
| 2156-05-15 20:23:28 | Transfer | → Medical Intensive Care Unit (MICU) (transfer) |
| 2156-05-22 14:16:00 | Discharge | To CHRONIC/LONG TERM ACUTE CARE |

## 10. Missing / Ambiguous Data

- No obvious missing critical fields detected.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
