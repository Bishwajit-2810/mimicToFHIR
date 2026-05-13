# Encounter Report — HADM 29279905

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 29279905 |
| Subject ID | 10019003 |
| Patient Sex | F |
| Patient Anchor Age (at anchor year) | 65 |
| Anchor Year | 2148 |
| Admission Time | 2153-03-27 23:25:00 |
| Discharge Time | 2153-04-07 16:20:00 |
| Admission Type | EW EMER. |
| Admission Location | EMERGENCY ROOM |
| Discharge Location | HOME HEALTH CARE |
| Insurance | Other |
| Language | ENGLISH |
| Marital Status | WIDOWED |
| Race/Ethnicity | WHITE |
| ED Registration | 2153-03-27 21:28:00 |
| ED Departure | 2153-03-28 02:21:00 |
| In-Hospital Mortality | No |
| Date of Death (overall) | 2155-12-03 |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| APR | 720 | SEPTICEMIA & DISSEMINATED INFECTIONS | 3.0 | 4.0 |
| HCFA | 871 | SEPTICEMIA OR SEVERE SEPSIS W/O MV >96 HOURS W MCC | N/A | N/A |

### Primary Diagnosis (seq_num = 1)

- **ICD-10 A419**: Sepsis, unspecified organism

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2153-03-27 23:26:24 | N/A | MED |
| 2153-03-31 16:59:21 | MED | OMED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-10 `A419`: Sepsis, unspecified organism
- (seq 2) ICD-10 `R6521`: Severe sepsis with septic shock
- (seq 3) ICD-10 `N179`: Acute kidney failure, unspecified
- (seq 4) ICD-10 `K264`: Chronic or unspecified duodenal ulcer with hemorrhage
- (seq 5) ICD-10 `D471`: Chronic myeloproliferative disease

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-10 | `A419` | Sepsis, unspecified organism |
| 2 | ICD-10 | `R6521` | Severe sepsis with septic shock |
| 3 | ICD-10 | `N179` | Acute kidney failure, unspecified |
| 4 | ICD-10 | `K264` | Chronic or unspecified duodenal ulcer with hemorrhage |
| 5 | ICD-10 | `D471` | Chronic myeloproliferative disease |
| 6 | ICD-10 | `D62` | Acute posthemorrhagic anemia |
| 7 | ICD-10 | `Z6841` | Body mass index (BMI) 40.0-44.9, adult |
| 8 | ICD-10 | `N390` | Urinary tract infection, site not specified |
| 9 | ICD-10 | `E860` | Dehydration |
| 10 | ICD-10 | `E039` | Hypothyroidism, unspecified |
| 11 | ICD-10 | `E780` | Pure hypercholesterolemia |
| 12 | ICD-10 | `R0902` | Hypoxemia |
| 13 | ICD-10 | `E119` | Type 2 diabetes mellitus without complications |
| 14 | ICD-10 | `J449` | Chronic obstructive pulmonary disease, unspecified |
| 15 | ICD-10 | `F329` | Major depressive disorder, single episode, unspecified |
| 16 | ICD-10 | `I10` | Essential (primary) hypertension |
| 17 | ICD-10 | `G4733` | Obstructive sleep apnea (adult) (pediatric) |
| 18 | ICD-10 | `J45909` | Unspecified asthma, uncomplicated |
| 19 | ICD-10 | `Z87891` | Personal history of nicotine dependence |
| 20 | ICD-10 | `K7581` | Nonalcoholic steatohepatitis (NASH) |
| 21 | ICD-10 | `L271` | Localized skin eruption due to drugs and medicaments taken internally |
| 22 | ICD-10 | `T504X5A` | Adverse effect of drugs affecting uric acid metabolism, initial encounter |
| 23 | ICD-10 | `T451X5A` | Adverse effect of antineoplastic and immunosuppressive drugs, initial encounter |
| 24 | ICD-10 | `K259` | Gastric ulcer, unspecified as acute or chronic, without hemorrhage or perforation |
| 25 | ICD-10 | `Z66` | Do not resuscitate |
| 26 | ICD-10 | `E6601` | Morbid (severe) obesity due to excess calories |

## 5. ICU Stays

| Stay ID | First Care Unit | Last Care Unit | ICU Admit | ICU Discharge | LOS (days) |
|---|---|---|---|---|---|
| 34107647 | Medical/Surgical Intensive Care Unit (MICU/SICU) | Medical/Surgical Intensive Care Unit (MICU/SICU) | 2153-03-28 02:21:00 | 2153-03-31 16:59:04 | 3.61 |

## 6. Escalation / Severity Indicators

The following critical conditions or interventions were detected:

- **Acute Kidney Injury** (ICD diagnosis)
- **Sepsis** (ICD diagnosis)

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2153-04-04 | ICD-10 | `0D598ZZ` | Destruction of Duodenum, Via Natural or Artificial Opening Endoscopic |
| 2 | 2153-03-27 | ICD-10 | `02HV33Z` | Insertion of Infusion Device into Superior Vena Cava, Percutaneous Approach |
| 3 | 2153-03-27 | ICD-10 | `B548ZZA` | Ultrasonography of Superior Vena Cava, Guidance |

### ICU Procedure Events (from `icu/procedureevents.csv.gz`)

- Multi Lumen (category: Access Lines - Invasive, started: 2153-03-28 02:30:00, status: FinishedRunning)
- 20 Gauge (category: Access Lines - Peripheral, started: 2153-03-28 03:11:00, status: FinishedRunning)
- Nasal Swab (category: 6-Cultures, started: 2153-03-28 03:11:00, status: FinishedRunning)

## 8. Critical Findings (Charted Events)

- **Code Status** (first noted: 2153-03-28 03:12:00)
- **Dialysis patient** (first noted: 2153-03-28 05:31:00)

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2153-03-27 21:28:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2153-03-27 21:28:00 | Transfer | → Emergency Department (ED) |
| 2153-03-27 23:25:00 | Admission | Admitted from EMERGENCY ROOM (EW EMER.) |
| 2153-03-28 02:21:00 | ED Departure | Left Emergency Dept. |
| 2153-03-28 02:21:00 | ICU Admission | Medical/Surgical Intensive Care Unit (MICU/SICU) (LOS: 3.6 days) |
| 2153-03-31 16:59:04 | Transfer | → Hematology/Oncology (transfer) |
| 2153-04-01 22:15:12 | Transfer | → Hematology/Oncology (transfer) |
| 2153-04-07 16:20:00 | Discharge | To HOME HEALTH CARE |

## 10. Missing / Ambiguous Data

- No obvious missing critical fields detected.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
