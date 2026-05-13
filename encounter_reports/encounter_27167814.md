# Encounter Report — HADM 27167814

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 27167814 |
| Subject ID | 10005866 |
| Patient Sex | M |
| Patient Anchor Age (at anchor year) | 57 |
| Anchor Year | 2146 |
| Admission Time | 2148-03-10 16:16:00 |
| Discharge Time | 2148-03-21 18:30:00 |
| Admission Type | EW EMER. |
| Admission Location | EMERGENCY ROOM |
| Discharge Location | SKILLED NURSING FACILITY |
| Insurance | Medicaid |
| Language | ENGLISH |
| Marital Status | SINGLE |
| Race/Ethnicity | PORTUGUESE |
| ED Registration | 2148-03-10 04:46:00 |
| ED Departure | 2148-03-10 11:27:00 |
| In-Hospital Mortality | No |
| Date of Death (overall) | 2149-11-21 |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| HCFA | 335 | PERITONEAL ADHESIOLYSIS W MCC | N/A | N/A |
| APR | 224 | PERITONEAL ADHESIOLYSIS | 3.0 | 3.0 |

### Primary Diagnosis (seq_num = 1)

- **ICD-10 K565**: Intestinal adhesions [bands] with obstruction (postinfection)

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2148-03-10 16:18:48 | N/A | SURG |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-10 `K565`: Intestinal adhesions [bands] with obstruction (postinfection)
- (seq 2) ICD-10 `E43`: Unspecified severe protein-calorie malnutrition
- (seq 3) ICD-10 `J189`: Pneumonia, unspecified organism
- (seq 4) ICD-10 `J952`: Acute pulmonary insufficiency following nonthoracic surgery
- (seq 5) ICD-10 `K766`: Portal hypertension

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-10 | `K565` | Intestinal adhesions [bands] with obstruction (postinfection) |
| 2 | ICD-10 | `E43` | Unspecified severe protein-calorie malnutrition |
| 3 | ICD-10 | `J189` | Pneumonia, unspecified organism |
| 4 | ICD-10 | `J952` | Acute pulmonary insufficiency following nonthoracic surgery |
| 5 | ICD-10 | `K766` | Portal hypertension |
| 6 | ICD-10 | `M96831` | Postprocedural hemorrhage of a musculoskeletal structure following other procedure |
| 7 | ICD-10 | `D62` | Acute posthemorrhagic anemia |
| 8 | ICD-10 | `T814XXA` | Infection following a procedure, initial encounter |
| 9 | ICD-10 | `L03311` | Cellulitis of abdominal wall |
| 10 | ICD-10 | `K7031` | Alcoholic cirrhosis of liver with ascites |
| 11 | ICD-10 | `M47817` | Spondylosis without myelopathy or radiculopathy, lumbosacral region |
| 12 | ICD-10 | `Z6823` | Body mass index (BMI) 23.0-23.9, adult |
| 13 | ICD-10 | `F17210` | Nicotine dependence, cigarettes, uncomplicated |
| 14 | ICD-10 | `D696` | Thrombocytopenia, unspecified |
| 15 | ICD-10 | `Y838` | Other surgical procedures as the cause of abnormal reaction of the patient, or of later complication, without mention of misadventure at the time of the procedure |
| 16 | ICD-10 | `Y92239` | Unspecified place in hospital as the place of occurrence of the external cause |
| 17 | ICD-10 | `T17990A` | Other foreign object in respiratory tract, part unspecified in causing asphyxiation, initial encounter |
| 18 | ICD-10 | `R339` | Retention of urine, unspecified |

## 5. ICU Stays

_No ICU stay recorded for this admission._

## 6. Escalation / Severity Indicators

The following critical conditions or interventions were detected:

- **Pneumonia** (ICD diagnosis)

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2148-03-10 | ICD-10 | `0DN80ZZ` | Release Small Intestine, Open Approach |
| 2 | 2148-03-15 | ICD-10 | `0W3F0ZZ` | Control Bleeding in Abdominal Wall, Open Approach |
| 3 | 2148-03-16 | ICD-10 | `0W9G3ZX` | Drainage of Peritoneal Cavity, Percutaneous Approach, Diagnostic |
| 4 | 2148-03-16 | ICD-10 | `0W9G3ZZ` | Drainage of Peritoneal Cavity, Percutaneous Approach |
| 5 | 2148-03-10 | ICD-10 | `5A1935Z` | Respiratory Ventilation, Less than 24 Consecutive Hours |
| 6 | 2148-03-10 | ICD-10 | `0BH17EZ` | Insertion of Endotracheal Airway into Trachea, Via Natural or Artificial Opening |


## 8. Critical Findings (Charted Events)

_No critical chart events detected._

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2148-03-10 04:46:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2148-03-10 04:46:00 | Transfer | → Emergency Department (ED) |
| 2148-03-10 11:27:00 | ED Departure | Left Emergency Dept. |
| 2148-03-10 16:16:00 | Admission | Admitted from EMERGENCY ROOM (EW EMER.) |
| 2148-03-11 14:30:28 | Transfer | → Transplant (transfer) |
| 2148-03-21 18:30:00 | Discharge | To SKILLED NURSING FACILITY |

## 10. Missing / Ambiguous Data

- No ICU stay — patient managed on floor/step-down only.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
