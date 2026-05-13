# Encounter Report — HADM 29295881

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 29295881 |
| Subject ID | 10023239 |
| Patient Sex | F |
| Patient Anchor Age (at anchor year) | 29 |
| Anchor Year | 2137 |
| Admission Time | 2137-06-19 17:35:00 |
| Discharge Time | 2137-06-22 14:57:00 |
| Admission Type | EW EMER. |
| Admission Location | EMERGENCY ROOM |
| Discharge Location | HOME |
| Insurance | Other |
| Language | ENGLISH |
| Marital Status | SINGLE |
| Race/Ethnicity | WHITE |
| ED Registration | 2137-06-19 15:05:00 |
| ED Departure | 2137-06-19 19:09:00 |
| In-Hospital Mortality | No |
| Date of Death (overall) | N/A |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| HCFA | 919 | COMPLICATIONS OF TREATMENT W MCC | N/A | N/A |
| APR | 813 | OTHER COMPLICATIONS OF TREATMENT | 2.0 | 1.0 |

### Primary Diagnosis (seq_num = 1)

- **ICD-9 99657**: Mechanical complication due to insulin pump

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2137-06-19 17:36:14 | N/A | MED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-9 `99657`: Mechanical complication due to insulin pump
- (seq 2) ICD-9 `486`: Pneumonia, organism unspecified
- (seq 3) ICD-9 `7916`: Acetonuria
- (seq 4) ICD-9 `2449`: Unspecified acquired hypothyroidism
- (seq 5) ICD-9 `2720`: Pure hypercholesterolemia

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-9 | `99657` | Mechanical complication due to insulin pump |
| 2 | ICD-9 | `486` | Pneumonia, organism unspecified |
| 3 | ICD-9 | `7916` | Acetonuria |
| 4 | ICD-9 | `2449` | Unspecified acquired hypothyroidism |
| 5 | ICD-9 | `2720` | Pure hypercholesterolemia |
| 6 | ICD-9 | `30000` | Anxiety state, unspecified |
| 7 | ICD-9 | `2724` | Other and unspecified hyperlipidemia |
| 8 | ICD-9 | `28860` | Leukocytosis, unspecified |
| 9 | ICD-9 | `34590` | Epilepsy, unspecified, without mention of intractable epilepsy |
| 10 | ICD-9 | `0088` | Intestinal infection due to other organism, not elsewhere classified |
| 11 | ICD-9 | `V5867` | Long-term (current) use of insulin |
| 12 | ICD-9 | `E8798` | Other specified procedures as the cause of abnormal reaction of patient, or of later complication, without mention of misadventure at time of procedure |

## 5. ICU Stays

| Stay ID | First Care Unit | Last Care Unit | ICU Admit | ICU Discharge | LOS (days) |
|---|---|---|---|---|---|
| 33846653 | Medical/Surgical Intensive Care Unit (MICU/SICU) | Medical/Surgical Intensive Care Unit (MICU/SICU) | 2137-06-19 19:09:00 | 2137-06-22 14:57:32 | 2.83 |

## 6. Escalation / Severity Indicators

The following critical conditions or interventions were detected:

- **Pneumonia** (ICD diagnosis)

## 7. Procedures and Interventions

_No ICD-coded procedures recorded._

### ICU Procedure Events (from `icu/procedureevents.csv.gz`)

- 20 Gauge (category: Access Lines - Peripheral, started: 2137-06-19 19:30:00, status: FinishedRunning)
- 18 Gauge (category: Access Lines - Peripheral, started: 2137-06-19 19:30:00, status: FinishedRunning)

## 8. Critical Findings (Charted Events)

- **Dialysis patient** (first noted: 2137-06-19 20:14:00)

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2137-06-19 15:05:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2137-06-19 15:05:00 | Transfer | → Emergency Department (ED) |
| 2137-06-19 17:35:00 | Admission | Admitted from EMERGENCY ROOM (EW EMER.) |
| 2137-06-19 19:09:00 | ED Departure | Left Emergency Dept. |
| 2137-06-19 19:09:00 | ICU Admission | Medical/Surgical Intensive Care Unit (MICU/SICU) (LOS: 2.8 days) |
| 2137-06-22 14:57:00 | Discharge | To HOME |

## 10. Missing / Ambiguous Data

- No procedure ICD codes — procedures may not have been coded or were minor.

## 11. Manual Review Recommendation

**This encounter is flagged for manual review:**

- ICU stay present but no ICD procedures coded.
