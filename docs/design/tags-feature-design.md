# Design: Tags feature (standards, patterns, products)

Status: Draft (hackathon)
Owner: SATRE contributors
Last updated: 2026-07-28

## 1. Summary

Add three new, optional tag types to each SATRE requirement, and surface them on the
Read the Docs site through a dedicated, filterable, exportable page.

- **standards** — maps a requirement to external standards it aligns with, with
  clause / control references.
- **patterns** — documented approaches that partially or fully meet a requirement.
- **products** — built or off-the-shelf things that partially or fully meet a
  requirement.

`patterns` and `products` share the same data shape but are distinct tag types so
they can be filtered independently.

The single source of truth remains `docs/source/spec/specification.yaml`. An authoring
spreadsheet plus a processing script provide a convenient way to bulk-author the tags
and merge them into the YAML. The spreadsheet is an authoring aid, **not** a second
source of truth.

## 2. Goals / non-goals

### Goals

- Extend the requirement data model with the three tag types, all optional and
  backwards compatible.
- Provide a controlled vocabulary for standards.
- Provide an authoring spreadsheet and an idempotent, validating processing script.
- Render tags on the site and provide a separate page with multi-select filters that
  shows a **covered vs not covered** split for the selected filters.
- Keep export flexible (scope and format kept open during the hackathon).

### Non-goals (for now)

- No backend / database. Everything is static and client-side on Read the Docs.
- No change to the existing per-pillar specification tables beyond optionally showing
  tag badges.
- No formal accreditation semantics — mappings are informational.

## 3. Data model

Each item in `specification.yaml` gains three optional fields.

```yaml
- pillar: Information Governance
  capability: Quality Management
  capability_index: "1.2"
  requirement_index: 1.2.04
  statement: You must audit your TRE organisation against relevant requirements and standards.
  guidance: ...
  importance: Mandatory
  architecture_url: https://...
  # --- new optional fields ---
  standards:
    - framework: ISO 27001
      reference: "A.5.35" # clause / control id, free text
    - framework: NHS DSPT
      reference: "1.3.1"
  patterns:
    - name: "Segregated project workspaces"
      description: "Per-project isolated compute + storage boundary."
      coverage: full # full | partial
      maturity: 7 # TRL 1-9
      url: "https://..." # optional
  products:
    - name: "Data Safe Haven"
      description: "Turing's open-source secure environment."
      coverage: partial
      maturity: 9
      url: "https://..."
```

### Controlled vocabulary — standards frameworks (day one)

| Framework (canonical `framework` value)     | Notes                                                              |
| ------------------------------------------- | ------------------------------------------------------------------ |
| `ISO 27001`                                 | Clause / Annex A control reference                                 |
| `NHS DSPT`                                  | NHS Digital Security and Protection Toolkit assertion/evidence ref |
| `Cyber Essentials Plus`                     | Control theme                                                      |
| `Digital Economy Act`                       | Section reference                                                  |
| `NHS Secure Data Environment Specification` | Requirement reference                                              |

The canonical list lives in one place the script and (optionally) the renderer can
read — proposed `docs/source/spec/standards.yaml`:

```yaml
standards:
  - id: iso-27001
    name: ISO 27001
    url: https://www.iso.org/standard/27001
  - id: nhs-dspt
    name: NHS DSPT
    url: https://www.dsptoolkit.nhs.uk/
  - id: cyber-essentials-plus
    name: Cyber Essentials Plus
    url: https://www.ncsc.gov.uk/cyberessentials/
  - id: digital-economy-act
    name: Digital Economy Act
    url: https://www.legislation.gov.uk/ukpga/2017/30/contents
  - id: nhs-sde-spec
    name: NHS Secure Data Environment Specification
    url: https://digital.nhs.uk/services/secure-data-environment-service
```

The processing script validates every `framework` value in the spreadsheet against
`standards.yaml` and rejects / warns on unknowns. New standards are added by editing
`standards.yaml` — one controlled place.

### Field definitions

**standards[]**

- `framework` (required) — must match a `name` in `standards.yaml`.
- `reference` (required) — clause / control id, free text (e.g. `A.5.35`, `1.3.1`).

**patterns[] and products[]** (identical shape)

- `name` (required)
- `description` (required)
- `coverage` (required) — `full` | `partial`
- `maturity` (required) — Technology Readiness Level (TRL), an integer `1`–`9`
- `url` (optional)

`coverage` (enum) and `maturity` (integer 1–9) are validated by the script. TRL labels
for each level are defined in `standards.yaml` and used for tooltips / the reference
sheet.

## 4. Authoring spreadsheet

Filename (proposed): `sourcefiles/satre-tags-authoring.xlsx`. Four sheets.

Each data sheet includes `capability` and `statement` text (copied from
`specification.yaml`) to give authors context while filling in tags. `guidance` is
deliberately excluded to keep rows readable. These context columns are **read-only /
informational**: the processing script keys everything off `requirement_index` and
ignores `capability` / `statement` on read (the YAML remains authoritative for that
text). The script can regenerate/refresh these context columns from the YAML.

### Sheet `standards`

| requirement_index | capability         | statement                                                                         | framework | reference |
| ----------------- | ------------------ | --------------------------------------------------------------------------------- | --------- | --------- |
| 1.2.04            | Quality Management | You must audit your TRE organisation against relevant requirements and standards. | ISO 27001 | A.5.35    |
| 1.2.04            | Quality Management | You must audit your TRE organisation against relevant requirements and standards. | NHS DSPT  | 1.3.1     |

### Sheet `patterns`

| requirement_index | capability | statement | name | description | coverage | maturity | url |
| ----------------- | ---------- | --------- | ---- | ----------- | -------- | -------- | --- |

### Sheet `products`

