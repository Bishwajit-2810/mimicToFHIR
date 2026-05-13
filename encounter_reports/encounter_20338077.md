# Encounter Report — HADM 20338077

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 20338077 |
| Subject ID | 10007928 |
| Patient Sex | F |
| Patient Anchor Age (at anchor year) | 59 |
| Anchor Year | 2129 |
| Admission Time | 2129-04-05 22:56:00 |
| Discharge Time | 2129-04-11 17:25:00 |
| Admission Type | EW EMER. |
| Admission Location | EMERGENCY ROOM |
| Discharge Location | HOME |
| Insurance | Other |
| Language | ENGLISH |
| Marital Status | DIVORCED |
| Race/Ethnicity | WHITE |
| ED Registration | 2129-04-05 21:18:00 |
| ED Departure | 2129-04-06 00:25:00 |
| In-Hospital Mortality | No |
| Date of Death (overall) | N/A |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| APR | 241 | PEPTIC ULCER & GASTRITIS | 4.0 | 4.0 |
| HCFA | 377 | G.I. HEMORRHAGE W MCC | N/A | N/A |

### Primary Diagnosis (seq_num = 1)

- **ICD-9 53140**: Chronic or unspecified gastric ulcer with hemorrhage, without mention of obstruction

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2129-04-05 22:57:00 | N/A | MED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-9 `53140`: Chronic or unspecified gastric ulcer with hemorrhage, without mention of obstruction
- (seq 2) ICD-9 `0088`: Intestinal infection due to other organism, not elsewhere classified
- (seq 3) ICD-9 `5070`: Pneumonitis due to inhalation of food or vomitus
- (seq 4) ICD-9 `51881`: Acute respiratory failure
- (seq 5) ICD-9 `0389`: Unspecified septicemia

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-9 | `53140` | Chronic or unspecified gastric ulcer with hemorrhage, without mention of obstruction |
| 2 | ICD-9 | `0088` | Intestinal infection due to other organism, not elsewhere classified |
| 3 | ICD-9 | `5070` | Pneumonitis due to inhalation of food or vomitus |
| 4 | ICD-9 | `51881` | Acute respiratory failure |
| 5 | ICD-9 | `0389` | Unspecified septicemia |
| 6 | ICD-9 | `99592` | Severe sepsis |
| 7 | ICD-9 | `5990` | Urinary tract infection, site not specified |
| 8 | ICD-9 | `2761` | Hyposmolality and/or hyponatremia |
| 9 | ICD-9 | `2764` | Mixed acid-base balance disorder |
| 10 | ICD-9 | `53240` | Chronic or unspecified duodenal ulcer with hemorrhage, without mention of obstruction |
| 11 | ICD-9 | `53010` | Esophagitis, unspecified |
| 12 | ICD-9 | `79902` | Hypoxemia |
| 13 | ICD-9 | `04149` | Other and unspecified Escherichia coli [E. coli] |
| 14 | ICD-9 | `5533` | Diaphragmatic hernia without mention of obstruction or gangrene |
| 15 | ICD-9 | `7904` | Nonspecific elevation of levels of transaminase or lactic acid dehydrogenase [LDH] |
| 16 | ICD-9 | `2769` | Electrolyte and fluid disorders not elsewhere classified |
| 17 | ICD-9 | `28860` | Leukocytosis, unspecified |
| 18 | ICD-9 | `30500` | Alcohol abuse, unspecified |
| 19 | ICD-9 | `3051` | Tobacco use disorder |
| 20 | ICD-9 | `E9353` | Salicylates causing adverse effects in therapeutic use |

## 5. ICU Stays

| Stay ID | First Care Unit | Last Care Unit | ICU Admit | ICU Discharge | LOS (days) |
|---|---|---|---|---|---|
| 35128235 | Medical Intensive Care Unit (MICU) | Medical Intensive Care Unit (MICU) | 2129-04-06 00:25:00 | 2129-04-08 21:02:55 | 2.86 |

## 6. Escalation / Severity Indicators

The following critical conditions or interventions were detected:

- **Respiratory Failure** (ICD diagnosis)
- **Sepsis** (ICD diagnosis)

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2129-04-06 | ICD-9 | `4513` | Other endoscopy of small intestine |

### ICU Procedure Events (from `icu/procedureevents.csv.gz`)

- 18 Gauge (category: Access Lines - Peripheral, started: 2129-04-06 00:08:00, status: FinishedRunning)
- Family updated by RN (category: 7-Communication, started: 2129-04-06 00:08:00, status: FinishedRunning)
- Nasal Swab (category: 6-Cultures, started: 2129-04-06 00:08:00, status: FinishedRunning)
- Blood Cultured (category: 6-Cultures, started: 2129-04-06 02:41:00, status: FinishedRunning)
- Urine Culture (category: 6-Cultures, started: 2129-04-06 02:42:00, status: FinishedRunning)
- 20 Gauge (category: Access Lines - Peripheral, started: 2129-04-06 10:50:00, status: FinishedRunning)
- Endoscopy (category: 4-Procedures, started: 2129-04-06 16:00:00, status: FinishedRunning)
- CT scan (category: 5-Imaging, started: 2129-04-06 22:43:00, status: FinishedRunning)
- Chest X-Ray (category: 5-Imaging, started: 2129-04-08 03:43:00, status: FinishedRunning)

## 8. Critical Findings (Charted Events)

- **Code Status** (first noted: 2129-04-06 00:03:00)
- **Seizure** (first noted: 2129-04-06 13:00:00)
- **Dialysis patient** (first noted: 2129-04-06 00:31:00)

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2129-04-05 21:18:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2129-04-05 21:18:00 | Transfer | → Emergency Department (ED) |
| 2129-04-05 22:56:00 | Admission | Admitted from EMERGENCY ROOM (EW EMER.) |
| 2129-04-06 00:25:00 | ED Departure | Left Emergency Dept. |
| 2129-04-06 00:25:00 | ICU Admission | Medical Intensive Care Unit (MICU) (LOS: 2.9 days) |
| 2129-04-08 21:02:55 | Transfer | → Med/Surg (transfer) |
| 2129-04-11 17:25:00 | Discharge | To HOME |

## 10. Missing / Ambiguous Data

- No obvious missing critical fields detected.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
