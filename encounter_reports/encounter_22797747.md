# Encounter Report — HADM 22797747

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 22797747 |
| Subject ID | 10038992 |
| Patient Sex | M |
| Patient Anchor Age (at anchor year) | 70 |
| Anchor Year | 2185 |
| Admission Time | 2185-11-02 18:26:00 |
| Discharge Time | 2185-11-08 16:22:00 |
| Admission Type | URGENT |
| Admission Location | TRANSFER FROM HOSPITAL |
| Discharge Location | HOME HEALTH CARE |
| Insurance | Medicare |
| Language | ENGLISH |
| Marital Status | MARRIED |
| Race/Ethnicity | UNKNOWN |
| ED Registration | N/A |
| ED Departure | N/A |
| In-Hospital Mortality | No |
| Date of Death (overall) | N/A |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| APR | 137 | MAJOR RESPIRATORY INFECTIONS & INFLAMMATIONS | 4.0 | 4.0 |
| HCFA | 177 | RESPIRATORY INFECTIONS & INFLAMMATIONS W MCC | N/A | N/A |

### Primary Diagnosis (seq_num = 1)

- **ICD-9 5070**: Pneumonitis due to inhalation of food or vomitus

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2185-11-02 18:27:04 | N/A | MED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-9 `5070`: Pneumonitis due to inhalation of food or vomitus
- (seq 2) ICD-9 `5845`: Acute kidney failure with lesion of tubular necrosis
- (seq 3) ICD-9 `34830`: Encephalopathy, unspecified
- (seq 4) ICD-9 `00845`: Intestinal infection due to Clostridium difficile
- (seq 5) ICD-9 `4589`: Hypotension, unspecified

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-9 | `5070` | Pneumonitis due to inhalation of food or vomitus |
| 2 | ICD-9 | `5845` | Acute kidney failure with lesion of tubular necrosis |
| 3 | ICD-9 | `34830` | Encephalopathy, unspecified |
| 4 | ICD-9 | `00845` | Intestinal infection due to Clostridium difficile |
| 5 | ICD-9 | `4589` | Hypotension, unspecified |
| 6 | ICD-9 | `5119` | Unspecified pleural effusion |
| 7 | ICD-9 | `4254` | Other primary cardiomyopathies |
| 8 | ICD-9 | `4239` | Unspecified disease of pericardium |
| 9 | ICD-9 | `4280` | Congestive heart failure, unspecified |
| 10 | ICD-9 | `29420` | Dementia, unspecified, without behavioral disturbance |
| 11 | ICD-9 | `5853` | Chronic kidney disease, Stage III (moderate) |
| 12 | ICD-9 | `79902` | Hypoxemia |
| 13 | ICD-9 | `42789` | Other specified cardiac dysrhythmias |
| 14 | ICD-9 | `2749` | Gout, unspecified |
| 15 | ICD-9 | `496` | Chronic airway obstruction, not elsewhere classified |
| 16 | ICD-9 | `78820` | Retention of urine, unspecified |
| 17 | ICD-9 | `40390` | Hypertensive chronic kidney disease, unspecified, with chronic kidney disease stage I through stage IV, or unspecified |
| 18 | ICD-9 | `7823` | Edema |
| 19 | ICD-9 | `7197` | Difficulty in walking |
| 20 | ICD-9 | `7904` | Nonspecific elevation of levels of transaminase or lactic acid dehydrogenase [LDH] |
| 21 | ICD-9 | `V5866` | Long-term (current) use of aspirin |
| 22 | ICD-9 | `92320` | Contusion of hand(s) |
| 23 | ICD-9 | `2449` | Unspecified acquired hypothyroidism |
| 24 | ICD-9 | `60001` | Hypertrophy (benign) of prostate with urinary obstruction and other lower urinary tract symptoms (LUTS) |
| 25 | ICD-9 | `59960` | Urinary obstruction, unspecified |
| 26 | ICD-9 | `71650` | Unspecified polyarthropathy or polyarthritis, site unspecified |
| 27 | ICD-9 | `78057` | Unspecified sleep apnea |
| 28 | ICD-9 | `311` | Depressive disorder, not elsewhere classified |
| 29 | ICD-9 | `25000` | Diabetes mellitus without mention of complication, type II or unspecified type, not stated as uncontrolled |
| 30 | ICD-9 | `E9063` | Bite of other animal except arthropod |
| 31 | ICD-9 | `5305` | Dyskinesia of esophagus |

## 5. ICU Stays

_No ICU stay recorded for this admission._

## 6. Escalation / Severity Indicators

The following critical conditions or interventions were detected:

- **Acute Kidney Injury** (ICD diagnosis)

## 7. Procedures and Interventions

_No ICD-coded procedures recorded._


## 8. Critical Findings (Charted Events)

_No critical chart events detected._

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2185-11-02 18:26:00 | Admission | Admitted from TRANSFER FROM HOSPITAL (URGENT) |
| 2185-11-03 17:04:16 | Transfer | → Medicine (transfer) |
| 2185-11-08 16:22:00 | Discharge | To HOME HEALTH CARE |

## 10. Missing / Ambiguous Data

- No ED registration time — admission may not have gone through ED.
- No procedure ICD codes — procedures may not have been coded or were minor.
- No ICU stay — patient managed on floor/step-down only.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
