# Encounter Report — HADM 21457723

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 21457723 |
| Subject ID | 10019003 |
| Patient Sex | F |
| Patient Anchor Age (at anchor year) | 65 |
| Anchor Year | 2148 |
| Admission Time | 2155-07-10 17:48:00 |
| Discharge Time | 2155-07-18 16:59:00 |
| Admission Type | EW EMER. |
| Admission Location | TRANSFER FROM HOSPITAL |
| Discharge Location | HOME |
| Insurance | Other |
| Language | ENGLISH |
| Marital Status | WIDOWED |
| Race/Ethnicity | WHITE |
| ED Registration | 2155-07-10 12:46:00 |
| ED Departure | 2155-07-10 19:03:00 |
| In-Hospital Mortality | No |
| Date of Death (overall) | 2155-12-03 |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| HCFA | 809 | MAJOR HEMATOL/IMMUN DIAG EXC SICKLE CELL CRISIS & COAGUL W CC | N/A | N/A |
| APR | 660 | MAJOR HEMATOLOGIC/IMMUNOLOGIC DIAG EXC SICKLE CELL CRISIS & COAGUL | 3.0 | 3.0 |

### Primary Diagnosis (seq_num = 1)

- **ICD-10 D61818**: Other pancytopenia

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2155-07-10 17:48:57 | N/A | OMED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-10 `D61818`: Other pancytopenia
- (seq 2) ICD-10 `I5032`: Chronic diastolic (congestive) heart failure
- (seq 3) ICD-10 `E872`: Acidosis
- (seq 4) ICD-10 `D689`: Coagulation defect, unspecified
- (seq 5) ICD-10 `D599`: Acquired hemolytic anemia, unspecified

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-10 | `D61818` | Other pancytopenia |
| 2 | ICD-10 | `I5032` | Chronic diastolic (congestive) heart failure |
| 3 | ICD-10 | `E872` | Acidosis |
| 4 | ICD-10 | `D689` | Coagulation defect, unspecified |
| 5 | ICD-10 | `D599` | Acquired hemolytic anemia, unspecified |
| 6 | ICD-10 | `D46Z` | Other myelodysplastic syndromes |
| 7 | ICD-10 | `R823` | Hemoglobinuria |
| 8 | ICD-10 | `R319` | Hematuria, unspecified |
| 9 | ICD-10 | `Z86718` | Personal history of other venous thrombosis and embolism |
| 10 | ICD-10 | `Z853` | Personal history of malignant neoplasm of breast |
| 11 | ICD-10 | `Z87891` | Personal history of nicotine dependence |
| 12 | ICD-10 | `I110` | Hypertensive heart disease with heart failure |
| 13 | ICD-10 | `J449` | Chronic obstructive pulmonary disease, unspecified |
| 14 | ICD-10 | `E119` | Type 2 diabetes mellitus without complications |
| 15 | ICD-10 | `E039` | Hypothyroidism, unspecified |
| 16 | ICD-10 | `E7800` | Pure hypercholesterolemia, unspecified |
| 17 | ICD-10 | `F329` | Major depressive disorder, single episode, unspecified |
| 18 | ICD-10 | `K7581` | Nonalcoholic steatohepatitis (NASH) |
| 19 | ICD-10 | `I2720` | Pulmonary hypertension, unspecified |
| 20 | ICD-10 | `E790` | Hyperuricemia without signs of inflammatory arthritis and tophaceous disease |
| 21 | ICD-10 | `G893` | Neoplasm related pain (acute) (chronic) |

## 5. ICU Stays

| Stay ID | First Care Unit | Last Care Unit | ICU Admit | ICU Discharge | LOS (days) |
|---|---|---|---|---|---|
| 35727289 | Medical/Surgical Intensive Care Unit (MICU/SICU) | Medical/Surgical Intensive Care Unit (MICU/SICU) | 2155-07-10 17:48:57 | 2155-07-13 15:04:42 | 2.89 |

## 6. Escalation / Severity Indicators

_No escalation indicators detected from ICD codes or ICU procedure events._

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2155-07-11 | ICD-10 | `07DR3ZX` | Extraction of Iliac Bone Marrow, Percutaneous Approach, Diagnostic |

### ICU Procedure Events (from `icu/procedureevents.csv.gz`)

- 20 Gauge (category: Access Lines - Peripheral, started: 2155-07-10 19:28:00, status: FinishedRunning)
- 18 Gauge (category: Access Lines - Peripheral, started: 2155-07-10 19:28:00, status: FinishedRunning)
- Ultrasound (category: 5-Imaging, started: 2155-07-11 09:00:00, status: FinishedRunning)
- Chest X-Ray (category: 5-Imaging, started: 2155-07-12 14:30:00, status: FinishedRunning)

## 8. Critical Findings (Charted Events)

- **Code Status** (first noted: 2155-07-10 19:29:00)
- **Dialysis patient** (first noted: 2155-07-10 19:32:00)

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2155-07-10 12:46:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2155-07-10 12:46:00 | Transfer | → Emergency Department (ED) |
| 2155-07-10 17:48:00 | Admission | Admitted from TRANSFER FROM HOSPITAL (EW EMER.) |
| 2155-07-10 17:48:57 | ICU Admission | Medical/Surgical Intensive Care Unit (MICU/SICU) (LOS: 2.9 days) |
| 2155-07-10 17:49:33 | Transfer | → Medical/Surgical Intensive Care Unit (MICU/SICU) (transfer) |
| 2155-07-10 19:03:00 | ED Departure | Left Emergency Dept. |
| 2155-07-13 15:04:42 | Transfer | → Hematology/Oncology Intermediate (transfer) |
| 2155-07-18 16:59:00 | Discharge | To HOME |

## 10. Missing / Ambiguous Data

- No obvious missing critical fields detected.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
