# Encounter Report — HADM 28477357

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 28477357 |
| Subject ID | 10007795 |
| Patient Sex | F |
| Patient Anchor Age (at anchor year) | 53 |
| Anchor Year | 2136 |
| Admission Time | 2136-04-10 20:33:00 |
| Discharge Time | 2136-05-02 16:35:00 |
| Admission Type | URGENT |
| Admission Location | TRANSFER FROM HOSPITAL |
| Discharge Location | CHRONIC/LONG TERM ACUTE CARE |
| Insurance | Medicare |
| Language | ENGLISH |
| Marital Status | SINGLE |
| Race/Ethnicity | WHITE |
| ED Registration | N/A |
| ED Departure | N/A |
| In-Hospital Mortality | No |
| Date of Death (overall) | N/A |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| APR | 264 | OTHER HEPATOBILIARY, PANCREAS & ABDOMINAL PROCEDURES | 4.0 | 3.0 |
| HCFA | 423 | OTHER HEPATOBILIARY OR PANCREAS O.R. PROCEDURES W MCC | N/A | N/A |

### Primary Diagnosis (seq_num = 1)

- **ICD-9 5772**: Cyst and pseudocyst of pancreas

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2136-04-10 20:34:05 | N/A | MED |
| 2136-04-23 19:13:38 | MED | SURG |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-9 `5772`: Cyst and pseudocyst of pancreas
- (seq 2) ICD-9 `5770`: Acute pancreatitis
- (seq 3) ICD-9 `486`: Pneumonia, organism unspecified
- (seq 4) ICD-9 `5184`: Acute edema of lung, unspecified
- (seq 5) ICD-9 `5180`: Pulmonary collapse

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-9 | `5772` | Cyst and pseudocyst of pancreas |
| 2 | ICD-9 | `5770` | Acute pancreatitis |
| 3 | ICD-9 | `486` | Pneumonia, organism unspecified |
| 4 | ICD-9 | `5184` | Acute edema of lung, unspecified |
| 5 | ICD-9 | `5180` | Pulmonary collapse |
| 6 | ICD-9 | `11289` | Other candidiasis of other specified sites |
| 7 | ICD-9 | `2869` | Other and unspecified coagulation defects |
| 8 | ICD-9 | `5771` | Chronic pancreatitis |
| 9 | ICD-9 | `5711` | Acute alcoholic hepatitis |
| 10 | ICD-9 | `30393` | Other and unspecified alcohol dependence, in remission |
| 11 | ICD-9 | `4019` | Unspecified essential hypertension |
| 12 | ICD-9 | `2720` | Pure hypercholesterolemia |
| 13 | ICD-9 | `24900` | Secondary diabetes mellitus without mention of complication, not stated as uncontrolled, or unspecified |
| 14 | ICD-9 | `V5867` | Long-term (current) use of insulin |
| 15 | ICD-9 | `311` | Depressive disorder, not elsewhere classified |
| 16 | ICD-9 | `28529` | Anemia of other chronic disease |
| 17 | ICD-9 | `V103` | Personal history of malignant neoplasm of breast |
| 18 | ICD-9 | `79311` | Solitary pulmonary nodule |
| 19 | ICD-9 | `56210` | Diverticulosis of colon (without mention of hemorrhage) |
| 20 | ICD-9 | `V443` | Colostomy status |
| 21 | ICD-9 | `6930` | Dermatitis due to drugs and medicines taken internally |
| 22 | ICD-9 | `E9319` | Other and unspecified anti-infectives causing adverse effects in therapeutic use |
| 23 | ICD-9 | `E8497` | Accidents occurring in residential institution |

## 5. ICU Stays

| Stay ID | First Care Unit | Last Care Unit | ICU Admit | ICU Discharge | LOS (days) |
|---|---|---|---|---|---|
| 31921355 | Medical/Surgical Intensive Care Unit (MICU/SICU) | Medical/Surgical Intensive Care Unit (MICU/SICU) | 2136-04-22 18:01:13 | 2136-04-23 19:13:58 | 1.05 |

## 6. Escalation / Severity Indicators

The following critical conditions or interventions were detected:

- **Pneumonia** (ICD diagnosis)

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2136-04-11 | ICD-9 | `9915` | Parenteral infusion of concentrated nutritional substances |
| 2 | 2136-04-13 | ICD-9 | `4699` | Other operations on intestines |
| 3 | 2136-04-17 | ICD-9 | `4699` | Other operations on intestines |
| 4 | 2136-04-13 | ICD-9 | `4513` | Other endoscopy of small intestine |
| 5 | 2136-04-17 | ICD-9 | `8874` | Diagnostic ultrasound of digestive system |
| 6 | 2136-04-17 | ICD-9 | `4513` | Other endoscopy of small intestine |
| 7 | 2136-04-13 | ICD-9 | `8874` | Diagnostic ultrasound of digestive system |
| 8 | 2136-04-19 | ICD-9 | `5491` | Percutaneous abdominal drainage |
| 9 | 2136-04-25 | ICD-9 | `966` | Enteral infusion of concentrated nutritional substances |

### ICU Procedure Events (from `icu/procedureevents.csv.gz`)

- PICC Line (category: Access Lines - Invasive, started: 2136-04-22 18:47:00, status: FinishedRunning)
- Chest X-Ray (category: 5-Imaging, started: 2136-04-23 05:00:00, status: FinishedRunning)
- 22 Gauge (category: Access Lines - Peripheral, started: 2136-04-23 18:25:00, status: FinishedRunning)

## 8. Critical Findings (Charted Events)

- **Dialysis patient** (first noted: 2136-04-22 18:30:00)

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2136-04-10 20:33:00 | Admission | Admitted from TRANSFER FROM HOSPITAL (URGENT) |
| 2136-04-22 18:01:13 | ICU Admission | Medical/Surgical Intensive Care Unit (MICU/SICU) (LOS: 1.1 days) |
| 2136-04-22 18:01:13 | Transfer | → Medical/Surgical Intensive Care Unit (MICU/SICU) (transfer) |
| 2136-04-23 19:13:58 | Transfer | → Med/Surg (transfer) |
| 2136-05-02 16:35:00 | Discharge | To CHRONIC/LONG TERM ACUTE CARE |

## 10. Missing / Ambiguous Data

- No ED registration time — admission may not have gone through ED.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
