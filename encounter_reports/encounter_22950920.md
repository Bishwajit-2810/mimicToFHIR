# Encounter Report — HADM 22950920

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 22950920 |
| Subject ID | 10010867 |
| Patient Sex | F |
| Patient Anchor Age (at anchor year) | 28 |
| Anchor Year | 2147 |
| Admission Time | 2148-01-25 22:58:00 |
| Discharge Time | 2148-01-30 11:23:00 |
| Admission Type | OBSERVATION ADMIT |
| Admission Location | EMERGENCY ROOM |
| Discharge Location | REHAB |
| Insurance | Other |
| Language | ENGLISH |
| Marital Status | DIVORCED |
| Race/Ethnicity | WHITE - BRAZILIAN |
| ED Registration | 2148-01-25 18:46:00 |
| ED Departure | 2148-01-26 01:27:00 |
| In-Hospital Mortality | No |
| Date of Death (overall) | N/A |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| HCFA | 458 | SPINAL FUS EXC CERV W SPINAL CURV/MALIG/INFEC OR EXT FUS W/O CC/MCC | N/A | N/A |
| APR | 304 | DORSAL & LUMBAR FUSION PROC EXCEPT FOR CURVATURE OF BACK | 3.0 | 1.0 |

### Primary Diagnosis (seq_num = 1)

- **ICD-10 S22059A**: Unspecified fracture of T5-T6 vertebra, initial encounter for closed fracture

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2148-01-25 22:58:57 | N/A | ORTHO |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-10 `S22059A`: Unspecified fracture of T5-T6 vertebra, initial encounter for closed fracture
- (seq 2) ICD-10 `F329`: Major depressive disorder, single episode, unspecified
- (seq 3) ICD-10 `S22069A`: Unspecified fracture of T7-T8 vertebra, initial encounter for closed fracture
- (seq 4) ICD-10 `V499XXA`: Car occupant (driver) (passenger) injured in unspecified traffic accident, initial encounter
- (seq 5) ICD-10 `Y929`: Unspecified place or not applicable

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-10 | `S22059A` | Unspecified fracture of T5-T6 vertebra, initial encounter for closed fracture |
| 2 | ICD-10 | `F329` | Major depressive disorder, single episode, unspecified |
| 3 | ICD-10 | `S22069A` | Unspecified fracture of T7-T8 vertebra, initial encounter for closed fracture |
| 4 | ICD-10 | `V499XXA` | Car occupant (driver) (passenger) injured in unspecified traffic accident, initial encounter |
| 5 | ICD-10 | `Y929` | Unspecified place or not applicable |
| 6 | ICD-10 | `E669` | Obesity, unspecified |
| 7 | ICD-10 | `Z6833` | Body mass index (BMI) 33.0-33.9, adult |
| 8 | ICD-10 | `Z981` | Arthrodesis status |
| 9 | ICD-10 | `J45909` | Unspecified asthma, uncomplicated |
| 10 | ICD-10 | `G43909` | Migraine, unspecified, not intractable, without status migrainosus |
| 11 | ICD-10 | `F1910` | Other psychoactive substance abuse, uncomplicated |
| 12 | ICD-10 | `M40209` | Unspecified kyphosis, site unspecified |

## 5. ICU Stays

_No ICU stay recorded for this admission._

## 6. Escalation / Severity Indicators

_No escalation indicators detected from ICD codes or ICU procedure events._

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2148-01-26 | ICD-10 | `0RG8071` | Fusion of 8 or more Thoracic Vertebral Joints with Autologous Tissue Substitute, Posterior Approach, Posterior Column, Open Approach |


## 8. Critical Findings (Charted Events)

_No critical chart events detected._

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2148-01-25 18:46:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2148-01-25 18:46:00 | Transfer | → Emergency Department (ED) |
| 2148-01-25 22:58:00 | Admission | Admitted from EMERGENCY ROOM (OBSERVATION ADMIT) |
| 2148-01-26 01:27:00 | ED Departure | Left Emergency Dept. |
| 2148-01-30 11:23:00 | Discharge | To REHAB |

## 10. Missing / Ambiguous Data

- No ICU stay — patient managed on floor/step-down only.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
