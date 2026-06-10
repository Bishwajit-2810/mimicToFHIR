"""Shared FHIR bundle parsing logic used by both web/app.py and web/fhir_blind_app.py."""

import base64
import re
from datetime import datetime

VITAL_LOINC = {
    "8867-4":  "Heart Rate",
    "8480-6":  "Systolic BP",
    "8462-4":  "Diastolic BP",
    "8478-0":  "Mean BP",
    "9279-1":  "Respiratory Rate",
    "8310-5":  "Temperature",
    "59408-5": "SpO2",
    "2708-6":  "SpO2",       # MIMIC chartevents item 220277 emits this code
    "29463-7": "Weight",
    "8302-2":  "Height",
}

VITAL_ICONS = {
    "Heart Rate":       "fa-heart-pulse",
    "Systolic BP":      "fa-gauge-high",
    "Diastolic BP":     "fa-gauge",
    "Mean BP":          "fa-gauge",
    "Respiratory Rate": "fa-lungs",
    "Temperature":      "fa-thermometer-half",
    "SpO2":             "fa-percent",
    "Weight":           "fa-weight-scale",
    "Height":           "fa-ruler-vertical",
}

VITAL_NORMAL = {
    "Heart Rate":       (60, 100),
    "Systolic BP":      (90, 140),
    "Diastolic BP":     (60, 90),
    "Mean BP":          (70, 100),
    "Respiratory Rate": (12, 20),
    "Temperature":      (97.0, 99.5),
    "SpO2":             (95, 100),
    "Weight":           None,
    "Height":           None,
}


def fmt_dt(raw: str | None) -> str | None:
    if not raw:
        return None
    try:
        s = re.sub(r"[+-]\d{2}:\d{2}$", "", raw).replace("Z", "")
        dt = datetime.fromisoformat(s)
        return dt.strftime("%Y-%m-%d %H:%M") if "T" in s else s
    except Exception:
        return raw


def concept_text(obj: dict) -> str:
    if not obj:
        return ""
    if obj.get("text"):
        return obj["text"]
    for c in obj.get("coding", []):
        if c.get("display"):
            return c["display"]
        if c.get("code"):
            return c["code"]
    return ""


def _demographics(patient: dict, all_encounters: list) -> dict:
    if not patient:
        return {}

    race = ethnicity = birth_sex = anchor_year = "Unknown"
    for ext in patient.get("extension", []):
        url = ext.get("url", "")
        if "us-core-race" in url:
            for n in ext.get("extension", []):
                if n.get("url") == "text":
                    race = n.get("valueString", race)
        elif "us-core-ethnicity" in url:
            for n in ext.get("extension", []):
                if n.get("url") == "text":
                    ethnicity = n.get("valueString", ethnicity)
        elif "us-core-birthsex" in url:
            birth_sex = ext.get("valueCode", birth_sex)
        elif "anchor-year-group" in url:
            anchor_year = ext.get("valueString", anchor_year)

    subject_id = next(
        (
            i.get("value", "")
            for i in patient.get("identifier", [])
            if "patient" in i.get("system", "")
        ),
        "",
    )

    birth_date = patient.get("birthDate", "")
    deceased = patient.get("deceasedDateTime", "")

    age = None
    if birth_date and all_encounters:
        dates = [
            e.get("period", {}).get("start", "")
            for e in all_encounters
            if e.get("period", {}).get("start")
        ]
        if dates:
            latest = max(dates)
            try:
                bd = datetime.strptime(birth_date, "%Y-%m-%d")
                ed = datetime.fromisoformat(re.sub(r"[+-]\d{2}:\d{2}$", "", latest))
                age = (ed - bd).days // 365
            except Exception:
                pass

    marital = concept_text(patient.get("maritalStatus", {}))
    langs = [
        concept_text(c.get("language", {}))
        for c in patient.get("communication", [])
        if c.get("language")
    ]

    return {
        "subjectId": subject_id,
        "gender": patient.get("gender", "unknown").capitalize(),
        "birthDate": birth_date,
        "age": age,
        "deceased": fmt_dt(deceased) if deceased else None,
        "race": race,
        "ethnicity": ethnicity,
        "birthSex": birth_sex,
        "maritalStatus": marital,
        "language": ", ".join(langs) or "Unknown",
        "anchorYear": anchor_year,
    }


