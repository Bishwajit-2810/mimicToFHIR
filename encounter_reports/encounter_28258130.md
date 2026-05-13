# Encounter Report — HADM 28258130

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 28258130 |
| Subject ID | 10039708 |
| Patient Sex | F |
| Patient Anchor Age (at anchor year) | 46 |
| Anchor Year | 2138 |
| Admission Time | 2140-01-23 16:19:00 |
| Discharge Time | 2140-02-26 18:15:00 |
| Admission Type | EW EMER. |
| Admission Location | EMERGENCY ROOM |
| Discharge Location | CHRONIC/LONG TERM ACUTE CARE |
| Insurance | Other |
| Language | ENGLISH |
| Marital Status | SINGLE |
| Race/Ethnicity | BLACK/AFRICAN AMERICAN |
| ED Registration | 2140-01-23 12:35:00 |
| ED Departure | 2140-01-23 18:08:00 |
| In-Hospital Mortality | No |
| Date of Death (overall) | N/A |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| HCFA | 802 | OTHER O.R. PROC OF THE BLOOD & BLOOD FORMING ORGANS W MCC | N/A | N/A |
| APR | 951 | MODERATELY EXTENSIVE PROCEDURE UNRELATED TO PRINCIPAL DIAGNOSIS | 4.0 | 4.0 |

### Primary Diagnosis (seq_num = 1)

- **ICD-10 D649**: Anemia, unspecified

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2140-01-23 16:19:58 | N/A | MED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-10 `D649`: Anemia, unspecified
- (seq 2) ICD-10 `N170`: Acute kidney failure with tubular necrosis
- (seq 3) ICD-10 `J9691`: Respiratory failure, unspecified with hypoxia
- (seq 4) ICD-10 `I214`: Non-ST elevation (NSTEMI) myocardial infarction
- (seq 5) ICD-10 `J690`: Pneumonitis due to inhalation of food and vomit

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-10 | `D649` | Anemia, unspecified |
| 2 | ICD-10 | `N170` | Acute kidney failure with tubular necrosis |
| 3 | ICD-10 | `J9691` | Respiratory failure, unspecified with hypoxia |
| 4 | ICD-10 | `I214` | Non-ST elevation (NSTEMI) myocardial infarction |
| 5 | ICD-10 | `J690` | Pneumonitis due to inhalation of food and vomit |
| 6 | ICD-10 | `G9340` | Encephalopathy, unspecified |
| 7 | ICD-10 | `I5021` | Acute systolic (congestive) heart failure |
| 8 | ICD-10 | `J95851` | Ventilator associated pneumonia |
| 9 | ICD-10 | `E43` | Unspecified severe protein-calorie malnutrition |
| 10 | ICD-10 | `R64` | Cachexia |
| 11 | ICD-10 | `E872` | Acidosis |
| 12 | ICD-10 | `E5112` | Wet beriberi |
| 13 | ICD-10 | `I82401` | Acute embolism and thrombosis of unspecified deep veins of right lower extremity |
| 14 | ICD-10 | `Z681` | Body mass index (BMI) 19.9 or less, adult |
| 15 | ICD-10 | `E873` | Alkalosis |
| 16 | ICD-10 | `I5181` | Takotsubo syndrome |
| 17 | ICD-10 | `E870` | Hyperosmolality and hypernatremia |
| 18 | ICD-10 | `R34` | Anuria and oliguria |
| 19 | ICD-10 | `D61818` | Other pancytopenia |
| 20 | ICD-10 | `D696` | Thrombocytopenia, unspecified |
| 21 | ICD-10 | `R680` | Hypothermia, not associated with low environmental temperature |
| 22 | ICD-10 | `F1020` | Alcohol dependence, uncomplicated |
| 23 | ICD-10 | `F17210` | Nicotine dependence, cigarettes, uncomplicated |
| 24 | ICD-10 | `E039` | Hypothyroidism, unspecified |
| 25 | ICD-10 | `I10` | Essential (primary) hypertension |
| 26 | ICD-10 | `I340` | Nonrheumatic mitral (valve) insufficiency |
| 27 | ICD-10 | `K7030` | Alcoholic cirrhosis of liver without ascites |
| 28 | ICD-10 | `K7010` | Alcoholic hepatitis without ascites |
| 29 | ICD-10 | `E59` | Dietary selenium deficiency |
| 30 | ICD-10 | `E60` | Dietary zinc deficiency |
| 31 | ICD-10 | `D124` | Benign neoplasm of descending colon |
| 32 | ICD-10 | `K5730` | Diverticulosis of large intestine without perforation or abscess without bleeding |
| 33 | ICD-10 | `E876` | Hypokalemia |
| 34 | ICD-10 | `R197` | Diarrhea, unspecified |
| 35 | ICD-10 | `J45909` | Unspecified asthma, uncomplicated |
| 36 | ICD-10 | `Z9884` | Bariatric surgery status |
| 37 | ICD-10 | `Y848` | Other medical procedures as the cause of abnormal reaction of the patient, or of later complication, without mention of misadventure at the time of the procedure |
| 38 | ICD-10 | `Y92230` | Patient room in hospital as the place of occurrence of the external cause |

