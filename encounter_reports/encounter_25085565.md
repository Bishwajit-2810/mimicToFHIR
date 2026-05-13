# Encounter Report — HADM 25085565

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 25085565 |
| Subject ID | 10015860 |
| Patient Sex | M |
| Patient Anchor Age (at anchor year) | 53 |
| Anchor Year | 2186 |
| Admission Time | 2186-09-15 16:12:00 |
| Discharge Time | 2186-09-29 18:05:00 |
| Admission Type | EW EMER. |
| Admission Location | EMERGENCY ROOM |
| Discharge Location | REHAB |
| Insurance | Other |
| Language | ENGLISH |
| Marital Status | SINGLE |
| Race/Ethnicity | WHITE |
| ED Registration | 2186-09-15 12:56:00 |
| ED Departure | 2186-09-15 17:15:00 |
| In-Hospital Mortality | No |
| Date of Death (overall) | N/A |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| APR | 710 | INFECTIOUS & PARASITIC DISEASES INCLUDING HIV W O.R. PROCEDURE | 3.0 | 2.0 |
| HCFA | 853 | INFECTIOUS & PARASITIC DISEASES W O.R. PROCEDURE W MCC | N/A | N/A |

### Primary Diagnosis (seq_num = 1)

- **ICD-9 0380**: Streptococcal septicemia

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2186-09-15 16:13:33 | N/A | CMED |
| 2186-09-15 16:13:57 | CMED | MED |
| 2186-09-16 11:18:20 | MED | SURG |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-9 `0380`: Streptococcal septicemia
- (seq 2) ICD-9 `25012`: Diabetes with ketoacidosis, type II or unspecified type, uncontrolled
- (seq 3) ICD-9 `6827`: Cellulitis and abscess of foot, except toes
- (seq 4) ICD-9 `6826`: Cellulitis and abscess of leg, except foot
- (seq 5) ICD-9 `2761`: Hyposmolality and/or hyponatremia

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-9 | `0380` | Streptococcal septicemia |
| 2 | ICD-9 | `25012` | Diabetes with ketoacidosis, type II or unspecified type, uncontrolled |
| 3 | ICD-9 | `6827` | Cellulitis and abscess of foot, except toes |
| 4 | ICD-9 | `6826` | Cellulitis and abscess of leg, except foot |
| 5 | ICD-9 | `2761` | Hyposmolality and/or hyponatremia |
| 6 | ICD-9 | `70715` | Ulcer of other part of foot |
| 7 | ICD-9 | `25062` | Diabetes with neurological manifestations, type II or unspecified type, uncontrolled |
| 8 | ICD-9 | `99591` | Sepsis |
| 9 | ICD-9 | `28529` | Anemia of other chronic disease |
| 10 | ICD-9 | `3572` | Polyneuropathy in diabetes |
| 11 | ICD-9 | `311` | Depressive disorder, not elsewhere classified |
| 12 | ICD-9 | `4019` | Unspecified essential hypertension |
| 13 | ICD-9 | `2720` | Pure hypercholesterolemia |
| 14 | ICD-9 | `1123` | Candidiasis of skin and nails |
| 15 | ICD-9 | `6929` | Contact dermatitis and other eczema, unspecified cause |
| 16 | ICD-9 | `V707` | Examination of participant in clinical trial |

## 5. ICU Stays

| Stay ID | First Care Unit | Last Care Unit | ICU Admit | ICU Discharge | LOS (days) |
|---|---|---|---|---|---|
| 32496174 | Medical Intensive Care Unit (MICU) | Medical Intensive Care Unit (MICU) | 2186-09-15 17:15:00 | 2186-09-16 11:17:40 | 0.75 |

## 6. Escalation / Severity Indicators

The following critical conditions or interventions were detected:

- **Sepsis** (ICD diagnosis)

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2186-09-23 | ICD-9 | `8669` | Other skin graft to other sites |
| 2 | 2186-09-23 | ICD-9 | `8344` | Other fasciectomy |
| 3 | 2186-09-15 | ICD-9 | `8604` | Other incision with drainage of skin and subcutaneous tissue |
| 4 | 2186-09-16 | ICD-9 | `8604` | Other incision with drainage of skin and subcutaneous tissue |
| 5 | 2186-09-18 | ICD-9 | `8604` | Other incision with drainage of skin and subcutaneous tissue |
| 6 | 2186-09-25 | ICD-9 | `3897` | Central venous catheter placement with guidance |

### ICU Procedure Events (from `icu/procedureevents.csv.gz`)

- 18 Gauge (category: Access Lines - Peripheral, started: 2186-09-15 18:38:00, status: FinishedRunning)
- 20 Gauge (category: Access Lines - Peripheral, started: 2186-09-15 21:28:00, status: FinishedRunning)
- OR Sent (category: 3-Significant Events, started: 2186-09-16 09:40:00, status: FinishedRunning)

## 8. Critical Findings (Charted Events)

- **Code Status** (first noted: 2186-09-15 21:22:00)
- **Dialysis patient** (first noted: 2186-09-15 19:06:00)

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2186-09-15 12:56:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2186-09-15 12:56:00 | Transfer | → Emergency Department (ED) |
| 2186-09-15 16:12:00 | Admission | Admitted from EMERGENCY ROOM (EW EMER.) |
| 2186-09-15 17:15:00 | ED Departure | Left Emergency Dept. |
| 2186-09-15 17:15:00 | ICU Admission | Medical Intensive Care Unit (MICU) (LOS: 0.8 days) |
| 2186-09-16 11:17:40 | Transfer | → PACU (transfer) |
| 2186-09-16 14:45:34 | Transfer | → Vascular (transfer) |
| 2186-09-29 18:05:00 | Discharge | To REHAB |

## 10. Missing / Ambiguous Data

- No obvious missing critical fields detected.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
