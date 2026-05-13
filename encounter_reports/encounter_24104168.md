# Encounter Report — HADM 24104168

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 24104168 |
| Subject ID | 10020187 |
| Patient Sex | F |
| Patient Anchor Age (at anchor year) | 63 |
| Anchor Year | 2169 |
| Admission Time | 2169-01-15 04:04:00 |
| Discharge Time | 2169-01-24 17:20:00 |
| Admission Type | OBSERVATION ADMIT |
| Admission Location | EMERGENCY ROOM |
| Discharge Location | HOME HEALTH CARE |
| Insurance | Other |
| Language | ? |
| Marital Status | MARRIED |
| Race/Ethnicity | HISPANIC/LATINO - SALVADORAN |
| ED Registration | 2169-01-14 23:26:00 |
| ED Departure | 2169-01-15 04:56:00 |
| In-Hospital Mortality | No |
| Date of Death (overall) | N/A |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| HCFA | 22 | INTRACRANIAL VASCULAR PROCEDURES W PDX HEMORRHAGE W/O CC/MCC | N/A | N/A |
| APR | 24 | EXTRACRANIAL VASCULAR PROCEDURES | 1.0 | 1.0 |

### Primary Diagnosis (seq_num = 1)

- **ICD-10 I6032**: Nontraumatic subarachnoid hemorrhage from left posterior communicating artery

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2169-01-15 04:04:33 | N/A | NSURG |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-10 `I6032`: Nontraumatic subarachnoid hemorrhage from left posterior communicating artery
- (seq 2) ICD-10 `I10`: Essential (primary) hypertension
- (seq 3) ICD-10 `E785`: Hyperlipidemia, unspecified
- (seq 4) ICD-10 `I2510`: Atherosclerotic heart disease of native coronary artery without angina pectoris
- (seq 5) ICD-10 `E780`: Pure hypercholesterolemia

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-10 | `I6032` | Nontraumatic subarachnoid hemorrhage from left posterior communicating artery |
| 2 | ICD-10 | `I10` | Essential (primary) hypertension |
| 3 | ICD-10 | `E785` | Hyperlipidemia, unspecified |
| 4 | ICD-10 | `I2510` | Atherosclerotic heart disease of native coronary artery without angina pectoris |
| 5 | ICD-10 | `E780` | Pure hypercholesterolemia |

## 5. ICU Stays

| Stay ID | First Care Unit | Last Care Unit | ICU Admit | ICU Discharge | LOS (days) |
|---|---|---|---|---|---|
| 37509585 | Neuro Surgical Intensive Care Unit (Neuro SICU) | Neuro Stepdown | 2169-01-15 04:56:00 | 2169-01-20 15:47:50 | 5.45 |

## 6. Escalation / Severity Indicators

The following critical conditions or interventions were detected:

- **Arterial Line** (ICU procedure event)

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2169-01-20 | ICD-10 | `03VG3DZ` | Restriction of Intracranial Artery with Intraluminal Device, Percutaneous Approach |

### ICU Procedure Events (from `icu/procedureevents.csv.gz`)

- 20 Gauge (category: Access Lines - Peripheral, started: 2169-01-15 05:20:00, status: FinishedRunning)
- Trans Esophageal Echo (category: 5-Imaging, started: 2169-01-15 11:28:00, status: FinishedRunning)
- Foley Catheter (category: GI/GU, started: 2169-01-15 12:00:00, status: FinishedRunning)
- Angiography (category: 5-Imaging, started: 2169-01-15 12:10:00, status: FinishedRunning)
- Arterial Line (category: Access Lines - Invasive, started: 2169-01-15 12:45:00, status: FinishedRunning)
- Sheath (Venous) (category: Access Lines - Invasive, started: 2169-01-15 14:19:00, status: FinishedRunning)
- Transcranial Doppler (category: 5-Imaging, started: 2169-01-17 10:18:00, status: FinishedRunning)
- 22 Gauge (category: Access Lines - Peripheral, started: 2169-01-18 12:00:00, status: FinishedRunning)

## 8. Critical Findings (Charted Events)

- **Dialysis patient** (first noted: 2169-01-15 05:51:00)

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2169-01-14 23:26:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2169-01-14 23:26:00 | Transfer | → Emergency Department (ED) |
| 2169-01-15 04:04:00 | Admission | Admitted from EMERGENCY ROOM (OBSERVATION ADMIT) |
| 2169-01-15 04:56:00 | ED Departure | Left Emergency Dept. |
| 2169-01-15 04:56:00 | ICU Admission | Neuro Surgical Intensive Care Unit (Neuro SICU) (LOS: 5.5 days) |
| 2169-01-17 15:38:12 | Transfer | → Neuro Stepdown (transfer) |
| 2169-01-20 15:47:50 | Transfer | → Neurology (transfer) |
| 2169-01-24 17:20:00 | Discharge | To HOME HEALTH CARE |

## 10. Missing / Ambiguous Data

- No obvious missing critical fields detected.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
