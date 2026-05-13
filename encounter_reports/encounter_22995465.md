# Encounter Report — HADM 22995465

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 22995465 |
| Subject ID | 10009049 |
| Patient Sex | M |
| Patient Anchor Age (at anchor year) | 56 |
| Anchor Year | 2174 |
| Admission Time | 2174-05-26 08:21:00 |
| Discharge Time | 2174-05-31 14:15:00 |
| Admission Type | EW EMER. |
| Admission Location | EMERGENCY ROOM |
| Discharge Location | HOME |
| Insurance | Other |
| Language | ENGLISH |
| Marital Status | MARRIED |
| Race/Ethnicity | WHITE |
| ED Registration | 2174-05-26 04:20:00 |
| ED Departure | 2174-05-26 09:18:00 |
| In-Hospital Mortality | No |
| Date of Death (overall) | N/A |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| APR | 720 | SEPTICEMIA & DISSEMINATED INFECTIONS | 3.0 | 2.0 |
| HCFA | 871 | SEPTICEMIA OR SEVERE SEPSIS W/O MV 96+ HOURS W MCC | N/A | N/A |

### Primary Diagnosis (seq_num = 1)

- **ICD-9 0388**: Other specified septicemias

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2174-05-26 08:22:06 | N/A | MED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-9 `0388`: Other specified septicemias
- (seq 2) ICD-9 `4829`: Bacterial pneumonia, unspecified
- (seq 3) ICD-9 `5849`: Acute kidney failure, unspecified
- (seq 4) ICD-9 `5601`: Paralytic ileus
- (seq 5) ICD-9 `2875`: Thrombocytopenia, unspecified

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-9 | `0388` | Other specified septicemias |
| 2 | ICD-9 | `4829` | Bacterial pneumonia, unspecified |
| 3 | ICD-9 | `5849` | Acute kidney failure, unspecified |
| 4 | ICD-9 | `5601` | Paralytic ileus |
| 5 | ICD-9 | `2875` | Thrombocytopenia, unspecified |
| 6 | ICD-9 | `5110` | Pleurisy without mention of effusion or current tuberculosis |
| 7 | ICD-9 | `99592` | Severe sepsis |
| 8 | ICD-9 | `2859` | Anemia, unspecified |
| 9 | ICD-9 | `60001` | Hypertrophy (benign) of prostate with urinary obstruction and other lower urinary tract symptoms (LUTS) |
| 10 | ICD-9 | `78820` | Retention of urine, unspecified |
| 11 | ICD-9 | `78791` | Diarrhea |
| 12 | ICD-9 | `79092` | Abnormal coagulation profile |
| 13 | ICD-9 | `2768` | Hypopotassemia |

## 5. ICU Stays

| Stay ID | First Care Unit | Last Care Unit | ICU Admit | ICU Discharge | LOS (days) |
|---|---|---|---|---|---|
| 35636875 | Cardiac Vascular Intensive Care Unit (CVICU) | Cardiac Vascular Intensive Care Unit (CVICU) | 2174-05-26 09:18:00 | 2174-05-27 14:31:12 | 1.22 |

## 6. Escalation / Severity Indicators

The following critical conditions or interventions were detected:

- **Acute Kidney Injury** (ICD diagnosis)
- **Pneumonia** (ICD diagnosis)
- **Sepsis** (ICD diagnosis)

## 7. Procedures and Interventions

_No ICD-coded procedures recorded._

### ICU Procedure Events (from `icu/procedureevents.csv.gz`)

- 20 Gauge (category: Access Lines - Peripheral, started: 2174-05-26 09:00:00, status: FinishedRunning)
- 18 Gauge (category: Access Lines - Peripheral, started: 2174-05-26 09:00:00, status: FinishedRunning)
- Chest X-Ray (category: 5-Imaging, started: 2174-05-27 08:00:00, status: FinishedRunning)

## 8. Critical Findings (Charted Events)

- **Dialysis patient** (first noted: 2174-05-26 10:55:00)

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2174-05-26 04:20:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2174-05-26 04:20:00 | Transfer | → Emergency Department (ED) |
| 2174-05-26 08:21:00 | Admission | Admitted from EMERGENCY ROOM (EW EMER.) |
| 2174-05-26 09:18:00 | ED Departure | Left Emergency Dept. |
| 2174-05-26 09:18:00 | ICU Admission | Cardiac Vascular Intensive Care Unit (CVICU) (LOS: 1.2 days) |
| 2174-05-27 14:31:12 | Transfer | → Medicine (transfer) |
| 2174-05-31 14:15:00 | Discharge | To HOME |

## 10. Missing / Ambiguous Data

- No procedure ICD codes — procedures may not have been coded or were minor.

## 11. Manual Review Recommendation

**This encounter is flagged for manual review:**

- ICU stay present but no ICD procedures coded.
