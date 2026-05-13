# Encounter Report — HADM 25696644

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 25696644 |
| Subject ID | 10002930 |
| Patient Sex | F |
| Patient Anchor Age (at anchor year) | 48 |
| Anchor Year | 2193 |
| Admission Time | 2196-04-14 12:25:00 |
| Discharge Time | 2196-04-17 15:28:00 |
| Admission Type | EW EMER. |
| Admission Location | EMERGENCY ROOM |
| Discharge Location | PSYCH FACILITY |
| Insurance | Medicare |
| Language | ENGLISH |
| Marital Status | SINGLE |
| Race/Ethnicity | BLACK/AFRICAN AMERICAN |
| ED Registration | 2196-04-14 05:55:00 |
| ED Departure | 2196-04-14 13:40:00 |
| In-Hospital Mortality | No |
| Date of Death (overall) | 2201-12-24 |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| HCFA | 644 | ENDOCRINE DISORDERS W CC | N/A | N/A |
| APR | 424 | OTHER ENDOCRINE DISORDERS | 1.0 | 2.0 |

### Primary Diagnosis (seq_num = 1)

- **ICD-9 2511**: Other specified hypoglycemia

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2196-04-14 12:26:15 | N/A | MED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-9 `2511`: Other specified hypoglycemia
- (seq 2) ICD-9 `V6284`: Suicidal ideation
- (seq 3) ICD-9 `2762`: Acidosis
- (seq 4) ICD-9 `V08`: Asymptomatic human immunodeficiency virus [HIV] infection status
- (seq 5) ICD-9 `33829`: Other chronic pain

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-9 | `2511` | Other specified hypoglycemia |
| 2 | ICD-9 | `V6284` | Suicidal ideation |
| 3 | ICD-9 | `2762` | Acidosis |
| 4 | ICD-9 | `V08` | Asymptomatic human immunodeficiency virus [HIV] infection status |
| 5 | ICD-9 | `33829` | Other chronic pain |
| 6 | ICD-9 | `V1552` | Personal history of traumatic brain injury |
| 7 | ICD-9 | `311` | Depressive disorder, not elsewhere classified |
| 8 | ICD-9 | `30590` | Other, mixed, or unspecified drug abuse, unspecified |
| 9 | ICD-9 | `30500` | Alcohol abuse, unspecified |
| 10 | ICD-9 | `V600` | Lack of housing |
| 11 | ICD-9 | `07054` | Chronic hepatitis C without mention of hepatic coma |
| 12 | ICD-9 | `37950` | Nystagmus, unspecified |

## 5. ICU Stays

| Stay ID | First Care Unit | Last Care Unit | ICU Admit | ICU Discharge | LOS (days) |
|---|---|---|---|---|---|
| 37049133 | Medical Intensive Care Unit (MICU) | Medical Intensive Care Unit (MICU) | 2196-04-14 13:40:00 | 2196-04-15 16:54:44 | 1.14 |

## 6. Escalation / Severity Indicators

_No escalation indicators detected from ICD codes or ICU procedure events._

## 7. Procedures and Interventions

_No ICD-coded procedures recorded._

### ICU Procedure Events (from `icu/procedureevents.csv.gz`)

- 20 Gauge (category: Access Lines - Peripheral, started: 2196-04-14 14:12:00, status: FinishedRunning)

## 8. Critical Findings (Charted Events)

- **Seizure** (first noted: 2196-04-14 14:18:00)
- **Dialysis patient** (first noted: 2196-04-14 16:37:00)

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2196-04-14 05:55:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2196-04-14 05:55:00 | Transfer | → Emergency Department (ED) |
| 2196-04-14 12:25:00 | Admission | Admitted from EMERGENCY ROOM (EW EMER.) |
| 2196-04-14 13:40:00 | ED Departure | Left Emergency Dept. |
| 2196-04-14 13:40:00 | ICU Admission | Medical Intensive Care Unit (MICU) (LOS: 1.1 days) |
| 2196-04-15 16:54:44 | Transfer | → Medicine (transfer) |
| 2196-04-17 15:28:00 | Discharge | To PSYCH FACILITY |

## 10. Missing / Ambiguous Data

- No procedure ICD codes — procedures may not have been coded or were minor.

## 11. Manual Review Recommendation

**This encounter is flagged for manual review:**

- ICU stay present but no ICD procedures coded.
