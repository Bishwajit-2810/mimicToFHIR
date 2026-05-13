# Encounter Report — HADM 24294180

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 24294180 |
| Subject ID | 10039997 |
| Patient Sex | F |
| Patient Anchor Age (at anchor year) | 67 |
| Anchor Year | 2134 |
| Admission Time | 2134-09-07 12:00:00 |
| Discharge Time | 2134-09-11 13:10:00 |
| Admission Type | SURGICAL SAME DAY ADMISSION |
| Admission Location | PHYSICIAN REFERRAL |
| Discharge Location | HOME |
| Insurance | Medicare |
| Language | ENGLISH |
| Marital Status | MARRIED |
| Race/Ethnicity | BLACK/AFRICAN AMERICAN |
| ED Registration | N/A |
| ED Departure | N/A |
| In-Hospital Mortality | No |
| Date of Death (overall) | N/A |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| APR | 21 | CRANIOTOMY EXCEPT FOR TRAUMA | 2.0 | 1.0 |
| HCFA | 27 | CRANIOTOMY & ENDOVASCULAR INTRACRANIAL PROCEDURES W/O CC/MCC | N/A | N/A |

### Primary Diagnosis (seq_num = 1)

- **ICD-9 4373**: Cerebral aneurysm, nonruptured

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2134-09-07 01:14:27 | N/A | NSURG |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-9 `4373`: Cerebral aneurysm, nonruptured
- (seq 2) ICD-9 `43889`: Other late effects of cerebrovascular disease
- (seq 3) ICD-9 `2724`: Other and unspecified hyperlipidemia
- (seq 4) ICD-9 `3051`: Tobacco use disorder
- (seq 5) ICD-9 `32723`: Obstructive sleep apnea (adult)(pediatric)

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-9 | `4373` | Cerebral aneurysm, nonruptured |
| 2 | ICD-9 | `43889` | Other late effects of cerebrovascular disease |
| 3 | ICD-9 | `2724` | Other and unspecified hyperlipidemia |
| 4 | ICD-9 | `3051` | Tobacco use disorder |
| 5 | ICD-9 | `32723` | Obstructive sleep apnea (adult)(pediatric) |
| 6 | ICD-9 | `27800` | Obesity, unspecified |
| 7 | ICD-9 | `72989` | Other musculoskeletal symptoms referable to limbs |
| 8 | ICD-9 | `4019` | Unspecified essential hypertension |
| 9 | ICD-9 | `V8532` | Body Mass Index 32.0-32.9, adult |

## 5. ICU Stays

| Stay ID | First Care Unit | Last Care Unit | ICU Admit | ICU Discharge | LOS (days) |
|---|---|---|---|---|---|
| 36893762 | Surgical Intensive Care Unit (SICU) | Surgical Intensive Care Unit (SICU) | 2134-09-07 18:03:58 | 2134-09-08 22:11:05 | 1.17 |

## 6. Escalation / Severity Indicators

The following critical conditions or interventions were detected:

- **Arterial Line** (ICU procedure event)

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2134-09-07 | ICD-9 | `3951` | Clipping of aneurysm |
| 2 | 2134-09-07 | ICD-9 | `0039` | Other computer assisted surgery |

### ICU Procedure Events (from `icu/procedureevents.csv.gz`)

- Multi Lumen (category: Access Lines - Invasive, started: 2134-09-07 18:32:00, status: FinishedRunning)
- Arterial Line (category: Access Lines - Invasive, started: 2134-09-07 18:33:00, status: FinishedRunning)
- 22 Gauge (category: Access Lines - Peripheral, started: 2134-09-07 18:34:00, status: FinishedRunning)
- Chest X-Ray (category: 5-Imaging, started: 2134-09-07 19:58:00, status: FinishedRunning)
- CT scan (category: 5-Imaging, started: 2134-09-07 20:45:00, status: FinishedRunning)

## 8. Critical Findings (Charted Events)

- **Dialysis patient** (first noted: 2134-09-07 21:25:00)

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2134-09-07 12:00:00 | Admission | Admitted from PHYSICIAN REFERRAL (SURGICAL SAME DAY ADMISSION) |
| 2134-09-07 18:03:58 | ICU Admission | Surgical Intensive Care Unit (SICU) (LOS: 1.2 days) |
| 2134-09-07 18:03:58 | Transfer | → Surgical Intensive Care Unit (SICU) (transfer) |
| 2134-09-08 22:11:05 | Transfer | → Neurology (transfer) |
| 2134-09-11 13:10:00 | Discharge | To HOME |

## 10. Missing / Ambiguous Data

- No ED registration time — admission may not have gone through ED.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
