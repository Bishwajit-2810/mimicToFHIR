# Encounter Report — HADM 22081550

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 22081550 |
| Subject ID | 10004720 |
| Patient Sex | M |
| Patient Anchor Age (at anchor year) | 61 |
| Anchor Year | 2183 |
| Admission Time | 2186-11-12 18:01:00 |
| Discharge Time | 2186-11-17 18:30:00 |
| Admission Type | EW EMER. |
| Admission Location | INFORMATION NOT AVAILABLE |
| Discharge Location | DIED |
| Insurance | Medicare |
| Language | ENGLISH |
| Marital Status | SINGLE |
| Race/Ethnicity | WHITE |
| ED Registration | 2186-11-12 16:09:00 |
| ED Departure | 2186-11-12 19:55:00 |
| In-Hospital Mortality | YES — Death time: 2186-11-17 18:30:00 |
| Date of Death (overall) | 2186-11-17 |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| HCFA | 207 | RESPIRATORY SYSTEM DIAGNOSIS W VENTILATOR SUPPORT >96 HOURS | N/A | N/A |
| APR | 950 | EXTENSIVE PROCEDURE UNRELATED TO PRINCIPAL DIAGNOSIS | 4.0 | 4.0 |

### Primary Diagnosis (seq_num = 1)

- **ICD-10 J690**: Pneumonitis due to inhalation of food and vomit

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2186-11-12 18:02:15 | N/A | MED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-10 `J690`: Pneumonitis due to inhalation of food and vomit
- (seq 2) ICD-10 `G931`: Anoxic brain damage, not elsewhere classified
- (seq 3) ICD-10 `I82621`: Acute embolism and thrombosis of deep veins of right upper extremity
- (seq 4) ICD-10 `Z8674`: Personal history of sudden cardiac arrest
- (seq 5) ICD-10 `J95811`: Postprocedural pneumothorax

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-10 | `J690` | Pneumonitis due to inhalation of food and vomit |
| 2 | ICD-10 | `G931` | Anoxic brain damage, not elsewhere classified |
| 3 | ICD-10 | `I82621` | Acute embolism and thrombosis of deep veins of right upper extremity |
| 4 | ICD-10 | `Z8674` | Personal history of sudden cardiac arrest |
| 5 | ICD-10 | `J95811` | Postprocedural pneumothorax |
| 6 | ICD-10 | `I959` | Hypotension, unspecified |
| 7 | ICD-10 | `J9600` | Acute respiratory failure, unspecified whether with hypoxia or hypercapnia |
| 8 | ICD-10 | `I10` | Essential (primary) hypertension |
| 9 | ICD-10 | `D638` | Anemia in other chronic diseases classified elsewhere |
| 10 | ICD-10 | `Y848` | Other medical procedures as the cause of abnormal reaction of the patient, or of later complication, without mention of misadventure at the time of the procedure |
| 11 | ICD-10 | `Y92238` | Other place in hospital as the place of occurrence of the external cause |
| 12 | ICD-10 | `Z66` | Do not resuscitate |
| 13 | ICD-10 | `Z515` | Encounter for palliative care |
| 14 | ICD-10 | `Z781` | Physical restraint status |
| 15 | ICD-10 | `F209` | Schizophrenia, unspecified |
| 16 | ICD-10 | `S42291D` | Other displaced fracture of upper end of right humerus, subsequent encounter for fracture with routine healing |
| 17 | ICD-10 | `W1830XD` | Fall on same level, unspecified, subsequent encounter |
| 18 | ICD-10 | `Z9181` | History of falling |
| 19 | ICD-10 | `Z85828` | Personal history of other malignant neoplasm of skin |
| 20 | ICD-10 | `H269` | Unspecified cataract |
| 21 | ICD-10 | `Z720` | Tobacco use |
| 22 | ICD-10 | `L409` | Psoriasis, unspecified |
| 23 | ICD-10 | `M810` | Age-related osteoporosis without current pathological fracture |
| 24 | ICD-10 | `L570` | Actinic keratosis |
| 25 | ICD-10 | `M720` | Palmar fascial fibromatosis [Dupuytren] |
| 26 | ICD-10 | `J309` | Allergic rhinitis, unspecified |
| 27 | ICD-10 | `F1021` | Alcohol dependence, in remission |
| 28 | ICD-10 | `Z7902` | Long term (current) use of antithrombotics/antiplatelets |
| 29 | ICD-10 | `H6120` | Impacted cerumen, unspecified ear |

