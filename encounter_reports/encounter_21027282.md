# Encounter Report — HADM 21027282

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 21027282 |
| Subject ID | 10018081 |
| Patient Sex | M |
| Patient Anchor Age (at anchor year) | 79 |
| Anchor Year | 2133 |
| Admission Time | 2133-12-18 16:58:00 |
| Discharge Time | 2134-01-12 11:00:00 |
| Admission Type | EW EMER. |
| Admission Location | EMERGENCY ROOM |
| Discharge Location | SKILLED NURSING FACILITY |
| Insurance | Medicare |
| Language | ENGLISH |
| Marital Status | MARRIED |
| Race/Ethnicity | WHITE |
| ED Registration | 2133-12-18 12:09:00 |
| ED Departure | 2133-12-18 17:10:00 |
| In-Hospital Mortality | No |
| Date of Death (overall) | 2134-10-28 |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| APR | 710 | INFECTIOUS & PARASITIC DISEASES INCLUDING HIV W O.R. PROCEDURE | 4.0 | 4.0 |
| HCFA | 853 | INFECTIOUS & PARASITIC DISEASES W O.R. PROCEDURE W MCC | N/A | N/A |

### Primary Diagnosis (seq_num = 1)

- **ICD-9 0389**: Unspecified septicemia

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2133-12-18 16:58:44 | N/A | SURG |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-9 `0389`: Unspecified septicemia
- (seq 2) ICD-9 `5570`: Acute vascular insufficiency of intestine
- (seq 3) ICD-9 `78552`: Septic shock
- (seq 4) ICD-9 `5845`: Acute kidney failure with lesion of tubular necrosis
- (seq 5) ICD-9 `4271`: Paroxysmal ventricular tachycardia

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-9 | `0389` | Unspecified septicemia |
| 2 | ICD-9 | `5570` | Acute vascular insufficiency of intestine |
| 3 | ICD-9 | `78552` | Septic shock |
| 4 | ICD-9 | `5845` | Acute kidney failure with lesion of tubular necrosis |
| 5 | ICD-9 | `4271` | Paroxysmal ventricular tachycardia |
| 6 | ICD-9 | `34830` | Encephalopathy, unspecified |
| 7 | ICD-9 | `514` | Pulmonary congestion and hypostasis |
| 8 | ICD-9 | `78959` | Other ascites |
| 9 | ICD-9 | `2760` | Hyperosmolality and/or hypernatremia |
| 10 | ICD-9 | `1120` | Candidiasis of mouth |
| 11 | ICD-9 | `2639` | Unspecified protein-calorie malnutrition |
| 12 | ICD-9 | `2762` | Acidosis |
| 13 | ICD-9 | `5990` | Urinary tract infection, site not specified |
| 14 | ICD-9 | `2761` | Hyposmolality and/or hyponatremia |
| 15 | ICD-9 | `4280` | Congestive heart failure, unspecified |
| 16 | ICD-9 | `42731` | Atrial fibrillation |
| 17 | ICD-9 | `4019` | Unspecified essential hypertension |
| 18 | ICD-9 | `2720` | Pure hypercholesterolemia |
| 19 | ICD-9 | `78820` | Retention of urine, unspecified |
| 20 | ICD-9 | `78838` | Overflow incontinence |
| 21 | ICD-9 | `2875` | Thrombocytopenia, unspecified |
| 22 | ICD-9 | `79092` | Abnormal coagulation profile |
| 23 | ICD-9 | `2768` | Hypopotassemia |
| 24 | ICD-9 | `V5861` | Long-term (current) use of anticoagulants |
| 25 | ICD-9 | `41401` | Coronary atherosclerosis of native coronary artery |
| 26 | ICD-9 | `2724` | Other and unspecified hyperlipidemia |
| 27 | ICD-9 | `99592` | Severe sepsis |
| 28 | ICD-9 | `55329` | Other ventral hernia without mention of obstruction or gangrene |
| 29 | ICD-9 | `V4572` | Acquired absence of intestine (large) (small) |

## 5. ICU Stays

| Stay ID | First Care Unit | Last Care Unit | ICU Admit | ICU Discharge | LOS (days) |
|---|---|---|---|---|---|
| 37293400 | Trauma SICU (TSICU) | Trauma SICU (TSICU) | 2133-12-18 17:10:00 | 2134-01-01 14:44:53 | 13.90 |

