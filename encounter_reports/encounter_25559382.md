# Encounter Report — HADM 25559382

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 25559382 |
| Subject ID | 10004457 |
| Patient Sex | M |
| Patient Anchor Age (at anchor year) | 65 |
| Anchor Year | 2140 |
| Admission Time | 2148-09-14 14:19:00 |
| Discharge Time | 2148-09-15 12:45:00 |
| Admission Type | DIRECT OBSERVATION |
| Admission Location | PHYSICIAN REFERRAL |
| Discharge Location | N/A |
| Insurance | Medicare |
| Language | ENGLISH |
| Marital Status | DIVORCED |
| Race/Ethnicity | WHITE |
| ED Registration | N/A |
| ED Departure | N/A |
| In-Hospital Mortality | No |
| Date of Death (overall) | N/A |

## 2. Hospital Visit Reason

### Primary Diagnosis (seq_num = 1)

- **ICD-10 I25110**: Atherosclerotic heart disease of native coronary artery with unstable angina pectoris

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2148-09-14 14:19:59 | N/A | CMED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-10 `I25110`: Atherosclerotic heart disease of native coronary artery with unstable angina pectoris
- (seq 2) ICD-10 `Z951`: Presence of aortocoronary bypass graft
- (seq 3) ICD-10 `Z955`: Presence of coronary angioplasty implant and graft
- (seq 4) ICD-10 `I110`: Hypertensive heart disease with heart failure
- (seq 5) ICD-10 `I5022`: Chronic systolic (congestive) heart failure

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-10 | `I25110` | Atherosclerotic heart disease of native coronary artery with unstable angina pectoris |
| 2 | ICD-10 | `Z951` | Presence of aortocoronary bypass graft |
| 3 | ICD-10 | `Z955` | Presence of coronary angioplasty implant and graft |
| 4 | ICD-10 | `I110` | Hypertensive heart disease with heart failure |
| 5 | ICD-10 | `I5022` | Chronic systolic (congestive) heart failure |
| 6 | ICD-10 | `E785` | Hyperlipidemia, unspecified |
| 7 | ICD-10 | `Z8673` | Personal history of transient ischemic attack (TIA), and cerebral infarction without residual deficits |
| 8 | ICD-10 | `Z7902` | Long term (current) use of antithrombotics/antiplatelets |
| 9 | ICD-10 | `R21` | Rash and other nonspecific skin eruption |
| 10 | ICD-10 | `J45909` | Unspecified asthma, uncomplicated |
| 11 | ICD-10 | `I4892` | Unspecified atrial flutter |
| 12 | ICD-10 | `I6522` | Occlusion and stenosis of left carotid artery |
| 13 | ICD-10 | `Z952` | Presence of prosthetic heart valve |
| 14 | ICD-10 | `Z8571` | Personal history of Hodgkin lymphoma |
| 15 | ICD-10 | `Z8546` | Personal history of malignant neoplasm of prostate |
| 16 | ICD-10 | `Z87891` | Personal history of nicotine dependence |
| 17 | ICD-10 | `Z8249` | Family history of ischemic heart disease and other diseases of the circulatory system |

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
| 2148-09-14 14:19:00 | Admission | Admitted from PHYSICIAN REFERRAL (DIRECT OBSERVATION) |
| 2148-09-15 12:45:00 | Discharge | To N/A |

## 10. Missing / Ambiguous Data

- No ED registration time — admission may not have gone through ED.
- Discharge location not recorded.
- No procedure ICD codes — procedures may not have been coded or were minor.
- No ICU stay — patient managed on floor/step-down only.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
