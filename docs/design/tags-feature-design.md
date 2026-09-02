# Design: Tags feature (standards, patterns, products)

Status: Implemented (hackathon)
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

`patterns` and `products` are distinct tag types (filtered independently) with mostly
the same shape. The difference: a pattern is documentation, so it carries a `status`
(`draft` | `published`); a product is built technology, so it carries a `maturity`
(Technology Readiness Level, TRL 1–9).

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
      status: published # draft | published
      url: "https://..." # optional
  products:
    - name: "Data Safe Haven"
      description: "Turing's open-source secure environment."
      coverage: partial
      maturity: 9 # TRL 1-9
      url: "https://..."
    # Special sentinel: requirement met by a local process, not a product.
    - name: "Local Process"
      local_process: true
```

Only `name` (products/patterns) and `framework` (standards) are truly required. All
other fields are optional — see §3 field definitions and the import rules in §5.

### Controlled vocabulary — standards frameworks (day one)

| Framework (canonical `framework` value)     | Notes                                                              |
| ------------------------------------------- | ------------------------------------------------------------------ |
| `ISO 27001`                                 | Clause / Annex A control reference                                 |
| `NHS DSPT`                                  | NHS Digital Security and Protection Toolkit assertion/evidence ref |
| `Cyber Essentials Plus`                     | Control theme                                                      |
| `Digital Economy Act`                       | Section reference                                                  |
| `NHS Secure Data Environment Specification` | Requirement reference                                              |

The canonical list lives in one place the script and the renderer both read —
`docs/source/spec/standards.yaml`:

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

# Enumerations validated by the processing script.
coverage: [full, partial]
status: [draft, published] # pattern lifecycle status
maturity: # product Technology Readiness Level
  values: [1, 2, 3, 4, 5, 6, 7, 8, 9]
  labels:
    1: Basic principles observed
    # ... through to ...
    9: Actual system proven in operational environment
```

The processing script validates every `framework` value in the spreadsheet against
`standards.yaml` and rejects unknowns. New standards are added by editing
`standards.yaml` — one controlled place.

### Field definitions

An entry is **identified by** its `framework` (standards) or `name` (patterns /
products). That identifying field is the only hard requirement; the remaining fields
are optional and, when omitted, are simply left out of the YAML. Supplying an _invalid_
value (unknown framework, bad `coverage` / `status`, out-of-range `maturity`) is a hard
error; supplying an _incomplete_ entry (identifier present, recommended fields missing)
is a warning but is still imported. See §5 for the full import rules.

**standards[]**

- `framework` (required) — must match a `name` in `standards.yaml`.
- `reference` (optional) — clause / control id, free text (e.g. `A.5.35`, `1.3.1`). If
  omitted, the mapping is recorded at framework level (a warning is emitted).

**patterns[]** (documentation)

- `name` (required)
- `description` (optional)
- `coverage` (optional) — `full` | `partial`
- `status` (optional) — `draft` | `published`
- `url` (optional)

**products[]** (built technology)

- `name` (required)
- `description` (optional)
- `coverage` (optional) — `full` | `partial`
- `maturity` (optional) — Technology Readiness Level (TRL), an integer `1`–`9`
- `url` (optional)
- `local_process` (special) — when `name` is the sentinel value `Local Process`, the
  entry is stored as `{name: "Local Process", local_process: true}` with no other
  fields. This marks a requirement as met by a local process rather than a product; it
  is expected never to carry a product, description, coverage or maturity.

Validated by the script when present: `framework` (must be in `standards.yaml`),
`coverage` (enum), `status` (enum, patterns), `maturity` (integer 1–9, products). TRL
labels for each level are defined in `standards.yaml` and used for tooltips / the
reference sheet.

## 4. Authoring spreadsheet

Two files, deliberately separated so regenerating the template never overwrites
author work:

- **Template** (generated): `sourcefiles/satre-tags-authoring.xlsx` — written by
  `generate_tags_spreadsheet.py`.
