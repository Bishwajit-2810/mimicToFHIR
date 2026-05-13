# Encounter Report — HADM 23559586

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 23559586 |
| Subject ID | 10003400 |
| Patient Sex | F |
| Patient Anchor Age (at anchor year) | 72 |
| Anchor Year | 2134 |
| Admission Time | 2137-08-04 00:07:00 |
| Discharge Time | 2137-09-02 17:05:00 |
| Admission Type | URGENT |
| Admission Location | TRANSFER FROM HOSPITAL |
| Discharge Location | DIED |
| Insurance | Medicare |
| Language | ENGLISH |
| Marital Status | MARRIED |
| Race/Ethnicity | BLACK/AFRICAN AMERICAN |
| ED Registration | N/A |
| ED Departure | N/A |
| In-Hospital Mortality | YES — Death time: 2137-09-02 17:05:00 |
| Date of Death (overall) | 2137-09-02 |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| HCFA | 987 | NON-EXTENSIVE O.R. PROC UNRELATED TO PRINCIPAL DIAGNOSIS W MCC | N/A | N/A |

### Primary Diagnosis (seq_num = 1)

- **ICD-10 T8131XA**: Disruption of external operation (surgical) wound, not elsewhere classified, initial encounter

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2137-08-05 00:13:22 | N/A | MED |
| 2137-08-17 17:36:52 | MED | CMED |
| 2137-08-22 07:58:54 | CMED | MED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-10 `T8131XA`: Disruption of external operation (surgical) wound, not elsewhere classified, initial encounter
- (seq 2) ICD-10 `R6521`: Severe sepsis with septic shock
- (seq 3) ICD-10 `J9601`: Acute respiratory failure with hypoxia
- (seq 4) ICD-10 `N179`: Acute kidney failure, unspecified
- (seq 5) ICD-10 `A419`: Sepsis, unspecified organism

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-10 | `T8131XA` | Disruption of external operation (surgical) wound, not elsewhere classified, initial encounter |
| 2 | ICD-10 | `R6521` | Severe sepsis with septic shock |
| 3 | ICD-10 | `J9601` | Acute respiratory failure with hypoxia |
| 4 | ICD-10 | `N179` | Acute kidney failure, unspecified |
| 5 | ICD-10 | `A419` | Sepsis, unspecified organism |
| 6 | ICD-10 | `G9340` | Encephalopathy, unspecified |
| 7 | ICD-10 | `C9000` | Multiple myeloma not having achieved remission |
| 8 | ICD-10 | `J910` | Malignant pleural effusion |
| 9 | ICD-10 | `K5660` | Unspecified intestinal obstruction |
| 10 | ICD-10 | `C786` | Secondary malignant neoplasm of retroperitoneum and peritoneum |
| 11 | ICD-10 | `C7889` | Secondary malignant neoplasm of other digestive organs |
| 12 | ICD-10 | `C211` | Malignant neoplasm of anal canal |
| 13 | ICD-10 | `E46` | Unspecified protein-calorie malnutrition |
| 14 | ICD-10 | `Q620` | Congenital hydronephrosis |
| 15 | ICD-10 | `T814XXA` | Infection following a procedure, initial encounter |
| 16 | ICD-10 | `T8359XA` | Infection and inflammatory reaction due to prosthetic device, implant and graft in urinary system, initial encounter |
| 17 | ICD-10 | `N12` | Tubulo-interstitial nephritis, not specified as acute or chronic |
| 18 | ICD-10 | `B3749` | Other urogenital candidiasis |
| 19 | ICD-10 | `K311` | Adult hypertrophic pyloric stenosis |
| 20 | ICD-10 | `I5032` | Chronic diastolic (congestive) heart failure |
| 21 | ICD-10 | `D62` | Acute posthemorrhagic anemia |
| 22 | ICD-10 | `Z66` | Do not resuscitate |
| 23 | ICD-10 | `Z515` | Encounter for palliative care |
| 24 | ICD-10 | `E8809` | Other disorders of plasma-protein metabolism, not elsewhere classified |
| 25 | ICD-10 | `I482` | Chronic atrial fibrillation |
| 26 | ICD-10 | `Z7901` | Long term (current) use of anticoagulants |
| 27 | ICD-10 | `M179` | Osteoarthritis of knee, unspecified |
| 28 | ICD-10 | `I129` | Hypertensive chronic kidney disease with stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease |
| 29 | ICD-10 | `B9562` | Methicillin resistant Staphylococcus aureus infection as the cause of diseases classified elsewhere |
| 30 | ICD-10 | `N183` | Chronic kidney disease, stage 3 (moderate) |
| 31 | ICD-10 | `Z433` | Encounter for attention to colostomy |
| 32 | ICD-10 | `R310` | Gross hematuria |
| 33 | ICD-10 | `E669` | Obesity, unspecified |
| 34 | ICD-10 | `Z6838` | Body mass index (BMI) 38.0-38.9, adult |
| 35 | ICD-10 | `Y848` | Other medical procedures as the cause of abnormal reaction of the patient, or of later complication, without mention of misadventure at the time of the procedure |
| 36 | ICD-10 | `Y92239` | Unspecified place in hospital as the place of occurrence of the external cause |
| 37 | ICD-10 | `B965` | Pseudomonas (aeruginosa) (mallei) (pseudomallei) as the cause of diseases classified elsewhere |
| 38 | ICD-10 | `D696` | Thrombocytopenia, unspecified |

