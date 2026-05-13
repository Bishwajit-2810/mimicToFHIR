# Encounter Report — HADM 25260176

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 25260176 |
| Subject ID | 10026406 |
| Patient Sex | M |
| Patient Anchor Age (at anchor year) | 45 |
| Anchor Year | 2129 |
| Admission Time | 2129-01-03 15:55:00 |
| Discharge Time | 2129-01-05 14:10:00 |
| Admission Type | EW EMER. |
| Admission Location | EMERGENCY ROOM |
| Discharge Location | AGAINST ADVICE |
| Insurance | Other |
| Language | ENGLISH |
| Marital Status | DIVORCED |
| Race/Ethnicity | WHITE |
| ED Registration | 2129-01-02 23:41:00 |
| ED Departure | 2129-01-03 18:33:00 |
| In-Hospital Mortality | No |
| Date of Death (overall) | N/A |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| HCFA | 894 | ALCOHOL/DRUG ABUSE OR DEPENDENCE, LEFT AMA | N/A | N/A |
| APR | 770 | DRUG & ALCOHOL ABUSE OR DEPENDENCE, LEFT AGAINST MEDICAL ADVICE | 2.0 | 1.0 |

### Primary Diagnosis (seq_num = 1)

- **ICD-9 29181**: Alcohol withdrawal

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2129-01-03 15:55:55 | N/A | MED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-9 `29181`: Alcohol withdrawal
- (seq 2) ICD-9 `78039`: Other convulsions
- (seq 3) ICD-9 `30301`: Acute alcoholic intoxication in alcoholism, continuous
- (seq 4) ICD-9 `8020`: Closed fracture of nasal bones
- (seq 5) ICD-9 `E9600`: Unarmed fight or brawl

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-9 | `29181` | Alcohol withdrawal |
| 2 | ICD-9 | `78039` | Other convulsions |
| 3 | ICD-9 | `30301` | Acute alcoholic intoxication in alcoholism, continuous |
| 4 | ICD-9 | `8020` | Closed fracture of nasal bones |
| 5 | ICD-9 | `E9600` | Unarmed fight or brawl |
| 6 | ICD-9 | `E8499` | Accidents occurring in unspecified place |
| 7 | ICD-9 | `53081` | Esophageal reflux |
| 8 | ICD-9 | `3051` | Tobacco use disorder |

## 5. ICU Stays

| Stay ID | First Care Unit | Last Care Unit | ICU Admit | ICU Discharge | LOS (days) |
|---|---|---|---|---|---|
| 30864406 | Medical Intensive Care Unit (MICU) | Medical Intensive Care Unit (MICU) | 2129-01-05 02:37:19 | 2129-01-05 14:11:03 | 0.48 |

## 6. Escalation / Severity Indicators

_No escalation indicators detected from ICD codes or ICU procedure events._

## 7. Procedures and Interventions

_No ICD-coded procedures recorded._

### ICU Procedure Events (from `icu/procedureevents.csv.gz`)

- 20 Gauge (category: Access Lines - Peripheral, started: 2129-01-05 03:00:00, status: FinishedRunning)

## 8. Critical Findings (Charted Events)

- **Code Status** (first noted: 2129-01-05 02:45:00)
- **Seizure** (first noted: 2129-01-05 08:01:00)
- **Dialysis patient** (first noted: 2129-01-05 04:19:00)

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2129-01-02 23:41:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2129-01-02 23:41:00 | Transfer | → Emergency Department (ED) |
| 2129-01-03 15:55:00 | Admission | Admitted from EMERGENCY ROOM (EW EMER.) |
| 2129-01-03 18:33:00 | ED Departure | Left Emergency Dept. |
| 2129-01-05 02:37:19 | ICU Admission | Medical Intensive Care Unit (MICU) (LOS: 0.5 days) |
| 2129-01-05 02:37:19 | Transfer | → Medical Intensive Care Unit (MICU) (transfer) |
| 2129-01-05 14:10:00 | Discharge | To AGAINST ADVICE |

## 10. Missing / Ambiguous Data

- No procedure ICD codes — procedures may not have been coded or were minor.

## 11. Manual Review Recommendation

**This encounter is flagged for manual review:**

- ICU stay present but no ICD procedures coded.
