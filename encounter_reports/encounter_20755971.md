# Encounter Report — HADM 20755971

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 20755971 |
| Subject ID | 10038081 |
| Patient Sex | F |
| Patient Anchor Age (at anchor year) | 63 |
| Anchor Year | 2115 |
| Admission Time | 2115-09-27 20:40:00 |
| Discharge Time | 2115-10-12 00:00:00 |
| Admission Type | URGENT |
| Admission Location | TRANSFER FROM HOSPITAL |
| Discharge Location | DIED |
| Insurance | Other |
| Language | ? |
| Marital Status | SINGLE |
| Race/Ethnicity | UNKNOWN |
| ED Registration | N/A |
| ED Departure | N/A |
| In-Hospital Mortality | YES — Death time: 2115-10-12 22:20:00 |
| Date of Death (overall) | 2115-10-12 |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| APR | 248 | MAJOR GASTROINTESTINAL & PERITONEAL INFECTIONS | 3.0 | 3.0 |
| HCFA | 371 | MAJOR GASTROINTESTINAL DISORDERS & PERITONEAL INFECTIONS W MCC | N/A | N/A |

### Primary Diagnosis (seq_num = 1)

- **ICD-9 56723**: Spontaneous bacterial peritonitis

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2115-09-27 20:42:20 | N/A | MED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-9 `56723`: Spontaneous bacterial peritonitis
- (seq 2) ICD-9 `51881`: Acute respiratory failure
- (seq 3) ICD-9 `4271`: Paroxysmal ventricular tachycardia
- (seq 4) ICD-9 `7885`: Oliguria and anuria
- (seq 5) ICD-9 `5849`: Acute kidney failure, unspecified

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-9 | `56723` | Spontaneous bacterial peritonitis |
| 2 | ICD-9 | `51881` | Acute respiratory failure |
| 3 | ICD-9 | `4271` | Paroxysmal ventricular tachycardia |
| 4 | ICD-9 | `7885` | Oliguria and anuria |
| 5 | ICD-9 | `5849` | Acute kidney failure, unspecified |
| 6 | ICD-9 | `2869` | Other and unspecified coagulation defects |
| 7 | ICD-9 | `7994` | Cachexia |
| 8 | ICD-9 | `5579` | Unspecified vascular insufficiency of intestine |
| 9 | ICD-9 | `4589` | Hypotension, unspecified |
| 10 | ICD-9 | `5370` | Acquired hypertrophic pyloric stenosis |
| 11 | ICD-9 | `4561` | Esophageal varices without mention of bleeding |
| 12 | ICD-9 | `5187` | Transfusion related acute lung injury (TRALI) |
| 13 | ICD-9 | `514` | Pulmonary congestion and hypostasis |
| 14 | ICD-9 | `78959` | Other ascites |
| 15 | ICD-9 | `2761` | Hyposmolality and/or hyponatremia |
| 16 | ICD-9 | `7824` | Jaundice, unspecified, not of newborn |
| 17 | ICD-9 | `5601` | Paralytic ileus |
| 18 | ICD-9 | `5723` | Portal hypertension |
| 19 | ICD-9 | `25541` | Glucocorticoid deficiency |
| 20 | ICD-9 | `5715` | Cirrhosis of liver without mention of alcohol |
| 21 | ICD-9 | `2767` | Hyperpotassemia |
| 22 | ICD-9 | `2859` | Anemia, unspecified |
| 23 | ICD-9 | `2724` | Other and unspecified hyperlipidemia |
| 24 | ICD-9 | `25002` | Diabetes mellitus without mention of complication, type II or unspecified type, uncontrolled |
| 25 | ICD-9 | `72889` | Other disorders of muscle, ligament, and fascia |
| 26 | ICD-9 | `27669` | Other fluid overload |
| 27 | ICD-9 | `78606` | Tachypnea |
| 28 | ICD-9 | `78097` | Altered mental status |
| 29 | ICD-9 | `5859` | Chronic kidney disease, unspecified |
| 30 | ICD-9 | `40390` | Hypertensive chronic kidney disease, unspecified, with chronic kidney disease stage I through stage IV, or unspecified |
| 31 | ICD-9 | `53789` | Other specified disorders of stomach and duodenum |
| 32 | ICD-9 | `49390` | Asthma, unspecified type, unspecified |
| 33 | ICD-9 | `7847` | Epistaxis |
| 34 | ICD-9 | `V7283` | Other specified pre-operative examination |
| 35 | ICD-9 | `V1001` | Personal history of malignant neoplasm of tongue |
| 36 | ICD-9 | `V667` | Encounter for palliative care |
| 37 | ICD-9 | `V4986` | Do not resuscitate status |
| 38 | ICD-9 | `E9347` | Natural blood and blood products causing adverse effects in therapeutic use |