## 5. ICU Stays

| Stay ID | First Care Unit | Last Care Unit | ICU Admit | ICU Discharge | LOS (days) |
|---|---|---|---|---|---|
| 34577403 | Medical/Surgical Intensive Care Unit (MICU/SICU) | Medical/Surgical Intensive Care Unit (MICU/SICU) | 2137-08-10 19:54:51 | 2137-08-13 17:54:54 | 2.92 |
| 38383343 | Coronary Care Unit (CCU) | Medical Intensive Care Unit (MICU) | 2137-08-17 17:36:37 | 2137-09-02 19:17:11 | 16.07 |

## 6. Escalation / Severity Indicators

The following critical conditions or interventions were detected:

- **Acute Kidney Injury** (ICD diagnosis)
- **Arterial Line** (ICU procedure event)
- **Endotracheal Intubation** (ICU procedure event)
- **Invasive Mechanical Ventilation** (ICU procedure event)
- **Non-Invasive Ventilation (NIV/BiPAP)** (ICU procedure event)
- **Respiratory Failure** (ICD diagnosis)
- **Sepsis** (ICD diagnosis)

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2137-08-10 | ICD-10 | `0T768DZ` | Dilation of Right Ureter with Intraluminal Device, Via Natural or Artificial Opening Endoscopic |
| 2 | 2137-08-10 | ICD-10 | `0TP98DZ` | Removal of Intraluminal Device from Ureter, Via Natural or Artificial Opening Endoscopic |
| 3 | 2137-08-10 | ICD-10 | `0TJB8ZZ` | Inspection of Bladder, Via Natural or Artificial Opening Endoscopic |
| 4 | 2137-08-10 | ICD-10 | `BT1FYZZ` | Fluoroscopy of Left Kidney, Ureter and Bladder using Other Contrast |
| 5 | 2137-08-10 | ICD-10 | `BT1DYZZ` | Fluoroscopy of Right Kidney, Ureter and Bladder using Other Contrast |
| 6 | 2137-08-10 | ICD-10 | `5A1945Z` | Respiratory Ventilation, 24-96 Consecutive Hours |
| 7 | 2137-08-13 | ICD-10 | `3E0G76Z` | Introduction of Nutritional Substance into Upper GI, Via Natural or Artificial Opening |
| 8 | 2137-08-18 | ICD-10 | `0W9930Z` | Drainage of Right Pleural Cavity with Drainage Device, Percutaneous Approach |
| 9 | 2137-08-17 | ICD-10 | `0BH17EZ` | Insertion of Endotracheal Airway into Trachea, Via Natural or Artificial Opening |
| 10 | 2137-08-17 | ICD-10 | `5A1945Z` | Respiratory Ventilation, 24-96 Consecutive Hours |
| 11 | 2137-08-20 | ICD-10 | `02HV33Z` | Insertion of Infusion Device into Superior Vena Cava, Percutaneous Approach |
| 12 | 2137-08-20 | ICD-10 | `B548ZZA` | Ultrasonography of Superior Vena Cava, Guidance |

