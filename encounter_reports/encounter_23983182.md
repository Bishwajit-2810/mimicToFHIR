# Encounter Report — HADM 23983182

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 23983182 |
| Subject ID | 10018081 |
| Patient Sex | M |
| Patient Anchor Age (at anchor year) | 79 |
| Anchor Year | 2133 |
| Admission Time | 2134-08-18 02:02:00 |
| Discharge Time | 2134-08-23 19:35:00 |
| Admission Type | URGENT |
| Admission Location | TRANSFER FROM HOSPITAL |
| Discharge Location | SKILLED NURSING FACILITY |
| Insurance | Medicare |
| Language | ENGLISH |
| Marital Status | MARRIED |
| Race/Ethnicity | WHITE |
| ED Registration | 2134-08-17 16:24:00 |
| ED Departure | 2134-08-18 03:15:00 |
| In-Hospital Mortality | No |
| Date of Death (overall) | 2134-10-28 |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| APR | 721 | POST-OPERATIVE, POST-TRAUMATIC, OTHER DEVICE INFECTIONS | 3.0 | 3.0 |
| HCFA | 862 | POSTOPERATIVE & POST-TRAUMATIC INFECTIONS W MCC | N/A | N/A |

### Primary Diagnosis (seq_num = 1)

- **ICD-9 99859**: Other postoperative infection

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2134-08-18 02:02:33 | N/A | SURG |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-9 `99859`: Other postoperative infection
- (seq 2) ICD-9 `56722`: Peritoneal abscess
- (seq 3) ICD-9 `5579`: Unspecified vascular insufficiency of intestine
- (seq 4) ICD-9 `56981`: Fistula of intestine, excluding rectum and anus
- (seq 5) ICD-9 `9986`: Persistent postoperative fistula

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-9 | `99859` | Other postoperative infection |
| 2 | ICD-9 | `56722` | Peritoneal abscess |
| 3 | ICD-9 | `5579` | Unspecified vascular insufficiency of intestine |
| 4 | ICD-9 | `56981` | Fistula of intestine, excluding rectum and anus |
| 5 | ICD-9 | `9986` | Persistent postoperative fistula |
| 6 | ICD-9 | `42842` | Chronic combined systolic and diastolic heart failure |
| 7 | ICD-9 | `41401` | Coronary atherosclerosis of native coronary artery |
| 8 | ICD-9 | `4280` | Congestive heart failure, unspecified |
| 9 | ICD-9 | `42731` | Atrial fibrillation |
| 10 | ICD-9 | `2724` | Other and unspecified hyperlipidemia |
| 11 | ICD-9 | `4019` | Unspecified essential hypertension |
| 12 | ICD-9 | `4240` | Mitral valve disorders |
| 13 | ICD-9 | `42769` | Other premature beats |
| 14 | ICD-9 | `29420` | Dementia, unspecified, without behavioral disturbance |
| 15 | ICD-9 | `2720` | Pure hypercholesterolemia |
| 16 | ICD-9 | `V1582` | Personal history of tobacco use |
| 17 | ICD-9 | `V5861` | Long-term (current) use of anticoagulants |
| 18 | ICD-9 | `V4365` | Knee joint replacement |
| 19 | ICD-9 | `E8798` | Other specified procedures as the cause of abnormal reaction of patient, or of later complication, without mention of misadventure at time of procedure |

## 5. ICU Stays

_No ICU stay recorded for this admission._

## 6. Escalation / Severity Indicators

_No escalation indicators detected from ICD codes or ICU procedure events._

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2134-08-18 | ICD-9 | `5491` | Percutaneous abdominal drainage |
| 2 | 2134-08-18 | ICD-9 | `9915` | Parenteral infusion of concentrated nutritional substances |


## 8. Critical Findings (Charted Events)

_No critical chart events detected._

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2134-08-17 16:24:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2134-08-17 16:24:00 | Transfer | → Emergency Department (ED) |
| 2134-08-18 02:02:00 | Admission | Admitted from TRANSFER FROM HOSPITAL (URGENT) |
| 2134-08-18 03:15:00 | ED Departure | Left Emergency Dept. |
| 2134-08-23 19:35:00 | Discharge | To SKILLED NURSING FACILITY |

## 10. Missing / Ambiguous Data

- No ICU stay — patient managed on floor/step-down only.

## 11. Manual Review Recommendation

**This encounter is flagged for manual review:**

- Urgent/Emergency admission but no clear escalation indicator found.
