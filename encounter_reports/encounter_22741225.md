# Encounter Report — HADM 22741225

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 22741225 |
| Subject ID | 10014354 |
| Patient Sex | M |
| Patient Anchor Age (at anchor year) | 60 |
| Anchor Year | 2146 |
| Admission Time | 2146-10-08 23:47:00 |
| Discharge Time | 2146-10-12 18:20:00 |
| Admission Type | EW EMER. |
| Admission Location | EMERGENCY ROOM |
| Discharge Location | HOME HEALTH CARE |
| Insurance | Other |
| Language | ENGLISH |
| Marital Status | MARRIED |
| Race/Ethnicity | WHITE |
| ED Registration | 2146-10-08 21:27:00 |
| ED Departure | 2146-10-09 01:08:00 |
| In-Hospital Mortality | No |
| Date of Death (overall) | N/A |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| APR | 58 | OTHER DISORDERS OF NERVOUS SYSTEM | 2.0 | 2.0 |
| HCFA | 57 | DEGENERATIVE NERVOUS SYSTEM DISORDERS W/O MCC | N/A | N/A |

### Primary Diagnosis (seq_num = 1)

- **ICD-10 I69354**: Hemiplegia and hemiparesis following cerebral infarction affecting left non-dominant side

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2146-10-08 23:48:00 | N/A | NMED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-10 `I69354`: Hemiplegia and hemiparesis following cerebral infarction affecting left non-dominant side
- (seq 2) ICD-10 `C9110`: Chronic lymphocytic leukemia of B-cell type not having achieved remission
- (seq 3) ICD-10 `G8194`: Hemiplegia, unspecified affecting left nondominant side
- (seq 4) ICD-10 `Z9282`: Status post administration of tPA (rtPA) in a different facility within the last 24 hours prior to admission to current facility
- (seq 5) ICD-10 `E785`: Hyperlipidemia, unspecified

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-10 | `I69354` | Hemiplegia and hemiparesis following cerebral infarction affecting left non-dominant side |
| 2 | ICD-10 | `C9110` | Chronic lymphocytic leukemia of B-cell type not having achieved remission |
| 3 | ICD-10 | `G8194` | Hemiplegia, unspecified affecting left nondominant side |
| 4 | ICD-10 | `Z9282` | Status post administration of tPA (rtPA) in a different facility within the last 24 hours prior to admission to current facility |
| 5 | ICD-10 | `E785` | Hyperlipidemia, unspecified |
| 6 | ICD-10 | `I10` | Essential (primary) hypertension |
| 7 | ICD-10 | `M25512` | Pain in left shoulder |
| 8 | ICD-10 | `E0865` | Diabetes mellitus due to underlying condition with hyperglycemia |
| 9 | ICD-10 | `J449` | Chronic obstructive pulmonary disease, unspecified |
| 10 | ICD-10 | `E6601` | Morbid (severe) obesity due to excess calories |
| 11 | ICD-10 | `F329` | Major depressive disorder, single episode, unspecified |
| 12 | ICD-10 | `E039` | Hypothyroidism, unspecified |
| 13 | ICD-10 | `Z950` | Presence of cardiac pacemaker |
| 14 | ICD-10 | `Z9884` | Bariatric surgery status |
| 15 | ICD-10 | `H409` | Unspecified glaucoma |
| 16 | ICD-10 | `G629` | Polyneuropathy, unspecified |

## 5. ICU Stays

| Stay ID | First Care Unit | Last Care Unit | ICU Admit | ICU Discharge | LOS (days) |
|---|---|---|---|---|---|
| 37200209 | Surgical Intensive Care Unit (SICU) | Surgical Intensive Care Unit (SICU) | 2146-10-09 01:08:00 | 2146-10-09 21:20:50 | 0.84 |

## 6. Escalation / Severity Indicators

_No escalation indicators detected from ICD codes or ICU procedure events._

## 7. Procedures and Interventions

_No ICD-coded procedures recorded._

### ICU Procedure Events (from `icu/procedureevents.csv.gz`)

- 20 Gauge (category: Access Lines - Peripheral, started: 2146-10-09 01:41:00, status: FinishedRunning)

## 8. Critical Findings (Charted Events)

- **Dialysis patient** (first noted: 2146-10-09 03:14:00)

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2146-10-08 21:27:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2146-10-08 21:27:00 | Transfer | → Emergency Department (ED) |
| 2146-10-08 23:47:00 | Admission | Admitted from EMERGENCY ROOM (EW EMER.) |
| 2146-10-09 01:08:00 | ED Departure | Left Emergency Dept. |
| 2146-10-09 01:08:00 | ICU Admission | Surgical Intensive Care Unit (SICU) (LOS: 0.8 days) |
| 2146-10-09 21:20:50 | Transfer | → Neurology (transfer) |
| 2146-10-10 21:01:29 | Transfer | → Neurology (transfer) |
| 2146-10-12 18:20:00 | Discharge | To HOME HEALTH CARE |

## 10. Missing / Ambiguous Data

- No procedure ICD codes — procedures may not have been coded or were minor.

## 11. Manual Review Recommendation

**This encounter is flagged for manual review:**

- ICU stay present but no ICD procedures coded.
