# Encounter Report — HADM 23488445

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 23488445 |
| Subject ID | 10020786 |
| Patient Sex | F |
| Patient Anchor Age (at anchor year) | 86 |
| Anchor Year | 2189 |
| Admission Time | 2189-06-09 12:45:00 |
| Discharge Time | 2189-06-13 17:20:00 |
| Admission Type | URGENT |
| Admission Location | TRANSFER FROM HOSPITAL |
| Discharge Location | HOME |
| Insurance | Medicare |
| Language | ENGLISH |
| Marital Status | WIDOWED |
| Race/Ethnicity | WHITE |
| ED Registration | N/A |
| ED Departure | N/A |
| In-Hospital Mortality | No |
| Date of Death (overall) | N/A |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| APR | 720 | SEPTICEMIA & DISSEMINATED INFECTIONS | 3.0 | 4.0 |
| HCFA | 871 | SEPTICEMIA OR SEVERE SEPSIS W/O MV >96 HOURS W MCC | N/A | N/A |

### Primary Diagnosis (seq_num = 1)

- **ICD-10 A419**: Sepsis, unspecified organism

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2189-06-09 12:46:30 | N/A | MED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-10 `A419`: Sepsis, unspecified organism
- (seq 2) ICD-10 `R6521`: Severe sepsis with septic shock
- (seq 3) ICD-10 `J189`: Pneumonia, unspecified organism
- (seq 4) ICD-10 `I4891`: Unspecified atrial fibrillation
- (seq 5) ICD-10 `J449`: Chronic obstructive pulmonary disease, unspecified

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-10 | `A419` | Sepsis, unspecified organism |
| 2 | ICD-10 | `R6521` | Severe sepsis with septic shock |
| 3 | ICD-10 | `J189` | Pneumonia, unspecified organism |
| 4 | ICD-10 | `I4891` | Unspecified atrial fibrillation |
| 5 | ICD-10 | `J449` | Chronic obstructive pulmonary disease, unspecified |
| 6 | ICD-10 | `E119` | Type 2 diabetes mellitus without complications |
| 7 | ICD-10 | `Z7901` | Long term (current) use of anticoagulants |
| 8 | ICD-10 | `E785` | Hyperlipidemia, unspecified |
| 9 | ICD-10 | `E039` | Hypothyroidism, unspecified |
| 10 | ICD-10 | `Z66` | Do not resuscitate |
| 11 | ICD-10 | `Z87891` | Personal history of nicotine dependence |
| 12 | ICD-10 | `I10` | Essential (primary) hypertension |
| 13 | ICD-10 | `K649` | Unspecified hemorrhoids |

## 5. ICU Stays

| Stay ID | First Care Unit | Last Care Unit | ICU Admit | ICU Discharge | LOS (days) |
|---|---|---|---|---|---|
| 33683112 | Medical/Surgical Intensive Care Unit (MICU/SICU) | Medical/Surgical Intensive Care Unit (MICU/SICU) | 2189-06-09 12:46:30 | 2189-06-10 22:58:09 | 1.42 |

## 6. Escalation / Severity Indicators

The following critical conditions or interventions were detected:

- **Pneumonia** (ICD diagnosis)
- **Sepsis** (ICD diagnosis)

## 7. Procedures and Interventions

_No ICD-coded procedures recorded._

### ICU Procedure Events (from `icu/procedureevents.csv.gz`)

- Chest X-Ray (category: 5-Imaging, started: 2189-06-09 15:28:00, status: FinishedRunning)
- Urine Culture (category: 6-Cultures, started: 2189-06-09 18:28:00, status: FinishedRunning)
- Nasal Swab (category: 6-Cultures, started: 2189-06-09 18:28:00, status: FinishedRunning)
- 20 Gauge (category: Access Lines - Peripheral, started: 2189-06-09 20:00:00, status: FinishedRunning)

## 8. Critical Findings (Charted Events)

- **Code Status** (first noted: 2189-06-09 13:50:00)
- **Dialysis patient** (first noted: 2189-06-09 13:08:00)

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2189-06-09 12:45:00 | Admission | Admitted from TRANSFER FROM HOSPITAL (URGENT) |
| 2189-06-09 12:46:30 | ICU Admission | Medical/Surgical Intensive Care Unit (MICU/SICU) (LOS: 1.4 days) |
| 2189-06-10 22:58:09 | Transfer | → Med/Surg/GYN (transfer) |
| 2189-06-13 17:20:00 | Discharge | To HOME |

## 10. Missing / Ambiguous Data

- No ED registration time — admission may not have gone through ED.
- No procedure ICD codes — procedures may not have been coded or were minor.

## 11. Manual Review Recommendation

**This encounter is flagged for manual review:**

- ICU stay present but no ICD procedures coded.
