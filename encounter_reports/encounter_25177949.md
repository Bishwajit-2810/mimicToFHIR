# Encounter Report — HADM 25177949

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 25177949 |
| Subject ID | 10032725 |
| Patient Sex | F |
| Patient Anchor Age (at anchor year) | 38 |
| Anchor Year | 2143 |
| Admission Time | 2143-02-17 14:20:00 |
| Discharge Time | 2143-03-16 17:15:00 |
| Admission Type | EW EMER. |
| Admission Location | EMERGENCY ROOM |
| Discharge Location | CHRONIC/LONG TERM ACUTE CARE |
| Insurance | Other |
| Language | ENGLISH |
| Marital Status | SINGLE |
| Race/Ethnicity | BLACK/AFRICAN AMERICAN |
| ED Registration | 2143-02-17 07:19:00 |
| ED Departure | 2143-02-17 15:18:00 |
| In-Hospital Mortality | No |
| Date of Death (overall) | 2143-03-30 |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| HCFA | 477 | BIOPSIES OF MUSCULOSKELETAL SYSTEM & CONNECTIVE TISSUE W MCC | N/A | N/A |
| APR | 309 | OTHER SIGNIFICANT HIP & FEMUR SURGERY | 3.0 | 3.0 |

### Primary Diagnosis (seq_num = 1)

- **ICD-9 1985**: Secondary malignant neoplasm of bone and bone marrow

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2143-02-17 14:21:25 | N/A | MED |
| 2143-03-01 18:53:21 | MED | OMED |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-9 `1985`: Secondary malignant neoplasm of bone and bone marrow
- (seq 2) ICD-9 `70723`: Pressure ulcer, stage III
- (seq 3) ICD-9 `1970`: Secondary malignant neoplasm of lung
- (seq 4) ICD-9 `1987`: Secondary malignant neoplasm of adrenal gland
- (seq 5) ICD-9 `1980`: Secondary malignant neoplasm of kidney

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-9 | `1985` | Secondary malignant neoplasm of bone and bone marrow |
| 2 | ICD-9 | `70723` | Pressure ulcer, stage III |
| 3 | ICD-9 | `1970` | Secondary malignant neoplasm of lung |
| 4 | ICD-9 | `1987` | Secondary malignant neoplasm of adrenal gland |
| 5 | ICD-9 | `1980` | Secondary malignant neoplasm of kidney |
| 6 | ICD-9 | `5990` | Urinary tract infection, site not specified |
| 7 | ICD-9 | `1120` | Candidiasis of mouth |
| 8 | ICD-9 | `1991` | Other malignant neoplasm without specification of site |
| 9 | ICD-9 | `V1042` | Personal history of malignant neoplasm of other parts of uterus |
| 10 | ICD-9 | `78652` | Painful respiration |
| 11 | ICD-9 | `3383` | Neoplasm related pain (acute) (chronic) |
| 12 | ICD-9 | `4019` | Unspecified essential hypertension |
| 13 | ICD-9 | `25000` | Diabetes mellitus without mention of complication, type II or unspecified type, not stated as uncontrolled |
| 14 | ICD-9 | `2724` | Other and unspecified hyperlipidemia |
| 15 | ICD-9 | `70703` | Pressure ulcer, lower back |
| 16 | ICD-9 | `78321` | Loss of weight |
| 17 | ICD-9 | `04149` | Other and unspecified Escherichia coli [E. coli] |
| 18 | ICD-9 | `56400` | Constipation, unspecified |
| 19 | ICD-9 | `46400` | Acute laryngitis without mention of obstruction |
| 20 | ICD-9 | `2853` | Antineoplastic chemotherapy induced anemia |
| 21 | ICD-9 | `E9331` | Antineoplastic and immunosuppressive drugs causing adverse effects in therapeutic use |
| 22 | ICD-9 | `78720` | Dysphagia, unspecified |
| 23 | ICD-9 | `27542` | Hypercalcemia |

## 5. ICU Stays

_No ICU stay recorded for this admission._

## 6. Escalation / Severity Indicators

_No escalation indicators detected from ICD codes or ICU procedure events._

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2143-03-03 | ICD-9 | `7855` | Internal fixation of bone without fracture reduction, femur |
| 2 | 2143-02-22 | ICD-9 | `7745` | Biopsy of bone, femur |
| 3 | 2143-03-09 | ICD-9 | `9229` | Other radiotherapeutic procedure |
| 4 | 2143-03-05 | ICD-9 | `9925` | Injection or infusion of cancer chemotherapeutic substance |


## 8. Critical Findings (Charted Events)

_No critical chart events detected._

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2143-02-17 07:19:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2143-02-17 07:19:00 | Transfer | → Emergency Department (ED) |
| 2143-02-17 14:20:00 | Admission | Admitted from EMERGENCY ROOM (EW EMER.) |
| 2143-02-17 15:18:00 | ED Departure | Left Emergency Dept. |
| 2143-02-18 19:38:52 | Transfer | → Med/Surg (transfer) |
| 2143-02-18 19:39:02 | Transfer | → Med/Surg (transfer) |
| 2143-02-28 20:50:47 | Transfer | → Med/Surg (transfer) |
| 2143-03-01 18:52:34 | Transfer | → Hematology/Oncology (transfer) |
| 2143-03-16 17:15:00 | Discharge | To CHRONIC/LONG TERM ACUTE CARE |

## 10. Missing / Ambiguous Data

- No ICU stay — patient managed on floor/step-down only.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
