# Encounter Report — HADM 28710730

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 28710730 |
| Subject ID | 10019568 |
| Patient Sex | F |
| Patient Anchor Age (at anchor year) | 59 |
| Anchor Year | 2120 |
| Admission Time | 2120-01-30 21:07:00 |
| Discharge Time | 2120-02-02 15:40:00 |
| Admission Type | EW EMER. |
| Admission Location | EMERGENCY ROOM |
| Discharge Location | HOME |
| Insurance | Medicare |
| Language | ENGLISH |
| Marital Status | SINGLE |
| Race/Ethnicity | WHITE |
| ED Registration | 2120-01-30 19:44:00 |
| ED Departure | 2120-01-30 22:51:00 |
| In-Hospital Mortality | No |
| Date of Death (overall) | N/A |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| HCFA | 184 | MAJOR CHEST TRAUMA W CC | N/A | N/A |
| APR | 135 | MAJOR CHEST & RESPIRATORY TRAUMA | 2.0 | 1.0 |

### Primary Diagnosis (seq_num = 1)

- **ICD-9 80707**: Closed fracture of seven ribs

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2120-01-30 21:08:27 | N/A | TRAUM |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-9 `80707`: Closed fracture of seven ribs
- (seq 2) ICD-9 `8600`: Traumatic pneumothorax without mention of open wound into thorax
- (seq 3) ICD-9 `E8809`: Accidental fall on or from other stairs or steps
- (seq 4) ICD-9 `E8490`: Home accidents
- (seq 5) ICD-9 `30500`: Alcohol abuse, unspecified

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-9 | `80707` | Closed fracture of seven ribs |
| 2 | ICD-9 | `8600` | Traumatic pneumothorax without mention of open wound into thorax |
| 3 | ICD-9 | `E8809` | Accidental fall on or from other stairs or steps |
| 4 | ICD-9 | `E8490` | Home accidents |
| 5 | ICD-9 | `30500` | Alcohol abuse, unspecified |
| 6 | ICD-9 | `4019` | Unspecified essential hypertension |

## 5. ICU Stays

| Stay ID | First Care Unit | Last Care Unit | ICU Admit | ICU Discharge | LOS (days) |
|---|---|---|---|---|---|
| 30876334 | Trauma SICU (TSICU) | Trauma SICU (TSICU) | 2120-01-30 22:51:00 | 2120-01-31 18:25:12 | 0.82 |

## 6. Escalation / Severity Indicators

_No escalation indicators detected from ICD codes or ICU procedure events._

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2120-01-30 | ICD-9 | `3404` | Insertion of intercostal catheter for drainage |

### ICU Procedure Events (from `icu/procedureevents.csv.gz`)

- 16 Gauge (category: Access Lines - Peripheral, started: 2120-01-30 23:07:00, status: FinishedRunning)
- 20 Gauge (category: Access Lines - Peripheral, started: 2120-01-30 23:09:00, status: FinishedRunning)
- 22 Gauge (category: Access Lines - Peripheral, started: 2120-01-31 09:27:00, status: FinishedRunning)

## 8. Critical Findings (Charted Events)

- **Seizure** (first noted: 2120-01-30 23:11:00)
- **Dialysis patient** (first noted: 2120-01-31 03:46:00)

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2120-01-30 19:44:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2120-01-30 19:44:00 | Transfer | → Emergency Department (ED) |
| 2120-01-30 21:07:00 | Admission | Admitted from EMERGENCY ROOM (EW EMER.) |
| 2120-01-30 22:51:00 | ED Departure | Left Emergency Dept. |
| 2120-01-30 22:51:00 | ICU Admission | Trauma SICU (TSICU) (LOS: 0.8 days) |
| 2120-01-31 18:25:12 | Transfer | → Med/Surg/Trauma (transfer) |
| 2120-02-02 15:40:00 | Discharge | To HOME |

## 10. Missing / Ambiguous Data

- No obvious missing critical fields detected.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
