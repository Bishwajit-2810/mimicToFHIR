# Encounter Report — HADM 27738145

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 27738145 |
| Subject ID | 10019777 |
| Patient Sex | M |
| Patient Anchor Age (at anchor year) | 51 |
| Anchor Year | 2187 |
| Admission Time | 2187-02-10 18:57:00 |
| Discharge Time | 2187-02-27 13:22:00 |
| Admission Type | EW EMER. |
| Admission Location | EMERGENCY ROOM |
| Discharge Location | HOSPICE |
| Insurance | Other |
| Language | ENGLISH |
| Marital Status | DIVORCED |
| Race/Ethnicity | WHITE |
| ED Registration | 2187-02-10 15:11:00 |
| ED Departure | 2187-02-10 20:34:00 |
| In-Hospital Mortality | No |
| Date of Death (overall) | 2187-04-29 |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| APR | 264 | OTHER HEPATOBILIARY, PANCREAS & ABDOMINAL PROCEDURES | 4.0 | 3.0 |
| HCFA | 423 | OTHER HEPATOBILIARY OR PANCREAS O.R. PROCEDURES W MCC | N/A | N/A |

### Primary Diagnosis (seq_num = 1)

- **ICD-9 1571**: Malignant neoplasm of body of pancreas

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2187-02-10 18:58:08 | N/A | MED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-9 `1571`: Malignant neoplasm of body of pancreas
- (seq 2) ICD-9 `51881`: Acute respiratory failure
- (seq 3) ICD-9 `V4611`: Dependence on respirator, status
- (seq 4) ICD-9 `5579`: Unspecified vascular insufficiency of intestine
- (seq 5) ICD-9 `44489`: Embolism and thrombosis of other specified artery

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-9 | `1571` | Malignant neoplasm of body of pancreas |
| 2 | ICD-9 | `51881` | Acute respiratory failure |
| 3 | ICD-9 | `V4611` | Dependence on respirator, status |
| 4 | ICD-9 | `5579` | Unspecified vascular insufficiency of intestine |
| 5 | ICD-9 | `44489` | Embolism and thrombosis of other specified artery |
| 6 | ICD-9 | `99731` | Ventilator associated pneumonia |
| 7 | ICD-9 | `4589` | Hypotension, unspecified |
| 8 | ICD-9 | `1977` | Malignant neoplasm of liver, secondary |
| 9 | ICD-9 | `2851` | Acute posthemorrhagic anemia |
| 10 | ICD-9 | `5789` | Hemorrhage of gastrointestinal tract, unspecified |
| 11 | ICD-9 | `99674` | Other complications due to other vascular device, implant, and graft |
| 12 | ICD-9 | `7824` | Jaundice, unspecified, not of newborn |
| 13 | ICD-9 | `4568` | Varices of other sites |
| 14 | ICD-9 | `53081` | Esophageal reflux |
| 15 | ICD-9 | `311` | Depressive disorder, not elsewhere classified |
| 16 | ICD-9 | `30503` | Alcohol abuse, in remission |
| 17 | ICD-9 | `4471` | Stricture of artery |
| 18 | ICD-9 | `V1271` | Personal history of peptic ulcer disease |
| 19 | ICD-9 | `V1582` | Personal history of tobacco use |
| 20 | ICD-9 | `E8798` | Other specified procedures as the cause of abnormal reaction of patient, or of later complication, without mention of misadventure at time of procedure |
| 21 | ICD-9 | `28860` | Leukocytosis, unspecified |
| 22 | ICD-9 | `7904` | Nonspecific elevation of levels of transaminase or lactic acid dehydrogenase [LDH] |
| 23 | ICD-9 | `3383` | Neoplasm related pain (acute) (chronic) |
| 24 | ICD-9 | `56409` | Other constipation |
| 25 | ICD-9 | `4019` | Unspecified essential hypertension |
| 26 | ICD-9 | `78094` | Early satiety |
| 27 | ICD-9 | `56889` | Other specified disorders of peritoneum |
| 28 | ICD-9 | `E9358` | Other specified analgesics and antipyretics causing adverse effects in therapeutic use |
| 29 | ICD-9 | `E8497` | Accidents occurring in residential institution |
| 30 | ICD-9 | `E8889` | Unspecified fall |
| 31 | ICD-9 | `V4986` | Do not resuscitate status |

## 5. ICU Stays

| Stay ID | First Care Unit | Last Care Unit | ICU Admit | ICU Discharge | LOS (days) |
|---|---|---|---|---|---|
| 34578020 | Medical Intensive Care Unit (MICU) | Medical Intensive Care Unit (MICU) | 2187-02-10 20:34:00 | 2187-02-17 23:38:57 | 7.13 |

## 6. Escalation / Severity Indicators

The following critical conditions or interventions were detected:

