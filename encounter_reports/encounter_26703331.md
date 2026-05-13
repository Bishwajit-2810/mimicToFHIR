# Encounter Report — HADM 26703331

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 26703331 |
| Subject ID | 10019003 |
| Patient Sex | F |
| Patient Anchor Age (at anchor year) | 65 |
| Anchor Year | 2148 |
| Admission Time | 2155-06-10 23:09:00 |
| Discharge Time | 2155-06-15 16:30:00 |
| Admission Type | EW EMER. |
| Admission Location | TRANSFER FROM HOSPITAL |
| Discharge Location | HOME HEALTH CARE |
| Insurance | Other |
| Language | ENGLISH |
| Marital Status | WIDOWED |
| Race/Ethnicity | WHITE |
| ED Registration | 2155-06-10 20:37:00 |
| ED Departure | 2155-06-11 01:53:00 |
| In-Hospital Mortality | No |
| Date of Death (overall) | 2155-12-03 |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| APR | 133 | RESPIRATORY FAILURE | 3.0 | 3.0 |
| HCFA | 189 | PULMONARY EDEMA & RESPIRATORY FAILURE | N/A | N/A |

### Primary Diagnosis (seq_num = 1)

- **ICD-10 J9601**: Acute respiratory failure with hypoxia

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2155-06-10 23:10:36 | N/A | OMED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-10 `J9601`: Acute respiratory failure with hypoxia
- (seq 2) ICD-10 `I5033`: Acute on chronic diastolic (congestive) heart failure
- (seq 3) ICD-10 `E883`: Tumor lysis syndrome
- (seq 4) ICD-10 `M351`: Other overlap syndromes
- (seq 5) ICD-10 `N179`: Acute kidney failure, unspecified

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-10 | `J9601` | Acute respiratory failure with hypoxia |
| 2 | ICD-10 | `I5033` | Acute on chronic diastolic (congestive) heart failure |
| 3 | ICD-10 | `E883` | Tumor lysis syndrome |
| 4 | ICD-10 | `M351` | Other overlap syndromes |
| 5 | ICD-10 | `N179` | Acute kidney failure, unspecified |
| 6 | ICD-10 | `N390` | Urinary tract infection, site not specified |
| 7 | ICD-10 | `I110` | Hypertensive heart disease with heart failure |
| 8 | ICD-10 | `G893` | Neoplasm related pain (acute) (chronic) |
| 9 | ICD-10 | `D469` | Myelodysplastic syndrome, unspecified |
| 10 | ICD-10 | `R161` | Splenomegaly, not elsewhere classified |
| 11 | ICD-10 | `D735` | Infarction of spleen |
| 12 | ICD-10 | `E8339` | Other disorders of phosphorus metabolism |
| 13 | ICD-10 | `D630` | Anemia in neoplastic disease |
| 14 | ICD-10 | `D6959` | Other secondary thrombocytopenia |
| 15 | ICD-10 | `E039` | Hypothyroidism, unspecified |
| 16 | ICD-10 | `E785` | Hyperlipidemia, unspecified |
| 17 | ICD-10 | `J449` | Chronic obstructive pulmonary disease, unspecified |
| 18 | ICD-10 | `E119` | Type 2 diabetes mellitus without complications |
| 19 | ICD-10 | `Z853` | Personal history of malignant neoplasm of breast |
| 20 | ICD-10 | `K7581` | Nonalcoholic steatohepatitis (NASH) |
| 21 | ICD-10 | `F329` | Major depressive disorder, single episode, unspecified |
| 22 | ICD-10 | `F419` | Anxiety disorder, unspecified |
| 23 | ICD-10 | `Z87891` | Personal history of nicotine dependence |
| 24 | ICD-10 | `Z66` | Do not resuscitate |

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
| 1 | 2155-06-12 | ICD-10 | `D7021ZZ` | Beam Radiation of Spleen using Photons 1 - 10 MeV |
| 2 | 2155-06-13 | ICD-10 | `02HV33Z` | Insertion of Infusion Device into Superior Vena Cava, Percutaneous Approach |


## 8. Critical Findings (Charted Events)

_No critical chart events detected._

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2155-06-10 20:37:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2155-06-10 20:37:00 | Transfer | → Emergency Department (ED) |
| 2155-06-10 23:09:00 | Admission | Admitted from TRANSFER FROM HOSPITAL (EW EMER.) |
| 2155-06-10 23:51:44 | Transfer | → Hematology/Oncology Intermediate (transfer) |
| 2155-06-11 01:53:00 | ED Departure | Left Emergency Dept. |
| 2155-06-11 21:12:24 | Transfer | → Hematology/Oncology Intermediate (transfer) |
| 2155-06-15 16:30:00 | Discharge | To HOME HEALTH CARE |

## 10. Missing / Ambiguous Data

- No ICU stay — patient managed on floor/step-down only.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
