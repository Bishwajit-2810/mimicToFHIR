# Encounter Report — HADM 24928679

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 24928679 |
| Subject ID | 10039708 |
| Patient Sex | F |
| Patient Anchor Age (at anchor year) | 46 |
| Anchor Year | 2138 |
| Admission Time | 2143-09-19 18:36:00 |
| Discharge Time | 2143-09-22 23:00:00 |
| Admission Type | OBSERVATION ADMIT |
| Admission Location | CLINIC REFERRAL |
| Discharge Location | HOME HEALTH CARE |
| Insurance | Other |
| Language | ENGLISH |
| Marital Status | SINGLE |
| Race/Ethnicity | BLACK/AFRICAN AMERICAN |
| ED Registration | 2143-09-19 10:57:00 |
| ED Departure | 2143-09-19 20:57:00 |
| In-Hospital Mortality | No |
| Date of Death (overall) | N/A |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| APR | 280 | ALCOHOLIC LIVER DISEASE | 3.0 | 4.0 |
| HCFA | 432 | CIRRHOSIS & ALCOHOLIC HEPATITIS W MCC | N/A | N/A |

### Primary Diagnosis (seq_num = 1)

- **ICD-10 K7031**: Alcoholic cirrhosis of liver with ascites

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2143-09-19 18:37:50 | N/A | MED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-10 `K7031`: Alcoholic cirrhosis of liver with ascites
- (seq 2) ICD-10 `I8511`: Secondary esophageal varices with bleeding
- (seq 3) ICD-10 `K767`: Hepatorenal syndrome
- (seq 4) ICD-10 `N186`: End stage renal disease
- (seq 5) ICD-10 `K284`: Chronic or unspecified gastrojejunal ulcer with hemorrhage

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-10 | `K7031` | Alcoholic cirrhosis of liver with ascites |
| 2 | ICD-10 | `I8511` | Secondary esophageal varices with bleeding |
| 3 | ICD-10 | `K767` | Hepatorenal syndrome |
| 4 | ICD-10 | `N186` | End stage renal disease |
| 5 | ICD-10 | `K284` | Chronic or unspecified gastrojejunal ulcer with hemorrhage |
| 6 | ICD-10 | `D62` | Acute posthemorrhagic anemia |
| 7 | ICD-10 | `K861` | Other chronic pancreatitis |
| 8 | ICD-10 | `E872` | Acidosis |
| 9 | ICD-10 | `K7040` | Alcoholic hepatic failure without coma |
| 10 | ICD-10 | `R600` | Localized edema |
| 11 | ICD-10 | `D539` | Nutritional anemia, unspecified |
| 12 | ICD-10 | `D6959` | Other secondary thrombocytopenia |
| 13 | ICD-10 | `E039` | Hypothyroidism, unspecified |
| 14 | ICD-10 | `M109` | Gout, unspecified |
| 15 | ICD-10 | `R300` | Dysuria |
| 16 | ICD-10 | `R7989` | Other specified abnormal findings of blood chemistry |
| 17 | ICD-10 | `E875` | Hyperkalemia |
| 18 | ICD-10 | `R2232` | Localized swelling, mass and lump, left upper limb |
| 19 | ICD-10 | `N281` | Cyst of kidney, acquired |
| 20 | ICD-10 | `F1010` | Alcohol abuse, uncomplicated |
| 21 | ICD-10 | `F17210` | Nicotine dependence, cigarettes, uncomplicated |
| 22 | ICD-10 | `Z992` | Dependence on renal dialysis |
| 23 | ICD-10 | `Z86718` | Personal history of other venous thrombosis and embolism |
| 24 | ICD-10 | `Z9884` | Bariatric surgery status |
| 25 | ICD-10 | `Z980` | Intestinal bypass and anastomosis status |

## 5. ICU Stays

| Stay ID | First Care Unit | Last Care Unit | ICU Admit | ICU Discharge | LOS (days) |
|---|---|---|---|---|---|
| 37323533 | Surgical Intensive Care Unit (SICU) | Surgical Intensive Care Unit (SICU) | 2143-09-19 19:40:55 | 2143-09-20 16:29:51 | 0.87 |

## 6. Escalation / Severity Indicators

_No escalation indicators detected from ICD codes or ICU procedure events._

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2143-09-20 | ICD-10 | `06L38CZ` | Occlusion of Esophageal Vein with Extraluminal Device, Via Natural or Artificial Opening Endoscopic |
| 2 | 2143-09-21 | ICD-10 | `5A1D70Z` | Performance of Urinary Filtration, Intermittent, Less than 6 Hours Per Day |

### ICU Procedure Events (from `icu/procedureevents.csv.gz`)

- 22 Gauge (category: Access Lines - Peripheral, started: 2143-09-19 21:19:00, status: FinishedRunning)
- 20 Gauge (category: Access Lines - Peripheral, started: 2143-09-19 21:19:00, status: FinishedRunning)
- EKG (category: 4-Procedures, started: 2143-09-20 06:12:00, status: FinishedRunning)

## 8. Critical Findings (Charted Events)

- **Seizure** (first noted: 2143-09-20 04:00:00)

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2143-09-19 10:57:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2143-09-19 10:57:00 | Transfer | → Emergency Department (ED) |
| 2143-09-19 18:36:00 | Admission | Admitted from CLINIC REFERRAL (OBSERVATION ADMIT) |
| 2143-09-19 19:40:55 | ICU Admission | Surgical Intensive Care Unit (SICU) (LOS: 0.9 days) |
| 2143-09-19 19:40:55 | Transfer | → Surgical Intensive Care Unit (SICU) (transfer) |
| 2143-09-19 20:57:00 | ED Departure | Left Emergency Dept. |
| 2143-09-20 16:29:51 | Transfer | → Transplant (transfer) |
| 2143-09-22 23:00:00 | Discharge | To HOME HEALTH CARE |

## 10. Missing / Ambiguous Data

- No obvious missing critical fields detected.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
