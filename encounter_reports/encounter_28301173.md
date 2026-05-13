# Encounter Report — HADM 28301173

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 28301173 |
| Subject ID | 10002930 |
| Patient Sex | F |
| Patient Anchor Age (at anchor year) | 48 |
| Anchor Year | 2193 |
| Admission Time | 2197-04-08 19:37:00 |
| Discharge Time | 2197-04-15 12:01:00 |
| Admission Type | URGENT |
| Admission Location | INTERNAL TRANSFER TO OR FROM PSYCH |
| Discharge Location | HOME |
| Insurance | Medicare |
| Language | ENGLISH |
| Marital Status | SINGLE |
| Race/Ethnicity | BLACK/AFRICAN AMERICAN |
| ED Registration | N/A |
| ED Departure | N/A |
| In-Hospital Mortality | No |
| Date of Death (overall) | 2201-12-24 |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| HCFA | 885 | PSYCHOSES | N/A | N/A |
| APR | 751 | MAJOR DEPRESSIVE DISORDERS & OTHER/UNSPECIFIED PSYCHOSES | 1.0 | 1.0 |

### Primary Diagnosis (seq_num = 1)

- **ICD-9 29633**: Major depressive affective disorder, recurrent episode, severe, without mention of psychotic behavior

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2197-04-08 19:38:31 | N/A | PSYCH |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-9 `29633`: Major depressive affective disorder, recurrent episode, severe, without mention of psychotic behavior
- (seq 2) ICD-9 `V6284`: Suicidal ideation
- (seq 3) ICD-9 `29284`: Drug-induced mood disorder
- (seq 4) ICD-9 `07070`: Unspecified viral hepatitis C without hepatic coma
- (seq 5) ICD-9 `V08`: Asymptomatic human immunodeficiency virus [HIV] infection status

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-9 | `29633` | Major depressive affective disorder, recurrent episode, severe, without mention of psychotic behavior |
| 2 | ICD-9 | `V6284` | Suicidal ideation |
| 3 | ICD-9 | `29284` | Drug-induced mood disorder |
| 4 | ICD-9 | `07070` | Unspecified viral hepatitis C without hepatic coma |
| 5 | ICD-9 | `V08` | Asymptomatic human immunodeficiency virus [HIV] infection status |
| 6 | ICD-9 | `V1552` | Personal history of traumatic brain injury |
| 7 | ICD-9 | `6253` | Dysmenorrhea |
| 8 | ICD-9 | `30500` | Alcohol abuse, unspecified |
| 9 | ICD-9 | `30560` | Cocaine abuse, unspecified |
| 10 | ICD-9 | `30553` | Opioid abuse, in remission |

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
| 2197-04-08 19:37:00 | Admission | Admitted from INTERNAL TRANSFER TO OR FROM PSYCH (URGENT) |
| 2197-04-15 12:01:00 | Discharge | To HOME |

## 10. Missing / Ambiguous Data

- No ED registration time — admission may not have gone through ED.
- No procedure ICD codes — procedures may not have been coded or were minor.
- No ICU stay — patient managed on floor/step-down only.

## 11. Manual Review Recommendation

**This encounter is flagged for manual review:**

- Urgent/Emergency admission but no clear escalation indicator found.
