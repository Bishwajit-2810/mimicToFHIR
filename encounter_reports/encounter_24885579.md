# Encounter Report — HADM 24885579

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 24885579 |
| Subject ID | 10037928 |
| Patient Sex | F |
| Patient Anchor Age (at anchor year) | 78 |
| Anchor Year | 2175 |
| Admission Time | 2182-04-29 04:29:00 |
| Discharge Time | 2182-05-03 17:20:00 |
| Admission Type | OBSERVATION ADMIT |
| Admission Location | WALK-IN/SELF REFERRAL |
| Discharge Location | HOME |
| Insurance | Medicare |
| Language | ? |
| Marital Status | WIDOWED |
| Race/Ethnicity | HISPANIC/LATINO - CUBAN |
| ED Registration | 2182-04-28 17:25:00 |
| ED Departure | 2182-04-29 07:49:00 |
| In-Hospital Mortality | No |
| Date of Death (overall) | N/A |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| HCFA | 395 | OTHER DIGESTIVE SYSTEM DIAGNOSES W/O CC/MCC | N/A | N/A |
| APR | 254 | OTHER DIGESTIVE SYSTEM DIAGNOSES | 2.0 | 2.0 |

### Primary Diagnosis (seq_num = 1)

- **ICD-10 K3580**: Unspecified acute appendicitis

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2182-04-29 04:30:12 | N/A | SURG |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-10 `K3580`: Unspecified acute appendicitis
- (seq 2) ICD-10 `E1165`: Type 2 diabetes mellitus with hyperglycemia
- (seq 3) ICD-10 `C029`: Malignant neoplasm of tongue, unspecified
- (seq 4) ICD-10 `I10`: Essential (primary) hypertension
- (seq 5) ICD-10 `Z794`: Long term (current) use of insulin

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-10 | `K3580` | Unspecified acute appendicitis |
| 2 | ICD-10 | `E1165` | Type 2 diabetes mellitus with hyperglycemia |
| 3 | ICD-10 | `C029` | Malignant neoplasm of tongue, unspecified |
| 4 | ICD-10 | `I10` | Essential (primary) hypertension |
| 5 | ICD-10 | `Z794` | Long term (current) use of insulin |
| 6 | ICD-10 | `E785` | Hyperlipidemia, unspecified |
| 7 | ICD-10 | `F329` | Major depressive disorder, single episode, unspecified |
| 8 | ICD-10 | `F419` | Anxiety disorder, unspecified |
| 9 | ICD-10 | `D509` | Iron deficiency anemia, unspecified |
| 10 | ICD-10 | `K219` | Gastro-esophageal reflux disease without esophagitis |
| 11 | ICD-10 | `G8929` | Other chronic pain |
| 12 | ICD-10 | `M545` | Low back pain |
| 13 | ICD-10 | `G4700` | Insomnia, unspecified |
| 14 | ICD-10 | `Z8711` | Personal history of peptic ulcer disease |
| 15 | ICD-10 | `Z801` | Family history of malignant neoplasm of trachea, bronchus and lung |
| 16 | ICD-10 | `Z8049` | Family history of malignant neoplasm of other genital organs |

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
| 2182-04-28 17:25:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2182-04-28 17:25:00 | Transfer | → Emergency Department (ED) |
| 2182-04-29 04:29:00 | Admission | Admitted from WALK-IN/SELF REFERRAL (OBSERVATION ADMIT) |
| 2182-04-29 07:49:00 | ED Departure | Left Emergency Dept. |
| 2182-04-29 18:42:30 | Transfer | → Neurology (transfer) |
| 2182-05-02 21:24:25 | Transfer | → Surgery/Trauma (transfer) |
| 2182-05-03 17:20:00 | Discharge | To HOME |

## 10. Missing / Ambiguous Data

- No procedure ICD codes — procedures may not have been coded or were minor.
- No ICU stay — patient managed on floor/step-down only.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
