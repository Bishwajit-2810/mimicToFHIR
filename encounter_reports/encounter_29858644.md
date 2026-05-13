# Encounter Report — HADM 29858644

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 29858644 |
| Subject ID | 10023117 |
| Patient Sex | M |
| Patient Anchor Age (at anchor year) | 53 |
| Anchor Year | 2170 |
| Admission Time | 2173-04-16 22:15:00 |
| Discharge Time | 2173-04-20 16:40:00 |
| Admission Type | EW EMER. |
| Admission Location | EMERGENCY ROOM |
| Discharge Location | HOME |
| Insurance | Medicare |
| Language | ENGLISH |
| Marital Status | WIDOWED |
| Race/Ethnicity | WHITE |
| ED Registration | 2173-04-16 17:00:00 |
| ED Departure | 2173-04-16 23:18:00 |
| In-Hospital Mortality | No |
| Date of Death (overall) | 2175-07-20 |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| APR | 194 | HEART FAILURE | 2.0 | 1.0 |
| HCFA | 292 | HEART FAILURE & SHOCK W CC | N/A | N/A |

### Primary Diagnosis (seq_num = 1)

- **ICD-9 42823**: Acute on chronic systolic heart failure

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2173-04-16 22:16:23 | N/A | CMED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-9 `42823`: Acute on chronic systolic heart failure
- (seq 2) ICD-9 `5849`: Acute kidney failure, unspecified
- (seq 3) ICD-9 `29530`: Paranoid type schizophrenia, unspecified
- (seq 4) ICD-9 `4280`: Congestive heart failure, unspecified
- (seq 5) ICD-9 `30000`: Anxiety state, unspecified

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-9 | `42823` | Acute on chronic systolic heart failure |
| 2 | ICD-9 | `5849` | Acute kidney failure, unspecified |
| 3 | ICD-9 | `29530` | Paranoid type schizophrenia, unspecified |
| 4 | ICD-9 | `4280` | Congestive heart failure, unspecified |
| 5 | ICD-9 | `30000` | Anxiety state, unspecified |
| 6 | ICD-9 | `4148` | Other specified forms of chronic ischemic heart disease |
| 7 | ICD-9 | `V5866` | Long-term (current) use of aspirin |
| 8 | ICD-9 | `40390` | Hypertensive chronic kidney disease, unspecified, with chronic kidney disease stage I through stage IV, or unspecified |
| 9 | ICD-9 | `5859` | Chronic kidney disease, unspecified |
| 10 | ICD-9 | `V4501` | Cardiac pacemaker in situ |
| 11 | ICD-9 | `7852` | Undiagnosed cardiac murmurs |

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
| 2173-04-16 17:00:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2173-04-16 17:00:00 | Transfer | → Emergency Department (ED) |
| 2173-04-16 22:15:00 | Admission | Admitted from EMERGENCY ROOM (EW EMER.) |
| 2173-04-16 23:18:00 | ED Departure | Left Emergency Dept. |
| 2173-04-20 16:40:00 | Discharge | To HOME |

## 10. Missing / Ambiguous Data

- No procedure ICD codes — procedures may not have been coded or were minor.
- No ICU stay — patient managed on floor/step-down only.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