- **Invasive Mechanical Ventilation** (ICU procedure event)
- **Respiratory Failure** (ICD diagnosis)

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2187-02-10 | ICD-9 | `5211` | Closed [aspiration] [needle] [percutaneous] biopsy of pancreas |
| 2 | 2187-02-12 | ICD-9 | `3950` | Angioplasty of other non-coronary vessel(s) |
| 3 | 2187-02-14 | ICD-9 | `3979` | Other endovascular procedures on other vessels |
| 4 | 2187-02-10 | ICD-9 | `4444` | Transcatheter embolization for gastric or duodenal bleeding |
| 5 | 2187-02-10 | ICD-9 | `4513` | Other endoscopy of small intestine |
| 6 | 2187-02-10 | ICD-9 | `8874` | Diagnostic ultrasound of digestive system |
| 7 | 2187-02-11 | ICD-9 | `4443` | Endoscopic control of gastric or duodenal bleeding |
| 8 | 2187-02-13 | ICD-9 | `4513` | Other endoscopy of small intestine |
| 9 | 2187-02-10 | ICD-9 | `8847` | Arteriography of other intra-abdominal arteries |
| 10 | 2187-02-10 | ICD-9 | `8848` | Arteriography of femoral and other lower extremity arteries |
| 11 | 2187-02-12 | ICD-9 | `8847` | Arteriography of other intra-abdominal arteries |
| 12 | 2187-02-12 | ICD-9 | `3893` | Venous catheterization, not elsewhere classified |
| 13 | 2187-02-12 | ICD-9 | `8864` | Phlebography of the portal venous system using contrast material |
| 14 | 2187-02-12 | ICD-9 | `9910` | Injection or infusion of thrombolytic agent |
| 15 | 2187-02-13 | ICD-9 | `8847` | Arteriography of other intra-abdominal arteries |
| 16 | 2187-02-12 | ICD-9 | `3897` | Central venous catheter placement with guidance |
| 17 | 2187-02-14 | ICD-9 | `3897` | Central venous catheter placement with guidance |
| 18 | 2187-02-12 | ICD-9 | `3990` | Insertion of non-drug-eluting peripheral (non-coronary) vessel stent(s) |
| 19 | 2187-02-12 | ICD-9 | `0045` | Insertion of one vascular stent |
| 20 | 2187-02-12 | ICD-9 | `0040` | Procedure on single vessel |
| 21 | 2187-02-10 | ICD-9 | `9672` | Continuous invasive mechanical ventilation for 96 consecutive hours or more |
| 22 | 2187-02-10 | ICD-9 | `9604` | Insertion of endotracheal tube |
| 23 | 2187-02-14 | ICD-9 | `8849` | Arteriography of other specified sites |

### ICU Procedure Events (from `icu/procedureevents.csv.gz`)

- Foley Catheter (category: GI/GU, started: 2187-02-10 19:00:00, status: FinishedRunning)
- Interventional Radiology (category: 5-Imaging, started: 2187-02-10 21:00:00, status: FinishedRunning)
- Invasive Ventilation (category: 2-Ventilation, started: 2187-02-10 23:00:00, status: FinishedRunning)
- Cordis/Introducer (category: Access Lines - Invasive, started: 2187-02-10 23:30:00, status: FinishedRunning)
- 18 Gauge (category: Access Lines - Peripheral, started: 2187-02-10 23:30:00, status: FinishedRunning)
- Family updated by RN (category: 7-Communication, started: 2187-02-11 00:30:00, status: FinishedRunning)
- Trauma line (category: Access Lines - Invasive, started: 2187-02-12 15:12:00, status: FinishedRunning)
- Multi Lumen (category: Access Lines - Invasive, started: 2187-02-12 19:34:00, status: FinishedRunning)
- Blood Cultured (category: 6-Cultures, started: 2187-02-13 03:26:00, status: FinishedRunning)
- Ultrasound (category: 5-Imaging, started: 2187-02-13 17:28:00, status: FinishedRunning)
- Endoscopy (category: 4-Procedures, started: 2187-02-13 18:15:00, status: FinishedRunning)
- CT scan (category: 5-Imaging, started: 2187-02-13 20:00:00, status: FinishedRunning)
- OR Sent (category: 3-Significant Events, started: 2187-02-14 11:00:00, status: FinishedRunning)
- OR Received (category: 3-Significant Events, started: 2187-02-14 13:30:00, status: FinishedRunning)
- Chest X-Ray (category: 5-Imaging, started: 2187-02-14 17:24:00, status: FinishedRunning)
- Extubation (category: 1-Intubation/Extubation, started: 2187-02-16 10:55:00, status: FinishedRunning)

## 8. Critical Findings (Charted Events)

- **Ventilator Type** (first noted: 2187-02-10 23:00:00)
- **Ventilator Mode** (first noted: 2187-02-10 23:00:00)
- **Ventilator Tank #2** (first noted: 2187-02-10 23:00:00)
- **Known difficult intubation** (first noted: 2187-02-10 23:00:00)
- **Code Status.** (first noted: 2187-02-13 03:44:00)
- **Code Status** (first noted: 2187-02-12 23:35:00)

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2187-02-10 15:11:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2187-02-10 15:11:00 | Transfer | → Emergency Department (ED) |
| 2187-02-10 18:57:00 | Admission | Admitted from EMERGENCY ROOM (EW EMER.) |
| 2187-02-10 20:34:00 | ED Departure | Left Emergency Dept. |
| 2187-02-10 20:34:00 | ICU Admission | Medical Intensive Care Unit (MICU) (LOS: 7.1 days) |
| 2187-02-17 23:38:57 | Transfer | → Hematology/Oncology (transfer) |
| 2187-02-19 17:19:43 | Transfer | → Hematology/Oncology (transfer) |
| 2187-02-21 23:31:46 | Transfer | → Hematology/Oncology (transfer) |
| 2187-02-27 10:24:32 | Transfer | → Hematology/Oncology (transfer) |
| 2187-02-27 13:22:00 | Discharge | To HOSPICE |

## 10. Missing / Ambiguous Data

- No obvious missing critical fields detected.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
