# Encounter Report — HADM 27494880

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 27494880 |
| Subject ID | 10014354 |
| Patient Sex | M |
| Patient Anchor Age (at anchor year) | 60 |
| Anchor Year | 2146 |
| Admission Time | 2147-06-04 00:42:00 |
| Discharge Time | 2147-06-04 15:00:00 |
| Admission Type | EU OBSERVATION |
| Admission Location | EMERGENCY ROOM |
| Discharge Location | N/A |
| Insurance | Other |
| Language | ENGLISH |
| Marital Status | SINGLE |
| Race/Ethnicity | WHITE |
| ED Registration | 2147-06-03 22:39:00 |
| ED Departure | 2147-06-04 09:54:00 |
| In-Hospital Mortality | No |
| Date of Death (overall) | N/A |

## 2. Hospital Visit Reason

### Primary Diagnosis (seq_num = 1)

- **ICD-10 R0789**: Other chest pain

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2147-06-04 00:45:19 | N/A | CMED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-10 `R0789`: Other chest pain
- (seq 2) ICD-10 `I2510`: Atherosclerotic heart disease of native coronary artery without angina pectoris
- (seq 3) ICD-10 `I10`: Essential (primary) hypertension
- (seq 4) ICD-10 `Z955`: Presence of coronary angioplasty implant and graft
- (seq 5) ICD-10 `Z7902`: Long term (current) use of antithrombotics/antiplatelets

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-10 | `R0789` | Other chest pain |
| 2 | ICD-10 | `I2510` | Atherosclerotic heart disease of native coronary artery without angina pectoris |
| 3 | ICD-10 | `I10` | Essential (primary) hypertension |
| 4 | ICD-10 | `Z955` | Presence of coronary angioplasty implant and graft |
| 5 | ICD-10 | `Z7902` | Long term (current) use of antithrombotics/antiplatelets |
| 6 | ICD-10 | `E785` | Hyperlipidemia, unspecified |
| 7 | ICD-10 | `C9110` | Chronic lymphocytic leukemia of B-cell type not having achieved remission |
| 8 | ICD-10 | `E119` | Type 2 diabetes mellitus without complications |
| 9 | ICD-10 | `Z794` | Long term (current) use of insulin |
| 10 | ICD-10 | `I4891` | Unspecified atrial fibrillation |
| 11 | ICD-10 | `E039` | Hypothyroidism, unspecified |
| 12 | ICD-10 | `F329` | Major depressive disorder, single episode, unspecified |
| 13 | ICD-10 | `M7071` | Other bursitis of hip, right hip |
| 14 | ICD-10 | `F0390` | Unspecified dementia without behavioral disturbance |
| 15 | ICD-10 | `G4733` | Obstructive sleep apnea (adult) (pediatric) |
| 16 | ICD-10 | `Z8673` | Personal history of transient ischemic attack (TIA), and cerebral infarction without residual deficits |
| 17 | ICD-10 | `Z950` | Presence of cardiac pacemaker |

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
| 2147-06-03 22:39:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2147-06-03 22:39:00 | Transfer | → Emergency Department (ED) |
| 2147-06-04 00:42:00 | Admission | Admitted from EMERGENCY ROOM (EU OBSERVATION) |
| 2147-06-04 01:07:14 | Transfer | → Discharge Lounge (transfer) |
| 2147-06-04 09:00:09 | Transfer | → Medicine (transfer) |
| 2147-06-04 09:54:00 | ED Departure | Left Emergency Dept. |
| 2147-06-04 15:00:00 | Discharge | To N/A |

## 10. Missing / Ambiguous Data

- Discharge location not recorded.
- No procedure ICD codes — procedures may not have been coded or were minor.
- No ICU stay — patient managed on floor/step-down only.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
