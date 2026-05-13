# Encounter Report — HADM 20291550

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 20291550 |
| Subject ID | 10008454 |
| Patient Sex | F |
| Patient Anchor Age (at anchor year) | 26 |
| Anchor Year | 2110 |
| Admission Time | 2110-11-30 06:31:00 |
| Discharge Time | 2110-12-10 15:53:00 |
| Admission Type | EW EMER. |
| Admission Location | EMERGENCY ROOM |
| Discharge Location | HOME HEALTH CARE |
| Insurance | Other |
| Language | ENGLISH |
| Marital Status | SINGLE |
| Race/Ethnicity | WHITE |
| ED Registration | 2110-11-30 04:45:00 |
| ED Departure | 2110-11-30 08:03:00 |
| In-Hospital Mortality | No |
| Date of Death (overall) | N/A |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| HCFA | 956 | LIMB REATTACHMENT, HIP & FEMUR PROC FOR MULTIPLE SIGNIFICANT TRAUMA | N/A | N/A |
| APR | 912 | MUSCULOSKELETAL & OTHER PROCEDURES FOR MULTIPLE SIGNIFICANT TRAUMA | 4.0 | 4.0 |

### Primary Diagnosis (seq_num = 1)

- **ICD-9 82111**: Open fracture of shaft of femur

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2110-11-30 06:32:14 | N/A | TRAUM |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-9 `82111`: Open fracture of shaft of femur
- (seq 2) ICD-9 `9010`: Injury to thoracic aorta
- (seq 3) ICD-9 `5184`: Acute edema of lung, unspecified
- (seq 4) ICD-9 `80704`: Closed fracture of four ribs
- (seq 5) ICD-9 `5990`: Urinary tract infection, site not specified

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-9 | `82111` | Open fracture of shaft of femur |
| 2 | ICD-9 | `9010` | Injury to thoracic aorta |
| 3 | ICD-9 | `5184` | Acute edema of lung, unspecified |
| 4 | ICD-9 | `80704` | Closed fracture of four ribs |
| 5 | ICD-9 | `5990` | Urinary tract infection, site not specified |
| 6 | ICD-9 | `E8120` | Other motor vehicle traffic accident involving collision with motor vehicle injuring driver of motor vehicle other than motorcycle |
| 7 | ICD-9 | `04104` | Streptococcus infection in conditions classified elsewhere and of unspecified site, streptococcus, group D [Enterococcus] |
| 8 | ICD-9 | `E8495` | Street and highway accidents |
| 9 | ICD-9 | `3051` | Tobacco use disorder |
| 10 | ICD-9 | `27800` | Obesity, unspecified |
| 11 | ICD-9 | `V5861` | Long-term (current) use of anticoagulants |

## 5. ICU Stays

| Stay ID | First Care Unit | Last Care Unit | ICU Admit | ICU Discharge | LOS (days) |
|---|---|---|---|---|---|
| 31959184 | Trauma SICU (TSICU) | Trauma SICU (TSICU) | 2110-11-30 17:11:36 | 2110-12-05 16:48:24 | 4.98 |

## 6. Escalation / Severity Indicators

The following critical conditions or interventions were detected:

- **Arterial Line** (ICU procedure event)

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2110-11-30 | ICD-9 | `7915` | Closed reduction of fracture with internal fixation, femur |

### ICU Procedure Events (from `icu/procedureevents.csv.gz`)

- 16 Gauge (category: Access Lines - Peripheral, started: 2110-11-30 18:36:00, status: FinishedRunning)
- 18 Gauge (category: Access Lines - Peripheral, started: 2110-11-30 18:36:00, status: FinishedRunning)
- Arterial Line (category: Access Lines - Invasive, started: 2110-11-30 18:36:00, status: FinishedRunning)
- Nasal Swab (category: 6-Cultures, started: 2110-11-30 18:42:00, status: FinishedRunning)
- Urine Culture (category: 6-Cultures, started: 2110-11-30 19:03:00, status: FinishedRunning)
- X-ray (category: 5-Imaging, started: 2110-11-30 20:28:00, status: FinishedRunning)
- Family meeting held (category: 7-Communication, started: 2110-12-01 12:32:00, status: FinishedRunning)
- Chest X-Ray (category: 5-Imaging, started: 2110-12-02 05:29:00, status: FinishedRunning)
- Family updated by MD (category: 7-Communication, started: 2110-12-02 13:00:00, status: FinishedRunning)
- Family updated by RN (category: 7-Communication, started: 2110-12-02 13:00:00, status: FinishedRunning)
- CT scan (category: 5-Imaging, started: 2110-12-03 14:00:00, status: FinishedRunning)
- Magnetic Resonance Imaging (category: 5-Imaging, started: 2110-12-04 11:20:00, status: FinishedRunning)
- 20 Gauge (category: Access Lines - Peripheral, started: 2110-12-04 23:00:00, status: FinishedRunning)

## 8. Critical Findings (Charted Events)

- **Code Status** (first noted: 2110-11-30 18:35:00)
- **Seizure Activity** (first noted: 2110-12-05 08:00:00)
- **Dialysis patient** (first noted: 2110-11-30 21:14:00)

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2110-11-30 04:45:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2110-11-30 04:45:00 | Transfer | → Emergency Department (ED) |
| 2110-11-30 06:31:00 | Admission | Admitted from EMERGENCY ROOM (EW EMER.) |
| 2110-11-30 07:24:41 | Transfer | → Med/Surg (transfer) |
| 2110-11-30 08:03:00 | ED Departure | Left Emergency Dept. |
| 2110-11-30 15:13:43 | Transfer | → Med/Surg (transfer) |
| 2110-11-30 17:11:36 | ICU Admission | Trauma SICU (TSICU) (LOS: 5.0 days) |
| 2110-11-30 17:11:36 | Transfer | → Trauma SICU (TSICU) (transfer) |
| 2110-11-30 18:18:45 | Transfer | → Trauma SICU (TSICU) (transfer) |
| 2110-12-05 16:48:24 | Transfer | → Med/Surg/Trauma (transfer) |
| 2110-12-09 00:43:05 | Transfer | → Med/Surg/Trauma (transfer) |
| 2110-12-09 00:58:01 | Transfer | → Med/Surg/Trauma (transfer) |
| 2110-12-10 15:53:00 | Discharge | To HOME HEALTH CARE |

## 10. Missing / Ambiguous Data

- No obvious missing critical fields detected.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