## 5. ICU Stays

| Stay ID | First Care Unit | Last Care Unit | ICU Admit | ICU Discharge | LOS (days) |
|---|---|---|---|---|---|
| 33281088 | Medical/Surgical Intensive Care Unit (MICU/SICU) | Medical/Surgical Intensive Care Unit (MICU/SICU) | 2140-01-23 18:08:00 | 2140-02-08 22:28:20 | 16.18 |

## 6. Escalation / Severity Indicators

The following critical conditions or interventions were detected:

- **Acute Kidney Injury** (ICD diagnosis)
- **Arterial Line** (ICU procedure event)
- **Endotracheal Intubation** (ICU procedure event)
- **Invasive Mechanical Ventilation** (ICU procedure event)
- **Renal Replacement Therapy / Dialysis** (ICU procedure event)
- **Respiratory Failure** (ICD diagnosis)

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2140-01-24 | ICD-10 | `0DJD8ZZ` | Inspection of Lower Intestinal Tract, Via Natural or Artificial Opening Endoscopic |
| 2 | 2140-01-31 | ICD-10 | `06H03DZ` | Insertion of Intraluminal Device into Inferior Vena Cava, Percutaneous Approach |
| 3 | 2140-02-02 | ICD-10 | `0B9D8ZZ` | Drainage of Right Middle Lung Lobe, Via Natural or Artificial Opening Endoscopic |
| 4 | 2140-02-03 | ICD-10 | `0B9D8ZZ` | Drainage of Right Middle Lung Lobe, Via Natural or Artificial Opening Endoscopic |
| 5 | 2140-01-24 | ICD-10 | `02HV33Z` | Insertion of Infusion Device into Superior Vena Cava, Percutaneous Approach |
| 6 | 2140-01-24 | ICD-10 | `B548ZZA` | Ultrasonography of Superior Vena Cava, Guidance |
| 7 | 2140-01-30 | ICD-10 | `05HM33Z` | Insertion of Infusion Device into Right Internal Jugular Vein, Percutaneous Approach |
| 8 | 2140-01-30 | ICD-10 | `B543ZZ3` | Ultrasonography of Right Jugular Veins, Intravascular |
| 9 | 2140-01-30 | ICD-10 | `3E0G76Z` | Introduction of Nutritional Substance into Upper GI, Via Natural or Artificial Opening |
| 10 | 2140-01-30 | ICD-10 | `5A1D60Z` | Performance of Urinary Filtration, Multiple |
| 11 | 2140-02-01 | ICD-10 | `5A1935Z` | Respiratory Ventilation, Less than 24 Consecutive Hours |
| 12 | 2140-02-01 | ICD-10 | `0BH17EZ` | Insertion of Endotracheal Airway into Trachea, Via Natural or Artificial Opening |
| 13 | 2140-02-02 | ICD-10 | `0BH17EZ` | Insertion of Endotracheal Airway into Trachea, Via Natural or Artificial Opening |
| 14 | 2140-02-02 | ICD-10 | `5A1945Z` | Respiratory Ventilation, 24-96 Consecutive Hours |
| 15 | 2140-02-04 | ICD-10 | `0BH17EZ` | Insertion of Endotracheal Airway into Trachea, Via Natural or Artificial Opening |
| 16 | 2140-02-04 | ICD-10 | `5A1945Z` | Respiratory Ventilation, 24-96 Consecutive Hours |
| 17 | 2140-02-18 | ICD-10 | `0DJ08ZZ` | Inspection of Upper Intestinal Tract, Via Natural or Artificial Opening Endoscopic |
| 18 | 2140-02-20 | ICD-10 | `05HM33Z` | Insertion of Infusion Device into Right Internal Jugular Vein, Percutaneous Approach |
| 19 | 2140-02-25 | ICD-10 | `0DJD8ZZ` | Inspection of Lower Intestinal Tract, Via Natural or Artificial Opening Endoscopic |
| 20 | 2140-01-23 | ICD-10 | `06HM33Z` | Insertion of Infusion Device into Right Femoral Vein, Percutaneous Approach |
| 21 | 2140-01-23 | ICD-10 | `B54BZZA` | Ultrasonography of Right Lower Extremity Veins, Guidance |

