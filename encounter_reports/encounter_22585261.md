# Encounter Report — HADM 22585261

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 22585261 |
| Subject ID | 10019917 |
| Patient Sex | M |
| Patient Anchor Age (at anchor year) | 44 |
| Anchor Year | 2182 |
| Admission Time | 2182-01-07 23:25:00 |
| Discharge Time | 2182-01-10 16:52:00 |
| Admission Type | URGENT |
| Admission Location | TRANSFER FROM HOSPITAL |
| Discharge Location | HOME |
| Insurance | Other |
| Language | ENGLISH |
| Marital Status | SINGLE |
| Race/Ethnicity | OTHER |
| ED Registration | N/A |
| ED Departure | N/A |
| In-Hospital Mortality | No |
| Date of Death (overall) | N/A |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| APR | 241 | PEPTIC ULCER & GASTRITIS | 1.0 | 1.0 |
| HCFA | 378 | G.I. HEMORRHAGE W CC | N/A | N/A |

### Primary Diagnosis (seq_num = 1)

- **ICD-9 53240**: Chronic or unspecified duodenal ulcer with hemorrhage, without mention of obstruction

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2182-01-07 23:26:32 | N/A | MED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-9 `53240`: Chronic or unspecified duodenal ulcer with hemorrhage, without mention of obstruction
- (seq 2) ICD-9 `2851`: Acute posthemorrhagic anemia
- (seq 3) ICD-9 `7200`: Ankylosing spondylitis
- (seq 4) ICD-9 `53560`: Duodenitis, without mention of hemorrhage

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-9 | `53240` | Chronic or unspecified duodenal ulcer with hemorrhage, without mention of obstruction |
| 2 | ICD-9 | `2851` | Acute posthemorrhagic anemia |
| 3 | ICD-9 | `7200` | Ankylosing spondylitis |
| 4 | ICD-9 | `53560` | Duodenitis, without mention of hemorrhage |

## 5. ICU Stays

| Stay ID | First Care Unit | Last Care Unit | ICU Admit | ICU Discharge | LOS (days) |
|---|---|---|---|---|---|
| 34324099 | Medical Intensive Care Unit (MICU) | Medical Intensive Care Unit (MICU) | 2182-01-07 23:26:32 | 2182-01-09 07:09:31 | 1.32 |

## 6. Escalation / Severity Indicators

_No escalation indicators detected from ICD codes or ICU procedure events._

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2182-01-09 | ICD-9 | `4516` | Esophagogastroduodenoscopy [EGD] with closed biopsy |
| 2 | 2182-01-09 | ICD-9 | `4523` | Colonoscopy |

### ICU Procedure Events (from `icu/procedureevents.csv.gz`)

- 20 Gauge (category: Access Lines - Peripheral, started: 2182-01-07 23:55:00, status: FinishedRunning)
- 22 Gauge (category: Access Lines - Peripheral, started: 2182-01-08 22:00:00, status: FinishedRunning)

## 8. Critical Findings (Charted Events)

- **Code Status** (first noted: 2182-01-07 23:33:00)

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2182-01-07 23:25:00 | Admission | Admitted from TRANSFER FROM HOSPITAL (URGENT) |
| 2182-01-07 23:26:32 | ICU Admission | Medical Intensive Care Unit (MICU) (LOS: 1.3 days) |
| 2182-01-09 07:09:31 | Transfer | → Medicine (transfer) |
| 2182-01-10 16:52:00 | Discharge | To HOME |

## 10. Missing / Ambiguous Data

- No ED registration time — admission may not have gone through ED.

## 11. Manual Review Recommendation

**This encounter is flagged for manual review:**

- Urgent/Emergency admission but no clear escalation indicator found.
