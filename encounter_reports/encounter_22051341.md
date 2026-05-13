# Encounter Report — HADM 22051341

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 22051341 |
| Subject ID | 10007795 |
| Patient Sex | F |
| Patient Anchor Age (at anchor year) | 53 |
| Anchor Year | 2136 |
| Admission Time | 2136-09-22 20:51:00 |
| Discharge Time | 2136-09-24 14:20:00 |
| Admission Type | EW EMER. |
| Admission Location | EMERGENCY ROOM |
| Discharge Location | HOME |
| Insurance | Medicare |
| Language | ENGLISH |
| Marital Status | SINGLE |
| Race/Ethnicity | WHITE |
| ED Registration | 2136-09-22 17:07:00 |
| ED Departure | 2136-09-22 22:30:00 |
| In-Hospital Mortality | No |
| Date of Death (overall) | N/A |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| APR | 422 | HYPOVOLEMIA & RELATED ELECTROLYTE DISORDERS | 1.0 | 1.0 |
| HCFA | 641 | MISC DISORDERS OF NUTRITION,METABOLISM,FLUIDS/ELECTROLYTES W/O MCC | N/A | N/A |

### Primary Diagnosis (seq_num = 1)

- **ICD-9 27651**: Dehydration

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2136-09-22 20:52:49 | N/A | SURG |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-9 `27651`: Dehydration
- (seq 2) ICD-9 `24900`: Secondary diabetes mellitus without mention of complication, not stated as uncontrolled, or unspecified
- (seq 3) ICD-9 `33819`: Other acute pain
- (seq 4) ICD-9 `33829`: Other chronic pain
- (seq 5) ICD-9 `78909`: Abdominal pain, other specified site

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-9 | `27651` | Dehydration |
| 2 | ICD-9 | `24900` | Secondary diabetes mellitus without mention of complication, not stated as uncontrolled, or unspecified |
| 3 | ICD-9 | `33819` | Other acute pain |
| 4 | ICD-9 | `33829` | Other chronic pain |
| 5 | ICD-9 | `78909` | Abdominal pain, other specified site |
| 6 | ICD-9 | `V443` | Colostomy status |
| 7 | ICD-9 | `4019` | Unspecified essential hypertension |
| 8 | ICD-9 | `2720` | Pure hypercholesterolemia |
| 9 | ICD-9 | `311` | Depressive disorder, not elsewhere classified |
| 10 | ICD-9 | `30500` | Alcohol abuse, unspecified |
| 11 | ICD-9 | `V103` | Personal history of malignant neoplasm of breast |
| 12 | ICD-9 | `V8741` | Personal history of antineoplastic chemotherapy |

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
| 2136-09-22 17:07:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2136-09-22 17:07:00 | Transfer | → Emergency Department (ED) |
| 2136-09-22 20:51:00 | Admission | Admitted from EMERGENCY ROOM (EW EMER.) |
| 2136-09-22 22:30:00 | ED Departure | Left Emergency Dept. |
| 2136-09-24 14:20:00 | Discharge | To HOME |

## 10. Missing / Ambiguous Data

- No procedure ICD codes — procedures may not have been coded or were minor.
- No ICU stay — patient managed on floor/step-down only.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
