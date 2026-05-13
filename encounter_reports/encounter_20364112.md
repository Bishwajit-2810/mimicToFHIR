# Encounter Report — HADM 20364112

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 20364112 |
| Subject ID | 10005866 |
| Patient Sex | M |
| Patient Anchor Age (at anchor year) | 57 |
| Anchor Year | 2146 |
| Admission Time | 2149-10-01 18:56:00 |
| Discharge Time | 2149-10-25 18:50:00 |
| Admission Type | OBSERVATION ADMIT |
| Admission Location | PHYSICIAN REFERRAL |
| Discharge Location | SKILLED NURSING FACILITY |
| Insurance | Medicaid |
| Language | ENGLISH |
| Marital Status | SINGLE |
| Race/Ethnicity | PORTUGUESE |
| ED Registration | 2149-10-01 02:07:00 |
| ED Departure | 2149-10-01 15:59:00 |
| In-Hospital Mortality | No |
| Date of Death (overall) | 2149-11-21 |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| HCFA | 356 | OTHER DIGESTIVE SYSTEM O.R. PROCEDURES W MCC | N/A | N/A |
| APR | 222 | OTHER STOMACH, ESOPHAGEAL & DUODENAL PROCEDURES | 3.0 | 3.0 |

### Primary Diagnosis (seq_num = 1)

- **ICD-10 K265**: Chronic or unspecified duodenal ulcer with perforation

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2149-10-01 18:56:59 | N/A | SURG |
| 2149-10-22 09:16:13 | SURG | MED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-10 `K265`: Chronic or unspecified duodenal ulcer with perforation
- (seq 2) ICD-10 `E43`: Unspecified severe protein-calorie malnutrition
- (seq 3) ICD-10 `J811`: Chronic pulmonary edema
- (seq 4) ICD-10 `D688`: Other specified coagulation defects
- (seq 5) ICD-10 `K766`: Portal hypertension

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-10 | `K265` | Chronic or unspecified duodenal ulcer with perforation |
| 2 | ICD-10 | `E43` | Unspecified severe protein-calorie malnutrition |
| 3 | ICD-10 | `J811` | Chronic pulmonary edema |
| 4 | ICD-10 | `D688` | Other specified coagulation defects |
| 5 | ICD-10 | `K766` | Portal hypertension |
| 6 | ICD-10 | `D6959` | Other secondary thrombocytopenia |
| 7 | ICD-10 | `D62` | Acute posthemorrhagic anemia |
| 8 | ICD-10 | `I471` | Supraventricular tachycardia |
| 9 | ICD-10 | `I959` | Hypotension, unspecified |
| 10 | ICD-10 | `K255` | Chronic or unspecified gastric ulcer with perforation |
| 11 | ICD-10 | `I4891` | Unspecified atrial fibrillation |
| 12 | ICD-10 | `K209` | Esophagitis, unspecified |
| 13 | ICD-10 | `B182` | Chronic viral hepatitis C |
| 14 | ICD-10 | `K7031` | Alcoholic cirrhosis of liver with ascites |
| 15 | ICD-10 | `F1011` | Alcohol abuse, in remission |
| 16 | ICD-10 | `K660` | Peritoneal adhesions (postprocedural) (postinfection) |
| 17 | ICD-10 | `K3189` | Other diseases of stomach and duodenum |
| 18 | ICD-10 | `Z5309` | Procedure and treatment not carried out because of other contraindication |
| 19 | ICD-10 | `G8929` | Other chronic pain |
| 20 | ICD-10 | `I8510` | Secondary esophageal varices without bleeding |
| 21 | ICD-10 | `Z66` | Do not resuscitate |
| 22 | ICD-10 | `Z515` | Encounter for palliative care |
| 23 | ICD-10 | `R0902` | Hypoxemia |
| 24 | ICD-10 | `D638` | Anemia in other chronic diseases classified elsewhere |
| 25 | ICD-10 | `Z590` | Homelessness |
| 26 | ICD-10 | `Z6824` | Body mass index (BMI) 24.0-24.9, adult |
| 27 | ICD-10 | `K449` | Diaphragmatic hernia without obstruction or gangrene |
| 28 | ICD-10 | `Z720` | Tobacco use |

