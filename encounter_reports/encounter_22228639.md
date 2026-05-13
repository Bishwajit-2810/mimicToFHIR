# Encounter Report — HADM 22228639

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 22228639 |
| Subject ID | 10037928 |
| Patient Sex | F |
| Patient Anchor Age (at anchor year) | 78 |
| Anchor Year | 2175 |
| Admission Time | 2183-08-04 04:04:00 |
| Discharge Time | 2183-08-04 16:07:00 |
| Admission Type | EU OBSERVATION |
| Admission Location | PHYSICIAN REFERRAL |
| Discharge Location | N/A |
| Insurance | Medicare |
| Language | ? |
| Marital Status | WIDOWED |
| Race/Ethnicity | HISPANIC/LATINO - CUBAN |
| ED Registration | 2183-08-03 19:27:00 |
| ED Departure | 2183-08-04 16:07:00 |
| In-Hospital Mortality | No |
| Date of Death (overall) | N/A |

## 2. Hospital Visit Reason

### Primary Diagnosis (seq_num = 1)

- **ICD-10 S2232XA**: Fracture of one rib, left side, initial encounter for closed fracture

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2183-08-04 04:07:05 | N/A | MED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-10 `S2232XA`: Fracture of one rib, left side, initial encounter for closed fracture
- (seq 2) ICD-10 `S22068A`: Other fracture of T7-T8 thoracic vertebra, initial encounter for closed fracture
- (seq 3) ICD-10 `W19XXXA`: Unspecified fall, initial encounter
- (seq 4) ICD-10 `Y929`: Unspecified place or not applicable
- (seq 5) ICD-10 `N390`: Urinary tract infection, site not specified

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-10 | `S2232XA` | Fracture of one rib, left side, initial encounter for closed fracture |
| 2 | ICD-10 | `S22068A` | Other fracture of T7-T8 thoracic vertebra, initial encounter for closed fracture |
| 3 | ICD-10 | `W19XXXA` | Unspecified fall, initial encounter |
| 4 | ICD-10 | `Y929` | Unspecified place or not applicable |
| 5 | ICD-10 | `N390` | Urinary tract infection, site not specified |
| 6 | ICD-10 | `R1012` | Left upper quadrant pain |
| 7 | ICD-10 | `J45909` | Unspecified asthma, uncomplicated |
| 8 | ICD-10 | `E119` | Type 2 diabetes mellitus without complications |
| 9 | ICD-10 | `F419` | Anxiety disorder, unspecified |
| 10 | ICD-10 | `F329` | Major depressive disorder, single episode, unspecified |
| 11 | ICD-10 | `K219` | Gastro-esophageal reflux disease without esophagitis |
| 12 | ICD-10 | `E785` | Hyperlipidemia, unspecified |
| 13 | ICD-10 | `I10` | Essential (primary) hypertension |
| 14 | ICD-10 | `D509` | Iron deficiency anemia, unspecified |
| 15 | ICD-10 | `Z85810` | Personal history of malignant neoplasm of tongue |

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
| 2183-08-03 19:27:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2183-08-03 19:27:00 | Transfer | → Emergency Department (ED) |
| 2183-08-04 04:04:00 | Admission | Admitted from PHYSICIAN REFERRAL (EU OBSERVATION) |
| 2183-08-04 16:07:00 | Discharge | To N/A |
| 2183-08-04 16:07:00 | ED Departure | Left Emergency Dept. |

## 10. Missing / Ambiguous Data

- Discharge location not recorded.
- No procedure ICD codes — procedures may not have been coded or were minor.
- No ICU stay — patient managed on floor/step-down only.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
