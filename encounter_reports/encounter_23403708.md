# Encounter Report — HADM 23403708

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 23403708 |
| Subject ID | 10025612 |
| Patient Sex | M |
| Patient Anchor Age (at anchor year) | 82 |
| Anchor Year | 2125 |
| Admission Time | 2125-09-25 07:15:00 |
| Discharge Time | 2125-10-03 12:24:00 |
| Admission Type | SURGICAL SAME DAY ADMISSION |
| Admission Location | PHYSICIAN REFERRAL |
| Discharge Location | HOME HEALTH CARE |
| Insurance | Medicare |
| Language | ENGLISH |
| Marital Status | MARRIED |
| Race/Ethnicity | WHITE |
| ED Registration | N/A |
| ED Departure | N/A |
| In-Hospital Mortality | No |
| Date of Death (overall) | N/A |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| APR | 120 | MAJOR RESPIRATORY & CHEST PROCEDURES | 2.0 | 1.0 |
| HCFA | 164 | MAJOR CHEST PROCEDURES W CC | N/A | N/A |

### Primary Diagnosis (seq_num = 1)

- **ICD-9 1622**: Malignant neoplasm of main bronchus

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2125-09-25 00:56:40 | N/A | TSURG |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-9 `1622`: Malignant neoplasm of main bronchus
- (seq 2) ICD-9 `99811`: Hemorrhage complicating a procedure
- (seq 3) ICD-9 `51189`: Other specified forms of effusion, except tuberculous
- (seq 4) ICD-9 `2851`: Acute posthemorrhagic anemia
- (seq 5) ICD-9 `E8786`: Removal of other organ (partial) (total) causing abnormal patient reaction, or later complication, without mention of misadventure at time of operation

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-9 | `1622` | Malignant neoplasm of main bronchus |
| 2 | ICD-9 | `99811` | Hemorrhage complicating a procedure |
| 3 | ICD-9 | `51189` | Other specified forms of effusion, except tuberculous |
| 4 | ICD-9 | `2851` | Acute posthemorrhagic anemia |
| 5 | ICD-9 | `E8786` | Removal of other organ (partial) (total) causing abnormal patient reaction, or later complication, without mention of misadventure at time of operation |
| 6 | ICD-9 | `E8497` | Accidents occurring in residential institution |
| 7 | ICD-9 | `V103` | Personal history of malignant neoplasm of breast |
| 8 | ICD-9 | `V1582` | Personal history of tobacco use |
| 9 | ICD-9 | `2449` | Unspecified acquired hypothyroidism |
| 10 | ICD-9 | `36250` | Macular degeneration (senile), unspecified |
| 11 | ICD-9 | `V8741` | Personal history of antineoplastic chemotherapy |
| 12 | ICD-9 | `V4561` | Cataract extraction status |
| 13 | ICD-9 | `V431` | Lens replaced by other means |
| 14 | ICD-9 | `V163` | Family history of malignant neoplasm of breast |
| 15 | ICD-9 | `V1642` | Family history of malignant neoplasm of prostate |
| 16 | ICD-9 | `33818` | Other acute postoperative pain |

## 5. ICU Stays

| Stay ID | First Care Unit | Last Care Unit | ICU Admit | ICU Discharge | LOS (days) |
|---|---|---|---|---|---|
| 32587226 | Surgical Intensive Care Unit (SICU) | Surgical Intensive Care Unit (SICU) | 2125-09-25 13:23:24 | 2125-09-30 18:54:33 | 5.23 |

## 6. Escalation / Severity Indicators

The following critical conditions or interventions were detected:

