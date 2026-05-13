# Encounter Report — HADM 27708593

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 27708593 |
| Subject ID | 10022880 |
| Patient Sex | M |
| Patient Anchor Age (at anchor year) | 66 |
| Anchor Year | 2177 |
| Admission Time | 2177-03-12 07:15:00 |
| Discharge Time | 2177-03-19 14:25:00 |
| Admission Type | SURGICAL SAME DAY ADMISSION |
| Admission Location | PHYSICIAN REFERRAL |
| Discharge Location | HOME |
| Insurance | Medicare |
| Language | ENGLISH |
| Marital Status | MARRIED |
| Race/Ethnicity | WHITE |
| ED Registration | N/A |
| ED Departure | N/A |
| In-Hospital Mortality | No |
| Date of Death (overall) | N/A |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| HCFA | 460 | SPINAL FUSION EXCEPT CERVICAL W/O MCC | N/A | N/A |
| APR | 304 | DORSAL & LUMBAR FUSION PROC EXCEPT FOR CURVATURE OF BACK | 2.0 | 1.0 |

### Primary Diagnosis (seq_num = 1)

- **ICD-9 72403**: Spinal stenosis, lumbar region, with neurogenic claudication

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2177-03-12 06:19:32 | N/A | NSURG |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-9 `72403`: Spinal stenosis, lumbar region, with neurogenic claudication
- (seq 2) ICD-9 `73730`: Scoliosis [and kyphoscoliosis], idiopathic
- (seq 3) ICD-9 `42731`: Atrial fibrillation
- (seq 4) ICD-9 `75612`: Spondylolisthesis
- (seq 5) ICD-9 `78820`: Retention of urine, unspecified

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-9 | `72403` | Spinal stenosis, lumbar region, with neurogenic claudication |
| 2 | ICD-9 | `73730` | Scoliosis [and kyphoscoliosis], idiopathic |
| 3 | ICD-9 | `42731` | Atrial fibrillation |
| 4 | ICD-9 | `75612` | Spondylolisthesis |
| 5 | ICD-9 | `78820` | Retention of urine, unspecified |
| 6 | ICD-9 | `V4364` | Hip joint replacement |
| 7 | ICD-9 | `56409` | Other constipation |
| 8 | ICD-9 | `V1254` | Personal history of transient ischemic attack (TIA), and cerebral infarction without residual deficits |
| 9 | ICD-9 | `V5861` | Long-term (current) use of anticoagulants |

## 5. ICU Stays

| Stay ID | First Care Unit | Last Care Unit | ICU Admit | ICU Discharge | LOS (days) |
|---|---|---|---|---|---|
| 39623478 | Surgical Intensive Care Unit (SICU) | Surgical Intensive Care Unit (SICU) | 2177-03-15 05:49:26 | 2177-03-15 22:47:09 | 0.71 |

## 6. Escalation / Severity Indicators

_No escalation indicators detected from ICD codes or ICU procedure events._

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2177-03-12 | ICD-9 | `8107` | Lumbar and lumbosacral fusion of the posterior column, posterior technique |
| 2 | 2177-03-12 | ICD-9 | `7770` | Excision of bone for graft, unspecified site |
| 3 | 2177-03-12 | ICD-9 | `8162` | Fusion or refusion of 2-3 vertebrae |

### ICU Procedure Events (from `icu/procedureevents.csv.gz`)

- 20 Gauge (category: Access Lines - Peripheral, started: 2177-03-15 06:00:00, status: FinishedRunning)
- 18 Gauge (category: Access Lines - Peripheral, started: 2177-03-15 06:00:00, status: FinishedRunning)

## 8. Critical Findings (Charted Events)

_No critical chart events detected._

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2177-03-12 07:15:00 | Admission | Admitted from PHYSICIAN REFERRAL (SURGICAL SAME DAY ADMISSION) |
| 2177-03-12 17:54:21 | Transfer | → Neurology (transfer) |
| 2177-03-15 05:49:26 | ICU Admission | Surgical Intensive Care Unit (SICU) (LOS: 0.7 days) |
| 2177-03-15 05:49:26 | Transfer | → Surgical Intensive Care Unit (SICU) (transfer) |
| 2177-03-15 06:09:22 | Transfer | → Surgical Intensive Care Unit (SICU) (transfer) |
| 2177-03-15 22:47:09 | Transfer | → Neurology (transfer) |
| 2177-03-19 14:25:00 | Discharge | To HOME |

## 10. Missing / Ambiguous Data

- No ED registration time — admission may not have gone through ED.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
