# Encounter Report — HADM 26706939

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 26706939 |
| Subject ID | 10018328 |
| Patient Sex | F |
| Patient Anchor Age (at anchor year) | 83 |
| Anchor Year | 2154 |
| Admission Time | 2154-02-05 21:58:00 |
| Discharge Time | 2154-02-09 15:15:00 |
| Admission Type | OBSERVATION ADMIT |
| Admission Location | TRANSFER FROM HOSPITAL |
| Discharge Location | HOME HEALTH CARE |
| Insurance | Other |
| Language | ENGLISH |
| Marital Status | DIVORCED |
| Race/Ethnicity | WHITE |
| ED Registration | 2154-02-05 17:09:00 |
| ED Departure | 2154-02-05 22:54:00 |
| In-Hospital Mortality | No |
| Date of Death (overall) | N/A |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| APR | 204 | SYNCOPE & COLLAPSE | 3.0 | 2.0 |
| HCFA | 312 | SYNCOPE & COLLAPSE | N/A | N/A |

### Primary Diagnosis (seq_num = 1)

- **ICD-10 R55**: Syncope and collapse

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2154-02-05 21:59:20 | N/A | SURG |
| 2154-02-06 19:34:46 | SURG | MED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-10 `R55`: Syncope and collapse
- (seq 2) ICD-10 `I671`: Cerebral aneurysm, nonruptured
- (seq 3) ICD-10 `S2242XA`: Multiple fractures of ribs, left side, initial encounter for closed fracture
- (seq 4) ICD-10 `M4854XA`: Collapsed vertebra, not elsewhere classified, thoracic region, initial encounter for fracture
- (seq 5) ICD-10 `N390`: Urinary tract infection, site not specified

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-10 | `R55` | Syncope and collapse |
| 2 | ICD-10 | `I671` | Cerebral aneurysm, nonruptured |
| 3 | ICD-10 | `S2242XA` | Multiple fractures of ribs, left side, initial encounter for closed fracture |
| 4 | ICD-10 | `M4854XA` | Collapsed vertebra, not elsewhere classified, thoracic region, initial encounter for fracture |
| 5 | ICD-10 | `N390` | Urinary tract infection, site not specified |
| 6 | ICD-10 | `W1830XA` | Fall on same level, unspecified, initial encounter |
| 7 | ICD-10 | `Y92512` | Supermarket, store or market as the place of occurrence of the external cause |
| 8 | ICD-10 | `I10` | Essential (primary) hypertension |
| 9 | ICD-10 | `E780` | Pure hypercholesterolemia |
| 10 | ICD-10 | `G4700` | Insomnia, unspecified |
| 11 | ICD-10 | `E876` | Hypokalemia |
| 12 | ICD-10 | `Z853` | Personal history of malignant neoplasm of breast |

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
| 2154-02-05 17:09:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2154-02-05 17:09:00 | Transfer | → Emergency Department (ED) |
| 2154-02-05 21:58:00 | Admission | Admitted from TRANSFER FROM HOSPITAL (OBSERVATION ADMIT) |
| 2154-02-05 22:54:00 | ED Departure | Left Emergency Dept. |
| 2154-02-06 02:37:27 | Transfer | → Med/Surg (transfer) |
| 2154-02-09 15:15:00 | Discharge | To HOME HEALTH CARE |

## 10. Missing / Ambiguous Data

- No procedure ICD codes — procedures may not have been coded or were minor.
- No ICU stay — patient managed on floor/step-down only.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
