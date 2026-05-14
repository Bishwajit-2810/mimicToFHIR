"""
Generate one markdown report per hospital encounter from MIMIC-IV demo data.
Sources: hosp/ and icu/ CSV.gz files.
"""

import os
import pandas as pd
from pathlib import Path

# ── Output directory ─────────────────────────────────────────────────────────
OUT_DIR = Path("encounter_reports")
OUT_DIR.mkdir(exist_ok=True)

# ── Load tables ──────────────────────────────────────────────────────────────
print("Loading hosp tables...")
admissions   = pd.read_csv("hosp/admissions.csv.gz")
patients     = pd.read_csv("hosp/patients.csv.gz")
diagnoses    = pd.read_csv("hosp/diagnoses_icd.csv.gz")
d_icd_diag   = pd.read_csv("hosp/d_icd_diagnoses.csv.gz")
procedures   = pd.read_csv("hosp/procedures_icd.csv.gz")
d_icd_proc   = pd.read_csv("hosp/d_icd_procedures.csv.gz")
services     = pd.read_csv("hosp/services.csv.gz")
transfers    = pd.read_csv("hosp/transfers.csv.gz")
drgcodes     = pd.read_csv("hosp/drgcodes.csv.gz")

print("Loading icu tables...")
icustays       = pd.read_csv("icu/icustays.csv.gz")
d_items        = pd.read_csv("icu/d_items.csv.gz")
proc_events    = pd.read_csv("icu/procedureevents.csv.gz")
chart_events   = pd.read_csv("icu/chartevents.csv.gz")

# ── Build lookup dictionaries ────────────────────────────────────────────────
diag_lookup = dict(zip(
    d_icd_diag["icd_code"].astype(str) + "_" + d_icd_diag["icd_version"].astype(str),
    d_icd_diag["long_title"]
))
proc_lookup = dict(zip(
    d_icd_proc["icd_code"].astype(str) + "_" + d_icd_proc["icd_version"].astype(str),
    d_icd_proc["long_title"]
))
item_lookup = dict(zip(d_items["itemid"], d_items["label"]))
item_cat    = dict(zip(d_items["itemid"], d_items["category"]))

# ── Escalation ICD code sets ─────────────────────────────────────────────────
SEPSIS_ICD10_PREFIXES   = ("A40", "A41", "R6520", "R6521")
SEPSIS_ICD9_PREFIXES    = ("038", "99591", "99592")
RESP_FAIL_ICD10         = ("J960", "J961", "J969")
RESP_FAIL_ICD9          = ("51881", "51882", "51884")
CARDIAC_ARREST_ICD10    = ("I46",)
CARDIAC_ARREST_ICD9     = ("4275",)
SHOCK_ICD10_PREFIXES    = ("R57",)
SHOCK_ICD9_PREFIXES     = ("7855",)
AKI_ICD10_PREFIXES      = ("N17",)
AKI_ICD9_PREFIXES       = ("584",)
LIVER_FAIL_ICD10        = ("K720", "K721", "K729")
LIVER_FAIL_ICD9         = ("5722", "5723")
DIC_ICD10               = ("D65",)
DIC_ICD9                = ("2866",)
PNEUMONIA_ICD10         = ("J12", "J13", "J14", "J15", "J16", "J17", "J18")
PNEUMONIA_ICD9          = ("480", "481", "482", "483", "484", "485", "486")

# Escalation procedure event item IDs
INVASIVE_VENT_ITEMS  = {225792}          # Invasive Ventilation
NIV_ITEMS            = {225794}          # Non-invasive Ventilation
INTUBATION_ITEMS     = {224385, 225291}  # Intubation / Indication(Intubation)
VASOPRESSOR_ITEMS    = {221906, 221289, 222315, 221662}  # NE, Epi, Vasopressin, Dopamine
DIALYSIS_ITEMS       = {225802, 225803, 225809, 225441, 225805, 225955}
ECMO_ITEMIDS         = set(d_items[d_items["category"] == "ECMO"]["itemid"].tolist())
TRACH_ITEMS          = {225448, 226237}   # Percutaneous / Open Tracheostomy
PACER_ITEMS          = set(d_items[d_items["category"].str.contains("Pacer", na=False)]["itemid"].tolist())
ARTERIAL_LINE_ITEMS  = {225752}          # Arterial Line

