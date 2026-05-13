# Encounter Report — HADM 20611640

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 20611640 |
| Subject ID | 10032725 |
| Patient Sex | F |
| Patient Anchor Age (at anchor year) | 38 |
| Anchor Year | 2143 |
| Admission Time | 2143-03-22 04:59:00 |
| Discharge Time | 2143-03-25 13:00:00 |
| Admission Type | EW EMER. |
| Admission Location | EMERGENCY ROOM |
| Discharge Location | HOSPICE |
| Insurance | Other |
| Language | ENGLISH |
| Marital Status | SINGLE |
| Race/Ethnicity | BLACK/AFRICAN AMERICAN |
| ED Registration | 2143-03-22 01:19:00 |
| ED Departure | 2143-03-22 06:42:00 |
| In-Hospital Mortality | No |
| Date of Death (overall) | 2143-03-30 |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| HCFA | 54 | NERVOUS SYSTEM NEOPLASMS W MCC | N/A | N/A |
| APR | 41 | NERVOUS SYSTEM MALIGNANCY | 4.0 | 4.0 |

### Primary Diagnosis (seq_num = 1)

- **ICD-9 1983**: Secondary malignant neoplasm of brain and spinal cord

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2143-03-22 05:00:23 | N/A | MED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-9 `1983`: Secondary malignant neoplasm of brain and spinal cord
- (seq 2) ICD-9 `431`: Intracerebral hemorrhage
- (seq 3) ICD-9 `3485`: Cerebral edema
- (seq 4) ICD-9 `43820`: Late effects of cerebrovascular disease, hemiplegia affecting unspecified side
- (seq 5) ICD-9 `1970`: Secondary malignant neoplasm of lung

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-9 | `1983` | Secondary malignant neoplasm of brain and spinal cord |
| 2 | ICD-9 | `431` | Intracerebral hemorrhage |
| 3 | ICD-9 | `3485` | Cerebral edema |
| 4 | ICD-9 | `43820` | Late effects of cerebrovascular disease, hemiplegia affecting unspecified side |
| 5 | ICD-9 | `1970` | Secondary malignant neoplasm of lung |
| 6 | ICD-9 | `1987` | Secondary malignant neoplasm of adrenal gland |
| 7 | ICD-9 | `1968` | Secondary and unspecified malignant neoplasm of lymph nodes of multiple sites |
| 8 | ICD-9 | `70703` | Pressure ulcer, lower back |
| 9 | ICD-9 | `70722` | Pressure ulcer, stage II |
| 10 | ICD-9 | `25000` | Diabetes mellitus without mention of complication, type II or unspecified type, not stated as uncontrolled |
| 11 | ICD-9 | `2720` | Pure hypercholesterolemia |
| 12 | ICD-9 | `4019` | Unspecified essential hypertension |
| 13 | ICD-9 | `V667` | Encounter for palliative care |
| 14 | ICD-9 | `V1042` | Personal history of malignant neoplasm of other parts of uterus |

## 5. ICU Stays

| Stay ID | First Care Unit | Last Care Unit | ICU Admit | ICU Discharge | LOS (days) |
|---|---|---|---|---|---|
| 30101877 | Medical/Surgical Intensive Care Unit (MICU/SICU) | Medical/Surgical Intensive Care Unit (MICU/SICU) | 2143-03-22 06:42:00 | 2143-03-25 15:05:33 | 3.35 |

## 6. Escalation / Severity Indicators

The following critical conditions or interventions were detected:

- **Endotracheal Intubation** (ICU procedure event)
- **Invasive Mechanical Ventilation** (ICU procedure event)

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2143-03-22 | ICD-9 | `9671` | Continuous invasive mechanical ventilation for less than 96 consecutive hours |
| 2 | 2143-03-22 | ICD-9 | `9604` | Insertion of endotracheal tube |
| 3 | 2143-03-23 | ICD-9 | `3893` | Venous catheterization, not elsewhere classified |

### ICU Procedure Events (from `icu/procedureevents.csv.gz`)

- 18 Gauge (category: Access Lines - Peripheral, started: 2143-03-22 08:33:00, status: Stopped)
- Invasive Ventilation (category: 2-Ventilation, started: 2143-03-22 09:45:00, status: FinishedRunning)
- Intubation (category: 1-Intubation/Extubation, started: 2143-03-22 09:48:00, status: FinishedRunning)
- Extubation (category: 1-Intubation/Extubation, started: 2143-03-22 19:40:00, status: FinishedRunning)
- 20 Gauge (category: Access Lines - Peripheral, started: 2143-03-23 00:00:00, status: FinishedRunning)
- Midline (category: Access Lines - Invasive, started: 2143-03-23 18:27:00, status: Stopped)

## 8. Critical Findings (Charted Events)

- **Ventilator Tank #1** (first noted: 2143-03-22 10:00:00)
- **Ventilator Mode** (first noted: 2143-03-22 10:00:00)
- **Ventilator Type** (first noted: 2143-03-22 10:00:00)
- **Known difficult intubation** (first noted: 2143-03-22 10:00:00)
- **Dialysis patient** (first noted: 2143-03-22 17:05:00)

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2143-03-22 01:19:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2143-03-22 01:19:00 | Transfer | → Emergency Department (ED) |
| 2143-03-22 04:59:00 | Admission | Admitted from EMERGENCY ROOM (EW EMER.) |
| 2143-03-22 06:42:00 | ED Departure | Left Emergency Dept. |
| 2143-03-22 06:42:00 | ICU Admission | Medical/Surgical Intensive Care Unit (MICU/SICU) (LOS: 3.3 days) |
| 2143-03-25 13:00:00 | Discharge | To HOSPICE |

## 10. Missing / Ambiguous Data

- No obvious missing critical fields detected.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
