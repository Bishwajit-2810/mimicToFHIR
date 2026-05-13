# Encounter Report — HADM 24096336

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 24096336 |
| Subject ID | 10014354 |
| Patient Sex | M |
| Patient Anchor Age (at anchor year) | 60 |
| Anchor Year | 2146 |
| Admission Time | 2149-06-19 22:54:00 |
| Discharge Time | 2149-06-20 13:48:00 |
| Admission Type | EU OBSERVATION |
| Admission Location | PHYSICIAN REFERRAL |
| Discharge Location | N/A |
| Insurance | Other |
| Language | ENGLISH |
| Marital Status | SINGLE |
| Race/Ethnicity | WHITE |
| ED Registration | 2149-06-19 17:01:00 |
| ED Departure | 2149-06-20 13:48:00 |
| In-Hospital Mortality | No |
| Date of Death (overall) | N/A |

## 2. Hospital Visit Reason

### Primary Diagnosis (seq_num = 1)

- **ICD-10 T383X1A**: Poisoning by insulin and oral hypoglycemic [antidiabetic] drugs, accidental (unintentional), initial encounter

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2149-06-19 22:55:33 | N/A | MED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-10 `T383X1A`: Poisoning by insulin and oral hypoglycemic [antidiabetic] drugs, accidental (unintentional), initial encounter
- (seq 2) ICD-10 `Y929`: Unspecified place or not applicable
- (seq 3) ICD-10 `E1165`: Type 2 diabetes mellitus with hyperglycemia
- (seq 4) ICD-10 `C9111`: Chronic lymphocytic leukemia of B-cell type in remission
- (seq 5) ICD-10 `Z794`: Long term (current) use of insulin

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-10 | `T383X1A` | Poisoning by insulin and oral hypoglycemic [antidiabetic] drugs, accidental (unintentional), initial encounter |
| 2 | ICD-10 | `Y929` | Unspecified place or not applicable |
| 3 | ICD-10 | `E1165` | Type 2 diabetes mellitus with hyperglycemia |
| 4 | ICD-10 | `C9111` | Chronic lymphocytic leukemia of B-cell type in remission |
| 5 | ICD-10 | `Z794` | Long term (current) use of insulin |
| 6 | ICD-10 | `I10` | Essential (primary) hypertension |
| 7 | ICD-10 | `M19019` | Primary osteoarthritis, unspecified shoulder |
| 8 | ICD-10 | `E039` | Hypothyroidism, unspecified |
| 9 | ICD-10 | `F323` | Major depressive disorder, single episode, severe with psychotic features |
| 10 | ICD-10 | `Z950` | Presence of cardiac pacemaker |
| 11 | ICD-10 | `Z7902` | Long term (current) use of antithrombotics/antiplatelets |
| 12 | ICD-10 | `M109` | Gout, unspecified |
| 13 | ICD-10 | `G4733` | Obstructive sleep apnea (adult) (pediatric) |
| 14 | ICD-10 | `E6601` | Morbid (severe) obesity due to excess calories |
| 15 | ICD-10 | `I480` | Paroxysmal atrial fibrillation |

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
| 2149-06-19 17:01:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2149-06-19 17:01:00 | Transfer | → Emergency Department (ED) |
| 2149-06-19 22:54:00 | Admission | Admitted from PHYSICIAN REFERRAL (EU OBSERVATION) |
| 2149-06-20 13:48:00 | Discharge | To N/A |
| 2149-06-20 13:48:00 | ED Departure | Left Emergency Dept. |

## 10. Missing / Ambiguous Data

- Discharge location not recorded.
- No procedure ICD codes — procedures may not have been coded or were minor.
- No ICU stay — patient managed on floor/step-down only.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
