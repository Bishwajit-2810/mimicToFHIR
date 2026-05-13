# Encounter Report — HADM 24698912

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 24698912 |
| Subject ID | 10015860 |
| Patient Sex | M |
| Patient Anchor Age (at anchor year) | 53 |
| Anchor Year | 2186 |
| Admission Time | 2192-05-12 07:42:00 |
| Discharge Time | 2192-05-27 18:50:00 |
| Admission Type | EW EMER. |
| Admission Location | PHYSICIAN REFERRAL |
| Discharge Location | SKILLED NURSING FACILITY |
| Insurance | Other |
| Language | ENGLISH |
| Marital Status | SINGLE |
| Race/Ethnicity | WHITE |
| ED Registration | 2192-05-11 16:26:00 |
| ED Departure | 2192-05-12 09:31:00 |
| In-Hospital Mortality | No |
| Date of Death (overall) | N/A |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| APR | 710 | INFECTIOUS & PARASITIC DISEASES INCLUDING HIV W O.R. PROCEDURE | 3.0 | 3.0 |
| HCFA | 853 | INFECTIOUS & PARASITIC DISEASES W O.R. PROCEDURE W MCC | N/A | N/A |

### Primary Diagnosis (seq_num = 1)

- **ICD-10 A419**: Sepsis, unspecified organism

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2192-05-12 07:43:24 | N/A | MED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-10 `A419`: Sepsis, unspecified organism
- (seq 2) ICD-10 `N186`: End stage renal disease
- (seq 3) ICD-10 `M726`: Necrotizing fasciitis
- (seq 4) ICD-10 `E872`: Acidosis
- (seq 5) ICD-10 `I120`: Hypertensive chronic kidney disease with stage 5 chronic kidney disease or end stage renal disease

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-10 | `A419` | Sepsis, unspecified organism |
| 2 | ICD-10 | `N186` | End stage renal disease |
| 3 | ICD-10 | `M726` | Necrotizing fasciitis |
| 4 | ICD-10 | `E872` | Acidosis |
| 5 | ICD-10 | `I120` | Hypertensive chronic kidney disease with stage 5 chronic kidney disease or end stage renal disease |
| 6 | ICD-10 | `E1152` | Type 2 diabetes mellitus with diabetic peripheral angiopathy with gangrene |
| 7 | ICD-10 | `M86171` | Other acute osteomyelitis, right ankle and foot |
| 8 | ICD-10 | `E871` | Hypo-osmolality and hyponatremia |
| 9 | ICD-10 | `B181` | Chronic viral hepatitis B without delta-agent |
| 10 | ICD-10 | `T8249XA` | Other complication of vascular dialysis catheter, initial encounter |
| 11 | ICD-10 | `R6520` | Severe sepsis without septic shock |
| 12 | ICD-10 | `E1122` | Type 2 diabetes mellitus with diabetic chronic kidney disease |
| 13 | ICD-10 | `E1169` | Type 2 diabetes mellitus with other specified complication |
| 14 | ICD-10 | `B954` | Other streptococcus as the cause of diseases classified elsewhere |
| 15 | ICD-10 | `B9689` | Other specified bacterial agents as the cause of diseases classified elsewhere |
| 16 | ICD-10 | `B9561` | Methicillin susceptible Staphylococcus aureus infection as the cause of diseases classified elsewhere |
| 17 | ICD-10 | `B965` | Pseudomonas (aeruginosa) (mallei) (pseudomallei) as the cause of diseases classified elsewhere |
| 18 | ICD-10 | `B966` | Bacteroides fragilis [B. fragilis] as the cause of diseases classified elsewhere |
| 19 | ICD-10 | `Y831` | Surgical operation with implant of artificial internal device as the cause of abnormal reaction of the patient, or of later complication, without mention of misadventure at the time of the procedure |
| 20 | ICD-10 | `Y92230` | Patient room in hospital as the place of occurrence of the external cause |
| 21 | ICD-10 | `E1140` | Type 2 diabetes mellitus with diabetic neuropathy, unspecified |
| 22 | ICD-10 | `E11621` | Type 2 diabetes mellitus with foot ulcer |
| 23 | ICD-10 | `L97514` | Non-pressure chronic ulcer of other part of right foot with necrosis of bone |
| 24 | ICD-10 | `E1165` | Type 2 diabetes mellitus with hyperglycemia |
| 25 | ICD-10 | `D509` | Iron deficiency anemia, unspecified |
| 26 | ICD-10 | `D631` | Anemia in chronic kidney disease |
| 27 | ICD-10 | `E785` | Hyperlipidemia, unspecified |
| 28 | ICD-10 | `D329` | Benign neoplasm of meninges, unspecified |
| 29 | ICD-10 | `F419` | Anxiety disorder, unspecified |
| 30 | ICD-10 | `R488` | Other symbolic dysfunctions |
| 31 | ICD-10 | `Z794` | Long term (current) use of insulin |
| 32 | ICD-10 | `Z89421` | Acquired absence of other right toe(s) |
| 33 | ICD-10 | `Z87891` | Personal history of nicotine dependence |

