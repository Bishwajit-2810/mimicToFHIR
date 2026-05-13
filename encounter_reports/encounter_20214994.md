# Encounter Report — HADM 20214994

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 20214994 |
| Subject ID | 10003400 |
| Patient Sex | F |
| Patient Anchor Age (at anchor year) | 72 |
| Anchor Year | 2134 |
| Admission Time | 2137-02-24 10:00:00 |
| Discharge Time | 2137-03-19 15:45:00 |
| Admission Type | URGENT |
| Admission Location | TRANSFER FROM SKILLED NURSING FACILITY |
| Discharge Location | CHRONIC/LONG TERM ACUTE CARE |
| Insurance | Medicare |
| Language | ENGLISH |
| Marital Status | MARRIED |
| Race/Ethnicity | BLACK/AFRICAN AMERICAN |
| ED Registration | N/A |
| ED Departure | N/A |
| In-Hospital Mortality | No |
| Date of Death (overall) | 2137-09-02 |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| HCFA | 329 | MAJOR SMALL & LARGE BOWEL PROCEDURES W MCC | N/A | N/A |

### Primary Diagnosis (seq_num = 1)

- **ICD-9 1543**: Malignant neoplasm of anus, unspecified site

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2137-02-24 14:05:00 | N/A | SURG |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-9 `1543`: Malignant neoplasm of anus, unspecified site
- (seq 2) ICD-9 `2866`: Defibrination syndrome
- (seq 3) ICD-9 `51881`: Acute respiratory failure
- (seq 4) ICD-9 `5845`: Acute kidney failure with lesion of tubular necrosis
- (seq 5) ICD-9 `99594`: Systemic inflammatory response syndrome due to noninfectious process with acute organ dysfunction

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-9 | `1543` | Malignant neoplasm of anus, unspecified site |
| 2 | ICD-9 | `2866` | Defibrination syndrome |
| 3 | ICD-9 | `51881` | Acute respiratory failure |
| 4 | ICD-9 | `5845` | Acute kidney failure with lesion of tubular necrosis |
| 5 | ICD-9 | `99594` | Systemic inflammatory response syndrome due to noninfectious process with acute organ dysfunction |
| 6 | ICD-9 | `20300` | Multiple myeloma, without mention of having achieved remission |
| 7 | ICD-9 | `2639` | Unspecified protein-calorie malnutrition |
| 8 | ICD-9 | `99809` | Postoperative shock, other |
| 9 | ICD-9 | `2930` | Delirium due to conditions classified elsewhere |
| 10 | ICD-9 | `45383` | Acute venous embolism and thrombosis of upper extremity, unspecified |
| 11 | ICD-9 | `99832` | Disruption of external operation (surgical) wound |
| 12 | ICD-9 | `99674` | Other complications due to other vascular device, implant, and graft |
| 13 | ICD-9 | `2851` | Acute posthemorrhagic anemia |
| 14 | ICD-9 | `99859` | Other postoperative infection |
| 15 | ICD-9 | `56089` | Other specified intestinal obstruction |
| 16 | ICD-9 | `55320` | Ventral, unspecified, hernia without mention of obstruction or gangrene |
| 17 | ICD-9 | `42731` | Atrial fibrillation |
| 18 | ICD-9 | `27800` | Obesity, unspecified |
| 19 | ICD-9 | `5853` | Chronic kidney disease, Stage III (moderate) |
| 20 | ICD-9 | `V4987` | Physical restraints status |
| 21 | ICD-9 | `5680` | Peritoneal adhesions (postoperative) (postinfection) |
| 22 | ICD-9 | `V1581` | Personal history of noncompliance with medical treatment, presenting hazards to health |
| 23 | ICD-9 | `V5861` | Long-term (current) use of anticoagulants |
| 24 | ICD-9 | `71596` | Osteoarthrosis, unspecified whether generalized or localized, lower leg |
| 25 | ICD-9 | `E8786` | Removal of other organ (partial) (total) causing abnormal patient reaction, or later complication, without mention of misadventure at time of operation |
| 26 | ICD-9 | `E8497` | Accidents occurring in residential institution |
| 27 | ICD-9 | `V153` | Personal history of irradiation, presenting hazards to health |
| 28 | ICD-9 | `E8798` | Other specified procedures as the cause of abnormal reaction of patient, or of later complication, without mention of misadventure at time of procedure |
| 29 | ICD-9 | `V6441` | Laparoscopic surgical procedure converted to open procedure |
| 30 | ICD-9 | `40390` | Hypertensive chronic kidney disease, unspecified, with chronic kidney disease stage I through stage IV, or unspecified |
| 31 | ICD-9 | `4280` | Congestive heart failure, unspecified |
| 32 | ICD-9 | `V8533` | Body Mass Index 33.0-33.9, adult |
| 33 | ICD-9 | `81600` | Closed fracture of phalanx or phalanges of hand, unspecified |
| 34 | ICD-9 | `E887` | Fracture, cause unspecified |
| 35 | ICD-9 | `E8499` | Accidents occurring in unspecified place |
| 36 | ICD-9 | `0417` | Pseudomonas infection in conditions classified elsewhere and of unspecified site |

