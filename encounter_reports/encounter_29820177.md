# Encounter Report — HADM 29820177

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 29820177 |
| Subject ID | 10020740 |
| Patient Sex | M |
| Patient Anchor Age (at anchor year) | 56 |
| Anchor Year | 2150 |
| Admission Time | 2150-07-09 22:09:00 |
| Discharge Time | 2150-07-12 18:00:00 |
| Admission Type | DIRECT OBSERVATION |
| Admission Location | CLINIC REFERRAL |
| Discharge Location | N/A |
| Insurance | Other |
| Language | ENGLISH |
| Marital Status | SINGLE |
| Race/Ethnicity | WHITE |
| ED Registration | N/A |
| ED Departure | N/A |
| In-Hospital Mortality | No |
| Date of Death (overall) | N/A |

## 2. Hospital Visit Reason

### Primary Diagnosis (seq_num = 1)

- **ICD-9 5770**: Acute pancreatitis

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2150-07-09 22:10:54 | N/A | MED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-9 `5770`: Acute pancreatitis
- (seq 2) ICD-9 `57450`: Calculus of bile duct without mention of cholecystitis, without mention of obstruction
- (seq 3) ICD-9 `6929`: Contact dermatitis and other eczema, unspecified cause
- (seq 4) ICD-9 `5939`: Unspecified disorder of kidney and ureter
- (seq 5) ICD-9 `V1204`: Personal history of Methicillin resistant Staphylococcus aureus

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-9 | `5770` | Acute pancreatitis |
| 2 | ICD-9 | `57450` | Calculus of bile duct without mention of cholecystitis, without mention of obstruction |
| 3 | ICD-9 | `6929` | Contact dermatitis and other eczema, unspecified cause |
| 4 | ICD-9 | `5939` | Unspecified disorder of kidney and ureter |
| 5 | ICD-9 | `V1204` | Personal history of Methicillin resistant Staphylococcus aureus |
| 6 | ICD-9 | `29570` | Schizoaffective disorder, unspecified |
| 7 | ICD-9 | `311` | Depressive disorder, not elsewhere classified |
| 8 | ICD-9 | `25000` | Diabetes mellitus without mention of complication, type II or unspecified type, not stated as uncontrolled |
| 9 | ICD-9 | `49390` | Asthma, unspecified type, unspecified |
| 10 | ICD-9 | `32723` | Obstructive sleep apnea (adult)(pediatric) |
| 11 | ICD-9 | `2724` | Other and unspecified hyperlipidemia |
| 12 | ICD-9 | `V173` | Family history of ischemic heart disease |
| 13 | ICD-9 | `V5867` | Long-term (current) use of insulin |
| 14 | ICD-9 | `7892` | Splenomegaly |

## 5. ICU Stays

_No ICU stay recorded for this admission._

## 6. Escalation / Severity Indicators

_No escalation indicators detected from ICD codes or ICU procedure events._

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2150-07-09 | ICD-9 | `4513` | Other endoscopy of small intestine |
| 2 | 2150-07-09 | ICD-9 | `8874` | Diagnostic ultrasound of digestive system |
| 3 | 2150-07-10 | ICD-9 | `9705` | Replacement of stent (tube) in biliary or pancreatic duct |
| 4 | 2150-07-10 | ICD-9 | `5188` | Endoscopic removal of stone(s) from biliary tract |


## 8. Critical Findings (Charted Events)

_No critical chart events detected._

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2150-07-09 22:09:00 | Admission | Admitted from CLINIC REFERRAL (DIRECT OBSERVATION) |
| 2150-07-12 18:00:00 | Discharge | To N/A |

## 10. Missing / Ambiguous Data

- No ED registration time — admission may not have gone through ED.
- Discharge location not recorded.
- No ICU stay — patient managed on floor/step-down only.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
