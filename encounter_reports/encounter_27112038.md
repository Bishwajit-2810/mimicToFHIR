# Encounter Report — HADM 27112038

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 27112038 |
| Subject ID | 10021487 |
| Patient Sex | M |
| Patient Anchor Age (at anchor year) | 43 |
| Anchor Year | 2116 |
| Admission Time | 2117-10-25 22:22:00 |
| Discharge Time | 2117-10-29 14:40:00 |
| Admission Type | EW EMER. |
| Admission Location | EMERGENCY ROOM |
| Discharge Location | HOME |
| Insurance | Other |
| Language | ENGLISH |
| Marital Status | DIVORCED |
| Race/Ethnicity | WHITE |
| ED Registration | 2117-10-25 15:49:00 |
| ED Departure | 2117-10-25 22:53:00 |
| In-Hospital Mortality | No |
| Date of Death (overall) | N/A |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| APR | 721 | POST-OPERATIVE, POST-TRAUMATIC, OTHER DEVICE INFECTIONS | 2.0 | 2.0 |
| HCFA | 862 | POSTOPERATIVE & POST-TRAUMATIC INFECTIONS W MCC | N/A | N/A |

### Primary Diagnosis (seq_num = 1)

- **ICD-9 99859**: Other postoperative infection

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2117-10-25 22:23:14 | N/A | SURG |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-9 `99859`: Other postoperative infection
- (seq 2) ICD-9 `56722`: Peritoneal abscess
- (seq 3) ICD-9 `04149`: Other and unspecified Escherichia coli [E. coli]
- (seq 4) ICD-9 `04185`: Other specified bacterial infections in conditions classified elsewhere and of unspecified site, other gram-negative organisms
- (seq 5) ICD-9 `V453`: Intestinal bypass or anastomosis status

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-9 | `99859` | Other postoperative infection |
| 2 | ICD-9 | `56722` | Peritoneal abscess |
| 3 | ICD-9 | `04149` | Other and unspecified Escherichia coli [E. coli] |
| 4 | ICD-9 | `04185` | Other specified bacterial infections in conditions classified elsewhere and of unspecified site, other gram-negative organisms |
| 5 | ICD-9 | `V453` | Intestinal bypass or anastomosis status |
| 6 | ICD-9 | `V1551` | Personal history of traumatic fracture |
| 7 | ICD-9 | `E8782` | Surgical operation with anastomosis, bypass, or graft, with natural or artificial tissues used as implant causing abnormal patient reaction, or later complication, without mention of misadventure at time of operation |

## 5. ICU Stays

_No ICU stay recorded for this admission._

## 6. Escalation / Severity Indicators

_No escalation indicators detected from ICD codes or ICU procedure events._

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2117-10-26 | ICD-9 | `5491` | Percutaneous abdominal drainage |


## 8. Critical Findings (Charted Events)

_No critical chart events detected._

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2117-10-25 15:49:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2117-10-25 15:49:00 | Transfer | → Emergency Department (ED) |
| 2117-10-25 22:22:00 | Admission | Admitted from EMERGENCY ROOM (EW EMER.) |
| 2117-10-25 22:53:00 | ED Departure | Left Emergency Dept. |
| 2117-10-29 14:40:00 | Discharge | To HOME |

## 10. Missing / Ambiguous Data

- No ICU stay — patient managed on floor/step-down only.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
