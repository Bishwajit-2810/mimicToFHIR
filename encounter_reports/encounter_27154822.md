# Encounter Report — HADM 27154822

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 27154822 |
| Subject ID | 10021938 |
| Patient Sex | M |
| Patient Anchor Age (at anchor year) | 65 |
| Anchor Year | 2181 |
| Admission Time | 2181-10-25 10:44:00 |
| Discharge Time | 2181-10-27 15:30:00 |
| Admission Type | EW EMER. |
| Admission Location | EMERGENCY ROOM |
| Discharge Location | HOME |
| Insurance | Medicare |
| Language | ENGLISH |
| Marital Status | SINGLE |
| Race/Ethnicity | WHITE |
| ED Registration | 2181-10-25 09:23:00 |
| ED Departure | 2181-10-25 11:35:00 |
| In-Hospital Mortality | No |
| Date of Death (overall) | 2182-10-16 |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| APR | 425 | OTHER NON-HYPOVOLEMIC ELECTROLYTE DISORDERS | 3.0 | 2.0 |
| HCFA | 640 | MISC DISORDERS OF NUTRITION,METABOLISM,FLUIDS/ELECTROLYTES W MCC | N/A | N/A |

### Primary Diagnosis (seq_num = 1)

- **ICD-9 2767**: Hyperpotassemia

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2181-10-25 10:45:06 | N/A | MED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-9 `2767`: Hyperpotassemia
- (seq 2) ICD-9 `5856`: End stage renal disease
- (seq 3) ICD-9 `40391`: Hypertensive chronic kidney disease, unspecified, with chronic kidney disease stage V or end stage renal disease
- (seq 4) ICD-9 `42822`: Chronic systolic heart failure
- (seq 5) ICD-9 `4280`: Congestive heart failure, unspecified

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-9 | `2767` | Hyperpotassemia |
| 2 | ICD-9 | `5856` | End stage renal disease |
| 3 | ICD-9 | `40391` | Hypertensive chronic kidney disease, unspecified, with chronic kidney disease stage V or end stage renal disease |
| 4 | ICD-9 | `42822` | Chronic systolic heart failure |
| 5 | ICD-9 | `4280` | Congestive heart failure, unspecified |
| 6 | ICD-9 | `5781` | Blood in stool |
| 7 | ICD-9 | `587` | Renal sclerosis, unspecified |
| 8 | ICD-9 | `V4511` | Renal dialysis status |
| 9 | ICD-9 | `V4512` | Noncompliance with renal dialysis |
| 10 | ICD-9 | `78900` | Abdominal pain, unspecified site |
| 11 | ICD-9 | `2724` | Other and unspecified hyperlipidemia |
| 12 | ICD-9 | `30393` | Other and unspecified alcohol dependence, in remission |
| 13 | ICD-9 | `28521` | Anemia in chronic kidney disease |

## 5. ICU Stays

| Stay ID | First Care Unit | Last Care Unit | ICU Admit | ICU Discharge | LOS (days) |
|---|---|---|---|---|---|
| 33083787 | Medical Intensive Care Unit (MICU) | Medical Intensive Care Unit (MICU) | 2181-10-25 11:35:00 | 2181-10-26 20:53:57 | 1.39 |

## 6. Escalation / Severity Indicators

The following critical conditions or interventions were detected:

- **Renal Replacement Therapy / Dialysis** (ICU procedure event)

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2181-10-25 | ICD-9 | `3995` | Hemodialysis |

### ICU Procedure Events (from `icu/procedureevents.csv.gz`)

- 18 Gauge (category: Access Lines - Peripheral, started: 2181-10-25 12:56:00, status: FinishedRunning)
- 20 Gauge (category: Access Lines - Peripheral, started: 2181-10-25 12:57:00, status: FinishedRunning)
- Hemodialysis (category: 4-Procedures, started: 2181-10-25 13:30:00, status: FinishedRunning)

## 8. Critical Findings (Charted Events)

- **Code Status** (first noted: 2181-10-25 12:54:00)
- **Dialysis patient** (first noted: 2181-10-25 13:41:00)
- **Hemodialysis Output** (first noted: 2181-10-25 18:40:00)

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2181-10-25 09:23:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2181-10-25 09:23:00 | Transfer | → Emergency Department (ED) |
| 2181-10-25 10:44:00 | Admission | Admitted from EMERGENCY ROOM (EW EMER.) |
| 2181-10-25 11:35:00 | ED Departure | Left Emergency Dept. |
| 2181-10-25 11:35:00 | ICU Admission | Medical Intensive Care Unit (MICU) (LOS: 1.4 days) |
| 2181-10-26 20:53:57 | Transfer | → Medicine (transfer) |
| 2181-10-27 15:30:00 | Discharge | To HOME |

## 10. Missing / Ambiguous Data

- No obvious missing critical fields detected.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
