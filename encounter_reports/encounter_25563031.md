# Encounter Report — HADM 25563031

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 25563031 |
| Subject ID | 10001725 |
| Patient Sex | F |
| Patient Anchor Age (at anchor year) | 46 |
| Anchor Year | 2110 |
| Admission Time | 2110-04-11 15:08:00 |
| Discharge Time | 2110-04-14 15:00:00 |
| Admission Type | EW EMER. |
| Admission Location | PACU |
| Discharge Location | HOME |
| Insurance | Other |
| Language | ENGLISH |
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
| APR | 951 | MODERATELY EXTENSIVE PROCEDURE UNRELATED TO PRINCIPAL DIAGNOSIS | 2.0 | 1.0 |
| HCFA | 982 | EXTENSIVE O.R. PROCEDURE UNRELATED TO PRINCIPAL DIAGNOSIS W CC | N/A | N/A |

### Primary Diagnosis (seq_num = 1)

- **ICD-9 78829**: Other specified retention of urine

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2110-04-11 15:09:36 | N/A | GYN |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-9 `78829`: Other specified retention of urine
- (seq 2) ICD-9 `9950`: Other anaphylactic reaction
- (seq 3) ICD-9 `6185`: Prolapse of vaginal vault after hysterectomy
- (seq 4) ICD-9 `49390`: Asthma, unspecified type, unspecified
- (seq 5) ICD-9 `53081`: Esophageal reflux

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-9 | `78829` | Other specified retention of urine |
| 2 | ICD-9 | `9950` | Other anaphylactic reaction |
| 3 | ICD-9 | `6185` | Prolapse of vaginal vault after hysterectomy |
| 4 | ICD-9 | `49390` | Asthma, unspecified type, unspecified |
| 5 | ICD-9 | `53081` | Esophageal reflux |
| 6 | ICD-9 | `30000` | Anxiety state, unspecified |
| 7 | ICD-9 | `311` | Depressive disorder, not elsewhere classified |
| 8 | ICD-9 | `7291` | Myalgia and myositis, unspecified |
| 9 | ICD-9 | `5641` | Irritable bowel syndrome |
| 10 | ICD-9 | `6186` | Vaginal enterocele, congenital or acquired |
| 11 | ICD-9 | `V1041` | Personal history of malignant neoplasm of cervix uteri |
| 12 | ICD-9 | `31401` | Attention deficit disorder with hyperactivity |
| 13 | ICD-9 | `V1582` | Personal history of tobacco use |
| 14 | ICD-9 | `4571` | Other lymphedema |
| 15 | ICD-9 | `3331` | Essential and other specified forms of tremor |
| 16 | ICD-9 | `56400` | Constipation, unspecified |
| 17 | ICD-9 | `E9352` | Other opiates and related narcotics causing adverse effects in therapeutic use |
| 18 | ICD-9 | `78052` | Insomnia, unspecified |

## 5. ICU Stays

| Stay ID | First Care Unit | Last Care Unit | ICU Admit | ICU Discharge | LOS (days) |
|---|---|---|---|---|---|
| 31205490 | Medical/Surgical Intensive Care Unit (MICU/SICU) | Medical/Surgical Intensive Care Unit (MICU/SICU) | 2110-04-11 15:52:22 | 2110-04-12 23:59:56 | 1.34 |

## 6. Escalation / Severity Indicators

_No escalation indicators detected from ICD codes or ICU procedure events._

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2110-04-11 | ICD-9 | `8696` | Insertion or replacement of other neurostimulator pulse generator |
| 2 | 2110-04-11 | ICD-9 | `7055` | Repair of rectocele with graft or prosthesis |
| 3 | 2110-04-11 | ICD-9 | `7094` | Insertion of biological graft |

### ICU Procedure Events (from `icu/procedureevents.csv.gz`)

- 20 Gauge (category: Access Lines - Peripheral, started: 2110-04-11 16:02:00, status: FinishedRunning)

## 8. Critical Findings (Charted Events)

- **Code Status** (first noted: 2110-04-11 16:01:00)
- **Dialysis patient** (first noted: 2110-04-11 18:20:00)

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2110-04-11 15:08:00 | Admission | Admitted from PACU (EW EMER.) |
| 2110-04-11 15:52:22 | ICU Admission | Medical/Surgical Intensive Care Unit (MICU/SICU) (LOS: 1.3 days) |
| 2110-04-11 15:52:22 | Transfer | → Medical/Surgical Intensive Care Unit (MICU/SICU) (transfer) |
| 2110-04-12 23:59:56 | Transfer | → Med/Surg/GYN (transfer) |
| 2110-04-13 19:00:15 | Transfer | → Med/Surg/GYN (transfer) |
| 2110-04-14 15:00:00 | Discharge | To HOME |

## 10. Missing / Ambiguous Data

- No ED registration time — admission may not have gone through ED.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
