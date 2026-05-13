# Encounter Report — HADM 21607814

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 21607814 |
| Subject ID | 10023117 |
| Patient Sex | M |
| Patient Anchor Age (at anchor year) | 53 |
| Anchor Year | 2170 |
| Admission Time | 2175-07-06 15:57:00 |
| Discharge Time | 2175-07-20 00:00:00 |
| Admission Type | OBSERVATION ADMIT |
| Admission Location | EMERGENCY ROOM |
| Discharge Location | DIED |
| Insurance | Medicare |
| Language | ENGLISH |
| Marital Status | WIDOWED |
| Race/Ethnicity | WHITE |
| ED Registration | 2175-07-06 14:02:00 |
| ED Departure | 2175-07-06 17:41:00 |
| In-Hospital Mortality | YES — Death time: 2175-07-20 22:50:00 |
| Date of Death (overall) | 2175-07-20 |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| APR | 194 | HEART FAILURE | 4.0 | 3.0 |
| HCFA | 292 | HEART FAILURE & SHOCK W CC | N/A | N/A |

### Primary Diagnosis (seq_num = 1)

- **ICD-10 I5023**: Acute on chronic systolic (congestive) heart failure

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2175-07-06 15:58:33 | N/A | CMED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-10 `I5023`: Acute on chronic systolic (congestive) heart failure
- (seq 2) ICD-10 `I428`: Other cardiomyopathies
- (seq 3) ICD-10 `R570`: Cardiogenic shock
- (seq 4) ICD-10 `D689`: Coagulation defect, unspecified
- (seq 5) ICD-10 `I959`: Hypotension, unspecified

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-10 | `I5023` | Acute on chronic systolic (congestive) heart failure |
| 2 | ICD-10 | `I428` | Other cardiomyopathies |
| 3 | ICD-10 | `R570` | Cardiogenic shock |
| 4 | ICD-10 | `D689` | Coagulation defect, unspecified |
| 5 | ICD-10 | `I959` | Hypotension, unspecified |
| 6 | ICD-10 | `N179` | Acute kidney failure, unspecified |
| 7 | ICD-10 | `I248` | Other forms of acute ischemic heart disease |
| 8 | ICD-10 | `K2270` | Barrett's esophagus without dysplasia |
| 9 | ICD-10 | `I361` | Nonrheumatic tricuspid (valve) insufficiency |
| 10 | ICD-10 | `F200` | Paranoid schizophrenia |
| 11 | ICD-10 | `Z95810` | Presence of automatic (implantable) cardiac defibrillator |
| 12 | ICD-10 | `E785` | Hyperlipidemia, unspecified |
| 13 | ICD-10 | `K219` | Gastro-esophageal reflux disease without esophagitis |
| 14 | ICD-10 | `I129` | Hypertensive chronic kidney disease with stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease |
| 15 | ICD-10 | `N189` | Chronic kidney disease, unspecified |
| 16 | ICD-10 | `I340` | Nonrheumatic mitral (valve) insufficiency |
| 17 | ICD-10 | `G4700` | Insomnia, unspecified |
| 18 | ICD-10 | `F329` | Major depressive disorder, single episode, unspecified |
| 19 | ICD-10 | `F419` | Anxiety disorder, unspecified |
| 20 | ICD-10 | `Z8249` | Family history of ischemic heart disease and other diseases of the circulatory system |
| 21 | ICD-10 | `Z85528` | Personal history of other malignant neoplasm of kidney |
| 22 | ICD-10 | `Z86718` | Personal history of other venous thrombosis and embolism |
| 23 | ICD-10 | `Z87891` | Personal history of nicotine dependence |
| 24 | ICD-10 | `E806` | Other disorders of bilirubin metabolism |
| 25 | ICD-10 | `R300` | Dysuria |
| 26 | ICD-10 | `Z515` | Encounter for palliative care |
| 27 | ICD-10 | `Z66` | Do not resuscitate |

## 5. ICU Stays

| Stay ID | First Care Unit | Last Care Unit | ICU Admit | ICU Discharge | LOS (days) |
|---|---|---|---|---|---|
| 30955999 | Coronary Care Unit (CCU) | Coronary Care Unit (CCU) | 2175-07-06 17:41:00 | 2175-07-19 22:50:08 | 13.21 |

## 6. Escalation / Severity Indicators

The following critical conditions or interventions were detected:

- **Acute Kidney Injury** (ICD diagnosis)
- **Shock** (ICD diagnosis)

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2175-07-08 | ICD-10 | `02HV33Z` | Insertion of Infusion Device into Superior Vena Cava, Percutaneous Approach |
| 2 | 2175-07-11 | ICD-10 | `02HV33Z` | Insertion of Infusion Device into Superior Vena Cava, Percutaneous Approach |

### ICU Procedure Events (from `icu/procedureevents.csv.gz`)

- 20 Gauge (category: Access Lines - Peripheral, started: 2175-07-06 17:53:00, status: FinishedRunning)
- 18 Gauge (category: Access Lines - Peripheral, started: 2175-07-11 01:35:00, status: FinishedRunning)
- PICC Line (category: Access Lines - Invasive, started: 2175-07-11 14:39:00, status: FinishedRunning)
- Urine Culture (category: 6-Cultures, started: 2175-07-14 01:08:00, status: FinishedRunning)
- Family updated by RN (category: 7-Communication, started: 2175-07-14 20:00:00, status: FinishedRunning)
- EKG (category: 4-Procedures, started: 2175-07-14 21:06:00, status: FinishedRunning)

## 8. Critical Findings (Charted Events)

- **Code Status** (first noted: 2175-07-14 00:49:00)
- **Dialysis patient** (first noted: 2175-07-06 18:06:00)

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2175-07-06 14:02:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2175-07-06 14:02:00 | Transfer | → Emergency Department (ED) |
| 2175-07-06 15:57:00 | Admission | Admitted from EMERGENCY ROOM (OBSERVATION ADMIT) |
| 2175-07-06 17:41:00 | ED Departure | Left Emergency Dept. |
| 2175-07-06 17:41:00 | ICU Admission | Coronary Care Unit (CCU) (LOS: 13.2 days) |
| 2175-07-19 22:50:08 | Transfer | → Medicine/Cardiology (transfer) |
| 2175-07-20 00:00:00 | Discharge | To DIED |
| 2175-07-20 22:50:00 | **IN-HOSPITAL DEATH** | |

## 10. Missing / Ambiguous Data

- No obvious missing critical fields detected.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
