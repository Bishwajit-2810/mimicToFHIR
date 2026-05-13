# Encounter Report — HADM 26549334

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 26549334 |
| Subject ID | 10002428 |
| Patient Sex | F |
| Patient Anchor Age (at anchor year) | 80 |
| Anchor Year | 2155 |
| Admission Time | 2160-07-15 23:37:00 |
| Discharge Time | 2160-07-16 18:49:00 |
| Admission Type | EU OBSERVATION |
| Admission Location | EMERGENCY ROOM |
| Discharge Location | N/A |
| Insurance | Medicare |
| Language | ENGLISH |
| Marital Status | WIDOWED |
| Race/Ethnicity | WHITE |
| ED Registration | 2160-07-15 17:34:00 |
| ED Departure | 2160-07-16 18:49:00 |
| In-Hospital Mortality | No |
| Date of Death (overall) | N/A |

## 2. Hospital Visit Reason

### Primary Diagnosis (seq_num = 1)

- **ICD-10 S0990XA**: Unspecified injury of head, initial encounter

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2160-07-15 23:37:52 | N/A | MED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-10 `S0990XA`: Unspecified injury of head, initial encounter
- (seq 2) ICD-10 `S4992XA`: Unspecified injury of left shoulder and upper arm, initial encounter
- (seq 3) ICD-10 `S79912A`: Unspecified injury of left hip, initial encounter
- (seq 4) ICD-10 `W1839XA`: Other fall on same level, initial encounter
- (seq 5) ICD-10 `Z9181`: History of falling

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-10 | `S0990XA` | Unspecified injury of head, initial encounter |
| 2 | ICD-10 | `S4992XA` | Unspecified injury of left shoulder and upper arm, initial encounter |
| 3 | ICD-10 | `S79912A` | Unspecified injury of left hip, initial encounter |
| 4 | ICD-10 | `W1839XA` | Other fall on same level, initial encounter |
| 5 | ICD-10 | `Z9181` | History of falling |
| 6 | ICD-10 | `Y92129` | Unspecified place in nursing home as the place of occurrence of the external cause |
| 7 | ICD-10 | `M3500` | Sicca syndrome, unspecified |
| 8 | ICD-10 | `H53143` | Visual discomfort, bilateral |
| 9 | ICD-10 | `H04123` | Dry eye syndrome of bilateral lacrimal glands |
| 10 | ICD-10 | `H3530` | Unspecified macular degeneration |
| 11 | ICD-10 | `Z961` | Presence of intraocular lens |
| 12 | ICD-10 | `E039` | Hypothyroidism, unspecified |
| 13 | ICD-10 | `M4856XA` | Collapsed vertebra, not elsewhere classified, lumbar region, initial encounter for fracture |
| 14 | ICD-10 | `I10` | Essential (primary) hypertension |
| 15 | ICD-10 | `M5030` | Other cervical disc degeneration, unspecified cervical region |
| 16 | ICD-10 | `E049` | Nontoxic goiter, unspecified |

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
| 2160-07-15 17:34:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2160-07-15 17:34:00 | Transfer | → Emergency Department (ED) |
| 2160-07-15 23:37:00 | Admission | Admitted from EMERGENCY ROOM (EU OBSERVATION) |
| 2160-07-16 18:49:00 | Discharge | To N/A |
| 2160-07-16 18:49:00 | ED Departure | Left Emergency Dept. |

## 10. Missing / Ambiguous Data

- Discharge location not recorded.
- No procedure ICD codes — procedures may not have been coded or were minor.
- No ICU stay — patient managed on floor/step-down only.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
