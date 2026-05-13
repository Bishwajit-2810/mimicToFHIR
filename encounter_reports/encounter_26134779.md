# Encounter Report — HADM 26134779

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 26134779 |
| Subject ID | 10005866 |
| Patient Sex | M |
| Patient Anchor Age (at anchor year) | 57 |
| Anchor Year | 2146 |
| Admission Time | 2149-09-13 07:36:00 |
| Discharge Time | 2149-09-19 18:00:00 |
| Admission Type | EW EMER. |
| Admission Location | EMERGENCY ROOM |
| Discharge Location | HOME |
| Insurance | Medicaid |
| Language | ENGLISH |
| Marital Status | SINGLE |
| Race/Ethnicity | PORTUGUESE |
| ED Registration | 2149-09-12 15:31:00 |
| ED Departure | 2149-09-13 09:02:00 |
| In-Hospital Mortality | No |
| Date of Death (overall) | 2149-11-21 |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| HCFA | 389 | G.I. OBSTRUCTION W CC | N/A | N/A |
| APR | 247 | INTESTINAL OBSTRUCTION | 2.0 | 2.0 |

### Primary Diagnosis (seq_num = 1)

- **ICD-10 K56600**: Partial intestinal obstruction, unspecified as to cause

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2149-09-13 07:37:37 | N/A | SURG |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-10 `K56600`: Partial intestinal obstruction, unspecified as to cause
- (seq 2) ICD-10 `K766`: Portal hypertension
- (seq 3) ICD-10 `I8510`: Secondary esophageal varices without bleeding
- (seq 4) ICD-10 `K7031`: Alcoholic cirrhosis of liver with ascites
- (seq 5) ICD-10 `F17210`: Nicotine dependence, cigarettes, uncomplicated

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-10 | `K56600` | Partial intestinal obstruction, unspecified as to cause |
| 2 | ICD-10 | `K766` | Portal hypertension |
| 3 | ICD-10 | `I8510` | Secondary esophageal varices without bleeding |
| 4 | ICD-10 | `K7031` | Alcoholic cirrhosis of liver with ascites |
| 5 | ICD-10 | `F17210` | Nicotine dependence, cigarettes, uncomplicated |
| 6 | ICD-10 | `M47818` | Spondylosis without myelopathy or radiculopathy, sacral and sacrococcygeal region |

## 5. ICU Stays

_No ICU stay recorded for this admission._

## 6. Escalation / Severity Indicators

_No escalation indicators detected from ICD codes or ICU procedure events._

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2149-09-17 | ICD-10 | `0W9G3ZZ` | Drainage of Peritoneal Cavity, Percutaneous Approach |


## 8. Critical Findings (Charted Events)

_No critical chart events detected._

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2149-09-12 15:31:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2149-09-12 15:31:00 | Transfer | → Emergency Department (ED) |
| 2149-09-13 07:36:00 | Admission | Admitted from EMERGENCY ROOM (EW EMER.) |
| 2149-09-13 09:02:00 | ED Departure | Left Emergency Dept. |
| 2149-09-19 18:00:00 | Discharge | To HOME |

## 10. Missing / Ambiguous Data

- No ICU stay — patient managed on floor/step-down only.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
