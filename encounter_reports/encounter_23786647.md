# Encounter Report — HADM 23786647

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 23786647 |
| Subject ID | 10018328 |
| Patient Sex | F |
| Patient Anchor Age (at anchor year) | 83 |
| Anchor Year | 2154 |
| Admission Time | 2154-04-24 03:15:00 |
| Discharge Time | 2154-05-03 14:00:00 |
| Admission Type | SURGICAL SAME DAY ADMISSION |
| Admission Location | PHYSICIAN REFERRAL |
| Discharge Location | HOME HEALTH CARE |
| Insurance | Other |
| Language | ENGLISH |
| Marital Status | DIVORCED |
| Race/Ethnicity | WHITE |
| ED Registration | N/A |
| ED Departure | N/A |
| In-Hospital Mortality | No |
| Date of Death (overall) | N/A |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| APR | 24 | EXTRACRANIAL VASCULAR PROCEDURES | 2.0 | 2.0 |
| HCFA | 25 | CRANIOTOMY & ENDOVASCULAR INTRACRANIAL PROCEDURES W MCC | N/A | N/A |

### Primary Diagnosis (seq_num = 1)

- **ICD-10 I671**: Cerebral aneurysm, nonruptured

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2154-04-24 03:16:00 | N/A | NSURG |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-10 `I671`: Cerebral aneurysm, nonruptured
- (seq 2) ICD-10 `G936`: Cerebral edema
- (seq 3) ICD-10 `I5031`: Acute diastolic (congestive) heart failure
- (seq 4) ICD-10 `R4701`: Aphasia
- (seq 5) ICD-10 `D62`: Acute posthemorrhagic anemia

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-10 | `I671` | Cerebral aneurysm, nonruptured |
| 2 | ICD-10 | `G936` | Cerebral edema |
| 3 | ICD-10 | `I5031` | Acute diastolic (congestive) heart failure |
| 4 | ICD-10 | `R4701` | Aphasia |
| 5 | ICD-10 | `D62` | Acute posthemorrhagic anemia |
| 6 | ICD-10 | `I97618` | Postprocedural hemorrhage of a circulatory system organ or structure following other circulatory system procedure |
| 7 | ICD-10 | `J942` | Hemothorax |
| 8 | ICD-10 | `I97131` | Postprocedural heart failure following other surgery |
| 9 | ICD-10 | `I9752` | Accidental puncture and laceration of a circulatory system organ or structure during other procedure |
| 10 | ICD-10 | `I10` | Essential (primary) hypertension |
| 11 | ICD-10 | `Z853` | Personal history of malignant neoplasm of breast |
| 12 | ICD-10 | `E785` | Hyperlipidemia, unspecified |
| 13 | ICD-10 | `I9581` | Postprocedural hypotension |
| 14 | ICD-10 | `R079` | Chest pain, unspecified |
| 15 | ICD-10 | `Y834` | Other reconstructive surgery as the cause of abnormal reaction of the patient, or of later complication, without mention of misadventure at the time of the procedure |
| 16 | ICD-10 | `Y92230` | Patient room in hospital as the place of occurrence of the external cause |

## 5. ICU Stays

| Stay ID | First Care Unit | Last Care Unit | ICU Admit | ICU Discharge | LOS (days) |
|---|---|---|---|---|---|
| 31269608 | Neuro Stepdown | Neuro Stepdown | 2154-04-24 23:03:44 | 2154-05-02 15:55:21 | 7.70 |

## 6. Escalation / Severity Indicators

The following critical conditions or interventions were detected:

- **Arterial Line** (ICU procedure event)

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2154-04-24 | ICD-10 | `03VG3DZ` | Restriction of Intracranial Artery with Intraluminal Device, Percutaneous Approach |
| 2 | 2154-04-24 | ICD-10 | `03VL3DZ` | Restriction of Left Internal Carotid Artery with Intraluminal Device, Percutaneous Approach |

### ICU Procedure Events (from `icu/procedureevents.csv.gz`)

- Arterial Line (category: Access Lines - Invasive, started: 2154-04-24 23:11:00, status: FinishedRunning)
- Foley Catheter (category: GI/GU, started: 2154-04-24 23:39:00, status: FinishedRunning)
- Chest X-Ray (category: 5-Imaging, started: 2154-04-25 11:30:00, status: FinishedRunning)
- Transthoracic Echo (category: 5-Imaging, started: 2154-04-25 13:00:00, status: FinishedRunning)
- CT scan (category: 5-Imaging, started: 2154-04-26 01:15:00, status: FinishedRunning)
- 20 Gauge (category: Access Lines - Peripheral, started: 2154-04-26 07:30:00, status: FinishedRunning)
- EKG (category: 4-Procedures, started: 2154-04-27 08:03:00, status: FinishedRunning)
- 22 Gauge (category: Access Lines - Peripheral, started: 2154-04-30 13:25:00, status: FinishedRunning)

## 8. Critical Findings (Charted Events)

_No critical chart events detected._

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2154-04-24 03:15:00 | Admission | Admitted from PHYSICIAN REFERRAL (SURGICAL SAME DAY ADMISSION) |
| 2154-04-24 22:11:37 | Transfer | → PACU (transfer) |
| 2154-04-24 23:03:44 | ICU Admission | Neuro Stepdown (LOS: 7.7 days) |
| 2154-04-24 23:03:44 | Transfer | → Neuro Stepdown (transfer) |
| 2154-04-26 05:53:13 | Transfer | → Trauma SICU (TSICU) (transfer) |
| 2154-04-28 21:51:32 | Transfer | → Neuro Stepdown (transfer) |
| 2154-05-02 15:55:21 | Transfer | → Neurology (transfer) |
| 2154-05-03 14:00:00 | Discharge | To HOME HEALTH CARE |

## 10. Missing / Ambiguous Data

- No ED registration time — admission may not have gone through ED.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
