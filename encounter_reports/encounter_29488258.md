# Encounter Report — HADM 29488258

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 29488258 |
| Subject ID | 10039708 |
| Patient Sex | F |
| Patient Anchor Age (at anchor year) | 46 |
| Anchor Year | 2138 |
| Admission Time | 2144-01-19 12:07:00 |
| Discharge Time | 2144-01-21 21:20:00 |
| Admission Type | OBSERVATION ADMIT |
| Admission Location | WALK-IN/SELF REFERRAL |
| Discharge Location | HOME |
| Insurance | Other |
| Language | ENGLISH |
| Marital Status | SINGLE |
| Race/Ethnicity | BLACK/AFRICAN AMERICAN |
| ED Registration | 2144-01-18 11:53:00 |
| ED Departure | 2144-01-19 13:59:00 |
| In-Hospital Mortality | No |
| Date of Death (overall) | N/A |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| APR | 279 | HEPATIC COMA & OTHER MAJOR ACUTE LIVER DISORDERS | 2.0 | 2.0 |
| HCFA | 441 | DISORDERS OF LIVER EXCEPT MALIG, CIRR, ALC HEPA W MCC | N/A | N/A |

### Primary Diagnosis (seq_num = 1)

- **ICD-10 K7290**: Hepatic failure, unspecified without coma

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2144-01-19 12:08:25 | N/A | MED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-10 `K7290`: Hepatic failure, unspecified without coma
- (seq 2) ICD-10 `N186`: End stage renal disease
- (seq 3) ICD-10 `F1019`: Alcohol abuse with unspecified alcohol-induced disorder
- (seq 4) ICD-10 `I8510`: Secondary esophageal varices without bleeding
- (seq 5) ICD-10 `K7030`: Alcoholic cirrhosis of liver without ascites

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-10 | `K7290` | Hepatic failure, unspecified without coma |
| 2 | ICD-10 | `N186` | End stage renal disease |
| 3 | ICD-10 | `F1019` | Alcohol abuse with unspecified alcohol-induced disorder |
| 4 | ICD-10 | `I8510` | Secondary esophageal varices without bleeding |
| 5 | ICD-10 | `K7030` | Alcoholic cirrhosis of liver without ascites |
| 6 | ICD-10 | `J45909` | Unspecified asthma, uncomplicated |
| 7 | ICD-10 | `T473X6A` | Underdosing of saline and osmotic laxatives, initial encounter |
| 8 | ICD-10 | `E039` | Hypothyroidism, unspecified |
| 9 | ICD-10 | `F17210` | Nicotine dependence, cigarettes, uncomplicated |
| 10 | ICD-10 | `D649` | Anemia, unspecified |
| 11 | ICD-10 | `Z992` | Dependence on renal dialysis |
| 12 | ICD-10 | `Z86718` | Personal history of other venous thrombosis and embolism |
| 13 | ICD-10 | `Z91128` | Patient's intentional underdosing of medication regimen for other reason |

## 5. ICU Stays

_No ICU stay recorded for this admission._

## 6. Escalation / Severity Indicators

The following critical conditions or interventions were detected:

- **Liver Failure** (ICD diagnosis)

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2144-01-20 | ICD-10 | `5A1D70Z` | Performance of Urinary Filtration, Intermittent, Less than 6 Hours Per Day |


## 8. Critical Findings (Charted Events)

_No critical chart events detected._

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2144-01-18 11:53:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2144-01-18 11:53:00 | Transfer | → Emergency Department (ED) |
| 2144-01-19 12:07:00 | Admission | Admitted from WALK-IN/SELF REFERRAL (OBSERVATION ADMIT) |
| 2144-01-19 13:59:00 | ED Departure | Left Emergency Dept. |
| 2144-01-19 21:14:49 | Transfer | → Transplant (transfer) |
| 2144-01-21 21:20:00 | Discharge | To HOME |

## 10. Missing / Ambiguous Data

- No ICU stay — patient managed on floor/step-down only.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
