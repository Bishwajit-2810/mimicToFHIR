# Encounter Report — HADM 25508812

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 25508812 |
| Subject ID | 10019003 |
| Patient Sex | F |
| Patient Anchor Age (at anchor year) | 65 |
| Anchor Year | 2148 |
| Admission Time | 2155-05-22 21:46:00 |
| Discharge Time | 2155-05-30 03:30:00 |
| Admission Type | OBSERVATION ADMIT |
| Admission Location | PHYSICIAN REFERRAL |
| Discharge Location | HOME |
| Insurance | Other |
| Language | ENGLISH |
| Marital Status | WIDOWED |
| Race/Ethnicity | WHITE |
| ED Registration | N/A |
| ED Departure | N/A |
| In-Hospital Mortality | No |
| Date of Death (overall) | 2155-12-03 |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| APR | 144 | RESPIRATORY SIGNS, SYMPTOMS & MINOR DIAGNOSES | 3.0 | 3.0 |
| HCFA | 167 | OTHER RESP SYSTEM O.R. PROCEDURES W CC | N/A | N/A |

### Primary Diagnosis (seq_num = 1)

- **ICD-10 R0902**: Hypoxemia

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2155-05-22 21:47:18 | N/A | OMED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-10 `R0902`: Hypoxemia
- (seq 2) ICD-10 `J90`: Pleural effusion, not elsewhere classified
- (seq 3) ICD-10 `J9811`: Atelectasis
- (seq 4) ICD-10 `J811`: Chronic pulmonary edema
- (seq 5) ICD-10 `Z87891`: Personal history of nicotine dependence

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-10 | `R0902` | Hypoxemia |
| 2 | ICD-10 | `J90` | Pleural effusion, not elsewhere classified |
| 3 | ICD-10 | `J9811` | Atelectasis |
| 4 | ICD-10 | `J811` | Chronic pulmonary edema |
| 5 | ICD-10 | `Z87891` | Personal history of nicotine dependence |
| 6 | ICD-10 | `D469` | Myelodysplastic syndrome, unspecified |
| 7 | ICD-10 | `E790` | Hyperuricemia without signs of inflammatory arthritis and tophaceous disease |
| 8 | ICD-10 | `D735` | Infarction of spleen |
| 9 | ICD-10 | `E785` | Hyperlipidemia, unspecified |
| 10 | ICD-10 | `E119` | Type 2 diabetes mellitus without complications |
| 11 | ICD-10 | `J449` | Chronic obstructive pulmonary disease, unspecified |
| 12 | ICD-10 | `Z66` | Do not resuscitate |
| 13 | ICD-10 | `E039` | Hypothyroidism, unspecified |
| 14 | ICD-10 | `F329` | Major depressive disorder, single episode, unspecified |
| 15 | ICD-10 | `Z853` | Personal history of malignant neoplasm of breast |

## 5. ICU Stays

_No ICU stay recorded for this admission._

## 6. Escalation / Severity Indicators

_No escalation indicators detected from ICD codes or ICU procedure events._

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2155-05-28 | ICD-10 | `0B9J8ZX` | Drainage of Left Lower Lung Lobe, Via Natural or Artificial Opening Endoscopic, Diagnostic |
| 2 | 2155-05-28 | ICD-10 | `0B9D8ZX` | Drainage of Right Middle Lung Lobe, Via Natural or Artificial Opening Endoscopic, Diagnostic |


## 8. Critical Findings (Charted Events)

_No critical chart events detected._

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2155-05-22 21:46:00 | Admission | Admitted from PHYSICIAN REFERRAL (OBSERVATION ADMIT) |
| 2155-05-30 03:30:00 | Discharge | To HOME |

## 10. Missing / Ambiguous Data

- No ED registration time — admission may not have gone through ED.
- No ICU stay — patient managed on floor/step-down only.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