## 5. ICU Stays

| Stay ID | First Care Unit | Last Care Unit | ICU Admit | ICU Discharge | LOS (days) |
|---|---|---|---|---|---|
| 34170353 | Trauma SICU (TSICU) | Surgical Intensive Care Unit (SICU) | 2149-10-02 12:48:08 | 2149-10-04 17:48:36 | 2.21 |

## 6. Escalation / Severity Indicators

The following critical conditions or interventions were detected:

- **Arterial Line** (ICU procedure event)

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2149-10-01 | ICD-10 | `0WJP0ZZ` | Inspection of Gastrointestinal Tract, Open Approach |
| 2 | 2149-10-16 | ICD-10 | `0D9630Z` | Drainage of Stomach with Drainage Device, Percutaneous Approach |
| 3 | 2149-10-16 | ICD-10 | `0D963ZX` | Drainage of Stomach, Percutaneous Approach, Diagnostic |
| 4 | 2149-10-02 | ICD-10 | `3E0336Z` | Introduction of Nutritional Substance into Peripheral Vein, Percutaneous Approach |
| 5 | 2149-10-03 | ICD-10 | `02HV33Z` | Insertion of Infusion Device into Superior Vena Cava, Percutaneous Approach |
| 6 | 2149-10-16 | ICD-10 | `0DH98UZ` | Insertion of Feeding Device into Duodenum, Via Natural or Artificial Opening Endoscopic |
| 7 | 2149-10-01 | ICD-10 | `0DJ08ZZ` | Inspection of Upper Intestinal Tract, Via Natural or Artificial Opening Endoscopic |
| 8 | 2149-10-16 | ICD-10 | `3E0G76Z` | Introduction of Nutritional Substance into Upper GI, Via Natural or Artificial Opening |

### ICU Procedure Events (from `icu/procedureevents.csv.gz`)

- 18 Gauge (category: Access Lines - Peripheral, started: 2149-10-02 13:14:00, status: FinishedRunning)
- Arterial Line (category: Access Lines - Invasive, started: 2149-10-02 13:14:00, status: FinishedRunning)
- Foley Catheter (category: GI/GU, started: 2149-10-02 19:00:00, status: FinishedRunning)
- EKG (category: 4-Procedures, started: 2149-10-03 11:16:00, status: FinishedRunning)
- PICC Line (category: Access Lines - Invasive, started: 2149-10-03 13:10:00, status: FinishedRunning)
- Chest X-Ray (category: 5-Imaging, started: 2149-10-03 13:10:00, status: FinishedRunning)
- Endoscopy (category: 4-Procedures, started: 2149-10-03 17:50:00, status: FinishedRunning)
- 20 Gauge (category: Access Lines - Peripheral, started: 2149-10-04 00:17:00, status: FinishedRunning)
- Portable Chest X-Ray (category: 5-Imaging, started: 2149-10-04 05:37:00, status: FinishedRunning)

## 8. Critical Findings (Charted Events)

- **Code Status** (first noted: 2149-10-02 13:15:00)

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2149-10-01 02:07:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2149-10-01 02:07:00 | Transfer | → Emergency Department (ED) |
| 2149-10-01 15:59:00 | ED Departure | Left Emergency Dept. |
| 2149-10-01 18:56:00 | Admission | Admitted from PHYSICIAN REFERRAL (OBSERVATION ADMIT) |
| 2149-10-02 12:48:08 | ICU Admission | Trauma SICU (TSICU) (LOS: 2.2 days) |
| 2149-10-02 12:48:08 | Transfer | → Trauma SICU (TSICU) (transfer) |
| 2149-10-03 16:44:58 | Transfer | → Medical/Surgical Intensive Care Unit (MICU/SICU) (transfer) |
| 2149-10-03 20:16:10 | Transfer | → Surgical Intensive Care Unit (SICU) (transfer) |
| 2149-10-04 17:48:36 | Transfer | → Transplant (transfer) |
| 2149-10-25 18:50:00 | Discharge | To SKILLED NURSING FACILITY |

## 10. Missing / Ambiguous Data

- No obvious missing critical fields detected.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
