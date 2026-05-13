# Encounter Report — HADM 22987108

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 22987108 |
| Subject ID | 10007818 |
| Patient Sex | M |
| Patient Anchor Age (at anchor year) | 69 |
| Anchor Year | 2146 |
| Admission Time | 2146-06-10 16:37:00 |
| Discharge Time | 2146-07-12 00:00:00 |
| Admission Type | DIRECT EMER. |
| Admission Location | PHYSICIAN REFERRAL |
| Discharge Location | DIED |
| Insurance | Medicare |
| Language | ENGLISH |
| Marital Status | MARRIED |
| Race/Ethnicity | WHITE |
| ED Registration | N/A |
| ED Departure | N/A |
| In-Hospital Mortality | YES — Death time: 2146-07-12 20:50:00 |
| Date of Death (overall) | 2146-07-12 |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| APR | 264 | OTHER HEPATOBILIARY, PANCREAS & ABDOMINAL PROCEDURES | 4.0 | 4.0 |
| HCFA | 420 | HEPATOBILIARY DIAGNOSTIC PROCEDURES W MCC | N/A | N/A |

### Primary Diagnosis (seq_num = 1)

- **ICD-10 K7469**: Other cirrhosis of liver

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2146-06-10 16:38:18 | N/A | MED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-10 `K7469`: Other cirrhosis of liver
- (seq 2) ICD-10 `K767`: Hepatorenal syndrome
- (seq 3) ICD-10 `J9600`: Acute respiratory failure, unspecified whether with hypoxia or hypercapnia
- (seq 4) ICD-10 `A4151`: Sepsis due to Escherichia coli [E. coli]
- (seq 5) ICD-10 `N179`: Acute kidney failure, unspecified

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-10 | `K7469` | Other cirrhosis of liver |
| 2 | ICD-10 | `K767` | Hepatorenal syndrome |
| 3 | ICD-10 | `J9600` | Acute respiratory failure, unspecified whether with hypoxia or hypercapnia |
| 4 | ICD-10 | `A4151` | Sepsis due to Escherichia coli [E. coli] |
| 5 | ICD-10 | `N179` | Acute kidney failure, unspecified |
| 6 | ICD-10 | `K661` | Hemoperitoneum |
| 7 | ICD-10 | `R571` | Hypovolemic shock |
| 8 | ICD-10 | `R6521` | Severe sepsis with septic shock |
| 9 | ICD-10 | `K659` | Peritonitis, unspecified |
| 10 | ICD-10 | `N183` | Chronic kidney disease, stage 3 (moderate) |
| 11 | ICD-10 | `E43` | Unspecified severe protein-calorie malnutrition |
| 12 | ICD-10 | `K7201` | Acute and subacute hepatic failure with coma |
| 13 | ICD-10 | `T8119XA` | Other postprocedural shock, initial encounter |
| 14 | ICD-10 | `K7200` | Acute and subacute hepatic failure without coma |
| 15 | ICD-10 | `D684` | Acquired coagulation factor deficiency |
| 16 | ICD-10 | `J95851` | Ventilator associated pneumonia |
| 17 | ICD-10 | `R188` | Other ascites |
| 18 | ICD-10 | `D62` | Acute posthemorrhagic anemia |
| 19 | ICD-10 | `I4892` | Unspecified atrial flutter |
| 20 | ICD-10 | `K766` | Portal hypertension |
| 21 | ICD-10 | `E871` | Hypo-osmolality and hyponatremia |
| 22 | ICD-10 | `N390` | Urinary tract infection, site not specified |
| 23 | ICD-10 | `K567` | Ileus, unspecified |
| 24 | ICD-10 | `E872` | Acidosis |
| 25 | ICD-10 | `J9811` | Atelectasis |
| 26 | ICD-10 | `I97610` | Postprocedural hemorrhage of a circulatory system organ or structure following a cardiac catheterization |
| 27 | ICD-10 | `T80219A` | Unspecified infection due to central venous catheter, initial encounter |
| 28 | ICD-10 | `K7581` | Nonalcoholic steatohepatitis (NASH) |
| 29 | ICD-10 | `I129` | Hypertensive chronic kidney disease with stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease |
| 30 | ICD-10 | `D638` | Anemia in other chronic diseases classified elsewhere |
| 31 | ICD-10 | `I25118` | Atherosclerotic heart disease of native coronary artery with other forms of angina pectoris |
| 32 | ICD-10 | `Z955` | Presence of coronary angioplasty implant and graft |
| 33 | ICD-10 | `E119` | Type 2 diabetes mellitus without complications |
| 34 | ICD-10 | `Z794` | Long term (current) use of insulin |
| 35 | ICD-10 | `R627` | Adult failure to thrive |
| 36 | ICD-10 | `I4891` | Unspecified atrial fibrillation |
| 37 | ICD-10 | `B9689` | Other specified bacterial agents as the cause of diseases classified elsewhere |
| 38 | ICD-10 | `B9561` | Methicillin susceptible Staphylococcus aureus infection as the cause of diseases classified elsewhere |
| 39 | ICD-10 | `Y848` | Other medical procedures as the cause of abnormal reaction of the patient, or of later complication, without mention of misadventure at the time of the procedure |

