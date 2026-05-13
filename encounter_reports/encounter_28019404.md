# Encounter Report — HADM 28019404

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 28019404 |
| Subject ID | 10036156 |
| Patient Sex | F |
| Patient Anchor Age (at anchor year) | 88 |
| Anchor Year | 2157 |
| Admission Time | 2157-07-01 04:52:00 |
| Discharge Time | 2157-07-03 15:08:00 |
| Admission Type | URGENT |
| Admission Location | TRANSFER FROM HOSPITAL |
| Discharge Location | HOME |
| Insurance | Other |
| Language | ENGLISH |
| Marital Status | N/A |
| Race/Ethnicity | UNKNOWN |
| ED Registration | N/A |
| ED Departure | N/A |
| In-Hospital Mortality | No |
| Date of Death (overall) | N/A |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| APR | 241 | PEPTIC ULCER & GASTRITIS | 3.0 | 3.0 |
| HCFA | 378 | G.I. HEMORRHAGE W CC | N/A | N/A |

### Primary Diagnosis (seq_num = 1)

- **ICD-9 53140**: Chronic or unspecified gastric ulcer with hemorrhage, without mention of obstruction

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2157-07-01 04:52:37 | N/A | MED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-9 `53140`: Chronic or unspecified gastric ulcer with hemorrhage, without mention of obstruction
- (seq 2) ICD-9 `4260`: Atrioventricular block, complete
- (seq 3) ICD-9 `4588`: Other specified hypotension
- (seq 4) ICD-9 `25000`: Diabetes mellitus without mention of complication, type II or unspecified type, not stated as uncontrolled
- (seq 5) ICD-9 `2724`: Other and unspecified hyperlipidemia

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-9 | `53140` | Chronic or unspecified gastric ulcer with hemorrhage, without mention of obstruction |
| 2 | ICD-9 | `4260` | Atrioventricular block, complete |
| 3 | ICD-9 | `4588` | Other specified hypotension |
| 4 | ICD-9 | `25000` | Diabetes mellitus without mention of complication, type II or unspecified type, not stated as uncontrolled |
| 5 | ICD-9 | `2724` | Other and unspecified hyperlipidemia |
| 6 | ICD-9 | `28860` | Leukocytosis, unspecified |
| 7 | ICD-9 | `78097` | Altered mental status |
| 8 | ICD-9 | `V4501` | Cardiac pacemaker in situ |
| 9 | ICD-9 | `V4589` | Other postprocedural status |
| 10 | ICD-9 | `4019` | Unspecified essential hypertension |
| 11 | ICD-9 | `79092` | Abnormal coagulation profile |

## 5. ICU Stays

| Stay ID | First Care Unit | Last Care Unit | ICU Admit | ICU Discharge | LOS (days) |
|---|---|---|---|---|---|
| 38587181 | Medical Intensive Care Unit (MICU) | Medical Intensive Care Unit (MICU) | 2157-07-01 04:52:37 | 2157-07-02 14:18:55 | 1.39 |

## 6. Escalation / Severity Indicators

_No escalation indicators detected from ICD codes or ICU procedure events._

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2157-07-01 | ICD-9 | `4444` | Transcatheter embolization for gastric or duodenal bleeding |
| 2 | 2157-07-01 | ICD-9 | `8847` | Arteriography of other intra-abdominal arteries |

### ICU Procedure Events (from `icu/procedureevents.csv.gz`)

- 22 Gauge (category: Access Lines - Peripheral, started: 2157-07-01 05:04:00, status: FinishedRunning)
- Urine Culture (category: 6-Cultures, started: 2157-07-01 09:00:00, status: FinishedRunning)
- 18 Gauge (category: Access Lines - Peripheral, started: 2157-07-01 09:30:00, status: FinishedRunning)
- CT scan (category: 5-Imaging, started: 2157-07-01 10:00:00, status: FinishedRunning)
- Interventional Radiology (category: 5-Imaging, started: 2157-07-01 10:15:00, status: FinishedRunning)

## 8. Critical Findings (Charted Events)

- **Code Status** (first noted: 2157-07-02 12:53:00)

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2157-07-01 04:52:00 | Admission | Admitted from TRANSFER FROM HOSPITAL (URGENT) |
| 2157-07-01 04:52:37 | ICU Admission | Medical Intensive Care Unit (MICU) (LOS: 1.4 days) |
| 2157-07-02 14:18:55 | Transfer | → Medicine (transfer) |
| 2157-07-03 15:08:00 | Discharge | To HOME |

## 10. Missing / Ambiguous Data

- No ED registration time — admission may not have gone through ED.

## 11. Manual Review Recommendation

**This encounter is flagged for manual review:**

- Urgent/Emergency admission but no clear escalation indicator found.
