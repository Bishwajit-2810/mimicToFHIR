# Encounter Report — HADM 20192635

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 20192635 |
| Subject ID | 10037928 |
| Patient Sex | F |
| Patient Anchor Age (at anchor year) | 78 |
| Anchor Year | 2175 |
| Admission Time | 2177-09-04 12:05:00 |
| Discharge Time | 2177-09-07 16:10:00 |
| Admission Type | EW EMER. |
| Admission Location | EMERGENCY ROOM |
| Discharge Location | HOME HEALTH CARE |
| Insurance | Medicare |
| Language | ? |
| Marital Status | WIDOWED |
| Race/Ethnicity | HISPANIC/LATINO - CUBAN |
| ED Registration | 2177-09-04 06:29:00 |
| ED Departure | 2177-09-04 14:44:00 |
| In-Hospital Mortality | No |
| Date of Death (overall) | N/A |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| HCFA | 918 | POISONING & TOXIC EFFECTS OF DRUGS W/O MCC | N/A | N/A |
| APR | 812 | POISONING OF MEDICINAL AGENTS | 3.0 | 3.0 |

### Primary Diagnosis (seq_num = 1)

- **ICD-9 9623**: Poisoning by insulins and antidiabetic agents

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2177-09-04 12:06:40 | N/A | MED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-9 `9623`: Poisoning by insulins and antidiabetic agents
- (seq 2) ICD-9 `5849`: Acute kidney failure, unspecified
- (seq 3) ICD-9 `25080`: Diabetes with other specified manifestations, type II or unspecified type, not stated as uncontrolled
- (seq 4) ICD-9 `2724`: Other and unspecified hyperlipidemia
- (seq 5) ICD-9 `V1001`: Personal history of malignant neoplasm of tongue

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-9 | `9623` | Poisoning by insulins and antidiabetic agents |
| 2 | ICD-9 | `5849` | Acute kidney failure, unspecified |
| 3 | ICD-9 | `25080` | Diabetes with other specified manifestations, type II or unspecified type, not stated as uncontrolled |
| 4 | ICD-9 | `2724` | Other and unspecified hyperlipidemia |
| 5 | ICD-9 | `V1001` | Personal history of malignant neoplasm of tongue |
| 6 | ICD-9 | `78065` | Hypothermia not associated with low environmental temperature |
| 7 | ICD-9 | `311` | Depressive disorder, not elsewhere classified |
| 8 | ICD-9 | `30000` | Anxiety state, unspecified |
| 9 | ICD-9 | `2809` | Iron deficiency anemia, unspecified |
| 10 | ICD-9 | `53081` | Esophageal reflux |
| 11 | ICD-9 | `75249` | Other anomalies of cervix, vagina, and external female genitalia |
| 12 | ICD-9 | `78820` | Retention of urine, unspecified |
| 13 | ICD-9 | `5989` | Urethral stricture, unspecified |
| 14 | ICD-9 | `7919` | Other nonspecific findings on examination of urine |
| 15 | ICD-9 | `5859` | Chronic kidney disease, unspecified |
| 16 | ICD-9 | `40390` | Hypertensive chronic kidney disease, unspecified, with chronic kidney disease stage I through stage IV, or unspecified |
| 17 | ICD-9 | `E8580` | Accidental poisoning by hormones and synthetic substitutes |
| 18 | ICD-9 | `V5867` | Long-term (current) use of insulin |

## 5. ICU Stays

_No ICU stay recorded for this admission._

## 6. Escalation / Severity Indicators

The following critical conditions or interventions were detected:

- **Acute Kidney Injury** (ICD diagnosis)

## 7. Procedures and Interventions

_No ICD-coded procedures recorded._


## 8. Critical Findings (Charted Events)

_No critical chart events detected._

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2177-09-04 06:29:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2177-09-04 06:29:00 | Transfer | → Emergency Department (ED) |
| 2177-09-04 12:05:00 | Admission | Admitted from EMERGENCY ROOM (EW EMER.) |
| 2177-09-04 12:59:33 | Transfer | → Medicine (transfer) |
| 2177-09-04 14:44:00 | ED Departure | Left Emergency Dept. |
| 2177-09-07 16:10:00 | Discharge | To HOME HEALTH CARE |

## 10. Missing / Ambiguous Data

- No procedure ICD codes — procedures may not have been coded or were minor.
- No ICU stay — patient managed on floor/step-down only.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
