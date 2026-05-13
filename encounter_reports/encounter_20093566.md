# Encounter Report — HADM 20093566

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 20093566 |
| Subject ID | 10039708 |
| Patient Sex | F |
| Patient Anchor Age (at anchor year) | 46 |
| Anchor Year | 2138 |
| Admission Time | 2143-09-26 18:24:00 |
| Discharge Time | 2143-09-30 20:00:00 |
| Admission Type | OBSERVATION ADMIT |
| Admission Location | CLINIC REFERRAL |
| Discharge Location | HOME HEALTH CARE |
| Insurance | Other |
| Language | ENGLISH |
| Marital Status | SINGLE |
| Race/Ethnicity | BLACK/AFRICAN AMERICAN |
| ED Registration | 2143-09-26 08:16:00 |
| ED Departure | 2143-09-26 19:52:00 |
| In-Hospital Mortality | No |
| Date of Death (overall) | N/A |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| APR | 280 | ALCOHOLIC LIVER DISEASE | 3.0 | 3.0 |
| HCFA | 432 | CIRRHOSIS & ALCOHOLIC HEPATITIS W MCC | N/A | N/A |

### Primary Diagnosis (seq_num = 1)

- **ICD-10 K7040**: Alcoholic hepatic failure without coma

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2143-09-26 18:25:09 | N/A | MED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-10 `K7040`: Alcoholic hepatic failure without coma
- (seq 2) ICD-10 `N186`: End stage renal disease
- (seq 3) ICD-10 `F10251`: Alcohol dependence with alcohol-induced psychotic disorder with hallucinations
- (seq 4) ICD-10 `F10239`: Alcohol dependence with withdrawal, unspecified
- (seq 5) ICD-10 `I8510`: Secondary esophageal varices without bleeding

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-10 | `K7040` | Alcoholic hepatic failure without coma |
| 2 | ICD-10 | `N186` | End stage renal disease |
| 3 | ICD-10 | `F10251` | Alcohol dependence with alcohol-induced psychotic disorder with hallucinations |
| 4 | ICD-10 | `F10239` | Alcohol dependence with withdrawal, unspecified |
| 5 | ICD-10 | `I8510` | Secondary esophageal varices without bleeding |
| 6 | ICD-10 | `I120` | Hypertensive chronic kidney disease with stage 5 chronic kidney disease or end stage renal disease |
| 7 | ICD-10 | `D62` | Acute posthemorrhagic anemia |
| 8 | ICD-10 | `K921` | Melena |
| 9 | ICD-10 | `E872` | Acidosis |
| 10 | ICD-10 | `K7030` | Alcoholic cirrhosis of liver without ascites |
| 11 | ICD-10 | `Z8711` | Personal history of peptic ulcer disease |
| 12 | ICD-10 | `Z992` | Dependence on renal dialysis |
| 13 | ICD-10 | `D638` | Anemia in other chronic diseases classified elsewhere |
| 14 | ICD-10 | `F17210` | Nicotine dependence, cigarettes, uncomplicated |
| 15 | ICD-10 | `J45909` | Unspecified asthma, uncomplicated |
| 16 | ICD-10 | `E039` | Hypothyroidism, unspecified |
| 17 | ICD-10 | `Z86718` | Personal history of other venous thrombosis and embolism |
| 18 | ICD-10 | `Z9884` | Bariatric surgery status |
| 19 | ICD-10 | `M109` | Gout, unspecified |
| 20 | ICD-10 | `S40022A` | Contusion of left upper arm, initial encounter |
| 21 | ICD-10 | `S40021A` | Contusion of right upper arm, initial encounter |
| 22 | ICD-10 | `S8012XA` | Contusion of left lower leg, initial encounter |
| 23 | ICD-10 | `S8011XA` | Contusion of right lower leg, initial encounter |
| 24 | ICD-10 | `S0003XA` | Contusion of scalp, initial encounter |
| 25 | ICD-10 | `S20222A` | Contusion of left back wall of thorax, initial encounter |
| 26 | ICD-10 | `S20221A` | Contusion of right back wall of thorax, initial encounter |
| 27 | ICD-10 | `W108XXA` | Fall (on) (from) other stairs and steps, initial encounter |
| 28 | ICD-10 | `Y92018` | Other place in single-family (private) house as the place of occurrence of the external cause |
| 29 | ICD-10 | `R740` | Nonspecific elevation of levels of transaminase and lactic acid dehydrogenase [LDH] |
| 30 | ICD-10 | `R748` | Abnormal levels of other serum enzymes |
| 31 | ICD-10 | `R600` | Localized edema |
| 32 | ICD-10 | `D696` | Thrombocytopenia, unspecified |

## 5. ICU Stays

_No ICU stay recorded for this admission._

## 6. Escalation / Severity Indicators

_No escalation indicators detected from ICD codes or ICU procedure events._

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2143-09-27 | ICD-10 | `5A1D70Z` | Performance of Urinary Filtration, Intermittent, Less than 6 Hours Per Day |


## 8. Critical Findings (Charted Events)

_No critical chart events detected._

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2143-09-26 08:16:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2143-09-26 08:16:00 | Transfer | → Emergency Department (ED) |
| 2143-09-26 18:24:00 | Admission | Admitted from CLINIC REFERRAL (OBSERVATION ADMIT) |
| 2143-09-26 19:52:00 | ED Departure | Left Emergency Dept. |
| 2143-09-30 20:00:00 | Discharge | To HOME HEALTH CARE |

## 10. Missing / Ambiguous Data

- No ICU stay — patient managed on floor/step-down only.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
