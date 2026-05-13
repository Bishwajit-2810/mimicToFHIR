# Encounter Report — HADM 27568122

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 27568122 |
| Subject ID | 10016742 |
| Patient Sex | F |
| Patient Anchor Age (at anchor year) | 58 |
| Anchor Year | 2178 |
| Admission Time | 2178-07-22 07:19:00 |
| Discharge Time | 2178-07-25 16:30:00 |
| Admission Type | OBSERVATION ADMIT |
| Admission Location | EMERGENCY ROOM |
| Discharge Location | CHRONIC/LONG TERM ACUTE CARE |
| Insurance | Medicaid |
| Language | ENGLISH |
| Marital Status | SINGLE |
| Race/Ethnicity | BLACK/AFRICAN AMERICAN |
| ED Registration | 2178-07-22 05:41:00 |
| ED Departure | 2178-07-22 08:19:00 |
| In-Hospital Mortality | No |
| Date of Death (overall) | N/A |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| APR | 133 | RESPIRATORY FAILURE | 3.0 | 3.0 |
| HCFA | 208 | RESPIRATORY SYSTEM DIAGNOSIS W VENTILATOR SUPPORT <96 HOURS | N/A | N/A |

### Primary Diagnosis (seq_num = 1)

- **ICD-10 J9621**: Acute and chronic respiratory failure with hypoxia

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2178-07-22 07:20:17 | N/A | MED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-10 `J9621`: Acute and chronic respiratory failure with hypoxia
- (seq 2) ICD-10 `G1221`: Amyotrophic lateral sclerosis
- (seq 3) ICD-10 `Z9911`: Dependence on respirator [ventilator] status
- (seq 4) ICD-10 `Z930`: Tracheostomy status
- (seq 5) ICD-10 `I319`: Disease of pericardium, unspecified

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-10 | `J9621` | Acute and chronic respiratory failure with hypoxia |
| 2 | ICD-10 | `G1221` | Amyotrophic lateral sclerosis |
| 3 | ICD-10 | `Z9911` | Dependence on respirator [ventilator] status |
| 4 | ICD-10 | `Z930` | Tracheostomy status |
| 5 | ICD-10 | `I319` | Disease of pericardium, unspecified |
| 6 | ICD-10 | `J9809` | Other diseases of bronchus, not elsewhere classified |
| 7 | ICD-10 | `Z434` | Encounter for attention to other artificial openings of digestive tract |
| 8 | ICD-10 | `G40909` | Epilepsy, unspecified, not intractable, without status epilepticus |
| 9 | ICD-10 | `E119` | Type 2 diabetes mellitus without complications |
| 10 | ICD-10 | `Z794` | Long term (current) use of insulin |
| 11 | ICD-10 | `D649` | Anemia, unspecified |

## 5. ICU Stays

| Stay ID | First Care Unit | Last Care Unit | ICU Admit | ICU Discharge | LOS (days) |
|---|---|---|---|---|---|
| 30425410 | Medical Intensive Care Unit (MICU) | Medical Intensive Care Unit (MICU) | 2178-07-22 08:19:00 | 2178-07-25 16:42:43 | 3.35 |

## 6. Escalation / Severity Indicators

The following critical conditions or interventions were detected:

- **Invasive Mechanical Ventilation** (ICU procedure event)

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2178-07-25 | ICD-10 | `5A1945Z` | Respiratory Ventilation, 24-96 Consecutive Hours |
| 2 | 2178-07-24 | ICD-10 | `0D2DXUZ` | Change Feeding Device in Lower Intestinal Tract, External Approach |
| 3 | 2178-07-25 | ICD-10 | `3E0H76Z` | Introduction of Nutritional Substance into Lower GI, Via Natural or Artificial Opening |
| 4 | 2178-07-23 | ICD-10 | `0BJ08ZZ` | Inspection of Tracheobronchial Tree, Via Natural or Artificial Opening Endoscopic |

### ICU Procedure Events (from `icu/procedureevents.csv.gz`)

- Invasive Ventilation (category: 2-Ventilation, started: 2178-07-22 08:33:00, status: FinishedRunning)
- PICC Line (category: Access Lines - Invasive, started: 2178-07-22 09:00:00, status: FinishedRunning)
- Foley Catheter (category: GI/GU, started: 2178-07-22 09:30:00, status: FinishedRunning)
- Bronchoscopy (category: 4-Procedures, started: 2178-07-23 17:02:00, status: FinishedRunning)

## 8. Critical Findings (Charted Events)

- **Ventilator Type** (first noted: 2178-07-22 08:00:00)
- **Ventilator Mode (Hamilton)** (first noted: 2178-07-22 08:00:00)
- **Ventilator Tank #1** (first noted: 2178-07-22 08:00:00)
- **Code Status** (first noted: 2178-07-22 08:52:00)
- **Dialysis patient** (first noted: 2178-07-22 09:02:00)

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2178-07-22 05:41:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2178-07-22 05:41:00 | Transfer | → Emergency Department (ED) |
| 2178-07-22 07:19:00 | Admission | Admitted from EMERGENCY ROOM (OBSERVATION ADMIT) |
| 2178-07-22 08:19:00 | ED Departure | Left Emergency Dept. |
| 2178-07-22 08:19:00 | ICU Admission | Medical Intensive Care Unit (MICU) (LOS: 3.3 days) |
| 2178-07-25 16:30:00 | Discharge | To CHRONIC/LONG TERM ACUTE CARE |

## 10. Missing / Ambiguous Data

- No obvious missing critical fields detected.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
