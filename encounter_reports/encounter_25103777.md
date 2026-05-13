# Encounter Report — HADM 25103777

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 25103777 |
| Subject ID | 10015860 |
| Patient Sex | M |
| Patient Anchor Age (at anchor year) | 53 |
| Anchor Year | 2186 |
| Admission Time | 2192-07-31 16:05:00 |
| Discharge Time | 2192-08-06 16:37:00 |
| Admission Type | OBSERVATION ADMIT |
| Admission Location | TRANSFER FROM SKILLED NURSING FACILITY |
| Discharge Location | SKILLED NURSING FACILITY |
| Insurance | Other |
| Language | ENGLISH |
| Marital Status | SINGLE |
| Race/Ethnicity | WHITE |
| ED Registration | 2192-07-31 11:00:00 |
| ED Departure | 2192-07-31 17:10:00 |
| In-Hospital Mortality | No |
| Date of Death (overall) | N/A |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| APR | 466 | MALFUNCTION, REACTION, COMPLIC OF GENITOURINARY DEVICE OR PROC | 4.0 | 3.0 |
| HCFA | 314 | OTHER CIRCULATORY SYSTEM DIAGNOSES W MCC | N/A | N/A |

### Primary Diagnosis (seq_num = 1)

- **ICD-10 T827XXA**: Infection and inflammatory reaction due to other cardiac and vascular devices, implants and grafts, initial encounter

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2192-07-31 16:06:52 | N/A | MED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-10 `T827XXA`: Infection and inflammatory reaction due to other cardiac and vascular devices, implants and grafts, initial encounter
- (seq 2) ICD-10 `A4102`: Sepsis due to Methicillin resistant Staphylococcus aureus
- (seq 3) ICD-10 `I330`: Acute and subacute infective endocarditis
- (seq 4) ICD-10 `N186`: End stage renal disease
- (seq 5) ICD-10 `I120`: Hypertensive chronic kidney disease with stage 5 chronic kidney disease or end stage renal disease

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-10 | `T827XXA` | Infection and inflammatory reaction due to other cardiac and vascular devices, implants and grafts, initial encounter |
| 2 | ICD-10 | `A4102` | Sepsis due to Methicillin resistant Staphylococcus aureus |
| 3 | ICD-10 | `I330` | Acute and subacute infective endocarditis |
| 4 | ICD-10 | `N186` | End stage renal disease |
| 5 | ICD-10 | `I120` | Hypertensive chronic kidney disease with stage 5 chronic kidney disease or end stage renal disease |
| 6 | ICD-10 | `E1122` | Type 2 diabetes mellitus with diabetic chronic kidney disease |
| 7 | ICD-10 | `E1121` | Type 2 diabetes mellitus with diabetic nephropathy |
| 8 | ICD-10 | `E875` | Hyperkalemia |
| 9 | ICD-10 | `E8770` | Fluid overload, unspecified |
| 10 | ICD-10 | `E785` | Hyperlipidemia, unspecified |
| 11 | ICD-10 | `K5900` | Constipation, unspecified |
| 12 | ICD-10 | `D631` | Anemia in chronic kidney disease |
| 13 | ICD-10 | `L851` | Acquired keratosis [keratoderma] palmaris et plantaris |
| 14 | ICD-10 | `Z992` | Dependence on renal dialysis |
| 15 | ICD-10 | `Z89421` | Acquired absence of other right toe(s) |
| 16 | ICD-10 | `Z794` | Long term (current) use of insulin |
| 17 | ICD-10 | `Z87891` | Personal history of nicotine dependence |

## 5. ICU Stays

_No ICU stay recorded for this admission._

## 6. Escalation / Severity Indicators

The following critical conditions or interventions were detected:

- **Sepsis** (ICD diagnosis)

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2192-07-31 | ICD-10 | `0JPTXXZ` | Removal of Tunneled Vascular Access Device from Trunk Subcutaneous Tissue and Fascia, External Approach |
| 2 | 2192-07-31 | ICD-10 | `02PAX3Z` | Removal of Infusion Device from Heart, External Approach |
| 3 | 2192-08-04 | ICD-10 | `0JH63XZ` | Insertion of Tunneled Vascular Access Device into Chest Subcutaneous Tissue and Fascia, Percutaneous Approach |
| 4 | 2192-08-04 | ICD-10 | `02H633Z` | Insertion of Infusion Device into Right Atrium, Percutaneous Approach |
| 5 | 2192-08-05 | ICD-10 | `5A1D70Z` | Performance of Urinary Filtration, Intermittent, Less than 6 Hours Per Day |


## 8. Critical Findings (Charted Events)

_No critical chart events detected._

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2192-07-31 11:00:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2192-07-31 11:00:00 | Transfer | → Emergency Department (ED) |
| 2192-07-31 16:05:00 | Admission | Admitted from TRANSFER FROM SKILLED NURSING FACILITY (OBSERVATION ADMIT) |
| 2192-07-31 17:10:00 | ED Departure | Left Emergency Dept. |
| 2192-08-06 16:37:00 | Discharge | To SKILLED NURSING FACILITY |

## 10. Missing / Ambiguous Data

- No ICU stay — patient managed on floor/step-down only.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
