# Encounter Report — HADM 25135483

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 25135483 |
| Subject ID | 10007795 |
| Patient Sex | F |
| Patient Anchor Age (at anchor year) | 53 |
| Anchor Year | 2136 |
| Admission Time | 2136-05-04 20:20:00 |
| Discharge Time | 2136-05-12 17:12:00 |
| Admission Type | URGENT |
| Admission Location | TRANSFER FROM HOSPITAL |
| Discharge Location | REHAB |
| Insurance | Medicare |
| Language | ENGLISH |
| Marital Status | SINGLE |
| Race/Ethnicity | WHITE |
| ED Registration | N/A |
| ED Departure | N/A |
| In-Hospital Mortality | No |
| Date of Death (overall) | N/A |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| APR | 260 | MAJOR PANCREAS, LIVER & SHUNT PROCEDURES | 2.0 | 1.0 |
| HCFA | 406 | PANCREAS, LIVER & SHUNT PROCEDURES W CC | N/A | N/A |

### Primary Diagnosis (seq_num = 1)

- **ICD-9 5770**: Acute pancreatitis

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2136-05-04 20:21:47 | N/A | SURG |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-9 `5770`: Acute pancreatitis
- (seq 2) ICD-9 `1179`: Other and unspecified mycoses
- (seq 3) ICD-9 `5772`: Cyst and pseudocyst of pancreas
- (seq 4) ICD-9 `5778`: Other specified diseases of pancreas
- (seq 5) ICD-9 `24900`: Secondary diabetes mellitus without mention of complication, not stated as uncontrolled, or unspecified

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-9 | `5770` | Acute pancreatitis |
| 2 | ICD-9 | `1179` | Other and unspecified mycoses |
| 3 | ICD-9 | `5772` | Cyst and pseudocyst of pancreas |
| 4 | ICD-9 | `5778` | Other specified diseases of pancreas |
| 5 | ICD-9 | `24900` | Secondary diabetes mellitus without mention of complication, not stated as uncontrolled, or unspecified |
| 6 | ICD-9 | `4019` | Unspecified essential hypertension |
| 7 | ICD-9 | `2720` | Pure hypercholesterolemia |
| 8 | ICD-9 | `2859` | Anemia, unspecified |
| 9 | ICD-9 | `V103` | Personal history of malignant neoplasm of breast |
| 10 | ICD-9 | `V4571` | Acquired absence of breast and nipple |
| 11 | ICD-9 | `V8741` | Personal history of antineoplastic chemotherapy |
| 12 | ICD-9 | `30500` | Alcohol abuse, unspecified |

## 5. ICU Stays

_No ICU stay recorded for this admission._

## 6. Escalation / Severity Indicators

_No escalation indicators detected from ICD codes or ICU procedure events._

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2136-05-05 | ICD-9 | `5222` | Other excision or destruction of lesion or tissue of pancreas or pancreatic duct |
| 2 | 2136-05-05 | ICD-9 | `5201` | Drainage of pancreatic cyst by catheter |
| 3 | 2136-05-06 | ICD-9 | `966` | Enteral infusion of concentrated nutritional substances |
| 4 | 2136-05-08 | ICD-9 | `3897` | Central venous catheter placement with guidance |


## 8. Critical Findings (Charted Events)

_No critical chart events detected._

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2136-05-04 20:20:00 | Admission | Admitted from TRANSFER FROM HOSPITAL (URGENT) |
| 2136-05-05 10:44:01 | Transfer | → Discharge Lounge (transfer) |
| 2136-05-05 20:57:25 | Transfer | → Med/Surg (transfer) |
| 2136-05-12 17:12:00 | Discharge | To REHAB |

## 10. Missing / Ambiguous Data

- No ED registration time — admission may not have gone through ED.
- No ICU stay — patient managed on floor/step-down only.

## 11. Manual Review Recommendation

**This encounter is flagged for manual review:**

- Urgent/Emergency admission but no clear escalation indicator found.
