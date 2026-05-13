# Encounter Report — HADM 23112364

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 23112364 |
| Subject ID | 10021938 |
| Patient Sex | M |
| Patient Anchor Age (at anchor year) | 65 |
| Anchor Year | 2181 |
| Admission Time | 2181-10-13 01:48:00 |
| Discharge Time | 2181-10-14 17:40:00 |
| Admission Type | EW EMER. |
| Admission Location | EMERGENCY ROOM |
| Discharge Location | HOME |
| Insurance | Medicare |
| Language | ENGLISH |
| Marital Status | SINGLE |
| Race/Ethnicity | WHITE |
| ED Registration | 2181-10-12 20:17:00 |
| ED Departure | 2181-10-13 02:52:00 |
| In-Hospital Mortality | No |
| Date of Death (overall) | 2182-10-16 |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| APR | 52 | ALTERATION IN CONSCIOUSNESS | 3.0 | 2.0 |
| HCFA | 70 | NONSPECIFIC CEREBROVASCULAR DISORDERS W MCC | N/A | N/A |

### Primary Diagnosis (seq_num = 1)

- **ICD-9 34839**: Other encephalopathy

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2181-10-13 01:49:21 | N/A | MED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-9 `34839`: Other encephalopathy
- (seq 2) ICD-9 `5856`: End stage renal disease
- (seq 3) ICD-9 `40391`: Hypertensive chronic kidney disease, unspecified, with chronic kidney disease stage V or end stage renal disease
- (seq 4) ICD-9 `2767`: Hyperpotassemia
- (seq 5) ICD-9 `V1581`: Personal history of noncompliance with medical treatment, presenting hazards to health

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-9 | `34839` | Other encephalopathy |
| 2 | ICD-9 | `5856` | End stage renal disease |
| 3 | ICD-9 | `40391` | Hypertensive chronic kidney disease, unspecified, with chronic kidney disease stage V or end stage renal disease |
| 4 | ICD-9 | `2767` | Hyperpotassemia |
| 5 | ICD-9 | `V1581` | Personal history of noncompliance with medical treatment, presenting hazards to health |
| 6 | ICD-9 | `2724` | Other and unspecified hyperlipidemia |
| 7 | ICD-9 | `30500` | Alcohol abuse, unspecified |
| 8 | ICD-9 | `V1582` | Personal history of tobacco use |
| 9 | ICD-9 | `79319` | Other nonspecific abnormal finding of lung field |

## 5. ICU Stays

| Stay ID | First Care Unit | Last Care Unit | ICU Admit | ICU Discharge | LOS (days) |
|---|---|---|---|---|---|
| 39492446 | Medical Intensive Care Unit (MICU) | Medical Intensive Care Unit (MICU) | 2181-10-13 02:52:00 | 2181-10-14 18:03:28 | 1.63 |

## 6. Escalation / Severity Indicators

_No escalation indicators detected from ICD codes or ICU procedure events._

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2181-10-13 | ICD-9 | `3995` | Hemodialysis |

### ICU Procedure Events (from `icu/procedureevents.csv.gz`)

- 18 Gauge (category: Access Lines - Peripheral, started: 2181-10-13 03:23:00, status: FinishedRunning)

## 8. Critical Findings (Charted Events)

- **Code Status** (first noted: 2181-10-13 06:44:00)
- **Dialysis patient** (first noted: 2181-10-13 03:21:00)

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2181-10-12 20:17:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2181-10-12 20:17:00 | Transfer | → Emergency Department (ED) |
| 2181-10-13 01:48:00 | Admission | Admitted from EMERGENCY ROOM (EW EMER.) |
| 2181-10-13 02:52:00 | ED Departure | Left Emergency Dept. |
| 2181-10-13 02:52:00 | ICU Admission | Medical Intensive Care Unit (MICU) (LOS: 1.6 days) |
| 2181-10-14 17:40:00 | Discharge | To HOME |

## 10. Missing / Ambiguous Data

- No obvious missing critical fields detected.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
