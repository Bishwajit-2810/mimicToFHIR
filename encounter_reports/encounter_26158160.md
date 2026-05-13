# Encounter Report — HADM 26158160

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 26158160 |
| Subject ID | 10005866 |
| Patient Sex | M |
| Patient Anchor Age (at anchor year) | 57 |
| Anchor Year | 2146 |
| Admission Time | 2146-06-06 00:50:00 |
| Discharge Time | 2146-06-09 16:45:00 |
| Admission Type | EW EMER. |
| Admission Location | EMERGENCY ROOM |
| Discharge Location | HOME |
| Insurance | Medicaid |
| Language | ENGLISH |
| Marital Status | SINGLE |
| Race/Ethnicity | PORTUGUESE |
| ED Registration | 2146-06-05 22:26:00 |
| ED Departure | 2146-06-06 01:45:00 |
| In-Hospital Mortality | No |
| Date of Death (overall) | 2149-11-21 |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| HCFA | 353 | HERNIA PROCEDURES EXCEPT INGUINAL & FEMORAL W MCC | N/A | N/A |
| APR | 228 | INGUINAL, FEMORAL & UMBILICAL HERNIA PROCEDURES | 3.0 | 1.0 |

### Primary Diagnosis (seq_num = 1)

- **ICD-9 5531**: Umbilical hernia without mention of obstruction or gangrene

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2146-06-06 00:51:19 | N/A | SURG |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-9 `5531`: Umbilical hernia without mention of obstruction or gangrene
- (seq 2) ICD-9 `56789`: Other specified peritonitis
- (seq 3) ICD-9 `78959`: Other ascites
- (seq 4) ICD-9 `5723`: Portal hypertension
- (seq 5) ICD-9 `3051`: Tobacco use disorder

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-9 | `5531` | Umbilical hernia without mention of obstruction or gangrene |
| 2 | ICD-9 | `56789` | Other specified peritonitis |
| 3 | ICD-9 | `78959` | Other ascites |
| 4 | ICD-9 | `5723` | Portal hypertension |
| 5 | ICD-9 | `3051` | Tobacco use disorder |
| 6 | ICD-9 | `5712` | Alcoholic cirrhosis of liver |
| 7 | ICD-9 | `07054` | Chronic hepatitis C without mention of hepatic coma |
| 8 | ICD-9 | `30503` | Alcohol abuse, in remission |

## 5. ICU Stays

_No ICU stay recorded for this admission._

## 6. Escalation / Severity Indicators

The following critical conditions or interventions were detected:

- **Liver Failure** (ICD diagnosis)

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2146-06-06 | ICD-9 | `5349` | Other open umbilical herniorrhaphy |


## 8. Critical Findings (Charted Events)

_No critical chart events detected._

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2146-06-05 22:26:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2146-06-05 22:26:00 | Transfer | → Emergency Department (ED) |
| 2146-06-06 00:50:00 | Admission | Admitted from EMERGENCY ROOM (EW EMER.) |
| 2146-06-06 01:45:00 | ED Departure | Left Emergency Dept. |
| 2146-06-08 06:54:08 | Transfer | → Transplant (transfer) |
| 2146-06-09 16:45:00 | Discharge | To HOME |

## 10. Missing / Ambiguous Data

- No ICU stay — patient managed on floor/step-down only.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
