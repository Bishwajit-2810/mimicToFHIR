# Encounter Report — HADM 24547356

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 24547356 |
| Subject ID | 10026354 |
| Patient Sex | M |
| Patient Anchor Age (at anchor year) | 34 |
| Anchor Year | 2119 |
| Admission Time | 2119-10-26 07:11:00 |
| Discharge Time | 2119-11-06 12:30:00 |
| Admission Type | URGENT |
| Admission Location | TRANSFER FROM HOSPITAL |
| Discharge Location | SKILLED NURSING FACILITY |
| Insurance | Other |
| Language | ? |
| Marital Status | N/A |
| Race/Ethnicity | WHITE |
| ED Registration | 2119-10-26 06:00:00 |
| ED Departure | 2119-10-26 06:37:00 |
| In-Hospital Mortality | No |
| Date of Death (overall) | N/A |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| HCFA | 131 | CRANIAL/FACIAL PROCEDURES W CC/MCC | N/A | N/A |
| APR | 912 | MUSCULOSKELETAL & OTHER PROCEDURES FOR MULTIPLE SIGNIFICANT TRAUMA | 2.0 | 1.0 |

### Primary Diagnosis (seq_num = 1)

- **ICD-10 S0262XA**: Fracture of subcondylar process of mandible, initial encounter for closed fracture

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2119-10-26 07:12:05 | N/A | SURG |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-10 `S0262XA`: Fracture of subcondylar process of mandible, initial encounter for closed fracture
- (seq 2) ICD-10 `S25512A`: Laceration of intercostal blood vessels, left side, initial encounter
- (seq 3) ICD-10 `S36892A`: Contusion of other intra-abdominal organs, initial encounter
- (seq 4) ICD-10 `D696`: Thrombocytopenia, unspecified
- (seq 5) ICD-10 `S030XXA`: Dislocation of jaw, initial encounter

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-10 | `S0262XA` | Fracture of subcondylar process of mandible, initial encounter for closed fracture |
| 2 | ICD-10 | `S25512A` | Laceration of intercostal blood vessels, left side, initial encounter |
| 3 | ICD-10 | `S36892A` | Contusion of other intra-abdominal organs, initial encounter |
| 4 | ICD-10 | `D696` | Thrombocytopenia, unspecified |
| 5 | ICD-10 | `S030XXA` | Dislocation of jaw, initial encounter |
| 6 | ICD-10 | `D649` | Anemia, unspecified |
| 7 | ICD-10 | `F1010` | Alcohol abuse, uncomplicated |
| 8 | ICD-10 | `Y040XXA` | Assault by unarmed brawl or fight, initial encounter |

## 5. ICU Stays

| Stay ID | First Care Unit | Last Care Unit | ICU Admit | ICU Discharge | LOS (days) |
|---|---|---|---|---|---|
| 36091287 | Trauma SICU (TSICU) | Trauma SICU (TSICU) | 2119-10-26 08:33:32 | 2119-10-27 17:50:50 | 1.39 |

## 6. Escalation / Severity Indicators

The following critical conditions or interventions were detected:

- **Arterial Line** (ICU procedure event)
- **Invasive Mechanical Ventilation** (ICU procedure event)

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2119-10-27 | ICD-10 | `0NST04Z` | Reposition Right Mandible with Internal Fixation Device, Open Approach |
| 2 | 2119-10-26 | ICD-10 | `03QY0ZZ` | Repair Upper Artery, Open Approach |
| 3 | 2119-10-27 | ICD-10 | `0NSV35Z` | Reposition Left Mandible with External Fixation Device, Percutaneous Approach |
| 4 | 2119-10-27 | ICD-10 | `0NSS35Z` | Reposition Left Maxilla with External Fixation Device, Percutaneous Approach |

### ICU Procedure Events (from `icu/procedureevents.csv.gz`)

- Invasive Ventilation (category: 2-Ventilation, started: 2119-10-26 08:40:00, status: FinishedRunning)
- Cordis/Introducer (category: Access Lines - Invasive, started: 2119-10-26 08:57:00, status: Stopped)
- Arterial Line (category: Access Lines - Invasive, started: 2119-10-26 08:57:00, status: Stopped)
- Foley Catheter (category: GI/GU, started: 2119-10-26 08:58:00, status: Stopped)
- Extubation (category: 1-Intubation/Extubation, started: 2119-10-26 21:28:00, status: FinishedRunning)
- 20 Gauge (category: Access Lines - Peripheral, started: 2119-10-27 13:00:00, status: FinishedRunning)
- OR Sent (category: 3-Significant Events, started: 2119-10-27 14:40:00, status: FinishedRunning)

## 8. Critical Findings (Charted Events)

- **Ventilator Tank #1** (first noted: 2119-10-26 08:00:00)
- **Ventilator Type** (first noted: 2119-10-26 08:00:00)
- **Ventilator Mode** (first noted: 2119-10-26 08:00:00)
- **Known difficult intubation** (first noted: 2119-10-26 08:00:00)

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2119-10-26 06:00:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2119-10-26 06:00:00 | Transfer | → Emergency Department (ED) |
| 2119-10-26 06:37:00 | ED Departure | Left Emergency Dept. |
| 2119-10-26 07:11:00 | Admission | Admitted from TRANSFER FROM HOSPITAL (URGENT) |
| 2119-10-26 08:33:32 | ICU Admission | Trauma SICU (TSICU) (LOS: 1.4 days) |
| 2119-10-26 08:33:32 | Transfer | → Trauma SICU (TSICU) (transfer) |
| 2119-10-27 17:50:50 | Transfer | → Med/Surg/Trauma (transfer) |
| 2119-10-28 16:23:40 | Transfer | → Med/Surg/Trauma (transfer) |
| 2119-10-28 17:27:54 | Transfer | → Med/Surg/Trauma (transfer) |
| 2119-11-05 20:19:12 | Transfer | → Med/Surg/Trauma (transfer) |
| 2119-11-06 12:30:00 | Discharge | To SKILLED NURSING FACILITY |

## 10. Missing / Ambiguous Data

- No obvious missing critical fields detected.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
