# Encounter Report — HADM 26048429

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 26048429 |
| Subject ID | 10003046 |
| Patient Sex | M |
| Patient Anchor Age (at anchor year) | 64 |
| Anchor Year | 2154 |
| Admission Time | 2154-01-02 07:15:00 |
| Discharge Time | 2154-01-09 11:53:00 |
| Admission Type | SURGICAL SAME DAY ADMISSION |
| Admission Location | PHYSICIAN REFERRAL |
| Discharge Location | HOME HEALTH CARE |
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
| HCFA | 327 | STOMACH, ESOPHAGEAL & DUODENAL PROC W CC | N/A | N/A |
| APR | 220 | MAJOR STOMACH, ESOPHAGEAL & DUODENAL PROCEDURES | 3.0 | 2.0 |

### Primary Diagnosis (seq_num = 1)

- **ICD-9 1505**: Malignant neoplasm of lower third of esophagus

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2154-01-02 00:15:52 | N/A | TSURG |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-9 `1505`: Malignant neoplasm of lower third of esophagus
- (seq 2) ICD-9 `2762`: Acidosis
- (seq 3) ICD-9 `53085`: Barrett's esophagus
- (seq 4) ICD-9 `53081`: Esophageal reflux

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-9 | `1505` | Malignant neoplasm of lower third of esophagus |
| 2 | ICD-9 | `2762` | Acidosis |
| 3 | ICD-9 | `53085` | Barrett's esophagus |
| 4 | ICD-9 | `53081` | Esophageal reflux |

## 5. ICU Stays

| Stay ID | First Care Unit | Last Care Unit | ICU Admit | ICU Discharge | LOS (days) |
|---|---|---|---|---|---|
| 35514836 | Trauma SICU (TSICU) | Trauma SICU (TSICU) | 2154-01-02 15:57:15 | 2154-01-04 15:19:56 | 1.97 |

## 6. Escalation / Severity Indicators

The following critical conditions or interventions were detected:

- **Arterial Line** (ICU procedure event)

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2154-01-02 | ICD-9 | `4242` | Total esophagectomy |
| 2 | 2154-01-03 | ICD-9 | `4639` | Other enterostomy |
| 3 | 2154-01-03 | ICD-9 | `966` | Enteral infusion of concentrated nutritional substances |

### ICU Procedure Events (from `icu/procedureevents.csv.gz`)

- OR Received (category: 3-Significant Events, started: 2154-01-02 16:18:00, status: FinishedRunning)
- Nasal Swab (category: 6-Cultures, started: 2154-01-02 16:19:00, status: FinishedRunning)
- 16 Gauge (category: Access Lines - Peripheral, started: 2154-01-02 16:27:00, status: FinishedRunning)
- Chest X-Ray (category: 5-Imaging, started: 2154-01-02 16:35:00, status: FinishedRunning)
- 20 Gauge (category: Access Lines - Peripheral, started: 2154-01-02 22:00:00, status: FinishedRunning)
- Arterial Line (category: Access Lines - Invasive, started: 2154-01-03 17:32:00, status: FinishedRunning)

## 8. Critical Findings (Charted Events)

- **Code Status** (first noted: 2154-01-02 16:18:00)
- **Dialysis patient** (first noted: 2154-01-02 17:29:00)

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2154-01-02 07:15:00 | Admission | Admitted from PHYSICIAN REFERRAL (SURGICAL SAME DAY ADMISSION) |
| 2154-01-02 15:57:15 | ICU Admission | Trauma SICU (TSICU) (LOS: 2.0 days) |
| 2154-01-02 15:57:15 | Transfer | → Trauma SICU (TSICU) (transfer) |
| 2154-01-04 15:19:56 | Transfer | → Med/Surg (transfer) |
| 2154-01-09 11:53:00 | Discharge | To HOME HEALTH CARE |

## 10. Missing / Ambiguous Data

- No ED registration time — admission may not have gone through ED.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
