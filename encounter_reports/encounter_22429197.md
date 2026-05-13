# Encounter Report — HADM 22429197

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 22429197 |
| Subject ID | 10010867 |
| Patient Sex | F |
| Patient Anchor Age (at anchor year) | 28 |
| Anchor Year | 2147 |
| Admission Time | 2147-12-30 08:40:00 |
| Discharge Time | 2148-01-11 17:55:00 |
| Admission Type | EW EMER. |
| Admission Location | EMERGENCY ROOM |
| Discharge Location | REHAB |
| Insurance | Other |
| Language | ENGLISH |
| Marital Status | SINGLE |
| Race/Ethnicity | WHITE - BRAZILIAN |
| ED Registration | 2147-12-30 06:45:00 |
| ED Departure | 2147-12-30 09:33:00 |
| In-Hospital Mortality | No |
| Date of Death (overall) | N/A |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| APR | 912 | MUSCULOSKELETAL & OTHER PROCEDURES FOR MULTIPLE SIGNIFICANT TRAUMA | 4.0 | 4.0 |
| HCFA | 957 | OTHER O.R. PROCEDURES FOR MULTIPLE SIGNIFICANT TRAUMA W MCC | N/A | N/A |

### Primary Diagnosis (seq_num = 1)

- **ICD-10 S12600A**: Unspecified displaced fracture of seventh cervical vertebra, initial encounter for closed fracture

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2147-12-30 08:41:03 | N/A | TRAUM |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-10 `S12600A`: Unspecified displaced fracture of seventh cervical vertebra, initial encounter for closed fracture
- (seq 2) ICD-10 `S271XXA`: Traumatic hemothorax, initial encounter
- (seq 3) ICD-10 `S066X0A`: Traumatic subarachnoid hemorrhage without loss of consciousness, initial encounter
- (seq 4) ICD-10 `J9600`: Acute respiratory failure, unspecified whether with hypoxia or hypercapnia
- (seq 5) ICD-10 `S240XXA`: Concussion and edema of thoracic spinal cord, initial encounter

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-10 | `S12600A` | Unspecified displaced fracture of seventh cervical vertebra, initial encounter for closed fracture |
| 2 | ICD-10 | `S271XXA` | Traumatic hemothorax, initial encounter |
| 3 | ICD-10 | `S066X0A` | Traumatic subarachnoid hemorrhage without loss of consciousness, initial encounter |
| 4 | ICD-10 | `J9600` | Acute respiratory failure, unspecified whether with hypoxia or hypercapnia |
| 5 | ICD-10 | `S240XXA` | Concussion and edema of thoracic spinal cord, initial encounter |
| 6 | ICD-10 | `F05` | Delirium due to known physiological condition |
| 7 | ICD-10 | `S22049A` | Unspecified fracture of fourth thoracic vertebra, initial encounter for closed fracture |
| 8 | ICD-10 | `S22059A` | Unspecified fracture of T5-T6 vertebra, initial encounter for closed fracture |
| 9 | ICD-10 | `S22069A` | Unspecified fracture of T7-T8 vertebra, initial encounter for closed fracture |
| 10 | ICD-10 | `S32029A` | Unspecified fracture of second lumbar vertebra, initial encounter for closed fracture |
| 11 | ICD-10 | `Z6841` | Body mass index (BMI) 40.0-44.9, adult |
| 12 | ICD-10 | `D62` | Acute posthemorrhagic anemia |
| 13 | ICD-10 | `J95851` | Ventilator associated pneumonia |
| 14 | ICD-10 | `R339` | Retention of urine, unspecified |
| 15 | ICD-10 | `F10129` | Alcohol abuse with intoxication, unspecified |
| 16 | ICD-10 | `F1290` | Cannabis use, unspecified, uncomplicated |
| 17 | ICD-10 | `E669` | Obesity, unspecified |
| 18 | ICD-10 | `F329` | Major depressive disorder, single episode, unspecified |
| 19 | ICD-10 | `Z781` | Physical restraint status |
| 20 | ICD-10 | `V270XXA` | Motorcycle driver injured in collision with fixed or stationary object in nontraffic accident, initial encounter |
| 21 | ICD-10 | `Y929` | Unspecified place or not applicable |
| 22 | ICD-10 | `S8012XA` | Contusion of left lower leg, initial encounter |
| 23 | ICD-10 | `Z23` | Encounter for immunization |
| 24 | ICD-10 | `Y848` | Other medical procedures as the cause of abnormal reaction of the patient, or of later complication, without mention of misadventure at the time of the procedure |
| 25 | ICD-10 | `Y92239` | Unspecified place in hospital as the place of occurrence of the external cause |
| 26 | ICD-10 | `F419` | Anxiety disorder, unspecified |

## 5. ICU Stays

| Stay ID | First Care Unit | Last Care Unit | ICU Admit | ICU Discharge | LOS (days) |
|---|---|---|---|---|---|
| 39880770 | Trauma SICU (TSICU) | Trauma SICU (TSICU) | 2147-12-30 09:33:00 | 2148-01-08 18:14:21 | 9.36 |

## 6. Escalation / Severity Indicators

The following critical conditions or interventions were detected:

