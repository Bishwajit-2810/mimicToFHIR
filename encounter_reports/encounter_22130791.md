# Encounter Report — HADM 22130791

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 22130791 |
| Subject ID | 10015931 |
| Patient Sex | M |
| Patient Anchor Age (at anchor year) | 87 |
| Anchor Year | 2176 |
| Admission Time | 2177-03-24 21:47:00 |
| Discharge Time | 2177-03-29 14:15:00 |
| Admission Type | URGENT |
| Admission Location | TRANSFER FROM HOSPITAL |
| Discharge Location | DIED |
| Insurance | Medicare |
| Language | ENGLISH |
| Marital Status | MARRIED |
| Race/Ethnicity | WHITE |
| ED Registration | N/A |
| ED Departure | N/A |
| In-Hospital Mortality | YES — Death time: 2177-03-29 14:15:00 |
| Date of Death (overall) | 2177-03-29 |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| APR | 254 | OTHER DIGESTIVE SYSTEM DIAGNOSES | 4.0 | 4.0 |
| HCFA | 377 | G.I. HEMORRHAGE W MCC | N/A | N/A |

### Primary Diagnosis (seq_num = 1)

- **ICD-10 K921**: Melena

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2177-03-24 21:48:07 | N/A | MED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-10 `K921`: Melena
- (seq 2) ICD-10 `I214`: Non-ST elevation (NSTEMI) myocardial infarction
- (seq 3) ICD-10 `N170`: Acute kidney failure with tubular necrosis
- (seq 4) ICD-10 `J9601`: Acute respiratory failure with hypoxia
- (seq 5) ICD-10 `R571`: Hypovolemic shock

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-10 | `K921` | Melena |
| 2 | ICD-10 | `I214` | Non-ST elevation (NSTEMI) myocardial infarction |
| 3 | ICD-10 | `N170` | Acute kidney failure with tubular necrosis |
| 4 | ICD-10 | `J9601` | Acute respiratory failure with hypoxia |
| 5 | ICD-10 | `R571` | Hypovolemic shock |
| 6 | ICD-10 | `N184` | Chronic kidney disease, stage 4 (severe) |
| 7 | ICD-10 | `G9340` | Encephalopathy, unspecified |
| 8 | ICD-10 | `D696` | Thrombocytopenia, unspecified |
| 9 | ICD-10 | `E872` | Acidosis |
| 10 | ICD-10 | `D62` | Acute posthemorrhagic anemia |
| 11 | ICD-10 | `I5042` | Chronic combined systolic (congestive) and diastolic (congestive) heart failure |
| 12 | ICD-10 | `I130` | Hypertensive heart and chronic kidney disease with heart failure and stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease |
| 13 | ICD-10 | `Q6432` | Congenital stricture of urethra |
| 14 | ICD-10 | `I4891` | Unspecified atrial fibrillation |
| 15 | ICD-10 | `E1122` | Type 2 diabetes mellitus with diabetic chronic kidney disease |
| 16 | ICD-10 | `Z7901` | Long term (current) use of anticoagulants |
| 17 | ICD-10 | `N400` | Benign prostatic hyperplasia without lower urinary tract symptoms |
| 18 | ICD-10 | `Z66` | Do not resuscitate |
| 19 | ICD-10 | `E875` | Hyperkalemia |
| 20 | ICD-10 | `E8339` | Other disorders of phosphorus metabolism |
| 21 | ICD-10 | `J449` | Chronic obstructive pulmonary disease, unspecified |
| 22 | ICD-10 | `Z87442` | Personal history of urinary calculi |
| 23 | ICD-10 | `Z953` | Presence of xenogenic heart valve |

## 5. ICU Stays

| Stay ID | First Care Unit | Last Care Unit | ICU Admit | ICU Discharge | LOS (days) |
|---|---|---|---|---|---|
| 37093652 | Medical/Surgical Intensive Care Unit (MICU/SICU) | Medical/Surgical Intensive Care Unit (MICU/SICU) | 2177-03-24 21:48:07 | 2177-03-29 18:03:36 | 4.84 |

## 6. Escalation / Severity Indicators

The following critical conditions or interventions were detected:

