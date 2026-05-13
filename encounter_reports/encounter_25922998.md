# Encounter Report — HADM 25922998

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 25922998 |
| Subject ID | 10002930 |
| Patient Sex | F |
| Patient Anchor Age (at anchor year) | 48 |
| Anchor Year | 2193 |
| Admission Time | 2198-04-17 19:38:00 |
| Discharge Time | 2198-04-22 16:02:00 |
| Admission Type | EW EMER. |
| Admission Location | EMERGENCY ROOM |
| Discharge Location | PSYCH FACILITY |
| Insurance | Medicare |
| Language | ENGLISH |
| Marital Status | SINGLE |
| Race/Ethnicity | BLACK/AFRICAN AMERICAN |
| ED Registration | 2198-04-17 11:42:00 |
| ED Departure | 2198-04-17 21:24:00 |
| In-Hospital Mortality | No |
| Date of Death (overall) | 2201-12-24 |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| HCFA | 897 | ALCOHOL/DRUG ABUSE OR DEPENDENCE W/O REHABILITATION THERAPY W/O MCC | N/A | N/A |
| APR | 773 | OPIOID ABUSE & DEPENDENCE | 2.0 | 1.0 |

### Primary Diagnosis (seq_num = 1)

- **ICD-10 F10239**: Alcohol dependence with withdrawal, unspecified

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2198-04-17 19:39:04 | N/A | MED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-10 `F10239`: Alcohol dependence with withdrawal, unspecified
- (seq 2) ICD-10 `F1110`: Opioid abuse, uncomplicated
- (seq 3) ICD-10 `R45851`: Suicidal ideations
- (seq 4) ICD-10 `Z87820`: Personal history of traumatic brain injury
- (seq 5) ICD-10 `B1920`: Unspecified viral hepatitis C without hepatic coma

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-10 | `F10239` | Alcohol dependence with withdrawal, unspecified |
| 2 | ICD-10 | `F1110` | Opioid abuse, uncomplicated |
| 3 | ICD-10 | `R45851` | Suicidal ideations |
| 4 | ICD-10 | `Z87820` | Personal history of traumatic brain injury |
| 5 | ICD-10 | `B1920` | Unspecified viral hepatitis C without hepatic coma |
| 6 | ICD-10 | `Z23` | Encounter for immunization |
| 7 | ICD-10 | `Z590` | Homelessness |
| 8 | ICD-10 | `F1410` | Cocaine abuse, uncomplicated |
| 9 | ICD-10 | `R509` | Fever, unspecified |
| 10 | ICD-10 | `F29` | Unspecified psychosis not due to a substance or known physiological condition |
| 11 | ICD-10 | `Z21` | Asymptomatic human immunodeficiency virus [HIV] infection status |
| 12 | ICD-10 | `Z9114` | Patient's other noncompliance with medication regimen |
| 13 | ICD-10 | `D72819` | Decreased white blood cell count, unspecified |

## 5. ICU Stays

| Stay ID | First Care Unit | Last Care Unit | ICU Admit | ICU Discharge | LOS (days) |
|---|---|---|---|---|---|
| 35629889 | Medical/Surgical Intensive Care Unit (MICU/SICU) | Medical/Surgical Intensive Care Unit (MICU/SICU) | 2198-04-17 21:24:00 | 2198-04-18 13:41:43 | 0.68 |

## 6. Escalation / Severity Indicators

_No escalation indicators detected from ICD codes or ICU procedure events._

## 7. Procedures and Interventions

_No ICD-coded procedures recorded._

### ICU Procedure Events (from `icu/procedureevents.csv.gz`)

- 22 Gauge (category: Access Lines - Peripheral, started: 2198-04-17 22:18:00, status: FinishedRunning)

## 8. Critical Findings (Charted Events)

- **Seizure** (first noted: 2198-04-17 22:00:00)

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2198-04-17 11:42:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2198-04-17 11:42:00 | Transfer | → Emergency Department (ED) |
| 2198-04-17 19:38:00 | Admission | Admitted from EMERGENCY ROOM (EW EMER.) |
| 2198-04-17 21:24:00 | ED Departure | Left Emergency Dept. |
| 2198-04-17 21:24:00 | ICU Admission | Medical/Surgical Intensive Care Unit (MICU/SICU) (LOS: 0.7 days) |
| 2198-04-18 13:41:43 | Transfer | → Medicine (transfer) |
| 2198-04-19 21:45:31 | Transfer | → Medicine (transfer) |
| 2198-04-22 16:02:00 | Discharge | To PSYCH FACILITY |

## 10. Missing / Ambiguous Data

- No procedure ICD codes — procedures may not have been coded or were minor.

## 11. Manual Review Recommendation

**This encounter is flagged for manual review:**

- ICU stay present but no ICD procedures coded.
