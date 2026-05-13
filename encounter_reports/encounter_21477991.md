# Encounter Report — HADM 21477991

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 21477991 |
| Subject ID | 10027602 |
| Patient Sex | F |
| Patient Anchor Age (at anchor year) | 71 |
| Anchor Year | 2201 |
| Admission Time | 2201-12-11 12:00:00 |
| Discharge Time | 2201-12-17 13:45:00 |
| Admission Type | SURGICAL SAME DAY ADMISSION |
| Admission Location | PHYSICIAN REFERRAL |
| Discharge Location | REHAB |
| Insurance | Other |
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
| APR | 21 | CRANIOTOMY EXCEPT FOR TRAUMA | 2.0 | 1.0 |
| HCFA | 26 | CRANIOTOMY & ENDOVASCULAR INTRACRANIAL PROCEDURES W CC | N/A | N/A |

### Primary Diagnosis (seq_num = 1)

- **ICD-9 4373**: Cerebral aneurysm, nonruptured

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2201-12-11 03:04:13 | N/A | NSURG |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-9 `4373`: Cerebral aneurysm, nonruptured
- (seq 2) ICD-9 `2930`: Delirium due to conditions classified elsewhere
- (seq 3) ICD-9 `51889`: Other diseases of lung, not elsewhere classified
- (seq 4) ICD-9 `V441`: Gastrostomy status
- (seq 5) ICD-9 `78720`: Dysphagia, unspecified

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-9 | `4373` | Cerebral aneurysm, nonruptured |
| 2 | ICD-9 | `2930` | Delirium due to conditions classified elsewhere |
| 3 | ICD-9 | `51889` | Other diseases of lung, not elsewhere classified |
| 4 | ICD-9 | `V441` | Gastrostomy status |
| 5 | ICD-9 | `78720` | Dysphagia, unspecified |
| 6 | ICD-9 | `31401` | Attention deficit disorder with hyperactivity |
| 7 | ICD-9 | `V4987` | Physical restraints status |
| 8 | ICD-9 | `V5861` | Long-term (current) use of anticoagulants |
| 9 | ICD-9 | `2449` | Unspecified acquired hypothyroidism |
| 10 | ICD-9 | `4019` | Unspecified essential hypertension |

## 5. ICU Stays

| Stay ID | First Care Unit | Last Care Unit | ICU Admit | ICU Discharge | LOS (days) |
|---|---|---|---|---|---|
| 32453351 | Surgical Intensive Care Unit (SICU) | Surgical Intensive Care Unit (SICU) | 2201-12-11 20:11:52 | 2201-12-13 18:29:00 | 1.93 |

## 6. Escalation / Severity Indicators

The following critical conditions or interventions were detected:

- **Arterial Line** (ICU procedure event)

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2201-12-11 | ICD-9 | `0159` | Other excision or destruction of lesion or tissue of brain |
| 2 | 2201-12-11 | ICD-9 | `8841` | Arteriography of cerebral arteries |
| 3 | 2201-12-11 | ICD-9 | `9359` | Other immobilization, pressure, and attention to wound |
| 4 | 2201-12-12 | ICD-9 | `966` | Enteral infusion of concentrated nutritional substances |

### ICU Procedure Events (from `icu/procedureevents.csv.gz`)

- Arterial Line (category: Access Lines - Invasive, started: 2201-12-11 22:11:00, status: FinishedRunning)
- Multi Lumen (category: Access Lines - Invasive, started: 2201-12-11 22:12:00, status: FinishedRunning)
- 18 Gauge (category: Access Lines - Peripheral, started: 2201-12-11 22:19:00, status: FinishedRunning)
- Chest X-Ray (category: 5-Imaging, started: 2201-12-12 10:00:00, status: FinishedRunning)
- CT scan (category: 5-Imaging, started: 2201-12-12 14:00:00, status: FinishedRunning)

## 8. Critical Findings (Charted Events)

_No critical chart events detected._

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2201-12-11 12:00:00 | Admission | Admitted from PHYSICIAN REFERRAL (SURGICAL SAME DAY ADMISSION) |
| 2201-12-11 20:11:52 | ICU Admission | Surgical Intensive Care Unit (SICU) (LOS: 1.9 days) |
| 2201-12-11 20:11:52 | Transfer | → Surgical Intensive Care Unit (SICU) (transfer) |
| 2201-12-13 18:29:00 | Transfer | → Neurology (transfer) |
| 2201-12-13 18:46:17 | Transfer | → Neurology (transfer) |
| 2201-12-17 13:45:00 | Discharge | To REHAB |

## 10. Missing / Ambiguous Data

- No ED registration time — admission may not have gone through ED.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