# Escalation chart event item IDs (to confirm mechanical ventilation)
VENT_CHART_ITEMS = {225792, 225794, 223849, 226260}  # MechVent flags

def code_matches(code: str, prefixes: tuple) -> bool:
    c = code.replace(".", "").upper().strip()
    return any(c.startswith(p.upper()) for p in prefixes)

def classify_escalation_from_diags(hadm_diags: pd.DataFrame) -> list[str]:
    flags = []
    for _, row in hadm_diags.iterrows():
        code = str(row["icd_code"])
        ver  = int(row["icd_version"])
        if ver == 10:
            if code_matches(code, SEPSIS_ICD10_PREFIXES):      flags.append("Sepsis")
            if code_matches(code, RESP_FAIL_ICD10):            flags.append("Respiratory Failure")
            if code_matches(code, CARDIAC_ARREST_ICD10):       flags.append("Cardiac Arrest")
            if code_matches(code, SHOCK_ICD10_PREFIXES):       flags.append("Shock")
            if code_matches(code, AKI_ICD10_PREFIXES):         flags.append("Acute Kidney Injury")
            if code_matches(code, LIVER_FAIL_ICD10):           flags.append("Liver Failure")
            if code_matches(code, DIC_ICD10):                  flags.append("DIC")
            if code_matches(code, PNEUMONIA_ICD10):            flags.append("Pneumonia")
        else:
            if code_matches(code, SEPSIS_ICD9_PREFIXES):       flags.append("Sepsis")
            if code_matches(code, RESP_FAIL_ICD9):             flags.append("Respiratory Failure")
            if code_matches(code, CARDIAC_ARREST_ICD9):        flags.append("Cardiac Arrest")
            if code_matches(code, SHOCK_ICD9_PREFIXES):        flags.append("Shock")
            if code_matches(code, AKI_ICD9_PREFIXES):          flags.append("Acute Kidney Injury")
            if code_matches(code, LIVER_FAIL_ICD9):            flags.append("Liver Failure")
            if code_matches(code, DIC_ICD9):                   flags.append("DIC")
            if code_matches(code, PNEUMONIA_ICD9):             flags.append("Pneumonia")
    return sorted(set(flags))

def classify_escalation_from_icu(hadm_id: int) -> list[str]:
    flags = []
    pev = proc_events[proc_events["hadm_id"] == hadm_id]
    if pev.empty:
        return flags
    item_ids = set(pev["itemid"].unique())

    if item_ids & INVASIVE_VENT_ITEMS:   flags.append("Invasive Mechanical Ventilation")
    if item_ids & NIV_ITEMS:             flags.append("Non-Invasive Ventilation (NIV/BiPAP)")
    if item_ids & INTUBATION_ITEMS:      flags.append("Endotracheal Intubation")
    if item_ids & VASOPRESSOR_ITEMS:
        names = [item_lookup.get(i, str(i)) for i in (item_ids & VASOPRESSOR_ITEMS)]
        flags.append("Vasopressors (" + ", ".join(sorted(names)) + ")")
    if item_ids & DIALYSIS_ITEMS:        flags.append("Renal Replacement Therapy / Dialysis")
    if item_ids & ECMO_ITEMIDS:          flags.append("ECMO")
    if item_ids & TRACH_ITEMS:           flags.append("Tracheostomy")
    if item_ids & PACER_ITEMS:           flags.append("Cardiac Pacing")
    if item_ids & ARTERIAL_LINE_ITEMS:   flags.append("Arterial Line")
    return sorted(set(flags))

def icu_procedure_detail(hadm_id: int) -> list[str]:
    """Return human-readable list of distinct ICU procedure events."""
    pev = proc_events[proc_events["hadm_id"] == hadm_id].copy()
    if pev.empty:
        return []
    pev["label"] = pev["itemid"].map(item_lookup)
    pev["category"] = pev["itemid"].map(item_cat)
    unique = (
        pev[["label", "category", "starttime", "statusdescription"]]
        .dropna(subset=["label"])
        .drop_duplicates(subset=["label"])
        .sort_values("starttime")
    )
    lines = []
    for _, r in unique.iterrows():
        line = f"- {r['label']} (category: {r['category']}, started: {r['starttime']}"
        if pd.notna(r["statusdescription"]):
            line += f", status: {r['statusdescription']}"
        line += ")"
        lines.append(line)
    return lines

