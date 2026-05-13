# Encounter Report — HADM 26321862

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 26321862 |
| Subject ID | 10021487 |
| Patient Sex | M |
| Patient Anchor Age (at anchor year) | 43 |
| Anchor Year | 2116 |
| Admission Time | 2117-01-28 00:19:00 |
| Discharge Time | 2117-02-05 15:40:00 |
| Admission Type | EW EMER. |
| Admission Location | EMERGENCY ROOM |
| Discharge Location | HOME |
| Insurance | Other |
| Language | ENGLISH |
| Marital Status | MARRIED |
| Race/Ethnicity | WHITE |
| ED Registration | 2117-01-27 18:19:00 |
| ED Departure | 2117-01-28 01:23:00 |
| In-Hospital Mortality | No |
| Date of Death (overall) | N/A |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| HCFA | 443 | DISORDERS OF LIVER EXCEPT MALIG,CIRR,ALC HEPA W/O CC/MCC | N/A | N/A |
| APR | 279 | HEPATIC COMA & OTHER MAJOR ACUTE LIVER DISORDERS | 3.0 | 1.0 |

### Primary Diagnosis (seq_num = 1)

- **ICD-9 5720**: Abscess of liver

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2117-01-28 00:20:58 | N/A | SURG |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-9 `5720`: Abscess of liver
- (seq 2) ICD-9 `04109`: Streptococcus infection in conditions classified elsewhere and of unspecified site, other streptococcus

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-9 | `5720` | Abscess of liver |
| 2 | ICD-9 | `04109` | Streptococcus infection in conditions classified elsewhere and of unspecified site, other streptococcus |

## 5. ICU Stays

_No ICU stay recorded for this admission._

## 6. Escalation / Severity Indicators

_No escalation indicators detected from ICD codes or ICU procedure events._

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2117-01-29 | ICD-9 | `5091` | Percutaneous aspiration of liver |
| 2 | 2117-02-05 | ICD-9 | `5091` | Percutaneous aspiration of liver |
| 3 | 2117-01-29 | ICD-9 | `9729` | Other nonoperative replacements |
| 4 | 2117-02-05 | ICD-9 | `9729` | Other nonoperative replacements |


## 8. Critical Findings (Charted Events)

_No critical chart events detected._

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2117-01-27 18:19:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2117-01-27 18:19:00 | Transfer | → Emergency Department (ED) |
| 2117-01-28 00:19:00 | Admission | Admitted from EMERGENCY ROOM (EW EMER.) |
| 2117-01-28 01:23:00 | ED Departure | Left Emergency Dept. |
| 2117-02-05 15:40:00 | Discharge | To HOME |

## 10. Missing / Ambiguous Data

- No ICU stay — patient managed on floor/step-down only.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
