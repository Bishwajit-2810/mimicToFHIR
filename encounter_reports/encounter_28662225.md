# Encounter Report — HADM 28662225

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 28662225 |
| Subject ID | 10002428 |
| Patient Sex | F |
| Patient Anchor Age (at anchor year) | 80 |
| Anchor Year | 2155 |
| Admission Time | 2156-04-12 14:16:00 |
| Discharge Time | 2156-04-29 16:26:00 |
| Admission Type | EW EMER. |
| Admission Location | EMERGENCY ROOM |
| Discharge Location | SKILLED NURSING FACILITY |
| Insurance | Medicare |
| Language | ENGLISH |
| Marital Status | WIDOWED |
| Race/Ethnicity | WHITE |
| ED Registration | 2156-04-12 09:56:00 |
| ED Departure | 2156-04-12 17:11:00 |
| In-Hospital Mortality | No |
| Date of Death (overall) | N/A |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| APR | 720 | SEPTICEMIA & DISSEMINATED INFECTIONS | 4.0 | 4.0 |
| HCFA | 871 | SEPTICEMIA OR SEVERE SEPSIS W/O MV 96+ HOURS W MCC | N/A | N/A |

### Primary Diagnosis (seq_num = 1)

- **ICD-9 0383**: Septicemia due to anaerobes

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2156-04-12 14:17:27 | N/A | MED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-9 `0383`: Septicemia due to anaerobes
- (seq 2) ICD-9 `78552`: Septic shock
- (seq 3) ICD-9 `5184`: Acute edema of lung, unspecified
- (seq 4) ICD-9 `5845`: Acute kidney failure with lesion of tubular necrosis
- (seq 5) ICD-9 `5809`: Acute glomerulonephritis with unspecified pathological lesion in kidney

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-9 | `0383` | Septicemia due to anaerobes |
| 2 | ICD-9 | `78552` | Septic shock |
| 3 | ICD-9 | `5184` | Acute edema of lung, unspecified |
| 4 | ICD-9 | `5845` | Acute kidney failure with lesion of tubular necrosis |
| 5 | ICD-9 | `5809` | Acute glomerulonephritis with unspecified pathological lesion in kidney |
| 6 | ICD-9 | `34831` | Metabolic encephalopathy |
| 7 | ICD-9 | `486` | Pneumonia, organism unspecified |
| 8 | ICD-9 | `51881` | Acute respiratory failure |
| 9 | ICD-9 | `00845` | Intestinal infection due to Clostridium difficile |
| 10 | ICD-9 | `2762` | Acidosis |
| 11 | ICD-9 | `2761` | Hyposmolality and/or hyponatremia |
| 12 | ICD-9 | `5119` | Unspecified pleural effusion |
| 13 | ICD-9 | `78959` | Other ascites |
| 14 | ICD-9 | `5601` | Paralytic ileus |
| 15 | ICD-9 | `99592` | Severe sepsis |
| 16 | ICD-9 | `5641` | Irritable bowel syndrome |
| 17 | ICD-9 | `2859` | Anemia, unspecified |
| 18 | ICD-9 | `2720` | Pure hypercholesterolemia |
| 19 | ICD-9 | `4019` | Unspecified essential hypertension |
| 20 | ICD-9 | `2449` | Unspecified acquired hypothyroidism |
| 21 | ICD-9 | `4240` | Mitral valve disorders |
| 22 | ICD-9 | `53081` | Esophageal reflux |
| 23 | ICD-9 | `73300` | Osteoporosis, unspecified |
| 24 | ICD-9 | `4739` | Unspecified sinusitis (chronic) |
| 25 | ICD-9 | `7102` | Sicca syndrome |
| 26 | ICD-9 | `78097` | Altered mental status |
| 27 | ICD-9 | `E9478` | Other drugs and medicinal substances causing adverse effects in therapeutic use |
| 28 | ICD-9 | `4940` | Bronchiectasis without acute exacerbation |
| 29 | ICD-9 | `56210` | Diverticulosis of colon (without mention of hemorrhage) |
| 30 | ICD-9 | `53550` | Unspecified gastritis and gastroduodenitis, without mention of hemorrhage |
| 31 | ICD-9 | `5768` | Other specified disorders of biliary tract |
| 32 | ICD-9 | `7904` | Nonspecific elevation of levels of transaminase or lactic acid dehydrogenase [LDH] |
| 33 | ICD-9 | `5730` | Chronic passive congestion of liver |
| 34 | ICD-9 | `2875` | Thrombocytopenia, unspecified |

## 5. ICU Stays

| Stay ID | First Care Unit | Last Care Unit | ICU Admit | ICU Discharge | LOS (days) |
|---|---|---|---|---|---|
| 33987268 | Medical Intensive Care Unit (MICU) | Medical Intensive Care Unit (MICU) | 2156-04-12 16:24:18 | 2156-04-17 15:57:08 | 4.98 |
| 38875437 | Medical Intensive Care Unit (MICU) | Medical Intensive Care Unit (MICU) | 2156-04-19 18:11:19 | 2156-04-26 18:58:41 | 7.03 |

## 6. Escalation / Severity Indicators

The following critical conditions or interventions were detected:

