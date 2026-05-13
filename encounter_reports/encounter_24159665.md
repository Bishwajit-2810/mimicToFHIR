# Encounter Report — HADM 24159665

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 24159665 |
| Subject ID | 10006580 |
| Patient Sex | F |
| Patient Anchor Age (at anchor year) | 63 |
| Anchor Year | 2137 |
| Admission Time | 2137-08-10 11:00:00 |
| Discharge Time | 2137-08-15 13:25:00 |
| Admission Type | ELECTIVE |
| Admission Location | PHYSICIAN REFERRAL |
| Discharge Location | HOME |
| Insurance | Medicaid |
| Language | ? |
| Marital Status | MARRIED |
| Race/Ethnicity | HISPANIC/LATINO - SALVADORAN |
| ED Registration | N/A |
| ED Departure | N/A |
| In-Hospital Mortality | No |
| Date of Death (overall) | N/A |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| HCFA | 983 | EXTENSIVE O.R. PROCEDURE UNRELATED TO PRINCIPAL DIAGNOSIS W/O CC/MCC | N/A | N/A |
| APR | 951 | MODERATELY EXTENSIVE PROCEDURE UNRELATED TO PRINCIPAL DIAGNOSIS | 1.0 | 1.0 |

### Primary Diagnosis (seq_num = 1)

- **ICD-9 2397**: Neoplasm of unspecified nature of endocrine glands and other parts of nervous system

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2137-08-10 05:32:24 | N/A | VSURG |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-9 `2397`: Neoplasm of unspecified nature of endocrine glands and other parts of nervous system
- (seq 2) ICD-9 `25000`: Diabetes mellitus without mention of complication, type II or unspecified type, not stated as uncontrolled
- (seq 3) ICD-9 `4019`: Unspecified essential hypertension
- (seq 4) ICD-9 `311`: Depressive disorder, not elsewhere classified
- (seq 5) ICD-9 `2724`: Other and unspecified hyperlipidemia

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-9 | `2397` | Neoplasm of unspecified nature of endocrine glands and other parts of nervous system |
| 2 | ICD-9 | `25000` | Diabetes mellitus without mention of complication, type II or unspecified type, not stated as uncontrolled |
| 3 | ICD-9 | `4019` | Unspecified essential hypertension |
| 4 | ICD-9 | `311` | Depressive disorder, not elsewhere classified |
| 5 | ICD-9 | `2724` | Other and unspecified hyperlipidemia |
| 6 | ICD-9 | `V4586` | Bariatric surgery status |
| 7 | ICD-9 | `71690` | Arthropathy, unspecified, site unspecified |
| 8 | ICD-9 | `V5866` | Long-term (current) use of aspirin |
| 9 | ICD-9 | `2749` | Gout, unspecified |
| 10 | ICD-9 | `V5867` | Long-term (current) use of insulin |

## 5. ICU Stays

| Stay ID | First Care Unit | Last Care Unit | ICU Admit | ICU Discharge | LOS (days) |
|---|---|---|---|---|---|
| 38329661 | Cardiac Vascular Intensive Care Unit (CVICU) | Cardiac Vascular Intensive Care Unit (CVICU) | 2137-08-10 16:23:10 | 2137-08-11 13:56:56 | 0.90 |

## 6. Escalation / Severity Indicators

The following critical conditions or interventions were detected:

- **Arterial Line** (ICU procedure event)

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2137-08-11 | ICD-9 | `3989` | Other operations on carotid body, carotid sinus and other vascular bodies |
| 2 | 2137-08-11 | ICD-9 | `3981` | Implantation or replacement of carotid sinus stimulation device, total system |

### ICU Procedure Events (from `icu/procedureevents.csv.gz`)

- Arterial Line (category: Access Lines - Invasive, started: 2137-08-10 16:30:00, status: FinishedRunning)
- 18 Gauge (category: Access Lines - Peripheral, started: 2137-08-10 17:15:00, status: FinishedRunning)
- OR Received (category: 3-Significant Events, started: 2137-08-10 17:15:00, status: FinishedRunning)
- EKG (category: 4-Procedures, started: 2137-08-10 18:30:00, status: FinishedRunning)

## 8. Critical Findings (Charted Events)

- **Dialysis patient** (first noted: 2137-08-10 21:15:00)

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2137-08-10 11:00:00 | Admission | Admitted from PHYSICIAN REFERRAL (ELECTIVE) |
| 2137-08-10 16:23:10 | ICU Admission | Cardiac Vascular Intensive Care Unit (CVICU) (LOS: 0.9 days) |
| 2137-08-10 16:23:10 | Transfer | → Cardiac Vascular Intensive Care Unit (CVICU) (transfer) |
| 2137-08-10 22:20:11 | Transfer | → Cardiac Vascular Intensive Care Unit (CVICU) (transfer) |
| 2137-08-11 13:56:56 | Transfer | → PACU (transfer) |
| 2137-08-11 14:31:54 | Transfer | → Vascular (transfer) |
| 2137-08-15 13:25:00 | Discharge | To HOME |

## 10. Missing / Ambiguous Data

- No ED registration time — admission may not have gone through ED.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
