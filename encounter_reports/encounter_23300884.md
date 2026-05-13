# Encounter Report — HADM 23300884

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 23300884 |
| Subject ID | 10014729 |
| Patient Sex | F |
| Patient Anchor Age (at anchor year) | 21 |
| Anchor Year | 2125 |
| Admission Time | 2125-03-19 16:58:00 |
| Discharge Time | 2125-03-28 13:37:00 |
| Admission Type | EW EMER. |
| Admission Location | EMERGENCY ROOM |
| Discharge Location | HOME HEALTH CARE |
| Insurance | Other |
| Language | ENGLISH |
| Marital Status | SINGLE |
| Race/Ethnicity | WHITE - OTHER EUROPEAN |
| ED Registration | 2125-03-19 12:36:00 |
| ED Departure | 2125-03-19 18:45:00 |
| In-Hospital Mortality | No |
| Date of Death (overall) | N/A |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| APR | 711 | POST-OP, POST-TRAUMA, OTHER DEVICE INFECTIONS W O.R. PROCEDURE | 3.0 | 2.0 |
| HCFA | 856 | POSTOPERATIVE OR POST-TRAUMATIC INFECTIONS W O.R. PROC W MCC | N/A | N/A |

### Primary Diagnosis (seq_num = 1)

- **ICD-9 99859**: Other postoperative infection

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2125-03-19 16:59:47 | N/A | VSURG |
| 2125-03-20 10:58:51 | VSURG | CSURG |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-9 `99859`: Other postoperative infection
- (seq 2) ICD-9 `5109`: Empyema without mention of fistula
- (seq 3) ICD-9 `99832`: Disruption of external operation (surgical) wound
- (seq 4) ICD-9 `51189`: Other specified forms of effusion, except tuberculous
- (seq 5) ICD-9 `6822`: Cellulitis and abscess of trunk

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-9 | `99859` | Other postoperative infection |
| 2 | ICD-9 | `5109` | Empyema without mention of fistula |
| 3 | ICD-9 | `99832` | Disruption of external operation (surgical) wound |
| 4 | ICD-9 | `51189` | Other specified forms of effusion, except tuberculous |
| 5 | ICD-9 | `6822` | Cellulitis and abscess of trunk |
| 6 | ICD-9 | `E8782` | Surgical operation with anastomosis, bypass, or graft, with natural or artificial tissues used as implant causing abnormal patient reaction, or later complication, without mention of misadventure at time of operation |
| 7 | ICD-9 | `E8497` | Accidents occurring in residential institution |
| 8 | ICD-9 | `V151` | Personal history of surgery to heart and great vessels, presenting hazards to health |
| 9 | ICD-9 | `V1204` | Personal history of Methicillin resistant Staphylococcus aureus |
| 10 | ICD-9 | `34600` | Migraine with aura, without mention of intractable migraine without mention of status migrainosus |
| 11 | ICD-9 | `04112` | Methicillin resistant Staphylococcus aureus in conditions classified elsewhere and of unspecified site |
| 12 | ICD-9 | `33812` | Acute post-thoracotomy pain |

## 5. ICU Stays

_No ICU stay recorded for this admission._

## 6. Escalation / Severity Indicators

_No escalation indicators detected from ICD codes or ICU procedure events._

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2125-03-20 | ICD-9 | `3403` | Reopening of recent thoracotomy site |
| 2 | 2125-03-24 | ICD-9 | `3452` | Thoracoscopic decortication of lung |
| 3 | 2125-03-20 | ICD-9 | `3404` | Insertion of intercostal catheter for drainage |
| 4 | 2125-03-23 | ICD-9 | `3897` | Central venous catheter placement with guidance |


## 8. Critical Findings (Charted Events)

_No critical chart events detected._

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2125-03-19 12:36:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2125-03-19 12:36:00 | Transfer | → Emergency Department (ED) |
| 2125-03-19 16:58:00 | Admission | Admitted from EMERGENCY ROOM (EW EMER.) |
| 2125-03-19 17:06:15 | Transfer | → Vascular (transfer) |
| 2125-03-19 18:45:00 | ED Departure | Left Emergency Dept. |
| 2125-03-20 10:39:52 | Transfer | → Cardiac Surgery (transfer) |
| 2125-03-20 12:58:37 | Transfer | → Cardiac Surgery (transfer) |
| 2125-03-20 13:04:10 | Transfer | → PACU (transfer) |
| 2125-03-20 18:08:40 | Transfer | → Cardiac Surgery (transfer) |
| 2125-03-21 09:39:19 | Transfer | → Cardiac Surgery (transfer) |
| 2125-03-23 17:15:22 | Transfer | → Cardiac Surgery (transfer) |
| 2125-03-28 13:37:00 | Discharge | To HOME HEALTH CARE |

## 10. Missing / Ambiguous Data

- No ICU stay — patient managed on floor/step-down only.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