## 5. ICU Stays

| Stay ID | First Care Unit | Last Care Unit | ICU Admit | ICU Discharge | LOS (days) |
|---|---|---|---|---|---|
| 32359580 | Medical Intensive Care Unit (MICU) | Medical Intensive Care Unit (MICU) | 2146-06-22 11:46:29 | 2146-07-13 00:27:47 | 20.53 |

## 6. Escalation / Severity Indicators

The following critical conditions or interventions were detected:

- **Acute Kidney Injury** (ICD diagnosis)
- **Arterial Line** (ICU procedure event)
- **Endotracheal Intubation** (ICU procedure event)
- **Invasive Mechanical Ventilation** (ICU procedure event)
- **Liver Failure** (ICD diagnosis)
- **Renal Replacement Therapy / Dialysis** (ICU procedure event)
- **Respiratory Failure** (ICD diagnosis)
- **Sepsis** (ICD diagnosis)
- **Shock** (ICD diagnosis)

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2146-06-11 | ICD-10 | `0W9G3ZZ` | Drainage of Peritoneal Cavity, Percutaneous Approach |
| 2 | 2146-06-19 | ICD-10 | `0W9G3ZX` | Drainage of Peritoneal Cavity, Percutaneous Approach, Diagnostic |
| 3 | 2146-06-22 | ICD-10 | `04LK3DZ` | Occlusion of Right Femoral Artery with Intraluminal Device, Percutaneous Approach |
| 4 | 2146-06-23 | ICD-10 | `03LP3DZ` | Occlusion of Right Vertebral Artery with Intraluminal Device, Percutaneous Approach |
| 5 | 2146-06-29 | ICD-10 | `0BCJ8ZZ` | Extirpation of Matter from Left Lower Lung Lobe, Via Natural or Artificial Opening Endoscopic |
| 6 | 2146-06-29 | ICD-10 | `0BCH8ZZ` | Extirpation of Matter from Lung Lingula, Via Natural or Artificial Opening Endoscopic |
| 7 | 2146-07-07 | ICD-10 | `0BCJ8ZZ` | Extirpation of Matter from Left Lower Lung Lobe, Via Natural or Artificial Opening Endoscopic |
| 8 | 2146-07-09 | ICD-10 | `0BCJ8ZZ` | Extirpation of Matter from Left Lower Lung Lobe, Via Natural or Artificial Opening Endoscopic |
| 9 | 2146-07-02 | ICD-10 | `0W9G3ZX` | Drainage of Peritoneal Cavity, Percutaneous Approach, Diagnostic |
| 10 | 2146-06-22 | ICD-10 | `5A1955Z` | Respiratory Ventilation, Greater than 96 Consecutive Hours |
| 11 | 2146-06-11 | ICD-10 | `3E0G76Z` | Introduction of Nutritional Substance into Upper GI, Via Natural or Artificial Opening |
| 12 | 2146-07-07 | ICD-10 | `3E0436Z` | Introduction of Nutritional Substance into Central Vein, Percutaneous Approach |
| 13 | 2146-06-22 | ICD-10 | `0BH17EZ` | Insertion of Endotracheal Airway into Trachea, Via Natural or Artificial Opening |
| 14 | 2146-06-13 | ICD-10 | `0W9G3ZZ` | Drainage of Peritoneal Cavity, Percutaneous Approach |
| 15 | 2146-06-20 | ICD-10 | `02H633Z` | Insertion of Infusion Device into Right Atrium, Percutaneous Approach |
| 16 | 2146-06-20 | ICD-10 | `B214YZZ` | Fluoroscopy of Right Heart using Other Contrast |
| 17 | 2146-06-21 | ICD-10 | `B211YZZ` | Fluoroscopy of Multiple Coronary Arteries using Other Contrast |
| 18 | 2146-06-22 | ICD-10 | `02HV33Z` | Insertion of Infusion Device into Superior Vena Cava, Percutaneous Approach |
| 19 | 2146-06-22 | ICD-10 | `B518YZA` | Fluoroscopy of Superior Vena Cava using Other Contrast, Guidance |
| 20 | 2146-06-21 | ICD-10 | `5A1D60Z` | Performance of Urinary Filtration, Multiple |
| 21 | 2146-07-10 | ICD-10 | `0BC78ZZ` | Extirpation of Matter from Left Main Bronchus, Via Natural or Artificial Opening Endoscopic |
| 22 | 2146-07-03 | ICD-10 | `0B968ZX` | Drainage of Right Lower Lobe Bronchus, Via Natural or Artificial Opening Endoscopic, Diagnostic |
| 23 | 2146-06-29 | ICD-10 | `0BC78ZZ` | Extirpation of Matter from Left Main Bronchus, Via Natural or Artificial Opening Endoscopic |