- **Arterial Line** (ICU procedure event)
- **Endotracheal Intubation** (ICU procedure event)
- **Invasive Mechanical Ventilation** (ICU procedure event)

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2125-09-27 | ICD-9 | `3348` | Other repair and plastic operations on bronchus |
| 2 | 2125-09-25 | ICD-9 | `3259` | Other and unspecified pneumonectomy |
| 3 | 2125-09-25 | ICD-9 | `3422` | Mediastinoscopy |
| 4 | 2125-09-25 | ICD-9 | `4011` | Biopsy of lymphatic structure |
| 5 | 2125-09-25 | ICD-9 | `3328` | Open biopsy of lung |
| 6 | 2125-09-25 | ICD-9 | `4059` | Radical excision of other lymph nodes |
| 7 | 2125-09-25 | ICD-9 | `3479` | Other repair of chest wall |
| 8 | 2125-09-27 | ICD-9 | `3403` | Reopening of recent thoracotomy site |
| 9 | 2125-09-25 | ICD-9 | `3324` | Closed [endoscopic] biopsy of bronchus |
| 10 | 2125-09-25 | ICD-9 | `0390` | Insertion of catheter into spinal canal for infusion of therapeutic or palliative substances |

### ICU Procedure Events (from `icu/procedureevents.csv.gz`)

- 18 Gauge (category: Access Lines - Peripheral, started: 2125-09-25 13:24:00, status: FinishedRunning)
- Arterial Line (category: Access Lines - Invasive, started: 2125-09-25 13:30:00, status: FinishedRunning)
- X-ray (category: 5-Imaging, started: 2125-09-27 00:00:00, status: FinishedRunning)
- Chest Tube Placed (category: 4-Procedures, started: 2125-09-27 01:30:00, status: FinishedRunning)
- Invasive Ventilation (category: 2-Ventilation, started: 2125-09-27 02:00:00, status: FinishedRunning)
- Intubation (category: 1-Intubation/Extubation, started: 2125-09-27 02:00:00, status: FinishedRunning)
- Family updated by MD (category: 7-Communication, started: 2125-09-27 02:15:00, status: FinishedRunning)
- OR Sent (category: 3-Significant Events, started: 2125-09-27 02:30:00, status: FinishedRunning)
- Ultrasound (category: 5-Imaging, started: 2125-09-27 04:28:00, status: FinishedRunning)
- Extubation (category: 1-Intubation/Extubation, started: 2125-09-27 09:52:00, status: FinishedRunning)
- EKG (category: 4-Procedures, started: 2125-09-27 10:28:00, status: FinishedRunning)
- Multi Lumen (category: Access Lines - Invasive, started: 2125-09-27 14:18:00, status: FinishedRunning)
- Chest X-Ray (category: 5-Imaging, started: 2125-09-28 03:00:00, status: FinishedRunning)
- Transthoracic Echo (category: 5-Imaging, started: 2125-09-28 09:00:00, status: FinishedRunning)
- 20 Gauge (category: Access Lines - Peripheral, started: 2125-09-30 16:30:00, status: FinishedRunning)

## 8. Critical Findings (Charted Events)

- **Ventilator Type** (first noted: 2125-09-27 02:00:00)
- **Ventilator Mode** (first noted: 2125-09-27 02:00:00)
- **Ventilator Tank #1** (first noted: 2125-09-27 05:00:00)
- **Known difficult intubation** (first noted: 2125-09-27 02:00:00)
- **Code Status** (first noted: 2125-09-27 03:07:00)

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2125-09-25 07:15:00 | Admission | Admitted from PHYSICIAN REFERRAL (SURGICAL SAME DAY ADMISSION) |
| 2125-09-25 13:23:24 | ICU Admission | Surgical Intensive Care Unit (SICU) (LOS: 5.2 days) |
| 2125-09-25 13:23:24 | Transfer | → Surgical Intensive Care Unit (SICU) (transfer) |
| 2125-09-30 18:54:33 | Transfer | → Med/Surg (transfer) |
| 2125-10-03 12:24:00 | Discharge | To HOME HEALTH CARE |

## 10. Missing / Ambiguous Data

- No ED registration time — admission may not have gone through ED.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
