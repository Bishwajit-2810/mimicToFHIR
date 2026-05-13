# Encounter Report — HADM 29374560

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 29374560 |
| Subject ID | 10016150 |
| Patient Sex | M |
| Patient Anchor Age (at anchor year) | 69 |
| Anchor Year | 2142 |
| Admission Time | 2142-05-10 15:05:00 |
| Discharge Time | 2142-05-15 19:49:00 |
| Admission Type | EW EMER. |
| Admission Location | PROCEDURE SITE |
| Discharge Location | REHAB |
| Insurance | Medicare |
| Language | ENGLISH |
| Marital Status | SINGLE |
| Race/Ethnicity | WHITE |
| ED Registration | N/A |
| ED Departure | N/A |
| In-Hospital Mortality | No |
| Date of Death (overall) | N/A |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| APR | 192 | CARDIAC CATHETERIZATION FOR OTHER NON-CORONARY CONDITIONS | 2.0 | 2.0 |
| HCFA | 287 | CIRCULATORY DISORDERS EXCEPT AMI, W CARD CATH W/O MCC | N/A | N/A |

### Primary Diagnosis (seq_num = 1)

- **ICD-9 41402**: Coronary atherosclerosis of autologous vein bypass graft

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2142-05-10 15:06:23 | N/A | CMED |
| 2142-05-10 20:24:25 | CMED | NSURG |
| 2142-05-15 18:27:45 | NSURG | NMED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-9 `41402`: Coronary atherosclerosis of autologous vein bypass graft
- (seq 2) ICD-9 `4254`: Other primary cardiomyopathies
- (seq 3) ICD-9 `42731`: Atrial fibrillation
- (seq 4) ICD-9 `25000`: Diabetes mellitus without mention of complication, type II or unspecified type, not stated as uncontrolled
- (seq 5) ICD-9 `7843`: Aphasia

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-9 | `41402` | Coronary atherosclerosis of autologous vein bypass graft |
| 2 | ICD-9 | `4254` | Other primary cardiomyopathies |
| 3 | ICD-9 | `42731` | Atrial fibrillation |
| 4 | ICD-9 | `25000` | Diabetes mellitus without mention of complication, type II or unspecified type, not stated as uncontrolled |
| 5 | ICD-9 | `7843` | Aphasia |
| 6 | ICD-9 | `40390` | Hypertensive chronic kidney disease, unspecified, with chronic kidney disease stage I through stage IV, or unspecified |
| 7 | ICD-9 | `3569` | Unspecified hereditary and idiopathic peripheral neuropathy |
| 8 | ICD-9 | `99702` | Iatrogenic cerebrovascular infarction or hemorrhage |
| 9 | ICD-9 | `41401` | Coronary atherosclerosis of native coronary artery |
| 10 | ICD-9 | `78194` | Facial weakness |
| 11 | ICD-9 | `E8790` | Cardiac catheterization as the cause of abnormal reaction of patient, or of later complication, without mention of misadventure at time of procedure |
| 12 | ICD-9 | `E8497` | Accidents occurring in residential institution |
| 13 | ICD-9 | `V5861` | Long-term (current) use of anticoagulants |
| 14 | ICD-9 | `5859` | Chronic kidney disease, unspecified |
| 15 | ICD-9 | `V5867` | Long-term (current) use of insulin |
| 16 | ICD-9 | `V4501` | Cardiac pacemaker in situ |
| 17 | ICD-9 | `V1582` | Personal history of tobacco use |

## 5. ICU Stays

| Stay ID | First Care Unit | Last Care Unit | ICU Admit | ICU Discharge | LOS (days) |
|---|---|---|---|---|---|
| 33652203 | Surgical Intensive Care Unit (SICU) | Surgical Intensive Care Unit (SICU) | 2142-05-10 16:39:15 | 2142-05-10 20:23:49 | 0.16 |

## 6. Escalation / Severity Indicators

_No escalation indicators detected from ICD codes or ICU procedure events._

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2142-05-10 | ICD-9 | `3722` | Left heart cardiac catheterization |
| 2 | 2142-05-10 | ICD-9 | `8853` | Angiocardiography of left heart structures |
| 3 | 2142-05-10 | ICD-9 | `8856` | Coronary arteriography using two catheters |

### ICU Procedure Events (from `icu/procedureevents.csv.gz`)

- 18 Gauge (category: Access Lines - Peripheral, started: 2142-05-10 16:57:00, status: FinishedRunning)
- 20 Gauge (category: Access Lines - Peripheral, started: 2142-05-10 16:58:00, status: FinishedRunning)

## 8. Critical Findings (Charted Events)

_No critical chart events detected._

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2142-05-10 15:05:00 | Admission | Admitted from PROCEDURE SITE (EW EMER.) |
| 2142-05-10 16:39:15 | ICU Admission | Surgical Intensive Care Unit (SICU) (LOS: 0.2 days) |
| 2142-05-10 16:39:15 | Transfer | → Surgical Intensive Care Unit (SICU) (transfer) |
| 2142-05-10 20:23:49 | Transfer | → Med/Surg (transfer) |
| 2142-05-10 20:24:48 | Transfer | → Med/Surg (transfer) |
| 2142-05-15 19:49:00 | Discharge | To REHAB |

## 10. Missing / Ambiguous Data

- No ED registration time — admission may not have gone through ED.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
