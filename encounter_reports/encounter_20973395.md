# Encounter Report — HADM 20973395

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 20973395 |
| Subject ID | 10016810 |
| Patient Sex | F |
| Patient Anchor Age (at anchor year) | 66 |
| Anchor Year | 2185 |
| Admission Time | 2185-06-16 01:31:00 |
| Discharge Time | 2185-06-21 15:55:00 |
| Admission Type | EW EMER. |
| Admission Location | EMERGENCY ROOM |
| Discharge Location | HOME |
| Insurance | Other |
| Language | ENGLISH |
| Marital Status | N/A |
| Race/Ethnicity | UNKNOWN |
| ED Registration | 2185-06-15 23:08:00 |
| ED Departure | 2185-06-16 02:16:00 |
| In-Hospital Mortality | No |
| Date of Death (overall) | N/A |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| HCFA | 331 | MAJOR SMALL & LARGE BOWEL PROCEDURES W/O CC/MCC | N/A | N/A |

### Primary Diagnosis (seq_num = 1)

- **ICD-9 5400**: Acute appendicitis with generalized peritonitis

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2185-06-16 01:31:44 | N/A | SURG |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-9 `5400`: Acute appendicitis with generalized peritonitis
- (seq 2) ICD-9 `4589`: Hypotension, unspecified
- (seq 3) ICD-9 `2449`: Unspecified acquired hypothyroidism
- (seq 4) ICD-9 `2720`: Pure hypercholesterolemia
- (seq 5) ICD-9 `4019`: Unspecified essential hypertension

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-9 | `5400` | Acute appendicitis with generalized peritonitis |
| 2 | ICD-9 | `4589` | Hypotension, unspecified |
| 3 | ICD-9 | `2449` | Unspecified acquired hypothyroidism |
| 4 | ICD-9 | `2720` | Pure hypercholesterolemia |
| 5 | ICD-9 | `4019` | Unspecified essential hypertension |
| 6 | ICD-9 | `25000` | Diabetes mellitus without mention of complication, type II or unspecified type, not stated as uncontrolled |
| 7 | ICD-9 | `3051` | Tobacco use disorder |
| 8 | ICD-9 | `V5866` | Long-term (current) use of aspirin |
| 9 | ICD-9 | `V1082` | Personal history of malignant melanoma of skin |
| 10 | ICD-9 | `V4577` | Acquired absence of organ, genital organs |

## 5. ICU Stays

| Stay ID | First Care Unit | Last Care Unit | ICU Admit | ICU Discharge | LOS (days) |
|---|---|---|---|---|---|
| 35436337 | Surgical Intensive Care Unit (SICU) | Surgical Intensive Care Unit (SICU) | 2185-06-16 02:16:00 | 2185-06-18 14:00:02 | 2.49 |

## 6. Escalation / Severity Indicators

The following critical conditions or interventions were detected:

- **Arterial Line** (ICU procedure event)

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2185-06-16 | ICD-9 | `4709` | Other appendectomy |
| 2 | 2185-06-16 | ICD-9 | `4572` | Open and other cecectomy |

### ICU Procedure Events (from `icu/procedureevents.csv.gz`)

- 20 Gauge (category: Access Lines - Peripheral, started: 2185-06-16 03:01:00, status: FinishedRunning)
- EKG (category: 4-Procedures, started: 2185-06-16 08:22:00, status: FinishedRunning)
- OR Sent (category: 3-Significant Events, started: 2185-06-16 22:40:00, status: FinishedRunning)
- OR Received (category: 3-Significant Events, started: 2185-06-17 00:45:00, status: FinishedRunning)
- 18 Gauge (category: Access Lines - Peripheral, started: 2185-06-17 01:35:00, status: FinishedRunning)
- Arterial Line (category: Access Lines - Invasive, started: 2185-06-17 01:35:00, status: FinishedRunning)
- 22 Gauge (category: Access Lines - Peripheral, started: 2185-06-18 12:00:00, status: FinishedRunning)

## 8. Critical Findings (Charted Events)

_No critical chart events detected._

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2185-06-15 23:08:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2185-06-15 23:08:00 | Transfer | → Emergency Department (ED) |
| 2185-06-16 01:31:00 | Admission | Admitted from EMERGENCY ROOM (EW EMER.) |
| 2185-06-16 02:16:00 | ED Departure | Left Emergency Dept. |
| 2185-06-16 02:16:00 | ICU Admission | Surgical Intensive Care Unit (SICU) (LOS: 2.5 days) |
| 2185-06-18 14:00:02 | Transfer | → Med/Surg/Trauma (transfer) |
| 2185-06-21 15:55:00 | Discharge | To HOME |

## 10. Missing / Ambiguous Data

- No obvious missing critical fields detected.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
