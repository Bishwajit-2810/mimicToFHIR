# Encounter Report — HADM 24597018

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 24597018 |
| Subject ID | 10001217 |
| Patient Sex | F |
| Patient Anchor Age (at anchor year) | 55 |
| Anchor Year | 2157 |
| Admission Time | 2157-11-18 22:56:00 |
| Discharge Time | 2157-11-25 18:00:00 |
| Admission Type | EW EMER. |
| Admission Location | EMERGENCY ROOM |
| Discharge Location | HOME HEALTH CARE |
| Insurance | Other |
| Language | ? |
| Marital Status | MARRIED |
| Race/Ethnicity | WHITE |
| ED Registration | 2157-11-18 17:38:00 |
| ED Departure | 2157-11-19 01:24:00 |
| In-Hospital Mortality | No |
| Date of Death (overall) | N/A |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| APR | 21 | CRANIOTOMY EXCEPT FOR TRAUMA | 3.0 | 4.0 |
| HCFA | 23 | CRANIO W MAJOR DEV IMPL/ACUTE COMPLEX CNS PDX W MCC OR CHEMO IMPLANT | N/A | N/A |

### Primary Diagnosis (seq_num = 1)

- **ICD-9 3240**: Intracranial abscess

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2157-11-18 22:57:43 | N/A | NMED |
| 2157-11-19 00:36:42 | NMED | NSURG |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-9 `3240`: Intracranial abscess
- (seq 2) ICD-9 `3484`: Compression of brain
- (seq 3) ICD-9 `3485`: Cerebral edema
- (seq 4) ICD-9 `5180`: Pulmonary collapse
- (seq 5) ICD-9 `340`: Multiple sclerosis

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-9 | `3240` | Intracranial abscess |
| 2 | ICD-9 | `3484` | Compression of brain |
| 3 | ICD-9 | `3485` | Cerebral edema |
| 4 | ICD-9 | `5180` | Pulmonary collapse |
| 5 | ICD-9 | `340` | Multiple sclerosis |
| 6 | ICD-9 | `04109` | Streptococcus infection in conditions classified elsewhere and of unspecified site, other streptococcus |
| 7 | ICD-9 | `3051` | Tobacco use disorder |
| 8 | ICD-9 | `4019` | Unspecified essential hypertension |
| 9 | ICD-9 | `V168` | Family history of other specified malignant neoplasm |
| 10 | ICD-9 | `V161` | Family history of malignant neoplasm of trachea, bronchus, and lung |

## 5. ICU Stays

| Stay ID | First Care Unit | Last Care Unit | ICU Admit | ICU Discharge | LOS (days) |
|---|---|---|---|---|---|
| 37067082 | Surgical Intensive Care Unit (SICU) | Surgical Intensive Care Unit (SICU) | 2157-11-20 19:18:02 | 2157-11-21 22:08:00 | 1.12 |

## 6. Escalation / Severity Indicators

_No escalation indicators detected from ICD codes or ICU procedure events._

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2157-11-20 | ICD-9 | `0139` | Other incision of brain |
| 2 | 2157-11-19 | ICD-9 | `0331` | Spinal tap |
| 3 | 2157-11-22 | ICD-9 | `3897` | Central venous catheter placement with guidance |

### ICU Procedure Events (from `icu/procedureevents.csv.gz`)

- CT scan (category: 5-Imaging, started: 2157-11-21 14:00:00, status: FinishedRunning)
- 22 Gauge (category: Access Lines - Peripheral, started: 2157-11-21 20:30:00, status: Stopped)
- Family updated by RN (category: 7-Communication, started: 2157-11-21 20:30:00, status: FinishedRunning)

## 8. Critical Findings (Charted Events)

_No critical chart events detected._

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2157-11-18 17:38:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2157-11-18 17:38:00 | Transfer | → Emergency Department (ED) |
| 2157-11-18 22:56:00 | Admission | Admitted from EMERGENCY ROOM (EW EMER.) |
| 2157-11-19 01:24:00 | ED Departure | Left Emergency Dept. |
| 2157-11-20 19:18:02 | ICU Admission | Surgical Intensive Care Unit (SICU) (LOS: 1.1 days) |
| 2157-11-20 19:18:02 | Transfer | → Surgical Intensive Care Unit (SICU) (transfer) |
| 2157-11-21 22:08:00 | Transfer | → Neurology (transfer) |
| 2157-11-24 15:32:32 | Transfer | → Neurology (transfer) |
| 2157-11-25 18:00:00 | Discharge | To HOME HEALTH CARE |

## 10. Missing / Ambiguous Data

- No obvious missing critical fields detected.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
