# FHIR Bundles — Repository Analysis

Generated: 2026-05-12

**Overview:**

- **Repository root:** contains application code and FHIR conversion outputs (see sections below).
- **Focus file analyzed:** `fhir_bundles/10004457.json` (active file in editor).

**Top-level files & folders:**

- .git/, .venv/, project config (`pyproject.toml`, `.python-version`)
- Application scripts: `app.py`, `main.py`, `load_mimic.py`, `mimic_to_bundle.py`, `mimic_to_fhir.py`
- Documentation: `README.md`, `HOWTO.md`, `README.txt`, `LICENSE.txt`, `SHA256SUMS.txt`
- Data folders: `fhir_bundles/`, `fhir_output/`, `sql/`, `static/`, `hosp/`, `icu/`

**`fhir_bundles/` directory:**

- Contains many individual patient bundle JSON files (examples: `10000032.json`, `10004457.json`, `10040025.json`, ...). These are FHIR Bundle resources exported per patient/subject.

**`fhir_output/` directory:**

- Contains newline-delimited JSON (NDJSON) files by resource type:
  - `Condition.ndjson`
  - `DiagnosticReport.ndjson`
  - `Encounter.ndjson`
  - `MedicationRequest.ndjson`
  - `Observation.ndjson`
  - `Patient.ndjson`
  - `Procedure.ndjson`

---

**Sample bundle analyzed: `fhir_bundles/10004457.json`**

Top-level bundle fields observed:

- `resourceType`: "Bundle"
- `type`: "transaction"
- `entry`: array of entries; each entry contains `fullUrl`, `resource`, and `request` (with `method` and `url`).

Entry-level common fields:

- `fullUrl` — a URN UUID for local reference (e.g., `urn:uuid:6e8a74e9-...`).
- `resource` — the FHIR resource object (Organization, Patient, Practitioner, Encounter, Condition, ...).
- `request` — HTTP action metadata used when the bundle is executed (e.g., `method`: `POST`, `url`: `Condition`).

Resource types present in this bundle (observed):

- `Organization`
- `Patient`
- `Practitioner` (many)
- `Encounter` (many)
- `Condition` (many)

For each resource type below, I list the fields seen in this bundle and example/value shape.

**Organization**

- `resourceType` (Organization)
- `id` (UUID)
- `identifier` (array): objects with `system`, `value`
- `active` (boolean)
- `type` (array): `coding` (system, code, display), `text`
- `name` (string)
- `address` (array): `line` (array of strings), `city`, `state`, `postalCode`, `country`

Example:

- `name`: "Beth Israel Deaconess Medical Center"

**Patient**

- `resourceType` (Patient)
- `id` (UUID)
- `extension` (array): observed extensions include
  - `http://hl7.org/fhir/us/core/StructureDefinition/us-core-race` with nested `ombCategory` (`valueCoding`) and `text` (`valueString`)
  - `http://hl7.org/fhir/us/core/StructureDefinition/us-core-ethnicity` similar structure
  - `http://hl7.org/fhir/us/core/StructureDefinition/us-core-birthsex` (`valueCode`)
  - `http://mimic.mit.edu/fhir/StructureDefinition/anchor-year-group` (`valueString`)
- `identifier` (array): has `type` (coding + text), `system`, `value` (patient MRN like `10004457`)
- `name` (array): `use`, `family`, `given` (array)
- `gender` (string; e.g., `male`)
- `birthDate` (date string)
- `maritalStatus` (object): `coding` (system, code, display), `text`
- `communication` (array): `language` (coding + text)

Notes: the patient's `birthDate` values in this synthetic dataset appear far-future (obfuscated) — e.g., `2075-07-01` — this is a data-masking artifact often used in demo datasets.

**Practitioner**

- `resourceType` (Practitioner)
- `id` (UUID)
- `identifier` (array): `system` (e.g., `http://mimic.mit.edu/fhir/provider`), `value` (provider code like `P98XG1`)
- `active` (boolean)
- `name` (array): `family`, `given` (array)

Many `Practitioner` entries include only identifying fields and are meant to populate `Encounter.participant` references.

**Encounter**

- `resourceType` (Encounter)
- `id` (UUID)
- `status` (string; e.g., `finished`)
- `class` (object): `system`, `code`, `display` (e.g., inpatient, ICU)
- `type` (array): each has `coding` (system, code, display) and `text`
- `subject` (reference) — reference to `Patient` via `urn:uuid:...`
- `serviceProvider` (reference + display) — reference to `Organization`
- `period` (object): `start`, `end` (dateTime strings)
- `hospitalization` (object): `admitSource` (`text`), `dischargeDisposition` (`text`)
- `participant` (array): each has `individual.reference` (Practitioner)
- `location` (array): `location.display`, `status`
- `partOf` (reference) — used to relate ICU stays to parent encounter
- `extension` (array) — custom extensions seen:
  - `http://mimic.mit.edu/fhir/StructureDefinition/insurance` (`valueString`, e.g., `Medicare`)
  - `http://mimic.mit.edu/fhir/StructureDefinition/los` (`valueDecimal`) — length of stay in days

**Condition**

- `resourceType` (Condition)
- `id` (UUID)
- `clinicalStatus` (object): `coding` (system, code)
- `verificationStatus` (object): `coding` (system, code)
- `category` (array): `coding` (system, code, display)
- `code` (object): `coding` (system, code, display) and `text`
  - Coding systems observed: ICD-9-CM (`http://hl7.org/fhir/sid/icd-9-cm`), ICD-10-CM (`http://hl7.org/fhir/sid/icd-10-cm`)
- `subject` (reference) — Patient
- `encounter` (reference) — Encounter
- `onsetDateTime`, `recordedDate` (dateTime strings)

Patterns & data types observed across resources:

- Identifiers: `system` (URI), `value` (string)
- Codings: `coding` objects with `system`, `code`, `display`
- Dates: `birthDate` (date), `period.start`/`end`, `onsetDateTime`, `recordedDate` (ISO 8601 dateTime strings)
- Extensions: used for dataset-specific metadata (`anchor-year-group`, `insurance`, `los`)
- References: many cross-reference using `urn:uuid:...` matching `fullUrl` values in the same bundle

Terminologies observed:

- SNOMED CT (via `snomed.info/sct`) for some encounter types
- ICD-9-CM and ICD-10-CM for conditions
- HL7 code systems for encounter/condition statuses

Observations about structure and conversion intent:

- Bundles appear to be generated for ingest into a FHIR server (`type`: `transaction`) where each `entry.request` contains a `POST` for the resource type.
- The `fhir_output/` NDJSON files suggest the repo also produces flattened per-resource outputs suitable for bulk import or analysis.
- The bundle links resources via `urn:uuid` fullUrl values rather than persistent server resource IDs — appropriate for transaction imports.

Limitations of this analysis:

- Only one bundle (`10004457.json`) was fully inspected. Other bundles likely follow the same schema but may contain additional resource types (Observation, Procedure, MedicationRequest, DiagnosticReport) — those types are present in the `fhir_output` folder.
- I did not enumerate every single `Condition` entry value (there are many); instead I summarized the schema and representative fields/coding systems.

Recommendations / next steps you might want:

- Generate a summary sheet (CSV) with counts per resource type across all bundles.
- Extract a canonical list of unique `Condition.code` values (ICD codes) for this patient set.
- Convert NDJSON files into a queryable database for analytics.

---

If you want, I can:

- produce a CSV with counts per resource type across `fhir_bundles/` (one line per bundle),
- extract all unique fields and present a normalized schema, or
- generate the per-resource CSV exports from the `fhir_output/` NDJSON files.

-- End of analysis