## 5. ICU Stays

| Stay ID | First Care Unit | Last Care Unit | ICU Admit | ICU Discharge | LOS (days) |
|---|---|---|---|---|---|
| 38430513 | Medical Intensive Care Unit (MICU) | Medical Intensive Care Unit (MICU) | 2115-10-09 10:15:25 | 2115-10-13 03:01:17 | 3.70 |

## 6. Escalation / Severity Indicators

The following critical conditions or interventions were detected:

- **Acute Kidney Injury** (ICD diagnosis)
- **Endotracheal Intubation** (ICU procedure event)
- **Invasive Mechanical Ventilation** (ICU procedure event)
- **Liver Failure** (ICD diagnosis)
- **Respiratory Failure** (ICD diagnosis)

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2115-09-30 | ICD-9 | `5491` | Percutaneous abdominal drainage |
| 2 | 2115-10-09 | ICD-9 | `9671` | Continuous invasive mechanical ventilation for less than 96 consecutive hours |
| 3 | 2115-10-09 | ICD-9 | `9604` | Insertion of endotracheal tube |
| 4 | 2115-10-03 | ICD-9 | `5491` | Percutaneous abdominal drainage |
| 5 | 2115-10-02 | ICD-9 | `4513` | Other endoscopy of small intestine |
| 6 | 2115-10-05 | ICD-9 | `3893` | Venous catheterization, not elsewhere classified |
| 7 | 2115-10-09 | ICD-9 | `2121` | Rhinoscopy |
| 8 | 2115-10-09 | ICD-9 | `3142` | Laryngoscopy and other tracheoscopy |
| 9 | 2115-10-09 | ICD-9 | `2101` | Control of epistaxis by anterior nasal packing |

### ICU Procedure Events (from `icu/procedureevents.csv.gz`)

- PICC Line (category: Access Lines - Invasive, started: 2115-10-09 10:38:00, status: FinishedRunning)
- Foley Catheter (category: GI/GU, started: 2115-10-09 10:38:00, status: FinishedRunning)
- Invasive Ventilation (category: 2-Ventilation, started: 2115-10-09 11:00:00, status: FinishedRunning)
- Intubation (category: 1-Intubation/Extubation, started: 2115-10-09 11:00:00, status: FinishedRunning)
- Abdominal X-Ray (category: 5-Imaging, started: 2115-10-09 11:03:00, status: FinishedRunning)
- Chest X-Ray (category: 5-Imaging, started: 2115-10-09 11:03:00, status: FinishedRunning)
- Blood Cultured (category: 6-Cultures, started: 2115-10-09 17:00:00, status: FinishedRunning)

## 8. Critical Findings (Charted Events)

- **Ventilator Mode (Hamilton)** (first noted: 2115-10-09 11:00:00)
- **Ventilator Tank #1** (first noted: 2115-10-09 11:00:00)
- **Ventilator Type** (first noted: 2115-10-09 11:00:00)
- **Known difficult intubation** (first noted: 2115-10-09 11:00:00)
- **Code Status** (first noted: 2115-10-09 10:47:00)

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2115-09-27 20:40:00 | Admission | Admitted from TRANSFER FROM HOSPITAL (URGENT) |
| 2115-10-01 00:49:43 | Transfer | → Transplant (transfer) |
| 2115-10-05 18:19:09 | Transfer | → Transplant (transfer) |
| 2115-10-08 22:10:17 | Transfer | → Transplant (transfer) |
| 2115-10-09 10:15:25 | ICU Admission | Medical Intensive Care Unit (MICU) (LOS: 3.7 days) |
| 2115-10-09 10:15:25 | Transfer | → Medical Intensive Care Unit (MICU) (transfer) |
| 2115-10-09 17:05:18 | Transfer | → Medical Intensive Care Unit (MICU) (transfer) |
| 2115-10-12 00:00:00 | Discharge | To DIED |
| 2115-10-12 22:20:00 | **IN-HOSPITAL DEATH** | |

## 10. Missing / Ambiguous Data

- No ED registration time — admission may not have gone through ED.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
