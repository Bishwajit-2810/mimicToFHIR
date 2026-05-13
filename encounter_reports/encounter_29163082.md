# Encounter Report — HADM 29163082

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 29163082 |
| Subject ID | 10027445 |
| Patient Sex | F |
| Patient Anchor Age (at anchor year) | 48 |
| Anchor Year | 2142 |
| Admission Time | 2142-08-27 21:05:00 |
| Discharge Time | 2142-09-05 17:33:00 |
| Admission Type | URGENT |
| Admission Location | TRANSFER FROM HOSPITAL |
| Discharge Location | HOME HEALTH CARE |
| Insurance | Other |
| Language | ENGLISH |
| Marital Status | WIDOWED |
| Race/Ethnicity | WHITE |
| ED Registration | N/A |
| ED Departure | N/A |
| In-Hospital Mortality | No |
| Date of Death (overall) | 2146-02-09 |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| APR | 175 | PERCUTANEOUS CORONARY INTERVENTION W/O AMI | 3.0 | 3.0 |
| HCFA | 250 | PERC CARDIOVASC PROC W/O CORONARY ARTERY STENT W MCC | N/A | N/A |

### Primary Diagnosis (seq_num = 1)

- **ICD-9 4240**: Mitral valve disorders

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2142-08-27 21:06:05 | N/A | CMED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-9 `4240`: Mitral valve disorders
- (seq 2) ICD-9 `42833`: Acute on chronic diastolic heart failure
- (seq 3) ICD-9 `9982`: Accidental puncture or laceration during a procedure, not elsewhere classified
- (seq 4) ICD-9 `2763`: Alkalosis
- (seq 5) ICD-9 `4280`: Congestive heart failure, unspecified

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-9 | `4240` | Mitral valve disorders |
| 2 | ICD-9 | `42833` | Acute on chronic diastolic heart failure |
| 3 | ICD-9 | `9982` | Accidental puncture or laceration during a procedure, not elsewhere classified |
| 4 | ICD-9 | `2763` | Alkalosis |
| 5 | ICD-9 | `4280` | Congestive heart failure, unspecified |
| 6 | ICD-9 | `25000` | Diabetes mellitus without mention of complication, type II or unspecified type, not stated as uncontrolled |
| 7 | ICD-9 | `515` | Postinflammatory pulmonary fibrosis |
| 8 | ICD-9 | `4168` | Other chronic pulmonary heart diseases |
| 9 | ICD-9 | `E8706` | Accidental cut, puncture, perforation or hemorrhage during heart catheterization |
| 10 | ICD-9 | `V5867` | Long-term (current) use of insulin |
| 11 | ICD-9 | `311` | Depressive disorder, not elsewhere classified |

## 5. ICU Stays

| Stay ID | First Care Unit | Last Care Unit | ICU Admit | ICU Discharge | LOS (days) |
|---|---|---|---|---|---|
| 36084484 | Coronary Care Unit (CCU) | Coronary Care Unit (CCU) | 2142-08-30 13:20:56 | 2142-08-31 18:19:36 | 1.21 |

## 6. Escalation / Severity Indicators

The following critical conditions or interventions were detected:

- **Arterial Line** (ICU procedure event)

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2142-09-03 | ICD-9 | `3596` | Percutaneous balloon valvuloplasty |
| 2 | 2142-08-30 | ICD-9 | `3721` | Right heart cardiac catheterization |
| 3 | 2142-08-30 | ICD-9 | `8872` | Diagnostic ultrasound of heart |
| 4 | 2142-08-28 | ICD-9 | `3723` | Combined right and left heart cardiac catheterization |
| 5 | 2142-08-28 | ICD-9 | `8854` | Combined right and left heart angiocardiography |

### ICU Procedure Events (from `icu/procedureevents.csv.gz`)

- Sheath (Venous) (category: Access Lines - Invasive, started: 2142-08-30 14:27:00, status: FinishedRunning)
- Arterial Line (category: Access Lines - Invasive, started: 2142-08-30 14:28:00, status: FinishedRunning)
- 20 Gauge (category: Access Lines - Peripheral, started: 2142-08-30 22:00:00, status: FinishedRunning)

## 8. Critical Findings (Charted Events)

- **Code Status** (first noted: 2142-08-30 21:25:00)
- **Dialysis patient** (first noted: 2142-08-30 13:46:00)

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2142-08-27 21:05:00 | Admission | Admitted from TRANSFER FROM HOSPITAL (URGENT) |
| 2142-08-30 13:20:56 | ICU Admission | Coronary Care Unit (CCU) (LOS: 1.2 days) |
| 2142-08-30 13:20:56 | Transfer | → Coronary Care Unit (CCU) (transfer) |
| 2142-08-31 18:19:36 | Transfer | → Medicine/Cardiology (transfer) |
| 2142-09-05 17:33:00 | Discharge | To HOME HEALTH CARE |

## 10. Missing / Ambiguous Data

- No ED registration time — admission may not have gone through ED.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
