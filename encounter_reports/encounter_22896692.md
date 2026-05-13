# Encounter Report — HADM 22896692

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 22896692 |
| Subject ID | 10012853 |
| Patient Sex | F |
| Patient Anchor Age (at anchor year) | 91 |
| Anchor Year | 2175 |
| Admission Time | 2176-08-11 15:17:00 |
| Discharge Time | 2176-08-11 17:35:00 |
| Admission Type | EU OBSERVATION |
| Admission Location | EMERGENCY ROOM |
| Discharge Location | N/A |
| Insurance | Medicare |
| Language | ENGLISH |
| Marital Status | WIDOWED |
| Race/Ethnicity | BLACK/AFRICAN AMERICAN |
| ED Registration | 2176-08-11 08:36:00 |
| ED Departure | 2176-08-11 17:35:00 |
| In-Hospital Mortality | No |
| Date of Death (overall) | N/A |

## 2. Hospital Visit Reason

### Primary Diagnosis (seq_num = 1)

- **ICD-10 R319**: Hematuria, unspecified

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2176-08-11 15:17:55 | N/A | MED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-10 `R319`: Hematuria, unspecified
- (seq 2) ICD-10 `N390`: Urinary tract infection, site not specified
- (seq 3) ICD-10 `I4891`: Unspecified atrial fibrillation
- (seq 4) ICD-10 `Z7901`: Long term (current) use of anticoagulants
- (seq 5) ICD-10 `N319`: Neuromuscular dysfunction of bladder, unspecified

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-10 | `R319` | Hematuria, unspecified |
| 2 | ICD-10 | `N390` | Urinary tract infection, site not specified |
| 3 | ICD-10 | `I4891` | Unspecified atrial fibrillation |
| 4 | ICD-10 | `Z7901` | Long term (current) use of anticoagulants |
| 5 | ICD-10 | `N319` | Neuromuscular dysfunction of bladder, unspecified |
| 6 | ICD-10 | `I129` | Hypertensive chronic kidney disease with stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease |
| 7 | ICD-10 | `N189` | Chronic kidney disease, unspecified |
| 8 | ICD-10 | `E785` | Hyperlipidemia, unspecified |
| 9 | ICD-10 | `Z86711` | Personal history of pulmonary embolism |
| 10 | ICD-10 | `Z8673` | Personal history of transient ischemic attack (TIA), and cerebral infarction without residual deficits |
| 11 | ICD-10 | `F17210` | Nicotine dependence, cigarettes, uncomplicated |

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
| 2176-08-11 08:36:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2176-08-11 08:36:00 | Transfer | → Emergency Department (ED) |
| 2176-08-11 15:17:00 | Admission | Admitted from EMERGENCY ROOM (EU OBSERVATION) |
| 2176-08-11 17:35:00 | Discharge | To N/A |
| 2176-08-11 17:35:00 | ED Departure | Left Emergency Dept. |

## 10. Missing / Ambiguous Data

- Discharge location not recorded.
- No procedure ICD codes — procedures may not have been coded or were minor.
- No ICU stay — patient managed on floor/step-down only.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
