# Encounter Report — HADM 22490490

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 22490490 |
| Subject ID | 10037928 |
| Patient Sex | F |
| Patient Anchor Age (at anchor year) | 78 |
| Anchor Year | 2175 |
| Admission Time | 2177-07-14 16:55:00 |
| Discharge Time | 2177-07-24 13:33:00 |
| Admission Type | EW EMER. |
| Admission Location | EMERGENCY ROOM |
| Discharge Location | HOME HEALTH CARE |
| Insurance | Medicare |
| Language | ? |
| Marital Status | WIDOWED |
| Race/Ethnicity | HISPANIC/LATINO - CUBAN |
| ED Registration | 2177-07-14 14:52:00 |
| ED Departure | 2177-07-14 20:38:00 |
| In-Hospital Mortality | No |
| Date of Death (overall) | N/A |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| APR | 420 | DIABETES | 3.0 | 4.0 |
| HCFA | 638 | DIABETES W CC | N/A | N/A |

### Primary Diagnosis (seq_num = 1)

- **ICD-9 25022**: Diabetes with hyperosmolarity, type II or unspecified type, uncontrolled

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2177-07-14 16:56:05 | N/A | MED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-9 `25022`: Diabetes with hyperosmolarity, type II or unspecified type, uncontrolled
- (seq 2) ICD-9 `5849`: Acute kidney failure, unspecified
- (seq 3) ICD-9 `5990`: Urinary tract infection, site not specified
- (seq 4) ICD-9 `2762`: Acidosis
- (seq 5) ICD-9 `5789`: Hemorrhage of gastrointestinal tract, unspecified

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-9 | `25022` | Diabetes with hyperosmolarity, type II or unspecified type, uncontrolled |
| 2 | ICD-9 | `5849` | Acute kidney failure, unspecified |
| 3 | ICD-9 | `5990` | Urinary tract infection, site not specified |
| 4 | ICD-9 | `2762` | Acidosis |
| 5 | ICD-9 | `5789` | Hemorrhage of gastrointestinal tract, unspecified |
| 6 | ICD-9 | `V5867` | Long-term (current) use of insulin |
| 7 | ICD-9 | `2724` | Other and unspecified hyperlipidemia |
| 8 | ICD-9 | `V1581` | Personal history of noncompliance with medical treatment, presenting hazards to health |
| 9 | ICD-9 | `27652` | Hypovolemia |
| 10 | ICD-9 | `2809` | Iron deficiency anemia, unspecified |
| 11 | ICD-9 | `40390` | Hypertensive chronic kidney disease, unspecified, with chronic kidney disease stage I through stage IV, or unspecified |
| 12 | ICD-9 | `61650` | Ulceration of vulva, unspecified |
| 13 | ICD-9 | `6273` | Postmenopausal atrophic vaginitis |
| 14 | ICD-9 | `311` | Depressive disorder, not elsewhere classified |
| 15 | ICD-9 | `5853` | Chronic kidney disease, Stage III (moderate) |
| 16 | ICD-9 | `04149` | Other and unspecified Escherichia coli [E. coli] |
| 17 | ICD-9 | `1419` | Malignant neoplasm of tongue, unspecified |

## 5. ICU Stays

| Stay ID | First Care Unit | Last Care Unit | ICU Admit | ICU Discharge | LOS (days) |
|---|---|---|---|---|---|
| 31552399 | Medical/Surgical Intensive Care Unit (MICU/SICU) | Medical/Surgical Intensive Care Unit (MICU/SICU) | 2177-07-14 20:38:00 | 2177-07-15 16:08:36 | 0.81 |

## 6. Escalation / Severity Indicators

The following critical conditions or interventions were detected:

- **Acute Kidney Injury** (ICD diagnosis)

## 7. Procedures and Interventions

_No ICD-coded procedures recorded._

### ICU Procedure Events (from `icu/procedureevents.csv.gz`)

- 20 Gauge (category: Access Lines - Peripheral, started: 2177-07-14 21:06:00, status: FinishedRunning)
- 18 Gauge (category: Access Lines - Peripheral, started: 2177-07-14 21:06:00, status: FinishedRunning)

## 8. Critical Findings (Charted Events)

- **Dialysis patient** (first noted: 2177-07-15 01:19:00)

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2177-07-14 14:52:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2177-07-14 14:52:00 | Transfer | → Emergency Department (ED) |
| 2177-07-14 16:55:00 | Admission | Admitted from EMERGENCY ROOM (EW EMER.) |
| 2177-07-14 20:38:00 | ED Departure | Left Emergency Dept. |
| 2177-07-14 20:38:00 | ICU Admission | Medical/Surgical Intensive Care Unit (MICU/SICU) (LOS: 0.8 days) |
| 2177-07-15 16:08:36 | Transfer | → Medicine (transfer) |
| 2177-07-15 16:11:26 | Transfer | → Medicine (transfer) |
| 2177-07-24 13:33:00 | Discharge | To HOME HEALTH CARE |

## 10. Missing / Ambiguous Data

- No procedure ICD codes — procedures may not have been coded or were minor.

## 11. Manual Review Recommendation

**This encounter is flagged for manual review:**

- ICU stay present but no ICD procedures coded.