def _parse_vital_obs(obs: dict) -> dict | None:
    loinc = next(
        (
            c.get("code")
            for c in obs.get("code", {}).get("coding", [])
            if "loinc" in c.get("system", "").lower()
        ),
        None,
    )
    name = VITAL_LOINC.get(loinc or "", "")
    if not name:
        return None
    qty = obs.get("valueQuantity", {})
    val = qty.get("value") if qty else obs.get("valueString")
    if val is None:
        return None
    unit = qty.get("unit", "")
    eff = obs.get("effectiveDateTime", "")
    nr = VITAL_NORMAL.get(name)
    status = "normal"
    if nr and isinstance(val, (int, float)):
        status = "normal" if nr[0] <= val <= nr[1] else "abnormal"
    return {
        "name": name,
        "value": val,
        "unit": unit,
        "raw": eff,
        "time": fmt_dt(eff),
        "icon": VITAL_ICONS.get(name, "fa-stethoscope"),
        "status": status,
        "normalRange": nr,
        "encounterRef": obs.get("encounter", {}).get("reference", ""),
    }


def _vitals(obs_list: list) -> list:
    latest: dict[str, dict] = {}
    for obs in obs_list:
        parsed = _parse_vital_obs(obs)
        if parsed is None:
            continue
        name = parsed["name"]
        if name not in latest or parsed["raw"] > latest[name]["raw"]:
            latest[name] = parsed
    return sorted(latest.values(), key=lambda x: x["name"])


def _vitals_by_encounter(obs_list: list) -> dict[str, list]:
    groups: dict[str, list] = {}
    for obs in obs_list:
        parsed = _parse_vital_obs(obs)
        if parsed is None:
            continue
        enc = parsed["encounterRef"]
        groups.setdefault(enc, []).append(parsed)
    for enc in groups:
        groups[enc].sort(key=lambda x: x["name"])
    return groups


def _parse_lab_obs(obs: dict) -> dict | None:
    name = concept_text(obs.get("code", {}))
    if not name:
        return None
    qty = obs.get("valueQuantity", {})
    val = qty.get("value") if qty else obs.get("valueString", "")
    unit = qty.get("unit", "") if qty else ""
    flag = next(
        (
            c.get("code", "")
            for i in obs.get("interpretation", [])
            for c in i.get("coding", [])
        ),
        "",
    )
    rr = obs.get("referenceRange", [{}])[0] if obs.get("referenceRange") else {}
    ref_lo = rr.get("low", {}).get("value") if rr else None
    ref_hi = rr.get("high", {}).get("value") if rr else None
    eff = obs.get("effectiveDateTime", "")
    return {
        "name": name,
        "value": val,
        "unit": unit,
        "flag": flag,
        "refLow": ref_lo,
        "refHigh": ref_hi,
        "time": fmt_dt(eff),
        "rawDt": eff,
        "encounterRef": obs.get("encounter", {}).get("reference", ""),
    }


def _labs(obs_list: list) -> list:
    seen: dict[str, dict] = {}
    for obs in obs_list:
        parsed = _parse_lab_obs(obs)
        if parsed is None:
            continue
        name = parsed["name"]
        if name not in seen or parsed["rawDt"] > seen[name]["rawDt"]:
            seen[name] = parsed
    return sorted(seen.values(), key=lambda x: x["name"])


def _labs_by_encounter(obs_list: list) -> dict[str, list]:
    groups: dict[str, list] = {}
    for obs in obs_list:
        parsed = _parse_lab_obs(obs)
        if parsed is None:
            continue
        enc = parsed["encounterRef"]
        groups.setdefault(enc, []).append(parsed)
    for enc in groups:
        groups[enc].sort(key=lambda x: x["name"])
    return groups


