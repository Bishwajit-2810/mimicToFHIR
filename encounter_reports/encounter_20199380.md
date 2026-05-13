# Encounter Report — HADM 20199380

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 20199380 |
| Subject ID | 10005909 |
| Patient Sex | F |
| Patient Anchor Age (at anchor year) | 40 |
| Anchor Year | 2144 |
| Admission Time | 2144-10-28 23:20:00 |
| Discharge Time | 2144-11-02 15:23:00 |
| Admission Type | OBSERVATION ADMIT |
| Admission Location | EMERGENCY ROOM |
| Discharge Location | HOME |
| Insurance | Other |
| Language | ENGLISH |
| Marital Status | MARRIED |
| Race/Ethnicity | WHITE |
| ED Registration | 2144-10-28 18:29:00 |
| ED Departure | 2144-10-29 00:10:00 |
| In-Hospital Mortality | No |
| Date of Death (overall) | N/A |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| HCFA | 271 | OTHER MAJOR CARDIOVASCULAR PROCEDURES W CC | N/A | N/A |

### Primary Diagnosis (seq_num = 1)

- **ICD-10 I82422**: Acute embolism and thrombosis of left iliac vein

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2144-10-28 23:20:44 | N/A | VSURG |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-10 `I82422`: Acute embolism and thrombosis of left iliac vein
- (seq 2) ICD-10 `I871`: Compression of vein
- (seq 3) ICD-10 `I9751`: Accidental puncture and laceration of a circulatory system organ or structure during a circulatory system procedure
- (seq 4) ICD-10 `Y838`: Other surgical procedures as the cause of abnormal reaction of the patient, or of later complication, without mention of misadventure at the time of the procedure
- (seq 5) ICD-10 `Y92234`: Operating room of hospital as the place of occurrence of the external cause

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-10 | `I82422` | Acute embolism and thrombosis of left iliac vein |
| 2 | ICD-10 | `I871` | Compression of vein |
| 3 | ICD-10 | `I9751` | Accidental puncture and laceration of a circulatory system organ or structure during a circulatory system procedure |
| 4 | ICD-10 | `Y838` | Other surgical procedures as the cause of abnormal reaction of the patient, or of later complication, without mention of misadventure at the time of the procedure |
| 5 | ICD-10 | `Y92234` | Operating room of hospital as the place of occurrence of the external cause |

## 5. ICU Stays

| Stay ID | First Care Unit | Last Care Unit | ICU Admit | ICU Discharge | LOS (days) |
|---|---|---|---|---|---|
| 36496303 | Cardiac Vascular Intensive Care Unit (CVICU) | Cardiac Vascular Intensive Care Unit (CVICU) | 2144-10-29 23:09:03 | 2144-11-02 15:24:29 | 3.68 |

## 6. Escalation / Severity Indicators

_No escalation indicators detected from ICD codes or ICU procedure events._

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2144-10-29 | ICD-10 | `06CD3ZZ` | Extirpation of Matter from Left Common Iliac Vein, Percutaneous Approach |
| 2 | 2144-10-29 | ICD-10 | `06H03DZ` | Insertion of Intraluminal Device into Inferior Vena Cava, Percutaneous Approach |
| 3 | 2144-10-31 | ICD-10 | `06CD3ZZ` | Extirpation of Matter from Left Common Iliac Vein, Percutaneous Approach |
| 4 | 2144-10-31 | ICD-10 | `06CN3ZZ` | Extirpation of Matter from Left Femoral Vein, Percutaneous Approach |
| 5 | 2144-10-31 | ICD-10 | `067D3DZ` | Dilation of Left Common Iliac Vein with Intraluminal Device, Percutaneous Approach |
| 6 | 2144-10-31 | ICD-10 | `067G3DZ` | Dilation of Left External Iliac Vein with Intraluminal Device, Percutaneous Approach |
| 7 | 2144-10-29 | ICD-10 | `3E03317` | Introduction of Other Thrombolytic into Peripheral Vein, Percutaneous Approach |

### ICU Procedure Events (from `icu/procedureevents.csv.gz`)

- 20 Gauge (category: Access Lines - Peripheral, started: 2144-10-29 23:56:00, status: FinishedRunning)
- OR Sent (category: 3-Significant Events, started: 2144-10-31 10:50:00, status: FinishedRunning)
- 18 Gauge (category: Access Lines - Peripheral, started: 2144-10-31 15:45:00, status: FinishedRunning)
- OR Received (category: 3-Significant Events, started: 2144-10-31 15:47:00, status: FinishedRunning)

## 8. Critical Findings (Charted Events)

_No critical chart events detected._

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2144-10-28 18:29:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2144-10-28 18:29:00 | Transfer | → Emergency Department (ED) |
| 2144-10-28 23:20:00 | Admission | Admitted from EMERGENCY ROOM (OBSERVATION ADMIT) |
| 2144-10-29 00:10:00 | ED Departure | Left Emergency Dept. |
| 2144-10-29 09:16:41 | Transfer | → Med/Surg (transfer) |
| 2144-10-29 12:05:08 | Transfer | → PACU (transfer) |
| 2144-10-29 23:09:03 | ICU Admission | Cardiac Vascular Intensive Care Unit (CVICU) (LOS: 3.7 days) |
| 2144-10-29 23:09:03 | Transfer | → Cardiac Vascular Intensive Care Unit (CVICU) (transfer) |
| 2144-10-30 18:52:43 | Transfer | → Cardiac Vascular Intensive Care Unit (CVICU) (transfer) |
| 2144-11-02 15:23:00 | Discharge | To HOME |

## 10. Missing / Ambiguous Data

- No obvious missing critical fields detected.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
