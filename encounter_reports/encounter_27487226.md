# Encounter Report — HADM 27487226

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 27487226 |
| Subject ID | 10014354 |
| Patient Sex | M |
| Patient Anchor Age (at anchor year) | 60 |
| Anchor Year | 2146 |
| Admission Time | 2148-06-30 01:09:00 |
| Discharge Time | 2148-07-13 19:35:00 |
| Admission Type | URGENT |
| Admission Location | TRANSFER FROM HOSPITAL |
| Discharge Location | HOME HEALTH CARE |
| Insurance | Other |
| Language | ENGLISH |
| Marital Status | SINGLE |
| Race/Ethnicity | WHITE |
| ED Registration | 2148-06-29 21:06:00 |
| ED Departure | 2148-06-30 02:27:00 |
| In-Hospital Mortality | No |
| Date of Death (overall) | N/A |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| APR | 139 | OTHER PNEUMONIA | 4.0 | 4.0 |
| HCFA | 193 | SIMPLE PNEUMONIA & PLEURISY W MCC | N/A | N/A |

### Primary Diagnosis (seq_num = 1)

- **ICD-10 J189**: Pneumonia, unspecified organism

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2148-06-30 01:09:34 | N/A | MED |
| 2148-07-01 21:00:50 | MED | OMED |
| 2148-07-04 20:19:52 | OMED | MED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-10 `J189`: Pneumonia, unspecified organism
- (seq 2) ICD-10 `R570`: Cardiogenic shock
- (seq 3) ICD-10 `I314`: Cardiac tamponade
- (seq 4) ICD-10 `I5033`: Acute on chronic diastolic (congestive) heart failure
- (seq 5) ICD-10 `N179`: Acute kidney failure, unspecified

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-10 | `J189` | Pneumonia, unspecified organism |
| 2 | ICD-10 | `R570` | Cardiogenic shock |
| 3 | ICD-10 | `I314` | Cardiac tamponade |
| 4 | ICD-10 | `I5033` | Acute on chronic diastolic (congestive) heart failure |
| 5 | ICD-10 | `N179` | Acute kidney failure, unspecified |
| 6 | ICD-10 | `I480` | Paroxysmal atrial fibrillation |
| 7 | ICD-10 | `C9110` | Chronic lymphocytic leukemia of B-cell type not having achieved remission |
| 8 | ICD-10 | `I4892` | Unspecified atrial flutter |
| 9 | ICD-10 | `E871` | Hypo-osmolality and hyponatremia |
| 10 | ICD-10 | `I313` | Pericardial effusion (noninflammatory) |
| 11 | ICD-10 | `E11649` | Type 2 diabetes mellitus with hypoglycemia without coma |
| 12 | ICD-10 | `E1142` | Type 2 diabetes mellitus with diabetic polyneuropathy |
| 13 | ICD-10 | `G4733` | Obstructive sleep apnea (adult) (pediatric) |
| 14 | ICD-10 | `I2510` | Atherosclerotic heart disease of native coronary artery without angina pectoris |
| 15 | ICD-10 | `Z955` | Presence of coronary angioplasty implant and graft |
| 16 | ICD-10 | `F259` | Schizoaffective disorder, unspecified |
| 17 | ICD-10 | `Z950` | Presence of cardiac pacemaker |
| 18 | ICD-10 | `Z8547` | Personal history of malignant neoplasm of testis |
| 19 | ICD-10 | `Z8673` | Personal history of transient ischemic attack (TIA), and cerebral infarction without residual deficits |
| 20 | ICD-10 | `Z9884` | Bariatric surgery status |
| 21 | ICD-10 | `E785` | Hyperlipidemia, unspecified |
| 22 | ICD-10 | `E039` | Hypothyroidism, unspecified |
| 23 | ICD-10 | `R740` | Nonspecific elevation of levels of transaminase and lactic acid dehydrogenase [LDH] |
| 24 | ICD-10 | `M940` | Chondrocostal junction syndrome [Tietze] |

## 5. ICU Stays

| Stay ID | First Care Unit | Last Care Unit | ICU Admit | ICU Discharge | LOS (days) |
|---|---|---|---|---|---|
| 34600477 | Medical/Surgical Intensive Care Unit (MICU/SICU) | Medical/Surgical Intensive Care Unit (MICU/SICU) | 2148-06-30 02:27:00 | 2148-07-01 20:58:50 | 1.77 |
| 38017367 | Neuro Surgical Intensive Care Unit (Neuro SICU) | Coronary Care Unit (CCU) | 2148-07-07 15:48:09 | 2148-07-10 18:25:51 | 3.11 |

## 6. Escalation / Severity Indicators

The following critical conditions or interventions were detected:

- **Acute Kidney Injury** (ICD diagnosis)
- **Pneumonia** (ICD diagnosis)
- **Shock** (ICD diagnosis)

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2148-07-07 | ICD-10 | `0W9D30Z` | Drainage of Pericardial Cavity with Drainage Device, Percutaneous Approach |

### ICU Procedure Events (from `icu/procedureevents.csv.gz`)

- 20 Gauge (category: Access Lines - Peripheral, started: 2148-06-30 03:00:00, status: FinishedRunning)
- Indwelling Port (category: Access Lines - Invasive, started: 2148-06-30 03:38:00, status: FinishedRunning)
- EKG (category: 4-Procedures, started: 2148-06-30 07:36:00, status: FinishedRunning)

## 8. Critical Findings (Charted Events)

- **Dialysis patient** (first noted: 2148-06-30 02:56:00)

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2148-06-29 21:06:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2148-06-29 21:06:00 | Transfer | → Emergency Department (ED) |
| 2148-06-30 01:09:00 | Admission | Admitted from TRANSFER FROM HOSPITAL (URGENT) |
| 2148-06-30 02:27:00 | ED Departure | Left Emergency Dept. |
| 2148-06-30 02:27:00 | ICU Admission | Medical/Surgical Intensive Care Unit (MICU/SICU) (LOS: 1.8 days) |
| 2148-07-01 20:58:50 | Transfer | → Hematology/Oncology Intermediate (transfer) |
| 2148-07-04 20:19:22 | Transfer | → Medicine/Cardiology (transfer) |
| 2148-07-07 15:48:09 | ICU Admission | Neuro Surgical Intensive Care Unit (Neuro SICU) (LOS: 3.1 days) |
| 2148-07-07 15:48:09 | Transfer | → Neuro Surgical Intensive Care Unit (Neuro SICU) (transfer) |
| 2148-07-07 21:44:48 | Transfer | → Coronary Care Unit (CCU) (transfer) |
| 2148-07-10 18:25:51 | Transfer | → Medicine/Cardiology (transfer) |
| 2148-07-13 19:35:00 | Discharge | To HOME HEALTH CARE |

## 10. Missing / Ambiguous Data

- No obvious missing critical fields detected.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
