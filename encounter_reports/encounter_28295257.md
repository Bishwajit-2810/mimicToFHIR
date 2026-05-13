# Encounter Report — HADM 28295257

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 28295257 |
| Subject ID | 10002428 |
| Patient Sex | F |
| Patient Anchor Age (at anchor year) | 80 |
| Anchor Year | 2155 |
| Admission Time | 2160-04-14 12:30:00 |
| Discharge Time | 2160-04-18 16:00:00 |
| Admission Type | OBSERVATION ADMIT |
| Admission Location | EMERGENCY ROOM |
| Discharge Location | SKILLED NURSING FACILITY |
| Insurance | Medicare |
| Language | ENGLISH |
| Marital Status | WIDOWED |
| Race/Ethnicity | WHITE |
| ED Registration | 2160-04-14 09:01:00 |
| ED Departure | 2160-04-14 14:28:00 |
| In-Hospital Mortality | No |
| Date of Death (overall) | N/A |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| APR | 253 | OTHER & UNSPECIFIED GASTROINTESTINAL HEMORRHAGE | 3.0 | 3.0 |
| HCFA | 377 | G.I. HEMORRHAGE W MCC | N/A | N/A |

### Primary Diagnosis (seq_num = 1)

- **ICD-10 K922**: Gastrointestinal hemorrhage, unspecified

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2160-04-14 12:31:23 | N/A | MED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-10 `K922`: Gastrointestinal hemorrhage, unspecified
- (seq 2) ICD-10 `E43`: Unspecified severe protein-calorie malnutrition
- (seq 3) ICD-10 `M8008XA`: Age-related osteoporosis with current pathological fracture, vertebra(e), initial encounter for fracture
- (seq 4) ICD-10 `F0390`: Unspecified dementia without behavioral disturbance
- (seq 5) ICD-10 `Z681`: Body mass index (BMI) 19.9 or less, adult

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-10 | `K922` | Gastrointestinal hemorrhage, unspecified |
| 2 | ICD-10 | `E43` | Unspecified severe protein-calorie malnutrition |
| 3 | ICD-10 | `M8008XA` | Age-related osteoporosis with current pathological fracture, vertebra(e), initial encounter for fracture |
| 4 | ICD-10 | `F0390` | Unspecified dementia without behavioral disturbance |
| 5 | ICD-10 | `Z681` | Body mass index (BMI) 19.9 or less, adult |
| 6 | ICD-10 | `R000` | Tachycardia, unspecified |
| 7 | ICD-10 | `I10` | Essential (primary) hypertension |
| 8 | ICD-10 | `F329` | Major depressive disorder, single episode, unspecified |
| 9 | ICD-10 | `E039` | Hypothyroidism, unspecified |
| 10 | ICD-10 | `Z66` | Do not resuscitate |
| 11 | ICD-10 | `Z931` | Gastrostomy status |
| 12 | ICD-10 | `M3500` | Sicca syndrome, unspecified |
| 13 | ICD-10 | `Z5309` | Procedure and treatment not carried out because of other contraindication |
| 14 | ICD-10 | `I340` | Nonrheumatic mitral (valve) insufficiency |

## 5. ICU Stays

_No ICU stay recorded for this admission._

## 6. Escalation / Severity Indicators

_No escalation indicators detected from ICD codes or ICU procedure events._

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2160-04-18 | ICD-10 | `0DJD8ZZ` | Inspection of Lower Intestinal Tract, Via Natural or Artificial Opening Endoscopic |


## 8. Critical Findings (Charted Events)

_No critical chart events detected._

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2160-04-14 09:01:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2160-04-14 09:01:00 | Transfer | → Emergency Department (ED) |
| 2160-04-14 12:30:00 | Admission | Admitted from EMERGENCY ROOM (OBSERVATION ADMIT) |
| 2160-04-14 14:28:00 | ED Departure | Left Emergency Dept. |
| 2160-04-18 16:00:00 | Discharge | To SKILLED NURSING FACILITY |

## 10. Missing / Ambiguous Data

- No ICU stay — patient managed on floor/step-down only.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
