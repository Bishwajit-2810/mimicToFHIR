# Encounter Report — HADM 25797028

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 25797028 |
| Subject ID | 10002428 |
| Patient Sex | F |
| Patient Anchor Age (at anchor year) | 80 |
| Anchor Year | 2155 |
| Admission Time | 2155-07-14 19:15:00 |
| Discharge Time | 2155-07-15 18:37:00 |
| Admission Type | EU OBSERVATION |
| Admission Location | EMERGENCY ROOM |
| Discharge Location | N/A |
| Insurance | Medicare |
| Language | ENGLISH |
| Marital Status | WIDOWED |
| Race/Ethnicity | WHITE |
| ED Registration | 2155-07-14 16:58:00 |
| ED Departure | 2155-07-14 20:04:00 |
| In-Hospital Mortality | No |
| Date of Death (overall) | N/A |

## 2. Hospital Visit Reason

### Primary Diagnosis (seq_num = 1)

- **ICD-9 7802**: Syncope and collapse

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2155-07-14 19:16:22 | N/A | MED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-9 `7802`: Syncope and collapse
- (seq 2) ICD-9 `5990`: Urinary tract infection, site not specified
- (seq 3) ICD-9 `78720`: Dysphagia, unspecified
- (seq 4) ICD-9 `4241`: Aortic valve disorders
- (seq 5) ICD-9 `7102`: Sicca syndrome

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-9 | `7802` | Syncope and collapse |
| 2 | ICD-9 | `5990` | Urinary tract infection, site not specified |
| 3 | ICD-9 | `78720` | Dysphagia, unspecified |
| 4 | ICD-9 | `4241` | Aortic valve disorders |
| 5 | ICD-9 | `7102` | Sicca syndrome |
| 6 | ICD-9 | `2449` | Unspecified acquired hypothyroidism |
| 7 | ICD-9 | `4019` | Unspecified essential hypertension |
| 8 | ICD-9 | `2859` | Anemia, unspecified |

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
| 2155-07-14 16:58:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2155-07-14 16:58:00 | Transfer | → Emergency Department (ED) |
| 2155-07-14 19:15:00 | Admission | Admitted from EMERGENCY ROOM (EU OBSERVATION) |
| 2155-07-14 20:04:00 | ED Departure | Left Emergency Dept. |
| 2155-07-15 18:37:00 | Discharge | To N/A |

## 10. Missing / Ambiguous Data

- Discharge location not recorded.
- No procedure ICD codes — procedures may not have been coded or were minor.
- No ICU stay — patient managed on floor/step-down only.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
