# Encounter Report — HADM 29600294

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 29600294 |
| Subject ID | 10014354 |
| Patient Sex | M |
| Patient Anchor Age (at anchor year) | 60 |
| Anchor Year | 2146 |
| Admission Time | 2148-08-14 22:57:00 |
| Discharge Time | 2148-08-18 21:12:00 |
| Admission Type | OBSERVATION ADMIT |
| Admission Location | PHYSICIAN REFERRAL |
| Discharge Location | AGAINST ADVICE |
| Insurance | Other |
| Language | ENGLISH |
| Marital Status | SINGLE |
| Race/Ethnicity | WHITE |
| ED Registration | 2148-08-14 16:32:00 |
| ED Departure | 2148-08-15 00:27:00 |
| In-Hospital Mortality | No |
| Date of Death (overall) | N/A |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| HCFA | 202 | BRONCHITIS & ASTHMA W CC/MCC | N/A | N/A |
| APR | 144 | RESPIRATORY SIGNS, SYMPTOMS & MINOR DIAGNOSES | 3.0 | 2.0 |

### Primary Diagnosis (seq_num = 1)

- **ICD-10 J208**: Acute bronchitis due to other specified organisms

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2148-08-14 22:57:46 | N/A | OMED |
| 2148-08-16 08:57:36 | OMED | MED |
| 2148-08-17 14:46:04 | MED | OMED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-10 `J208`: Acute bronchitis due to other specified organisms
- (seq 2) ICD-10 `C9110`: Chronic lymphocytic leukemia of B-cell type not having achieved remission
- (seq 3) ICD-10 `N179`: Acute kidney failure, unspecified
- (seq 4) ICD-10 `E222`: Syndrome of inappropriate secretion of antidiuretic hormone
- (seq 5) ICD-10 `I480`: Paroxysmal atrial fibrillation

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-10 | `J208` | Acute bronchitis due to other specified organisms |
| 2 | ICD-10 | `C9110` | Chronic lymphocytic leukemia of B-cell type not having achieved remission |
| 3 | ICD-10 | `N179` | Acute kidney failure, unspecified |
| 4 | ICD-10 | `E222` | Syndrome of inappropriate secretion of antidiuretic hormone |
| 5 | ICD-10 | `I480` | Paroxysmal atrial fibrillation |
| 6 | ICD-10 | `F259` | Schizoaffective disorder, unspecified |
| 7 | ICD-10 | `I110` | Hypertensive heart disease with heart failure |
| 8 | ICD-10 | `I5032` | Chronic diastolic (congestive) heart failure |
| 9 | ICD-10 | `I4892` | Unspecified atrial flutter |
| 10 | ICD-10 | `I4891` | Unspecified atrial fibrillation |
| 11 | ICD-10 | `B3749` | Other urogenital candidiasis |
| 12 | ICD-10 | `E861` | Hypovolemia |
| 13 | ICD-10 | `E119` | Type 2 diabetes mellitus without complications |
| 14 | ICD-10 | `D630` | Anemia in neoplastic disease |
| 15 | ICD-10 | `E039` | Hypothyroidism, unspecified |
| 16 | ICD-10 | `I2510` | Atherosclerotic heart disease of native coronary artery without angina pectoris |
| 17 | ICD-10 | `Z955` | Presence of coronary angioplasty implant and graft |
| 18 | ICD-10 | `I69398` | Other sequelae of cerebral infarction |
| 19 | ICD-10 | `E785` | Hyperlipidemia, unspecified |
| 20 | ICD-10 | `G4733` | Obstructive sleep apnea (adult) (pediatric) |
| 21 | ICD-10 | `Z7901` | Long term (current) use of anticoagulants |
| 22 | ICD-10 | `G8929` | Other chronic pain |
| 23 | ICD-10 | `Z794` | Long term (current) use of insulin |
| 24 | ICD-10 | `R339` | Retention of urine, unspecified |
| 25 | ICD-10 | `E669` | Obesity, unspecified |
| 26 | ICD-10 | `Z6836` | Body mass index (BMI) 36.0-36.9, adult |

## 5. ICU Stays

| Stay ID | First Care Unit | Last Care Unit | ICU Admit | ICU Discharge | LOS (days) |
|---|---|---|---|---|---|
| 39864867 | Medical/Surgical Intensive Care Unit (MICU/SICU) | Medical/Surgical Intensive Care Unit (MICU/SICU) | 2148-08-16 08:57:26 | 2148-08-17 14:45:17 | 1.24 |

## 6. Escalation / Severity Indicators

The following critical conditions or interventions were detected:

- **Acute Kidney Injury** (ICD diagnosis)

## 7. Procedures and Interventions

_No ICD-coded procedures recorded._

### ICU Procedure Events (from `icu/procedureevents.csv.gz`)

- EKG (category: 4-Procedures, started: 2148-08-16 09:31:00, status: FinishedRunning)
- Indwelling Port (category: Access Lines - Invasive, started: 2148-08-16 09:35:00, status: FinishedRunning)
- Foley Catheter (category: GI/GU, started: 2148-08-16 13:33:00, status: FinishedRunning)
- Urine Culture (category: 6-Cultures, started: 2148-08-16 14:50:00, status: FinishedRunning)
- 22 Gauge (category: Access Lines - Peripheral, started: 2148-08-16 18:00:00, status: FinishedRunning)
- 20 Gauge (category: Access Lines - Peripheral, started: 2148-08-17 04:15:00, status: FinishedRunning)

## 8. Critical Findings (Charted Events)

_No critical chart events detected._

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2148-08-14 16:32:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2148-08-14 16:32:00 | Transfer | → Emergency Department (ED) |
| 2148-08-14 22:57:00 | Admission | Admitted from PHYSICIAN REFERRAL (OBSERVATION ADMIT) |
| 2148-08-15 00:27:00 | ED Departure | Left Emergency Dept. |
| 2148-08-16 08:57:26 | ICU Admission | Medical/Surgical Intensive Care Unit (MICU/SICU) (LOS: 1.2 days) |
| 2148-08-16 08:57:26 | Transfer | → Medical/Surgical Intensive Care Unit (MICU/SICU) (transfer) |
| 2148-08-17 14:45:17 | Transfer | → Hematology/Oncology Intermediate (transfer) |
| 2148-08-18 21:12:00 | Discharge | To AGAINST ADVICE |

## 10. Missing / Ambiguous Data

- No procedure ICD codes — procedures may not have been coded or were minor.

## 11. Manual Review Recommendation

**This encounter is flagged for manual review:**

- ICU stay present but no ICD procedures coded.
