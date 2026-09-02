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
      maturity: established # concept | emerging | established | proven
      url: "https://..." # optional
  products:
    - name: "Data Safe Haven"
      description: "Turing's open-source secure environment."
      coverage: partial
      maturity: proven
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
- `maturity` (required) — `concept` | `emerging` | `established` | `proven`
- `url` (optional)

Enumerations (`coverage`, `maturity`) are validated by the script.

## 4. Authoring spreadsheet

Filename (proposed): `sourcefiles/satre-tags-authoring.xlsx`. Four sheets.

### Sheet `standards`

| requirement_index | framework | reference |
| ----------------- | --------- | --------- |
| 1.2.04            | ISO 27001 | A.5.35    |
| 1.2.04            | NHS DSPT  | 1.3.1     |

### Sheet `patterns`

| requirement_index | name | description | coverage | maturity | url |
| ----------------- | ---- | ----------- | -------- | -------- | --- |

### Sheet `products`

| requirement_index | name | description | coverage | maturity | url |
| ----------------- | ---- | ----------- | -------- | -------- | --- |

### Sheet `_reference` (read-only helper)

Lists valid framework names, coverage values, and maturity values so authors can use
data-validation dropdowns. Generated by the script (or maintained by hand) from
`standards.yaml`.

One row per mapping (multi-valued tags = multiple rows with the same
`requirement_index`). This keeps the sheet flat and easy to fill in.

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
   - preserve field ordering and existing formatting as far as practical
     (use `ruamel.yaml` to preserve comments/quotes, or `yaml` with a fixed dumper —
     decision below).
6. Write back `specification.yaml` (and optionally emit a JSON sidecar for the site JS,
   see §6).

CLI sketch:

```
python sourcefiles/process_tags.py \
  --spec docs/source/spec/specification.yaml \
  --standards docs/source/spec/standards.yaml \
  --xlsx sourcefiles/satre-tags-authoring.xlsx \
  [--check]   # validate only, no write
```

Open decision: `ruamel.yaml` (preserves comments/quoting, nicer diffs) vs stdlib
`yaml` (already a dependency via the extension). Leaning `ruamel.yaml` for clean diffs;
falls back to `yaml` if we want zero new deps.

## 6. Rendering on the site

### 6a. Tag data availability for the client

The filter page needs the tag data in the browser. Two options:

- **A. JSON sidecar** — a small build step (or the `yamlspec` extension) writes
  `_static/spec-tags.json` from the YAML. The filter page's JS fetches it. Clean
  separation, easy to reason about. Preferred.
- **B. Data attributes in the DOM** — embed tags as `data-*` attributes on table rows
  and read them with JS. No fetch, but couples UI to table markup.

Preferred: **A** for the dedicated filter page; optionally **B** for lightweight badges
on the existing spec tables.

### 6b. Badges on existing spec tables (optional, low priority)

Extend `yamlspec.py` to append compact badges under the statement/guidance for each
requirement that has tags (e.g. `ISO 27001 A.5.35`, `pattern`, `product`). Kept subtle
to avoid overloading the already-dense table. This is a nice-to-have; the dedicated
page is the primary deliverable.

### 6c. Dedicated filter / coverage page

New page: `docs/source/coverage.md` (title e.g. "Coverage & Mappings"), added to the
`toctree` in `index.md` under the Specification caption. It hosts a `raw html` mount
point plus `custom.js` / `custom.css` (the `custom.js` hook already exists commented-out
in `conf.py`).

Behaviour:

- **Filter controls**: multi-select for standards (by framework), patterns, products.
  Selecting multiple filters is supported (union or intersection — see open decision).
- **Result view**: the spec requirements split into two groups:
  - **Covered** — requirements matched by the current filter selection, each showing
    which selected tag(s) cover it.
  - **Not covered** — requirements not matched by the current selection.
    Grouped by pillar / capability so gaps are visible at capability level (echoes the
    evaluation model where a capability is "met" only if all its mandatory items are).
- **Export**: button to export the current view. Scope (all vs filtered) and format
  (CSV vs xlsx) kept as toggles so we can experiment during the hackathon. CSV is
  zero-dependency; xlsx would use a small client-side lib (e.g. SheetJS) loaded via
  `html_js_files`.

Open decision — multi-filter semantics:

- **Union (OR)**: "covered" = matched by _any_ selected tag. Good for "what do all
  these things cover between them?"
- **Intersection (AND)**: "covered" = matched by _all_ selected tags. Good for "what is
  covered by both X and Y?"
- Proposal: default to **union**, with a toggle for intersection. This directly serves
  the phrasing "these statements are covered by these things, and these are not."

## 7. Build / infra impact

- Read the Docs stays static. New JS/CSS shipped via `_static/` and registered in
  `conf.py` (`html_js_files`, existing `html_css_files`).
- If we add a JSON sidecar generated by the extension, it is produced at build time — no
  runtime dependency. If generated by the script instead, it is committed alongside the
  YAML.
- New Python dep only if we pick `ruamel.yaml` (dev/authoring only, not needed at RTD
  build time since the tags are already merged into the YAML by then).

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
5. **Export** — CSV first (zero-dep), then optional xlsx.
6. **Badges on spec tables** — optional polish if time remains.

Steps 1–3 deliver "tags authored and merged into the spec"; step 4 delivers the
interactive page. Either is a coherent stopping point.

## 10. Open decisions (need a call)

1. YAML writer: `ruamel.yaml` (nicer diffs, new dep) vs stdlib `yaml` (no new dep).
2. Tag data to browser: JSON sidecar (preferred) vs DOM data attributes.
3. Multi-filter semantics: union default + intersection toggle (proposed).
4. Export scope + format: kept flexible; CSV first, xlsx optional.
5. Show badges on the main spec tables, or keep tags only on the coverage page?

```

```
