# Encounter Report — HADM 27996267

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 27996267 |
| Subject ID | 10040025 |
| Patient Sex | F |
| Patient Anchor Age (at anchor year) | 64 |
| Anchor Year | 2143 |
| Admission Time | 2148-01-23 12:18:00 |
| Discharge Time | 2148-02-04 20:51:00 |
| Admission Type | OBSERVATION ADMIT |
| Admission Location | TRANSFER FROM SKILLED NURSING FACILITY |
| Discharge Location | HOSPICE |
| Insurance | Other |
| Language | ENGLISH |
| Marital Status | DIVORCED |
| Race/Ethnicity | WHITE |
| ED Registration | 2148-01-22 14:47:00 |
| ED Departure | 2148-01-23 09:42:00 |
| In-Hospital Mortality | No |
| Date of Death (overall) | 2148-02-07 |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| APR | 711 | POST-OP, POST-TRAUMA, OTHER DEVICE INFECTIONS W O.R. PROCEDURE | 3.0 | 3.0 |
| HCFA | 856 | POSTOPERATIVE OR POST-TRAUMATIC INFECTIONS W O.R. PROC W MCC | N/A | N/A |

### Primary Diagnosis (seq_num = 1)

- **ICD-10 T814XXA**: Infection following a procedure, initial encounter

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2148-01-23 12:18:49 | N/A | VSURG |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-10 `T814XXA`: Infection following a procedure, initial encounter
- (seq 2) ICD-10 `I5033`: Acute on chronic diastolic (congestive) heart failure
- (seq 3) ICD-10 `N179`: Acute kidney failure, unspecified
- (seq 4) ICD-10 `N184`: Chronic kidney disease, stage 4 (severe)
- (seq 5) ICD-10 `D62`: Acute posthemorrhagic anemia

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-10 | `T814XXA` | Infection following a procedure, initial encounter |
| 2 | ICD-10 | `I5033` | Acute on chronic diastolic (congestive) heart failure |
| 3 | ICD-10 | `N179` | Acute kidney failure, unspecified |
| 4 | ICD-10 | `N184` | Chronic kidney disease, stage 4 (severe) |
| 5 | ICD-10 | `D62` | Acute posthemorrhagic anemia |
| 6 | ICD-10 | `E1152` | Type 2 diabetes mellitus with diabetic peripheral angiopathy with gangrene |
| 7 | ICD-10 | `F05` | Delirium due to known physiological condition |
| 8 | ICD-10 | `T8119XA` | Other postprocedural shock, initial encounter |
| 9 | ICD-10 | `T8131XA` | Disruption of external operation (surgical) wound, not elsewhere classified, initial encounter |
| 10 | ICD-10 | `I130` | Hypertensive heart and chronic kidney disease with heart failure and stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease |
| 11 | ICD-10 | `Y832` | Surgical operation with anastomosis, bypass or graft as the cause of abnormal reaction of the patient, or of later complication, without mention of misadventure at the time of the procedure |
| 12 | ICD-10 | `Y929` | Unspecified place or not applicable |
| 13 | ICD-10 | `E1122` | Type 2 diabetes mellitus with diabetic chronic kidney disease |
| 14 | ICD-10 | `Z66` | Do not resuscitate |
| 15 | ICD-10 | `Z515` | Encounter for palliative care |
| 16 | ICD-10 | `Z781` | Physical restraint status |
| 17 | ICD-10 | `R791` | Abnormal coagulation profile |
| 18 | ICD-10 | `B952` | Enterococcus as the cause of diseases classified elsewhere |
| 19 | ICD-10 | `Z1621` | Resistance to vancomycin |
| 20 | ICD-10 | `B9689` | Other specified bacterial agents as the cause of diseases classified elsewhere |
| 21 | ICD-10 | `Z1623` | Resistance to quinolones and fluoroquinolones |
| 22 | ICD-10 | `B954` | Other streptococcus as the cause of diseases classified elsewhere |
| 23 | ICD-10 | `L89899` | Pressure ulcer of other site, unspecified stage |
| 24 | ICD-10 | `E785` | Hyperlipidemia, unspecified |
| 25 | ICD-10 | `E039` | Hypothyroidism, unspecified |
| 26 | ICD-10 | `I2510` | Atherosclerotic heart disease of native coronary artery without angina pectoris |
| 27 | ICD-10 | `M109` | Gout, unspecified |
| 28 | ICD-10 | `I4891` | Unspecified atrial fibrillation |
| 29 | ICD-10 | `F329` | Major depressive disorder, single episode, unspecified |
| 30 | ICD-10 | `J449` | Chronic obstructive pulmonary disease, unspecified |
| 31 | ICD-10 | `K219` | Gastro-esophageal reflux disease without esophagitis |
| 32 | ICD-10 | `E11621` | Type 2 diabetes mellitus with foot ulcer |
| 33 | ICD-10 | `L97529` | Non-pressure chronic ulcer of other part of left foot with unspecified severity |
| 34 | ICD-10 | `R159` | Full incontinence of feces |
| 35 | ICD-10 | `R197` | Diarrhea, unspecified |
| 36 | ICD-10 | `R748` | Abnormal levels of other serum enzymes |
| 37 | ICD-10 | `K5903` | Drug induced constipation |
| 38 | ICD-10 | `T402X5A` | Adverse effect of other opioids, initial encounter |
| 39 | ICD-10 | `Y92230` | Patient room in hospital as the place of occurrence of the external cause |

