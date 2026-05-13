# Encounter Report — HADM 27672872

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 27672872 |
| Subject ID | 10017492 |
| Patient Sex | M |
| Patient Anchor Age (at anchor year) | 84 |
| Anchor Year | 2114 |
| Admission Time | 2114-03-19 20:05:00 |
| Discharge Time | 2114-04-02 18:30:00 |
| Admission Type | EW EMER. |
| Admission Location | EMERGENCY ROOM |
| Discharge Location | HOME HEALTH CARE |
| Insurance | Other |
| Language | ? |
| Marital Status | SINGLE |
| Race/Ethnicity | PATIENT DECLINED TO ANSWER |
| ED Registration | 2114-03-19 15:57:00 |
| ED Departure | 2114-03-19 21:38:00 |
| In-Hospital Mortality | No |
| Date of Death (overall) | 2116-07-05 |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| APR | 45 | CVA & PRECEREBRAL OCCLUSION W INFARCT | 2.0 | 2.0 |
| HCFA | 65 | INTRACRANIAL HEMORRHAGE OR CEREBRAL INFARCTION W CC | N/A | N/A |

### Primary Diagnosis (seq_num = 1)

- **ICD-9 43491**: Cerebral artery occlusion, unspecified with cerebral infarction

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2114-03-19 20:06:36 | N/A | NMED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-9 `43491`: Cerebral artery occlusion, unspecified with cerebral infarction
- (seq 2) ICD-9 `5990`: Urinary tract infection, site not specified
- (seq 3) ICD-9 `78830`: Urinary incontinence, unspecified
- (seq 4) ICD-9 `2859`: Anemia, unspecified
- (seq 5) ICD-9 `4019`: Unspecified essential hypertension

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-9 | `43491` | Cerebral artery occlusion, unspecified with cerebral infarction |
| 2 | ICD-9 | `5990` | Urinary tract infection, site not specified |
| 3 | ICD-9 | `78830` | Urinary incontinence, unspecified |
| 4 | ICD-9 | `2859` | Anemia, unspecified |
| 5 | ICD-9 | `4019` | Unspecified essential hypertension |
| 6 | ICD-9 | `7843` | Aphasia |
| 7 | ICD-9 | `43310` | Occlusion and stenosis of carotid artery without mention of cerebral infarction |
| 8 | ICD-9 | `78469` | Other symbolic dysfunction |
| 9 | ICD-9 | `2989` | Unspecified psychosis |

## 5. ICU Stays

_No ICU stay recorded for this admission._

## 6. Escalation / Severity Indicators

_No escalation indicators detected from ICD codes or ICU procedure events._

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2114-03-23 | ICD-9 | `0331` | Spinal tap |


## 8. Critical Findings (Charted Events)

_No critical chart events detected._

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2114-03-19 15:57:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2114-03-19 15:57:00 | Transfer | → Emergency Department (ED) |
| 2114-03-19 20:05:00 | Admission | Admitted from EMERGENCY ROOM (EW EMER.) |
| 2114-03-19 21:38:00 | ED Departure | Left Emergency Dept. |
| 2114-03-20 16:28:20 | Transfer | → Neurology (transfer) |
| 2114-03-21 12:08:23 | Transfer | → Discharge Lounge (transfer) |
| 2114-03-21 13:39:04 | Transfer | → Neurology (transfer) |
| 2114-04-02 18:30:00 | Discharge | To HOME HEALTH CARE |

## 10. Missing / Ambiguous Data

- No ICU stay — patient managed on floor/step-down only.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
