# Encounter Report — HADM 25864431

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 25864431 |
| Subject ID | 10039708 |
| Patient Sex | F |
| Patient Anchor Age (at anchor year) | 46 |
| Anchor Year | 2138 |
| Admission Time | 2142-03-26 06:08:00 |
| Discharge Time | 2142-04-11 21:00:00 |
| Admission Type | URGENT |
| Admission Location | TRANSFER FROM HOSPITAL |
| Discharge Location | HOME HEALTH CARE |
| Insurance | Other |
| Language | ENGLISH |
| Marital Status | SINGLE |
| Race/Ethnicity | BLACK/AFRICAN AMERICAN |
| ED Registration | 2142-03-25 22:22:00 |
| ED Departure | 2142-03-26 08:08:00 |
| In-Hospital Mortality | No |
| Date of Death (overall) | N/A |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| APR | 264 | OTHER HEPATOBILIARY, PANCREAS & ABDOMINAL PROCEDURES | 4.0 | 4.0 |
| HCFA | 441 | DISORDERS OF LIVER EXCEPT MALIG,CIRR,ALC HEPA W MCC | N/A | N/A |

### Primary Diagnosis (seq_num = 1)

- **ICD-10 K7290**: Hepatic failure, unspecified without coma

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2142-03-26 06:09:35 | N/A | MED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-10 `K7290`: Hepatic failure, unspecified without coma
- (seq 2) ICD-10 `K8520`: Alcohol induced acute pancreatitis without necrosis or infection
- (seq 3) ICD-10 `K767`: Hepatorenal syndrome
- (seq 4) ICD-10 `E43`: Unspecified severe protein-calorie malnutrition
- (seq 5) ICD-10 `J189`: Pneumonia, unspecified organism

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-10 | `K7290` | Hepatic failure, unspecified without coma |
| 2 | ICD-10 | `K8520` | Alcohol induced acute pancreatitis without necrosis or infection |
| 3 | ICD-10 | `K767` | Hepatorenal syndrome |
| 4 | ICD-10 | `E43` | Unspecified severe protein-calorie malnutrition |
| 5 | ICD-10 | `J189` | Pneumonia, unspecified organism |
| 6 | ICD-10 | `K7681` | Hepatopulmonary syndrome |
| 7 | ICD-10 | `D689` | Coagulation defect, unspecified |
| 8 | ICD-10 | `N184` | Chronic kidney disease, stage 4 (severe) |
| 9 | ICD-10 | `N179` | Acute kidney failure, unspecified |
| 10 | ICD-10 | `D62` | Acute posthemorrhagic anemia |
| 11 | ICD-10 | `I8510` | Secondary esophageal varices without bleeding |
| 12 | ICD-10 | `K860` | Alcohol-induced chronic pancreatitis |
| 13 | ICD-10 | `D6959` | Other secondary thrombocytopenia |
| 14 | ICD-10 | `K7011` | Alcoholic hepatitis with ascites |
| 15 | ICD-10 | `K7031` | Alcoholic cirrhosis of liver with ascites |
| 16 | ICD-10 | `F1020` | Alcohol dependence, uncomplicated |
| 17 | ICD-10 | `M109` | Gout, unspecified |
| 18 | ICD-10 | `E039` | Hypothyroidism, unspecified |
| 19 | ICD-10 | `D539` | Nutritional anemia, unspecified |
| 20 | ICD-10 | `I129` | Hypertensive chronic kidney disease with stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease |
| 21 | ICD-10 | `F17210` | Nicotine dependence, cigarettes, uncomplicated |
| 22 | ICD-10 | `R0902` | Hypoxemia |
| 23 | ICD-10 | `Z66` | Do not resuscitate |
| 24 | ICD-10 | `Z9884` | Bariatric surgery status |
| 25 | ICD-10 | `Z86718` | Personal history of other venous thrombosis and embolism |
| 26 | ICD-10 | `Z6830` | Body mass index (BMI) 30.0-30.9, adult |

## 5. ICU Stays

_No ICU stay recorded for this admission._

## 6. Escalation / Severity Indicators

The following critical conditions or interventions were detected:

- **Acute Kidney Injury** (ICD diagnosis)
- **Liver Failure** (ICD diagnosis)
- **Pneumonia** (ICD diagnosis)

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2142-04-01 | ICD-10 | `0W9G3ZZ` | Drainage of Peritoneal Cavity, Percutaneous Approach |
| 2 | 2142-04-05 | ICD-10 | `0DJ08ZZ` | Inspection of Upper Intestinal Tract, Via Natural or Artificial Opening Endoscopic |
| 3 | 2142-04-05 | ICD-10 | `0DHA8UZ` | Insertion of Feeding Device into Jejunum, Via Natural or Artificial Opening Endoscopic |
| 4 | 2142-04-06 | ICD-10 | `3E0H76Z` | Introduction of Nutritional Substance into Lower GI, Via Natural or Artificial Opening |
| 5 | 2142-03-30 | ICD-10 | `02H633Z` | Insertion of Infusion Device into Right Atrium, Percutaneous Approach |
| 6 | 2142-03-31 | ICD-10 | `5A1D70Z` | Performance of Urinary Filtration, Intermittent, Less than 6 Hours Per Day |
| 7 | 2142-04-08 | ICD-10 | `0W9G3ZX` | Drainage of Peritoneal Cavity, Percutaneous Approach, Diagnostic |
| 8 | 2142-04-01 | ICD-10 | `0W9G3ZX` | Drainage of Peritoneal Cavity, Percutaneous Approach, Diagnostic |


## 8. Critical Findings (Charted Events)

_No critical chart events detected._

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2142-03-25 22:22:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2142-03-25 22:22:00 | Transfer | → Emergency Department (ED) |
| 2142-03-26 06:08:00 | Admission | Admitted from TRANSFER FROM HOSPITAL (URGENT) |
| 2142-03-26 08:08:00 | ED Departure | Left Emergency Dept. |
| 2142-04-11 21:00:00 | Discharge | To HOME HEALTH CARE |

## 10. Missing / Ambiguous Data

- No ICU stay — patient managed on floor/step-down only.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
