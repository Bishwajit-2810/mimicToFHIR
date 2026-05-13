# Encounter Report — HADM 22168393

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 22168393 |
| Subject ID | 10008287 |
| Patient Sex | F |
| Patient Anchor Age (at anchor year) | 43 |
| Anchor Year | 2145 |
| Admission Time | 2145-09-28 01:17:00 |
| Discharge Time | 2145-10-02 13:35:00 |
| Admission Type | SURGICAL SAME DAY ADMISSION |
| Admission Location | PHYSICIAN REFERRAL |
| Discharge Location | HOME HEALTH CARE |
| Insurance | Other |
| Language | ENGLISH |
| Marital Status | SINGLE |
| Race/Ethnicity | WHITE |
| ED Registration | N/A |
| ED Departure | N/A |
| In-Hospital Mortality | No |
| Date of Death (overall) | N/A |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| APR | 21 | CRANIOTOMY EXCEPT FOR TRAUMA | 1.0 | 1.0 |
| HCFA | 27 | CRANIOTOMY & ENDOVASCULAR INTRACRANIAL PROCEDURES W/O CC/MCC | N/A | N/A |

### Primary Diagnosis (seq_num = 1)

- **ICD-10 D1802**: Hemangioma of intracranial structures

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2145-09-28 01:18:21 | N/A | NSURG |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-10 `D1802`: Hemangioma of intracranial structures
- (seq 2) ICD-10 `G40909`: Epilepsy, unspecified, not intractable, without status epilepticus
- (seq 3) ICD-10 `Z85850`: Personal history of malignant neoplasm of thyroid

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-10 | `D1802` | Hemangioma of intracranial structures |
| 2 | ICD-10 | `G40909` | Epilepsy, unspecified, not intractable, without status epilepticus |
| 3 | ICD-10 | `Z85850` | Personal history of malignant neoplasm of thyroid |

## 5. ICU Stays

| Stay ID | First Care Unit | Last Care Unit | ICU Admit | ICU Discharge | LOS (days) |
|---|---|---|---|---|---|
| 33348260 | Surgical Intensive Care Unit (SICU) | Surgical Intensive Care Unit (SICU) | 2145-09-28 20:59:43 | 2145-09-30 00:34:15 | 1.15 |

## 6. Escalation / Severity Indicators

The following critical conditions or interventions were detected:

- **Arterial Line** (ICU procedure event)

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2145-09-28 | ICD-10 | `00B60ZZ` | Excision of Cerebral Ventricle, Open Approach |

### ICU Procedure Events (from `icu/procedureevents.csv.gz`)

- Arterial Line (category: Access Lines - Invasive, started: 2145-09-28 21:22:00, status: FinishedRunning)
- 18 Gauge (category: Access Lines - Peripheral, started: 2145-09-28 21:23:00, status: FinishedRunning)
- Foley Catheter (category: GI/GU, started: 2145-09-28 21:23:00, status: FinishedRunning)
- CT scan (category: 5-Imaging, started: 2145-09-29 23:00:00, status: FinishedRunning)

## 8. Critical Findings (Charted Events)

- **Dialysis patient** (first noted: 2145-09-28 21:24:00)

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2145-09-28 01:17:00 | Admission | Admitted from PHYSICIAN REFERRAL (SURGICAL SAME DAY ADMISSION) |
| 2145-09-28 20:59:43 | ICU Admission | Surgical Intensive Care Unit (SICU) (LOS: 1.1 days) |
| 2145-09-28 20:59:43 | Transfer | → Surgical Intensive Care Unit (SICU) (transfer) |
| 2145-09-30 00:34:15 | Transfer | → Neurology (transfer) |
| 2145-09-30 17:10:15 | Transfer | → Neurology (transfer) |
| 2145-10-02 13:35:00 | Discharge | To HOME HEALTH CARE |

## 10. Missing / Ambiguous Data

- No ED registration time — admission may not have gone through ED.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