### ICU Procedure Events (from `icu/procedureevents.csv.gz`)

- Foley Catheter (category: GI/GU, started: 2146-06-22 12:15:00, status: FinishedRunning)
- Intubation (category: 1-Intubation/Extubation, started: 2146-06-22 12:49:00, status: FinishedRunning)
- Invasive Ventilation (category: 2-Ventilation, started: 2146-06-22 12:49:00, status: FinishedRunning)
- Intraosseous Device (category: Access Lines - Invasive, started: 2146-06-22 13:30:00, status: FinishedRunning)
- Trauma line (category: Access Lines - Invasive, started: 2146-06-22 18:00:00, status: FinishedRunning)
- Dialysis Catheter (category: Access Lines - Invasive, started: 2146-06-22 18:00:00, status: FinishedRunning)
- Dialysis - CRRT (category: Dialysis, started: 2146-06-22 21:10:00, status: FinishedRunning)
- CT scan (category: 5-Imaging, started: 2146-06-23 08:35:00, status: FinishedRunning)
- 18 Gauge (category: Access Lines - Peripheral, started: 2146-06-23 15:00:00, status: FinishedRunning)
- Chest X-Ray (category: 5-Imaging, started: 2146-06-23 21:00:00, status: FinishedRunning)
- Ultrasound (category: 5-Imaging, started: 2146-06-26 11:30:00, status: FinishedRunning)
- Family updated by RN (category: 7-Communication, started: 2146-06-26 12:04:00, status: FinishedRunning)
- Bronchoscopy (category: 4-Procedures, started: 2146-06-29 17:00:00, status: FinishedRunning)
- X-ray (category: 5-Imaging, started: 2146-06-30 12:00:00, status: FinishedRunning)
- Sputum Culture (category: 6-Cultures, started: 2146-06-30 20:19:00, status: FinishedRunning)
- 20 Gauge (category: Access Lines - Peripheral, started: 2146-07-01 13:54:00, status: FinishedRunning)
- EKG (category: 4-Procedures, started: 2146-07-02 01:25:00, status: FinishedRunning)
- Family updated by MD (category: 7-Communication, started: 2146-07-03 15:00:00, status: FinishedRunning)
- Arterial Line (category: Access Lines - Invasive, started: 2146-07-04 19:00:00, status: FinishedRunning)
- Multi Lumen (category: Access Lines - Invasive, started: 2146-07-04 22:30:00, status: FinishedRunning)
- Paracentesis (category: 4-Procedures, started: 2146-07-05 13:30:00, status: FinishedRunning)
- Blood Cultured (category: 6-Cultures, started: 2146-07-05 18:26:00, status: FinishedRunning)
- Hemodialysis (category: 4-Procedures, started: 2146-07-06 08:30:00, status: FinishedRunning)
- Interventional Radiology (category: 5-Imaging, started: 2146-07-08 11:41:00, status: FinishedRunning)

## 8. Critical Findings (Charted Events)

- **Ventilator Mode** (first noted: 2146-06-22 13:00:00)
- **Ventilator Type** (first noted: 2146-06-22 13:00:00)
- **Ventilator Tank #1** (first noted: 2146-06-22 13:00:00)
- **Known difficult intubation** (first noted: 2146-06-22 13:00:00)
- **Code Status** (first noted: 2146-07-11 00:46:00)
- **Dialysis Catheter Placement Confirmed by X-ray** (first noted: 2146-06-23 02:24:00)
- **Dialysis Catheter Dressing Occlusive** (first noted: 2146-06-23 02:24:00)
- **Dialysis Catheter Site Appear** (first noted: 2146-06-23 02:24:00)

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2146-06-10 16:37:00 | Admission | Admitted from PHYSICIAN REFERRAL (DIRECT EMER.) |
| 2146-06-22 11:46:29 | ICU Admission | Medical Intensive Care Unit (MICU) (LOS: 20.5 days) |
| 2146-06-22 11:46:29 | Transfer | → Medical Intensive Care Unit (MICU) (transfer) |
| 2146-07-12 00:00:00 | Discharge | To DIED |
| 2146-07-12 20:50:00 | **IN-HOSPITAL DEATH** | |

## 10. Missing / Ambiguous Data

- No ED registration time — admission may not have gone through ED.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
