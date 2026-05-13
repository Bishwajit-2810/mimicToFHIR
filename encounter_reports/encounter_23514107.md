# Encounter Report — HADM 23514107

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 23514107 |
| Subject ID | 10005866 |
| Patient Sex | M |
| Patient Anchor Age (at anchor year) | 57 |
| Anchor Year | 2146 |
| Admission Time | 2149-06-20 19:27:00 |
| Discharge Time | 2149-06-25 15:55:00 |
| Admission Type | OBSERVATION ADMIT |
| Admission Location | EMERGENCY ROOM |
| Discharge Location | HOME |
| Insurance | Medicaid |
| Language | ENGLISH |
| Marital Status | SINGLE |
| Race/Ethnicity | PORTUGUESE |
| ED Registration | 2149-06-20 10:20:00 |
| ED Departure | 2149-06-20 20:59:00 |
| In-Hospital Mortality | No |
| Date of Death (overall) | 2149-11-21 |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| HCFA | 388 | G.I. OBSTRUCTION W MCC | N/A | N/A |
| APR | 247 | INTESTINAL OBSTRUCTION | 4.0 | 3.0 |

### Primary Diagnosis (seq_num = 1)

- **ICD-10 K565**: Intestinal adhesions [bands] with obstruction (postinfection)

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2149-06-20 19:27:45 | N/A | SURG |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-10 `K565`: Intestinal adhesions [bands] with obstruction (postinfection)
- (seq 2) ICD-10 `K7031`: Alcoholic cirrhosis of liver with ascites
- (seq 3) ICD-10 `I8510`: Secondary esophageal varices without bleeding
- (seq 4) ICD-10 `K766`: Portal hypertension
- (seq 5) ICD-10 `F17210`: Nicotine dependence, cigarettes, uncomplicated

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-10 | `K565` | Intestinal adhesions [bands] with obstruction (postinfection) |
| 2 | ICD-10 | `K7031` | Alcoholic cirrhosis of liver with ascites |
| 3 | ICD-10 | `I8510` | Secondary esophageal varices without bleeding |
| 4 | ICD-10 | `K766` | Portal hypertension |
| 5 | ICD-10 | `F17210` | Nicotine dependence, cigarettes, uncomplicated |
| 6 | ICD-10 | `Z6823` | Body mass index (BMI) 23.0-23.9, adult |
| 7 | ICD-10 | `B1920` | Unspecified viral hepatitis C without hepatic coma |
| 8 | ICD-10 | `I81` | Portal vein thrombosis |
| 9 | ICD-10 | `E43` | Unspecified severe protein-calorie malnutrition |

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
| 2149-06-20 10:20:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2149-06-20 10:20:00 | Transfer | → Emergency Department (ED) |
| 2149-06-20 19:27:00 | Admission | Admitted from EMERGENCY ROOM (OBSERVATION ADMIT) |
| 2149-06-20 20:59:00 | ED Departure | Left Emergency Dept. |
| 2149-06-25 15:55:00 | Discharge | To HOME |

## 10. Missing / Ambiguous Data

- No procedure ICD codes — procedures may not have been coded or were minor.
- No ICU stay — patient managed on floor/step-down only.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
