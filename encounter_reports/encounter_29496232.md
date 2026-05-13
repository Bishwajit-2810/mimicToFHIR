# Encounter Report — HADM 29496232

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 29496232 |
| Subject ID | 10005348 |
| Patient Sex | M |
| Patient Anchor Age (at anchor year) | 76 |
| Anchor Year | 2128 |
| Admission Time | 2128-09-05 08:30:00 |
| Discharge Time | 2128-09-12 16:55:00 |
| Admission Type | ELECTIVE |
| Admission Location | PHYSICIAN REFERRAL |
| Discharge Location | HOME HEALTH CARE |
| Insurance | Other |
| Language | ENGLISH |
| Marital Status | MARRIED |
| Race/Ethnicity | WHITE |
| ED Registration | N/A |
| ED Departure | N/A |
| In-Hospital Mortality | No |
| Date of Death (overall) | N/A |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| APR | 120 | MAJOR RESPIRATORY & CHEST PROCEDURES | 3.0 | 2.0 |
| HCFA | 164 | MAJOR CHEST PROCEDURES W CC | N/A | N/A |

### Primary Diagnosis (seq_num = 1)

- **ICD-9 1625**: Malignant neoplasm of lower lobe, bronchus or lung

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2128-09-05 04:04:09 | N/A | TSURG |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-9 `1625`: Malignant neoplasm of lower lobe, bronchus or lung
- (seq 2) ICD-9 `42612`: Mobitz (type) II atrioventricular block
- (seq 3) ICD-9 `78321`: Loss of weight
- (seq 4) ICD-9 `V851`: Body Mass Index between 19-24, adult
- (seq 5) ICD-9 `41401`: Coronary atherosclerosis of native coronary artery

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-9 | `1625` | Malignant neoplasm of lower lobe, bronchus or lung |
| 2 | ICD-9 | `42612` | Mobitz (type) II atrioventricular block |
| 3 | ICD-9 | `78321` | Loss of weight |
| 4 | ICD-9 | `V851` | Body Mass Index between 19-24, adult |
| 5 | ICD-9 | `41401` | Coronary atherosclerosis of native coronary artery |
| 6 | ICD-9 | `V4582` | Percutaneous transluminal coronary angioplasty status |
| 7 | ICD-9 | `V1046` | Personal history of malignant neoplasm of prostate |
| 8 | ICD-9 | `4241` | Aortic valve disorders |
| 9 | ICD-9 | `4370` | Cerebral atherosclerosis |
| 10 | ICD-9 | `2859` | Anemia, unspecified |
| 11 | ICD-9 | `4019` | Unspecified essential hypertension |
| 12 | ICD-9 | `2724` | Other and unspecified hyperlipidemia |
| 13 | ICD-9 | `79022` | Impaired glucose tolerance test (oral) |
| 14 | ICD-9 | `30393` | Other and unspecified alcohol dependence, in remission |
| 15 | ICD-9 | `71594` | Osteoarthrosis, unspecified whether generalized or localized, hand |
| 16 | ICD-9 | `7210` | Cervical spondylosis without myelopathy |
| 17 | ICD-9 | `7213` | Lumbosacral spondylosis without myelopathy |
| 18 | ICD-9 | `311` | Depressive disorder, not elsewhere classified |
| 19 | ICD-9 | `3659` | Unspecified glaucoma |
| 20 | ICD-9 | `3569` | Unspecified hereditary and idiopathic peripheral neuropathy |
| 21 | ICD-9 | `78442` | Dysphonia |
| 22 | ICD-9 | `V1582` | Personal history of tobacco use |
| 23 | ICD-9 | `78820` | Retention of urine, unspecified |
| 24 | ICD-9 | `4580` | Orthostatic hypotension |
| 25 | ICD-9 | `42731` | Atrial fibrillation |
| 26 | ICD-9 | `2768` | Hypopotassemia |
| 27 | ICD-9 | `2753` | Disorders of phosphorus metabolism |
| 28 | ICD-9 | `2752` | Disorders of magnesium metabolism |

## 5. ICU Stays

_No ICU stay recorded for this admission._

## 6. Escalation / Severity Indicators

_No escalation indicators detected from ICD codes or ICU procedure events._

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2128-09-05 | ICD-9 | `3241` | Thoracoscopic lobectomy of lung |
| 2 | 2128-09-05 | ICD-9 | `403` | Regional lymph node excision |


## 8. Critical Findings (Charted Events)

_No critical chart events detected._

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2128-09-05 08:30:00 | Admission | Admitted from PHYSICIAN REFERRAL (ELECTIVE) |
| 2128-09-05 16:28:46 | Transfer | → Med/Surg (transfer) |
| 2128-09-12 16:55:00 | Discharge | To HOME HEALTH CARE |

## 10. Missing / Ambiguous Data

- No ED registration time — admission may not have gone through ED.
- No ICU stay — patient managed on floor/step-down only.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
