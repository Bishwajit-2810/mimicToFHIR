# Encounter Report — HADM 28108313

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 28108313 |
| Subject ID | 10004457 |
| Patient Sex | M |
| Patient Anchor Age (at anchor year) | 65 |
| Anchor Year | 2140 |
| Admission Time | 2147-12-19 00:00:00 |
| Discharge Time | 2147-12-21 16:10:00 |
| Admission Type | SURGICAL SAME DAY ADMISSION |
| Admission Location | PHYSICIAN REFERRAL |
| Discharge Location | SKILLED NURSING FACILITY |
| Insurance | Medicare |
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
| HCFA | 39 | EXTRACRANIAL PROCEDURES W/O CC/MCC | N/A | N/A |
| APR | 24 | EXTRACRANIAL VASCULAR PROCEDURES | 2.0 | 1.0 |

### Primary Diagnosis (seq_num = 1)

- **ICD-10 I6521**: Occlusion and stenosis of right carotid artery

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2147-12-19 02:11:29 | N/A | VSURG |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-10 `I6521`: Occlusion and stenosis of right carotid artery
- (seq 2) ICD-10 `I2510`: Atherosclerotic heart disease of native coronary artery without angina pectoris
- (seq 3) ICD-10 `Z955`: Presence of coronary angioplasty implant and graft
- (seq 4) ICD-10 `Z8546`: Personal history of malignant neoplasm of prostate
- (seq 5) ICD-10 `Z8571`: Personal history of Hodgkin lymphoma

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-10 | `I6521` | Occlusion and stenosis of right carotid artery |
| 2 | ICD-10 | `I2510` | Atherosclerotic heart disease of native coronary artery without angina pectoris |
| 3 | ICD-10 | `Z955` | Presence of coronary angioplasty implant and graft |
| 4 | ICD-10 | `Z8546` | Personal history of malignant neoplasm of prostate |
| 5 | ICD-10 | `Z8571` | Personal history of Hodgkin lymphoma |
| 6 | ICD-10 | `E785` | Hyperlipidemia, unspecified |
| 7 | ICD-10 | `Z951` | Presence of aortocoronary bypass graft |
| 8 | ICD-10 | `I081` | Rheumatic disorders of both mitral and tricuspid valves |
| 9 | ICD-10 | `Z952` | Presence of prosthetic heart valve |
| 10 | ICD-10 | `G4733` | Obstructive sleep apnea (adult) (pediatric) |

## 5. ICU Stays

_No ICU stay recorded for this admission._

## 6. Escalation / Severity Indicators

_No escalation indicators detected from ICD codes or ICU procedure events._

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2147-12-19 | ICD-10 | `03CM0ZZ` | Extirpation of Matter from Right External Carotid Artery, Open Approach |
| 2 | 2147-12-19 | ICD-10 | `03UH0KZ` | Supplement Right Common Carotid Artery with Nonautologous Tissue Substitute, Open Approach |
| 3 | 2147-12-19 | ICD-10 | `03UM0KZ` | Supplement Right External Carotid Artery with Nonautologous Tissue Substitute, Open Approach |


## 8. Critical Findings (Charted Events)

_No critical chart events detected._

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2147-12-19 00:00:00 | Admission | Admitted from PHYSICIAN REFERRAL (SURGICAL SAME DAY ADMISSION) |
| 2147-12-19 13:54:28 | Transfer | → Medicine (transfer) |
| 2147-12-21 16:10:00 | Discharge | To SKILLED NURSING FACILITY |

## 10. Missing / Ambiguous Data

- No ED registration time — admission may not have gone through ED.
- No ICU stay — patient managed on floor/step-down only.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
