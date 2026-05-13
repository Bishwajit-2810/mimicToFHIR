# Encounter Report — HADM 22059910

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 22059910 |
| Subject ID | 10026255 |
| Patient Sex | M |
| Patient Anchor Age (at anchor year) | 66 |
| Anchor Year | 2200 |
| Admission Time | 2201-07-07 18:15:00 |
| Discharge Time | 2201-07-13 23:27:00 |
| Admission Type | EW EMER. |
| Admission Location | EMERGENCY ROOM |
| Discharge Location | DIED |
| Insurance | Other |
| Language | ENGLISH |
| Marital Status | MARRIED |
| Race/Ethnicity | WHITE |
| ED Registration | 2201-07-07 12:31:00 |
| ED Departure | 2201-07-07 19:40:00 |
| In-Hospital Mortality | YES — Death time: 2201-07-13 23:27:00 |
| Date of Death (overall) | 2201-07-13 |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| HCFA | 180 | RESPIRATORY NEOPLASMS W MCC | N/A | N/A |
| APR | 136 | RESPIRATORY MALIGNANCY | 4.0 | 4.0 |

### Primary Diagnosis (seq_num = 1)

- **ICD-9 1629**: Malignant neoplasm of bronchus and lung, unspecified

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2201-07-07 18:16:14 | N/A | MED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-9 `1629`: Malignant neoplasm of bronchus and lung, unspecified
- (seq 2) ICD-9 `41519`: Other pulmonary embolism and infarction
- (seq 3) ICD-9 `51881`: Acute respiratory failure
- (seq 4) ICD-9 `1971`: Secondary malignant neoplasm of mediastinum
- (seq 5) ICD-9 `2762`: Acidosis

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-9 | `1629` | Malignant neoplasm of bronchus and lung, unspecified |
| 2 | ICD-9 | `41519` | Other pulmonary embolism and infarction |
| 3 | ICD-9 | `51881` | Acute respiratory failure |
| 4 | ICD-9 | `1971` | Secondary malignant neoplasm of mediastinum |
| 5 | ICD-9 | `2762` | Acidosis |
| 6 | ICD-9 | `4238` | Other specified diseases of pericardium |
| 7 | ICD-9 | `07032` | Chronic viral hepatitis B without mention of hepatic coma without mention of hepatitis delta |
| 8 | ICD-9 | `07070` | Unspecified viral hepatitis C without hepatic coma |
| 9 | ICD-9 | `496` | Chronic airway obstruction, not elsewhere classified |
| 10 | ICD-9 | `2930` | Delirium due to conditions classified elsewhere |
| 11 | ICD-9 | `41189` | Other acute and subacute forms of ischemic heart disease, other |
| 12 | ICD-9 | `7295` | Pain in limb |
| 13 | ICD-9 | `28860` | Leukocytosis, unspecified |
| 14 | ICD-9 | `9086` | Late effect of certain complications of trauma |
| 15 | ICD-9 | `34550` | Localization-related (focal) (partial) epilepsy and epileptic syndromes with simple partial seizures, without mention of intractable epilepsy |
| 16 | ICD-9 | `42731` | Atrial fibrillation |
| 17 | ICD-9 | `3051` | Tobacco use disorder |
| 18 | ICD-9 | `E9290` | Late effects of motor vehicle accident |
| 19 | ICD-9 | `30981` | Posttraumatic stress disorder |
| 20 | ICD-9 | `V4986` | Do not resuscitate status |
| 21 | ICD-9 | `4019` | Unspecified essential hypertension |
| 22 | ICD-9 | `2724` | Other and unspecified hyperlipidemia |

## 5. ICU Stays

| Stay ID | First Care Unit | Last Care Unit | ICU Admit | ICU Discharge | LOS (days) |
|---|---|---|---|---|---|
| 31248398 | Coronary Care Unit (CCU) | Coronary Care Unit (CCU) | 2201-07-07 19:40:00 | 2201-07-08 15:43:15 | 0.84 |
| 38229329 | Surgical Intensive Care Unit (SICU) | Surgical Intensive Care Unit (SICU) | 2201-07-10 10:10:47 | 2201-07-11 13:48:02 | 1.15 |

## 6. Escalation / Severity Indicators

The following critical conditions or interventions were detected:

- **Non-Invasive Ventilation (NIV/BiPAP)** (ICU procedure event)
- **Respiratory Failure** (ICD diagnosis)

## 7. Procedures and Interventions

_No ICD-coded procedures recorded._

### ICU Procedure Events (from `icu/procedureevents.csv.gz`)

- 20 Gauge (category: Access Lines - Peripheral, started: 2201-07-07 19:45:00, status: FinishedRunning)
- 18 Gauge (category: Access Lines - Peripheral, started: 2201-07-07 19:45:00, status: FinishedRunning)
- Nasal Swab (category: 6-Cultures, started: 2201-07-07 20:00:00, status: FinishedRunning)
- Transthoracic Echo (category: 5-Imaging, started: 2201-07-08 08:09:00, status: FinishedRunning)
- EKG (category: 4-Procedures, started: 2201-07-08 08:16:00, status: FinishedRunning)
- 22 Gauge (category: Access Lines - Peripheral, started: 2201-07-09 10:25:00, status: FinishedRunning)
- Non-invasive Ventilation (category: 2-Ventilation, started: 2201-07-10 12:32:00, status: FinishedRunning)
- CT scan (category: 5-Imaging, started: 2201-07-10 17:07:00, status: FinishedRunning)

## 8. Critical Findings (Charted Events)

- **Ventilator Type** (first noted: 2201-07-10 12:00:00)
- **Ventilator Mode** (first noted: 2201-07-10 12:00:00)
- **Code Status** (first noted: 2201-07-07 19:09:00)
- **Dialysis patient** (first noted: 2201-07-07 19:10:00)

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2201-07-07 12:31:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2201-07-07 12:31:00 | Transfer | → Emergency Department (ED) |
| 2201-07-07 18:15:00 | Admission | Admitted from EMERGENCY ROOM (EW EMER.) |
| 2201-07-07 19:40:00 | ED Departure | Left Emergency Dept. |
| 2201-07-07 19:40:00 | ICU Admission | Coronary Care Unit (CCU) (LOS: 0.8 days) |
| 2201-07-08 15:43:15 | Transfer | → Med/Surg (transfer) |
| 2201-07-09 14:53:20 | Transfer | → Med/Surg (transfer) |
| 2201-07-10 10:10:47 | ICU Admission | Surgical Intensive Care Unit (SICU) (LOS: 1.2 days) |
| 2201-07-10 10:10:47 | Transfer | → Surgical Intensive Care Unit (SICU) (transfer) |
| 2201-07-11 13:48:02 | Transfer | → Medicine (transfer) |
| 2201-07-13 23:27:00 | **IN-HOSPITAL DEATH** | |
| 2201-07-13 23:27:00 | Discharge | To DIED |

## 10. Missing / Ambiguous Data

- No procedure ICD codes — procedures may not have been coded or were minor.

## 11. Manual Review Recommendation

**This encounter is flagged for manual review:**

- ICU stay present but no ICD procedures coded.
