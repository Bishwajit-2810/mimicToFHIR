# Encounter Report — HADM 23819016

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 23819016 |
| Subject ID | 10039708 |
| Patient Sex | F |
| Patient Anchor Age (at anchor year) | 46 |
| Anchor Year | 2138 |
| Admission Time | 2140-06-18 00:22:00 |
| Discharge Time | 2140-06-22 17:40:00 |
| Admission Type | OBSERVATION ADMIT |
| Admission Location | EMERGENCY ROOM |
| Discharge Location | HOME |
| Insurance | Other |
| Language | ENGLISH |
| Marital Status | SINGLE |
| Race/Ethnicity | BLACK/AFRICAN AMERICAN |
| ED Registration | 2140-06-17 17:47:00 |
| ED Departure | 2140-06-18 01:41:00 |
| In-Hospital Mortality | No |
| Date of Death (overall) | N/A |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| APR | 720 | SEPTICEMIA & DISSEMINATED INFECTIONS | 4.0 | 4.0 |
| HCFA | 871 | SEPTICEMIA OR SEVERE SEPSIS W/O MV >96 HOURS W MCC | N/A | N/A |

### Primary Diagnosis (seq_num = 1)

- **ICD-10 A4189**: Other specified sepsis

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2140-06-18 00:23:15 | N/A | MED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-10 `A4189`: Other specified sepsis
- (seq 2) ICD-10 `K859`: Acute pancreatitis, unspecified
- (seq 3) ICD-10 `R6521`: Severe sepsis with septic shock
- (seq 4) ICD-10 `N179`: Acute kidney failure, unspecified
- (seq 5) ICD-10 `R64`: Cachexia

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-10 | `A4189` | Other specified sepsis |
| 2 | ICD-10 | `K859` | Acute pancreatitis, unspecified |
| 3 | ICD-10 | `R6521` | Severe sepsis with septic shock |
| 4 | ICD-10 | `N179` | Acute kidney failure, unspecified |
| 5 | ICD-10 | `R64` | Cachexia |
| 6 | ICD-10 | `E46` | Unspecified protein-calorie malnutrition |
| 7 | ICD-10 | `E872` | Acidosis |
| 8 | ICD-10 | `E5112` | Wet beriberi |
| 9 | ICD-10 | `G629` | Polyneuropathy, unspecified |
| 10 | ICD-10 | `F1020` | Alcohol dependence, uncomplicated |
| 11 | ICD-10 | `K7010` | Alcoholic hepatitis without ascites |
| 12 | ICD-10 | `E039` | Hypothyroidism, unspecified |
| 13 | ICD-10 | `I129` | Hypertensive chronic kidney disease with stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease |
| 14 | ICD-10 | `N189` | Chronic kidney disease, unspecified |
| 15 | ICD-10 | `Z720` | Tobacco use |
| 16 | ICD-10 | `J45909` | Unspecified asthma, uncomplicated |
| 17 | ICD-10 | `M109` | Gout, unspecified |
| 18 | ICD-10 | `D649` | Anemia, unspecified |
| 19 | ICD-10 | `R410` | Disorientation, unspecified |
| 20 | ICD-10 | `Z86718` | Personal history of other venous thrombosis and embolism |
| 21 | ICD-10 | `Z9884` | Bariatric surgery status |

## 5. ICU Stays

| Stay ID | First Care Unit | Last Care Unit | ICU Admit | ICU Discharge | LOS (days) |
|---|---|---|---|---|---|
| 38559363 | Trauma SICU (TSICU) | Trauma SICU (TSICU) | 2140-06-18 01:41:00 | 2140-06-19 21:47:16 | 1.84 |

## 6. Escalation / Severity Indicators

The following critical conditions or interventions were detected:

- **Acute Kidney Injury** (ICD diagnosis)
- **Sepsis** (ICD diagnosis)

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2140-06-18 | ICD-10 | `02HV33Z` | Insertion of Infusion Device into Superior Vena Cava, Percutaneous Approach |

### ICU Procedure Events (from `icu/procedureevents.csv.gz`)

- 20 Gauge (category: Access Lines - Peripheral, started: 2140-06-18 01:41:00, status: FinishedRunning)
- 18 Gauge (category: Access Lines - Peripheral, started: 2140-06-18 01:41:00, status: FinishedRunning)
- Foley Catheter (category: GI/GU, started: 2140-06-18 04:04:00, status: FinishedRunning)
- Multi Lumen (category: Access Lines - Invasive, started: 2140-06-18 16:53:00, status: FinishedRunning)
- CT scan (category: 5-Imaging, started: 2140-06-19 14:41:00, status: FinishedRunning)

## 8. Critical Findings (Charted Events)

- **Code Status** (first noted: 2140-06-19 20:38:00)
- **Dialysis patient** (first noted: 2140-06-18 01:46:00)

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2140-06-17 17:47:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2140-06-17 17:47:00 | Transfer | → Emergency Department (ED) |
| 2140-06-18 00:22:00 | Admission | Admitted from EMERGENCY ROOM (OBSERVATION ADMIT) |
| 2140-06-18 01:41:00 | ED Departure | Left Emergency Dept. |
| 2140-06-18 01:41:00 | ICU Admission | Trauma SICU (TSICU) (LOS: 1.8 days) |
| 2140-06-19 21:47:16 | Transfer | → Medicine (transfer) |
| 2140-06-20 03:37:38 | Transfer | → Medicine (transfer) |
| 2140-06-22 17:40:00 | Discharge | To HOME |

## 10. Missing / Ambiguous Data

- No obvious missing critical fields detected.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
