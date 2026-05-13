# Encounter Report — HADM 28889419

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 28889419 |
| Subject ID | 10014729 |
| Patient Sex | F |
| Patient Anchor Age (at anchor year) | 21 |
| Anchor Year | 2125 |
| Admission Time | 2125-02-27 07:15:00 |
| Discharge Time | 2125-03-06 14:25:00 |
| Admission Type | SURGICAL SAME DAY ADMISSION |
| Admission Location | PHYSICIAN REFERRAL |
| Discharge Location | HOME HEALTH CARE |
| Insurance | Other |
| Language | ENGLISH |
| Marital Status | SINGLE |
| Race/Ethnicity | WHITE - OTHER EUROPEAN |
| ED Registration | N/A |
| ED Departure | N/A |
| In-Hospital Mortality | No |
| Date of Death (overall) | N/A |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| HCFA | 908 | OTHER O.R. PROCEDURES FOR INJURIES W CC | N/A | N/A |
| APR | 169 | MAJOR ABDOMINAL VASCULAR PROCEDURES | 2.0 | 3.0 |

### Primary Diagnosis (seq_num = 1)

- **ICD-9 9010**: Injury to thoracic aorta

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2125-02-27 04:14:41 | N/A | CSURG |
| 2125-02-27 16:17:02 | CSURG | VSURG |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-9 `9010`: Injury to thoracic aorta
- (seq 2) ICD-9 `9962`: Mechanical complication of nervous system device, implant, and graft
- (seq 3) ICD-9 `49390`: Asthma, unspecified type, unspecified
- (seq 4) ICD-9 `V1204`: Personal history of Methicillin resistant Staphylococcus aureus
- (seq 5) ICD-9 `E8120`: Other motor vehicle traffic accident involving collision with motor vehicle injuring driver of motor vehicle other than motorcycle

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-9 | `9010` | Injury to thoracic aorta |
| 2 | ICD-9 | `9962` | Mechanical complication of nervous system device, implant, and graft |
| 3 | ICD-9 | `49390` | Asthma, unspecified type, unspecified |
| 4 | ICD-9 | `V1204` | Personal history of Methicillin resistant Staphylococcus aureus |
| 5 | ICD-9 | `E8120` | Other motor vehicle traffic accident involving collision with motor vehicle injuring driver of motor vehicle other than motorcycle |
| 6 | ICD-9 | `E8798` | Other specified procedures as the cause of abnormal reaction of patient, or of later complication, without mention of misadventure at time of procedure |
| 7 | ICD-9 | `E8495` | Street and highway accidents |
| 8 | ICD-9 | `E8497` | Accidents occurring in residential institution |

## 5. ICU Stays

| Stay ID | First Care Unit | Last Care Unit | ICU Admit | ICU Discharge | LOS (days) |
|---|---|---|---|---|---|
| 33558396 | Cardiac Vascular Intensive Care Unit (CVICU) | Cardiac Vascular Intensive Care Unit (CVICU) | 2125-02-27 10:03:08 | 2125-03-01 21:21:37 | 2.47 |

## 6. Escalation / Severity Indicators

The following critical conditions or interventions were detected:

- **Arterial Line** (ICU procedure event)
- **Invasive Mechanical Ventilation** (ICU procedure event)

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2125-02-27 | ICD-9 | `3845` | Resection of vessel with replacement, thoracic vessels |
| 2 | 2125-02-27 | ICD-9 | `3959` | Other repair of vessel |
| 3 | 2125-02-27 | ICD-9 | `3961` | Extracorporeal circulation auxiliary to open heart surgery |
| 4 | 2125-02-28 | ICD-9 | `0390` | Insertion of catheter into spinal canal for infusion of therapeutic or palliative substances |
| 5 | 2125-02-28 | ICD-9 | `0391` | Injection of anesthetic into spinal canal for analgesia |
| 6 | 2125-03-03 | ICD-9 | `8605` | Incision with removal of foreign body or device from skin and subcutaneous tissue |

### ICU Procedure Events (from `icu/procedureevents.csv.gz`)

- Invasive Ventilation (category: 2-Ventilation, started: 2125-02-27 14:45:00, status: FinishedRunning)
- Cordis/Introducer (category: Access Lines - Invasive, started: 2125-02-27 14:45:00, status: FinishedRunning)
- CCO PAC (category: Access Lines - Invasive, started: 2125-02-27 14:45:00, status: FinishedRunning)
- 16 Gauge (category: Access Lines - Peripheral, started: 2125-02-27 14:45:00, status: FinishedRunning)
- 18 Gauge (category: Access Lines - Peripheral, started: 2125-02-27 14:45:00, status: FinishedRunning)
- OR Received (category: 3-Significant Events, started: 2125-02-27 14:45:00, status: FinishedRunning)
- Arterial Line (category: Access Lines - Invasive, started: 2125-02-27 14:45:00, status: FinishedRunning)
- Extubation (category: 1-Intubation/Extubation, started: 2125-02-27 19:04:00, status: FinishedRunning)
- Epidural Placement (category: 4-Procedures, started: 2125-02-28 11:46:00, status: FinishedRunning)
- Chest Tube Removed (category: 4-Procedures, started: 2125-03-01 09:23:00, status: FinishedRunning)
- Chest X-Ray (category: 5-Imaging, started: 2125-03-01 09:45:00, status: FinishedRunning)

## 8. Critical Findings (Charted Events)

- **Ventilator Tank #2** (first noted: 2125-02-27 15:00:00)
- **Ventilator Mode** (first noted: 2125-02-27 15:00:00)
- **Ventilator Type** (first noted: 2125-02-27 15:00:00)
- **Known difficult intubation** (first noted: 2125-02-27 15:00:00)
- **Code Status** (first noted: 2125-02-27 10:03:00)
- **Dialysis patient** (first noted: 2125-02-27 12:35:00)

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2125-02-27 07:15:00 | Admission | Admitted from PHYSICIAN REFERRAL (SURGICAL SAME DAY ADMISSION) |
| 2125-02-27 10:03:08 | ICU Admission | Cardiac Vascular Intensive Care Unit (CVICU) (LOS: 2.5 days) |
| 2125-02-27 10:03:08 | Transfer | → Cardiac Vascular Intensive Care Unit (CVICU) (transfer) |
| 2125-03-01 21:21:37 | Transfer | → Vascular (transfer) |
| 2125-03-06 14:25:00 | Discharge | To HOME HEALTH CARE |

## 10. Missing / Ambiguous Data

- No ED registration time — admission may not have gone through ED.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
