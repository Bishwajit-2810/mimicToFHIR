# Encounter Report — HADM 28998349

> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, `hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, `hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, `hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, `icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`

## 1. Encounter Information

| Field | Value |
|---|---|
| Hospital Admission ID | 28998349 |
| Subject ID | 10021487 |
| Patient Sex | M |
| Patient Anchor Age (at anchor year) | 43 |
| Anchor Year | 2116 |
| Admission Time | 2116-12-03 00:23:00 |
| Discharge Time | 2116-12-28 13:19:00 |
| Admission Type | EW EMER. |
| Admission Location | EMERGENCY ROOM |
| Discharge Location | HOME |
| Insurance | Other |
| Language | ENGLISH |
| Marital Status | MARRIED |
| Race/Ethnicity | WHITE |
| ED Registration | 2116-12-02 22:57:00 |
| ED Departure | 2116-12-03 01:02:00 |
| In-Hospital Mortality | No |
| Date of Death (overall) | N/A |

## 2. Hospital Visit Reason

### DRG Codes (MS-DRG / HCFA)

| Type | Code | Description | Severity | Mortality |
|---|---|---|---|---|
| APR | 911 | EXTENSIVE ABDOMINAL/THORACIC PROCEDURES FOR MULT SIGNIFICANT TRAUMA | 4.0 | 4.0 |
| HCFA | 957 | OTHER O.R. PROCEDURES FOR MULTIPLE SIGNIFICANT TRAUMA W MCC | N/A | N/A |

### Primary Diagnosis (seq_num = 1)

- **ICD-9 86803**: Injury to other intra-abdominal organs without mention of open wound into cavity, peritoneum

### Clinical Services

| Time | Previous Service | Current Service |
|---|---|---|
| 2116-12-03 00:24:58 | N/A | TRAUM |

## 3. Symptoms and Chief Complaint

> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. Chief complaints and symptom narratives are not available. Symptoms are inferred from ICD codes and DRG descriptions.

Coded conditions (top 5 by sequence) that may reflect presenting symptoms:

- (seq 1) ICD-9 `86803`: Injury to other intra-abdominal organs without mention of open wound into cavity, peritoneum
- (seq 2) ICD-9 `9584`: Traumatic shock
- (seq 3) ICD-9 `86401`: Injury to liver without mention of open wound into cavity, hematoma and contusion
- (seq 4) ICD-9 `570`: Acute and subacute necrosis of liver
- (seq 5) ICD-9 `5570`: Acute vascular insufficiency of intestine

## 4. Diagnoses

| Seq | ICD Version | ICD Code | Description |
|---|---|---|---|
| 1 | ICD-9 | `86803` | Injury to other intra-abdominal organs without mention of open wound into cavity, peritoneum |
| 2 | ICD-9 | `9584` | Traumatic shock |
| 3 | ICD-9 | `86401` | Injury to liver without mention of open wound into cavity, hematoma and contusion |
| 4 | ICD-9 | `570` | Acute and subacute necrosis of liver |
| 5 | ICD-9 | `5570` | Acute vascular insufficiency of intestine |
| 6 | ICD-9 | `48241` | Methicillin susceptible pneumonia due to Staphylococcus aureus |
| 7 | ICD-9 | `51851` | Acute respiratory failure following trauma and surgery |
| 8 | ICD-9 | `5845` | Acute kidney failure with lesion of tubular necrosis |
| 9 | ICD-9 | `9585` | Traumatic anuria |
| 10 | ICD-9 | `80704` | Closed fracture of four ribs |
| 11 | ICD-9 | `8052` | Closed fracture of dorsal [thoracic] vertebra without mention of spinal cord injury |
| 12 | ICD-9 | `8054` | Closed fracture of lumbar vertebra without mention of spinal cord injury |
| 13 | ICD-9 | `80506` | Closed fracture of sixth cervical vertebra |
| 14 | ICD-9 | `72888` | Rhabdomyolysis |
| 15 | ICD-9 | `2762` | Acidosis |
| 16 | ICD-9 | `9971` | Cardiac complications, not elsewhere classified |
| 17 | ICD-9 | `4264` | Right bundle branch block |
| 18 | ICD-9 | `7850` | Tachycardia, unspecified |
| 19 | ICD-9 | `45829` | Other iatrogenic hypotension |
| 20 | ICD-9 | `8602` | Traumatic hemothorax without mention of open wound into thorax |
| 21 | ICD-9 | `83908` | Closed dislocation, multiple cervical vertebrae |
| 22 | ICD-9 | `86405` | Injury to liver without mention of open wound into cavity laceration, unspecified |
| 23 | ICD-9 | `5718` | Other chronic nonalcoholic liver disease |
| 24 | ICD-9 | `86801` | Injury to other intra-abdominal organs without mention of open wound into cavity, adrenal gland |
| 25 | ICD-9 | `86100` | Unspecified injury of heart without mention of open wound into thorax |
| 26 | ICD-9 | `86121` | Contusion of lung without mention of open wound into thorax |
| 27 | ICD-9 | `86389` | Injury to other gastrointestinal sites, without mention of open wound into cavity |
| 28 | ICD-9 | `2767` | Hyperpotassemia |
| 29 | ICD-9 | `60886` | Edema of male genital organs |
| 30 | ICD-9 | `6926` | Contact dermatitis and other eczema due to plants [except food] |
| 31 | ICD-9 | `E8654` | Accidental poisoning from other specified plants |
| 32 | ICD-9 | `27669` | Other fluid overload |
| 33 | ICD-9 | `30500` | Alcohol abuse, unspecified |
| 34 | ICD-9 | `E8150` | Other motor vehicle traffic accident involving collision on the highway injuring driver of motor vehicle other than motorcycle |
| 35 | ICD-9 | `V140` | Personal history of allergy to penicillin |

## 5. ICU Stays

| Stay ID | First Care Unit | Last Care Unit | ICU Admit | ICU Discharge | LOS (days) |
|---|---|---|---|---|---|
| 38197705 | Trauma SICU (TSICU) | Trauma SICU (TSICU) | 2116-12-03 01:02:00 | 2116-12-18 17:34:03 | 15.69 |

## 6. Escalation / Severity Indicators

The following critical conditions or interventions were detected:

- **Acute Kidney Injury** (ICD diagnosis)
- **Arterial Line** (ICU procedure event)
- **Endotracheal Intubation** (ICU procedure event)
- **Invasive Mechanical Ventilation** (ICU procedure event)
- **Pneumonia** (ICD diagnosis)

## 7. Procedures and Interventions

### ICD-Coded Procedures

| Seq | Date | ICD Version | ICD Code | Description |
|---|---|---|---|---|
| 1 | 2116-12-03 | ICD-9 | `5419` | Other laparotomy |
| 2 | 2116-12-03 | ICD-9 | `5029` | Other destruction of lesion of liver |
| 3 | 2116-12-03 | ICD-9 | `4573` | Open and other right hemicolectomy |
| 4 | 2116-12-03 | ICD-9 | `5412` | Reopening of recent laparotomy site |
| 5 | 2116-12-03 | ICD-9 | `5475` | Other repair of mesentery |
| 6 | 2116-12-03 | ICD-9 | `5425` | Peritoneal lavage |
| 7 | 2116-12-03 | ICD-9 | `9604` | Insertion of endotracheal tube |
| 8 | 2116-12-03 | ICD-9 | `9672` | Continuous invasive mechanical ventilation for 96 consecutive hours or more |
| 9 | 2116-12-11 | ICD-9 | `5491` | Percutaneous abdominal drainage |
| 10 | 2116-12-11 | ICD-9 | `8876` | Diagnostic ultrasound of abdomen and retroperitoneum |
| 11 | 2116-12-03 | ICD-9 | `3893` | Venous catheterization, not elsewhere classified |
| 12 | 2116-12-27 | ICD-9 | `3491` | Thoracentesis |
| 13 | 2116-12-07 | ICD-9 | `3891` | Arterial catheterization |
| 14 | 2116-12-09 | ICD-9 | `3324` | Closed [endoscopic] biopsy of bronchus |
| 15 | 2116-12-12 | ICD-9 | `966` | Enteral infusion of concentrated nutritional substances |

### ICU Procedure Events (from `icu/procedureevents.csv.gz`)

- Invasive Ventilation (category: 2-Ventilation, started: 2116-12-03 00:25:00, status: FinishedRunning)
- Intubation (category: 1-Intubation/Extubation, started: 2116-12-03 00:25:00, status: FinishedRunning)
- Arterial Line (category: Access Lines - Invasive, started: 2116-12-03 01:00:00, status: FinishedRunning)
- EKG (category: 4-Procedures, started: 2116-12-03 01:30:00, status: FinishedRunning)
- 14 Gauge (category: Access Lines - Peripheral, started: 2116-12-03 01:45:00, status: FinishedRunning)
- 18 Gauge (category: Access Lines - Peripheral, started: 2116-12-03 01:45:00, status: FinishedRunning)
- Transthoracic Echo (category: 5-Imaging, started: 2116-12-03 02:00:00, status: FinishedRunning)
- OR Received (category: 3-Significant Events, started: 2116-12-03 06:20:00, status: FinishedRunning)
- Family meeting held (category: 7-Communication, started: 2116-12-03 17:31:00, status: FinishedRunning)
- Family updated by MD (category: 7-Communication, started: 2116-12-03 19:00:00, status: FinishedRunning)
- OR Sent (category: 3-Significant Events, started: 2116-12-03 19:20:00, status: FinishedRunning)
- Family met with Social Worker (category: 7-Communication, started: 2116-12-05 17:27:00, status: FinishedRunning)
- Family updated by RN (category: 7-Communication, started: 2116-12-06 10:08:00, status: FinishedRunning)
- Pan Culture (category: 6-Cultures, started: 2116-12-06 10:25:00, status: FinishedRunning)
- Sputum Culture (category: 6-Cultures, started: 2116-12-07 15:05:00, status: FinishedRunning)
- Magnetic Resonance Imaging (category: 5-Imaging, started: 2116-12-07 16:40:00, status: FinishedRunning)
- X-ray (category: 5-Imaging, started: 2116-12-07 20:29:00, status: FinishedRunning)
- Bronchoscopy (category: 4-Procedures, started: 2116-12-09 14:32:00, status: FinishedRunning)
- Urine Culture (category: 6-Cultures, started: 2116-12-09 15:36:00, status: FinishedRunning)
- 20 Gauge (category: Access Lines - Peripheral, started: 2116-12-10 12:00:00, status: FinishedRunning)
- Multi Lumen (category: Access Lines - Invasive, started: 2116-12-10 12:30:00, status: FinishedRunning)
- Blood Cultured (category: 6-Cultures, started: 2116-12-14 17:05:00, status: FinishedRunning)
- CT scan (category: 5-Imaging, started: 2116-12-17 17:19:00, status: FinishedRunning)
- Chest X-Ray (category: 5-Imaging, started: 2116-12-18 05:32:00, status: FinishedRunning)

## 8. Critical Findings (Charted Events)

- **Ventilator Type** (first noted: 2116-12-03 01:00:00)
- **Ventilator Mode** (first noted: 2116-12-03 01:00:00)
- **Ventilator Tank #2** (first noted: 2116-12-03 08:30:00)
- **Known difficult intubation** (first noted: 2116-12-09 19:00:00)
- **Code Status** (first noted: 2116-12-03 03:00:00)
- **Dialysis patient** (first noted: 2116-12-03 05:13:00)

## 9. Timeline Summary

| Time | Event | Detail |
|---|---|---|
| 2116-12-02 22:57:00 | ED Registration | Patient arrived in Emergency Dept. |
| 2116-12-02 22:57:00 | Transfer | → Emergency Department (ED) |
| 2116-12-03 00:23:00 | Admission | Admitted from EMERGENCY ROOM (EW EMER.) |
| 2116-12-03 01:02:00 | ED Departure | Left Emergency Dept. |
| 2116-12-03 01:02:00 | ICU Admission | Trauma SICU (TSICU) (LOS: 15.7 days) |
| 2116-12-18 17:34:03 | Transfer | → Med/Surg/Trauma (transfer) |
| 2116-12-18 17:38:32 | Transfer | → Med/Surg/Trauma (transfer) |
| 2116-12-28 13:19:00 | Discharge | To HOME |

## 10. Missing / Ambiguous Data

- No obvious missing critical fields detected.

## 11. Manual Review Recommendation

No specific flags for manual review. Standard clinical review recommended.
