# Encounter Report — HADM 26228185

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 26228185 |
| Subject ID | 10014354 |
| Patient Sex | M |
| Patient Anchor Age (at anchor year) | 60 |
| Anchor Year | 2146 |
| Admission Time | 2150-04-30 20:19:00 |
| Discharge Time | 2150-05-07 14:10:00 |
| Admission Type | OBSERVATION ADMIT |
| Admission Location | TRANSFER FROM HOSPITAL |
| Discharge Location | HOME HEALTH CARE |
| Insurance | Other |
| Language | ENGLISH |
| Marital Status | SINGLE |
| Race/Ethnicity | WHITE |
| ED Registration | 2150-04-30 14:26:00 |
| ED Departure | 2150-04-30 21:54:00 |
| In-Hospital Mortality | No |
| Date of Death (overall) | N/A |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| APR | 469 | ACUTE KIDNEY INJURY | 3.0 | 3.0 |
| HCFA | 683 | RENAL FAILURE W CC | N/A | N/A |

### Primary Diagnosis (seq_num = 1)

- **ICD-10 N179**: Acute kidney failure, unspecified

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2150-04-30 20:20:30 | N/A | OMED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-10 `N179`: Acute kidney failure, unspecified
- (seq 2) ICD-10 `N390`: Urinary tract infection, site not specified
- (seq 3) ICD-10 `C9110`: Chronic lymphocytic leukemia of B-cell type not having achieved remission
- (seq 4) ICD-10 `I69354`: Hemiplegia and hemiparesis following cerebral infarction affecting left non-dominant side
- (seq 5) ICD-10 `Z950`: Presence of cardiac pacemaker

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-10 | `N179` | Acute kidney failure, unspecified |
| 2 | ICD-10 | `N390` | Urinary tract infection, site not specified |
| 3 | ICD-10 | `C9110` | Chronic lymphocytic leukemia of B-cell type not having achieved remission |
| 4 | ICD-10 | `I69354` | Hemiplegia and hemiparesis following cerebral infarction affecting left non-dominant side |
| 5 | ICD-10 | `Z950` | Presence of cardiac pacemaker |
| 6 | ICD-10 | `I2510` | Atherosclerotic heart disease of native coronary artery without angina pectoris |
| 7 | ICD-10 | `Z955` | Presence of coronary angioplasty implant and graft |
| 8 | ICD-10 | `E1142` | Type 2 diabetes mellitus with diabetic polyneuropathy |
| 9 | ICD-10 | `Z794` | Long term (current) use of insulin |
| 10 | ICD-10 | `I480` | Paroxysmal atrial fibrillation |
| 11 | ICD-10 | `Z7901` | Long term (current) use of anticoagulants |
| 12 | ICD-10 | `E785` | Hyperlipidemia, unspecified |
| 13 | ICD-10 | `E6601` | Morbid (severe) obesity due to excess calories |
| 14 | ICD-10 | `G4733` | Obstructive sleep apnea (adult) (pediatric) |
| 15 | ICD-10 | `E039` | Hypothyroidism, unspecified |
| 16 | ICD-10 | `F419` | Anxiety disorder, unspecified |
| 17 | ICD-10 | `Z9884` | Bariatric surgery status |
| 18 | ICD-10 | `I10` | Essential (primary) hypertension |
| 19 | ICD-10 | `G8929` | Other chronic pain |
| 20 | ICD-10 | `D696` | Thrombocytopenia, unspecified |
| 21 | ICD-10 | `D509` | Iron deficiency anemia, unspecified |
| 22 | ICD-10 | `F329` | Major depressive disorder, single episode, unspecified |
| 23 | ICD-10 | `I495` | Sick sinus syndrome |
| 24 | ICD-10 | `M109` | Gout, unspecified |
| 25 | ICD-10 | `K289` | Gastrojejunal ulcer, unspecified as acute or chronic, without hemorrhage or perforation |
| 26 | ICD-10 | `R339` | Retention of urine, unspecified |
| 27 | ICD-10 | `I959` | Hypotension, unspecified |
| 28 | ICD-10 | `Z8547` | Personal history of malignant neoplasm of testis |
| 29 | ICD-10 | `R319` | Hematuria, unspecified |
| 30 | ICD-10 | `R740` | Nonspecific elevation of levels of transaminase and lactic acid dehydrogenase [LDH] |
| 31 | ICD-10 | `R5383` | Other fatigue |
| 32 | ICD-10 | `T402X5A` | Adverse effect of other opioids, initial encounter |
| 33 | ICD-10 | `K5900` | Constipation, unspecified |
| 34 | ICD-10 | `E861` | Hypovolemia |

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
| 2150-04-30 14:26:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2150-04-30 14:26:00 | Transfer | → Emergency Department (ED) |
| 2150-04-30 20:19:00 | Admission | Admitted from TRANSFER FROM HOSPITAL (OBSERVATION ADMIT) |
| 2150-04-30 21:54:00 | ED Departure | Left Emergency Dept. |
| 2150-05-02 18:06:10 | Transfer | → Hematology/Oncology Intermediate (transfer) |
| 2150-05-07 14:10:00 | Discharge | To HOME HEALTH CARE |

## 10. Missing / Ambiguous Data

- No procedure ICD codes — procedures may not have been coded or were minor.
- No ICU stay — patient managed on floor/step-down only.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
