# Encounter Report — HADM 21599196

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 21599196 |
| Subject ID | 10035631 |
| Patient Sex | M |
| Patient Anchor Age (at anchor year) | 63 |
| Anchor Year | 2112 |
| Admission Time | 2116-02-13 11:17:00 |
| Discharge Time | 2116-02-15 17:09:00 |
| Admission Type | DIRECT EMER. |
| Admission Location | PHYSICIAN REFERRAL |
| Discharge Location | HOME |
| Insurance | Other |
| Language | ENGLISH |
| Marital Status | MARRIED |
| Race/Ethnicity | WHITE |
| ED Registration | N/A |
| ED Departure | N/A |
| In-Hospital Mortality | No |
| Date of Death (overall) | 2116-03-12 |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| HCFA | 838 | CHEMO W ACUTE LEUKEMIA AS SDX W CC OR HIGH DOSE CHEMO AGENT | N/A | N/A |
| APR | 681 | OTHER O.R. PROCEDURES FOR LYMPHATIC/HEMATOPOIETIC/OTHER NEOPLASMS | 3.0 | 2.0 |

### Primary Diagnosis (seq_num = 1)

- **ICD-10 Z5111**: Encounter for antineoplastic chemotherapy

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2116-02-13 11:18:04 | N/A | OMED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-10 `Z5111`: Encounter for antineoplastic chemotherapy
- (seq 2) ICD-10 `C9202`: Acute myeloblastic leukemia, in relapse
- (seq 3) ICD-10 `Z9484`: Stem cells transplant status
- (seq 4) ICD-10 `Z853`: Personal history of malignant neoplasm of breast
- (seq 5) ICD-10 `Z87891`: Personal history of nicotine dependence

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-10 | `Z5111` | Encounter for antineoplastic chemotherapy |
| 2 | ICD-10 | `C9202` | Acute myeloblastic leukemia, in relapse |
| 3 | ICD-10 | `Z9484` | Stem cells transplant status |
| 4 | ICD-10 | `Z853` | Personal history of malignant neoplasm of breast |
| 5 | ICD-10 | `Z87891` | Personal history of nicotine dependence |

## 5. ICU Stays

_No ICU stay recorded for this admission._

## 6. Escalation / Severity Indicators

_No escalation indicators detected from ICD codes or ICU procedure events._

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2116-02-13 | ICD-10 | `3E04305` | Introduction of Other Antineoplastic into Central Vein, Percutaneous Approach |
| 2 | 2116-02-13 | ICD-10 | `02H633Z` | Insertion of Infusion Device into Right Atrium, Percutaneous Approach |


## 8. Critical Findings (Charted Events)

_No critical chart events detected._

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2116-02-13 11:17:00 | Admission | Admitted from PHYSICIAN REFERRAL (DIRECT EMER.) |
| 2116-02-15 17:09:00 | Discharge | To HOME |

## 10. Missing / Ambiguous Data

- No ED registration time — admission may not have gone through ED.
- No ICU stay — patient managed on floor/step-down only.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
