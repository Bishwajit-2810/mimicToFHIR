# Encounter Report — HADM 27504040

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 27504040 |
| Subject ID | 10039708 |
| Patient Sex | F |
| Patient Anchor Age (at anchor year) | 46 |
| Anchor Year | 2138 |
| Admission Time | 2142-07-06 09:08:00 |
| Discharge Time | 2142-07-07 16:40:00 |
| Admission Type | EU OBSERVATION |
| Admission Location | PHYSICIAN REFERRAL |
| Discharge Location | N/A |
| Insurance | Other |
| Language | ENGLISH |
| Marital Status | SINGLE |
| Race/Ethnicity | BLACK/AFRICAN AMERICAN |
| ED Registration | 2142-07-06 07:21:00 |
| ED Departure | 2142-07-06 08:27:00 |
| In-Hospital Mortality | No |
| Date of Death (overall) | N/A |

## 2. Hospital Visit Reason

### Primary Diagnosis (seq_num = 1)

- **ICD-10 I120**: Hypertensive chronic kidney disease with stage 5 chronic kidney disease or end stage renal disease

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2142-07-06 09:09:11 | N/A | SURG |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-10 `I120`: Hypertensive chronic kidney disease with stage 5 chronic kidney disease or end stage renal disease
- (seq 2) ICD-10 `N186`: End stage renal disease
- (seq 3) ICD-10 `Z992`: Dependence on renal dialysis
- (seq 4) ICD-10 `K7030`: Alcoholic cirrhosis of liver without ascites
- (seq 5) ICD-10 `K7010`: Alcoholic hepatitis without ascites

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-10 | `I120` | Hypertensive chronic kidney disease with stage 5 chronic kidney disease or end stage renal disease |
| 2 | ICD-10 | `N186` | End stage renal disease |
| 3 | ICD-10 | `Z992` | Dependence on renal dialysis |
| 4 | ICD-10 | `K7030` | Alcoholic cirrhosis of liver without ascites |
| 5 | ICD-10 | `K7010` | Alcoholic hepatitis without ascites |
| 6 | ICD-10 | `K767` | Hepatorenal syndrome |
| 7 | ICD-10 | `J45909` | Unspecified asthma, uncomplicated |
| 8 | ICD-10 | `D631` | Anemia in chronic kidney disease |
| 9 | ICD-10 | `M109` | Gout, unspecified |
| 10 | ICD-10 | `K861` | Other chronic pancreatitis |
| 11 | ICD-10 | `Z86718` | Personal history of other venous thrombosis and embolism |
| 12 | ICD-10 | `E039` | Hypothyroidism, unspecified |
| 13 | ICD-10 | `F17210` | Nicotine dependence, cigarettes, uncomplicated |
| 14 | ICD-10 | `D696` | Thrombocytopenia, unspecified |

## 5. ICU Stays

_No ICU stay recorded for this admission._

## 6. Escalation / Severity Indicators

_No escalation indicators detected from ICD codes or ICU procedure events._

## 7. Procedures and Interventions

_No ICD-coded procedures recorded._


## 8. Critical Findings (Charted Events)

_No critical chart events detected._

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2142-07-06 07:21:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2142-07-06 07:21:00 | Transfer | → Emergency Department (ED) |
| 2142-07-06 08:27:00 | ED Departure | Left Emergency Dept. |
| 2142-07-06 09:08:00 | Admission | Admitted from PHYSICIAN REFERRAL (EU OBSERVATION) |
| 2142-07-07 16:40:00 | Discharge | To N/A |

## 10. Missing / Ambiguous Data

- Discharge location not recorded.
- No procedure ICD codes — procedures may not have been coded or were minor.
- No ICU stay — patient managed on floor/step-down only.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