def _conditions(conds: list) -> list:
    out = []
    for c in conds:
        code_obj = c.get("code", {})
        name = concept_text(code_obj)
        icd = next((cd.get("code", "") for cd in code_obj.get("coding", [])), "")
        sys_raw = next((cd.get("system", "") for cd in code_obj.get("coding", [])), "")
        icd_sys = (
            "ICD-10" if "icd-10" in sys_raw else ("ICD-9" if "icd-9" in sys_raw else "")
        )
        status = next(
            (
                cd.get("code", "")
                for s in [c.get("clinicalStatus", {})]
                for cd in s.get("coding", [])
            ),
            "",
        )
        out.append(
            {
                "name": name,
                "code": icd,
                "codeSystem": icd_sys,
                "status": status,
                "encounterRef": c.get("encounter", {}).get("reference", ""),
            }
        )
    return out


def _medications(meds: list) -> list:
    seen: dict[str, dict] = {}
    for m in meds:
        name = concept_text(m.get("medicationCodeableConcept", {}))
        if not name or name in seen:
            continue

        dosages = m.get("dosageInstruction", [{}])
        d = dosages[0] if dosages else {}
        route = concept_text(d.get("route", {}))
        dose_val = next(
            (
                f"{dr.get('doseQuantity', {}).get('value', '')} "
                f"{dr.get('doseQuantity', {}).get('unit', '')}".strip()
                for dr in d.get("doseAndRate", [])
                if dr.get("doseQuantity", {}).get("value") is not None
            ),
            "",
        )

        period = m.get("dispenseRequest", {}).get("validityPeriod", {})
        seen[name] = {
            "name": name,
            "status": m.get("status", ""),
            "dose": dose_val,
            "route": route,
            "start": fmt_dt(period.get("start")),
            "end": fmt_dt(period.get("end")),
            "encounterRef": m.get("encounter", {}).get("reference", ""),
        }
    return sorted(seen.values(), key=lambda x: x["name"])


def _encounters(encs: list) -> list:
    hospital, icu = [], []
    for e in encs:
        cls = e.get("class", {}).get("code", "")
        period = e.get("period", {})
        types = e.get("type", [])
        locs = e.get("location", [])
        hosp_info = e.get("hospitalization", {})
        exts = {x.get("url"): x for x in e.get("extension", [])}
        ins = exts.get("http://mimic.mit.edu/fhir/StructureDefinition/insurance", {}).get("valueString", "")
        los = exts.get("http://mimic.mit.edu/fhir/StructureDefinition/los", {}).get("valueDecimal")

        svc = e.get("serviceType", {})
        svc_codings = svc.get("coding", []) if svc else []
        svc_label = ""
        if svc_codings:
            c0 = svc_codings[0]
            code = c0.get("code", "")
            display = c0.get("display", "")
            if code and display:
                svc_label = f"{code}/{display}"
            elif display:
                svc_label = display
            elif code:
                svc_label = code

        row = {
            "id": "urn:uuid:" + e.get("id", ""),
            "cls": cls,
            "type": concept_text(types[0]) if types else "",
            "status": e.get("status", ""),
            "start": fmt_dt(period.get("start")),
            "end": fmt_dt(period.get("end")),
            "rawStart": period.get("start", ""),
            "serviceType": svc_label,
            "location": locs[0].get("location", {}).get("display", "") if locs else "",
            "admitSource": concept_text(hosp_info.get("admitSource", {})),
            "dischDisp": concept_text(hosp_info.get("dischargeDisposition", {})),
            "insurance": ins,
            "los": round(los, 2) if los is not None else None,
            "partOf": e.get("partOf", {}).get("reference", ""),
            "children": [],
            "participantRefs": [
                p.get("individual", {}).get("reference", "")
                for p in e.get("participant", [])
            ],
        }

        if row["partOf"]:
            icu.append(row)
        else:
            hospital.append(row)

    by_id = {h["id"]: h for h in hospital}
    for i in icu:
        parent = by_id.get(i["partOf"])
        if parent is not None:
            parent["children"].append(i)
        else:
            hospital.append(i)

    hospital.sort(key=lambda x: x["rawStart"], reverse=True)
    return hospital