## 5. ICU Stays

| Stay ID | First Care Unit | Last Care Unit | ICU Admit | ICU Discharge | LOS (days) |
|---|---|---|---|---|---|
| 36734659 | Surgical Intensive Care Unit (SICU) | Surgical Intensive Care Unit (SICU) | 2192-05-12 09:31:00 | 2192-05-13 00:55:45 | 0.64 |

## 6. Escalation / Severity Indicators

The following critical conditions or interventions were detected:

- **Sepsis** (ICD diagnosis)

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2192-05-12 | ICD-10 | `0Y6R0Z0` | Detachment at Right 2nd Toe, Complete, Open Approach |
| 2 | 2192-05-12 | ICD-10 | `0JBQ0ZZ` | Excision of Right Foot Subcutaneous Tissue and Fascia, Open Approach |
| 3 | 2192-05-12 | ICD-10 | `0QBN0ZZ` | Excision of Right Metatarsal, Open Approach |
| 4 | 2192-05-19 | ICD-10 | `0QBN0ZZ` | Excision of Right Metatarsal, Open Approach |
| 5 | 2192-05-16 | ICD-10 | `5A1D70Z` | Performance of Urinary Filtration, Intermittent, Less than 6 Hours Per Day |
| 6 | 2192-05-16 | ICD-10 | `0JH63XZ` | Insertion of Tunneled Vascular Access Device into Chest Subcutaneous Tissue and Fascia, Percutaneous Approach |
| 7 | 2192-05-16 | ICD-10 | `02H633Z` | Insertion of Infusion Device into Right Atrium, Percutaneous Approach |
| 8 | 2192-05-18 | ICD-10 | `0J2TXYZ` | Change Other Device in Trunk Subcutaneous Tissue and Fascia, External Approach |

### ICU Procedure Events (from `icu/procedureevents.csv.gz`)

- 20 Gauge (category: Access Lines - Peripheral, started: 2192-05-12 10:20:00, status: FinishedRunning)
- OR Sent (category: 3-Significant Events, started: 2192-05-12 11:30:00, status: FinishedRunning)
- OR Received (category: 3-Significant Events, started: 2192-05-12 12:51:00, status: FinishedRunning)
- EKG (category: 4-Procedures, started: 2192-05-12 22:00:00, status: FinishedRunning)

## 8. Critical Findings (Charted Events)

- **Dialysis patient** (first noted: 2192-05-12 09:39:00)

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2192-05-11 16:26:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2192-05-11 16:26:00 | Transfer | → Emergency Department (ED) |
| 2192-05-12 07:42:00 | Admission | Admitted from PHYSICIAN REFERRAL (EW EMER.) |
| 2192-05-12 09:31:00 | ED Departure | Left Emergency Dept. |
| 2192-05-12 09:31:00 | ICU Admission | Surgical Intensive Care Unit (SICU) (LOS: 0.6 days) |
| 2192-05-13 00:55:45 | Transfer | → Medicine (transfer) |
| 2192-05-27 18:50:00 | Discharge | To SKILLED NURSING FACILITY |

## 10. Missing / Ambiguous Data

- No obvious missing critical fields detected.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