- **Acute Kidney Injury** (ICD diagnosis)
- **Arterial Line** (ICU procedure event)
- **Endotracheal Intubation** (ICU procedure event)
- **Invasive Mechanical Ventilation** (ICU procedure event)
- **Respiratory Failure** (ICD diagnosis)
- **Shock** (ICD diagnosis)

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2177-03-25 | ICD-10 | `0DJ08ZZ` | Inspection of Upper Intestinal Tract, Via Natural or Artificial Opening Endoscopic |
| 2 | 2177-03-26 | ICD-10 | `0DC68ZZ` | Extirpation of Matter from Stomach, Via Natural or Artificial Opening Endoscopic |
| 3 | 2177-03-27 | ICD-10 | `0DJ08ZZ` | Inspection of Upper Intestinal Tract, Via Natural or Artificial Opening Endoscopic |
| 4 | 2177-03-25 | ICD-10 | `B415YZZ` | Fluoroscopy of Inferior Mesenteric Artery using Other Contrast |
| 5 | 2177-03-25 | ICD-10 | `B414YZZ` | Fluoroscopy of Superior Mesenteric Artery using Other Contrast |
| 6 | 2177-03-26 | ICD-10 | `04L23DZ` | Occlusion of Gastric Artery with Intraluminal Device, Percutaneous Approach |
| 7 | 2177-03-25 | ICD-10 | `5A1945Z` | Respiratory Ventilation, 24-96 Consecutive Hours |
| 8 | 2177-03-26 | ICD-10 | `02HV33Z` | Insertion of Infusion Device into Superior Vena Cava, Percutaneous Approach |
| 9 | 2177-03-26 | ICD-10 | `04HL33Z` | Insertion of Infusion Device into Left Femoral Artery, Percutaneous Approach |

### ICU Procedure Events (from `icu/procedureevents.csv.gz`)

- PICC Line (category: Access Lines - Invasive, started: 2177-03-24 22:30:00, status: FinishedRunning)
- EKG (category: 4-Procedures, started: 2177-03-24 23:51:00, status: FinishedRunning)
- 20 Gauge (category: Access Lines - Peripheral, started: 2177-03-25 00:00:00, status: FinishedRunning)
- Interventional Radiology (category: 5-Imaging, started: 2177-03-25 03:45:00, status: FinishedRunning)
- Intubation (category: 1-Intubation/Extubation, started: 2177-03-25 09:57:00, status: FinishedRunning)
- Invasive Ventilation (category: 2-Ventilation, started: 2177-03-25 10:00:00, status: FinishedRunning)
- Foley Catheter (category: GI/GU, started: 2177-03-25 17:45:00, status: FinishedRunning)
- X-ray (category: 5-Imaging, started: 2177-03-25 22:45:00, status: FinishedRunning)
- Arterial Line (category: Access Lines - Invasive, started: 2177-03-26 11:00:00, status: FinishedRunning)
- Multi Lumen (category: Access Lines - Invasive, started: 2177-03-26 11:00:00, status: FinishedRunning)
- Transthoracic Echo (category: 5-Imaging, started: 2177-03-26 14:00:00, status: FinishedRunning)
- Chest X-Ray (category: 5-Imaging, started: 2177-03-26 20:36:00, status: FinishedRunning)
- Blood Cultured (category: 6-Cultures, started: 2177-03-27 12:00:00, status: FinishedRunning)
- Endoscopy (category: 4-Procedures, started: 2177-03-27 13:20:00, status: FinishedRunning)
- Urine Culture (category: 6-Cultures, started: 2177-03-27 16:08:00, status: FinishedRunning)
- CT scan (category: 5-Imaging, started: 2177-03-28 11:35:00, status: FinishedRunning)
- Extubation (category: 1-Intubation/Extubation, started: 2177-03-29 13:11:00, status: FinishedRunning)

## 8. Critical Findings (Charted Events)

- **Ventilator Tank #2** (first noted: 2177-03-25 10:00:00)
- **Ventilator Mode** (first noted: 2177-03-25 10:00:00)
- **Ventilator Tank #1** (first noted: 2177-03-25 10:00:00)
- **Known difficult intubation** (first noted: 2177-03-25 10:00:00)
- **Stroke Volume Index (SVI NICOM)** (first noted: 2177-03-26 04:00:00)
- **Dialysis patient** (first noted: 2177-03-25 00:38:00)

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2177-03-24 21:47:00 | Admission | Admitted from TRANSFER FROM HOSPITAL (URGENT) |
| 2177-03-24 21:48:07 | ICU Admission | Medical/Surgical Intensive Care Unit (MICU/SICU) (LOS: 4.8 days) |
| 2177-03-29 14:15:00 | **IN-HOSPITAL DEATH** | |
| 2177-03-29 14:15:00 | Discharge | To DIED |

## 10. Missing / Ambiguous Data

- No ED registration time — admission may not have gone through ED.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
