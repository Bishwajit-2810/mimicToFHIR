# Encounter Report — HADM 26924951

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 26924951 |
| Subject ID | 10039831 |
| Patient Sex | F |
| Patient Anchor Age (at anchor year) | 57 |
| Anchor Year | 2115 |
| Admission Time | 2115-12-28 07:15:00 |
| Discharge Time | 2116-01-02 14:34:00 |
| Admission Type | SURGICAL SAME DAY ADMISSION |
| Admission Location | PHYSICIAN REFERRAL |
| Discharge Location | HOME HEALTH CARE |
| Insurance | Other |
| Language | ENGLISH |
| Marital Status | MARRIED |
| Race/Ethnicity | UNABLE TO OBTAIN |
| ED Registration | N/A |
| ED Departure | N/A |
| In-Hospital Mortality | No |
| Date of Death (overall) | N/A |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| HCFA | 821 | LYMPHOMA & LEUKEMIA W MAJOR O.R. PROCEDURE W CC | N/A | N/A |
| APR | 680 | MAJOR O.R. PROCEDURES FOR LYMPHATIC/HEMATOPOIETIC/OTHER NEOPLASMS | 2.0 | 1.0 |

### Primary Diagnosis (seq_num = 1)

- **ICD-9 1962**: Secondary and unspecified malignant neoplasm of intra-abdominal lymph nodes

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2115-12-28 04:06:40 | N/A | SURG |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-9 `1962`: Secondary and unspecified malignant neoplasm of intra-abdominal lymph nodes
- (seq 2) ICD-9 `44489`: Embolism and thrombosis of other specified artery
- (seq 3) ICD-9 `9982`: Accidental puncture or laceration during a procedure, not elsewhere classified
- (seq 4) ICD-9 `E8700`: Accidental cut, puncture, perforation or hemorrhage during surgical operation
- (seq 5) ICD-9 `3051`: Tobacco use disorder

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-9 | `1962` | Secondary and unspecified malignant neoplasm of intra-abdominal lymph nodes |
| 2 | ICD-9 | `44489` | Embolism and thrombosis of other specified artery |
| 3 | ICD-9 | `9982` | Accidental puncture or laceration during a procedure, not elsewhere classified |
| 4 | ICD-9 | `E8700` | Accidental cut, puncture, perforation or hemorrhage during surgical operation |
| 5 | ICD-9 | `3051` | Tobacco use disorder |
| 6 | ICD-9 | `V1009` | Personal history of malignant neoplasm of other gastrointestinal tract |
| 7 | ICD-9 | `V1042` | Personal history of malignant neoplasm of other parts of uterus |

## 5. ICU Stays

| Stay ID | First Care Unit | Last Care Unit | ICU Admit | ICU Discharge | LOS (days) |
|---|---|---|---|---|---|
| 39142259 | Surgical Intensive Care Unit (SICU) | Surgical Intensive Care Unit (SICU) | 2115-12-28 19:36:43 | 2115-12-30 16:31:48 | 1.87 |

## 6. Escalation / Severity Indicators

The following critical conditions or interventions were detected:

- **Arterial Line** (ICU procedure event)

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2115-12-28 | ICD-9 | `403` | Regional lymph node excision |
| 2 | 2115-12-28 | ICD-9 | `3956` | Repair of blood vessel with tissue patch graft |

### ICU Procedure Events (from `icu/procedureevents.csv.gz`)

- 16 Gauge (category: Access Lines - Peripheral, started: 2115-12-28 20:51:00, status: FinishedRunning)
- Arterial Line (category: Access Lines - Invasive, started: 2115-12-28 20:51:00, status: FinishedRunning)
- 20 Gauge (category: Access Lines - Peripheral, started: 2115-12-28 20:53:00, status: FinishedRunning)
- Ultrasound (category: 5-Imaging, started: 2115-12-29 07:30:00, status: FinishedRunning)
- CT scan (category: 5-Imaging, started: 2115-12-29 11:30:00, status: FinishedRunning)

## 8. Critical Findings (Charted Events)

- **Dialysis patient** (first noted: 2115-12-29 00:37:00)

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2115-12-28 07:15:00 | Admission | Admitted from PHYSICIAN REFERRAL (SURGICAL SAME DAY ADMISSION) |
| 2115-12-28 19:36:43 | ICU Admission | Surgical Intensive Care Unit (SICU) (LOS: 1.9 days) |
| 2115-12-28 19:36:43 | Transfer | → Surgical Intensive Care Unit (SICU) (transfer) |
| 2115-12-30 16:31:48 | Transfer | → Transplant (transfer) |
| 2116-01-02 14:34:00 | Discharge | To HOME HEALTH CARE |

## 10. Missing / Ambiguous Data

- No ED registration time — admission may not have gone through ED.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
