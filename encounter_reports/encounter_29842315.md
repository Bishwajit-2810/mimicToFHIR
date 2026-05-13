# Encounter Report — HADM 29842315

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 29842315 |
| Subject ID | 10010471 |
| Patient Sex | F |
| Patient Anchor Age (at anchor year) | 89 |
| Anchor Year | 2155 |
| Admission Time | 2155-12-02 19:36:00 |
| Discharge Time | 2155-12-07 15:30:00 |
| Admission Type | EW EMER. |
| Admission Location | EMERGENCY ROOM |
| Discharge Location | DIED |
| Insurance | Medicare |
| Language | ENGLISH |
| Marital Status | WIDOWED |
| Race/Ethnicity | WHITE |
| ED Registration | 2155-12-02 16:00:00 |
| ED Departure | 2155-12-02 20:33:00 |
| In-Hospital Mortality | YES — Death time: 2155-12-07 15:30:00 |
| Date of Death (overall) | 2155-12-07 |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| APR | 190 | ACUTE MYOCARDIAL INFARCTION | 4.0 | 4.0 |
| HCFA | 283 | ACUTE MYOCARDIAL INFARCTION, EXPIRED W MCC | N/A | N/A |

### Primary Diagnosis (seq_num = 1)

- **ICD-10 I214**: Non-ST elevation (NSTEMI) myocardial infarction

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2155-12-02 19:38:44 | N/A | CMED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-10 `I214`: Non-ST elevation (NSTEMI) myocardial infarction
- (seq 2) ICD-10 `N186`: End stage renal disease
- (seq 3) ICD-10 `I462`: Cardiac arrest due to underlying cardiac condition
- (seq 4) ICD-10 `J9690`: Respiratory failure, unspecified, unspecified whether with hypoxia or hypercapnia
- (seq 5) ICD-10 `I5033`: Acute on chronic diastolic (congestive) heart failure

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-10 | `I214` | Non-ST elevation (NSTEMI) myocardial infarction |
| 2 | ICD-10 | `N186` | End stage renal disease |
| 3 | ICD-10 | `I462` | Cardiac arrest due to underlying cardiac condition |
| 4 | ICD-10 | `J9690` | Respiratory failure, unspecified, unspecified whether with hypoxia or hypercapnia |
| 5 | ICD-10 | `I5033` | Acute on chronic diastolic (congestive) heart failure |
| 6 | ICD-10 | `S2243XA` | Multiple fractures of ribs, bilateral, initial encounter for closed fracture |
| 7 | ICD-10 | `I959` | Hypotension, unspecified |
| 8 | ICD-10 | `R7881` | Bacteremia |
| 9 | ICD-10 | `I132` | Hypertensive heart and chronic kidney disease with heart failure and with stage 5 chronic kidney disease, or end stage renal disease |
| 10 | ICD-10 | `I480` | Paroxysmal atrial fibrillation |
| 11 | ICD-10 | `Z9981` | Dependence on supplemental oxygen |
| 12 | ICD-10 | `J449` | Chronic obstructive pulmonary disease, unspecified |
| 13 | ICD-10 | `I080` | Rheumatic disorders of both mitral and aortic valves |
| 14 | ICD-10 | `I447` | Left bundle-branch block, unspecified |
| 15 | ICD-10 | `E785` | Hyperlipidemia, unspecified |
| 16 | ICD-10 | `I2510` | Atherosclerotic heart disease of native coronary artery without angina pectoris |
| 17 | ICD-10 | `E039` | Hypothyroidism, unspecified |
| 18 | ICD-10 | `M5489` | Other dorsalgia |
| 19 | ICD-10 | `Z87891` | Personal history of nicotine dependence |
| 20 | ICD-10 | `K219` | Gastro-esophageal reflux disease without esophagitis |
| 21 | ICD-10 | `Z45018` | Encounter for adjustment and management of other part of cardiac pacemaker |
| 22 | ICD-10 | `D631` | Anemia in chronic kidney disease |
| 23 | ICD-10 | `Z992` | Dependence on renal dialysis |
| 24 | ICD-10 | `Y848` | Other medical procedures as the cause of abnormal reaction of the patient, or of later complication, without mention of misadventure at the time of the procedure |
| 25 | ICD-10 | `Y9289` | Other specified places as the place of occurrence of the external cause |
| 26 | ICD-10 | `R740` | Nonspecific elevation of levels of transaminase and lactic acid dehydrogenase [LDH] |
| 27 | ICD-10 | `Z515` | Encounter for palliative care |
| 28 | ICD-10 | `M7981` | Nontraumatic hematoma of soft tissue |
| 29 | ICD-10 | `T45515A` | Adverse effect of anticoagulants, initial encounter |
| 30 | ICD-10 | `Y92239` | Unspecified place in hospital as the place of occurrence of the external cause |

