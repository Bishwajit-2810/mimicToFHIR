# Encounter Report — HADM 22733922

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 22733922 |
| Subject ID | 10002930 |
| Patient Sex | F |
| Patient Anchor Age (at anchor year) | 48 |
| Anchor Year | 2193 |
| Admission Time | 2198-04-22 16:17:00 |
| Discharge Time | 2198-05-04 13:20:00 |
| Admission Type | URGENT |
| Admission Location | INTERNAL TRANSFER TO OR FROM PSYCH |
| Discharge Location | HOME |
| Insurance | Medicare |
| Language | ENGLISH |
| Marital Status | SINGLE |
| Race/Ethnicity | BLACK/AFRICAN AMERICAN |
| ED Registration | N/A |
| ED Departure | N/A |
| In-Hospital Mortality | No |
| Date of Death (overall) | 2201-12-24 |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| HCFA | 896 | ALCOHOL/DRUG ABUSE OR DEPENDENCE W/O REHABILITATION THERAPY W MCC | N/A | N/A |
| APR | 774 | COCAINE ABUSE & DEPENDENCE | 3.0 | 1.0 |

### Primary Diagnosis (seq_num = 1)

- **ICD-10 F1994**: Other psychoactive substance use, unspecified with psychoactive substance-induced mood disorder

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2198-04-22 16:19:39 | N/A | PSYCH |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-10 `F1994`: Other psychoactive substance use, unspecified with psychoactive substance-induced mood disorder
- (seq 2) ICD-10 `B20`: Human immunodeficiency virus [HIV] disease
- (seq 3) ICD-10 `F1490`: Cocaine use, unspecified, uncomplicated
- (seq 4) ICD-10 `F1099`: Alcohol use, unspecified with unspecified alcohol-induced disorder
- (seq 5) ICD-10 `F209`: Schizophrenia, unspecified

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-10 | `F1994` | Other psychoactive substance use, unspecified with psychoactive substance-induced mood disorder |
| 2 | ICD-10 | `B20` | Human immunodeficiency virus [HIV] disease |
| 3 | ICD-10 | `F1490` | Cocaine use, unspecified, uncomplicated |
| 4 | ICD-10 | `F1099` | Alcohol use, unspecified with unspecified alcohol-induced disorder |
| 5 | ICD-10 | `F209` | Schizophrenia, unspecified |
| 6 | ICD-10 | `Z87820` | Personal history of traumatic brain injury |
| 7 | ICD-10 | `B1920` | Unspecified viral hepatitis C without hepatic coma |
| 8 | ICD-10 | `Z87891` | Personal history of nicotine dependence |

## 5. ICU Stays

_No ICU stay recorded for this admission._

## 6. Escalation / Severity Indicators

_No escalation indicators detected from ICD codes or ICU procedure events._

## 7. Procedures and Interventions

_No ICD-coded procedures recorded._


## 8. Critical Findings (Charted Events)

_No critical chart events detected._

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2198-04-22 16:17:00 | Admission | Admitted from INTERNAL TRANSFER TO OR FROM PSYCH (URGENT) |
| 2198-05-04 13:20:00 | Discharge | To HOME |

## 10. Missing / Ambiguous Data

- No ED registration time — admission may not have gone through ED.
- No procedure ICD codes — procedures may not have been coded or were minor.
- No ICU stay — patient managed on floor/step-down only.

## 11. Manual Review Recommendation

**This encounter is flagged for manual review:**

- Urgent/Emergency admission but no clear escalation indicator found.
