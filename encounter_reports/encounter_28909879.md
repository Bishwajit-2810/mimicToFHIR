# Encounter Report — HADM 28909879

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 28909879 |
| Subject ID | 10022041 |
| Patient Sex | M |
| Patient Anchor Age (at anchor year) | 64 |
| Anchor Year | 2187 |
| Admission Time | 2187-05-18 17:08:00 |
| Discharge Time | 2187-05-23 17:20:00 |
| Admission Type | EW EMER. |
| Admission Location | EMERGENCY ROOM |
| Discharge Location | HOME HEALTH CARE |
| Insurance | Medicare |
| Language | ENGLISH |
| Marital Status | MARRIED |
| Race/Ethnicity | OTHER |
| ED Registration | 2187-05-18 14:59:00 |
| ED Departure | 2187-05-18 18:39:00 |
| In-Hospital Mortality | No |
| Date of Death (overall) | N/A |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| APR | 951 | MODERATELY EXTENSIVE PROCEDURE UNRELATED TO PRINCIPAL DIAGNOSIS | 2.0 | 1.0 |
| HCFA | 981 | EXTENSIVE O.R. PROCEDURE UNRELATED TO PRINCIPAL DIAGNOSIS W MCC | N/A | N/A |

### Primary Diagnosis (seq_num = 1)

- **ICD-9 29181**: Alcohol withdrawal

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2187-05-18 17:09:18 | N/A | NMED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-9 `29181`: Alcohol withdrawal
- (seq 2) ICD-9 `3453`: Grand mal status
- (seq 3) ICD-9 `81201`: Closed fracture of surgical neck of humerus
- (seq 4) ICD-9 `4019`: Unspecified essential hypertension
- (seq 5) ICD-9 `2724`: Other and unspecified hyperlipidemia

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-9 | `29181` | Alcohol withdrawal |
| 2 | ICD-9 | `3453` | Grand mal status |
| 3 | ICD-9 | `81201` | Closed fracture of surgical neck of humerus |
| 4 | ICD-9 | `4019` | Unspecified essential hypertension |
| 5 | ICD-9 | `2724` | Other and unspecified hyperlipidemia |
| 6 | ICD-9 | `E8889` | Unspecified fall |
| 7 | ICD-9 | `6961` | Other psoriasis |
| 8 | ICD-9 | `7245` | Backache, unspecified |
| 9 | ICD-9 | `30390` | Other and unspecified alcohol dependence, unspecified |

## 5. ICU Stays

| Stay ID | First Care Unit | Last Care Unit | ICU Admit | ICU Discharge | LOS (days) |
|---|---|---|---|---|---|
| 30913302 | Surgical Intensive Care Unit (SICU) | Surgical Intensive Care Unit (SICU) | 2187-05-18 18:39:00 | 2187-05-20 16:04:02 | 1.89 |

## 6. Escalation / Severity Indicators

The following critical conditions or interventions were detected:

- **Invasive Mechanical Ventilation** (ICU procedure event)

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2187-05-20 | ICD-9 | `7931` | Open reduction of fracture with internal fixation, humerus |
| 2 | 2187-05-18 | ICD-9 | `9671` | Continuous invasive mechanical ventilation for less than 96 consecutive hours |

### ICU Procedure Events (from `icu/procedureevents.csv.gz`)

- Invasive Ventilation (category: 2-Ventilation, started: 2187-05-18 18:30:00, status: FinishedRunning)
- 18 Gauge (category: Access Lines - Peripheral, started: 2187-05-18 18:45:00, status: FinishedRunning)
- Nasal Swab (category: 6-Cultures, started: 2187-05-18 20:15:00, status: FinishedRunning)
- Urine Culture (category: 6-Cultures, started: 2187-05-18 21:00:00, status: FinishedRunning)
- EEG (category: 4-Procedures, started: 2187-05-18 21:30:00, status: FinishedRunning)
- Family updated by RN (category: 7-Communication, started: 2187-05-18 22:10:00, status: FinishedRunning)
- Magnetic Resonance Imaging (category: 5-Imaging, started: 2187-05-19 00:45:00, status: FinishedRunning)
- 20 Gauge (category: Access Lines - Peripheral, started: 2187-05-20 08:26:00, status: Stopped)
- OR Sent (category: 3-Significant Events, started: 2187-05-20 15:22:00, status: FinishedRunning)

## 8. Critical Findings (Charted Events)

- **Ventilator Tank #2** (first noted: 2187-05-18 20:00:00)
- **Ventilator Mode** (first noted: 2187-05-18 18:30:00)
- **Ventilator Tank #1** (first noted: 2187-05-18 20:00:00)
- **Seizure** (first noted: 2187-05-19 17:30:00)
- **Dialysis patient** (first noted: 2187-05-19 04:52:00)

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2187-05-18 14:59:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2187-05-18 14:59:00 | Transfer | → Emergency Department (ED) |
| 2187-05-18 17:08:00 | Admission | Admitted from EMERGENCY ROOM (EW EMER.) |
| 2187-05-18 18:39:00 | ED Departure | Left Emergency Dept. |
| 2187-05-18 18:39:00 | ICU Admission | Surgical Intensive Care Unit (SICU) (LOS: 1.9 days) |
| 2187-05-20 16:04:02 | Transfer | → PACU (transfer) |
| 2187-05-20 22:56:39 | Transfer | → Neurology (transfer) |
| 2187-05-23 17:20:00 | Discharge | To HOME HEALTH CARE |

## 10. Missing / Ambiguous Data

- No obvious missing critical fields detected.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
