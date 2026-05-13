# Encounter Report — HADM 28477280

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 28477280 |
| Subject ID | 10031757 |
| Patient Sex | F |
| Patient Anchor Age (at anchor year) | 67 |
| Anchor Year | 2137 |
| Admission Time | 2137-10-12 22:43:00 |
| Discharge Time | 2137-10-24 17:30:00 |
| Admission Type | DIRECT EMER. |
| Admission Location | CLINIC REFERRAL |
| Discharge Location | HOSPICE |
| Insurance | Other |
| Language | ENGLISH |
| Marital Status | DIVORCED |
| Race/Ethnicity | WHITE |
| ED Registration | N/A |
| ED Departure | N/A |
| In-Hospital Mortality | No |
| Date of Death (overall) | 2137-10-31 |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| APR | 950 | EXTENSIVE PROCEDURE UNRELATED TO PRINCIPAL DIAGNOSIS | 2.0 | 2.0 |
| HCFA | 981 | EXTENSIVE O.R. PROCEDURE UNRELATED TO PRINCIPAL DIAGNOSIS W MCC | N/A | N/A |

### Primary Diagnosis (seq_num = 1)

- **ICD-9 1551**: Malignant neoplasm of intrahepatic bile ducts

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2137-10-12 22:44:57 | N/A | SURG |
| 2137-10-14 17:36:40 | SURG | MED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-9 `1551`: Malignant neoplasm of intrahepatic bile ducts
- (seq 2) ICD-9 `44329`: Dissection of other artery
- (seq 3) ICD-9 `03842`: Septicemia due to escherichia coli [E. coli]
- (seq 4) ICD-9 `78552`: Septic shock
- (seq 5) ICD-9 `34982`: Toxic encephalopathy

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-9 | `1551` | Malignant neoplasm of intrahepatic bile ducts |
| 2 | ICD-9 | `44329` | Dissection of other artery |
| 3 | ICD-9 | `03842` | Septicemia due to escherichia coli [E. coli] |
| 4 | ICD-9 | `78552` | Septic shock |
| 5 | ICD-9 | `34982` | Toxic encephalopathy |
| 6 | ICD-9 | `1985` | Secondary malignant neoplasm of bone and bone marrow |
| 7 | ICD-9 | `5601` | Paralytic ileus |
| 8 | ICD-9 | `2875` | Thrombocytopenia, unspecified |
| 9 | ICD-9 | `99592` | Severe sepsis |
| 10 | ICD-9 | `5990` | Urinary tract infection, site not specified |
| 11 | ICD-9 | `9982` | Accidental puncture or laceration during a procedure, not elsewhere classified |
| 12 | ICD-9 | `V8541` | Body Mass Index 40.0-44.9, adult |
| 13 | ICD-9 | `99749` | Other digestive system complications |
| 14 | ICD-9 | `E8708` | Accidental cut, puncture, perforation or hemorrhage during other specified medical care |
| 15 | ICD-9 | `E8497` | Accidents occurring in residential institution |
| 16 | ICD-9 | `4019` | Unspecified essential hypertension |
| 17 | ICD-9 | `2724` | Other and unspecified hyperlipidemia |
| 18 | ICD-9 | `41401` | Coronary atherosclerosis of native coronary artery |
| 19 | ICD-9 | `V4582` | Percutaneous transluminal coronary angioplasty status |
| 20 | ICD-9 | `49390` | Asthma, unspecified type, unspecified |
| 21 | ICD-9 | `V4365` | Knee joint replacement |
| 22 | ICD-9 | `311` | Depressive disorder, not elsewhere classified |
| 23 | ICD-9 | `V1582` | Personal history of tobacco use |
| 24 | ICD-9 | `V5866` | Long-term (current) use of aspirin |
| 25 | ICD-9 | `V667` | Encounter for palliative care |
| 26 | ICD-9 | `70400` | Alopecia, unspecified |
| 27 | ICD-9 | `2410` | Nontoxic uninodular goiter |
| 28 | ICD-9 | `53081` | Esophageal reflux |
| 29 | ICD-9 | `2859` | Anemia, unspecified |
| 30 | ICD-9 | `33818` | Other acute postoperative pain |
| 31 | ICD-9 | `79902` | Hypoxemia |
| 32 | ICD-9 | `56409` | Other constipation |
| 33 | ICD-9 | `2753` | Disorders of phosphorus metabolism |
| 34 | ICD-9 | `2752` | Disorders of magnesium metabolism |
| 35 | ICD-9 | `79021` | Impaired fasting glucose |
| 36 | ICD-9 | `27800` | Obesity, unspecified |
| 37 | ICD-9 | `3383` | Neoplasm related pain (acute) (chronic) |

