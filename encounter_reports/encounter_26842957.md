# Encounter Report — HADM 26842957

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 26842957 |
| Subject ID | 10020187 |
| Patient Sex | F |
| Patient Anchor Age (at anchor year) | 63 |
| Anchor Year | 2169 |
| Admission Time | 2170-02-24 00:00:00 |
| Discharge Time | 2170-02-25 15:00:00 |
| Admission Type | SURGICAL SAME DAY ADMISSION |
| Admission Location | PHYSICIAN REFERRAL |
| Discharge Location | HOME |
| Insurance | Other |
| Language | ? |
| Marital Status | MARRIED |
| Race/Ethnicity | HISPANIC/LATINO - SALVADORAN |
| ED Registration | N/A |
| ED Departure | N/A |
| In-Hospital Mortality | No |
| Date of Death (overall) | N/A |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| APR | 24 | EXTRACRANIAL VASCULAR PROCEDURES | 2.0 | 1.0 |
| HCFA | 26 | CRANIOTOMY & ENDOVASCULAR INTRACRANIAL PROCEDURES W CC | N/A | N/A |

### Primary Diagnosis (seq_num = 1)

- **ICD-10 I671**: Cerebral aneurysm, nonruptured

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2170-02-24 02:07:13 | N/A | NSURG |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-10 `I671`: Cerebral aneurysm, nonruptured
- (seq 2) ICD-10 `Z6841`: Body mass index (BMI) 40.0-44.9, adult
- (seq 3) ICD-10 `I10`: Essential (primary) hypertension
- (seq 4) ICD-10 `E785`: Hyperlipidemia, unspecified
- (seq 5) ICD-10 `E669`: Obesity, unspecified

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-10 | `I671` | Cerebral aneurysm, nonruptured |
| 2 | ICD-10 | `Z6841` | Body mass index (BMI) 40.0-44.9, adult |
| 3 | ICD-10 | `I10` | Essential (primary) hypertension |
| 4 | ICD-10 | `E785` | Hyperlipidemia, unspecified |
| 5 | ICD-10 | `E669` | Obesity, unspecified |
| 6 | ICD-10 | `M1712` | Unilateral primary osteoarthritis, left knee |
| 7 | ICD-10 | `Z96651` | Presence of right artificial knee joint |
| 8 | ICD-10 | `K2270` | Barrett's esophagus without dysplasia |
| 9 | ICD-10 | `Z7902` | Long term (current) use of antithrombotics/antiplatelets |

## 5. ICU Stays

| Stay ID | First Care Unit | Last Care Unit | ICU Admit | ICU Discharge | LOS (days) |
|---|---|---|---|---|---|
| 32554129 | Neuro Intermediate | Neuro Intermediate | 2170-02-24 18:18:46 | 2170-02-25 15:15:26 | 0.87 |

## 6. Escalation / Severity Indicators

The following critical conditions or interventions were detected:

- **Arterial Line** (ICU procedure event)

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2170-02-24 | ICD-10 | `03VG3DZ` | Restriction of Intracranial Artery with Intraluminal Device, Percutaneous Approach |

### ICU Procedure Events (from `icu/procedureevents.csv.gz`)

- Arterial Line (category: Access Lines - Invasive, started: 2170-02-24 18:27:00, status: FinishedRunning)
- 18 Gauge (category: Access Lines - Peripheral, started: 2170-02-24 18:28:00, status: FinishedRunning)
- Foley Catheter (category: GI/GU, started: 2170-02-24 18:38:00, status: FinishedRunning)

## 8. Critical Findings (Charted Events)

- **Dialysis patient** (first noted: 2170-02-24 18:33:00)

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2170-02-24 00:00:00 | Admission | Admitted from PHYSICIAN REFERRAL (SURGICAL SAME DAY ADMISSION) |
| 2170-02-24 18:18:46 | ICU Admission | Neuro Intermediate (LOS: 0.9 days) |
| 2170-02-24 18:18:46 | Transfer | → Neuro Intermediate (transfer) |
| 2170-02-25 15:00:00 | Discharge | To HOME |

## 10. Missing / Ambiguous Data

- No ED registration time — admission may not have gone through ED.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