## 5. ICU Stays

| Stay ID | First Care Unit | Last Care Unit | ICU Admit | ICU Discharge | LOS (days) |
|---|---|---|---|---|---|
| 35009126 | Surgical Intensive Care Unit (SICU) | Medical Intensive Care Unit (MICU) | 2186-11-12 19:55:00 | 2186-11-17 21:15:55 | 5.06 |

## 6. Escalation / Severity Indicators

The following critical conditions or interventions were detected:

- **Invasive Mechanical Ventilation** (ICU procedure event)
- **Respiratory Failure** (ICD diagnosis)

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2186-11-12 | ICD-10 | `5A1955Z` | Respiratory Ventilation, Greater than 96 Consecutive Hours |
| 2 | 2186-11-12 | ICD-10 | `0W9930Z` | Drainage of Right Pleural Cavity with Drainage Device, Percutaneous Approach |
| 3 | 2186-11-12 | ICD-10 | `02H633Z` | Insertion of Infusion Device into Right Atrium, Percutaneous Approach |
| 4 | 2186-11-15 | ICD-10 | `3E0G76Z` | Introduction of Nutritional Substance into Upper GI, Via Natural or Artificial Opening |

### ICU Procedure Events (from `icu/procedureevents.csv.gz`)

- Foley Catheter (category: GI/GU, started: 2186-11-12 18:02:00, status: FinishedRunning)
- Multi Lumen (category: Access Lines - Invasive, started: 2186-11-12 20:00:00, status: FinishedRunning)
- 18 Gauge (category: Access Lines - Peripheral, started: 2186-11-12 20:00:00, status: FinishedRunning)
- Invasive Ventilation (category: 2-Ventilation, started: 2186-11-12 20:29:00, status: FinishedRunning)
- EEG (category: 4-Procedures, started: 2186-11-12 23:30:00, status: FinishedRunning)
- Portable Chest X-Ray (category: 5-Imaging, started: 2186-11-13 04:00:00, status: FinishedRunning)
- Ultrasound (category: 5-Imaging, started: 2186-11-13 08:25:00, status: FinishedRunning)
- EKG (category: 4-Procedures, started: 2186-11-13 08:25:00, status: FinishedRunning)
- Transthoracic Echo (category: 5-Imaging, started: 2186-11-13 09:06:00, status: FinishedRunning)
- Nasal Swab (category: 6-Cultures, started: 2186-11-13 12:30:00, status: FinishedRunning)
- Blood Cultured (category: 6-Cultures, started: 2186-11-13 14:59:00, status: FinishedRunning)
- Chest X-Ray (category: 5-Imaging, started: 2186-11-14 05:06:00, status: FinishedRunning)
- Sputum Culture (category: 6-Cultures, started: 2186-11-14 11:23:00, status: FinishedRunning)
- Extubation (category: 1-Intubation/Extubation, started: 2186-11-17 14:00:00, status: FinishedRunning)

## 8. Critical Findings (Charted Events)

- **Ventilator Mode (Hamilton)** (first noted: 2186-11-12 20:00:00)
- **Ventilator Type** (first noted: 2186-11-12 20:00:00)
- **Ventilator Tank #2** (first noted: 2186-11-13 19:00:00)
- **Known difficult intubation** (first noted: 2186-11-12 20:00:00)
- **Stroke Volume Index (SVI NICOM)** (first noted: 2186-11-16 06:20:00)
- **Stroke Volume Variation (SVV NICOM)** (first noted: 2186-11-16 06:20:00)
- **Stroke Volume (SV NICOM)** (first noted: 2186-11-16 06:20:00)
- **Dialysis patient** (first noted: 2186-11-12 23:49:00)

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2186-11-12 16:09:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2186-11-12 16:09:00 | Transfer | → Emergency Department (ED) |
| 2186-11-12 18:01:00 | Admission | Admitted from INFORMATION NOT AVAILABLE (EW EMER.) |
| 2186-11-12 19:55:00 | ED Departure | Left Emergency Dept. |
| 2186-11-12 19:55:00 | ICU Admission | Surgical Intensive Care Unit (SICU) (LOS: 5.1 days) |
| 2186-11-16 11:28:07 | Transfer | → Medical Intensive Care Unit (MICU) (transfer) |
| 2186-11-17 18:30:00 | **IN-HOSPITAL DEATH** | |
| 2186-11-17 18:30:00 | Discharge | To DIED |

## 10. Missing / Ambiguous Data

- No obvious missing critical fields detected.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