def _diagnostic_reports(rpts: list) -> list:
    out = []
    for r in rpts:
        cats = r.get("category", [])
        out.append(
            {
                "name": concept_text(r.get("code", {})),
                "category": concept_text(cats[0]) if cats else "",
                "time": fmt_dt(r.get("effectiveDateTime")),
                "status": r.get("status", ""),
                "encounterRef": r.get("encounter", {}).get("reference", ""),
            }
        )
    out.sort(key=lambda x: x.get("time") or "", reverse=True)
    return out


def _procedures(procs: list) -> list:
    out = []
    for p in procs:
        out.append(
            {
                "name": concept_text(p.get("code", {})),
                "time": fmt_dt(p.get("performedDateTime")),
                "status": p.get("status", ""),
                "encounterRef": p.get("encounter", {}).get("reference", ""),
            }
        )
    out.sort(key=lambda x: x.get("time") or "", reverse=True)
    return out


def _practitioners(pract_list: list) -> dict:
    result = {}
    for p in pract_list:
        uid = "urn:uuid:" + p.get("id", "")
        names = p.get("name", [{}])
        n = names[0] if names else {}
        given = " ".join(n.get("given", []))
        family = n.get("family", "")
        full = f"{given} {family}".strip()
        ident = next(
            (i.get("value", "") for i in p.get("identifier", [])),
            "",
        )
        result[uid] = {"name": full, "providerId": ident}
    return result


_NOTE_LOINC_LABEL: dict[str, str] = {
    "18842-5": "Discharge Summary",
    "18726-0": "Radiology Report",
    "68604-8": "Radiology Report",
    "11524-6": "ECG Study",
    "34750-4": "Echocardiography",
    "47049-6": "Pharmacy Note",
    "34109-3": "Note",
}

_NOTE_CATEGORY: dict[str, str] = {
    "18842-5": "discharge",
    "18726-0": "radiology",
    "68604-8": "radiology",
}


def _notes(doc_refs: list) -> list:
    out = []
    for doc in doc_refs:
        type_obj = doc.get("type", {})
        codings = type_obj.get("coding", [])
        loinc_code = next(
            (c.get("code", "") for c in codings if "loinc" in c.get("system", "").lower()),
            "",
        )
        type_display = (
            _NOTE_LOINC_LABEL.get(loinc_code)
            or concept_text(type_obj)
            or "Note"
        )
        category = _NOTE_CATEGORY.get(loinc_code, "other")

        text = ""
        for content in doc.get("content", []):
            raw = content.get("attachment", {}).get("data", "")
            if raw:
                try:
                    text = base64.b64decode(raw).decode("utf-8", errors="replace")
                except Exception:
                    text = raw
                break

        ctx = doc.get("context", {})
        enc_refs = ctx.get("encounter", [])
        enc_ref = enc_refs[0].get("reference", "") if enc_refs else ""
        raw_date = doc.get("date", "")

        out.append(
            {
                "id": doc.get("id", ""),
                "typeDisplay": type_display,
                "loincCode": loinc_code,
                "category": category,
                "date": fmt_dt(raw_date),
                "rawDate": raw_date,
                "text": text,
                "preview": text[:300].strip() if text else "",
                "encounterRef": enc_ref,
            }
        )
    out.sort(key=lambda x: x.get("rawDate") or "", reverse=True)
    return out


