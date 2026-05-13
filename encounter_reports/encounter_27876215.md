# Encounter Report — HADM 27876215

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 27876215 |
| Subject ID | 10040025 |
| Patient Sex | F |
| Patient Anchor Age (at anchor year) | 64 |
| Anchor Year | 2143 |
| Admission Time | 2147-11-09 08:02:00 |
| Discharge Time | 2147-11-14 18:53:00 |
| Admission Type | EW EMER. |
| Admission Location | EMERGENCY ROOM |
| Discharge Location | SKILLED NURSING FACILITY |
| Insurance | Other |
| Language | ENGLISH |
| Marital Status | DIVORCED |
| Race/Ethnicity | WHITE |
| ED Registration | 2147-11-09 04:17:00 |
| ED Departure | 2147-11-09 10:56:00 |
| In-Hospital Mortality | No |
| Date of Death (overall) | 2148-02-07 |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| APR | 244 | DIVERTICULITIS & DIVERTICULOSIS | 3.0 | 3.0 |
| HCFA | 377 | G.I. HEMORRHAGE W MCC | N/A | N/A |

### Primary Diagnosis (seq_num = 1)

- **ICD-10 K5791**: Diverticulosis of intestine, part unspecified, without perforation or abscess with bleeding

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2147-11-09 08:02:52 | N/A | MED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-10 `K5791`: Diverticulosis of intestine, part unspecified, without perforation or abscess with bleeding
- (seq 2) ICD-10 `I130`: Hypertensive heart and chronic kidney disease with heart failure and stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease
- (seq 3) ICD-10 `I5023`: Acute on chronic systolic (congestive) heart failure
- (seq 4) ICD-10 `E1122`: Type 2 diabetes mellitus with diabetic chronic kidney disease
- (seq 5) ICD-10 `N183`: Chronic kidney disease, stage 3 (moderate)

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-10 | `K5791` | Diverticulosis of intestine, part unspecified, without perforation or abscess with bleeding |
| 2 | ICD-10 | `I130` | Hypertensive heart and chronic kidney disease with heart failure and stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease |
| 3 | ICD-10 | `I5023` | Acute on chronic systolic (congestive) heart failure |
| 4 | ICD-10 | `E1122` | Type 2 diabetes mellitus with diabetic chronic kidney disease |
| 5 | ICD-10 | `N183` | Chronic kidney disease, stage 3 (moderate) |
| 6 | ICD-10 | `N179` | Acute kidney failure, unspecified |
| 7 | ICD-10 | `D62` | Acute posthemorrhagic anemia |
| 8 | ICD-10 | `I4891` | Unspecified atrial fibrillation |
| 9 | ICD-10 | `I272` | Other secondary pulmonary hypertension |
| 10 | ICD-10 | `R791` | Abnormal coagulation profile |
| 11 | ICD-10 | `D631` | Anemia in chronic kidney disease |
| 12 | ICD-10 | `D509` | Iron deficiency anemia, unspecified |
| 13 | ICD-10 | `I2510` | Atherosclerotic heart disease of native coronary artery without angina pectoris |
| 14 | ICD-10 | `I340` | Nonrheumatic mitral (valve) insufficiency |
| 15 | ICD-10 | `S9032XA` | Contusion of left foot, initial encounter |
| 16 | ICD-10 | `W208XXA` | Other cause of strike by thrown, projected or falling object, initial encounter |
| 17 | ICD-10 | `Y92239` | Unspecified place in hospital as the place of occurrence of the external cause |
| 18 | ICD-10 | `F329` | Major depressive disorder, single episode, unspecified |
| 19 | ICD-10 | `M109` | Gout, unspecified |
| 20 | ICD-10 | `E785` | Hyperlipidemia, unspecified |
| 21 | ICD-10 | `E039` | Hypothyroidism, unspecified |
| 22 | ICD-10 | `E669` | Obesity, unspecified |
| 23 | ICD-10 | `Z6830` | Body mass index (BMI) 30.0-30.9, adult |
| 24 | ICD-10 | `I252` | Old myocardial infarction |
| 25 | ICD-10 | `Z794` | Long term (current) use of insulin |
| 26 | ICD-10 | `Z7901` | Long term (current) use of anticoagulants |
| 27 | ICD-10 | `Z7902` | Long term (current) use of antithrombotics/antiplatelets |
| 28 | ICD-10 | `Z955` | Presence of coronary angioplasty implant and graft |
| 29 | ICD-10 | `Z87891` | Personal history of nicotine dependence |
| 30 | ICD-10 | `Z800` | Family history of malignant neoplasm of digestive organs |

## 5. ICU Stays

_No ICU stay recorded for this admission._

## 6. Escalation / Severity Indicators

The following critical conditions or interventions were detected:

- **Acute Kidney Injury** (ICD diagnosis)

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2147-11-09 | ICD-10 | `30283B1` | Transfusion of Nonautologous 4-Factor Prothrombin Complex Concentrate into Vein, Percutaneous Approach |
| 2 | 2147-11-10 | ICD-10 | `02HV33Z` | Insertion of Infusion Device into Superior Vena Cava, Percutaneous Approach |


## 8. Critical Findings (Charted Events)

_No critical chart events detected._

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2147-11-09 04:17:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2147-11-09 04:17:00 | Transfer | → Emergency Department (ED) |
| 2147-11-09 08:02:00 | Admission | Admitted from EMERGENCY ROOM (EW EMER.) |
| 2147-11-09 08:23:42 | Transfer | → Discharge Lounge (transfer) |
| 2147-11-09 08:37:53 | Transfer | → Neurology (transfer) |
| 2147-11-09 10:56:00 | ED Departure | Left Emergency Dept. |
| 2147-11-14 18:53:00 | Discharge | To SKILLED NURSING FACILITY |

## 10. Missing / Ambiguous Data

- No ICU stay — patient managed on floor/step-down only.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
