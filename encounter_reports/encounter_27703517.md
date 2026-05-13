# Encounter Report — HADM 27703517

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 27703517 |
| Subject ID | 10001217 |
| Patient Sex | F |
| Patient Anchor Age (at anchor year) | 55 |
| Anchor Year | 2157 |
| Admission Time | 2157-12-18 16:58:00 |
| Discharge Time | 2157-12-24 14:55:00 |
| Admission Type | DIRECT EMER. |
| Admission Location | PHYSICIAN REFERRAL |
| Discharge Location | HOME HEALTH CARE |
| Insurance | Other |
| Language | ? |
| Marital Status | MARRIED |
| Race/Ethnicity | WHITE |
| ED Registration | N/A |
| ED Departure | N/A |
| In-Hospital Mortality | No |
| Date of Death (overall) | N/A |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| APR | 21 | CRANIOTOMY EXCEPT FOR TRAUMA | 3.0 | 2.0 |
| HCFA | 23 | CRANIO W MAJOR DEV IMPL/ACUTE COMPLEX CNS PDX W MCC OR CHEMO IMPLANT | N/A | N/A |

### Primary Diagnosis (seq_num = 1)

- **ICD-9 3240**: Intracranial abscess

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2157-12-18 16:59:25 | N/A | NSURG |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-9 `3240`: Intracranial abscess
- (seq 2) ICD-9 `3485`: Cerebral edema
- (seq 3) ICD-9 `340`: Multiple sclerosis
- (seq 4) ICD-9 `04102`: Streptococcus infection in conditions classified elsewhere and of unspecified site, streptococcus, group B
- (seq 5) ICD-9 `04184`: Other specified bacterial infections in conditions classified elsewhere and of unspecified site, other anaerobes

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-9 | `3240` | Intracranial abscess |
| 2 | ICD-9 | `3485` | Cerebral edema |
| 3 | ICD-9 | `340` | Multiple sclerosis |
| 4 | ICD-9 | `04102` | Streptococcus infection in conditions classified elsewhere and of unspecified site, streptococcus, group B |
| 5 | ICD-9 | `04184` | Other specified bacterial infections in conditions classified elsewhere and of unspecified site, other anaerobes |
| 6 | ICD-9 | `4019` | Unspecified essential hypertension |
| 7 | ICD-9 | `3051` | Tobacco use disorder |

## 5. ICU Stays

| Stay ID | First Care Unit | Last Care Unit | ICU Admit | ICU Discharge | LOS (days) |
|---|---|---|---|---|---|
| 34592300 | Surgical Intensive Care Unit (SICU) | Surgical Intensive Care Unit (SICU) | 2157-12-19 15:42:24 | 2157-12-20 14:27:41 | 0.95 |

## 6. Escalation / Severity Indicators

_No escalation indicators detected from ICD codes or ICU procedure events._

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2157-12-19 | ICD-9 | `0139` | Other incision of brain |

### ICU Procedure Events (from `icu/procedureevents.csv.gz`)

- 20 Gauge (category: Access Lines - Peripheral, started: 2157-12-19 17:41:00, status: Stopped)
- PICC Line (category: Access Lines - Invasive, started: 2157-12-19 17:42:00, status: FinishedRunning)
- CT scan (category: 5-Imaging, started: 2157-12-19 20:19:00, status: FinishedRunning)

## 8. Critical Findings (Charted Events)

- **Code Status.** (first noted: 2157-12-20 06:47:00)

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2157-12-18 16:58:00 | Admission | Admitted from PHYSICIAN REFERRAL (DIRECT EMER.) |
| 2157-12-18 18:23:43 | Transfer | → Neurology (transfer) |
| 2157-12-19 15:42:24 | ICU Admission | Surgical Intensive Care Unit (SICU) (LOS: 0.9 days) |
| 2157-12-19 15:42:24 | Transfer | → Surgical Intensive Care Unit (SICU) (transfer) |
| 2157-12-20 14:27:41 | Transfer | → Neurology (transfer) |
| 2157-12-24 14:55:00 | Discharge | To HOME HEALTH CARE |

## 10. Missing / Ambiguous Data

- No ED registration time — admission may not have gone through ED.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