### ICU Procedure Events (from `icu/procedureevents.csv.gz`)

- 22 Gauge (category: Access Lines - Peripheral, started: 2137-08-10 20:00:00, status: FinishedRunning)
- Chest X-Ray (category: 5-Imaging, started: 2137-08-12 05:10:00, status: FinishedRunning)
- Foley Catheter (category: GI/GU, started: 2137-08-12 21:11:00, status: FinishedRunning)
- Indwelling Port (PortaCath) (category: Access Lines - Invasive, started: 2137-08-17 18:00:00, status: FinishedRunning)
- Non-invasive Ventilation (category: 2-Ventilation, started: 2137-08-17 19:00:00, status: FinishedRunning)
- Invasive Ventilation (category: 2-Ventilation, started: 2137-08-17 21:21:00, status: FinishedRunning)
- Intubation (category: 1-Intubation/Extubation, started: 2137-08-17 21:21:00, status: FinishedRunning)
- Arterial Line (category: Access Lines - Invasive, started: 2137-08-19 08:00:00, status: FinishedRunning)
- 20 Gauge (category: Access Lines - Peripheral, started: 2137-08-19 12:13:00, status: FinishedRunning)
- Extubation (category: 1-Intubation/Extubation, started: 2137-08-21 15:40:00, status: FinishedRunning)
- Ultrasound (category: 5-Imaging, started: 2137-08-21 16:45:00, status: FinishedRunning)
- CT scan (category: 5-Imaging, started: 2137-08-24 17:08:00, status: FinishedRunning)
- PICC Line (category: Access Lines - Invasive, started: 2137-08-30 12:02:00, status: Stopped)

## 8. Critical Findings (Charted Events)

- **Ventilator Type** (first noted: 2137-08-10 20:00:00)
- **Ventilator Mode** (first noted: 2137-08-10 20:00:00)
- **Ventilator Tank #2** (first noted: 2137-08-10 20:00:00)
- **Known difficult intubation** (first noted: 2137-08-11 07:29:00)
- **Code Status** (first noted: 2137-08-17 23:50:00)
- **Code Status.** (first noted: 2137-08-17 20:22:00)

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2137-08-04 00:07:00 | Admission | Admitted from TRANSFER FROM HOSPITAL (URGENT) |
| 2137-08-10 16:16:04 | Transfer | → PACU (transfer) |
| 2137-08-10 19:54:51 | ICU Admission | Medical/Surgical Intensive Care Unit (MICU/SICU) (LOS: 2.9 days) |
| 2137-08-10 19:54:51 | Transfer | → Medical/Surgical Intensive Care Unit (MICU/SICU) (transfer) |
| 2137-08-13 17:54:54 | Transfer | → Medicine (transfer) |
| 2137-08-17 17:36:37 | ICU Admission | Coronary Care Unit (CCU) (LOS: 16.1 days) |
| 2137-08-17 17:36:37 | Transfer | → Coronary Care Unit (CCU) (transfer) |
| 2137-08-18 20:54:06 | Transfer | → Medical Intensive Care Unit (MICU) (transfer) |
| 2137-09-02 17:05:00 | **IN-HOSPITAL DEATH** | |
| 2137-09-02 17:05:00 | Discharge | To DIED |

## 10. Missing / Ambiguous Data

- No ED registration time — admission may not have gone through ED.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
