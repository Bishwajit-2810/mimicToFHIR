# Encounter Report — HADM 28829452

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 28829452 |
| Subject ID | 10021312 |
| Patient Sex | F |
| Patient Anchor Age (at anchor year) | 55 |
| Anchor Year | 2113 |
| Admission Time | 2113-09-12 14:42:00 |
| Discharge Time | 2113-09-20 18:40:00 |
| Admission Type | URGENT |
| Admission Location | TRANSFER FROM HOSPITAL |
| Discharge Location | ACUTE HOSPITAL |
| Insurance | Other |
| Language | ENGLISH |
| Marital Status | N/A |
| Race/Ethnicity | UNKNOWN |
| ED Registration | N/A |
| ED Departure | N/A |
| In-Hospital Mortality | No |
| Date of Death (overall) | N/A |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| APR | 121 | OTHER RESPIRATORY & CHEST PROCEDURES | 2.0 | 2.0 |
| HCFA | 163 | MAJOR CHEST PROCEDURES W MCC | N/A | N/A |

### Primary Diagnosis (seq_num = 1)

- **ICD-10 J9601**: Acute respiratory failure with hypoxia

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2113-09-12 14:44:10 | N/A | MED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-10 `J9601`: Acute respiratory failure with hypoxia
- (seq 2) ICD-10 `J690`: Pneumonitis due to inhalation of food and vomit
- (seq 3) ICD-10 `C3490`: Malignant neoplasm of unspecified part of unspecified bronchus or lung
- (seq 4) ICD-10 `B370`: Candidal stomatitis
- (seq 5) ICD-10 `J9809`: Other diseases of bronchus, not elsewhere classified

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-10 | `J9601` | Acute respiratory failure with hypoxia |
| 2 | ICD-10 | `J690` | Pneumonitis due to inhalation of food and vomit |
| 3 | ICD-10 | `C3490` | Malignant neoplasm of unspecified part of unspecified bronchus or lung |
| 4 | ICD-10 | `B370` | Candidal stomatitis |
| 5 | ICD-10 | `J9809` | Other diseases of bronchus, not elsewhere classified |
| 6 | ICD-10 | `R1319` | Other dysphagia |
| 7 | ICD-10 | `K222` | Esophageal obstruction |
| 8 | ICD-10 | `B9562` | Methicillin resistant Staphylococcus aureus infection as the cause of diseases classified elsewhere |
| 9 | ICD-10 | `F329` | Major depressive disorder, single episode, unspecified |
| 10 | ICD-10 | `F419` | Anxiety disorder, unspecified |
| 11 | ICD-10 | `R079` | Chest pain, unspecified |
| 12 | ICD-10 | `G8929` | Other chronic pain |
| 13 | ICD-10 | `M797` | Fibromyalgia |
| 14 | ICD-10 | `R000` | Tachycardia, unspecified |
| 15 | ICD-10 | `I10` | Essential (primary) hypertension |
| 16 | ICD-10 | `Z87891` | Personal history of nicotine dependence |
| 17 | ICD-10 | `R12` | Heartburn |

## 5. ICU Stays

| Stay ID | First Care Unit | Last Care Unit | ICU Admit | ICU Discharge | LOS (days) |
|---|---|---|---|---|---|
| 37507305 | Medical Intensive Care Unit (MICU) | Medical Intensive Care Unit (MICU) | 2113-09-14 10:19:17 | 2113-09-15 12:43:00 | 1.10 |

## 6. Escalation / Severity Indicators

The following critical conditions or interventions were detected:

- **Non-Invasive Ventilation (NIV/BiPAP)** (ICU procedure event)
- **Respiratory Failure** (ICD diagnosis)

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2113-09-14 | ICD-10 | `0B578ZZ` | Destruction of Left Main Bronchus, Via Natural or Artificial Opening Endoscopic |
| 2 | 2113-09-14 | ICD-10 | `0B778DZ` | Dilation of Left Main Bronchus with Intraluminal Device, Via Natural or Artificial Opening Endoscopic |
| 3 | 2113-09-14 | ICD-10 | `0BB78ZZ` | Excision of Left Main Bronchus, Via Natural or Artificial Opening Endoscopic |
| 4 | 2113-09-14 | ICD-10 | `0BBF8ZZ` | Excision of Right Lower Lung Lobe, Via Natural or Artificial Opening Endoscopic |
| 5 | 2113-09-14 | ICD-10 | `0B5F8ZZ` | Destruction of Right Lower Lung Lobe, Via Natural or Artificial Opening Endoscopic |
| 6 | 2113-09-14 | ICD-10 | `0BC78ZZ` | Extirpation of Matter from Left Main Bronchus, Via Natural or Artificial Opening Endoscopic |
| 7 | 2113-09-15 | ICD-10 | `0D738DZ` | Dilation of Lower Esophagus with Intraluminal Device, Via Natural or Artificial Opening Endoscopic |
| 8 | 2113-09-16 | ICD-10 | `0BB78ZZ` | Excision of Left Main Bronchus, Via Natural or Artificial Opening Endoscopic |
| 9 | 2113-09-16 | ICD-10 | `0B978ZX` | Drainage of Left Main Bronchus, Via Natural or Artificial Opening Endoscopic, Diagnostic |

### ICU Procedure Events (from `icu/procedureevents.csv.gz`)

- Non-invasive Ventilation (category: 2-Ventilation, started: 2113-09-14 10:40:00, status: FinishedRunning)
- 22 Gauge (category: Access Lines - Peripheral, started: 2113-09-14 10:46:00, status: FinishedRunning)
- 20 Gauge (category: Access Lines - Peripheral, started: 2113-09-14 10:50:00, status: FinishedRunning)

## 8. Critical Findings (Charted Events)

- **Ventilator Mode (Hamilton)** (first noted: 2113-09-14 10:43:00)
- **Ventilator Type** (first noted: 2113-09-14 10:39:00)
- **Code Status** (first noted: 2113-09-14 12:41:00)

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2113-09-12 14:42:00 | Admission | Admitted from TRANSFER FROM HOSPITAL (URGENT) |
| 2113-09-14 10:19:17 | ICU Admission | Medical Intensive Care Unit (MICU) (LOS: 1.1 days) |
| 2113-09-14 10:19:17 | Transfer | → Medical Intensive Care Unit (MICU) (transfer) |
| 2113-09-15 12:43:00 | Transfer | → Hematology/Oncology (transfer) |
| 2113-09-20 18:40:00 | Discharge | To ACUTE HOSPITAL |

## 10. Missing / Ambiguous Data

- No ED registration time — admission may not have gone through ED.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