| requirement_index | capability | statement | name | description | coverage | maturity | url |
| ----------------- | ---------- | --------- | ---- | ----------- | -------- | -------- | --- |

### Sheet `_reference` (read-only helper)

Lists valid framework names, coverage values, and maturity values so authors can use
data-validation dropdowns. Generated by the script (or maintained by hand) from
`standards.yaml`.

One row per mapping (multi-valued tags = multiple rows with the same
`requirement_index`). This keeps the sheet flat and easy to fill in. The
`capability` / `statement` columns repeat per row for context.

## 5. Processing script

Location (proposed): `sourcefiles/process_tags.py`.

Responsibilities:

1. Load `standards.yaml` (controlled vocab) and `specification.yaml`.
2. Read the three data sheets from the authoring xlsx (`openpyxl`).
3. Validate:
   - every `requirement_index` exists in `specification.yaml`;
   - every `framework` exists in `standards.yaml`;
   - `coverage` and `maturity` are within the allowed enums;
   - required fields present.
     Collect all problems and report them together; non-zero exit on error.
4. Group rows by `requirement_index` and build the `standards` / `patterns` /
   `products` lists.
5. Merge into `specification.yaml`:
   - **idempotent**: re-running with the same spreadsheet yields no diff;
   - `--replace` (default) overwrites the three fields for touched requirements;
   - a requirement absent from the spreadsheet is left untouched;
   - preserve field ordering and existing formatting using `ruamel.yaml` (see
     decision D1) so diffs show only changed lines.
6. Write back `specification.yaml` (and emit the JSON sidecar for the site JS, see §6).

CLI sketch:

```
python sourcefiles/process_tags.py \
  --spec docs/source/spec/specification.yaml \
  --standards docs/source/spec/standards.yaml \
  --xlsx sourcefiles/satre-tags-authoring.xlsx \
  [--check]   # validate only, no write
```

Decision D1: use `ruamel.yaml` (preserves comments/quoting, produces clean diffs).
Authoring-time dependency only; not required for the Read the Docs build.

## 6. Rendering on the site

### 6a. Tag data availability for the client

Decision D2: use a **JSON sidecar**. A build step (in the `yamlspec` extension) writes
`_static/spec-tags.json` from the YAML at build time. The coverage page's JS fetches it
and filters against a clean structured object. This keeps the data independent of table
markup and is the easiest base for filtering and CSV export.

(Rejected alternative: embedding tags as `data-*` attributes on table rows — couples the
UI to markup and makes rich fields like description/coverage/maturity awkward to encode.)

### 6b. Dedicated filter / coverage page

New page: `docs/source/coverage.md` (title e.g. "Coverage & Mappings"), added to the
`toctree` in `index.md` under the Specification caption. It hosts a `raw html` mount
point plus `custom.js` / `custom.css` (the `custom.js` hook already exists commented-out
in `conf.py`).

Behaviour:

- **Filter controls**: multi-select for standards (by framework), patterns, products.
  Selecting multiple filters is supported.
- **Result view**: the spec requirements split into two groups:
  - **Covered** — requirements matched by the current filter selection, each showing
    which selected tag(s) cover it.
  - **Not covered** — requirements not matched by the current selection.
    Grouped by pillar / capability so gaps are visible at capability level (echoes the
    evaluation model where a capability is "met" only if all its mandatory items are).
- **Export**: button to export the current view as **CSV** (decision D4). Zero
  client-side dependencies. Export scope (all vs currently-filtered) is left as a toggle
  in the UI so we can experiment; xlsx can be added later if wanted.

Multi-filter semantics (decision D3): default to **union (OR)** — a requirement is
"covered" if it matches _any_ selected tag, with an optional toggle for **intersection
(AND)** — covered only if it matches _all_ selected tags. Union matches the primary goal
("these statements are covered by these things, and these are not"); intersection helps
spot overlap between two things.

## 7. Build / infra impact

- Read the Docs stays static. New JS/CSS shipped via `_static/` and registered in
  `conf.py` (`html_js_files`, existing `html_css_files`).
- The JSON sidecar (`_static/spec-tags.json`) is generated by the `yamlspec` extension
  at build time — no runtime dependency.
- New Python dep: `ruamel.yaml`, used only by the authoring script (`process_tags.py`).
  Not needed for the RTD build, since tags are already merged into the YAML by then.

## 8. Backwards compatibility

- All three fields are optional. `yamlspec.py` already uses `item.get(..., "")`, so
  requirements without tags render unchanged.
- No change to `requirement_index` anchors or existing columns.

## 9. Suggested build order (de-risked for one day)

1. **Schema + controlled vocab** — add `standards.yaml`; hand-add tags to 2–3 example
   requirements in `specification.yaml` to exercise the model end to end.
2. **Authoring spreadsheet** — create the four-sheet xlsx template.
3. **Processing script** — `process_tags.py` with `--check` validation first, then
   merge/write.
4. **JSON sidecar + filter page** — the primary user-facing deliverable.
5. **CSV export** — export the current coverage view.

Steps 1–3 deliver "tags authored and merged into the spec"; step 4 delivers the
interactive page. Either is a coherent stopping point.

## 10. Decisions (resolved)

- **D1 — YAML writer**: `ruamel.yaml` (clean diffs; authoring-time dependency only).
- **D2 — Tag data to browser**: JSON sidecar (`_static/spec-tags.json`, built by the
  `yamlspec` extension).
- **D3 — Multi-filter semantics**: union (OR) by default, with an intersection (AND)
  toggle.
- **D4 — Export**: CSV only for now; export-scope toggle (all vs filtered) in the UI.
- **D5 — Badges on main spec tables**: no — tags surface only on the coverage page.
- **Spreadsheet context columns**: include `capability` and `statement`; exclude
  `guidance`.
