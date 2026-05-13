# Encounter Report — HADM 20321825

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 20321825 |
| Subject ID | 10002428 |
| Patient Sex | F |
| Patient Anchor Age (at anchor year) | 80 |
| Anchor Year | 2155 |
| Admission Time | 2156-04-30 20:35:00 |
| Discharge Time | 2156-05-03 16:36:00 |
| Admission Type | EW EMER. |
| Admission Location | EMERGENCY ROOM |
| Discharge Location | CHRONIC/LONG TERM ACUTE CARE |
| Insurance | Medicare |
| Language | ENGLISH |
| Marital Status | WIDOWED |
| Race/Ethnicity | WHITE |
| ED Registration | 2156-04-30 18:30:00 |
| ED Departure | 2156-04-30 21:53:00 |
| In-Hospital Mortality | No |
| Date of Death (overall) | N/A |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| APR | 133 | RESPIRATORY FAILURE | 3.0 | 3.0 |
| HCFA | 189 | PULMONARY EDEMA & RESPIRATORY FAILURE | N/A | N/A |

### Primary Diagnosis (seq_num = 1)

- **ICD-9 51881**: Acute respiratory failure

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2156-04-30 20:36:25 | N/A | MED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-9 `51881`: Acute respiratory failure
- (seq 2) ICD-9 `2764`: Mixed acid-base balance disorder
- (seq 3) ICD-9 `00845`: Intestinal infection due to Clostridium difficile
- (seq 4) ICD-9 `29281`: Drug-induced delirium
- (seq 5) ICD-9 `5119`: Unspecified pleural effusion

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-9 | `51881` | Acute respiratory failure |
| 2 | ICD-9 | `2764` | Mixed acid-base balance disorder |
| 3 | ICD-9 | `00845` | Intestinal infection due to Clostridium difficile |
| 4 | ICD-9 | `29281` | Drug-induced delirium |
| 5 | ICD-9 | `5119` | Unspecified pleural effusion |
| 6 | ICD-9 | `1122` | Candidiasis of other urogenital sites |
| 7 | ICD-9 | `5781` | Blood in stool |
| 8 | ICD-9 | `27669` | Other fluid overload |
| 9 | ICD-9 | `7102` | Sicca syndrome |
| 10 | ICD-9 | `E9393` | Other antipsychotics, neuroleptics, and major tranquilizers causing adverse effects in therapeutic use |
| 11 | ICD-9 | `2859` | Anemia, unspecified |
| 12 | ICD-9 | `73300` | Osteoporosis, unspecified |
| 13 | ICD-9 | `4019` | Unspecified essential hypertension |
| 14 | ICD-9 | `2449` | Unspecified acquired hypothyroidism |
| 15 | ICD-9 | `4240` | Mitral valve disorders |

## 5. ICU Stays

| Stay ID | First Care Unit | Last Care Unit | ICU Admit | ICU Discharge | LOS (days) |
|---|---|---|---|---|---|
| 34807493 | Medical Intensive Care Unit (MICU) | Medical Intensive Care Unit (MICU) | 2156-04-30 21:53:00 | 2156-05-02 22:27:20 | 2.02 |

## 6. Escalation / Severity Indicators

The following critical conditions or interventions were detected:

- **Non-Invasive Ventilation (NIV/BiPAP)** (ICU procedure event)
- **Respiratory Failure** (ICD diagnosis)

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2156-04-30 | ICD-9 | `9390` | Non-invasive mechanical ventilation |

### ICU Procedure Events (from `icu/procedureevents.csv.gz`)

- Non-invasive Ventilation (category: 2-Ventilation, started: 2156-04-30 22:54:00, status: FinishedRunning)
- PICC Line (category: Access Lines - Invasive, started: 2156-04-30 22:56:00, status: FinishedRunning)
- 20 Gauge (category: Access Lines - Peripheral, started: 2156-04-30 22:57:00, status: FinishedRunning)
- Urine Culture (category: 6-Cultures, started: 2156-05-01 12:30:00, status: FinishedRunning)
- 18 Gauge (category: Access Lines - Peripheral, started: 2156-05-01 12:52:00, status: FinishedRunning)

## 8. Critical Findings (Charted Events)

- **Ventilator Mode** (first noted: 2156-04-30 22:00:00)
- **Ventilator Type** (first noted: 2156-04-30 22:00:00)
- **Code Status** (first noted: 2156-04-30 22:57:00)

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2156-04-30 18:30:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2156-04-30 18:30:00 | Transfer | → Emergency Department (ED) |
| 2156-04-30 20:35:00 | Admission | Admitted from EMERGENCY ROOM (EW EMER.) |
| 2156-04-30 21:53:00 | ED Departure | Left Emergency Dept. |
| 2156-04-30 21:53:00 | ICU Admission | Medical Intensive Care Unit (MICU) (LOS: 2.0 days) |
| 2156-05-02 22:27:20 | Transfer | → Medicine (transfer) |
| 2156-05-02 22:36:13 | Transfer | → Medicine (transfer) |
| 2156-05-03 16:36:00 | Discharge | To CHRONIC/LONG TERM ACUTE CARE |

## 10. Missing / Ambiguous Data

- No obvious missing critical fields detected.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