def icu_critical_chart_events(hadm_id: int) -> list[str]:
    """Return flagged chart events suggesting deterioration."""
    cev = chart_events[chart_events["hadm_id"] == hadm_id].copy()
    if cev.empty:
        return []
    cev["label"] = cev["itemid"].map(item_lookup)
    critical_keywords = [
        "ventilat", "intubat", "pressors", "arrest", "code", "defibrillat",
        "bradycard", "tachycard", "hypotens", "hypertens", "seizure", "stroke",
        "resuscitat", "shock", "cpr", "pacemaker", "ecmo", "dialysis",
    ]
    results = []
    for kw in critical_keywords:
        matches = cev[cev["label"].str.lower().str.contains(kw, na=False)]
        if not matches.empty:
            labels = matches["label"].dropna().unique()[:3]
            for lbl in labels:
                sub = matches[matches["label"] == lbl]
                earliest = sub["charttime"].min()
                results.append(f"- **{lbl}** (first noted: {earliest})")
    return list(dict.fromkeys(results))  # deduplicate while preserving order

def fmt_null(val) -> str:
    if pd.isna(val):
        return "N/A"
    return str(val)

def generate_report(hadm_id: int) -> str:
    # ── Admission ────────────────────────────────────────────────────────────
    adm_row = admissions[admissions["hadm_id"] == hadm_id].iloc[0]
    subject_id = int(adm_row["subject_id"])

    pat_row = patients[patients["subject_id"] == subject_id]
    patient_age  = fmt_null(pat_row["anchor_age"].values[0]) if not pat_row.empty else "N/A"
    patient_sex  = fmt_null(pat_row["gender"].values[0])     if not pat_row.empty else "N/A"
    anchor_year  = fmt_null(pat_row["anchor_year"].values[0]) if not pat_row.empty else "N/A"
    dod          = fmt_null(pat_row["dod"].values[0])         if not pat_row.empty else "N/A"

    admittime  = fmt_null(adm_row["admittime"])
    dischtime  = fmt_null(adm_row["dischtime"])
    deathtime  = fmt_null(adm_row["deathtime"])
    adm_type   = fmt_null(adm_row["admission_type"])
    adm_loc    = fmt_null(adm_row["admission_location"])
    disch_loc  = fmt_null(adm_row["discharge_location"])
    insurance  = fmt_null(adm_row["insurance"])
    language   = fmt_null(adm_row["language"])
    marital    = fmt_null(adm_row["marital_status"])
    race       = fmt_null(adm_row["race"])
    expired    = bool(adm_row["hospital_expire_flag"])
    edregtime  = fmt_null(adm_row.get("edregtime", float("nan")))
    edouttime  = fmt_null(adm_row.get("edouttime", float("nan")))

    # ── Diagnoses ─────────────────────────────────────────────────────────────
    hadm_diags = (
        diagnoses[diagnoses["hadm_id"] == hadm_id]
        .sort_values("seq_num")
        .copy()
    )
    hadm_diags["key"] = hadm_diags["icd_code"].astype(str) + "_" + hadm_diags["icd_version"].astype(str)
    hadm_diags["title"] = hadm_diags["key"].map(diag_lookup).fillna("Unknown")

    # ── Procedures (ICD) ─────────────────────────────────────────────────────
    hadm_procs = (
        procedures[procedures["hadm_id"] == hadm_id]
        .sort_values("seq_num")
        .copy()
    )
    hadm_procs["key"] = hadm_procs["icd_code"].astype(str) + "_" + hadm_procs["icd_version"].astype(str)
    hadm_procs["title"] = hadm_procs["key"].map(proc_lookup).fillna("Unknown")

    # ── DRG codes ─────────────────────────────────────────────────────────────
    hadm_drg = drgcodes[drgcodes["hadm_id"] == hadm_id].copy()

    # ── Services ─────────────────────────────────────────────────────────────
    hadm_svc = services[services["hadm_id"] == hadm_id].sort_values("transfertime").copy()

    # ── Transfers ─────────────────────────────────────────────────────────────
    hadm_xfr = transfers[transfers["hadm_id"] == hadm_id].sort_values("intime").copy()

    # ── ICU stays ─────────────────────────────────────────────────────────────
    hadm_icu = icustays[icustays["hadm_id"] == hadm_id].sort_values("intime").copy()

    # ── Escalation detection ─────────────────────────────────────────────────
    dx_escalations  = classify_escalation_from_diags(hadm_diags)
    icu_escalations = classify_escalation_from_icu(hadm_id)
    icu_procedures  = icu_procedure_detail(hadm_id)
    critical_charts = icu_critical_chart_events(hadm_id)

    all_escalations = sorted(set(dx_escalations + icu_escalations))

    # ── Ambiguity / manual review flags ──────────────────────────────────────
    review_flags = []
    if adm_type in ("URGENT", "EMERGENCY") and not all_escalations:
        review_flags.append("Urgent/Emergency admission but no clear escalation indicator found.")
    if expired and not any(x in all_escalations for x in ("Cardiac Arrest", "Respiratory Failure", "Sepsis", "Shock")):
        review_flags.append("Patient expired in-hospital but cause of death not clearly coded.")
    if hadm_diags.empty:
        review_flags.append("No ICD diagnoses found — data may be incomplete.")
    if hadm_procs.empty and not hadm_icu.empty:
        review_flags.append("ICU stay present but no ICD procedures coded.")
    if hadm_diags["title"].str.contains("Unknown").any():
        n_unk = (hadm_diags["title"] == "Unknown").sum()
        review_flags.append(f"{n_unk} diagnosis code(s) could not be resolved in d_icd_diagnoses.")

    # ── Timeline ─────────────────────────────────────────────────────────────
    timeline = []
    timeline.append(f"| {admittime} | Admission | Admitted from {adm_loc} ({adm_type}) |")
    if edregtime != "N/A":
        timeline.append(f"| {edregtime} | ED Registration | Patient arrived in Emergency Dept. |")
    if edouttime != "N/A":
        timeline.append(f"| {edouttime} | ED Departure | Left Emergency Dept. |")
    for _, r in hadm_xfr.iterrows():
        careunit = fmt_null(r["careunit"])
        evtype   = fmt_null(r["eventtype"])
        intime   = fmt_null(r["intime"])
        if evtype not in ("discharge", "admit"):
            timeline.append(f"| {intime} | Transfer | → {careunit} ({evtype}) |")
    for _, r in hadm_icu.iterrows():
        timeline.append(
            f"| {r['intime']} | ICU Admission | {r['first_careunit']} (LOS: {r['los']:.1f} days) |"
        )
    timeline.append(f"| {dischtime} | Discharge | To {disch_loc} |")
    if deathtime != "N/A":
        timeline.append(f"| {deathtime} | **IN-HOSPITAL DEATH** | |")

    # ── Markdown report ───────────────────────────────────────────────────────
    lines = []
    lines.append(f"# Encounter Report — HADM {hadm_id}")
    lines.append("")
    lines.append("> **Source files:** `hosp/admissions.csv.gz`, `hosp/diagnoses_icd.csv.gz`, "
                 "`hosp/d_icd_diagnoses.csv.gz`, `hosp/procedures_icd.csv.gz`, "
                 "`hosp/d_icd_procedures.csv.gz`, `hosp/services.csv.gz`, "
                 "`hosp/transfers.csv.gz`, `hosp/drgcodes.csv.gz`, "
                 "`icu/icustays.csv.gz`, `icu/procedureevents.csv.gz`, `icu/chartevents.csv.gz`")
    lines.append("")

    # 1. Encounter Info
    lines.append("## 1. Encounter Information")
    lines.append("")
    lines.append(f"| Field | Value |")
    lines.append(f"|---|---|")
    lines.append(f"| Hospital Admission ID | {hadm_id} |")
    lines.append(f"| Subject ID | {subject_id} |")
    lines.append(f"| Patient Sex | {patient_sex} |")
    lines.append(f"| Patient Anchor Age (at anchor year) | {patient_age} |")
    lines.append(f"| Anchor Year | {anchor_year} |")
    lines.append(f"| Admission Time | {admittime} |")
    lines.append(f"| Discharge Time | {dischtime} |")
    lines.append(f"| Admission Type | {adm_type} |")
    lines.append(f"| Admission Location | {adm_loc} |")
    lines.append(f"| Discharge Location | {disch_loc} |")
    lines.append(f"| Insurance | {insurance} |")
    lines.append(f"| Language | {language} |")
    lines.append(f"| Marital Status | {marital} |")
    lines.append(f"| Race/Ethnicity | {race} |")
    lines.append(f"| ED Registration | {edregtime} |")
    lines.append(f"| ED Departure | {edouttime} |")
    lines.append(f"| In-Hospital Mortality | {'YES — Death time: ' + deathtime if expired else 'No'} |")
    lines.append(f"| Date of Death (overall) | {dod} |")
    lines.append("")

    # 2. Hospital Visit Reason (DRG + primary diagnosis)
    lines.append("## 2. Hospital Visit Reason")
    lines.append("")
    if not hadm_drg.empty:
        lines.append("### DRG Codes (MS-DRG / HCFA)")
        lines.append("")
        lines.append("| Type | Code | Description | Severity | Mortality |")
        lines.append("|---|---|---|---|---|")
        for _, r in hadm_drg.iterrows():
            lines.append(
                f"| {fmt_null(r['drg_type'])} | {fmt_null(r['drg_code'])} "
                f"| {fmt_null(r['description'])} "
                f"| {fmt_null(r.get('drg_severity', float('nan')))} "
                f"| {fmt_null(r.get('drg_mortality', float('nan')))} |"
            )
        lines.append("")

    if not hadm_diags.empty:
        primary = hadm_diags[hadm_diags["seq_num"] == 1]
        if not primary.empty:
            lines.append("### Primary Diagnosis (seq_num = 1)")
            lines.append("")
            r = primary.iloc[0]
            lines.append(f"- **ICD-{r['icd_version']} {r['icd_code']}**: {r['title']}")
            lines.append("")

    if not hadm_svc.empty:
        lines.append("### Clinical Services")
        lines.append("")
        lines.append("| Time | Previous Service | Current Service |")
        lines.append("|---|---|---|")
        for _, r in hadm_svc.iterrows():
            lines.append(
                f"| {fmt_null(r['transfertime'])} | {fmt_null(r['prev_service'])} | {r['curr_service']} |"
            )
        lines.append("")

    # 3. Symptoms / Chief Complaint
    lines.append("## 3. Symptoms and Chief Complaint")
    lines.append("")
    lines.append(
        "> **Note:** MIMIC-IV demo does not include free-text nursing/physician notes in this dataset. "
        "Chief complaints and symptom narratives are not available. "
        "Symptoms are inferred from ICD codes and DRG descriptions."
    )
    lines.append("")
    symptom_codes = hadm_diags[hadm_diags["seq_num"] <= 5].copy()
    if not symptom_codes.empty:
        lines.append("Coded conditions (top 5 by sequence) that may reflect presenting symptoms:")
        lines.append("")
        for _, r in symptom_codes.iterrows():
            lines.append(f"- (seq {r['seq_num']}) ICD-{r['icd_version']} `{r['icd_code']}`: {r['title']}")
    lines.append("")

    # 4. Full Diagnoses List
    lines.append("## 4. Diagnoses")
    lines.append("")
    if hadm_diags.empty:
        lines.append("_No diagnoses found for this admission._")
    else:
        lines.append("| Seq | ICD Version | ICD Code | Description |")
        lines.append("|---|---|---|---|")
        for _, r in hadm_diags.iterrows():
            lines.append(
                f"| {r['seq_num']} | ICD-{r['icd_version']} | `{r['icd_code']}` | {r['title']} |"
            )
    lines.append("")

    # 5. ICU Information
    lines.append("## 5. ICU Stays")
    lines.append("")
    if hadm_icu.empty:
        lines.append("_No ICU stay recorded for this admission._")
    else:
        lines.append("| Stay ID | First Care Unit | Last Care Unit | ICU Admit | ICU Discharge | LOS (days) |")
        lines.append("|---|---|---|---|---|---|")
        for _, r in hadm_icu.iterrows():
            lines.append(
                f"| {r['stay_id']} | {r['first_careunit']} | {r['last_careunit']} "
                f"| {r['intime']} | {r['outtime']} | {r['los']:.2f} |"
            )
    lines.append("")

    # 6. ICU Severity / Escalation Indicators
    lines.append("## 6. Escalation / Severity Indicators")
    lines.append("")
    if not all_escalations:
        lines.append("_No escalation indicators detected from ICD codes or ICU procedure events._")
    else:
        lines.append("The following critical conditions or interventions were detected:")
        lines.append("")
        for flag in all_escalations:
            src = "(ICD diagnosis)" if flag in dx_escalations else "(ICU procedure event)"
            if flag in dx_escalations and flag in icu_escalations:
                src = "(ICD + ICU procedure)"
            lines.append(f"- **{flag}** {src}")
    lines.append("")

    # 7. Procedures / Interventions
    lines.append("## 7. Procedures and Interventions")
    lines.append("")
    if hadm_procs.empty:
        lines.append("_No ICD-coded procedures recorded._")
    else:
        lines.append("### ICD-Coded Procedures")
        lines.append("")
        lines.append("| Seq | Date | ICD Version | ICD Code | Description |")
        lines.append("|---|---|---|---|---|")
        for _, r in hadm_procs.iterrows():
            lines.append(
                f"| {r['seq_num']} | {fmt_null(r.get('chartdate', float('nan')))} "
                f"| ICD-{r['icd_version']} | `{r['icd_code']}` | {r['title']} |"
            )
    lines.append("")

    if icu_procedures:
        lines.append("### ICU Procedure Events (from `icu/procedureevents.csv.gz`)")
        lines.append("")
        lines.extend(icu_procedures)
    lines.append("")

    # 8. Critical Findings
    lines.append("## 8. Critical Findings (Charted Events)")
    lines.append("")
    if not critical_charts:
        lines.append("_No critical chart events detected._")
    else:
        lines.extend(critical_charts)
    lines.append("")

    # 9. Timeline Summary
    lines.append("## 9. Timeline Summary")
    lines.append("")
    lines.append("| Time | Event | Detail |")
    lines.append("|---|---|---|")
    for t in sorted(set(timeline)):
        lines.append(t)
    lines.append("")

    # 10. Missing / Ambiguous Data
    lines.append("## 10. Missing / Ambiguous Data")
    lines.append("")
    missing = []
    if edregtime == "N/A":
        missing.append("No ED registration time — admission may not have gone through ED.")
    if adm_loc == "N/A":
        missing.append("Admission location not recorded.")
    if disch_loc == "N/A" and not expired:
        missing.append("Discharge location not recorded.")
    if hadm_procs.empty:
        missing.append("No procedure ICD codes — procedures may not have been coded or were minor.")
    if hadm_icu.empty:
        missing.append("No ICU stay — patient managed on floor/step-down only.")
    if dod == "N/A" and expired:
        missing.append("Hospital expire flag set but no date of death in patients table.")
    if not missing:
        missing.append("No obvious missing critical fields detected.")
    for m in missing:
        lines.append(f"- {m}")
    lines.append("")

    # 11. Manual Review Recommendation
    lines.append("## 11. Manual Review Recommendation")
    lines.append("")
    if review_flags:
        lines.append("**This encounter is flagged for manual review:**")
        lines.append("")
        for f in review_flags:
            lines.append(f"- {f}")
    else:
        lines.append("No specific flags for manual review. Standard clinical review recommended.")
    lines.append("")

    return "\n".join(lines)


# ── Main loop ─────────────────────────────────────────────────────────────────
hadm_ids = sorted(admissions["hadm_id"].unique())
print(f"Generating reports for {len(hadm_ids)} encounters...")

for i, hadm_id in enumerate(hadm_ids, 1):
    report = generate_report(int(hadm_id))
    out_path = OUT_DIR / f"encounter_{hadm_id}.md"
    out_path.write_text(report, encoding="utf-8")
    if i % 25 == 0 or i == len(hadm_ids):
        print(f"  {i}/{len(hadm_ids)} done — last: {hadm_id}")

print(f"\nAll reports written to ./{OUT_DIR}/")
