# Encounter Report — HADM 27417763

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 27417763 |
| Subject ID | 10017492 |
| Patient Sex | M |
| Patient Anchor Age (at anchor year) | 84 |
| Anchor Year | 2114 |
| Admission Time | 2116-06-26 18:25:00 |
| Discharge Time | 2116-07-05 08:05:00 |
| Admission Type | EW EMER. |
| Admission Location | EMERGENCY ROOM |
| Discharge Location | DIED |
| Insurance | Medicaid |
| Language | ? |
| Marital Status | SINGLE |
| Race/Ethnicity | PATIENT DECLINED TO ANSWER |
| ED Registration | 2116-06-26 14:29:00 |
| ED Departure | 2116-06-26 21:46:00 |
| In-Hospital Mortality | YES — Death time: 2116-07-05 08:05:00 |
| Date of Death (overall) | 2116-07-05 |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| APR | 308 | HIP & FEMUR FRACTURE REPAIR | 4.0 | 4.0 |
| HCFA | 480 | HIP & FEMUR PROCEDURES EXCEPT MAJOR JOINT W MCC | N/A | N/A |

### Primary Diagnosis (seq_num = 1)

- **ICD-9 82021**: Closed fracture of intertrochanteric section of neck of femur

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2116-06-26 18:26:30 | N/A | TRAUM |
| 2116-06-27 18:28:12 | TRAUM | ORTHO |
| 2116-07-03 22:00:43 | ORTHO | MED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-9 `82021`: Closed fracture of intertrochanteric section of neck of femur
- (seq 2) ICD-9 `5849`: Acute kidney failure, unspecified
- (seq 3) ICD-9 `431`: Intracerebral hemorrhage
- (seq 4) ICD-9 `34830`: Encephalopathy, unspecified
- (seq 5) ICD-9 `2760`: Hyperosmolality and/or hypernatremia

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-9 | `82021` | Closed fracture of intertrochanteric section of neck of femur |
| 2 | ICD-9 | `5849` | Acute kidney failure, unspecified |
| 3 | ICD-9 | `431` | Intracerebral hemorrhage |
| 4 | ICD-9 | `34830` | Encephalopathy, unspecified |
| 5 | ICD-9 | `2760` | Hyperosmolality and/or hypernatremia |
| 6 | ICD-9 | `5990` | Urinary tract infection, site not specified |
| 7 | ICD-9 | `43820` | Late effects of cerebrovascular disease, hemiplegia affecting unspecified side |
| 8 | ICD-9 | `43811` | Late effects of cerebrovascular disease, aphasia |
| 9 | ICD-9 | `43889` | Other late effects of cerebrovascular disease |
| 10 | ICD-9 | `78830` | Urinary incontinence, unspecified |
| 11 | ICD-9 | `4380` | Late effects of cerebrovascular disease, cognitive deficits |
| 12 | ICD-9 | `E8889` | Unspecified fall |
| 13 | ICD-9 | `4019` | Unspecified essential hypertension |
| 14 | ICD-9 | `2724` | Other and unspecified hyperlipidemia |
| 15 | ICD-9 | `V1046` | Personal history of malignant neoplasm of prostate |
| 16 | ICD-9 | `V4986` | Do not resuscitate status |
| 17 | ICD-9 | `2809` | Iron deficiency anemia, unspecified |
| 18 | ICD-9 | `78820` | Retention of urine, unspecified |
| 19 | ICD-9 | `E9352` | Other opiates and related narcotics causing adverse effects in therapeutic use |
| 20 | ICD-9 | `79902` | Hypoxemia |
| 21 | ICD-9 | `78701` | Nausea with vomiting |

## 5. ICU Stays

| Stay ID | First Care Unit | Last Care Unit | ICU Admit | ICU Discharge | LOS (days) |
|---|---|---|---|---|---|
| 39543480 | Trauma SICU (TSICU) | Trauma SICU (TSICU) | 2116-06-26 20:35:09 | 2116-06-27 15:44:27 | 0.80 |
| 36035031 | Trauma SICU (TSICU) | Trauma SICU (TSICU) | 2116-06-27 17:35:34 | 2116-06-27 20:26:18 | 0.12 |
| 36871784 | Coronary Care Unit (CCU) | Coronary Care Unit (CCU) | 2116-07-05 06:50:16 | 2116-07-05 13:06:59 | 0.26 |

## 6. Escalation / Severity Indicators

The following critical conditions or interventions were detected:

- **Acute Kidney Injury** (ICD diagnosis)

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2116-06-27 | ICD-9 | `7915` | Closed reduction of fracture with internal fixation, femur |

### ICU Procedure Events (from `icu/procedureevents.csv.gz`)

- 20 Gauge (category: Access Lines - Peripheral, started: 2116-06-26 21:52:00, status: FinishedRunning)
- Urine Culture (category: 6-Cultures, started: 2116-06-26 23:39:00, status: FinishedRunning)
- Nasal Swab (category: 6-Cultures, started: 2116-06-26 23:39:00, status: FinishedRunning)
- OR Sent (category: 3-Significant Events, started: 2116-06-27 15:30:00, status: FinishedRunning)
- 18 Gauge (category: Access Lines - Peripheral, started: 2116-06-27 17:30:00, status: FinishedRunning)
- OR Received (category: 3-Significant Events, started: 2116-06-27 17:30:00, status: FinishedRunning)

## 8. Critical Findings (Charted Events)

- **Code Status.** (first noted: 2116-06-27 06:46:00)
- **Dialysis patient** (first noted: 2116-06-27 03:03:00)

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2116-06-26 14:29:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2116-06-26 14:29:00 | Transfer | → Emergency Department (ED) |
| 2116-06-26 18:25:00 | Admission | Admitted from EMERGENCY ROOM (EW EMER.) |
| 2116-06-26 20:11:07 | Transfer | → Emergency Department Observation (transfer) |
| 2116-06-26 20:35:09 | ICU Admission | Trauma SICU (TSICU) (LOS: 0.8 days) |
| 2116-06-26 20:35:09 | Transfer | → Trauma SICU (TSICU) (transfer) |
| 2116-06-26 21:46:00 | ED Departure | Left Emergency Dept. |
| 2116-06-27 15:44:27 | Transfer | → PACU (transfer) |
| 2116-06-27 17:35:34 | ICU Admission | Trauma SICU (TSICU) (LOS: 0.1 days) |
| 2116-06-27 17:35:34 | Transfer | → Trauma SICU (TSICU) (transfer) |
| 2116-06-27 20:26:18 | Transfer | → Med/Surg/Trauma (transfer) |
| 2116-06-28 23:10:53 | Transfer | → Med/Surg/Trauma (transfer) |
| 2116-07-05 06:50:16 | ICU Admission | Coronary Care Unit (CCU) (LOS: 0.3 days) |
| 2116-07-05 06:50:16 | Transfer | → Coronary Care Unit (CCU) (transfer) |
| 2116-07-05 08:05:00 | **IN-HOSPITAL DEATH** | |
| 2116-07-05 08:05:00 | Discharge | To DIED |

## 10. Missing / Ambiguous Data

- No obvious missing critical fields detected.

## 11. Manual Review Recommendation

**This encounter is flagged for manual review:**

- Patient expired in-hospital but cause of death not clearly coded.
