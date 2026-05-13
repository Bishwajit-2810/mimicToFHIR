# Encounter Report — HADM 28506150

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 28506150 |
| Subject ID | 10016742 |
| Patient Sex | F |
| Patient Anchor Age (at anchor year) | 58 |
| Anchor Year | 2178 |
| Admission Time | 2178-07-13 05:40:00 |
| Discharge Time | 2178-07-16 02:00:00 |
| Admission Type | OBSERVATION ADMIT |
| Admission Location | EMERGENCY ROOM |
| Discharge Location | SKILLED NURSING FACILITY |
| Insurance | Medicaid |
| Language | ENGLISH |
| Marital Status | SINGLE |
| Race/Ethnicity | BLACK/AFRICAN AMERICAN |
| ED Registration | 2178-07-13 04:37:00 |
| ED Departure | 2178-07-13 08:16:00 |
| In-Hospital Mortality | No |
| Date of Death (overall) | N/A |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| HCFA | 939 | O.R. PROC W DIAGNOSES OF OTHER CONTACT W HEALTH SERVICES W MCC | N/A | N/A |
| APR | 850 | PROCEDURE W DIAG OF REHAB, AFTERCARE OR OTH CONTACT W HEALTH SERVICE | 4.0 | 4.0 |

### Primary Diagnosis (seq_num = 1)

- **ICD-10 R4182**: Altered mental status, unspecified

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2178-07-13 05:40:59 | N/A | MED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-10 `R4182`: Altered mental status, unspecified
- (seq 2) ICD-10 `I214`: Non-ST elevation (NSTEMI) myocardial infarction
- (seq 3) ICD-10 `G1221`: Amyotrophic lateral sclerosis
- (seq 4) ICD-10 `Z9911`: Dependence on respirator [ventilator] status
- (seq 5) ICD-10 `J95851`: Ventilator associated pneumonia

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-10 | `R4182` | Altered mental status, unspecified |
| 2 | ICD-10 | `I214` | Non-ST elevation (NSTEMI) myocardial infarction |
| 3 | ICD-10 | `G1221` | Amyotrophic lateral sclerosis |
| 4 | ICD-10 | `Z9911` | Dependence on respirator [ventilator] status |
| 5 | ICD-10 | `J95851` | Ventilator associated pneumonia |
| 6 | ICD-10 | `Z930` | Tracheostomy status |
| 7 | ICD-10 | `I959` | Hypotension, unspecified |
| 8 | ICD-10 | `I319` | Disease of pericardium, unspecified |
| 9 | ICD-10 | `N390` | Urinary tract infection, site not specified |
| 10 | ICD-10 | `E119` | Type 2 diabetes mellitus without complications |
| 11 | ICD-10 | `G3109` | Other frontotemporal dementia |
| 12 | ICD-10 | `F259` | Schizoaffective disorder, unspecified |
| 13 | ICD-10 | `T17990A` | Other foreign object in respiratory tract, part unspecified in causing asphyxiation, initial encounter |
| 14 | ICD-10 | `Y92230` | Patient room in hospital as the place of occurrence of the external cause |
| 15 | ICD-10 | `Z794` | Long term (current) use of insulin |
| 16 | ICD-10 | `I10` | Essential (primary) hypertension |
| 17 | ICD-10 | `R569` | Unspecified convulsions |
| 18 | ICD-10 | `I2510` | Atherosclerotic heart disease of native coronary artery without angina pectoris |

## 5. ICU Stays

| Stay ID | First Care Unit | Last Care Unit | ICU Admit | ICU Discharge | LOS (days) |
|---|---|---|---|---|---|
| 32314488 | Medical Intensive Care Unit (MICU) | Medical Intensive Care Unit (MICU) | 2178-07-13 08:16:00 | 2178-07-16 14:41:31 | 3.27 |

## 6. Escalation / Severity Indicators

The following critical conditions or interventions were detected:

- **Invasive Mechanical Ventilation** (ICU procedure event)

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2178-07-13 | ICD-10 | `5A1945Z` | Respiratory Ventilation, 24-96 Consecutive Hours |
| 2 | 2178-07-14 | ICD-10 | `0BCF8ZZ` | Extirpation of Matter from Right Lower Lung Lobe, Via Natural or Artificial Opening Endoscopic |
| 3 | 2178-07-14 | ICD-10 | `0BCB8ZZ` | Extirpation of Matter from Left Lower Lobe Bronchus, Via Natural or Artificial Opening Endoscopic |

### ICU Procedure Events (from `icu/procedureevents.csv.gz`)

- Invasive Ventilation (category: 2-Ventilation, started: 2178-07-13 08:00:00, status: FinishedRunning)
- PICC Line (category: Access Lines - Invasive, started: 2178-07-13 08:00:00, status: FinishedRunning)
- Chest X-Ray (category: 5-Imaging, started: 2178-07-15 07:30:00, status: FinishedRunning)

## 8. Critical Findings (Charted Events)

- **Ventilator Type** (first noted: 2178-07-13 08:00:00)
- **Ventilator Tank #1** (first noted: 2178-07-13 08:00:00)
- **Ventilator Mode** (first noted: 2178-07-13 08:00:00)
- **Code Status** (first noted: 2178-07-13 09:10:00)
- **Dialysis patient** (first noted: 2178-07-13 10:26:00)

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2178-07-13 04:37:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2178-07-13 04:37:00 | Transfer | → Emergency Department (ED) |
| 2178-07-13 05:40:00 | Admission | Admitted from EMERGENCY ROOM (OBSERVATION ADMIT) |
| 2178-07-13 08:16:00 | ED Departure | Left Emergency Dept. |
| 2178-07-13 08:16:00 | ICU Admission | Medical Intensive Care Unit (MICU) (LOS: 3.3 days) |
| 2178-07-16 02:00:00 | Discharge | To SKILLED NURSING FACILITY |

## 10. Missing / Ambiguous Data

- No obvious missing critical fields detected.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
