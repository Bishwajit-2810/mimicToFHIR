# Encounter Report — HADM 21759936

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 21759936 |
| Subject ID | 10023239 |
| Patient Sex | F |
| Patient Anchor Age (at anchor year) | 29 |
| Anchor Year | 2137 |
| Admission Time | 2140-10-03 09:06:00 |
| Discharge Time | 2140-10-08 15:28:00 |
| Admission Type | EW EMER. |
| Admission Location | TRANSFER FROM HOSPITAL |
| Discharge Location | HOME |
| Insurance | Other |
| Language | ENGLISH |
| Marital Status | MARRIED |
| Race/Ethnicity | WHITE |
| ED Registration | 2140-10-03 06:20:00 |
| ED Departure | 2140-10-03 11:04:00 |
| In-Hospital Mortality | No |
| Date of Death (overall) | N/A |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| APR | 952 | NONEXTENSIVE PROCEDURE UNRELATED TO PRINCIPAL DIAGNOSIS | 4.0 | 3.0 |
| HCFA | 987 | NON-EXTENSIVE O.R. PROC UNRELATED TO PRINCIPAL DIAGNOSIS W MCC | N/A | N/A |

### Primary Diagnosis (seq_num = 1)

- **ICD-10 T85694A**: Other mechanical complication of insulin pump, initial encounter

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2140-10-03 09:07:56 | N/A | MED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-10 `T85694A`: Other mechanical complication of insulin pump, initial encounter
- (seq 2) ICD-10 `E1010`: Type 1 diabetes mellitus with ketoacidosis without coma
- (seq 3) ICD-10 `J9601`: Acute respiratory failure with hypoxia
- (seq 4) ICD-10 `J15211`: Pneumonia due to Methicillin susceptible Staphylococcus aureus
- (seq 5) ICD-10 `N179`: Acute kidney failure, unspecified

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-10 | `T85694A` | Other mechanical complication of insulin pump, initial encounter |
| 2 | ICD-10 | `E1010` | Type 1 diabetes mellitus with ketoacidosis without coma |
| 3 | ICD-10 | `J9601` | Acute respiratory failure with hypoxia |
| 4 | ICD-10 | `J15211` | Pneumonia due to Methicillin susceptible Staphylococcus aureus |
| 5 | ICD-10 | `N179` | Acute kidney failure, unspecified |
| 6 | ICD-10 | `Z794` | Long term (current) use of insulin |
| 7 | ICD-10 | `G40909` | Epilepsy, unspecified, not intractable, without status epilepticus |
| 8 | ICD-10 | `E039` | Hypothyroidism, unspecified |
| 9 | ICD-10 | `E7800` | Pure hypercholesterolemia, unspecified |
| 10 | ICD-10 | `F419` | Anxiety disorder, unspecified |
| 11 | ICD-10 | `Z006` | Encounter for examination for normal comparison and control in clinical research program |
| 12 | ICD-10 | `T383X6A` | Underdosing of insulin and oral hypoglycemic [antidiabetic] drugs, initial encounter |
| 13 | ICD-10 | `D869` | Sarcoidosis, unspecified |
| 14 | ICD-10 | `R000` | Tachycardia, unspecified |
| 15 | ICD-10 | `F39` | Unspecified mood [affective] disorder |

## 5. ICU Stays

| Stay ID | First Care Unit | Last Care Unit | ICU Admit | ICU Discharge | LOS (days) |
|---|---|---|---|---|---|
| 35024147 | Medical/Surgical Intensive Care Unit (MICU/SICU) | Medical/Surgical Intensive Care Unit (MICU/SICU) | 2140-10-03 09:07:56 | 2140-10-05 19:31:27 | 2.43 |

## 6. Escalation / Severity Indicators

The following critical conditions or interventions were detected:

- **Acute Kidney Injury** (ICD diagnosis)
- **Pneumonia** (ICD diagnosis)
- **Respiratory Failure** (ICD diagnosis)

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2140-10-04 | ICD-10 | `0B9D8ZX` | Drainage of Right Middle Lung Lobe, Via Natural or Artificial Opening Endoscopic, Diagnostic |
| 2 | 2140-10-04 | ICD-10 | `07B74ZX` | Excision of Thorax Lymphatic, Percutaneous Endoscopic Approach, Diagnostic |
| 3 | 2140-10-04 | ICD-10 | `0BBD8ZX` | Excision of Right Middle Lung Lobe, Via Natural or Artificial Opening Endoscopic, Diagnostic |

### ICU Procedure Events (from `icu/procedureevents.csv.gz`)

- 20 Gauge (category: Access Lines - Peripheral, started: 2140-10-03 12:00:00, status: FinishedRunning)
- 18 Gauge (category: Access Lines - Peripheral, started: 2140-10-03 12:00:00, status: FinishedRunning)
- Family updated by RN (category: 7-Communication, started: 2140-10-04 16:50:00, status: FinishedRunning)
- OR Sent (category: 3-Significant Events, started: 2140-10-04 16:51:00, status: FinishedRunning)
- Chest X-Ray (category: 5-Imaging, started: 2140-10-04 21:26:00, status: FinishedRunning)

## 8. Critical Findings (Charted Events)

- **Dialysis patient** (first noted: 2140-10-03 15:33:00)

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2140-10-03 06:20:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2140-10-03 06:20:00 | Transfer | → Emergency Department (ED) |
| 2140-10-03 09:06:00 | Admission | Admitted from TRANSFER FROM HOSPITAL (EW EMER.) |
| 2140-10-03 09:07:56 | ICU Admission | Medical/Surgical Intensive Care Unit (MICU/SICU) (LOS: 2.4 days) |
| 2140-10-03 09:15:56 | Transfer | → Medical/Surgical Intensive Care Unit (MICU/SICU) (transfer) |
| 2140-10-03 11:04:00 | ED Departure | Left Emergency Dept. |
| 2140-10-05 19:31:27 | Transfer | → Med/Surg/GYN (transfer) |
| 2140-10-08 15:28:00 | Discharge | To HOME |

## 10. Missing / Ambiguous Data

- No obvious missing critical fields detected.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