## 5. ICU Stays

| Stay ID | First Care Unit | Last Care Unit | ICU Admit | ICU Discharge | LOS (days) |
|---|---|---|---|---|---|
| 32119961 | Coronary Care Unit (CCU) | Coronary Care Unit (CCU) | 2155-12-02 20:33:00 | 2155-12-07 18:19:18 | 4.91 |

## 6. Escalation / Severity Indicators

The following critical conditions or interventions were detected:

- **Cardiac Arrest** (ICD diagnosis)
- **Renal Replacement Therapy / Dialysis** (ICU procedure event)
- **Respiratory Failure** (ICD diagnosis)

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2155-12-05 | ICD-10 | `4A023N6` | Measurement of Cardiac Sampling and Pressure, Right Heart, Percutaneous Approach |
| 2 | 2155-12-05 | ICD-10 | `B211YZZ` | Fluoroscopy of Multiple Coronary Arteries using Other Contrast |

### ICU Procedure Events (from `icu/procedureevents.csv.gz`)

- 18 Gauge (category: Access Lines - Peripheral, started: 2155-12-02 20:52:00, status: FinishedRunning)
- Dialysis Catheter (category: Access Lines - Invasive, started: 2155-12-02 21:13:00, status: FinishedRunning)
- 22 Gauge (category: Access Lines - Peripheral, started: 2155-12-02 21:13:00, status: FinishedRunning)
- Foley Catheter (category: GI/GU, started: 2155-12-02 21:16:00, status: FinishedRunning)
- Blood Cultured (category: 6-Cultures, started: 2155-12-03 20:23:00, status: FinishedRunning)
- Hemodialysis (category: 4-Procedures, started: 2155-12-04 13:30:00, status: FinishedRunning)
- EKG (category: 4-Procedures, started: 2155-12-04 15:46:00, status: FinishedRunning)
- Multi Lumen (category: Access Lines - Invasive, started: 2155-12-05 17:55:00, status: FinishedRunning)

## 8. Critical Findings (Charted Events)

- **Dialysis patient** (first noted: 2155-12-02 20:04:00)
- **Hemodialysis Output** (first noted: 2155-12-03 12:02:00)
- **Dialysis Catheter Site Appear** (first noted: 2155-12-02 21:13:00)

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2155-12-02 16:00:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2155-12-02 16:00:00 | Transfer | → Emergency Department (ED) |
| 2155-12-02 19:36:00 | Admission | Admitted from EMERGENCY ROOM (EW EMER.) |
| 2155-12-02 20:33:00 | ED Departure | Left Emergency Dept. |
| 2155-12-02 20:33:00 | ICU Admission | Coronary Care Unit (CCU) (LOS: 4.9 days) |
| 2155-12-07 15:30:00 | **IN-HOSPITAL DEATH** | |
| 2155-12-07 15:30:00 | Discharge | To DIED |

## 10. Missing / Ambiguous Data

- No obvious missing critical fields detected.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
