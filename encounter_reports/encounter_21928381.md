# Encounter Report — HADM 21928381

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 21928381 |
| Subject ID | 10021487 |
| Patient Sex | M |
| Patient Anchor Age (at anchor year) | 43 |
| Anchor Year | 2116 |
| Admission Time | 2117-12-03 17:07:00 |
| Discharge Time | 2117-12-06 17:30:00 |
| Admission Type | EW EMER. |
| Admission Location | PROCEDURE SITE |
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
| APR | 721 | POST-OPERATIVE, POST-TRAUMATIC, OTHER DEVICE INFECTIONS | 3.0 | 2.0 |
| HCFA | 862 | POSTOPERATIVE & POST-TRAUMATIC INFECTIONS W MCC | N/A | N/A |

### Primary Diagnosis (seq_num = 1)

- **ICD-9 99859**: Other postoperative infection

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2117-12-03 17:08:29 | N/A | SURG |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-9 `99859`: Other postoperative infection
- (seq 2) ICD-9 `56722`: Peritoneal abscess
- (seq 3) ICD-9 `6822`: Cellulitis and abscess of trunk
- (seq 4) ICD-9 `56981`: Fistula of intestine, excluding rectum and anus
- (seq 5) ICD-9 `E8782`: Surgical operation with anastomosis, bypass, or graft, with natural or artificial tissues used as implant causing abnormal patient reaction, or later complication, without mention of misadventure at time of operation

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-9 | `99859` | Other postoperative infection |
| 2 | ICD-9 | `56722` | Peritoneal abscess |
| 3 | ICD-9 | `6822` | Cellulitis and abscess of trunk |
| 4 | ICD-9 | `56981` | Fistula of intestine, excluding rectum and anus |
| 5 | ICD-9 | `E8782` | Surgical operation with anastomosis, bypass, or graft, with natural or artificial tissues used as implant causing abnormal patient reaction, or later complication, without mention of misadventure at time of operation |
| 6 | ICD-9 | `V4572` | Acquired absence of intestine (large) (small) |
| 7 | ICD-9 | `V453` | Intestinal bypass or anastomosis status |
| 8 | ICD-9 | `V1551` | Personal history of traumatic fracture |
| 9 | ICD-9 | `04185` | Other specified bacterial infections in conditions classified elsewhere and of unspecified site, other gram-negative organisms |
| 10 | ICD-9 | `04109` | Streptococcus infection in conditions classified elsewhere and of unspecified site, other streptococcus |
| 11 | ICD-9 | `04119` | Staphylococcus infection in conditions classified elsewhere and of unspecified site, other staphylococcus |

## 5. ICU Stays

_No ICU stay recorded for this admission._

## 6. Escalation / Severity Indicators

_No escalation indicators detected from ICD codes or ICU procedure events._

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2117-12-03 | ICD-9 | `5491` | Percutaneous abdominal drainage |


## 8. Critical Findings (Charted Events)

_No critical chart events detected._

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2117-12-03 17:07:00 | Admission | Admitted from PROCEDURE SITE (EW EMER.) |
| 2117-12-06 17:30:00 | Discharge | To HOME |

## 10. Missing / Ambiguous Data

- No ED registration time — admission may not have gone through ED.
- No ICU stay — patient managed on floor/step-down only.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
