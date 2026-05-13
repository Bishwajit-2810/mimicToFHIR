# Encounter Report — HADM 24470193

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 24470193 |
| Subject ID | 10025463 |
| Patient Sex | M |
| Patient Anchor Age (at anchor year) | 66 |
| Anchor Year | 2136 |
| Admission Time | 2137-10-08 21:20:00 |
| Discharge Time | 2137-10-09 15:30:00 |
| Admission Type | EW EMER. |
| Admission Location | EMERGENCY ROOM |
| Discharge Location | DIED |
| Insurance | Other |
| Language | ENGLISH |
| Marital Status | MARRIED |
| Race/Ethnicity | WHITE |
| ED Registration | 2137-10-08 18:16:00 |
| ED Departure | 2137-10-08 20:44:00 |
| In-Hospital Mortality | YES — Death time: 2137-10-09 15:30:00 |
| Date of Death (overall) | 2137-10-09 |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| APR | 21 | CRANIOTOMY EXCEPT FOR TRAUMA | 2.0 | 3.0 |
| HCFA | 24 | CRANIO W MAJOR DEV IMPL/ACUTE COMPLEX CNS PDX W/O MCC | N/A | N/A |

### Primary Diagnosis (seq_num = 1)

- **ICD-9 431**: Intracerebral hemorrhage

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2137-10-08 21:20:50 | N/A | NSURG |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-9 `431`: Intracerebral hemorrhage
- (seq 2) ICD-9 `3314`: Obstructive hydrocephalus
- (seq 3) ICD-9 `42731`: Atrial fibrillation
- (seq 4) ICD-9 `V4987`: Physical restraints status
- (seq 5) ICD-9 `4019`: Unspecified essential hypertension

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-9 | `431` | Intracerebral hemorrhage |
| 2 | ICD-9 | `3314` | Obstructive hydrocephalus |
| 3 | ICD-9 | `42731` | Atrial fibrillation |
| 4 | ICD-9 | `V4987` | Physical restraints status |
| 5 | ICD-9 | `4019` | Unspecified essential hypertension |
| 6 | ICD-9 | `2724` | Other and unspecified hyperlipidemia |
| 7 | ICD-9 | `V5861` | Long-term (current) use of anticoagulants |
| 8 | ICD-9 | `V4986` | Do not resuscitate status |
| 9 | ICD-9 | `V1582` | Personal history of tobacco use |
| 10 | ICD-9 | `4558` | Unspecified hemorrhoids with other complication |

## 5. ICU Stays

| Stay ID | First Care Unit | Last Care Unit | ICU Admit | ICU Discharge | LOS (days) |
|---|---|---|---|---|---|
| 38275267 | Surgical Intensive Care Unit (SICU) | Surgical Intensive Care Unit (SICU) | 2137-10-09 02:51:25 | 2137-10-09 17:32:37 | 0.61 |

## 6. Escalation / Severity Indicators

The following critical conditions or interventions were detected:

- **Invasive Mechanical Ventilation** (ICU procedure event)

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2137-10-08 | ICD-9 | `0221` | Insertion or replacement of external ventricular drain [EVD] |
| 2 | 2137-10-08 | ICD-9 | `9671` | Continuous invasive mechanical ventilation for less than 96 consecutive hours |
| 3 | 2137-10-08 | ICD-9 | `0096` | Infusion of 4-Factor Prothrombin Complex Concentrate |
| 4 | 2137-10-09 | ICD-9 | `3893` | Venous catheterization, not elsewhere classified |

### ICU Procedure Events (from `icu/procedureevents.csv.gz`)

- 16 Gauge (category: Access Lines - Peripheral, started: 2137-10-09 03:00:00, status: FinishedRunning)
- 18 Gauge (category: Access Lines - Peripheral, started: 2137-10-09 03:00:00, status: FinishedRunning)
- Invasive Ventilation (category: 2-Ventilation, started: 2137-10-09 03:20:00, status: FinishedRunning)
- Multi Lumen (category: Access Lines - Invasive, started: 2137-10-09 07:50:00, status: Stopped)
- NEOB notified (category: 7-Communication, started: 2137-10-09 08:24:00, status: FinishedRunning)
- Family met with Social Worker (category: 7-Communication, started: 2137-10-09 09:00:00, status: FinishedRunning)
- Family updated by MD (category: 7-Communication, started: 2137-10-09 10:13:00, status: FinishedRunning)
- Extubation (category: 1-Intubation/Extubation, started: 2137-10-09 15:20:00, status: FinishedRunning)

## 8. Critical Findings (Charted Events)

- **Ventilator Type** (first noted: 2137-10-09 03:00:00)
- **Ventilator Mode** (first noted: 2137-10-09 03:00:00)
- **Ventilator Tank #1** (first noted: 2137-10-09 05:00:00)

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2137-10-08 18:16:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2137-10-08 18:16:00 | Transfer | → Emergency Department (ED) |
| 2137-10-08 20:44:00 | ED Departure | Left Emergency Dept. |
| 2137-10-08 21:20:00 | Admission | Admitted from EMERGENCY ROOM (EW EMER.) |
| 2137-10-09 02:51:25 | ICU Admission | Surgical Intensive Care Unit (SICU) (LOS: 0.6 days) |
| 2137-10-09 02:51:25 | Transfer | → Surgical Intensive Care Unit (SICU) (transfer) |
| 2137-10-09 15:30:00 | **IN-HOSPITAL DEATH** | |
| 2137-10-09 15:30:00 | Discharge | To DIED |

## 10. Missing / Ambiguous Data

- No obvious missing critical fields detected.

## 11. Manual Review Recommendation

**This encounter is flagged for manual review:**

- Patient expired in-hospital but cause of death not clearly coded.
