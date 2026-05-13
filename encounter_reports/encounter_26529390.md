# Encounter Report — HADM 26529390

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 26529390 |
| Subject ID | 10019003 |
| Patient Sex | F |
| Patient Anchor Age (at anchor year) | 65 |
| Anchor Year | 2148 |
| Admission Time | 2155-05-17 00:02:00 |
| Discharge Time | 2155-05-19 18:27:00 |
| Admission Type | DIRECT EMER. |
| Admission Location | PHYSICIAN REFERRAL |
| Discharge Location | HOME |
| Insurance | Other |
| Language | ENGLISH |
| Marital Status | WIDOWED |
| Race/Ethnicity | WHITE |
| ED Registration | 2155-05-17 21:03:00 |
| ED Departure | 2155-05-18 03:03:00 |
| In-Hospital Mortality | No |
| Date of Death (overall) | 2155-12-03 |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| APR | 663 | OTHER ANEMIA & DISORDERS OF BLOOD & BLOOD-FORMING ORGANS | 4.0 | 4.0 |
| HCFA | 987 | NON-EXTENSIVE O.R. PROC UNRELATED TO PRINCIPAL DIAGNOSIS W MCC | N/A | N/A |

### Primary Diagnosis (seq_num = 1)

- **ICD-10 D735**: Infarction of spleen

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2155-05-18 00:03:15 | N/A | OMED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-10 `D735`: Infarction of spleen
- (seq 2) ICD-10 `J9601`: Acute respiratory failure with hypoxia
- (seq 3) ICD-10 `I5033`: Acute on chronic diastolic (congestive) heart failure
- (seq 4) ICD-10 `E883`: Tumor lysis syndrome
- (seq 5) ICD-10 `N179`: Acute kidney failure, unspecified

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-10 | `D735` | Infarction of spleen |
| 2 | ICD-10 | `J9601` | Acute respiratory failure with hypoxia |
| 3 | ICD-10 | `I5033` | Acute on chronic diastolic (congestive) heart failure |
| 4 | ICD-10 | `E883` | Tumor lysis syndrome |
| 5 | ICD-10 | `N179` | Acute kidney failure, unspecified |
| 6 | ICD-10 | `J60` | Coalworker's pneumoconiosis |
| 7 | ICD-10 | `J9811` | Atelectasis |
| 8 | ICD-10 | `J811` | Chronic pulmonary edema |
| 9 | ICD-10 | `M351` | Other overlap syndromes |
| 10 | ICD-10 | `D6959` | Other secondary thrombocytopenia |
| 11 | ICD-10 | `D630` | Anemia in neoplastic disease |
| 12 | ICD-10 | `J449` | Chronic obstructive pulmonary disease, unspecified |
| 13 | ICD-10 | `D469` | Myelodysplastic syndrome, unspecified |
| 14 | ICD-10 | `E119` | Type 2 diabetes mellitus without complications |
| 15 | ICD-10 | `E039` | Hypothyroidism, unspecified |
| 16 | ICD-10 | `E790` | Hyperuricemia without signs of inflammatory arthritis and tophaceous disease |
| 17 | ICD-10 | `G893` | Neoplasm related pain (acute) (chronic) |
| 18 | ICD-10 | `R109` | Unspecified abdominal pain |
| 19 | ICD-10 | `I110` | Hypertensive heart disease with heart failure |
| 20 | ICD-10 | `E785` | Hyperlipidemia, unspecified |
| 21 | ICD-10 | `F329` | Major depressive disorder, single episode, unspecified |
| 22 | ICD-10 | `Z853` | Personal history of malignant neoplasm of breast |
| 23 | ICD-10 | `Z87891` | Personal history of nicotine dependence |
| 24 | ICD-10 | `Z66` | Do not resuscitate |
| 25 | ICD-10 | `N390` | Urinary tract infection, site not specified |
| 26 | ICD-10 | `R161` | Splenomegaly, not elsewhere classified |
| 27 | ICD-10 | `E8339` | Other disorders of phosphorus metabolism |
| 28 | ICD-10 | `K7581` | Nonalcoholic steatohepatitis (NASH) |
| 29 | ICD-10 | `F419` | Anxiety disorder, unspecified |

## 5. ICU Stays

_No ICU stay recorded for this admission._

## 6. Escalation / Severity Indicators

The following critical conditions or interventions were detected:

- **Acute Kidney Injury** (ICD diagnosis)
- **Respiratory Failure** (ICD diagnosis)

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2155-05-18 | ICD-10 | `07DR3ZX` | Extraction of Iliac Bone Marrow, Percutaneous Approach, Diagnostic |
| 2 | 2155-05-28 | ICD-10 | `0B9J8ZX` | Drainage of Left Lower Lung Lobe, Via Natural or Artificial Opening Endoscopic, Diagnostic |
| 3 | 2155-05-28 | ICD-10 | `0B9D8ZX` | Drainage of Right Middle Lung Lobe, Via Natural or Artificial Opening Endoscopic, Diagnostic |
| 4 | 2155-06-12 | ICD-10 | `D7021ZZ` | Beam Radiation of Spleen using Photons 1 - 10 MeV |
| 5 | 2155-06-13 | ICD-10 | `02HV33Z` | Insertion of Infusion Device into Superior Vena Cava, Percutaneous Approach |


## 8. Critical Findings (Charted Events)

_No critical chart events detected._

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2155-05-17 00:02:00 | Admission | Admitted from PHYSICIAN REFERRAL (DIRECT EMER.) |
| 2155-05-17 21:03:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2155-05-17 21:03:00 | Transfer | → Emergency Department (ED) |
| 2155-05-18 00:09:26 | Transfer | → Hematology/Oncology Intermediate (transfer) |
| 2155-05-18 03:03:00 | ED Departure | Left Emergency Dept. |
| 2155-05-18 07:59:12 | Transfer | → Hematology/Oncology Intermediate (transfer) |
| 2155-05-19 18:27:00 | Discharge | To HOME |

## 10. Missing / Ambiguous Data

- No ICU stay — patient managed on floor/step-down only.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
