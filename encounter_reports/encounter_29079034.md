# Encounter Report — HADM 29079034

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 29079034 |
| Subject ID | 10000032 |
| Patient Sex | F |
| Patient Anchor Age (at anchor year) | 52 |
| Anchor Year | 2180 |
| Admission Time | 2180-07-23 12:35:00 |
| Discharge Time | 2180-07-25 17:55:00 |
| Admission Type | EW EMER. |
| Admission Location | EMERGENCY ROOM |
| Discharge Location | HOME |
| Insurance | Medicaid |
| Language | ENGLISH |
| Marital Status | WIDOWED |
| Race/Ethnicity | WHITE |
| ED Registration | 2180-07-23 05:54:00 |
| ED Departure | 2180-07-23 14:00:00 |
| In-Hospital Mortality | No |
| Date of Death (overall) | 2180-09-09 |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| APR | 207 | OTHER CIRCULATORY SYSTEM DIAGNOSES | 3.0 | 3.0 |
| HCFA | 312 | SYNCOPE & COLLAPSE | N/A | N/A |

### Primary Diagnosis (seq_num = 1)

- **ICD-9 45829**: Other iatrogenic hypotension

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2180-07-23 12:36:04 | N/A | MED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-9 `45829`: Other iatrogenic hypotension
- (seq 2) ICD-9 `07044`: Chronic hepatitis C with hepatic coma
- (seq 3) ICD-9 `7994`: Cachexia
- (seq 4) ICD-9 `2761`: Hyposmolality and/or hyponatremia
- (seq 5) ICD-9 `78959`: Other ascites

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-9 | `45829` | Other iatrogenic hypotension |
| 2 | ICD-9 | `07044` | Chronic hepatitis C with hepatic coma |
| 3 | ICD-9 | `7994` | Cachexia |
| 4 | ICD-9 | `2761` | Hyposmolality and/or hyponatremia |
| 5 | ICD-9 | `78959` | Other ascites |
| 6 | ICD-9 | `2767` | Hyperpotassemia |
| 7 | ICD-9 | `3051` | Tobacco use disorder |
| 8 | ICD-9 | `V08` | Asymptomatic human immunodeficiency virus [HIV] infection status |
| 9 | ICD-9 | `V4986` | Do not resuscitate status |
| 10 | ICD-9 | `V462` | Other dependence on machines, supplemental oxygen |
| 11 | ICD-9 | `496` | Chronic airway obstruction, not elsewhere classified |
| 12 | ICD-9 | `29680` | Bipolar disorder, unspecified |
| 13 | ICD-9 | `5715` | Cirrhosis of liver without mention of alcohol |

## 5. ICU Stays

| Stay ID | First Care Unit | Last Care Unit | ICU Admit | ICU Discharge | LOS (days) |
|---|---|---|---|---|---|
| 39553978 | Medical Intensive Care Unit (MICU) | Medical Intensive Care Unit (MICU) | 2180-07-23 14:00:00 | 2180-07-23 23:50:47 | 0.41 |

## 6. Escalation / Severity Indicators

_No escalation indicators detected from ICD codes or ICU procedure events._

## 7. Procedures and Interventions

_No ICD-coded procedures recorded._

### ICU Procedure Events (from `icu/procedureevents.csv.gz`)

- 20 Gauge (category: Access Lines - Peripheral, started: 2180-07-23 14:24:00, status: FinishedRunning)
- 18 Gauge (category: Access Lines - Peripheral, started: 2180-07-23 14:24:00, status: FinishedRunning)
- Nasal Swab (category: 6-Cultures, started: 2180-07-23 14:43:00, status: FinishedRunning)

## 8. Critical Findings (Charted Events)

- **Code Status** (first noted: 2180-07-23 14:22:00)

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2180-07-22 16:24:00 | Transfer | → Emergency Department (ED) |
| 2180-07-23 05:54:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2180-07-23 05:54:00 | Transfer | → Emergency Department (ED) |
| 2180-07-23 12:35:00 | Admission | Admitted from EMERGENCY ROOM (EW EMER.) |
| 2180-07-23 14:00:00 | ED Departure | Left Emergency Dept. |
| 2180-07-23 14:00:00 | ICU Admission | Medical Intensive Care Unit (MICU) (LOS: 0.4 days) |
| 2180-07-23 23:50:47 | Transfer | → Transplant (transfer) |
| 2180-07-24 19:52:58 | Transfer | → Transplant (transfer) |
| 2180-07-25 17:55:00 | Discharge | To HOME |

## 10. Missing / Ambiguous Data

- No procedure ICD codes — procedures may not have been coded or were minor.

## 11. Manual Review Recommendation

**This encounter is flagged for manual review:**

- ICU stay present but no ICD procedures coded.
