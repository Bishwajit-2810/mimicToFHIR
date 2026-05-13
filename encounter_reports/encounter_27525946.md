# Encounter Report — HADM 27525946

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 27525946 |
| Subject ID | 10019003 |
| Patient Sex | F |
| Patient Anchor Age (at anchor year) | 65 |
| Anchor Year | 2148 |
| Admission Time | 2153-04-12 19:07:00 |
| Discharge Time | 2153-04-20 17:09:00 |
| Admission Type | EW EMER. |
| Admission Location | EMERGENCY ROOM |
| Discharge Location | HOME |
| Insurance | Other |
| Language | ENGLISH |
| Marital Status | WIDOWED |
| Race/Ethnicity | WHITE |
| ED Registration | 2153-04-12 13:03:00 |
| ED Departure | 2153-04-12 21:40:00 |
| In-Hospital Mortality | No |
| Date of Death (overall) | 2155-12-03 |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| HCFA | 326 | STOMACH, ESOPHAGEAL & DUODENAL PROC W MCC | N/A | N/A |
| APR | 220 | MAJOR STOMACH, ESOPHAGEAL & DUODENAL PROCEDURES | 4.0 | 4.0 |

### Primary Diagnosis (seq_num = 1)

- **ICD-10 K264**: Chronic or unspecified duodenal ulcer with hemorrhage

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2153-04-12 19:07:59 | N/A | OMED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-10 `K264`: Chronic or unspecified duodenal ulcer with hemorrhage
- (seq 2) ICD-10 `A419`: Sepsis, unspecified organism
- (seq 3) ICD-10 `J9601`: Acute respiratory failure with hypoxia
- (seq 4) ICD-10 `R6521`: Severe sepsis with septic shock
- (seq 5) ICD-10 `J690`: Pneumonitis due to inhalation of food and vomit

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-10 | `K264` | Chronic or unspecified duodenal ulcer with hemorrhage |
| 2 | ICD-10 | `A419` | Sepsis, unspecified organism |
| 3 | ICD-10 | `J9601` | Acute respiratory failure with hypoxia |
| 4 | ICD-10 | `R6521` | Severe sepsis with septic shock |
| 5 | ICD-10 | `J690` | Pneumonitis due to inhalation of food and vomit |
| 6 | ICD-10 | `E8881` | Metabolic syndrome |
| 7 | ICD-10 | `D696` | Thrombocytopenia, unspecified |
| 8 | ICD-10 | `D62` | Acute posthemorrhagic anemia |
| 9 | ICD-10 | `C9590` | Leukemia, unspecified not having achieved remission |
| 10 | ICD-10 | `C946` | Myelodysplastic disease, not classified |
| 11 | ICD-10 | `Z87891` | Personal history of nicotine dependence |
| 12 | ICD-10 | `E039` | Hypothyroidism, unspecified |
| 13 | ICD-10 | `J449` | Chronic obstructive pulmonary disease, unspecified |
| 14 | ICD-10 | `I10` | Essential (primary) hypertension |
| 15 | ICD-10 | `E785` | Hyperlipidemia, unspecified |
| 16 | ICD-10 | `F329` | Major depressive disorder, single episode, unspecified |
| 17 | ICD-10 | `Z66` | Do not resuscitate |
| 18 | ICD-10 | `Z781` | Physical restraint status |
| 19 | ICD-10 | `Z853` | Personal history of malignant neoplasm of breast |
| 20 | ICD-10 | `Z923` | Personal history of irradiation |
| 21 | ICD-10 | `E669` | Obesity, unspecified |
| 22 | ICD-10 | `Z6833` | Body mass index (BMI) 33.0-33.9, adult |
| 23 | ICD-10 | `E119` | Type 2 diabetes mellitus without complications |
| 24 | ICD-10 | `Z794` | Long term (current) use of insulin |

## 5. ICU Stays

| Stay ID | First Care Unit | Last Care Unit | ICU Admit | ICU Discharge | LOS (days) |
|---|---|---|---|---|---|
| 35214014 | Medical/Surgical Intensive Care Unit (MICU/SICU) | Medical/Surgical Intensive Care Unit (MICU/SICU) | 2153-04-13 19:45:30 | 2153-04-16 21:15:15 | 3.06 |