- **Input** (author-filled): `sourcefiles/satre-tags-authoring_input.xlsx` — the
  workbook authors edit and that `process_tags.py` reads by default.

Both have four sheets.

Each data sheet is **pre-populated with a row per requirement** (all of them), with the
context columns `requirement_index`, `capability` and `statement` filled in from
`specification.yaml`. Authors work through the whole specification, filling in the tag
columns only for the requirements they want to tag; the rest are left blank. To make it
easy to add several entries against one requirement (e.g. multiple products), each
requirement is given one or more spare blank rows; authors can also add more rows
manually — any row sharing a `requirement_index` is imported as an additional entry.
`guidance` is deliberately excluded to keep rows readable. The context columns are
**read-only / informational**: the processing script keys everything off
`requirement_index` and ignores `capability` / `statement` on read (the YAML remains
authoritative for that text). Re-running the generator refreshes the context columns and
pre-populates any tags already present in the YAML.

### Sheet `standards`

| requirement_index | capability         | statement                                                                         | framework | reference |
| ----------------- | ------------------ | --------------------------------------------------------------------------------- | --------- | --------- |
| 1.2.04            | Quality Management | You must audit your TRE organisation against relevant requirements and standards. | ISO 27001 | A.5.35    |
| 1.2.04            | Quality Management | You must audit your TRE organisation against relevant requirements and standards. | NHS DSPT  | 1.3.1     |

### Sheet `patterns`

| requirement_index | capability | statement | name | description | coverage | status | url |
| ----------------- | ---------- | --------- | ---- | ----------- | -------- | ------ | --- |

### Sheet `products`

| requirement_index | capability | statement | name | description | coverage | maturity | url |
| ----------------- | ---------- | --------- | ---- | ----------- | -------- | -------- | --- |

### Sheet `_reference` (read-only helper)

Lists valid framework names, coverage values, pattern status values, and maturity
(TRL 1–9) values so authors can use data-validation dropdowns. Generated from
`standards.yaml`.

One row per entry: a requirement with several tags of a type occupies several rows
sharing the same `requirement_index`. This keeps the sheet flat and easy to fill in.
The `capability` / `statement` columns repeat per row for context.

## 5. Processing script

Location (proposed): `sourcefiles/process_tags.py`.

Responsibilities:

1. Load `standards.yaml` (controlled vocab) and `specification.yaml`.
2. Read the three data sheets from the authoring xlsx (`openpyxl`).
3. Validate each row using a three-tier quality check keyed off the row's
   **identifier** (`framework` for standards; `name` for patterns / products). Since
   the sheets are pre-populated with a row per requirement, most rows are blank and
   must be tolerated:

   - **Ignore (silent)** — a row with no identifier (blank `framework` / `name`). This
     covers untagged requirements and spare blank rows. Nothing is imported.
   - **Error (blocks import, non-zero exit)** — a row whose supplied values are
     _invalid_: unknown `requirement_index`, unknown `framework` (not in
     `standards.yaml`), or an out-of-vocabulary `coverage` / `status` / `maturity`.
   - **Warning (imported anyway)** — a row with a valid identifier but _missing_
     recommended fields (e.g. a product with a `name` but no `coverage` / `maturity`, or
     a standard with a `framework` but no `reference`). The available data is imported
     and the gap is reported, so partial capture is not blocked but stays visible.

   Special case: on the products sheet, the name `Local Process` (case-insensitive) is
   a recognised sentinel — imported as `{name: "Local Process", local_process: true}`
   with no further fields required and no warning.

   All errors and warnings are collected and reported together (warnings to stderr,
   prefixed `!`; errors prefixed `-`). Exit is non-zero only if there are errors.

4. Group the imported entries by `requirement_index` and build the `standards` /
   `patterns` / `products` lists.
5. Merge into `specification.yaml`:
   - **idempotent**: re-running with the same input yields no diff;
   - the three managed fields are replaced for each touched requirement;
   - a requirement absent from the spreadsheet is left untouched;
   - uses **targeted text insertion** (not a full document round-trip) to keep diffs
     minimal — see decision D1 and the note below.
