# Encounter Report — HADM 27882036

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 27882036 |
| Subject ID | 10012853 |
| Patient Sex | F |
| Patient Anchor Age (at anchor year) | 91 |
| Anchor Year | 2175 |
| Admission Time | 2176-11-25 21:28:00 |
| Discharge Time | 2176-12-03 15:24:00 |
| Admission Type | EW EMER. |
| Admission Location | EMERGENCY ROOM |
| Discharge Location | SKILLED NURSING FACILITY |
| Insurance | Medicare |
| Language | ENGLISH |
| Marital Status | WIDOWED |
| Race/Ethnicity | BLACK/AFRICAN AMERICAN |
| ED Registration | 2176-11-25 18:34:00 |
| ED Departure | 2176-11-25 23:51:00 |
| In-Hospital Mortality | No |
| Date of Death (overall) | N/A |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| HCFA | 299 | PERIPHERAL VASCULAR DISORDERS W MCC | N/A | N/A |
| APR | 197 | PERIPHERAL & OTHER VASCULAR DISORDERS | 3.0 | 3.0 |

### Primary Diagnosis (seq_num = 1)

- **ICD-10 I82622**: Acute embolism and thrombosis of deep veins of left upper extremity

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2176-11-25 21:28:30 | N/A | MED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-10 `I82622`: Acute embolism and thrombosis of deep veins of left upper extremity
- (seq 2) ICD-10 `J9621`: Acute and chronic respiratory failure with hypoxia
- (seq 3) ICD-10 `I480`: Paroxysmal atrial fibrillation
- (seq 4) ICD-10 `N319`: Neuromuscular dysfunction of bladder, unspecified
- (seq 5) ICD-10 `J449`: Chronic obstructive pulmonary disease, unspecified

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-10 | `I82622` | Acute embolism and thrombosis of deep veins of left upper extremity |
| 2 | ICD-10 | `J9621` | Acute and chronic respiratory failure with hypoxia |
| 3 | ICD-10 | `I480` | Paroxysmal atrial fibrillation |
| 4 | ICD-10 | `N319` | Neuromuscular dysfunction of bladder, unspecified |
| 5 | ICD-10 | `J449` | Chronic obstructive pulmonary disease, unspecified |
| 6 | ICD-10 | `D472` | Monoclonal gammopathy |
| 7 | ICD-10 | `J9622` | Acute and chronic respiratory failure with hypercapnia |
| 8 | ICD-10 | `I129` | Hypertensive chronic kidney disease with stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease |
| 9 | ICD-10 | `N183` | Chronic kidney disease, stage 3 (moderate) |
| 10 | ICD-10 | `I739` | Peripheral vascular disease, unspecified |
| 11 | ICD-10 | `E042` | Nontoxic multinodular goiter |
| 12 | ICD-10 | `E119` | Type 2 diabetes mellitus without complications |
| 13 | ICD-10 | `D509` | Iron deficiency anemia, unspecified |
| 14 | ICD-10 | `Z6829` | Body mass index (BMI) 29.0-29.9, adult |
| 15 | ICD-10 | `I714` | Abdominal aortic aneurysm, without rupture |
| 16 | ICD-10 | `M1000` | Idiopathic gout, unspecified site |
| 17 | ICD-10 | `J398` | Other specified diseases of upper respiratory tract |
| 18 | ICD-10 | `K5790` | Diverticulosis of intestine, part unspecified, without perforation or abscess without bleeding |
| 19 | ICD-10 | `E669` | Obesity, unspecified |
| 20 | ICD-10 | `G4733` | Obstructive sleep apnea (adult) (pediatric) |
| 21 | ICD-10 | `F17210` | Nicotine dependence, cigarettes, uncomplicated |
| 22 | ICD-10 | `K8020` | Calculus of gallbladder without cholecystitis without obstruction |
| 23 | ICD-10 | `M19072` | Primary osteoarthritis, left ankle and foot |
| 24 | ICD-10 | `E780` | Pure hypercholesterolemia |
| 25 | ICD-10 | `M109` | Gout, unspecified |
| 26 | ICD-10 | `I2510` | Atherosclerotic heart disease of native coronary artery without angina pectoris |
| 27 | ICD-10 | `Z7982` | Long term (current) use of aspirin |
| 28 | ICD-10 | `Z86711` | Personal history of pulmonary embolism |
| 29 | ICD-10 | `Z7901` | Long term (current) use of anticoagulants |
| 30 | ICD-10 | `Z8673` | Personal history of transient ischemic attack (TIA), and cerebral infarction without residual deficits |

## 5. ICU Stays

| Stay ID | First Care Unit | Last Care Unit | ICU Admit | ICU Discharge | LOS (days) |
|---|---|---|---|---|---|
| 31338022 | Trauma SICU (TSICU) | Trauma SICU (TSICU) | 2176-11-26 02:34:49 | 2176-11-29 20:58:54 | 3.77 |

## 6. Escalation / Severity Indicators

_No escalation indicators detected from ICD codes or ICU procedure events._

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2176-11-26 | ICD-10 | `5A09557` | Assistance with Respiratory Ventilation, Greater than 96 Consecutive Hours, Continuous Positive Airway Pressure |

### ICU Procedure Events (from `icu/procedureevents.csv.gz`)

- 22 Gauge (category: Access Lines - Peripheral, started: 2176-11-26 02:38:00, status: FinishedRunning)
- 18 Gauge (category: Access Lines - Peripheral, started: 2176-11-26 02:39:00, status: FinishedRunning)
- Family updated by RN (category: 7-Communication, started: 2176-11-26 03:09:00, status: FinishedRunning)
- EKG (category: 4-Procedures, started: 2176-11-26 08:15:00, status: FinishedRunning)

## 8. Critical Findings (Charted Events)

- **Code Status** (first noted: 2176-11-26 08:15:00)
- **Dialysis patient** (first noted: 2176-11-26 03:13:00)

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2176-11-25 18:34:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2176-11-25 18:34:00 | Transfer | → Emergency Department (ED) |
| 2176-11-25 21:28:00 | Admission | Admitted from EMERGENCY ROOM (EW EMER.) |
| 2176-11-25 23:51:00 | ED Departure | Left Emergency Dept. |
| 2176-11-26 02:34:49 | ICU Admission | Trauma SICU (TSICU) (LOS: 3.8 days) |
| 2176-11-26 02:34:49 | Transfer | → Trauma SICU (TSICU) (transfer) |
| 2176-11-27 18:04:59 | Transfer | → Trauma SICU (TSICU) (transfer) |
| 2176-11-29 20:58:54 | Transfer | → Vascular (transfer) |
| 2176-12-03 15:24:00 | Discharge | To SKILLED NURSING FACILITY |

## 10. Missing / Ambiguous Data

- No obvious missing critical fields detected.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
