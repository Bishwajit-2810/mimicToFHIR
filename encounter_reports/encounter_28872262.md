# Encounter Report — HADM 28872262

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 28872262 |
| Subject ID | 10023117 |
| Patient Sex | M |
| Patient Anchor Age (at anchor year) | 53 |
| Anchor Year | 2170 |
| Admission Time | 2171-11-07 21:37:00 |
| Discharge Time | 2171-11-22 15:30:00 |
| Admission Type | EW EMER. |
| Admission Location | EMERGENCY ROOM |
| Discharge Location | HOME HEALTH CARE |
| Insurance | Medicare |
| Language | ENGLISH |
| Marital Status | WIDOWED |
| Race/Ethnicity | WHITE |
| ED Registration | 2171-11-07 17:40:00 |
| ED Departure | 2171-11-07 22:50:00 |
| In-Hospital Mortality | No |
| Date of Death (overall) | 2175-07-20 |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| HCFA | 261 | CARDIAC PACEMAKER REVISION EXCEPT DEVICE REPLACEMENT W CC | N/A | N/A |
| APR | 177 | CARDIAC PACEMAKER & DEFIBRILLATOR REVISION EXCEPT DEVICE REPLACEMENT | 3.0 | 3.0 |

### Primary Diagnosis (seq_num = 1)

- **ICD-9 42823**: Acute on chronic systolic heart failure

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2171-11-07 21:37:36 | N/A | CMED |
| 2171-11-14 10:06:54 | CMED | CSURG |
| 2171-11-15 13:53:10 | CSURG | CMED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-9 `42823`: Acute on chronic systolic heart failure
- (seq 2) ICD-9 `5849`: Acute kidney failure, unspecified
- (seq 3) ICD-9 `4589`: Hypotension, unspecified
- (seq 4) ICD-9 `4259`: Secondary cardiomyopathy, unspecified
- (seq 5) ICD-9 `2761`: Hyposmolality and/or hyponatremia

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-9 | `42823` | Acute on chronic systolic heart failure |
| 2 | ICD-9 | `5849` | Acute kidney failure, unspecified |
| 3 | ICD-9 | `4589` | Hypotension, unspecified |
| 4 | ICD-9 | `4259` | Secondary cardiomyopathy, unspecified |
| 5 | ICD-9 | `2761` | Hyposmolality and/or hyponatremia |
| 6 | ICD-9 | `53085` | Barrett's esophagus |
| 7 | ICD-9 | `29532` | Paranoid type schizophrenia, chronic |
| 8 | ICD-9 | `5180` | Pulmonary collapse |
| 9 | ICD-9 | `9961` | Mechanical complication of other vascular device, implant, and graft |
| 10 | ICD-9 | `4280` | Congestive heart failure, unspecified |
| 11 | ICD-9 | `V4502` | Automatic implantable cardiac defibrillator in situ |
| 12 | ICD-9 | `4263` | Other left bundle branch block |
| 13 | ICD-9 | `2724` | Other and unspecified hyperlipidemia |
| 14 | ICD-9 | `V1052` | Personal history of malignant neoplasm of kidney |
| 15 | ICD-9 | `53081` | Esophageal reflux |
| 16 | ICD-9 | `V1582` | Personal history of tobacco use |
| 17 | ICD-9 | `5859` | Chronic kidney disease, unspecified |
| 18 | ICD-9 | `40390` | Hypertensive chronic kidney disease, unspecified, with chronic kidney disease stage I through stage IV, or unspecified |
| 19 | ICD-9 | `30000` | Anxiety state, unspecified |
| 20 | ICD-9 | `27800` | Obesity, unspecified |
| 21 | ICD-9 | `V8532` | Body Mass Index 32.0-32.9, adult |
| 22 | ICD-9 | `E8781` | Surgical operation with implant of artificial internal device causing abnormal patient reaction, or later complication,without mention of misadventure at time of operation |
| 23 | ICD-9 | `E8490` | Home accidents |
| 24 | ICD-9 | `E8768` | Other specified misadventures during medical care |
| 25 | ICD-9 | `E8497` | Accidents occurring in residential institution |

## 5. ICU Stays

| Stay ID | First Care Unit | Last Care Unit | ICU Admit | ICU Discharge | LOS (days) |
|---|---|---|---|---|---|
| 30057454 | Cardiac Vascular Intensive Care Unit (CVICU) | Coronary Care Unit (CCU) | 2171-11-14 10:06:41 | 2171-11-18 20:49:43 | 4.45 |

## 6. Escalation / Severity Indicators

The following critical conditions or interventions were detected:

- **Acute Kidney Injury** (ICD diagnosis)
- **Arterial Line** (ICU procedure event)

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2171-11-14 | ICD-9 | `3774` | Insertion or replacement of epicardial lead [electrode] into epicardium |
| 2 | 2171-11-11 | ICD-9 | `3721` | Right heart cardiac catheterization |
| 3 | 2171-11-12 | ICD-9 | `3897` | Central venous catheter placement with guidance |
| 4 | 2171-11-15 | ICD-9 | `3893` | Venous catheterization, not elsewhere classified |
| 5 | 2171-11-16 | ICD-9 | `3891` | Arterial catheterization |
| 6 | 2171-11-15 | ICD-9 | `8949` | Automatic implantable cardioverter/defibrillator (AICD) check |

### ICU Procedure Events (from `icu/procedureevents.csv.gz`)

- Multi Lumen (category: Access Lines - Invasive, started: 2171-11-14 11:29:00, status: FinishedRunning)
- PICC Line (category: Access Lines - Invasive, started: 2171-11-14 11:29:00, status: FinishedRunning)
- 20 Gauge (category: Access Lines - Peripheral, started: 2171-11-14 11:34:00, status: FinishedRunning)
- Transthoracic Echo (category: 5-Imaging, started: 2171-11-15 10:07:00, status: FinishedRunning)
- Family updated by RN (category: 7-Communication, started: 2171-11-16 10:58:00, status: FinishedRunning)
- Arterial Line (category: Access Lines - Invasive, started: 2171-11-16 14:45:00, status: FinishedRunning)
- Sputum Culture (category: 6-Cultures, started: 2171-11-16 18:56:00, status: FinishedRunning)

## 8. Critical Findings (Charted Events)

- **Code Status** (first noted: 2171-11-14 10:08:00)

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2171-11-07 17:40:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2171-11-07 17:40:00 | Transfer | → Emergency Department (ED) |
| 2171-11-07 21:37:00 | Admission | Admitted from EMERGENCY ROOM (EW EMER.) |
| 2171-11-07 22:50:00 | ED Departure | Left Emergency Dept. |
| 2171-11-09 19:28:16 | Transfer | → Medicine/Cardiology (transfer) |
| 2171-11-14 10:06:41 | ICU Admission | Cardiac Vascular Intensive Care Unit (CVICU) (LOS: 4.4 days) |
| 2171-11-14 10:06:41 | Transfer | → Cardiac Vascular Intensive Care Unit (CVICU) (transfer) |
| 2171-11-15 13:53:00 | Transfer | → Coronary Care Unit (CCU) (transfer) |
| 2171-11-18 20:49:43 | Transfer | → Medicine/Cardiology (transfer) |
| 2171-11-22 15:30:00 | Discharge | To HOME HEALTH CARE |

## 10. Missing / Ambiguous Data

- No obvious missing critical fields detected.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