def parse_bundle(bundle: dict) -> dict:
    resources: dict[str, list] = {
        "Patient": [],
        "Encounter": [],
        "Condition": [],
        "ObsLab": [],
        "ObsVital": [],
        "ObsOther": [],
        "MedicationRequest": [],
        "DiagnosticReport": [],
        "Procedure": [],
        "Practitioner": [],
        "DocumentReference": [],
    }

    for entry in bundle.get("entry", []):
        r = entry.get("resource", {})
        rt = r.get("resourceType", "")
        if rt == "Patient":
            resources["Patient"].append(r)
        elif rt == "Encounter":
            resources["Encounter"].append(r)
        elif rt == "Condition":
            resources["Condition"].append(r)
        elif rt == "Observation":
            cats = {
                cd.get("code", "")
                for cat in r.get("category", [])
                for cd in cat.get("coding", [])
            }
            if "laboratory" in cats:
                resources["ObsLab"].append(r)
            elif "vital-signs" in cats:
                resources["ObsVital"].append(r)
            else:
                resources["ObsOther"].append(r)
        elif rt == "MedicationRequest":
            resources["MedicationRequest"].append(r)
        elif rt == "DiagnosticReport":
            resources["DiagnosticReport"].append(r)
        elif rt == "Procedure":
            resources["Procedure"].append(r)
        elif rt == "Practitioner":
            resources["Practitioner"].append(r)
        elif rt == "DocumentReference":
            resources["DocumentReference"].append(r)

    patient = resources["Patient"][0] if resources["Patient"] else {}
    raw_encs = resources["Encounter"]

    demo = _demographics(patient, raw_encs)
    encs = _encounters(raw_encs)
    conds = _conditions(resources["Condition"])
    meds = _medications(resources["MedicationRequest"])
    vitals = _vitals(resources["ObsVital"])
    labs = _labs(resources["ObsLab"])
    reports = _diagnostic_reports(resources["DiagnosticReport"])
    procs = _procedures(resources["Procedure"])
    notes = _notes(resources["DocumentReference"])

    prac_lookup = _practitioners(resources["Practitioner"])
    vitals_by_enc = _vitals_by_encounter(resources["ObsVital"])
    labs_by_enc = _labs_by_encounter(resources["ObsLab"])
    notes_by_enc: dict[str, list] = {}
    for n in notes:
        notes_by_enc.setdefault(n["encounterRef"], []).append(n)

    for enc in encs:
        eid = enc["id"]

        own_vitals = vitals_by_enc.get(eid, [])
        if not own_vitals:
            child_vitals: list = []
            for child in enc.get("children", []):
                child_vitals.extend(vitals_by_enc.get(child["id"], []))
            own_vitals = sorted(child_vitals, key=lambda x: x["name"])

        enc_conds = [c for c in conds if c.get("encounterRef") == eid]
        enc_meds = [m for m in meds if m.get("encounterRef") == eid]
        enc_procs = [p for p in procs if p.get("encounterRef") == eid]
        enc_rpts = [r for r in reports if r.get("encounterRef") == eid]
        enc_labs = labs_by_enc.get(eid, [])
        enc_notes = notes_by_enc.get(eid, [])

        chief_complaint = enc_conds[0]["name"] if enc_conds else None

        providers = [
            prac_lookup[ref]
            for ref in enc.get("participantRefs", [])
            if ref in prac_lookup
        ]

        enc["encounterData"] = {
            "chiefComplaint": chief_complaint,
            "providers": providers,
            "conditions": enc_conds,
            "medications": enc_meds,
            "procedures": enc_procs,
            "diagnosticReports": enc_rpts,
            "vitals": own_vitals,
            "labs": enc_labs,
            "notes": enc_notes,
        }

    chief = "Not recorded"
    if encs and conds:
        recent_id = encs[0]["id"]
        primary = next(
            (c for c in conds if c["encounterRef"] == recent_id),
            None,
        )
        if primary:
            chief = primary["name"]

    return {
        "demographics": demo,
        "vitals": vitals,
        "conditions": conds,
        "medications": meds,
        "labs": labs,
        "diagnosticReports": reports,
        "procedures": procs,
        "encounters": encs,
        "notes": notes,
        "chiefComplaint": chief,
    }