- **Arterial Line** (ICU procedure event)
- **Invasive Mechanical Ventilation** (ICU procedure event)
- **Respiratory Failure** (ICD diagnosis)

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2147-12-31 | ICD-10 | `0RG10A0` | Fusion of Cervical Vertebral Joint with Interbody Fusion Device, Anterior Approach, Anterior Column, Open Approach |
| 2 | 2148-01-02 | ICD-10 | `0RG1071` | Fusion of Cervical Vertebral Joint with Autologous Tissue Substitute, Posterior Approach, Posterior Column, Open Approach |
| 3 | 2147-12-31 | ICD-10 | `0RB30ZZ` | Excision of Cervical Vertebral Disc, Open Approach |
| 4 | 2148-01-01 | ICD-10 | `0BJ08ZZ` | Inspection of Tracheobronchial Tree, Via Natural or Artificial Opening Endoscopic |
| 5 | 2147-12-30 | ICD-10 | `5A1955Z` | Respiratory Ventilation, Greater than 96 Consecutive Hours |
| 6 | 2148-01-04 | ICD-10 | `0B9B8ZX` | Drainage of Left Lower Lobe Bronchus, Via Natural or Artificial Opening Endoscopic, Diagnostic |
| 7 | 2148-01-04 | ICD-10 | `0B948ZX` | Drainage of Right Upper Lobe Bronchus, Via Natural or Artificial Opening Endoscopic, Diagnostic |
| 8 | 2148-01-04 | ICD-10 | `0B988ZX` | Drainage of Left Upper Lobe Bronchus, Via Natural or Artificial Opening Endoscopic, Diagnostic |
| 9 | 2148-01-01 | ICD-10 | `3E0G76Z` | Introduction of Nutritional Substance into Upper GI, Via Natural or Artificial Opening |
| 10 | 2148-01-06 | ICD-10 | `02H633Z` | Insertion of Infusion Device into Right Atrium, Percutaneous Approach |

### ICU Procedure Events (from `icu/procedureevents.csv.gz`)

- 18 Gauge (category: Access Lines - Peripheral, started: 2147-12-30 09:33:00, status: FinishedRunning)
- Invasive Ventilation (category: 2-Ventilation, started: 2147-12-30 09:35:00, status: FinishedRunning)
- Foley Catheter (category: GI/GU, started: 2147-12-30 20:00:00, status: FinishedRunning)
- OR Sent (category: 3-Significant Events, started: 2147-12-31 19:00:00, status: FinishedRunning)
- OR Received (category: 3-Significant Events, started: 2147-12-31 20:17:00, status: FinishedRunning)
- Arterial Line (category: Access Lines - Invasive, started: 2148-01-01 11:51:00, status: FinishedRunning)
- X-ray (category: 5-Imaging, started: 2148-01-02 18:15:00, status: FinishedRunning)
- 20 Gauge (category: Access Lines - Peripheral, started: 2148-01-03 01:42:00, status: FinishedRunning)
- Family updated by MD (category: 7-Communication, started: 2148-01-03 09:00:00, status: FinishedRunning)
- Ultrasound (category: 5-Imaging, started: 2148-01-03 12:05:00, status: FinishedRunning)
- CT scan (category: 5-Imaging, started: 2148-01-03 14:46:00, status: FinishedRunning)
- Blood Cultured (category: 6-Cultures, started: 2148-01-04 07:10:00, status: FinishedRunning)
- Urine Culture (category: 6-Cultures, started: 2148-01-04 11:00:00, status: FinishedRunning)
- BAL Fluid Culture (category: 6-Cultures, started: 2148-01-04 12:30:00, status: FinishedRunning)
- Chest X-Ray (category: 5-Imaging, started: 2148-01-05 06:33:00, status: FinishedRunning)
- Bronchoscopy (category: 4-Procedures, started: 2148-01-05 11:37:00, status: FinishedRunning)
- PICC Line (category: Access Lines - Invasive, started: 2148-01-06 08:38:00, status: FinishedRunning)
- Extubation (category: 1-Intubation/Extubation, started: 2148-01-07 10:50:00, status: FinishedRunning)
- Family met with Social Worker (category: 7-Communication, started: 2148-01-07 11:53:00, status: FinishedRunning)

## 8. Critical Findings (Charted Events)

- **Ventilator Mode (Hamilton)** (first noted: 2147-12-30 09:21:00)
- **Ventilator Type** (first noted: 2147-12-30 09:20:00)
- **Ventilator Tank #1** (first noted: 2147-12-30 16:00:00)
- **Known difficult intubation** (first noted: 2147-12-30 09:00:00)
- **Code Status** (first noted: 2147-12-30 20:48:00)
- **Dialysis patient** (first noted: 2147-12-30 10:23:00)

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2147-12-30 06:45:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2147-12-30 06:45:00 | Transfer | → Emergency Department (ED) |
| 2147-12-30 08:40:00 | Admission | Admitted from EMERGENCY ROOM (EW EMER.) |
| 2147-12-30 09:33:00 | ED Departure | Left Emergency Dept. |
| 2147-12-30 09:33:00 | ICU Admission | Trauma SICU (TSICU) (LOS: 9.4 days) |
| 2148-01-02 23:24:32 | Transfer | → Trauma SICU (TSICU) (transfer) |
| 2148-01-08 18:14:21 | Transfer | → Med/Surg/Trauma (transfer) |
| 2148-01-11 17:55:00 | Discharge | To REHAB |

## 10. Missing / Ambiguous Data

- No obvious missing critical fields detected.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
