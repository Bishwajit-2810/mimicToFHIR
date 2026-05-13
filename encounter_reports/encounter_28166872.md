# Encounter Report — HADM 28166872

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 28166872 |
| Subject ID | 10027602 |
| Patient Sex | F |
| Patient Anchor Age (at anchor year) | 71 |
| Anchor Year | 2201 |
| Admission Time | 2201-10-30 12:05:00 |
| Discharge Time | 2201-11-20 14:45:00 |
| Admission Type | EW EMER. |
| Admission Location | EMERGENCY ROOM |
| Discharge Location | REHAB |
| Insurance | Other |
| Language | ENGLISH |
| Marital Status | SINGLE |
| Race/Ethnicity | WHITE |
| ED Registration | 2201-10-30 10:48:00 |
| ED Departure | 2201-10-30 12:25:00 |
| In-Hospital Mortality | No |
| Date of Death (overall) | N/A |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| HCFA | 20 | INTRACRANIAL VASCULAR PROCEDURES W PDX HEMORRHAGE W MCC | N/A | N/A |
| APR | 21 | CRANIOTOMY EXCEPT FOR TRAUMA | 4.0 | 4.0 |

### Primary Diagnosis (seq_num = 1)

- **ICD-9 430**: Subarachnoid hemorrhage

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2201-10-30 12:07:45 | N/A | NSURG |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-9 `430`: Subarachnoid hemorrhage
- (seq 2) ICD-9 `3485`: Cerebral edema
- (seq 3) ICD-9 `51881`: Acute respiratory failure
- (seq 4) ICD-9 `48242`: Methicillin resistant pneumonia due to Staphylococcus aureus
- (seq 5) ICD-9 `5990`: Urinary tract infection, site not specified

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-9 | `430` | Subarachnoid hemorrhage |
| 2 | ICD-9 | `3485` | Cerebral edema |
| 3 | ICD-9 | `51881` | Acute respiratory failure |
| 4 | ICD-9 | `48242` | Methicillin resistant pneumonia due to Staphylococcus aureus |
| 5 | ICD-9 | `5990` | Urinary tract infection, site not specified |
| 6 | ICD-9 | `V0481` | Need for prophylactic vaccination and inoculation against influenza |
| 7 | ICD-9 | `V4987` | Physical restraints status |
| 8 | ICD-9 | `78039` | Other convulsions |
| 9 | ICD-9 | `78722` | Dysphagia, oropharyngeal phase |
| 10 | ICD-9 | `04104` | Streptococcus infection in conditions classified elsewhere and of unspecified site, streptococcus, group D [Enterococcus] |
| 11 | ICD-9 | `79902` | Hypoxemia |
| 12 | ICD-9 | `31401` | Attention deficit disorder with hyperactivity |
| 13 | ICD-9 | `4019` | Unspecified essential hypertension |
| 14 | ICD-9 | `49390` | Asthma, unspecified type, unspecified |
| 15 | ICD-9 | `53081` | Esophageal reflux |
| 16 | ICD-9 | `2449` | Unspecified acquired hypothyroidism |
| 17 | ICD-9 | `79311` | Solitary pulmonary nodule |

## 5. ICU Stays

| Stay ID | First Care Unit | Last Care Unit | ICU Admit | ICU Discharge | LOS (days) |
|---|---|---|---|---|---|
| 32391858 | Surgical Intensive Care Unit (SICU) | Surgical Intensive Care Unit (SICU) | 2201-10-30 12:25:00 | 2201-11-12 18:37:10 | 13.26 |

## 6. Escalation / Severity Indicators

The following critical conditions or interventions were detected:

- **Arterial Line** (ICU procedure event)
- **Endotracheal Intubation** (ICU procedure event)
- **Invasive Mechanical Ventilation** (ICU procedure event)
- **Pneumonia** (ICD diagnosis)
- **Respiratory Failure** (ICD diagnosis)

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2201-11-04 | ICD-9 | `3972` | Endovascular (total) embolization or occlusion of head and neck vessels |
| 2 | 2201-10-30 | ICD-9 | `0221` | Insertion or replacement of external ventricular drain [EVD] |
| 3 | 2201-11-16 | ICD-9 | `4311` | Percutaneous [endoscopic] gastrostomy [PEG] |
| 4 | 2201-10-30 | ICD-9 | `9672` | Continuous invasive mechanical ventilation for 96 consecutive hours or more |
| 5 | 2201-11-08 | ICD-9 | `3972` | Endovascular (total) embolization or occlusion of head and neck vessels |
| 6 | 2201-11-06 | ICD-9 | `0221` | Insertion or replacement of external ventricular drain [EVD] |
| 7 | 2201-11-01 | ICD-9 | `966` | Enteral infusion of concentrated nutritional substances |
| 8 | 2201-11-07 | ICD-9 | `9671` | Continuous invasive mechanical ventilation for less than 96 consecutive hours |
| 9 | 2201-11-03 | ICD-9 | `8841` | Arteriography of cerebral arteries |
| 10 | 2201-11-04 | ICD-9 | `8841` | Arteriography of cerebral arteries |
| 11 | 2201-11-08 | ICD-9 | `8841` | Arteriography of cerebral arteries |
| 12 | 2201-11-08 | ICD-9 | `3324` | Closed [endoscopic] biopsy of bronchus |
| 13 | 2201-11-07 | ICD-9 | `9604` | Insertion of endotracheal tube |

