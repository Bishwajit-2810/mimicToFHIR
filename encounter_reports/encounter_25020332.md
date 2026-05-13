# Encounter Report — HADM 25020332

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 25020332 |
| Subject ID | 10021312 |
| Patient Sex | F |
| Patient Anchor Age (at anchor year) | 55 |
| Anchor Year | 2113 |
| Admission Time | 2113-08-16 00:32:00 |
| Discharge Time | 2113-08-18 17:35:00 |
| Admission Type | URGENT |
| Admission Location | TRANSFER FROM HOSPITAL |
| Discharge Location | HOME |
| Insurance | Other |
| Language | ENGLISH |
| Marital Status | N/A |
| Race/Ethnicity | UNKNOWN |
| ED Registration | N/A |
| ED Departure | N/A |
| In-Hospital Mortality | No |
| Date of Death (overall) | N/A |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| APR | 121 | OTHER RESPIRATORY & CHEST PROCEDURES | 1.0 | 1.0 |
| HCFA | 165 | MAJOR CHEST PROCEDURES W/O CC/MCC | N/A | N/A |

### Primary Diagnosis (seq_num = 1)

- **ICD-10 C3402**: Malignant neoplasm of left main bronchus

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2113-08-16 00:34:06 | N/A | MED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-10 `C3402`: Malignant neoplasm of left main bronchus
- (seq 2) ICD-10 `C3401`: Malignant neoplasm of right main bronchus
- (seq 3) ICD-10 `R1310`: Dysphagia, unspecified
- (seq 4) ICD-10 `B379`: Candidiasis, unspecified
- (seq 5) ICD-10 `F329`: Major depressive disorder, single episode, unspecified

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-10 | `C3402` | Malignant neoplasm of left main bronchus |
| 2 | ICD-10 | `C3401` | Malignant neoplasm of right main bronchus |
| 3 | ICD-10 | `R1310` | Dysphagia, unspecified |
| 4 | ICD-10 | `B379` | Candidiasis, unspecified |
| 5 | ICD-10 | `F329` | Major depressive disorder, single episode, unspecified |
| 6 | ICD-10 | `F419` | Anxiety disorder, unspecified |
| 7 | ICD-10 | `F17210` | Nicotine dependence, cigarettes, uncomplicated |
| 8 | ICD-10 | `M797` | Fibromyalgia |
| 9 | ICD-10 | `M5430` | Sciatica, unspecified side |
| 10 | ICD-10 | `Z23` | Encounter for immunization |
| 11 | ICD-10 | `Z8701` | Personal history of pneumonia (recurrent) |

## 5. ICU Stays

_No ICU stay recorded for this admission._

## 6. Escalation / Severity Indicators

_No escalation indicators detected from ICD codes or ICU procedure events._

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2113-08-16 | ICD-10 | `0B538ZZ` | Destruction of Right Main Bronchus, Via Natural or Artificial Opening Endoscopic |
| 2 | 2113-08-16 | ICD-10 | `0B578ZZ` | Destruction of Left Main Bronchus, Via Natural or Artificial Opening Endoscopic |
| 3 | 2113-08-16 | ICD-10 | `0B778DZ` | Dilation of Left Main Bronchus with Intraluminal Device, Via Natural or Artificial Opening Endoscopic |
| 4 | 2113-08-16 | ICD-10 | `0B738DZ` | Dilation of Right Main Bronchus with Intraluminal Device, Via Natural or Artificial Opening Endoscopic |
| 5 | 2113-08-16 | ICD-10 | `0BJ08ZZ` | Inspection of Tracheobronchial Tree, Via Natural or Artificial Opening Endoscopic |
| 6 | 2113-08-16 | ICD-10 | `0BB78ZX` | Excision of Left Main Bronchus, Via Natural or Artificial Opening Endoscopic, Diagnostic |
| 7 | 2113-08-16 | ICD-10 | `0BB38ZX` | Excision of Right Main Bronchus, Via Natural or Artificial Opening Endoscopic, Diagnostic |


## 8. Critical Findings (Charted Events)

_No critical chart events detected._

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2113-08-16 00:32:00 | Admission | Admitted from TRANSFER FROM HOSPITAL (URGENT) |
| 2113-08-18 17:35:00 | Discharge | To HOME |

## 10. Missing / Ambiguous Data

- No ED registration time — admission may not have gone through ED.
- No ICU stay — patient managed on floor/step-down only.

## 11. Manual Review Recommendation

**This encounter is flagged for manual review:**

- Urgent/Emergency admission but no clear escalation indicator found.
