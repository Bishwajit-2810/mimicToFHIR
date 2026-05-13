# Encounter Report — HADM 28723315

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 28723315 |
| Subject ID | 10004457 |
| Patient Sex | M |
| Patient Anchor Age (at anchor year) | 65 |
| Anchor Year | 2140 |
| Admission Time | 2141-08-12 16:02:00 |
| Discharge Time | 2141-08-13 17:47:00 |
| Admission Type | EW EMER. |
| Admission Location | EMERGENCY ROOM |
| Discharge Location | HOME |
| Insurance | Medicare |
| Language | ENGLISH |
| Marital Status | SINGLE |
| Race/Ethnicity | WHITE |
| ED Registration | 2141-08-12 12:08:00 |
| ED Departure | 2141-08-12 17:20:00 |
| In-Hospital Mortality | No |
| Date of Death (overall) | N/A |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| HCFA | 307 | CARDIAC CONGENITAL & VALVULAR DISORDERS W/O MCC | N/A | N/A |
| APR | 200 | CARDIAC STRUCTURAL & VALVULAR DISORDERS | 2.0 | 1.0 |

### Primary Diagnosis (seq_num = 1)

- **ICD-9 4241**: Aortic valve disorders

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2141-08-12 16:03:05 | N/A | CMED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-9 `4241`: Aortic valve disorders
- (seq 2) ICD-9 `41401`: Coronary atherosclerosis of native coronary artery
- (seq 3) ICD-9 `41189`: Other acute and subacute forms of ischemic heart disease, other
- (seq 4) ICD-9 `2749`: Gout, unspecified
- (seq 5) ICD-9 `V4582`: Percutaneous transluminal coronary angioplasty status

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-9 | `4241` | Aortic valve disorders |
| 2 | ICD-9 | `41401` | Coronary atherosclerosis of native coronary artery |
| 3 | ICD-9 | `41189` | Other acute and subacute forms of ischemic heart disease, other |
| 4 | ICD-9 | `2749` | Gout, unspecified |
| 5 | ICD-9 | `V4582` | Percutaneous transluminal coronary angioplasty status |
| 6 | ICD-9 | `V1046` | Personal history of malignant neoplasm of prostate |
| 7 | ICD-9 | `V1079` | Personal history of other lymphatic and hematopoietic neoplasms |
| 8 | ICD-9 | `V4577` | Acquired absence of organ, genital organs |
| 9 | ICD-9 | `V153` | Personal history of irradiation, presenting hazards to health |
| 10 | ICD-9 | `V8741` | Personal history of antineoplastic chemotherapy |
| 11 | ICD-9 | `V4579` | Other acquired absence of organ |
| 12 | ICD-9 | `49390` | Asthma, unspecified type, unspecified |
| 13 | ICD-9 | `V4986` | Do not resuscitate status |

## 5. ICU Stays

_No ICU stay recorded for this admission._

## 6. Escalation / Severity Indicators

_No escalation indicators detected from ICD codes or ICU procedure events._

## 7. Procedures and Interventions

_No ICD-coded procedures recorded._


## 8. Critical Findings (Charted Events)

_No critical chart events detected._

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2141-08-12 12:08:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2141-08-12 12:08:00 | Transfer | → Emergency Department (ED) |
| 2141-08-12 16:02:00 | Admission | Admitted from EMERGENCY ROOM (EW EMER.) |
| 2141-08-12 17:20:00 | ED Departure | Left Emergency Dept. |
| 2141-08-13 17:47:00 | Discharge | To HOME |

## 10. Missing / Ambiguous Data

- No procedure ICD codes — procedures may not have been coded or were minor.
- No ICU stay — patient managed on floor/step-down only.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
