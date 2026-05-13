# Encounter Report — HADM 27488741

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 27488741 |
| Subject ID | 10027445 |
| Patient Sex | F |
| Patient Anchor Age (at anchor year) | 48 |
| Anchor Year | 2142 |
| Admission Time | 2145-12-08 19:47:00 |
| Discharge Time | 2145-12-19 14:36:00 |
| Admission Type | URGENT |
| Admission Location | TRANSFER FROM HOSPITAL |
| Discharge Location | HOME HEALTH CARE |
| Insurance | Other |
| Language | ENGLISH |
| Marital Status | WIDOWED |
| Race/Ethnicity | WHITE |
| ED Registration | N/A |
| ED Departure | N/A |
| In-Hospital Mortality | No |
| Date of Death (overall) | 2146-02-09 |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| APR | 194 | HEART FAILURE | 3.0 | 3.0 |
| HCFA | 291 | HEART FAILURE & SHOCK W MCC | N/A | N/A |

### Primary Diagnosis (seq_num = 1)

- **ICD-9 42833**: Acute on chronic diastolic heart failure

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2145-12-08 19:48:49 | N/A | CMED |
| 2145-12-08 20:39:42 | CMED | MED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-9 `42833`: Acute on chronic diastolic heart failure
- (seq 2) ICD-9 `34830`: Encephalopathy, unspecified
- (seq 3) ICD-9 `11289`: Other candidiasis of other specified sites
- (seq 4) ICD-9 `5168`: Other specified alveolar and parietoalveolar pneumonopathies
- (seq 5) ICD-9 `4168`: Other chronic pulmonary heart diseases

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-9 | `42833` | Acute on chronic diastolic heart failure |
| 2 | ICD-9 | `34830` | Encephalopathy, unspecified |
| 3 | ICD-9 | `11289` | Other candidiasis of other specified sites |
| 4 | ICD-9 | `5168` | Other specified alveolar and parietoalveolar pneumonopathies |
| 5 | ICD-9 | `4168` | Other chronic pulmonary heart diseases |
| 6 | ICD-9 | `5730` | Chronic passive congestion of liver |
| 7 | ICD-9 | `6822` | Cellulitis and abscess of trunk |
| 8 | ICD-9 | `V8542` | Body Mass Index 45.0-49.9, adult |
| 9 | ICD-9 | `41401` | Coronary atherosclerosis of native coronary artery |
| 10 | ICD-9 | `3940` | Mitral stenosis |
| 11 | ICD-9 | `4280` | Congestive heart failure, unspecified |
| 12 | ICD-9 | `412` | Old myocardial infarction |
| 13 | ICD-9 | `4439` | Peripheral vascular disease, unspecified |
| 14 | ICD-9 | `4019` | Unspecified essential hypertension |
| 15 | ICD-9 | `45981` | Venous (peripheral) insufficiency, unspecified |
| 16 | ICD-9 | `25000` | Diabetes mellitus without mention of complication, type II or unspecified type, not stated as uncontrolled |
| 17 | ICD-9 | `8449` | Sprains and strains of unspecified site of knee and leg |
| 18 | ICD-9 | `9168` | Other and unspecified superficial injury of hip, thigh, leg, and ankle, without mention of infection |
| 19 | ICD-9 | `E9289` | Unspecified accident |
| 20 | ICD-9 | `E8490` | Home accidents |
| 21 | ICD-9 | `2768` | Hypopotassemia |
| 22 | ICD-9 | `27800` | Obesity, unspecified |
| 23 | ICD-9 | `5533` | Diaphragmatic hernia without mention of obstruction or gangrene |
| 24 | ICD-9 | `53081` | Esophageal reflux |
| 25 | ICD-9 | `34690` | Migraine, unspecified, without mention of intractable migraine without mention of status migrainosus |
| 26 | ICD-9 | `3051` | Tobacco use disorder |
| 27 | ICD-9 | `311` | Depressive disorder, not elsewhere classified |
| 28 | ICD-9 | `30000` | Anxiety state, unspecified |
| 29 | ICD-9 | `33829` | Other chronic pain |
| 30 | ICD-9 | `V462` | Other dependence on machines, supplemental oxygen |
| 31 | ICD-9 | `V5867` | Long-term (current) use of insulin |
| 32 | ICD-9 | `V8801` | Acquired absence of both cervix and uterus |

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
| 2145-12-08 19:47:00 | Admission | Admitted from TRANSFER FROM HOSPITAL (URGENT) |
| 2145-12-08 20:39:17 | Transfer | → Med/Surg (transfer) |
| 2145-12-08 21:48:05 | Transfer | → Med/Surg (transfer) |
| 2145-12-09 14:04:50 | Transfer | → Med/Surg (transfer) |
| 2145-12-19 14:36:00 | Discharge | To HOME HEALTH CARE |

## 10. Missing / Ambiguous Data

- No ED registration time — admission may not have gone through ED.
- No procedure ICD codes — procedures may not have been coded or were minor.
- No ICU stay — patient managed on floor/step-down only.

## 11. Manual Review Recommendation

**This encounter is flagged for manual review:**

- Urgent/Emergency admission but no clear escalation indicator found.