## 5. ICU Stays

| Stay ID | First Care Unit | Last Care Unit | ICU Admit | ICU Discharge | LOS (days) |
|---|---|---|---|---|---|
| 36107367 | Surgical Intensive Care Unit (SICU) | Surgical Intensive Care Unit (SICU) | 2148-01-24 04:50:17 | 2148-01-30 17:45:09 | 6.54 |

## 6. Escalation / Severity Indicators

The following critical conditions or interventions were detected:

- **Acute Kidney Injury** (ICD diagnosis)
- **Invasive Mechanical Ventilation** (ICU procedure event)

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2148-01-23 | ICD-10 | `0LBW0ZZ` | Excision of Left Foot Tendon, Open Approach |
| 2 | 2148-01-23 | ICD-10 | `0JDM0ZZ` | Extraction of Left Upper Leg Subcutaneous Tissue and Fascia, Open Approach |
| 3 | 2148-01-25 | ICD-10 | `0JBP0ZZ` | Excision of Left Lower Leg Subcutaneous Tissue and Fascia, Open Approach |
| 4 | 2148-01-31 | ICD-10 | `0JDM0ZZ` | Extraction of Left Upper Leg Subcutaneous Tissue and Fascia, Open Approach |
| 5 | 2148-01-31 | ICD-10 | `0JDP0ZZ` | Extraction of Left Lower Leg Subcutaneous Tissue and Fascia, Open Approach |
| 6 | 2148-01-24 | ICD-10 | `02HV33Z` | Insertion of Infusion Device into Superior Vena Cava, Percutaneous Approach |

### ICU Procedure Events (from `icu/procedureevents.csv.gz`)

- Multi Lumen (category: Access Lines - Invasive, started: 2148-01-24 05:00:00, status: FinishedRunning)
- Foley Catheter (category: GI/GU, started: 2148-01-24 05:00:00, status: FinishedRunning)
- Portable Chest X-Ray (category: 5-Imaging, started: 2148-01-24 05:40:00, status: FinishedRunning)
- Transthoracic Echo (category: 5-Imaging, started: 2148-01-24 11:58:00, status: FinishedRunning)
- 18 Gauge (category: Access Lines - Peripheral, started: 2148-01-24 16:46:00, status: FinishedRunning)
- OR Sent (category: 3-Significant Events, started: 2148-01-25 07:50:00, status: FinishedRunning)
- Invasive Ventilation (category: 2-Ventilation, started: 2148-01-25 09:50:00, status: FinishedRunning)
- Extubation (category: 1-Intubation/Extubation, started: 2148-01-26 16:54:00, status: FinishedRunning)
- Nursing Water Swallow Screening (category: 4-Procedures, started: 2148-01-26 17:00:00, status: FinishedRunning)
- VAC Change (category: 4-Procedures, started: 2148-01-28 13:30:00, status: FinishedRunning)
- PICC Line (category: Access Lines - Invasive, started: 2148-01-30 11:00:00, status: FinishedRunning)

## 8. Critical Findings (Charted Events)

- **Ventilator Tank #1** (first noted: 2148-01-25 09:00:00)
- **Ventilator Type** (first noted: 2148-01-25 09:00:00)
- **Ventilator Tank #2** (first noted: 2148-01-25 09:00:00)

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2148-01-22 14:47:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2148-01-22 14:47:00 | Transfer | → Emergency Department (ED) |
| 2148-01-23 09:42:00 | ED Departure | Left Emergency Dept. |
| 2148-01-23 12:18:00 | Admission | Admitted from TRANSFER FROM SKILLED NURSING FACILITY (OBSERVATION ADMIT) |
| 2148-01-23 14:23:57 | Transfer | → Vascular (transfer) |
| 2148-01-24 04:50:17 | ICU Admission | Surgical Intensive Care Unit (SICU) (LOS: 6.5 days) |
| 2148-01-24 04:50:17 | Transfer | → Surgical Intensive Care Unit (SICU) (transfer) |
| 2148-01-30 17:45:09 | Transfer | → Vascular (transfer) |
| 2148-02-04 20:51:00 | Discharge | To HOSPICE |

## 10. Missing / Ambiguous Data

- No obvious missing critical fields detected.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