## 5. ICU Stays

| Stay ID | First Care Unit | Last Care Unit | ICU Admit | ICU Discharge | LOS (days) |
|---|---|---|---|---|---|
| 30458995 | Surgical Intensive Care Unit (SICU) | Surgical Intensive Care Unit (SICU) | 2137-10-12 22:44:57 | 2137-10-14 17:08:34 | 1.77 |
| 33244906 | Surgical Intensive Care Unit (SICU) | Surgical Intensive Care Unit (SICU) | 2137-10-15 17:29:21 | 2137-10-17 22:16:51 | 2.20 |

## 6. Escalation / Severity Indicators

The following critical conditions or interventions were detected:

- **Arterial Line** (ICU procedure event)
- **Sepsis** (ICD diagnosis)
- **Shock** (ICD diagnosis)

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2137-10-12 | ICD-9 | `3979` | Other endovascular procedures on other vessels |
| 2 | 2137-10-12 | ICD-9 | `8847` | Arteriography of other intra-abdominal arteries |
| 3 | 2137-10-12 | ICD-9 | `8842` | Aortography |
| 4 | 2137-10-24 | ICD-9 | `3897` | Central venous catheter placement with guidance |

### ICU Procedure Events (from `icu/procedureevents.csv.gz`)

- 20 Gauge (category: Access Lines - Peripheral, started: 2137-10-12 23:00:00, status: FinishedRunning)
- Arterial Line (category: Access Lines - Invasive, started: 2137-10-13 01:07:00, status: FinishedRunning)
- 18 Gauge (category: Access Lines - Peripheral, started: 2137-10-13 06:46:00, status: FinishedRunning)
- EKG (category: 4-Procedures, started: 2137-10-16 08:00:00, status: FinishedRunning)
- Abdominal X-Ray (category: 5-Imaging, started: 2137-10-16 14:00:00, status: FinishedRunning)
- Chest X-Ray (category: 5-Imaging, started: 2137-10-17 05:08:00, status: FinishedRunning)

## 8. Critical Findings (Charted Events)

- **Code Status** (first noted: 2137-10-13 03:21:00)
- **Dialysis patient** (first noted: 2137-10-15 19:12:00)

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2137-10-12 22:43:00 | Admission | Admitted from CLINIC REFERRAL (DIRECT EMER.) |
| 2137-10-12 22:44:57 | ICU Admission | Surgical Intensive Care Unit (SICU) (LOS: 1.8 days) |
| 2137-10-14 17:08:34 | Transfer | → Transplant (transfer) |
| 2137-10-15 17:29:21 | ICU Admission | Surgical Intensive Care Unit (SICU) (LOS: 2.2 days) |
| 2137-10-15 17:29:21 | Transfer | → Surgical Intensive Care Unit (SICU) (transfer) |
| 2137-10-17 13:54:47 | Transfer | → Surgical Intensive Care Unit (SICU) (transfer) |
| 2137-10-17 22:16:51 | Transfer | → Transplant (transfer) |
| 2137-10-18 15:40:08 | Transfer | → Transplant (transfer) |
| 2137-10-24 17:30:00 | Discharge | To HOSPICE |

## 10. Missing / Ambiguous Data

- No ED registration time — admission may not have gone through ED.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
