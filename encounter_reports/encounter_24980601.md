# Encounter Report — HADM 24980601

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 24980601 |
| Subject ID | 10014354 |
| Patient Sex | M |
| Patient Anchor Age (at anchor year) | 60 |
| Anchor Year | 2146 |
| Admission Time | 2150-02-04 20:12:00 |
| Discharge Time | 2150-02-08 14:10:00 |
| Admission Type | OBSERVATION ADMIT |
| Admission Location | PHYSICIAN REFERRAL |
| Discharge Location | AGAINST ADVICE |
| Insurance | Other |
| Language | ENGLISH |
| Marital Status | SINGLE |
| Race/Ethnicity | WHITE |
| ED Registration | 2150-02-04 14:50:00 |
| ED Departure | 2150-02-04 22:44:00 |
| In-Hospital Mortality | No |
| Date of Death (overall) | N/A |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| HCFA | 880 | ACUTE ADJUSTMENT REACTION & PSYCHOSOCIAL DYSFUNCTION | N/A | N/A |
| APR | 756 | ACUTE ANXIETY & DELIRIUM STATES | 3.0 | 2.0 |

### Primary Diagnosis (seq_num = 1)

- **ICD-10 F447**: Conversion disorder with mixed symptom presentation

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2150-02-04 20:13:49 | N/A | MED |
| 2150-02-04 22:08:01 | MED | OMED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-10 `F447`: Conversion disorder with mixed symptom presentation
- (seq 2) ICD-10 `C9110`: Chronic lymphocytic leukemia of B-cell type not having achieved remission
- (seq 3) ICD-10 `I495`: Sick sinus syndrome
- (seq 4) ICD-10 `E11649`: Type 2 diabetes mellitus with hypoglycemia without coma
- (seq 5) ICD-10 `E1142`: Type 2 diabetes mellitus with diabetic polyneuropathy

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-10 | `F447` | Conversion disorder with mixed symptom presentation |
| 2 | ICD-10 | `C9110` | Chronic lymphocytic leukemia of B-cell type not having achieved remission |
| 3 | ICD-10 | `I495` | Sick sinus syndrome |
| 4 | ICD-10 | `E11649` | Type 2 diabetes mellitus with hypoglycemia without coma |
| 5 | ICD-10 | `E1142` | Type 2 diabetes mellitus with diabetic polyneuropathy |
| 6 | ICD-10 | `H53462` | Homonymous bilateral field defects, left side |
| 7 | ICD-10 | `I10` | Essential (primary) hypertension |
| 8 | ICD-10 | `E785` | Hyperlipidemia, unspecified |
| 9 | ICD-10 | `E669` | Obesity, unspecified |
| 10 | ICD-10 | `I2510` | Atherosclerotic heart disease of native coronary artery without angina pectoris |
| 11 | ICD-10 | `I69344` | Monoplegia of lower limb following cerebral infarction affecting left non-dominant side |
| 12 | ICD-10 | `Z45018` | Encounter for adjustment and management of other part of cardiac pacemaker |
| 13 | ICD-10 | `G4733` | Obstructive sleep apnea (adult) (pediatric) |
| 14 | ICD-10 | `E039` | Hypothyroidism, unspecified |
| 15 | ICD-10 | `H409` | Unspecified glaucoma |
| 16 | ICD-10 | `H8110` | Benign paroxysmal vertigo, unspecified ear |
| 17 | ICD-10 | `F419` | Anxiety disorder, unspecified |
| 18 | ICD-10 | `G4700` | Insomnia, unspecified |
| 19 | ICD-10 | `R2240` | Localized swelling, mass and lump, unspecified lower limb |
| 20 | ICD-10 | `G8929` | Other chronic pain |
| 21 | ICD-10 | `D649` | Anemia, unspecified |
| 22 | ICD-10 | `R740` | Nonspecific elevation of levels of transaminase and lactic acid dehydrogenase [LDH] |
| 23 | ICD-10 | `F325` | Major depressive disorder, single episode, in full remission |
| 24 | ICD-10 | `F09` | Unspecified mental disorder due to known physiological condition |
| 25 | ICD-10 | `L299` | Pruritus, unspecified |
| 26 | ICD-10 | `Z6837` | Body mass index (BMI) 37.0-37.9, adult |
| 27 | ICD-10 | `Z8547` | Personal history of malignant neoplasm of testis |
| 28 | ICD-10 | `Z955` | Presence of coronary angioplasty implant and graft |
| 29 | ICD-10 | `Z794` | Long term (current) use of insulin |
| 30 | ICD-10 | `Z9884` | Bariatric surgery status |

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
| 2150-02-04 14:50:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2150-02-04 14:50:00 | Transfer | → Emergency Department (ED) |
| 2150-02-04 20:12:00 | Admission | Admitted from PHYSICIAN REFERRAL (OBSERVATION ADMIT) |
| 2150-02-04 21:24:55 | Transfer | → Hematology/Oncology Intermediate (transfer) |
| 2150-02-04 22:44:00 | ED Departure | Left Emergency Dept. |
| 2150-02-08 14:10:00 | Discharge | To AGAINST ADVICE |

## 10. Missing / Ambiguous Data

- No procedure ICD codes — procedures may not have been coded or were minor.
- No ICU stay — patient managed on floor/step-down only.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
