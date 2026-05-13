# Encounter Report — HADM 23052851

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 23052851 |
| Subject ID | 10020306 |
| Patient Sex | F |
| Patient Anchor Age (at anchor year) | 74 |
| Anchor Year | 2129 |
| Admission Time | 2135-01-15 20:55:00 |
| Discharge Time | 2135-02-07 17:50:00 |
| Admission Type | OBSERVATION ADMIT |
| Admission Location | PHYSICIAN REFERRAL |
| Discharge Location | SKILLED NURSING FACILITY |
| Insurance | Other |
| Language | ENGLISH |
| Marital Status | WIDOWED |
| Race/Ethnicity | BLACK/AFRICAN AMERICAN |
| ED Registration | 2135-01-15 16:12:00 |
| ED Departure | 2135-01-15 22:38:00 |
| In-Hospital Mortality | No |
| Date of Death (overall) | N/A |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| HCFA | 640 | MISC DISORDERS OF NUTRITION,METABOLISM,FLUIDS/ELECTROLYTES W MCC | N/A | N/A |
| APR | 951 | MODERATELY EXTENSIVE PROCEDURE UNRELATED TO PRINCIPAL DIAGNOSIS | 4.0 | 4.0 |

### Primary Diagnosis (seq_num = 1)

- **ICD-10 E43**: Unspecified severe protein-calorie malnutrition

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2135-01-15 20:56:36 | N/A | MED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-10 `E43`: Unspecified severe protein-calorie malnutrition
- (seq 2) ICD-10 `R570`: Cardiogenic shock
- (seq 3) ICD-10 `N170`: Acute kidney failure with tubular necrosis
- (seq 4) ICD-10 `G92`: Toxic encephalopathy
- (seq 5) ICD-10 `I5043`: Acute on chronic combined systolic (congestive) and diastolic (congestive) heart failure

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-10 | `E43` | Unspecified severe protein-calorie malnutrition |
| 2 | ICD-10 | `R570` | Cardiogenic shock |
| 3 | ICD-10 | `N170` | Acute kidney failure with tubular necrosis |
| 4 | ICD-10 | `G92` | Toxic encephalopathy |
| 5 | ICD-10 | `I5043` | Acute on chronic combined systolic (congestive) and diastolic (congestive) heart failure |
| 6 | ICD-10 | `I69351` | Hemiplegia and hemiparesis following cerebral infarction affecting right dominant side |
| 7 | ICD-10 | `I481` | Persistent atrial fibrillation |
| 8 | ICD-10 | `D689` | Coagulation defect, unspecified |
| 9 | ICD-10 | `A0472` | Enterocolitis due to Clostridium difficile, not specified as recurrent |
| 10 | ICD-10 | `E874` | Mixed disorder of acid-base balance |
| 11 | ICD-10 | `R64` | Cachexia |
| 12 | ICD-10 | `E870` | Hyperosmolality and hypernatremia |
| 13 | ICD-10 | `I110` | Hypertensive heart disease with heart failure |
| 14 | ICD-10 | `I69322` | Dysarthria following cerebral infarction |
| 15 | ICD-10 | `I69391` | Dysphagia following cerebral infarction |
| 16 | ICD-10 | `R1310` | Dysphagia, unspecified |
| 17 | ICD-10 | `I951` | Orthostatic hypotension |
| 18 | ICD-10 | `E11649` | Type 2 diabetes mellitus with hypoglycemia without coma |
| 19 | ICD-10 | `L0591` | Pilonidal cyst without abscess |
| 20 | ICD-10 | `I2510` | Atherosclerotic heart disease of native coronary artery without angina pectoris |
| 21 | ICD-10 | `D649` | Anemia, unspecified |
| 22 | ICD-10 | `G4733` | Obstructive sleep apnea (adult) (pediatric) |
| 23 | ICD-10 | `E039` | Hypothyroidism, unspecified |
| 24 | ICD-10 | `K219` | Gastro-esophageal reflux disease without esophagitis |
| 25 | ICD-10 | `Z6824` | Body mass index (BMI) 24.0-24.9, adult |
| 26 | ICD-10 | `Z853` | Personal history of malignant neoplasm of breast |
| 27 | ICD-10 | `Z781` | Physical restraint status |
| 28 | ICD-10 | `E8339` | Other disorders of phosphorus metabolism |

## 5. ICU Stays

| Stay ID | First Care Unit | Last Care Unit | ICU Admit | ICU Discharge | LOS (days) |
|---|---|---|---|---|---|
| 38540883 | Trauma SICU (TSICU) | Trauma SICU (TSICU) | 2135-01-21 17:01:57 | 2135-01-24 21:47:45 | 3.20 |

## 6. Escalation / Severity Indicators

The following critical conditions or interventions were detected:

- **Acute Kidney Injury** (ICD diagnosis)
- **Arterial Line** (ICU procedure event)
- **Shock** (ICD diagnosis)

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2135-02-04 | ICD-10 | `0DH63UZ` | Insertion of Feeding Device into Stomach, Percutaneous Approach |
| 2 | 2135-02-04 | ICD-10 | `3E0G76Z` | Introduction of Nutritional Substance into Upper GI, Via Natural or Artificial Opening |
| 3 | 2135-01-22 | ICD-10 | `02HV33Z` | Insertion of Infusion Device into Superior Vena Cava, Percutaneous Approach |
| 4 | 2135-01-22 | ICD-10 | `03HY32Z` | Insertion of Monitoring Device into Upper Artery, Percutaneous Approach |

### ICU Procedure Events (from `icu/procedureevents.csv.gz`)

- Midline (category: Access Lines - Invasive, started: 2135-01-21 17:05:00, status: FinishedRunning)
- 20 Gauge (category: Access Lines - Peripheral, started: 2135-01-21 17:06:00, status: FinishedRunning)
- Ultrasound (category: 5-Imaging, started: 2135-01-21 18:47:00, status: FinishedRunning)
- Arterial Line (category: Access Lines - Invasive, started: 2135-01-22 02:25:00, status: FinishedRunning)
- Foley Catheter (category: GI/GU, started: 2135-01-22 03:47:00, status: FinishedRunning)
- PICC Line (category: Access Lines - Invasive, started: 2135-01-22 11:46:00, status: FinishedRunning)
- EKG (category: 4-Procedures, started: 2135-01-24 16:53:00, status: FinishedRunning)

## 8. Critical Findings (Charted Events)

_No critical chart events detected._

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2135-01-15 16:12:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2135-01-15 16:12:00 | Transfer | → Emergency Department (ED) |
| 2135-01-15 20:55:00 | Admission | Admitted from PHYSICIAN REFERRAL (OBSERVATION ADMIT) |
| 2135-01-15 22:38:00 | ED Departure | Left Emergency Dept. |
| 2135-01-21 17:01:57 | ICU Admission | Trauma SICU (TSICU) (LOS: 3.2 days) |
| 2135-01-21 17:01:57 | Transfer | → Trauma SICU (TSICU) (transfer) |
| 2135-01-24 21:47:45 | Transfer | → Medicine/Cardiology Intermediate (transfer) |
| 2135-02-07 17:50:00 | Discharge | To SKILLED NURSING FACILITY |

## 10. Missing / Ambiguous Data

- No obvious missing critical fields detected.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
