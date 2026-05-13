# Encounter Report — HADM 20429160

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 20429160 |
| Subject ID | 10021487 |
| Patient Sex | M |
| Patient Anchor Age (at anchor year) | 43 |
| Anchor Year | 2116 |
| Admission Time | 2117-07-16 07:15:00 |
| Discharge Time | 2117-07-25 12:34:00 |
| Admission Type | ELECTIVE |
| Admission Location | PHYSICIAN REFERRAL |
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
| APR | 260 | MAJOR PANCREAS, LIVER & SHUNT PROCEDURES | 2.0 | 1.0 |
| HCFA | 405 | PANCREAS, LIVER & SHUNT PROCEDURES W MCC | N/A | N/A |

### Primary Diagnosis (seq_num = 1)

- **ICD-9 5720**: Abscess of liver

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2117-07-16 03:24:55 | N/A | SURG |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-9 `5720`: Abscess of liver
- (seq 2) ICD-9 `570`: Acute and subacute necrosis of liver
- (seq 3) ICD-9 `5601`: Paralytic ileus
- (seq 4) ICD-9 `99749`: Other digestive system complications
- (seq 5) ICD-9 `5680`: Peritoneal adhesions (postoperative) (postinfection)

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-9 | `5720` | Abscess of liver |
| 2 | ICD-9 | `570` | Acute and subacute necrosis of liver |
| 3 | ICD-9 | `5601` | Paralytic ileus |
| 4 | ICD-9 | `99749` | Other digestive system complications |
| 5 | ICD-9 | `5680` | Peritoneal adhesions (postoperative) (postinfection) |
| 6 | ICD-9 | `56989` | Other specified disorders of intestine |
| 7 | ICD-9 | `E8788` | Other specified surgical operations and procedures causing abnormal patient reaction, or later complication, without mention of misadventure at time of operation |

## 5. ICU Stays

_No ICU stay recorded for this admission._

## 6. Escalation / Severity Indicators

_No escalation indicators detected from ICD codes or ICU procedure events._

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2117-07-16 | ICD-9 | `5029` | Other destruction of lesion of liver |
| 2 | 2117-07-16 | ICD-9 | `4573` | Open and other right hemicolectomy |
| 3 | 2117-07-16 | ICD-9 | `5459` | Other lysis of peritoneal adhesions |
| 4 | 2117-07-21 | ICD-9 | `3897` | Central venous catheter placement with guidance |


## 8. Critical Findings (Charted Events)

_No critical chart events detected._

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2117-07-16 07:15:00 | Admission | Admitted from PHYSICIAN REFERRAL (ELECTIVE) |
| 2117-07-16 21:12:23 | Transfer | → Transplant (transfer) |
| 2117-07-25 12:34:00 | Discharge | To HOME |

## 10. Missing / Ambiguous Data

- No ED registration time — admission may not have gone through ED.
- No ICU stay — patient managed on floor/step-down only.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
