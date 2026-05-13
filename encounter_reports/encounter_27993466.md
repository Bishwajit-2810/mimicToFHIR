# Encounter Report — HADM 27993466

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 27993466 |
| Subject ID | 10015272 |
| Patient Sex | F |
| Patient Anchor Age (at anchor year) | 78 |
| Anchor Year | 2137 |
| Admission Time | 2137-06-12 18:36:00 |
| Discharge Time | 2137-06-18 15:45:00 |
| Admission Type | EW EMER. |
| Admission Location | EMERGENCY ROOM |
| Discharge Location | HOME HEALTH CARE |
| Insurance | Medicare |
| Language | ENGLISH |
| Marital Status | N/A |
| Race/Ethnicity | WHITE |
| ED Registration | 2137-06-12 16:54:00 |
| ED Departure | 2137-06-12 20:37:00 |
| In-Hospital Mortality | No |
| Date of Death (overall) | N/A |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| HCFA | 176 | PULMONARY EMBOLISM W/O MCC | N/A | N/A |
| APR | 134 | PULMONARY EMBOLISM | 3.0 | 3.0 |

### Primary Diagnosis (seq_num = 1)

- **ICD-10 I2699**: Other pulmonary embolism without acute cor pulmonale

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2137-06-12 18:37:22 | N/A | MED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-10 `I2699`: Other pulmonary embolism without acute cor pulmonale
- (seq 2) ICD-10 `I472`: Ventricular tachycardia
- (seq 3) ICD-10 `C9000`: Multiple myeloma not having achieved remission
- (seq 4) ICD-10 `I5022`: Chronic systolic (congestive) heart failure
- (seq 5) ICD-10 `I82412`: Acute embolism and thrombosis of left femoral vein

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-10 | `I2699` | Other pulmonary embolism without acute cor pulmonale |
| 2 | ICD-10 | `I472` | Ventricular tachycardia |
| 3 | ICD-10 | `C9000` | Multiple myeloma not having achieved remission |
| 4 | ICD-10 | `I5022` | Chronic systolic (congestive) heart failure |
| 5 | ICD-10 | `I82412` | Acute embolism and thrombosis of left femoral vein |
| 6 | ICD-10 | `I82432` | Acute embolism and thrombosis of left popliteal vein |
| 7 | ICD-10 | `Z951` | Presence of aortocoronary bypass graft |
| 8 | ICD-10 | `I4891` | Unspecified atrial fibrillation |
| 9 | ICD-10 | `D472` | Monoclonal gammopathy |
| 10 | ICD-10 | `Z7982` | Long term (current) use of aspirin |
| 11 | ICD-10 | `Z7901` | Long term (current) use of anticoagulants |
| 12 | ICD-10 | `I272` | Other secondary pulmonary hypertension |
| 13 | ICD-10 | `Z9181` | History of falling |
| 14 | ICD-10 | `R141` | Gas pain |

## 5. ICU Stays

| Stay ID | First Care Unit | Last Care Unit | ICU Admit | ICU Discharge | LOS (days) |
|---|---|---|---|---|---|
| 37267577 | Cardiac Vascular Intensive Care Unit (CVICU) | Medical/Surgical Intensive Care Unit (MICU/SICU) | 2137-06-12 18:37:22 | 2137-06-14 20:25:41 | 2.08 |

## 6. Escalation / Severity Indicators

_No escalation indicators detected from ICD codes or ICU procedure events._

## 7. Procedures and Interventions

_No ICD-coded procedures recorded._

### ICU Procedure Events (from `icu/procedureevents.csv.gz`)

- 20 Gauge (category: Access Lines - Peripheral, started: 2137-06-12 21:00:00, status: FinishedRunning)
- Transthoracic Echo (category: 5-Imaging, started: 2137-06-13 09:22:00, status: FinishedRunning)

## 8. Critical Findings (Charted Events)

- **Code Status** (first noted: 2137-06-14 11:24:00)

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2137-06-12 16:54:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2137-06-12 16:54:00 | Transfer | → Emergency Department (ED) |
| 2137-06-12 18:36:00 | Admission | Admitted from EMERGENCY ROOM (EW EMER.) |
| 2137-06-12 18:37:22 | ICU Admission | Cardiac Vascular Intensive Care Unit (CVICU) (LOS: 2.1 days) |
| 2137-06-12 18:45:08 | Transfer | → Medical/Surgical Intensive Care Unit (MICU/SICU) (transfer) |
| 2137-06-12 19:43:17 | Transfer | → Medical/Surgical Intensive Care Unit (MICU/SICU) (transfer) |
| 2137-06-12 20:37:00 | ED Departure | Left Emergency Dept. |
| 2137-06-14 20:25:41 | Transfer | → Medicine (transfer) |
| 2137-06-18 15:45:00 | Discharge | To HOME HEALTH CARE |

## 10. Missing / Ambiguous Data

- No procedure ICD codes — procedures may not have been coded or were minor.

## 11. Manual Review Recommendation

**This encounter is flagged for manual review:**

- ICU stay present but no ICD procedures coded.