## 6. Escalation / Severity Indicators

The following critical conditions or interventions were detected:

- **Arterial Line** (ICU procedure event)
- **Invasive Mechanical Ventilation** (ICU procedure event)
- **Respiratory Failure** (ICD diagnosis)
- **Sepsis** (ICD diagnosis)

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2153-04-13 | ICD-10 | `0DJ08ZZ` | Inspection of Upper Intestinal Tract, Via Natural or Artificial Opening Endoscopic |
| 2 | 2153-04-13 | ICD-10 | `0DQ98ZZ` | Repair Duodenum, Via Natural or Artificial Opening Endoscopic |
| 3 | 2153-04-15 | ICD-10 | `04L33DZ` | Occlusion of Hepatic Artery with Intraluminal Device, Percutaneous Approach |
| 4 | 2153-04-13 | ICD-10 | `3E0G8GC` | Introduction of Other Therapeutic Substance into Upper GI, Via Natural or Artificial Opening Endoscopic |
| 5 | 2153-04-13 | ICD-10 | `0D598ZZ` | Destruction of Duodenum, Via Natural or Artificial Opening Endoscopic |
| 6 | 2153-04-15 | ICD-10 | `04L23DZ` | Occlusion of Gastric Artery with Intraluminal Device, Percutaneous Approach |
| 7 | 2153-04-14 | ICD-10 | `02HV33Z` | Insertion of Infusion Device into Superior Vena Cava, Percutaneous Approach |
| 8 | 2153-04-14 | ICD-10 | `B548ZZA` | Ultrasonography of Superior Vena Cava, Guidance |

### ICU Procedure Events (from `icu/procedureevents.csv.gz`)

- 18 Gauge (category: Access Lines - Peripheral, started: 2153-04-13 19:45:00, status: FinishedRunning)
- Foley Catheter (category: GI/GU, started: 2153-04-13 19:45:00, status: FinishedRunning)
- Invasive Ventilation (category: 2-Ventilation, started: 2153-04-13 19:46:00, status: FinishedRunning)
- Blood Cultured (category: 6-Cultures, started: 2153-04-13 21:00:00, status: FinishedRunning)
- Urine Culture (category: 6-Cultures, started: 2153-04-13 21:30:00, status: FinishedRunning)
- Arterial Line (category: Access Lines - Invasive, started: 2153-04-13 22:00:00, status: FinishedRunning)
- 20 Gauge (category: Access Lines - Peripheral, started: 2153-04-13 23:15:00, status: FinishedRunning)
- PICC Line (category: Access Lines - Invasive, started: 2153-04-14 13:00:00, status: FinishedRunning)
- X-ray (category: 5-Imaging, started: 2153-04-14 14:00:00, status: FinishedRunning)
- Extubation (category: 1-Intubation/Extubation, started: 2153-04-14 17:50:00, status: FinishedRunning)

## 8. Critical Findings (Charted Events)

- **Ventilator Tank #2** (first noted: 2153-04-13 19:00:00)
- **Ventilator Tank #1** (first noted: 2153-04-13 19:00:00)
- **Ventilator Type** (first noted: 2153-04-13 19:45:00)
- **Known difficult intubation** (first noted: 2153-04-13 19:00:00)
- **Dialysis patient** (first noted: 2153-04-14 11:09:00)

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2153-04-12 13:03:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2153-04-12 13:03:00 | Transfer | → Emergency Department (ED) |
| 2153-04-12 19:07:00 | Admission | Admitted from EMERGENCY ROOM (EW EMER.) |
| 2153-04-12 21:40:00 | ED Departure | Left Emergency Dept. |
| 2153-04-13 18:19:25 | Transfer | → PACU (transfer) |
| 2153-04-13 19:45:30 | ICU Admission | Medical/Surgical Intensive Care Unit (MICU/SICU) (LOS: 3.1 days) |
| 2153-04-13 19:45:30 | Transfer | → Medical/Surgical Intensive Care Unit (MICU/SICU) (transfer) |
| 2153-04-16 21:15:15 | Transfer | → Medicine (transfer) |
| 2153-04-20 17:09:00 | Discharge | To HOME |

## 10. Missing / Ambiguous Data

- No obvious missing critical fields detected.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
