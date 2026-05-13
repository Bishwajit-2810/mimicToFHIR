# Encounter Report — HADM 23720373

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 23720373 |
| Subject ID | 10002930 |
| Patient Sex | F |
| Patient Anchor Age (at anchor year) | 48 |
| Anchor Year | 2193 |
| Admission Time | 2199-02-17 21:45:00 |
| Discharge Time | 2199-02-19 13:38:00 |
| Admission Type | EU OBSERVATION |
| Admission Location | EMERGENCY ROOM |
| Discharge Location | N/A |
| Insurance | Medicare |
| Language | ENGLISH |
| Marital Status | SINGLE |
| Race/Ethnicity | BLACK/AFRICAN AMERICAN |
| ED Registration | 2199-02-17 14:32:00 |
| ED Departure | 2199-02-19 13:38:00 |
| In-Hospital Mortality | No |
| Date of Death (overall) | 2201-12-24 |

## 2. Hospital Visit Reason

### Primary Diagnosis (seq_num = 1)

- **ICD-10 F29**: Unspecified psychosis not due to a substance or known physiological condition

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2199-02-17 21:46:40 | N/A | MED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-10 `F29`: Unspecified psychosis not due to a substance or known physiological condition
- (seq 2) ICD-10 `S0990XA`: Unspecified injury of head, initial encounter
- (seq 3) ICD-10 `F1910`: Other psychoactive substance abuse, uncomplicated
- (seq 4) ICD-10 `N390`: Urinary tract infection, site not specified
- (seq 5) ICD-10 `F1010`: Alcohol abuse, uncomplicated

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-10 | `F29` | Unspecified psychosis not due to a substance or known physiological condition |
| 2 | ICD-10 | `S0990XA` | Unspecified injury of head, initial encounter |
| 3 | ICD-10 | `F1910` | Other psychoactive substance abuse, uncomplicated |
| 4 | ICD-10 | `N390` | Urinary tract infection, site not specified |
| 5 | ICD-10 | `F1010` | Alcohol abuse, uncomplicated |
| 6 | ICD-10 | `F39` | Unspecified mood [affective] disorder |
| 7 | ICD-10 | `F17200` | Nicotine dependence, unspecified, uncomplicated |
| 8 | ICD-10 | `Z87820` | Personal history of traumatic brain injury |
| 9 | ICD-10 | `Z590` | Homelessness |
| 10 | ICD-10 | `Z21` | Asymptomatic human immunodeficiency virus [HIV] infection status |
| 11 | ICD-10 | `W19XXXA` | Unspecified fall, initial encounter |
| 12 | ICD-10 | `Y929` | Unspecified place or not applicable |

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
| 2199-02-17 14:32:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2199-02-17 14:32:00 | Transfer | → Emergency Department (ED) |
| 2199-02-17 21:45:00 | Admission | Admitted from EMERGENCY ROOM (EU OBSERVATION) |
| 2199-02-19 13:38:00 | Discharge | To N/A |
| 2199-02-19 13:38:00 | ED Departure | Left Emergency Dept. |

## 10. Missing / Ambiguous Data

- Discharge location not recorded.
- No procedure ICD codes — procedures may not have been coded or were minor.
- No ICU stay — patient managed on floor/step-down only.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