### ICU Procedure Events (from `icu/procedureevents.csv.gz`)

- Trauma line (category: Access Lines - Invasive, started: 2140-01-23 18:00:00, status: FinishedRunning)
- 22 Gauge (category: Access Lines - Peripheral, started: 2140-01-23 18:00:00, status: FinishedRunning)
- 20 Gauge (category: Access Lines - Peripheral, started: 2140-01-23 18:00:00, status: FinishedRunning)
- Foley Catheter (category: GI/GU, started: 2140-01-23 18:53:00, status: FinishedRunning)
- Nasal Swab (category: 6-Cultures, started: 2140-01-23 19:15:00, status: FinishedRunning)
- EKG (category: 4-Procedures, started: 2140-01-23 20:33:00, status: FinishedRunning)
- Stool Culture (category: 6-Cultures, started: 2140-01-23 22:01:00, status: FinishedRunning)
- Urine Culture (category: 6-Cultures, started: 2140-01-24 01:43:00, status: FinishedRunning)
- PICC Line (category: Access Lines - Invasive, started: 2140-01-24 16:00:00, status: FinishedRunning)
- Chest X-Ray (category: 5-Imaging, started: 2140-01-27 04:52:00, status: FinishedRunning)
- CT scan (category: 5-Imaging, started: 2140-01-29 15:30:00, status: FinishedRunning)
- Interventional Radiology (category: 5-Imaging, started: 2140-01-30 16:10:00, status: FinishedRunning)
- Dialysis Catheter (category: Access Lines - Invasive, started: 2140-01-30 20:00:00, status: Stopped)
- Arterial Line (category: Access Lines - Invasive, started: 2140-01-31 00:00:00, status: Stopped)
- Invasive Ventilation (category: 2-Ventilation, started: 2140-02-01 16:33:00, status: FinishedRunning)
- Dialysis - CRRT (category: Dialysis, started: 2140-02-01 17:34:00, status: FinishedRunning)
- Extubation (category: 1-Intubation/Extubation, started: 2140-02-02 17:40:00, status: FinishedRunning)
- Intubation (category: 1-Intubation/Extubation, started: 2140-02-02 19:03:00, status: FinishedRunning)
- Ultrasound (category: 5-Imaging, started: 2140-02-08 14:34:00, status: FinishedRunning)

## 8. Critical Findings (Charted Events)

- **Ventilator Mode** (first noted: 2140-02-01 14:00:00)
- **Ventilator Type** (first noted: 2140-02-01 14:00:00)
- **Ventilator Tank #2** (first noted: 2140-02-01 16:00:00)
- **Known difficult intubation** (first noted: 2140-02-01 14:00:00)
- **Code Status** (first noted: 2140-01-24 19:45:00)
- **Seizure** (first noted: 2140-01-23 20:00:00)
- **Stroke Volume Index (SVI NICOM)** (first noted: 2140-02-05 11:31:00)
- **Dialysis Catheter Placement Confirmed by X-ray** (first noted: 2140-01-30 20:00:00)
- **Dialysis Catheter placed in outside facility** (first noted: 2140-01-30 20:00:00)
- **Dialysis Catheter Dressing Occlusive** (first noted: 2140-01-30 20:00:00)

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2140-01-23 12:35:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2140-01-23 12:35:00 | Transfer | → Emergency Department (ED) |
| 2140-01-23 16:19:00 | Admission | Admitted from EMERGENCY ROOM (EW EMER.) |
| 2140-01-23 18:08:00 | ED Departure | Left Emergency Dept. |
| 2140-01-23 18:08:00 | ICU Admission | Medical/Surgical Intensive Care Unit (MICU/SICU) (LOS: 16.2 days) |
| 2140-02-08 22:28:20 | Transfer | → Medicine (transfer) |
| 2140-02-26 18:15:00 | Discharge | To CHRONIC/LONG TERM ACUTE CARE |

## 10. Missing / Ambiguous Data

- No obvious missing critical fields detected.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
