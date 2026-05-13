# Encounter Report — HADM 27660781

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 27660781 |
| Subject ID | 10021487 |
| Patient Sex | M |
| Patient Anchor Age (at anchor year) | 43 |
| Anchor Year | 2116 |
| Admission Time | 2117-03-03 15:59:00 |
| Discharge Time | 2117-03-27 16:40:00 |
| Admission Type | DIRECT EMER. |
| Admission Location | CLINIC REFERRAL |
| Discharge Location | HOME |
| Insurance | Other |
| Language | ENGLISH |
| Marital Status | DIVORCED |
| Race/Ethnicity | WHITE |
| ED Registration | N/A |
| ED Departure | N/A |
| In-Hospital Mortality | No |
| Date of Death (overall) | N/A |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| APR | 279 | HEPATIC COMA & OTHER MAJOR ACUTE LIVER DISORDERS | 4.0 | 2.0 |
| HCFA | 441 | DISORDERS OF LIVER EXCEPT MALIG,CIRR,ALC HEPA W MCC | N/A | N/A |

### Primary Diagnosis (seq_num = 1)

- **ICD-9 5720**: Abscess of liver

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2117-03-03 15:59:43 | N/A | SURG |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-9 `5720`: Abscess of liver
- (seq 2) ICD-9 `5770`: Acute pancreatitis
- (seq 3) ICD-9 `5762`: Obstruction of bile duct
- (seq 4) ICD-9 `56722`: Peritoneal abscess
- (seq 5) ICD-9 `2639`: Unspecified protein-calorie malnutrition

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-9 | `5720` | Abscess of liver |
| 2 | ICD-9 | `5770` | Acute pancreatitis |
| 3 | ICD-9 | `5762` | Obstruction of bile duct |
| 4 | ICD-9 | `56722` | Peritoneal abscess |
| 5 | ICD-9 | `2639` | Unspecified protein-calorie malnutrition |
| 6 | ICD-9 | `5601` | Paralytic ileus |
| 7 | ICD-9 | `5119` | Unspecified pleural effusion |
| 8 | ICD-9 | `7837` | Adult failure to thrive |

## 5. ICU Stays

| Stay ID | First Care Unit | Last Care Unit | ICU Admit | ICU Discharge | LOS (days) |
|---|---|---|---|---|---|
| 35065627 | Surgical Intensive Care Unit (SICU) | Surgical Intensive Care Unit (SICU) | 2117-03-07 23:06:21 | 2117-03-09 18:01:57 | 1.79 |

## 6. Escalation / Severity Indicators

_No escalation indicators detected from ICD codes or ICU procedure events._

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2117-03-04 | ICD-9 | `5185` | Endoscopic sphincterotomy and papillotomy |
| 2 | 2117-03-04 | ICD-9 | `5187` | Endoscopic insertion of stent (tube) into bile duct |
| 3 | 2117-03-04 | ICD-9 | `5293` | Endoscopic insertion of stent (tube) into pancreatic duct |
| 4 | 2117-03-04 | ICD-9 | `966` | Enteral infusion of concentrated nutritional substances |
| 5 | 2117-03-12 | ICD-9 | `5491` | Percutaneous abdominal drainage |
| 6 | 2117-03-08 | ICD-9 | `9915` | Parenteral infusion of concentrated nutritional substances |
| 7 | 2117-03-08 | ICD-9 | `3893` | Venous catheterization, not elsewhere classified |

### ICU Procedure Events (from `icu/procedureevents.csv.gz`)

- 22 Gauge (category: Access Lines - Peripheral, started: 2117-03-07 23:31:00, status: FinishedRunning)
- Multi Lumen (category: Access Lines - Invasive, started: 2117-03-08 01:14:00, status: FinishedRunning)

## 8. Critical Findings (Charted Events)

- **Dialysis patient** (first noted: 2117-03-07 23:26:00)

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2117-03-03 15:59:00 | Admission | Admitted from CLINIC REFERRAL (DIRECT EMER.) |
| 2117-03-07 23:06:21 | ICU Admission | Surgical Intensive Care Unit (SICU) (LOS: 1.8 days) |
| 2117-03-07 23:06:21 | Transfer | → Surgical Intensive Care Unit (SICU) (transfer) |
| 2117-03-09 18:01:57 | Transfer | → Transplant (transfer) |
| 2117-03-27 16:40:00 | Discharge | To HOME |

## 10. Missing / Ambiguous Data

- No ED registration time — admission may not have gone through ED.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
