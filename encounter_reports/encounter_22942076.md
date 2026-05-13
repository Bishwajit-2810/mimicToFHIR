# Encounter Report — HADM 22942076

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 22942076 |
| Subject ID | 10006053 |
| Patient Sex | M |
| Patient Anchor Age (at anchor year) | 52 |
| Anchor Year | 2111 |
| Admission Time | 2111-11-13 23:39:00 |
| Discharge Time | 2111-11-15 17:20:00 |
| Admission Type | URGENT |
| Admission Location | TRANSFER FROM HOSPITAL |
| Discharge Location | DIED |
| Insurance | Medicaid |
| Language | ENGLISH |
| Marital Status | N/A |
| Race/Ethnicity | UNKNOWN |
| ED Registration | N/A |
| ED Departure | N/A |
| In-Hospital Mortality | YES — Death time: 2111-11-15 17:20:00 |
| Date of Death (overall) | 2111-11-15 |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| APR | 260 | MAJOR PANCREAS, LIVER & SHUNT PROCEDURES | 4.0 | 4.0 |
| HCFA | 405 | PANCREAS, LIVER & SHUNT PROCEDURES W MCC | N/A | N/A |

### Primary Diagnosis (seq_num = 1)

- **ICD-9 5722**: Hepatic encephalopathy

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2111-11-13 23:40:00 | N/A | MED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-9 `5722`: Hepatic encephalopathy
- (seq 2) ICD-9 `2866`: Defibrination syndrome
- (seq 3) ICD-9 `41071`: Subendocardial infarction, initial episode of care
- (seq 4) ICD-9 `45620`: Esophageal varices in diseases classified elsewhere, with bleeding
- (seq 5) ICD-9 `5845`: Acute kidney failure with lesion of tubular necrosis

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-9 | `5722` | Hepatic encephalopathy |
| 2 | ICD-9 | `2866` | Defibrination syndrome |
| 3 | ICD-9 | `41071` | Subendocardial infarction, initial episode of care |
| 4 | ICD-9 | `45620` | Esophageal varices in diseases classified elsewhere, with bleeding |
| 5 | ICD-9 | `5845` | Acute kidney failure with lesion of tubular necrosis |
| 6 | ICD-9 | `78959` | Other ascites |
| 7 | ICD-9 | `5712` | Alcoholic cirrhosis of liver |
| 8 | ICD-9 | `30301` | Acute alcoholic intoxication in alcoholism, continuous |
| 9 | ICD-9 | `5711` | Acute alcoholic hepatitis |
| 10 | ICD-9 | `45989` | Other specified disorders of circulatory system |

## 5. ICU Stays

| Stay ID | First Care Unit | Last Care Unit | ICU Admit | ICU Discharge | LOS (days) |
|---|---|---|---|---|---|
| 32895909 | Medical Intensive Care Unit (MICU) | Medical Intensive Care Unit (MICU) | 2111-11-13 23:40:00 | 2111-11-14 00:14:10 | 0.02 |
| 34617352 | Medical Intensive Care Unit (MICU) | Medical Intensive Care Unit (MICU) | 2111-11-14 00:19:12 | 2111-11-15 18:21:10 | 1.75 |

## 6. Escalation / Severity Indicators

The following critical conditions or interventions were detected:

- **Acute Kidney Injury** (ICD diagnosis)
- **Arterial Line** (ICU procedure event)
- **DIC** (ICD diagnosis)
- **Invasive Mechanical Ventilation** (ICU procedure event)
- **Liver Failure** (ICD diagnosis)

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2111-11-15 | ICD-9 | `5491` | Percutaneous abdominal drainage |
| 2 | 2111-11-15 | ICD-9 | `391` | Intra-abdominal venous shunt |
| 3 | 2111-11-15 | ICD-9 | `3893` | Venous catheterization, not elsewhere classified |

### ICU Procedure Events (from `icu/procedureevents.csv.gz`)

- Multi Lumen (category: Access Lines - Invasive, started: 2111-11-14 01:00:00, status: FinishedRunning)
- 20 Gauge (category: Access Lines - Peripheral, started: 2111-11-14 01:00:00, status: FinishedRunning)
- 16 Gauge (category: Access Lines - Peripheral, started: 2111-11-14 01:00:00, status: FinishedRunning)
- Invasive Ventilation (category: 2-Ventilation, started: 2111-11-14 02:00:00, status: FinishedRunning)
- Arterial Line (category: Access Lines - Invasive, started: 2111-11-14 02:00:00, status: FinishedRunning)
- Ultrasound (category: 5-Imaging, started: 2111-11-15 08:38:00, status: FinishedRunning)
- Blakemore / MinnesotaTube Inserted (category: 4-Procedures, started: 2111-11-15 12:06:00, status: FinishedRunning)
- Chest X-Ray (category: 5-Imaging, started: 2111-11-15 12:06:00, status: FinishedRunning)

## 8. Critical Findings (Charted Events)

- **Ventilator Mode** (first noted: 2111-11-14 00:19:00)
- **Ventilator Type** (first noted: 2111-11-14 00:00:00)
- **Ventilator Tank #1** (first noted: 2111-11-14 00:00:00)
- **Code Status** (first noted: 2111-11-14 00:24:00)

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2111-11-13 23:39:00 | Admission | Admitted from TRANSFER FROM HOSPITAL (URGENT) |
| 2111-11-13 23:40:00 | ICU Admission | Medical Intensive Care Unit (MICU) (LOS: 0.0 days) |
| 2111-11-14 00:14:10 | Transfer | → Discharge Lounge (transfer) |
| 2111-11-14 00:19:12 | ICU Admission | Medical Intensive Care Unit (MICU) (LOS: 1.8 days) |
| 2111-11-14 00:19:12 | Transfer | → Medical Intensive Care Unit (MICU) (transfer) |
| 2111-11-15 17:20:00 | **IN-HOSPITAL DEATH** | |
| 2111-11-15 17:20:00 | Discharge | To DIED |

## 10. Missing / Ambiguous Data

- No ED registration time — admission may not have gone through ED.

## 11. Manual Review Recommendation

**This encounter is flagged for manual review:**

- Patient expired in-hospital but cause of death not clearly coded.
