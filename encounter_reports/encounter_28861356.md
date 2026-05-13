# Encounter Report — HADM 28861356

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 28861356 |
| Subject ID | 10018081 |
| Patient Sex | M |
| Patient Anchor Age (at anchor year) | 79 |
| Anchor Year | 2133 |
| Admission Time | 2134-08-02 07:15:00 |
| Discharge Time | 2134-08-13 17:34:00 |
| Admission Type | SURGICAL SAME DAY ADMISSION |
| Admission Location | PHYSICIAN REFERRAL |
| Discharge Location | SKILLED NURSING FACILITY |
| Insurance | Medicare |
| Language | ENGLISH |
| Marital Status | MARRIED |
| Race/Ethnicity | WHITE |
| ED Registration | N/A |
| ED Departure | N/A |
| In-Hospital Mortality | No |
| Date of Death (overall) | 2134-10-28 |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| HCFA | 345 | MINOR SMALL & LARGE BOWEL PROCEDURES W CC | N/A | N/A |
| APR | 223 | OTHER SMALL & LARGE BOWEL PROCEDURES | 2.0 | 2.0 |

### Primary Diagnosis (seq_num = 1)

- **ICD-9 V552**: Attention to ileostomy

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2134-08-02 05:43:11 | N/A | TRAUM |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-9 `V552`: Attention to ileostomy
- (seq 2) ICD-9 `99830`: Disruption of wound, unspecified
- (seq 3) ICD-9 `2930`: Delirium due to conditions classified elsewhere
- (seq 4) ICD-9 `4280`: Congestive heart failure, unspecified
- (seq 5) ICD-9 `5180`: Pulmonary collapse

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-9 | `V552` | Attention to ileostomy |
| 2 | ICD-9 | `99830` | Disruption of wound, unspecified |
| 3 | ICD-9 | `2930` | Delirium due to conditions classified elsewhere |
| 4 | ICD-9 | `4280` | Congestive heart failure, unspecified |
| 5 | ICD-9 | `5180` | Pulmonary collapse |
| 6 | ICD-9 | `53012` | Acute esophagitis |
| 7 | ICD-9 | `53290` | Duodenal ulcer, unspecified as acute or chronic, without hemorrhage or perforation, without mention of obstruction |
| 8 | ICD-9 | `V4572` | Acquired absence of intestine (large) (small) |
| 9 | ICD-9 | `V5861` | Long-term (current) use of anticoagulants |
| 10 | ICD-9 | `4019` | Unspecified essential hypertension |
| 11 | ICD-9 | `E8782` | Surgical operation with anastomosis, bypass, or graft, with natural or artificial tissues used as implant causing abnormal patient reaction, or later complication, without mention of misadventure at time of operation |
| 12 | ICD-9 | `E8497` | Accidents occurring in residential institution |
| 13 | ICD-9 | `53190` | Gastric ulcer, unspecified as acute or chronic, without mention of hemorrhage or perforation, without mention of obstruction |
| 14 | ICD-9 | `2800` | Iron deficiency anemia secondary to blood loss (chronic) |
| 15 | ICD-9 | `V5866` | Long-term (current) use of aspirin |
| 16 | ICD-9 | `7850` | Tachycardia, unspecified |
| 17 | ICD-9 | `V5832` | Encounter for removal of sutures |
| 18 | ICD-9 | `2724` | Other and unspecified hyperlipidemia |

## 5. ICU Stays

| Stay ID | First Care Unit | Last Care Unit | ICU Admit | ICU Discharge | LOS (days) |
|---|---|---|---|---|---|
| 38333427 | Trauma SICU (TSICU) | Trauma SICU (TSICU) | 2134-08-05 14:53:33 | 2134-08-07 17:32:43 | 2.11 |

## 6. Escalation / Severity Indicators

The following critical conditions or interventions were detected:

- **Arterial Line** (ICU procedure event)

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2134-08-02 | ICD-9 | `4651` | Closure of stoma of small intestine |
| 2 | 2134-08-05 | ICD-9 | `4513` | Other endoscopy of small intestine |
| 3 | 2134-08-05 | ICD-9 | `3891` | Arterial catheterization |
| 4 | 2134-08-09 | ICD-9 | `8628` | Nonexcisional debridement of wound, infection or burn |
| 5 | 2134-08-10 | ICD-9 | `3897` | Central venous catheter placement with guidance |
| 6 | 2134-08-12 | ICD-9 | `9357` | Application of other wound dressing |

### ICU Procedure Events (from `icu/procedureevents.csv.gz`)

- 20 Gauge (category: Access Lines - Peripheral, started: 2134-08-05 15:38:00, status: FinishedRunning)
- 18 Gauge (category: Access Lines - Peripheral, started: 2134-08-05 15:42:00, status: FinishedRunning)
- Chest X-Ray (category: 5-Imaging, started: 2134-08-05 15:43:00, status: FinishedRunning)
- Multi Lumen (category: Access Lines - Invasive, started: 2134-08-05 18:00:00, status: FinishedRunning)
- Arterial Line (category: Access Lines - Invasive, started: 2134-08-05 18:23:00, status: FinishedRunning)
- Transthoracic Echo (category: 5-Imaging, started: 2134-08-06 10:27:00, status: FinishedRunning)
- CT scan (category: 5-Imaging, started: 2134-08-06 15:15:00, status: FinishedRunning)

## 8. Critical Findings (Charted Events)

- **Code Status** (first noted: 2134-08-06 22:02:00)
- **Dialysis patient** (first noted: 2134-08-06 08:02:00)

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2134-08-02 07:15:00 | Admission | Admitted from PHYSICIAN REFERRAL (SURGICAL SAME DAY ADMISSION) |
| 2134-08-02 15:05:36 | Transfer | → Med/Surg/Trauma (transfer) |
| 2134-08-03 23:03:01 | Transfer | → Med/Surg/Trauma (transfer) |
| 2134-08-05 14:53:33 | ICU Admission | Trauma SICU (TSICU) (LOS: 2.1 days) |
| 2134-08-05 14:53:33 | Transfer | → Trauma SICU (TSICU) (transfer) |
| 2134-08-07 17:32:43 | Transfer | → Med/Surg/Trauma (transfer) |
| 2134-08-13 17:34:00 | Discharge | To SKILLED NURSING FACILITY |

## 10. Missing / Ambiguous Data

- No ED registration time — admission may not have gone through ED.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
