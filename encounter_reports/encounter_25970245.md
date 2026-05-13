# Encounter Report — HADM 25970245

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 25970245 |
| Subject ID | 10004235 |
| Patient Sex | M |
| Patient Anchor Age (at anchor year) | 47 |
| Anchor Year | 2196 |
| Admission Time | 2196-06-14 08:30:00 |
| Discharge Time | 2196-06-19 14:54:00 |
| Admission Type | SURGICAL SAME DAY ADMISSION |
| Admission Location | PHYSICIAN REFERRAL |
| Discharge Location | HOME HEALTH CARE |
| Insurance | Medicaid |
| Language | ENGLISH |
| Marital Status | SINGLE |
| Race/Ethnicity | BLACK/CAPE VERDEAN |
| ED Registration | N/A |
| ED Departure | N/A |
| In-Hospital Mortality | No |
| Date of Death (overall) | N/A |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| APR | 260 | MAJOR PANCREAS, LIVER & SHUNT PROCEDURES | 3.0 | 2.0 |
| HCFA | 406 | PANCREAS, LIVER & SHUNT PROCEDURES W CC | N/A | N/A |

### Primary Diagnosis (seq_num = 1)

- **ICD-9 1560**: Malignant neoplasm of gallbladder

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2196-06-14 07:02:15 | N/A | SURG |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-9 `1560`: Malignant neoplasm of gallbladder
- (seq 2) ICD-9 `1978`: Secondary malignant neoplasm of other digestive organs and spleen
- (seq 3) ICD-9 `27800`: Obesity, unspecified
- (seq 4) ICD-9 `42731`: Atrial fibrillation
- (seq 5) ICD-9 `57512`: Acute and chronic cholecystitis

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-9 | `1560` | Malignant neoplasm of gallbladder |
| 2 | ICD-9 | `1978` | Secondary malignant neoplasm of other digestive organs and spleen |
| 3 | ICD-9 | `27800` | Obesity, unspecified |
| 4 | ICD-9 | `42731` | Atrial fibrillation |
| 5 | ICD-9 | `57512` | Acute and chronic cholecystitis |
| 6 | ICD-9 | `2749` | Gout, unspecified |
| 7 | ICD-9 | `42789` | Other specified cardiac dysrhythmias |
| 8 | ICD-9 | `4019` | Unspecified essential hypertension |
| 9 | ICD-9 | `V5861` | Long-term (current) use of anticoagulants |
| 10 | ICD-9 | `V8535` | Body Mass Index 35.0-35.9, adult |

## 5. ICU Stays

_No ICU stay recorded for this admission._

## 6. Escalation / Severity Indicators

_No escalation indicators detected from ICD codes or ICU procedure events._

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2196-06-14 | ICD-9 | `5123` | Laparoscopic cholecystectomy |
| 2 | 2196-06-14 | ICD-9 | `5022` | Partial hepatectomy |
| 3 | 2196-06-14 | ICD-9 | `5169` | Excision of other bile duct |
| 4 | 2196-06-14 | ICD-9 | `5137` | Anastomosis of hepatic duct to gastrointestinal tract |
| 5 | 2196-06-14 | ICD-9 | `4029` | Simple excision of other lymphatic structure |
| 6 | 2196-06-14 | ICD-9 | `1742` | Laparoscopic robotic assisted procedure |


## 8. Critical Findings (Charted Events)

_No critical chart events detected._

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2196-06-14 08:30:00 | Admission | Admitted from PHYSICIAN REFERRAL (SURGICAL SAME DAY ADMISSION) |
| 2196-06-14 22:14:50 | Transfer | → PACU (transfer) |
| 2196-06-15 00:22:18 | Transfer | → Transplant (transfer) |
| 2196-06-15 17:03:11 | Transfer | → Transplant (transfer) |
| 2196-06-19 14:54:00 | Discharge | To HOME HEALTH CARE |

## 10. Missing / Ambiguous Data

- No ED registration time — admission may not have gone through ED.
- No ICU stay — patient managed on floor/step-down only.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
