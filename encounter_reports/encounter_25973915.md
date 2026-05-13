# Encounter Report — HADM 25973915

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 25973915 |
| Subject ID | 10018081 |
| Patient Sex | M |
| Patient Anchor Age (at anchor year) | 79 |
| Anchor Year | 2133 |
| Admission Time | 2134-09-06 15:57:00 |
| Discharge Time | 2134-09-18 15:50:00 |
| Admission Type | EW EMER. |
| Admission Location | EMERGENCY ROOM |
| Discharge Location | CHRONIC/LONG TERM ACUTE CARE |
| Insurance | Medicare |
| Language | ENGLISH |
| Marital Status | MARRIED |
| Race/Ethnicity | WHITE |
| ED Registration | 2134-09-05 16:14:00 |
| ED Departure | 2134-09-06 16:49:00 |
| In-Hospital Mortality | No |
| Date of Death (overall) | 2134-10-28 |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| APR | 194 | HEART FAILURE | 3.0 | 3.0 |
| HCFA | 292 | HEART FAILURE & SHOCK W CC | N/A | N/A |

### Primary Diagnosis (seq_num = 1)

- **ICD-9 42833**: Acute on chronic diastolic heart failure

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2134-09-06 15:57:55 | N/A | SURG |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-9 `42833`: Acute on chronic diastolic heart failure
- (seq 2) ICD-9 `4271`: Paroxysmal ventricular tachycardia
- (seq 3) ICD-9 `2760`: Hyperosmolality and/or hypernatremia
- (seq 4) ICD-9 `5990`: Urinary tract infection, site not specified
- (seq 5) ICD-9 `2930`: Delirium due to conditions classified elsewhere

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-9 | `42833` | Acute on chronic diastolic heart failure |
| 2 | ICD-9 | `4271` | Paroxysmal ventricular tachycardia |
| 3 | ICD-9 | `2760` | Hyperosmolality and/or hypernatremia |
| 4 | ICD-9 | `5990` | Urinary tract infection, site not specified |
| 5 | ICD-9 | `2930` | Delirium due to conditions classified elsewhere |
| 6 | ICD-9 | `4280` | Congestive heart failure, unspecified |
| 7 | ICD-9 | `41401` | Coronary atherosclerosis of native coronary artery |
| 8 | ICD-9 | `42731` | Atrial fibrillation |
| 9 | ICD-9 | `V5861` | Long-term (current) use of anticoagulants |
| 10 | ICD-9 | `V4572` | Acquired absence of intestine (large) (small) |
| 11 | ICD-9 | `4380` | Late effects of cerebrovascular disease, cognitive deficits |
| 12 | ICD-9 | `2859` | Anemia, unspecified |
| 13 | ICD-9 | `V1582` | Personal history of tobacco use |
| 14 | ICD-9 | `78451` | Dysarthria |
| 15 | ICD-9 | `4240` | Mitral valve disorders |
| 16 | ICD-9 | `2724` | Other and unspecified hyperlipidemia |

## 5. ICU Stays

_No ICU stay recorded for this admission._

## 6. Escalation / Severity Indicators

_No escalation indicators detected from ICD codes or ICU procedure events._

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2134-09-07 | ICD-9 | `9915` | Parenteral infusion of concentrated nutritional substances |


## 8. Critical Findings (Charted Events)

_No critical chart events detected._

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2134-09-05 16:14:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2134-09-05 16:14:00 | Transfer | → Emergency Department (ED) |
| 2134-09-06 15:57:00 | Admission | Admitted from EMERGENCY ROOM (EW EMER.) |
| 2134-09-06 16:22:59 | Transfer | → Discharge Lounge (transfer) |
| 2134-09-06 16:24:03 | Transfer | → Medicine (transfer) |
| 2134-09-06 16:49:00 | ED Departure | Left Emergency Dept. |
| 2134-09-09 17:36:28 | Transfer | → Medicine (transfer) |
| 2134-09-15 17:32:25 | Transfer | → Medicine (transfer) |
| 2134-09-18 15:50:00 | Discharge | To CHRONIC/LONG TERM ACUTE CARE |

## 10. Missing / Ambiguous Data

- No ICU stay — patient managed on floor/step-down only.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
