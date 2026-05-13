# Encounter Report — HADM 29757856

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 29757856 |
| Subject ID | 10014354 |
| Patient Sex | M |
| Patient Anchor Age (at anchor year) | 60 |
| Anchor Year | 2146 |
| Admission Time | 2150-04-10 02:40:00 |
| Discharge Time | 2150-04-15 18:00:00 |
| Admission Type | EW EMER. |
| Admission Location | WALK-IN/SELF REFERRAL |
| Discharge Location | HOME HEALTH CARE |
| Insurance | Other |
| Language | ENGLISH |
| Marital Status | SINGLE |
| Race/Ethnicity | WHITE |
| ED Registration | 2150-04-09 19:50:00 |
| ED Departure | 2150-04-10 03:46:00 |
| In-Hospital Mortality | No |
| Date of Death (overall) | N/A |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| HCFA | 381 | COMPLICATED PEPTIC ULCER W CC | N/A | N/A |
| APR | 241 | PEPTIC ULCER & GASTRITIS | 3.0 | 3.0 |

### Primary Diagnosis (seq_num = 1)

- **ICD-10 K289**: Gastrojejunal ulcer, unspecified as acute or chronic, without hemorrhage or perforation

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2150-04-10 02:41:44 | N/A | OMED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-10 `K289`: Gastrojejunal ulcer, unspecified as acute or chronic, without hemorrhage or perforation
- (seq 2) ICD-10 `K9589`: Other complications of other bariatric procedure
- (seq 3) ICD-10 `K316`: Fistula of stomach and duodenum
- (seq 4) ICD-10 `N179`: Acute kidney failure, unspecified
- (seq 5) ICD-10 `I5032`: Chronic diastolic (congestive) heart failure

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-10 | `K289` | Gastrojejunal ulcer, unspecified as acute or chronic, without hemorrhage or perforation |
| 2 | ICD-10 | `K9589` | Other complications of other bariatric procedure |
| 3 | ICD-10 | `K316` | Fistula of stomach and duodenum |
| 4 | ICD-10 | `N179` | Acute kidney failure, unspecified |
| 5 | ICD-10 | `I5032` | Chronic diastolic (congestive) heart failure |
| 6 | ICD-10 | `F05` | Delirium due to known physiological condition |
| 7 | ICD-10 | `C9110` | Chronic lymphocytic leukemia of B-cell type not having achieved remission |
| 8 | ICD-10 | `Z6841` | Body mass index (BMI) 40.0-44.9, adult |
| 9 | ICD-10 | `F3340` | Major depressive disorder, recurrent, in remission, unspecified |
| 10 | ICD-10 | `N141` | Nephropathy induced by other drugs, medicaments and biological substances |
| 11 | ICD-10 | `I129` | Hypertensive chronic kidney disease with stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease |
| 12 | ICD-10 | `N183` | Chronic kidney disease, stage 3 (moderate) |
| 13 | ICD-10 | `E1122` | Type 2 diabetes mellitus with diabetic chronic kidney disease |
| 14 | ICD-10 | `E1142` | Type 2 diabetes mellitus with diabetic polyneuropathy |
| 15 | ICD-10 | `E1165` | Type 2 diabetes mellitus with hyperglycemia |
| 16 | ICD-10 | `I480` | Paroxysmal atrial fibrillation |
| 17 | ICD-10 | `E039` | Hypothyroidism, unspecified |
| 18 | ICD-10 | `T508X5A` | Adverse effect of diagnostic agents, initial encounter |
| 19 | ICD-10 | `Y92238` | Other place in hospital as the place of occurrence of the external cause |
| 20 | ICD-10 | `K219` | Gastro-esophageal reflux disease without esophagitis |
| 21 | ICD-10 | `K449` | Diaphragmatic hernia without obstruction or gangrene |
| 22 | ICD-10 | `E781` | Pure hyperglyceridemia |
| 23 | ICD-10 | `E6601` | Morbid (severe) obesity due to excess calories |
| 24 | ICD-10 | `D649` | Anemia, unspecified |
| 25 | ICD-10 | `R5383` | Other fatigue |
| 26 | ICD-10 | `I69344` | Monoplegia of lower limb following cerebral infarction affecting left non-dominant side |
| 27 | ICD-10 | `M109` | Gout, unspecified |
| 28 | ICD-10 | `M160` | Bilateral primary osteoarthritis of hip |
| 29 | ICD-10 | `M19012` | Primary osteoarthritis, left shoulder |
| 30 | ICD-10 | `M19011` | Primary osteoarthritis, right shoulder |
| 31 | ICD-10 | `G4733` | Obstructive sleep apnea (adult) (pediatric) |
| 32 | ICD-10 | `R7989` | Other specified abnormal findings of blood chemistry |
| 33 | ICD-10 | `L853` | Xerosis cutis |
| 34 | ICD-10 | `F419` | Anxiety disorder, unspecified |
| 35 | ICD-10 | `I252` | Old myocardial infarction |
| 36 | ICD-10 | `Z7901` | Long term (current) use of anticoagulants |
| 37 | ICD-10 | `Z794` | Long term (current) use of insulin |
| 38 | ICD-10 | `Z8547` | Personal history of malignant neoplasm of testis |
| 39 | ICD-10 | `Z950` | Presence of cardiac pacemaker |

## 5. ICU Stays

_No ICU stay recorded for this admission._

## 6. Escalation / Severity Indicators

The following critical conditions or interventions were detected:

- **Acute Kidney Injury** (ICD diagnosis)

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2150-04-11 | ICD-10 | `0DD68ZX` | Extraction of Stomach, Via Natural or Artificial Opening Endoscopic, Diagnostic |


## 8. Critical Findings (Charted Events)

_No critical chart events detected._

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2150-04-09 19:50:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2150-04-09 19:50:00 | Transfer | → Emergency Department (ED) |
| 2150-04-10 02:40:00 | Admission | Admitted from WALK-IN/SELF REFERRAL (EW EMER.) |
| 2150-04-10 03:46:00 | ED Departure | Left Emergency Dept. |
| 2150-04-15 18:00:00 | Discharge | To HOME HEALTH CARE |

## 10. Missing / Ambiguous Data

- No ICU stay — patient managed on floor/step-down only.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
