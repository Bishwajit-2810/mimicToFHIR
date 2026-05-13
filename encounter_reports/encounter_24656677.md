# Encounter Report — HADM 24656677

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 24656677 |
| Subject ID | 10037928 |
| Patient Sex | F |
| Patient Anchor Age (at anchor year) | 78 |
| Anchor Year | 2175 |
| Admission Time | 2178-12-21 05:30:00 |
| Discharge Time | 2178-12-26 18:35:00 |
| Admission Type | EW EMER. |
| Admission Location | EMERGENCY ROOM |
| Discharge Location | HOME HEALTH CARE |
| Insurance | Medicare |
| Language | ? |
| Marital Status | WIDOWED |
| Race/Ethnicity | HISPANIC/LATINO - CUBAN |
| ED Registration | 2178-12-21 03:17:00 |
| ED Departure | 2178-12-21 08:27:00 |
| In-Hospital Mortality | No |
| Date of Death (overall) | N/A |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| APR | 420 | DIABETES | 2.0 | 2.0 |
| HCFA | 638 | DIABETES W CC | N/A | N/A |

### Primary Diagnosis (seq_num = 1)

- **ICD-9 25012**: Diabetes with ketoacidosis, type II or unspecified type, uncontrolled

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2178-12-21 05:30:41 | N/A | MED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-9 `25012`: Diabetes with ketoacidosis, type II or unspecified type, uncontrolled
- (seq 2) ICD-9 `5990`: Urinary tract infection, site not specified
- (seq 3) ICD-9 `5849`: Acute kidney failure, unspecified
- (seq 4) ICD-9 `V5867`: Long-term (current) use of insulin
- (seq 5) ICD-9 `04149`: Other and unspecified Escherichia coli [E. coli]

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-9 | `25012` | Diabetes with ketoacidosis, type II or unspecified type, uncontrolled |
| 2 | ICD-9 | `5990` | Urinary tract infection, site not specified |
| 3 | ICD-9 | `5849` | Acute kidney failure, unspecified |
| 4 | ICD-9 | `V5867` | Long-term (current) use of insulin |
| 5 | ICD-9 | `04149` | Other and unspecified Escherichia coli [E. coli] |
| 6 | ICD-9 | `7813` | Lack of coordination |
| 7 | ICD-9 | `V1588` | History of fall |
| 8 | ICD-9 | `78701` | Nausea with vomiting |
| 9 | ICD-9 | `4019` | Unspecified essential hypertension |
| 10 | ICD-9 | `2724` | Other and unspecified hyperlipidemia |
| 11 | ICD-9 | `311` | Depressive disorder, not elsewhere classified |
| 12 | ICD-9 | `30000` | Anxiety state, unspecified |
| 13 | ICD-9 | `53081` | Esophageal reflux |
| 14 | ICD-9 | `2809` | Iron deficiency anemia, unspecified |
| 15 | ICD-9 | `2989` | Unspecified psychosis |
| 16 | ICD-9 | `V1001` | Personal history of malignant neoplasm of tongue |
| 17 | ICD-9 | `78052` | Insomnia, unspecified |
| 18 | ICD-9 | `V1271` | Personal history of peptic ulcer disease |
| 19 | ICD-9 | `7260` | Adhesive capsulitis of shoulder |

## 5. ICU Stays

| Stay ID | First Care Unit | Last Care Unit | ICU Admit | ICU Discharge | LOS (days) |
|---|---|---|---|---|---|
| 39804682 | Medical/Surgical Intensive Care Unit (MICU/SICU) | Medical/Surgical Intensive Care Unit (MICU/SICU) | 2178-12-21 06:05:18 | 2178-12-22 02:16:08 | 0.84 |

## 6. Escalation / Severity Indicators

The following critical conditions or interventions were detected:

- **Acute Kidney Injury** (ICD diagnosis)

## 7. Procedures and Interventions

_No ICD-coded procedures recorded._

### ICU Procedure Events (from `icu/procedureevents.csv.gz`)

- 18 Gauge (category: Access Lines - Peripheral, started: 2178-12-21 09:26:00, status: FinishedRunning)
- 22 Gauge (category: Access Lines - Peripheral, started: 2178-12-21 09:27:00, status: FinishedRunning)

## 8. Critical Findings (Charted Events)

_No critical chart events detected._

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2178-12-21 03:17:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2178-12-21 03:17:00 | Transfer | → Emergency Department (ED) |
| 2178-12-21 05:30:00 | Admission | Admitted from EMERGENCY ROOM (EW EMER.) |
| 2178-12-21 05:32:19 | Transfer | → Discharge Lounge (transfer) |
| 2178-12-21 06:05:18 | ICU Admission | Medical/Surgical Intensive Care Unit (MICU/SICU) (LOS: 0.8 days) |
| 2178-12-21 06:05:18 | Transfer | → Medical/Surgical Intensive Care Unit (MICU/SICU) (transfer) |
| 2178-12-21 08:27:00 | ED Departure | Left Emergency Dept. |
| 2178-12-22 02:16:08 | Transfer | → Med/Surg/GYN (transfer) |
| 2178-12-26 18:35:00 | Discharge | To HOME HEALTH CARE |

## 10. Missing / Ambiguous Data

- No procedure ICD codes — procedures may not have been coded or were minor.

## 11. Manual Review Recommendation

**This encounter is flagged for manual review:**

- ICU stay present but no ICD procedures coded.
