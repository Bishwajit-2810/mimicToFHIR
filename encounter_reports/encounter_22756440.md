# Encounter Report — HADM 22756440

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 22756440 |
| Subject ID | 10021666 |
| Patient Sex | M |
| Patient Anchor Age (at anchor year) | 87 |
| Anchor Year | 2172 |
| Admission Time | 2172-03-12 23:47:00 |
| Discharge Time | 2172-03-23 15:40:00 |
| Admission Type | EW EMER. |
| Admission Location | EMERGENCY ROOM |
| Discharge Location | CHRONIC/LONG TERM ACUTE CARE |
| Insurance | Medicare |
| Language | ENGLISH |
| Marital Status | MARRIED |
| Race/Ethnicity | WHITE |
| ED Registration | 2172-03-12 20:52:00 |
| ED Departure | 2172-03-13 01:46:00 |
| In-Hospital Mortality | No |
| Date of Death (overall) | 2172-04-19 |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| HCFA | 85 | TRAUMATIC STUPOR & COMA, COMA <1 HR W MCC | N/A | N/A |
| APR | 55 | HEAD TRAUMA W COMA >1 HR OR HEMORRHAGE | 4.0 | 4.0 |

### Primary Diagnosis (seq_num = 1)

- **ICD-9 85201**: Subarachnoid hemorrhage following injury without mention of open intracranial wound, with no loss of consciousness

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2172-03-12 23:48:22 | N/A | NSURG |
| 2172-03-17 16:36:05 | NSURG | MED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-9 `85201`: Subarachnoid hemorrhage following injury without mention of open intracranial wound, with no loss of consciousness
- (seq 2) ICD-9 `34831`: Metabolic encephalopathy
- (seq 3) ICD-9 `2930`: Delirium due to conditions classified elsewhere
- (seq 4) ICD-9 `81342`: Other closed fractures of distal end of radius (alone)
- (seq 5) ICD-9 `5849`: Acute kidney failure, unspecified

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-9 | `85201` | Subarachnoid hemorrhage following injury without mention of open intracranial wound, with no loss of consciousness |
| 2 | ICD-9 | `34831` | Metabolic encephalopathy |
| 3 | ICD-9 | `2930` | Delirium due to conditions classified elsewhere |
| 4 | ICD-9 | `81342` | Other closed fractures of distal end of radius (alone) |
| 5 | ICD-9 | `5849` | Acute kidney failure, unspecified |
| 6 | ICD-9 | `2760` | Hyperosmolality and/or hypernatremia |
| 7 | ICD-9 | `42822` | Chronic systolic heart failure |
| 8 | ICD-9 | `85221` | Subdural hemorrhage following injury without mention of open intracranial wound, with no loss of consciousness |
| 9 | ICD-9 | `E8889` | Unspecified fall |
| 10 | ICD-9 | `4280` | Congestive heart failure, unspecified |
| 11 | ICD-9 | `41401` | Coronary atherosclerosis of native coronary artery |
| 12 | ICD-9 | `30501` | Alcohol abuse, continuous |
| 13 | ICD-9 | `29420` | Dementia, unspecified, without behavioral disturbance |
| 14 | ICD-9 | `3682` | Diplopia |
| 15 | ICD-9 | `2875` | Thrombocytopenia, unspecified |
| 16 | ICD-9 | `78729` | Other dysphagia |
| 17 | ICD-9 | `40390` | Hypertensive chronic kidney disease, unspecified, with chronic kidney disease stage I through stage IV, or unspecified |
| 18 | ICD-9 | `5853` | Chronic kidney disease, Stage III (moderate) |
| 19 | ICD-9 | `58389` | Nephritis and nephropathy, not specified as acute or chronic, with other specified pathological lesion in kidney |
| 20 | ICD-9 | `60000` | Hypertrophy (benign) of prostate without urinary obstruction and other lower urinary tract symptom (LUTS) |
| 21 | ICD-9 | `49390` | Asthma, unspecified type, unspecified |
| 22 | ICD-9 | `2724` | Other and unspecified hyperlipidemia |
| 23 | ICD-9 | `28860` | Leukocytosis, unspecified |
| 24 | ICD-9 | `42731` | Atrial fibrillation |
| 25 | ICD-9 | `56400` | Constipation, unspecified |
| 26 | ICD-9 | `2252` | Benign neoplasm of cerebral meninges |
| 27 | ICD-9 | `2819` | Unspecified deficiency anemia |
| 28 | ICD-9 | `3898` | Other specified forms of hearing loss |
| 29 | ICD-9 | `412` | Old myocardial infarction |
| 30 | ICD-9 | `V4502` | Automatic implantable cardiac defibrillator in situ |
| 31 | ICD-9 | `V4364` | Hip joint replacement |
| 32 | ICD-9 | `V4986` | Do not resuscitate status |

## 5. ICU Stays

| Stay ID | First Care Unit | Last Care Unit | ICU Admit | ICU Discharge | LOS (days) |
|---|---|---|---|---|---|
| 35475449 | Surgical Intensive Care Unit (SICU) | Surgical Intensive Care Unit (SICU) | 2172-03-13 01:46:00 | 2172-03-13 16:33:34 | 0.62 |

## 6. Escalation / Severity Indicators

The following critical conditions or interventions were detected:

- **Acute Kidney Injury** (ICD diagnosis)

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2172-03-15 | ICD-9 | `966` | Enteral infusion of concentrated nutritional substances |
| 2 | 2172-03-23 | ICD-9 | `9608` | Insertion of (naso-)intestinal tube |

### ICU Procedure Events (from `icu/procedureevents.csv.gz`)

- 22 Gauge (category: Access Lines - Peripheral, started: 2172-03-13 03:05:00, status: FinishedRunning)
- 20 Gauge (category: Access Lines - Peripheral, started: 2172-03-13 03:05:00, status: FinishedRunning)
- CT scan (category: 5-Imaging, started: 2172-03-13 06:47:00, status: FinishedRunning)

## 8. Critical Findings (Charted Events)

_No critical chart events detected._

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2172-03-12 20:52:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2172-03-12 20:52:00 | Transfer | → Emergency Department (ED) |
| 2172-03-12 23:47:00 | Admission | Admitted from EMERGENCY ROOM (EW EMER.) |
| 2172-03-13 01:46:00 | ED Departure | Left Emergency Dept. |
| 2172-03-13 01:46:00 | ICU Admission | Surgical Intensive Care Unit (SICU) (LOS: 0.6 days) |
| 2172-03-13 16:33:34 | Transfer | → Neurology (transfer) |
| 2172-03-13 16:42:23 | Transfer | → Neurology (transfer) |
| 2172-03-23 15:40:00 | Discharge | To CHRONIC/LONG TERM ACUTE CARE |

## 10. Missing / Ambiguous Data

- No obvious missing critical fields detected.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