## 5. ICU Stays

| Stay ID | First Care Unit | Last Care Unit | ICU Admit | ICU Discharge | LOS (days) |
|---|---|---|---|---|---|
| 32128372 | Medical/Surgical Intensive Care Unit (MICU/SICU) | Medical/Surgical Intensive Care Unit (MICU/SICU) | 2137-02-25 23:37:19 | 2137-03-10 21:29:36 | 12.91 |

## 6. Escalation / Severity Indicators

The following critical conditions or interventions were detected:

- **Acute Kidney Injury** (ICD diagnosis)
- **Arterial Line** (ICU procedure event)
- **DIC** (ICD diagnosis)
- **Invasive Mechanical Ventilation** (ICU procedure event)
- **Respiratory Failure** (ICD diagnosis)

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2137-02-25 | ICD-9 | `4852` | Open abdominoperineal resection of the rectum |
| 2 | 2137-02-25 | ICD-9 | `4562` | Other partial resection of small intestine |
| 3 | 2137-02-25 | ICD-9 | `5459` | Other lysis of peritoneal adhesions |
| 4 | 2137-02-25 | ICD-9 | `5369` | Other and open repair of other hernia of anterior abdominal wall with graft or prosthesis |
| 5 | 2137-02-25 | ICD-9 | `8674` | Attachment of pedicle or flap graft to other sites |
| 6 | 2137-02-25 | ICD-9 | `9977` | Application or administration of an adhesion barrier substance |
| 7 | 2137-03-01 | ICD-9 | `966` | Enteral infusion of concentrated nutritional substances |
| 8 | 2137-03-07 | ICD-9 | `8628` | Nonexcisional debridement of wound, infection or burn |
| 9 | 2137-02-26 | ICD-9 | `3897` | Central venous catheter placement with guidance |
| 10 | 2137-02-25 | ICD-9 | `9671` | Continuous invasive mechanical ventilation for less than 96 consecutive hours |

### ICU Procedure Events (from `icu/procedureevents.csv.gz`)

- Invasive Ventilation (category: 2-Ventilation, started: 2137-02-25 23:37:00, status: FinishedRunning)
- Trauma line (category: Access Lines - Invasive, started: 2137-02-26 02:37:00, status: FinishedRunning)
- Intraosseous Device (category: Access Lines - Invasive, started: 2137-02-26 02:39:00, status: FinishedRunning)
- Indwelling Port (PortaCath) (category: Access Lines - Invasive, started: 2137-02-26 02:40:00, status: FinishedRunning)
- Arterial Line (category: Access Lines - Invasive, started: 2137-02-26 02:42:00, status: FinishedRunning)
- Blood Cultured (category: 6-Cultures, started: 2137-02-26 02:45:00, status: FinishedRunning)
- Urine Culture (category: 6-Cultures, started: 2137-02-26 04:56:00, status: FinishedRunning)
- X-ray (category: 5-Imaging, started: 2137-02-26 14:54:00, status: FinishedRunning)
- EKG (category: 4-Procedures, started: 2137-02-28 11:31:00, status: FinishedRunning)
- PICC Line (category: Access Lines - Invasive, started: 2137-03-02 14:30:00, status: FinishedRunning)
- Chest X-Ray (category: 5-Imaging, started: 2137-03-02 17:06:00, status: FinishedRunning)
- CT scan (category: 5-Imaging, started: 2137-03-06 17:12:00, status: FinishedRunning)
- Ultrasound (category: 5-Imaging, started: 2137-03-07 09:00:00, status: FinishedRunning)

## 8. Critical Findings (Charted Events)

- **Ventilator Type** (first noted: 2137-02-25 23:30:00)
- **Ventilator Tank #1** (first noted: 2137-02-26 04:00:00)
- **Ventilator Tank #2** (first noted: 2137-02-26 04:00:00)
- **Known difficult intubation** (first noted: 2137-02-26 04:00:00)
- **Code Status.** (first noted: 2137-02-27 06:24:00)
- **Code Status** (first noted: 2137-02-26 07:26:00)

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2137-02-24 10:00:00 | Admission | Admitted from TRANSFER FROM SKILLED NURSING FACILITY (URGENT) |
| 2137-02-25 19:43:32 | Transfer | → PACU (transfer) |
| 2137-02-25 23:37:19 | ICU Admission | Medical/Surgical Intensive Care Unit (MICU/SICU) (LOS: 12.9 days) |
| 2137-02-25 23:37:19 | Transfer | → Medical/Surgical Intensive Care Unit (MICU/SICU) (transfer) |
| 2137-03-07 00:35:27 | Transfer | → Medical/Surgical Intensive Care Unit (MICU/SICU) (transfer) |
| 2137-03-10 21:29:36 | Transfer | → Medicine (transfer) |
| 2137-03-11 14:40:55 | Transfer | → Medicine (transfer) |
| 2137-03-19 15:45:00 | Discharge | To CHRONIC/LONG TERM ACUTE CARE |

## 10. Missing / Ambiguous Data

- No ED registration time — admission may not have gone through ED.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
