# Encounter Report — HADM 25826145

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 25826145 |
| Subject ID | 10020740 |
| Patient Sex | M |
| Patient Anchor Age (at anchor year) | 56 |
| Anchor Year | 2150 |
| Admission Time | 2150-06-03 20:12:00 |
| Discharge Time | 2150-06-07 15:05:00 |
| Admission Type | EW EMER. |
| Admission Location | PACU |
| Discharge Location | SKILLED NURSING FACILITY |
| Insurance | Other |
| Language | ENGLISH |
| Marital Status | SINGLE |
| Race/Ethnicity | WHITE |
| ED Registration | N/A |
| ED Departure | N/A |
| In-Hospital Mortality | No |
| Date of Death (overall) | N/A |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| HCFA | 418 | LAPAROSCOPIC CHOLECYSTECTOMY W/O C.D.E. W CC | N/A | N/A |
| APR | 263 | CHOLECYSTECTOMY | 3.0 | 2.0 |

### Primary Diagnosis (seq_num = 1)

- **ICD-9 5770**: Acute pancreatitis

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2150-06-03 20:12:32 | N/A | SURG |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-9 `5770`: Acute pancreatitis
- (seq 2) ICD-9 `75310`: Cystic kidney disease, unspecified
- (seq 3) ICD-9 `5723`: Portal hypertension
- (seq 4) ICD-9 `2875`: Thrombocytopenia, unspecified
- (seq 5) ICD-9 `V4987`: Physical restraints status

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-9 | `5770` | Acute pancreatitis |
| 2 | ICD-9 | `75310` | Cystic kidney disease, unspecified |
| 3 | ICD-9 | `5723` | Portal hypertension |
| 4 | ICD-9 | `2875` | Thrombocytopenia, unspecified |
| 5 | ICD-9 | `V4987` | Physical restraints status |
| 6 | ICD-9 | `45829` | Other iatrogenic hypotension |
| 7 | ICD-9 | `57450` | Calculus of bile duct without mention of cholecystitis, without mention of obstruction |
| 8 | ICD-9 | `25000` | Diabetes mellitus without mention of complication, type II or unspecified type, not stated as uncontrolled |
| 9 | ICD-9 | `29570` | Schizoaffective disorder, unspecified |
| 10 | ICD-9 | `49390` | Asthma, unspecified type, unspecified |
| 11 | ICD-9 | `32723` | Obstructive sleep apnea (adult)(pediatric) |
| 12 | ICD-9 | `5680` | Peritoneal adhesions (postoperative) (postinfection) |
| 13 | ICD-9 | `27652` | Hypovolemia |
| 14 | ICD-9 | `2859` | Anemia, unspecified |
| 15 | ICD-9 | `5531` | Umbilical hernia without mention of obstruction or gangrene |
| 16 | ICD-9 | `311` | Depressive disorder, not elsewhere classified |
| 17 | ICD-9 | `2724` | Other and unspecified hyperlipidemia |
| 18 | ICD-9 | `V5867` | Long-term (current) use of insulin |
| 19 | ICD-9 | `V1204` | Personal history of Methicillin resistant Staphylococcus aureus |
| 20 | ICD-9 | `V4589` | Other postprocedural status |

## 5. ICU Stays

| Stay ID | First Care Unit | Last Care Unit | ICU Admit | ICU Discharge | LOS (days) |
|---|---|---|---|---|---|
| 32145159 | Trauma SICU (TSICU) | Trauma SICU (TSICU) | 2150-06-03 20:12:32 | 2150-06-04 21:05:58 | 1.04 |

## 6. Escalation / Severity Indicators

The following critical conditions or interventions were detected:

- **Liver Failure** (ICD diagnosis)

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2150-06-03 | ICD-9 | `5124` | Laparoscopic partial cholecystectomy |
| 2 | 2150-06-03 | ICD-9 | `5451` | Laparoscopic lysis of peritoneal adhesions |
| 3 | 2150-06-03 | ICD-9 | `5343` | Other laparoscopic umbilical herniorrhaphy |

### ICU Procedure Events (from `icu/procedureevents.csv.gz`)

- 16 Gauge (category: Access Lines - Peripheral, started: 2150-06-03 20:29:00, status: FinishedRunning)
- 18 Gauge (category: Access Lines - Peripheral, started: 2150-06-03 20:29:00, status: FinishedRunning)

## 8. Critical Findings (Charted Events)

_No critical chart events detected._

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2150-06-03 20:12:00 | Admission | Admitted from PACU (EW EMER.) |
| 2150-06-03 20:12:32 | ICU Admission | Trauma SICU (TSICU) (LOS: 1.0 days) |
| 2150-06-04 21:05:58 | Transfer | → Med/Surg (transfer) |
| 2150-06-04 21:12:51 | Transfer | → Med/Surg (transfer) |
| 2150-06-07 15:05:00 | Discharge | To SKILLED NURSING FACILITY |

## 10. Missing / Ambiguous Data

- No ED registration time — admission may not have gone through ED.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