6. Write back `specification.yaml`. (The JSON sidecar for the site is produced
   separately by the `yamlspec` extension at build time — see §6.)

CLI sketch:

```
python sourcefiles/process_tags.py \
  --spec docs/source/spec/specification.yaml \
  --standards docs/source/spec/standards.yaml \
  --xlsx sourcefiles/satre-tags-authoring_input.xlsx \
  [--check]   # validate only, no write
```

Decision D1 (as implemented): keep diffs minimal via **targeted text insertion**.
`specification.yaml` is formatted by `prettier` (a pre-commit hook; the file is not in
`.prettierignore`), which prose-wraps long scalars at widths that a full `ruamel.yaml`
round-trip cannot reproduce — a naive load-and-dump reformats ~1300 lines. Instead the
script edits the file as text: it splits on `  - pillar:` item boundaries, strips any
existing managed tag block for a touched requirement, and inserts a freshly serialised
tag block (the small tag mapping only, via `ruamel.yaml`) right after that item's
`architecture_url:` line. Every other line is left byte-for-byte, so the diff shows only
the tags actually added. `prettier` in CI may re-wrap the inserted lines on commit,
which is expected. `ruamel.yaml` is an authoring-time dependency only; not required for
the Read the Docs build.

## 6. Rendering on the site

### 6a. Tag data availability for the client

Decision D2: use a **JSON sidecar**. A build step (in the `yamlspec` extension) writes
`_static/spec-tags.json` from the YAML at build time. The coverage page's JS fetches it
and filters against a clean structured object. This keeps the data independent of table
markup and is the easiest base for filtering and CSV export.

(Rejected alternative: embedding tags as `data-*` attributes on table rows — couples the
UI to markup and makes rich fields like description/coverage/maturity awkward to encode.)

### 6b. Dedicated filter / coverage page

New page: `docs/source/coverage.md` (title "Coverage & Mappings"), added to the
`toctree` in `index.md` under the Specification caption. It hosts a `raw html` mount
point (`<div id="coverage-app">`) served by `_static/coverage.js` (registered via
`html_js_files` in `conf.py`), with styles appended to `_static/custom.css`.

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

## 9. Build status

All parts are implemented:

1. ✅ **Schema + controlled vocab** — `docs/source/spec/standards.yaml`; example tags in
   `specification.yaml`.
2. ✅ **Authoring spreadsheet** — `generate_tags_spreadsheet.py` builds the four-sheet
   template (`satre-tags-authoring.xlsx`); authors fill in
   `satre-tags-authoring_input.xlsx`.
3. ✅ **Processing script** — `process_tags.py` (`--check` validation + merge/write,
   skip/warn/error tiers, `Local Process` sentinel).
4. ✅ **JSON sidecar + filter page** — `yamlspec.py` emits `_static/spec-tags.json`;
   `coverage.md` + `coverage.js` + coverage styles in `custom.css`.
5. ✅ **CSV export** — export the current coverage view (all / filtered scope).

The scripts and both spreadsheets live under `sourcefiles/`, which is gitignored (the
same location as the repo's other authoring helpers). `_static/spec-tags.json` is also
gitignored (regenerated at build time).

## 10. Decisions (resolved)

- **D1 — YAML writing / clean diffs**: targeted text insertion (strip + reinsert only
  the tag block per touched item), using `ruamel.yaml` to serialise the small tag
  mapping. A full round-trip was rejected because `prettier` formats the file and a
  round-trip reformats ~1300 lines. Authoring-time dependency only.
- **D2 — Tag data to browser**: JSON sidecar (`_static/spec-tags.json`, built by the
  `yamlspec` extension).
- **D3 — Multi-filter semantics**: union (OR) by default, with an intersection (AND)
  toggle.
- **D4 — Export**: CSV only for now; export-scope toggle (all vs filtered) in the UI.
- **D5 — Badges on main spec tables**: no — tags surface only on the coverage page.
- **Spreadsheet context columns**: include `capability` and `statement`; exclude
  `guidance`.
