# Encounter Report — HADM 22508257

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 22508257 |
| Subject ID | 10014354 |
| Patient Sex | M |
| Patient Anchor Age (at anchor year) | 60 |
| Anchor Year | 2146 |
| Admission Time | 2148-05-10 23:29:00 |
| Discharge Time | 2148-05-20 14:30:00 |
| Admission Type | OBSERVATION ADMIT |
| Admission Location | EMERGENCY ROOM |
| Discharge Location | HOME HEALTH CARE |
| Insurance | Other |
| Language | ENGLISH |
| Marital Status | SINGLE |
| Race/Ethnicity | WHITE |
| ED Registration | 2148-05-10 20:25:00 |
| ED Departure | 2148-05-11 01:22:00 |
| In-Hospital Mortality | No |
| Date of Death (overall) | N/A |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| APR | 253 | OTHER & UNSPECIFIED GASTROINTESTINAL HEMORRHAGE | 3.0 | 2.0 |
| HCFA | 378 | G.I. HEMORRHAGE W CC | N/A | N/A |

### Primary Diagnosis (seq_num = 1)

- **ICD-10 K625**: Hemorrhage of anus and rectum

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2148-05-10 23:30:06 | N/A | OMED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-10 `K625`: Hemorrhage of anus and rectum
- (seq 2) ICD-10 `D62`: Acute posthemorrhagic anemia
- (seq 3) ICD-10 `C9110`: Chronic lymphocytic leukemia of B-cell type not having achieved remission
- (seq 4) ICD-10 `I5032`: Chronic diastolic (congestive) heart failure
- (seq 5) ICD-10 `E11649`: Type 2 diabetes mellitus with hypoglycemia without coma

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-10 | `K625` | Hemorrhage of anus and rectum |
| 2 | ICD-10 | `D62` | Acute posthemorrhagic anemia |
| 3 | ICD-10 | `C9110` | Chronic lymphocytic leukemia of B-cell type not having achieved remission |
| 4 | ICD-10 | `I5032` | Chronic diastolic (congestive) heart failure |
| 5 | ICD-10 | `E11649` | Type 2 diabetes mellitus with hypoglycemia without coma |
| 6 | ICD-10 | `I481` | Persistent atrial fibrillation |
| 7 | ICD-10 | `E871` | Hypo-osmolality and hyponatremia |
| 8 | ICD-10 | `E1136` | Type 2 diabetes mellitus with diabetic cataract |
| 9 | ICD-10 | `I2510` | Atherosclerotic heart disease of native coronary artery without angina pectoris |
| 10 | ICD-10 | `Z950` | Presence of cardiac pacemaker |
| 11 | ICD-10 | `Z7901` | Long term (current) use of anticoagulants |
| 12 | ICD-10 | `K648` | Other hemorrhoids |
| 13 | ICD-10 | `K635` | Polyp of colon |
| 14 | ICD-10 | `Z9884` | Bariatric surgery status |
| 15 | ICD-10 | `G4733` | Obstructive sleep apnea (adult) (pediatric) |
| 16 | ICD-10 | `E039` | Hypothyroidism, unspecified |
| 17 | ICD-10 | `H409` | Unspecified glaucoma |
| 18 | ICD-10 | `Z8547` | Personal history of malignant neoplasm of testis |
| 19 | ICD-10 | `F329` | Major depressive disorder, single episode, unspecified |
| 20 | ICD-10 | `F419` | Anxiety disorder, unspecified |
| 21 | ICD-10 | `M549` | Dorsalgia, unspecified |
| 22 | ICD-10 | `M25519` | Pain in unspecified shoulder |
| 23 | ICD-10 | `G8929` | Other chronic pain |
| 24 | ICD-10 | `R791` | Abnormal coagulation profile |
| 25 | ICD-10 | `I129` | Hypertensive chronic kidney disease with stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease |
| 26 | ICD-10 | `K6389` | Other specified diseases of intestine |
| 27 | ICD-10 | `E669` | Obesity, unspecified |
| 28 | ICD-10 | `Z6835` | Body mass index (BMI) 35.0-35.9, adult |

## 5. ICU Stays

_No ICU stay recorded for this admission._

## 6. Escalation / Severity Indicators

_No escalation indicators detected from ICD codes or ICU procedure events._

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2148-05-19 | ICD-10 | `0DBH8ZX` | Excision of Cecum, Via Natural or Artificial Opening Endoscopic, Diagnostic |
| 2 | 2148-05-19 | ICD-10 | `0DBM8ZX` | Excision of Descending Colon, Via Natural or Artificial Opening Endoscopic, Diagnostic |
| 3 | 2148-05-12 | ICD-10 | `0DJD8ZZ` | Inspection of Lower Intestinal Tract, Via Natural or Artificial Opening Endoscopic |
| 4 | 2148-05-18 | ICD-10 | `0DJD8ZZ` | Inspection of Lower Intestinal Tract, Via Natural or Artificial Opening Endoscopic |


## 8. Critical Findings (Charted Events)

_No critical chart events detected._

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2148-05-10 20:25:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2148-05-10 20:25:00 | Transfer | → Emergency Department (ED) |
| 2148-05-10 23:29:00 | Admission | Admitted from EMERGENCY ROOM (OBSERVATION ADMIT) |
| 2148-05-11 01:22:00 | ED Departure | Left Emergency Dept. |
| 2148-05-11 15:02:38 | Transfer | → Hematology/Oncology Intermediate (transfer) |
| 2148-05-20 14:30:00 | Discharge | To HOME HEALTH CARE |

## 10. Missing / Ambiguous Data

- No ICU stay — patient managed on floor/step-down only.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
