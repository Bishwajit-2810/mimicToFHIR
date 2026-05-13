# Encounter Report — HADM 21540783

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 21540783 |
| Subject ID | 10019172 |
| Patient Sex | F |
| Patient Anchor Age (at anchor year) | 63 |
| Anchor Year | 2118 |
| Admission Time | 2118-10-08 14:00:00 |
| Discharge Time | 2118-10-11 20:15:00 |
| Admission Type | ELECTIVE |
| Admission Location | PHYSICIAN REFERRAL |
| Discharge Location | HOME |
| Insurance | Other |
| Language | ENGLISH |
| Marital Status | N/A |
| Race/Ethnicity | UNABLE TO OBTAIN |
| ED Registration | N/A |
| ED Departure | N/A |
| In-Hospital Mortality | No |
| Date of Death (overall) | N/A |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| HCFA | 988 | NON-EXTENSIVE O.R. PROC UNRELATED TO PRINCIPAL DIAGNOSIS W CC | N/A | N/A |
| APR | 952 | NONEXTENSIVE PROCEDURE UNRELATED TO PRINCIPAL DIAGNOSIS | 2.0 | 1.0 |

### Primary Diagnosis (seq_num = 1)

- **ICD-9 4241**: Aortic valve disorders

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2118-10-08 12:37:19 | N/A | CSURG |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-9 `4241`: Aortic valve disorders
- (seq 2) ICD-9 `5990`: Urinary tract infection, site not specified
- (seq 3) ICD-9 `42731`: Atrial fibrillation
- (seq 4) ICD-9 `V5861`: Long-term (current) use of anticoagulants
- (seq 5) ICD-9 `4019`: Unspecified essential hypertension

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-9 | `4241` | Aortic valve disorders |
| 2 | ICD-9 | `5990` | Urinary tract infection, site not specified |
| 3 | ICD-9 | `42731` | Atrial fibrillation |
| 4 | ICD-9 | `V5861` | Long-term (current) use of anticoagulants |
| 5 | ICD-9 | `4019` | Unspecified essential hypertension |
| 6 | ICD-9 | `3051` | Tobacco use disorder |
| 7 | ICD-9 | `4293` | Cardiomegaly |
| 8 | ICD-9 | `78062` | Postprocedural fever |
| 9 | ICD-9 | `5262` | Other cysts of jaws |
| 10 | ICD-9 | `V641` | Surgical or other procedure not carried out because of contraindication |

## 5. ICU Stays

_No ICU stay recorded for this admission._

## 6. Escalation / Severity Indicators

_No escalation indicators detected from ICD codes or ICU procedure events._

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2118-10-09 | ICD-9 | `244` | Excision of dental lesion of jaw |
| 2 | 2118-10-09 | ICD-9 | `2309` | Extraction of other tooth |


## 8. Critical Findings (Charted Events)

_No critical chart events detected._

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2118-10-08 14:00:00 | Admission | Admitted from PHYSICIAN REFERRAL (ELECTIVE) |
| 2118-10-09 15:11:32 | Transfer | → Cardiac Surgery (transfer) |
| 2118-10-11 20:15:00 | Discharge | To HOME |

## 10. Missing / Ambiguous Data

- No ED registration time — admission may not have gone through ED.
- No ICU stay — patient managed on floor/step-down only.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