## 6. Escalation / Severity Indicators

The following critical conditions or interventions were detected:

- **Acute Kidney Injury** (ICD diagnosis)
- **Arterial Line** (ICU procedure event)
- **Endotracheal Intubation** (ICU procedure event)
- **Invasive Mechanical Ventilation** (ICU procedure event)
- **Sepsis** (ICD diagnosis)
- **Shock** (ICD diagnosis)

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2133-12-18 | ICD-9 | `4573` | Open and other right hemicolectomy |
| 2 | 2133-12-20 | ICD-9 | `5359` | Repair of other hernia of anterior abdominal wall |
| 3 | 2133-12-20 | ICD-9 | `4620` | Ileostomy, not otherwise specified |
| 4 | 2133-12-20 | ICD-9 | `9672` | Continuous invasive mechanical ventilation for 96 consecutive hours or more |
| 5 | 2134-01-09 | ICD-9 | `4311` | Percutaneous [endoscopic] gastrostomy [PEG] |
| 6 | 2133-12-23 | ICD-9 | `966` | Enteral infusion of concentrated nutritional substances |

### ICU Procedure Events (from `icu/procedureevents.csv.gz`)

- Invasive Ventilation (category: 2-Ventilation, started: 2133-12-18 17:00:00, status: FinishedRunning)
- 20 Gauge (category: Access Lines - Peripheral, started: 2133-12-18 17:00:00, status: FinishedRunning)
- OR Received (category: 3-Significant Events, started: 2133-12-18 17:00:00, status: FinishedRunning)
- Multi Lumen (category: Access Lines - Invasive, started: 2133-12-18 20:00:00, status: FinishedRunning)
- Arterial Line (category: Access Lines - Invasive, started: 2133-12-18 20:00:00, status: FinishedRunning)
- EKG (category: 4-Procedures, started: 2133-12-18 22:12:00, status: FinishedRunning)
- Transthoracic Echo (category: 5-Imaging, started: 2133-12-20 10:50:00, status: FinishedRunning)
- OR Sent (category: 3-Significant Events, started: 2133-12-20 10:50:00, status: FinishedRunning)
- Chest X-Ray (category: 5-Imaging, started: 2133-12-20 14:30:00, status: FinishedRunning)
- Extubation (category: 1-Intubation/Extubation, started: 2133-12-21 05:05:00, status: FinishedRunning)
- Intubation (category: 1-Intubation/Extubation, started: 2133-12-21 05:06:00, status: FinishedRunning)
- Family updated by RN (category: 7-Communication, started: 2133-12-23 08:50:00, status: FinishedRunning)
- Urine Culture (category: 6-Cultures, started: 2133-12-25 16:09:00, status: FinishedRunning)
- Blood Cultured (category: 6-Cultures, started: 2133-12-26 11:00:00, status: FinishedRunning)
- CT scan (category: 5-Imaging, started: 2133-12-27 16:00:00, status: FinishedRunning)
- Family updated by MD (category: 7-Communication, started: 2133-12-27 20:12:00, status: FinishedRunning)

## 8. Critical Findings (Charted Events)

- **Ventilator Type** (first noted: 2133-12-18 17:00:00)
- **Ventilator Mode** (first noted: 2133-12-18 17:00:00)
- **Ventilator Tank #2** (first noted: 2133-12-18 17:00:00)
- **Known difficult intubation** (first noted: 2133-12-18 20:31:00)
- **Code Status** (first noted: 2133-12-19 02:28:00)

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2133-12-18 12:09:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2133-12-18 12:09:00 | Transfer | → Emergency Department (ED) |
| 2133-12-18 16:58:00 | Admission | Admitted from EMERGENCY ROOM (EW EMER.) |
| 2133-12-18 17:10:00 | ED Departure | Left Emergency Dept. |
| 2133-12-18 17:10:00 | ICU Admission | Trauma SICU (TSICU) (LOS: 13.9 days) |
| 2134-01-01 14:44:53 | Transfer | → Med/Surg/Trauma (transfer) |
| 2134-01-12 11:00:00 | Discharge | To SKILLED NURSING FACILITY |

## 10. Missing / Ambiguous Data

- No obvious missing critical fields detected.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