### ICU Procedure Events (from `icu/procedureevents.csv.gz`)

- Invasive Ventilation (category: 2-Ventilation, started: 2201-10-30 12:30:00, status: FinishedRunning)
- 20 Gauge (category: Access Lines - Peripheral, started: 2201-10-30 13:03:00, status: FinishedRunning)
- ICP Catheter (category: Access Lines - Invasive, started: 2201-10-30 13:43:00, status: FinishedRunning)
- Nasal Swab (category: 6-Cultures, started: 2201-10-30 17:00:00, status: FinishedRunning)
- Chest X-Ray (category: 5-Imaging, started: 2201-10-30 17:00:00, status: FinishedRunning)
- Multi Lumen (category: Access Lines - Invasive, started: 2201-10-30 17:18:00, status: FinishedRunning)
- Magnetic Resonance Imaging (category: 5-Imaging, started: 2201-11-02 02:26:00, status: FinishedRunning)
- Sheath (Venous) (category: Access Lines - Invasive, started: 2201-11-03 14:32:00, status: FinishedRunning)
- Family updated by MD (category: 7-Communication, started: 2201-11-03 14:36:00, status: FinishedRunning)
- Arterial Line (category: Access Lines - Invasive, started: 2201-11-04 14:03:00, status: FinishedRunning)
- Pan Culture (category: 6-Cultures, started: 2201-11-05 02:30:00, status: FinishedRunning)
- Intraventricular Drain Inserted (category: 4-Procedures, started: 2201-11-06 13:00:00, status: FinishedRunning)
- Extubation (category: 1-Intubation/Extubation, started: 2201-11-07 13:40:00, status: FinishedRunning)
- Intubation (category: 1-Intubation/Extubation, started: 2201-11-07 15:00:00, status: FinishedRunning)
- Angiography (category: 5-Imaging, started: 2201-11-08 15:00:00, status: FinishedRunning)
- CT scan (category: 5-Imaging, started: 2201-11-10 14:00:00, status: FinishedRunning)
- X-ray (category: 5-Imaging, started: 2201-11-11 05:09:00, status: FinishedRunning)
- 18 Gauge (category: Access Lines - Peripheral, started: 2201-11-11 09:54:00, status: FinishedRunning)

## 8. Critical Findings (Charted Events)

- **Ventilator Mode** (first noted: 2201-10-30 12:00:00)
- **Ventilator Tank #1** (first noted: 2201-10-31 08:00:00)
- **Ventilator Type** (first noted: 2201-10-30 12:00:00)
- **Known difficult intubation** (first noted: 2201-10-30 20:01:00)
- **Seizure Duration** (first noted: 2201-10-31 08:00:00)
- **Seizure Activity** (first noted: 2201-10-31 08:00:00)

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2201-10-30 10:48:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2201-10-30 10:48:00 | Transfer | → Emergency Department (ED) |
| 2201-10-30 12:05:00 | Admission | Admitted from EMERGENCY ROOM (EW EMER.) |
| 2201-10-30 12:25:00 | ED Departure | Left Emergency Dept. |
| 2201-10-30 12:25:00 | ICU Admission | Surgical Intensive Care Unit (SICU) (LOS: 13.3 days) |
| 2201-11-12 18:37:10 | Transfer | → Neurology (transfer) |
| 2201-11-12 19:13:44 | Transfer | → Neurology (transfer) |
| 2201-11-12 19:14:05 | Transfer | → Neurology (transfer) |
| 2201-11-14 13:45:02 | Transfer | → Neurology (transfer) |
| 2201-11-20 14:45:00 | Discharge | To REHAB |

## 10. Missing / Ambiguous Data

- No obvious missing critical fields detected.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
