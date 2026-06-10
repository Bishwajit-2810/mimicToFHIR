"""Cohort filtering for the bundle / fhir_blind / all pipelines.

Exposes one CLI flag per dimension shown on the dashboard "axes" (demographics +
encounter details), letting the user carve out a subset of patients and route
their FHIR and FHIR (Blinded) bundles into a dedicated, self-describing folder under
``filtered/``.

Dimensions (and the MIMIC column each maps to):

  Demographics
    --gender              hosp.patients.gender            male | female
    --min-age/--max-age   hosp.patients.anchor_age        inclusive range
    --anchor-year         hosp.patients.anchor_year       exact year
    --anchor-year-group   hosp.patients.anchor_year_group substring (e.g. 2011)
    --deceased            hosp.patients.dod IS NOT NULL    has a date of death
    --race                hosp.admissions.race            substring
    --ethnicity           hosp.admissions.race            substring (hispanic/…)
    --language            hosp.admissions.language        substring
    --marital-status      hosp.admissions.marital_status  substring

  Encounter
    --service             hosp.services.curr_service      code (MED) or name
    --admission-type      hosp.admissions.admission_type  substring
    --admit-source        hosp.admissions.admission_location   substring
    --discharge-location  hosp.admissions.discharge_location   substring
    --insurance           hosp.admissions.insurance       substring
    --expired             hosp.admissions.hospital_expire_flag = 1 (death this stay)

All filters combine with AND. A patient is selected if *any* of their
admissions / services satisfy the admission/service-level filters.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path

# Service display names, kept in sync with mimic_to_bundle._SERVICE_DISPLAY so
# users can pass either the MIMIC code (MED) or the human name ("medicine").
from etl.mimic_to_bundle import _SERVICE_DISPLAY

FILTERED_ROOT = Path("filtered")

# Subfolder names inside filtered/<slug>/ — one for each pipeline.
FHIR_SUBDIR = "fhir"
FHIR_BLIND_SUBDIR = "fhir_blind"

_NAME_TO_CODE = {display.lower(): code for code, display in _SERVICE_DISPLAY.items()}

# Admission-level substring (ILIKE) filters.
#   (arg dest, db column, slug label)
# Several flags can target the same column (race / ethnicity) — that's fine.
_ADMISSION_TEXT_FILTERS = [
    ("race",               "race",               "race"),
    ("ethnicity",          "race",               "ethnicity"),
    ("insurance",          "insurance",          "insurance"),
    ("language",           "language",           "language"),
    ("marital_status",     "marital_status",     "marital"),
    ("admission_type",     "admission_type",     "admissiontype"),
    ("admit_source",       "admission_location", "admitsource"),
    ("discharge_location", "discharge_location", "discharge"),
]


def normalize_gender(value: str) -> str:
    v = value.strip().lower()
    if v in ("m", "male"):
        return "M"
    if v in ("f", "female"):
        return "F"
    raise ValueError(f"Unknown gender {value!r} (use male/female)")


def normalize_service(value: str) -> str:
    """Accept a MIMIC service code (MED) or a display name ("medicine")."""
    v = value.strip()
    if v.upper() in _SERVICE_DISPLAY:
        return v.upper()
    if v.lower() in _NAME_TO_CODE:
        return _NAME_TO_CODE[v.lower()]
    # Fall back to the raw upper-cased token so unknown-but-valid codes still work.
    return v.upper()


def add_filter_args(parser: argparse.ArgumentParser) -> None:
    """Attach cohort-filter options to a subcommand parser."""
    g = parser.add_argument_group("cohort filters (extract a subset into filtered/<slug>/)")
    # Demographics
    g.add_argument("--gender", default=None, help="male | female")
    g.add_argument("--min-age", type=int, default=None, help="Minimum anchor_age (inclusive)")
    g.add_argument("--max-age", type=int, default=None, help="Maximum anchor_age (inclusive)")
    g.add_argument("--anchor-year", type=int, default=None, help="Exact anchor_year")
    g.add_argument("--anchor-year-group", default=None, help="Match anchor_year_group containing this text")
    g.add_argument("--deceased", action="store_true", help="Only patients with a recorded date of death")
    g.add_argument("--race", default=None, help="Match patients whose race contains this text")
    g.add_argument("--ethnicity", default=None, help="Match race/ethnicity text (e.g. hispanic)")
    g.add_argument("--language", default=None, help="Match language containing this text")
    g.add_argument("--marital-status", default=None, help="Match marital_status containing this text")
    # Encounter
    g.add_argument("--service", default=None,
                   help="Hospital service code (MED) or name (medicine). See README for the full list.")
    g.add_argument("--admission-type", default=None, help="Match admission_type containing this text")
    g.add_argument("--admit-source", default=None, help="Match admission_location (admit source)")
    g.add_argument("--discharge-location", default=None, help="Match discharge_location (disposition)")
    g.add_argument("--insurance", default=None, help="Match patients whose insurance contains this text")
    g.add_argument("--expired", action="store_true", help="Only patients with an in-hospital death")


def extract_filters(args) -> dict:
    """Pull the active (non-default) filters off parsed args into a normalized dict."""
    filters: dict = {}
    if getattr(args, "gender", None):
        filters["gender"] = normalize_gender(args.gender)
    if getattr(args, "service", None):
        filters["service"] = normalize_service(args.service)
    if getattr(args, "min_age", None) is not None:
        filters["min_age"] = args.min_age
    if getattr(args, "max_age", None) is not None:
        filters["max_age"] = args.max_age
    if getattr(args, "anchor_year", None) is not None:
        filters["anchor_year"] = args.anchor_year
    if getattr(args, "anchor_year_group", None):
        filters["anchor_year_group"] = args.anchor_year_group
    if getattr(args, "deceased", False):
        filters["deceased"] = True
    if getattr(args, "expired", False):
        filters["expired"] = True
    for dest, _col, _label in _ADMISSION_TEXT_FILTERS:
        val = getattr(args, dest, None)
        if val:
            filters[dest] = val
    return filters


def _slugify(value) -> str:
    return re.sub(r"[^a-z0-9]+", "-", str(value).strip().lower()).strip("-")


def slug_for(filters: dict) -> str:
    """Build a stable, human-readable folder name from the active filters."""
    parts: list[str] = []
    if "gender" in filters:
        parts.append("gender-" + ("male" if filters["gender"] == "M" else "female"))
    if "service" in filters:
        parts.append("service-" + _slugify(filters["service"]))
    if "min_age" in filters or "max_age" in filters:
        lo = filters.get("min_age", "min")
        hi = filters.get("max_age", "max")
        parts.append(f"age-{lo}-{hi}")
    if "anchor_year" in filters:
        parts.append(f"anchoryear-{filters['anchor_year']}")
    if "anchor_year_group" in filters:
        parts.append("anchoryeargroup-" + _slugify(filters["anchor_year_group"]))
    for dest, _col, label in _ADMISSION_TEXT_FILTERS:
        if dest in filters:
            parts.append(f"{label}-{_slugify(filters[dest])}")
    if filters.get("deceased"):
        parts.append("deceased")
    if filters.get("expired"):
        parts.append("expired")
    return "_".join(parts) if parts else "all"


def default_output_base(filters: dict) -> Path:
    """Where a filtered extract lands when --output is not given."""
    return FILTERED_ROOT / slug_for(filters)


def select_subject_ids(cur, filters: dict, *, random_sample: bool = True,
                       limit: int | None = None, offset: int = 0) -> list[int]:
    """Return subject_ids matching ``filters``.

    ``cur`` is a psycopg2 cursor (RealDictCursor expected). Selection mirrors the
    default behaviour of the pipelines: random sample capped at 10,000 unless a
    limit is given, or sequential (by subject_id) when ``random_sample`` is False.
    """
    conds: list[str] = []
    params: list = []
    need_services = False
    need_admissions = False

    # ── patient-level ──
    if "gender" in filters:
        conds.append("p.gender = %s")
        params.append(filters["gender"])
    if "min_age" in filters:
        conds.append("p.anchor_age >= %s")
        params.append(filters["min_age"])
    if "max_age" in filters:
        conds.append("p.anchor_age <= %s")
        params.append(filters["max_age"])
    if "anchor_year" in filters:
        conds.append("p.anchor_year = %s")
        params.append(filters["anchor_year"])
    if "anchor_year_group" in filters:
        conds.append("p.anchor_year_group ILIKE %s")
        params.append(f"%{filters['anchor_year_group']}%")
    if filters.get("deceased"):
        conds.append("p.dod IS NOT NULL")

    # ── service-level ──
    if "service" in filters:
        need_services = True
        conds.append("s.curr_service = %s")
        params.append(filters["service"])

    # ── admission-level ──
    for dest, col, _label in _ADMISSION_TEXT_FILTERS:
        if dest in filters:
            need_admissions = True
            conds.append(f"a.{col} ILIKE %s")
            params.append(f"%{filters[dest]}%")
    if filters.get("expired"):
        need_admissions = True
        conds.append("a.hospital_expire_flag = 1")

    joins = ""
    if need_services:
        joins += " JOIN hosp.services s ON s.subject_id = p.subject_id"
    if need_admissions:
        joins += " JOIN hosp.admissions a ON a.subject_id = p.subject_id"
    where = (" WHERE " + " AND ".join(conds)) if conds else ""

    inner = f"SELECT DISTINCT p.subject_id FROM hosp.patients p{joins}{where}"
    order = "RANDOM()" if random_sample else "subject_id"
    query = f"SELECT subject_id FROM ({inner}) t ORDER BY {order}"
    if not random_sample and offset:
        query += f" OFFSET {int(offset)}"
    effective_limit = limit if limit is not None else (10000 if random_sample else None)
    if effective_limit:
        query += f" LIMIT {int(effective_limit)}"

    cur.execute(query, params)
    return [r["subject_id"] for r in cur.fetchall()]