- **Acute Kidney Injury** (ICD diagnosis)
- **Arterial Line** (ICU procedure event)
- **Invasive Mechanical Ventilation** (ICU procedure event)
- **Pneumonia** (ICD diagnosis)
- **Respiratory Failure** (ICD diagnosis)
- **Sepsis** (ICD diagnosis)
- **Shock** (ICD diagnosis)

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2156-04-19 | ICD-9 | `9604` | Insertion of endotracheal tube |
| 2 | 2156-04-19 | ICD-9 | `9671` | Continuous invasive mechanical ventilation for less than 96 consecutive hours |
| 3 | 2156-04-19 | ICD-9 | `3893` | Venous catheterization, not elsewhere classified |
| 4 | 2156-04-19 | ICD-9 | `3891` | Arterial catheterization |
| 5 | 2156-04-21 | ICD-9 | `3491` | Thoracentesis |
| 6 | 2156-04-21 | ICD-9 | `3409` | Other incision of pleura |
| 7 | 2156-04-20 | ICD-9 | `3324` | Closed [endoscopic] biopsy of bronchus |
| 8 | 2156-04-14 | ICD-9 | `3893` | Venous catheterization, not elsewhere classified |
| 9 | 2156-04-17 | ICD-9 | `9915` | Parenteral infusion of concentrated nutritional substances |
| 10 | 2156-04-24 | ICD-9 | `966` | Enteral infusion of concentrated nutritional substances |

### ICU Procedure Events (from `icu/procedureevents.csv.gz`)

- 18 Gauge (category: Access Lines - Peripheral, started: 2156-04-12 18:16:00, status: FinishedRunning)
- X-ray (category: 5-Imaging, started: 2156-04-13 09:32:00, status: FinishedRunning)
- Transthoracic Echo (category: 5-Imaging, started: 2156-04-13 14:36:00, status: FinishedRunning)
- PICC Line (category: Access Lines - Invasive, started: 2156-04-14 16:18:00, status: FinishedRunning)
- Family updated by RN (category: 7-Communication, started: 2156-04-19 19:30:00, status: FinishedRunning)
- Invasive Ventilation (category: 2-Ventilation, started: 2156-04-19 20:10:00, status: FinishedRunning)
- 20 Gauge (category: Access Lines - Peripheral, started: 2156-04-19 20:47:00, status: FinishedRunning)
- Multi Lumen (category: Access Lines - Invasive, started: 2156-04-19 21:02:00, status: FinishedRunning)
- Chest X-Ray (category: 5-Imaging, started: 2156-04-19 22:00:00, status: FinishedRunning)
- Arterial Line (category: Access Lines - Invasive, started: 2156-04-20 00:30:00, status: FinishedRunning)
- CT scan (category: 5-Imaging, started: 2156-04-20 02:15:00, status: FinishedRunning)
- Extubation (category: 1-Intubation/Extubation, started: 2156-04-22 17:10:00, status: FinishedRunning)

## 8. Critical Findings (Charted Events)

- **Ventilator Tank #2** (first noted: 2156-04-19 20:00:00)
- **Ventilator Mode** (first noted: 2156-04-19 20:00:00)
- **Ventilator Type** (first noted: 2156-04-19 20:00:00)
- **Known difficult intubation** (first noted: 2156-04-19 20:00:00)
- **Code Status** (first noted: 2156-04-14 23:07:00)
- **Stroke Volume Variation (SVV NICOM)** (first noted: 2156-04-20 10:45:00)
- **Stroke Volume Index (SVI NICOM)** (first noted: 2156-04-20 10:45:00)
- **Stroke Volume (SV NICOM)** (first noted: 2156-04-22 00:49:00)

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2156-04-12 09:56:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2156-04-12 09:56:00 | Transfer | → Emergency Department (ED) |
| 2156-04-12 14:16:00 | Admission | Admitted from EMERGENCY ROOM (EW EMER.) |
| 2156-04-12 16:00:59 | Transfer | → Emergency Department Observation (transfer) |
| 2156-04-12 16:24:18 | ICU Admission | Medical Intensive Care Unit (MICU) (LOS: 5.0 days) |
| 2156-04-12 16:24:18 | Transfer | → Medical Intensive Care Unit (MICU) (transfer) |
| 2156-04-12 17:11:00 | ED Departure | Left Emergency Dept. |
| 2156-04-17 15:57:08 | Transfer | → Medicine (transfer) |
| 2156-04-19 18:11:19 | ICU Admission | Medical Intensive Care Unit (MICU) (LOS: 7.0 days) |
| 2156-04-19 18:11:19 | Transfer | → Medical Intensive Care Unit (MICU) (transfer) |
| 2156-04-19 18:13:35 | Transfer | → Medical Intensive Care Unit (MICU) (transfer) |
| 2156-04-23 15:16:45 | Transfer | → Medical Intensive Care Unit (MICU) (transfer) |
| 2156-04-26 18:58:41 | Transfer | → Medicine (transfer) |
| 2156-04-29 16:26:00 | Discharge | To SKILLED NURSING FACILITY |

## 10. Missing / Ambiguous Data

- No obvious missing critical fields detected.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
