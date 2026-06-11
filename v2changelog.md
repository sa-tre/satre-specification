# SATRE Specification Change Log: v1.1 → v2.0

---

## Cross-Cutting Changes

### Requirement Index Format

All requirement indices have been reformatted from `x.y.z` to `x.y.0z` (zero-padded), e.g. `1.2.1` → `1.2.01`. This applies uniformly across all pillars and capabilities. Cross-references within guidance text have been updated to match.

### Architectural Rationalisation

Several capabilities in v1.1 were misaligned with the underlying architecture. v2 corrects this by dissolving four capabilities in Pillar 3 (Security Levels and Tiering, Research Meta-Data, Meta-Data Search and Discovery Application, and the secondary Data Lifecycle Management grouping at 3.8) and redistributing their requirements into better-fitting capabilities. A similar rationalisation applies in Pillar 2, where the monolithic Information Security capability has been split into four focused capabilities reflecting distinct security domains.

### New Pillar: Federation

Pillar 5 — Federation — is entirely new in v2. It comprises 21 requirements across 7 capabilities covering the governance, security, operational, and data management requirements for TREs operating as part of a federation. The pillar was developed through structured community engagement as part of the DARE UK TREvolution programme, including workshops at the UK TRE Conference in Leeds and a dedicated TREvolution programme workshop, engaging approximately 90 participants. There are no removed, moved, or modified requirements in Pillar 5 — all content is new.

### Terminology

The term "member" in the context of researcher accreditation has been replaced with "researcher" throughout (e.g. `Member Accreditation` → `Researcher Accreditation`), reflecting the more precise SATRE role terminology.

---

## Pillar 1 — Information Governance

### Structural Changes

**Capability renamed**

- `1.5 Member Accreditation` → `1.5 Researcher Accreditation` (requirement indices 1.5.01–1.5.06; no statement or guidance changes)

**New capability added**

- `1.7 Public Involvement and Engagement` — four requirements moved here from v1.1 Pillar 4 (4.8.1–4.8.4). See _Moved Requirements_ below.

**Requirement index format change (all capabilities)**

- All requirement indices reformatted from `x.y.z` to `x.y.0z` (zero-padded, e.g. `1.2.1` → `1.2.01`). Applies uniformly across the pillar.

**Known data quality issue in v1.1 corrected**

- Requirement `1.2.2` (Quality Management) carried index `1.1.2` in the v1.1 YAML — a numbering error. In v2 this is correctly numbered `1.2.02`.

---

### Moved Requirements

| v1.1 index | v1.1 capability (pillar)                     | v2 index | v2 capability (pillar)                       | Notes                         |
| ---------- | -------------------------------------------- | -------- | -------------------------------------------- | ----------------------------- |
| 4.8.1      | Public Involvement and Engagement (Pillar 4) | 1.7.01   | Public Involvement and Engagement (Pillar 1) | Statement updated — see below |
| 4.8.2      | Public Involvement and Engagement (Pillar 4) | 1.7.02   | Public Involvement and Engagement (Pillar 1) | Statement updated — see below |
| 4.8.3      | Public Involvement and Engagement (Pillar 4) | 1.7.03   | Public Involvement and Engagement (Pillar 1) | Statement updated — see below |
| 4.8.4      | Public Involvement and Engagement (Pillar 4) | 1.7.04   | Public Involvement and Engagement (Pillar 1) | Unchanged                     |

---

### New Requirements

| v2 index | Capability       | Importance  | Statement                                                                                  |
| -------- | ---------------- | ----------- | ------------------------------------------------------------------------------------------ |
| 1.4.07   | Study Management | Mandatory\* | TREs holding data about the public must provide that data for research for public benefit. |

_Note: index slot 1.4.07 in v2 is occupied by this new requirement; what was v1.1 1.4.7 has become v2 1.4.06 — see Removed Requirements below._

---

### Removed Requirements

| v1.1 index | Capability       | Importance | Statement                                                                      | Fate                                                                                                    |
| ---------- | ---------------- | ---------- | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------- |
| 1.4.6      | Study Management | Mandatory  | You must keep a complete record of all the data assets held within the system. | **Dropped** — no equivalent in v2. The index slot is absorbed into the revised 1.4.06 (formerly 1.4.7). |

---

### Changed Importance

| Requirement | Capability         | v1.1 importance                                  | v2 importance | Notes                                                                                                                |
| ----------- | ------------------ | ------------------------------------------------ | ------------- | -------------------------------------------------------------------------------------------------------------------- |
| 1.2.08      | Quality Management | `Mandatory (where physical assets are in scope)` | `Mandatory*`  | Semantically equivalent; reformatted to the standard `Mandatory*` convention. Qualification added to statement text. |

---

### Updated Statement Text

| v2 index | Capability                        | v1.1 statement                                                                                                                  | v2 statement                                                                                                                                 | Nature of change                                                      |
| -------- | --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------- |
| 1.1.02   | Information Governance            | "You must ensure controls are implemented to **ensure the requirements are met**."                                              | "You must ensure controls are implemented to **meet stakeholder requirements**."                                                             | Tightened; makes stakeholders explicit                                |
| 1.2.08   | Quality Management                | "You must track and maintain any physical assets used by your TRE."                                                             | Same + "(\*optional for TREs without physical assets)"                                                                                       | Qualification added inline to match `Mandatory*` convention           |
| 1.3.01   | Risk Management                   | "…a way to **score** risk…"                                                                                                     | "…a way to **quantify** risk…"                                                                                                               | Word substitution; more precise                                       |
| 1.4.05   | Study Management                  | "…automates **the processes within this capability**."                                                                          | "…automates **components relating to study management**."                                                                                    | Scoped more specifically                                              |
| 1.4.06   | Study Management                  | _(was 1.4.7)_ "You should keep a complete record of all the research studies and projects within the TRE current and **past**." | "You should keep a complete record of all the research studies **(Safe Projects)** and projects within the TRE current and **historic**."    | Introduces "Safe Projects" terminology; "past" → "historic"           |
| 1.7.01   | Public Involvement and Engagement | _(was 4.8.1)_ "All public engagement activities must include **a range of perspectives and be inclusive**"                      | "Public engagement activities must have **a fair and balanced inclusion of people with different backgrounds, experiences, and identities**" | Significantly strengthened and made more specific                     |
| 1.7.02   | Public Involvement and Engagement | _(was 4.8.2)_ "…data **should** be publicly available"                                                                          | "…data **must** be publicly available"                                                                                                       | "should" → "must" (strengthened)                                      |
| 1.7.03   | Public Involvement and Engagement | _(was 4.8.3)_ "Members of the public **should** be included in TRE operations and/or oversight"                                 | "Members of the public **must** be effectively involved in TRE operations and/or oversight"                                                  | "should" → "must"; "included" → "effectively involved" (strengthened) |

---

### Updated Guidance Text

| v2 index | Capability                       | Nature of change                                                                                                                                                                                                |
| -------- | -------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1.2.06   | Quality Management               | Minor typo fix: "in during procurement" → "during procurement"                                                                                                                                                  |
| 1.3.01   | Risk Management                  | Reframed from prescriptive ("You have a risk assessment methodology…") to illustrative ("For example, a risk assessment methodology may…")                                                                      |
| 1.3.02   | Risk Management                  | Minor typo fix: "an existing regulatory requirements" → "existing regulatory requirements"                                                                                                                      |
| 1.4.02   | Study Management                 | Minor typo fix: "contracts remain in valid" → "contracts remain valid"                                                                                                                                          |
| 1.4.06   | Study Management                 | Substantially rewritten: v1.1 guidance was about data asset metadata and compliance records; v2 guidance focuses on study register content and references the HDRUK data use registry standard (DOI link added) |
| 1.6.02   | Training Management and Delivery | Cross-reference added: "(See 1.6.01 to determine training needed for a role)" replaces the more discursive "Details of what training is needed will have been determined above."                                |

---

## Pillar 2 — Computing Technology and Information Security

### Structural Changes

**Capability split: Information Security (2.5) restructured into four new capabilities**

The most significant structural change in Pillar 2 is that v1.1's monolithic `2.5 Information Security` (18 requirements) has been broken into four focused capabilities plus a slimmed-down `2.5 Information Security` (3 requirements):

| v2 capability            | v2 index range | Requirements | What moved in from v1.1                                     |
| ------------------------ | -------------- | ------------ | ----------------------------------------------------------- |
| Information Security     | 2.5.01–2.5.03  | 3            | Regulatory compliance (was 2.5.18); plus 2 new requirements |
| Cyber Resilience         | 2.6.01–2.6.05  | 5            | Backups, redundancy, incident response (was 2.5.1–2.5.5)    |
| Vulnerability Management | 2.7.01–2.7.06  | 6            | Scanning, patching, pen testing (was 2.5.6–2.5.11)          |
| Encryption               | 2.8.01–2.8.05  | 5            | At-rest and in-transit encryption (was 2.5.12–2.5.16)       |
| Physical Security        | 2.9.01         | 1            | Physical protection measures (was 2.5.17)                   |

**Requirement removed from Infrastructure Management (2.2)**

- v1.1 `2.2.13` ("You should regularly monitor the network configuration…") has been dropped; its role is absorbed by the rewritten `2.2.12` (see statement changes below). This collapses a two-requirement monitoring pair into a single, broader statement.

**Infrastructure Management logging requirements renumbered**

The removal of v1.1 `2.2.13` causes a one-position shift: v1.1 `2.2.14–2.2.16` become v2 `2.2.13–2.2.15`.

---

### New Requirements

| v2 index | Capability           | Importance | Statement                                                                                                                                            |
| -------- | -------------------- | ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| 2.5.02   | Information Security | Optional   | Your TRE could use threat modelling to identify areas of risk to infrastructure.                                                                     |
| 2.5.03   | Information Security | Mandatory  | Your TRE must maintain security logs of significant events and have a process for reviewing these logs to detect and respond to suspicious activity. |

_Note: 2.5.01 is not new — it is the upgraded and renamed version of v1.1 2.5.18; see Changed Importance below._

---

### Removed Requirements

| v1.1 index | Capability                | Importance  | Statement                                                                                                              | Fate                                                                                                                                                  |
| ---------- | ------------------------- | ----------- | ---------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| 2.2.13     | Infrastructure Management | Recommended | You should regularly monitor the network configuration of your TRE to check for misconfigurations and vulnerabilities. | **Dropped** — merged into revised 2.2.12, which now covers monitoring more broadly, removing the explicit "regularly" requirement as a separate item. |

---

### Moved Requirements (Information Security split)

All of the following retain their statement text (with minor exceptions noted under Statement Changes). The only change is capability name and index.

| v1.1 index | v1.1 capability      | v2 index | v2 capability                                                    |
| ---------- | -------------------- | -------- | ---------------------------------------------------------------- |
| 2.5.1      | Information Security | 2.6.01   | Cyber Resilience                                                 |
| 2.5.2      | Information Security | 2.6.02   | Cyber Resilience                                                 |
| 2.5.3      | Information Security | 2.6.03   | Cyber Resilience                                                 |
| 2.5.4      | Information Security | 2.6.04   | Cyber Resilience                                                 |
| 2.5.5      | Information Security | 2.6.05   | Cyber Resilience                                                 |
| 2.5.6      | Information Security | 2.7.01   | Vulnerability Management                                         |
| 2.5.7      | Information Security | 2.7.02   | Vulnerability Management                                         |
| 2.5.8      | Information Security | 2.7.03   | Vulnerability Management                                         |
| 2.5.9      | Information Security | 2.7.04   | Vulnerability Management                                         |
| 2.5.10     | Information Security | 2.7.05   | Vulnerability Management                                         |
| 2.5.11     | Information Security | 2.7.06   | Vulnerability Management                                         |
| 2.5.12     | Information Security | 2.8.01   | Encryption                                                       |
| 2.5.13     | Information Security | 2.8.02   | Encryption                                                       |
| 2.5.14     | Information Security | 2.8.03   | Encryption                                                       |
| 2.5.15     | Information Security | 2.8.04   | Encryption                                                       |
| 2.5.16     | Information Security | 2.8.05   | Encryption                                                       |
| 2.5.17     | Information Security | 2.9.01   | Physical Security                                                |
| 2.5.18     | Information Security | 2.5.01   | Information Security (retained; importance upgraded — see below) |

---

### Changed Importance

| v1.1 index → v2 index | Capability           | v1.1 importance | v2 importance | Notes                                                             |
| --------------------- | -------------------- | --------------- | ------------- | ----------------------------------------------------------------- |
| 2.5.18 → 2.5.01       | Information Security | Recommended     | Mandatory     | Statement also strengthened: "may need to comply" → "must comply" |

---

### Updated Statement Text

| v2 index | Capability                | v1.1 statement                                                                                                                | v2 statement                                                                                               | Nature of change                                                                                                                          |
| -------- | ------------------------- | ----------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| 2.1.04   | End User Computing        | "…accessible **using** commonly available applications."                                                                      | "…using commonly available applications."                                                                  | Minor: word "accessible" removed (tightened)                                                                                              |
| 2.1.08   | End User Computing        | "…shared services are **only available to users working on the same project**."                                               | "…shared services **do not allow users to access data from another project**."                             | Reframed: outcome-focused (data access) rather than access control                                                                        |
| 2.1.10   | End User Computing        | "…software applications that are **relevant to** working with the data in the TRE."                                           | "…software applications that are **required by the data consumers** working in the TRE."                   | Stronger: "relevant" → "required"; makes data consumers the reference point                                                               |
| 2.1.14   | End User Computing        | "…when using **non-standard** compute."                                                                                       | "…when using **all compute, including HPC**."                                                              | Broadened: replaces vague "non-standard" with an explicit all-compute scope including HPC                                                 |
| 2.2.12   | Infrastructure Management | "You should **be able to monitor the network** configuration of your TRE to check for misconfigurations and vulnerabilities." | "You should **monitor the** configuration of your TRE to check for misconfigurations and vulnerabilities." | Strengthened and broadened: removes "be able to" (passive capability → active obligation); drops "network" (now covers all configuration) |
| 2.3.01   | Capacity Management       | "…all **projects** understand what resources are available…"                                                                  | "…all **project members** understand what resources are available…"                                        | More precise: makes clear it is individuals, not projects as abstract entities                                                            |
| 2.5.01   | Information Security      | "Your TRE **may need** to comply with specific regulatory requirements…"                                                      | "Your TRE **must** comply with specific regulatory requirements…"                                          | "may need to" → "must"; conditional removed, now unconditional Mandatory                                                                  |

---

### Updated Guidance Text

| v2 index | Capability                | Nature of change                                                                                                                                                                                  |
| -------- | ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 2.1.05   | End User Computing        | Minor typo fix: "as oppose to" → "as opposed to"                                                                                                                                                  |
| 2.1.15   | End User Computing        | Minor punctuation/grammar: "on a HPC cluster" → "on an HPC cluster"; added comma after "For example"                                                                                              |
| 2.2.07   | Infrastructure Management | Minor typo fix: "uninterruptable" → "uninterruptible"                                                                                                                                             |
| 2.3.01   | Capacity Management       | Minor punctuation: missing full stop added after first paragraph                                                                                                                                  |
| 2.5.01   | Information Security      | Substantially rewritten to reflect Mandatory status: v1.1 focused on general backup rationale; v2 guidance explicitly addresses regulatory frameworks and the need for specific security measures |
| 2.5.02   | Information Security      | New guidance (new requirement): references OWASP threat modelling framework with URL                                                                                                              |
| 2.5.03   | Information Security      | New guidance (new requirement): specifies minimum log event categories (authentication, privileged actions, access control changes, data egress) and tamper-protection requirements               |

---

## Pillar 3 — Data Management

### Structural Changes

**Capabilities 3.5, 3.6, 3.7, 3.8 dissolved — all requirements absorbed into existing capabilities**

The most significant structural change in Pillar 3 is the removal of four standalone capabilities, correcting a misalignment with the v1.1 architecture. Their requirements have been redistributed as follows:

| v1.1 capability                            | v1.1 indices | Fate in v2                                                    |
| ------------------------------------------ | ------------ | ------------------------------------------------------------- |
| Security Levels and Tiering                | 3.5.1–3.5.3  | Moved into Data Lifecycle Management as 3.1.17–3.1.19         |
| Research Meta-Data                         | 3.6.1–3.6.2  | Moved into Information Search and Discovery as 3.4.02, 3.4.04 |
| Meta-Data Search and Discovery Application | 3.7.1        | Moved into Information Search and Discovery as 3.4.03         |
| Data Lifecycle Management (archiving)      | 3.8.1–3.8.2  | Moved into Data Lifecycle Management as 3.1.14–3.1.15         |

**Data Lifecycle Management (3.1) significantly expanded**

v1.1 had 13 requirements in 3.1; v2 has 20. The additions come from absorbed capabilities plus genuinely new requirements (see New Requirements below).

**Information Search and Discovery (3.4) expanded**

v1.1 had a single requirement (3.4.1); v2 has four (3.4.01–3.4.04), absorbing Research Meta-Data and Meta-Data Search and Discovery Application from v1.1.

**Output Management (3.3) internally reordered**

Requirements within 3.3 have been resequenced. The order in v1.1 was: classify → establish outputs → disclosure control → assign responsibility → handle unchecked → statistical basis → semi-automated → minimum outputs. In v2 the order is: classify → minimum outputs → establish outputs → disclosure control → assign responsibility → statistical basis → handle unchecked → semi-automated → [new 3.3.09]. The substantive content of each requirement is unchanged except where noted below.

**Statement correction in 3.8.2 → 3.1.15**

v1.1 3.8.2 reads "Long-term archives **must** be held in simple, standard formats…" with importance Recommended — an internal inconsistency (mandatory language, recommended importance). v2 3.1.15 corrects this: "Long-term archives **should** be held…", aligning statement language with the Recommended importance.

---

### New Requirements

| v2 index | Capability                | Importance  | Statement                                                                                                                                                                                   | Notes                                                                                                                   |
| -------- | ------------------------- | ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| 3.1.16   | Data Lifecycle Management | Recommended | Where a project intends to train or fine-tune machine learning models on sensitive data, you should ensure a data management plan for ML artefacts is agreed prior to project commencement. | New ML/AI-specific requirement; guidance covers model export controls, operational registers, and decommissioning plans |
| 3.1.20   | Data Lifecycle Management | Recommended | Metadata should be checked for disclosure risk at the point of data upload.                                                                                                                 | New; guidance notes metadata can be informative about data subjects independently of research outputs                   |
| 3.3.09   | Output Management         | Optional    | TREs should generate, store, and retain a machine-readable record of all disclosure-control criteria applied to each set of outputs released from a project.                                | New; guidance specifies JSON/YAML format, audit retention, and linkage to released output packages                      |

---

### Removed Requirements

No requirements have been fully dropped from Pillar 3. All v1.1 requirements appear in v2, either in place or absorbed into a different capability.

---

### Moved Requirements

| v1.1 index | v1.1 capability                            | v2 index | v2 capability                    | Changes                                                                |
| ---------- | ------------------------------------------ | -------- | -------------------------------- | ---------------------------------------------------------------------- |
| 3.5.1      | Security Levels and Tiering                | 3.1.17   | Data Lifecycle Management        | None                                                                   |
| 3.5.2      | Security Levels and Tiering                | 3.1.18   | Data Lifecycle Management        | None                                                                   |
| 3.5.3      | Security Levels and Tiering                | 3.1.19   | Data Lifecycle Management        | None                                                                   |
| 3.6.1      | Research Meta-Data                         | 3.4.02   | Information Search and Discovery | Minor: "meta-data data model" → "metadata data model" (hyphen removed) |
| 3.6.2      | Research Meta-Data                         | 3.4.04   | Information Search and Discovery | None                                                                   |
| 3.7.1      | Meta-Data Search and Discovery Application | 3.4.03   | Information Search and Discovery | None                                                                   |
| 3.8.1      | Data Lifecycle Management                  | 3.1.14   | Data Lifecycle Management        | None                                                                   |
| 3.8.2      | Data Lifecycle Management                  | 3.1.15   | Data Lifecycle Management        | Statement corrected: "must" → "should" (see Structural Changes)        |

---

### Changed Importance

No importance changes within Pillar 3 beyond the 3.8.2 → 3.1.15 statement correction noted above.

---

### Updated Statement Text

| v2 index | Capability                | v1.1 statement                                                                                                                               | v2 statement                                                                        | Nature of change                                                                               |
| -------- | ------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| 3.1.02   | Data Lifecycle Management | "You should keep records of data handling decisions."                                                                                        | "You should **consult appropriately and** keep records of data handling decisions." | Strengthened: adds a consultation obligation, particularly for decisions affecting public data |
| 3.1.15   | Data Lifecycle Management | _(was 3.8.2)_ "Long-term archives **must** be held in simple, standard formats…"                                                             | "Long-term archives **should** be held in simple, standard formats…"                | Corrects internal inconsistency: aligns statement language with Recommended importance         |
| 3.3.02   | Output Management         | _(was 3.3.8)_ "TRE outputs should be limited to the minimum required for sharing results of any analyses."                                   | Unchanged statement, reordered to position 2                                        | Position only — see Output Management reorder note                                             |
| 3.3.03   | Output Management         | _(was 3.3.2)_ "You should establish the intended outputs of each project from the outset."                                                   | Unchanged statement, reordered to position 3                                        | Position only                                                                                  |
| 3.3.07   | Output Management         | _(was 3.3.5)_ "You must have a documented policy for handling disclosure risks associated with any outputs that cannot be manually checked." | Unchanged statement, reordered to position 7                                        | Position only; but **guidance substantially expanded** — see Guidance Changes                  |

---

### Updated Guidance Text

| v2 index | Capability                       | Nature of change                                                                                                                                                                                                                                              |
| -------- | -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 3.1.02   | Data Lifecycle Management        | Substantially rewritten: v1.1 guidance was generic ("decisions should be recorded and made available for inspection by all stakeholders"); v2 guidance specifically addresses public involvement in decisions affecting data about the public                 |
| 3.1.06   | Data Lifecycle Management        | Minor punctuation: cross-reference updated from "(see 3.1.5)" to "(see 3.1.05)" to match new index format; missing full stop added                                                                                                                            |
| 3.1.07   | Data Lifecycle Management        | Minor punctuation: missing full stop added at end of guidance                                                                                                                                                                                                 |
| 3.1.08   | Data Lifecycle Management        | Terminology: "contact details for the data owner" → "contact details for the **information asset owner**" (consistent with SATRE terminology)                                                                                                                 |
| 3.3.01   | Output Management                | Extended: reference to the SDAP SDC Handbook added with hyperlink                                                                                                                                                                                             |
| 3.3.02   | Output Management                | _(was 3.3.8)_ Guidance unchanged in substance; moved with the reordered requirement                                                                                                                                                                           |
| 3.3.03   | Output Management                | _(was 3.3.2)_ Guidance streamlined: v1.1 included rationale about data protection compliance; v2 retains only the practical guidance about output sensitivity                                                                                                 |
| 3.3.07   | Output Management                | _(was 3.3.5)_ Substantially expanded: adds explicit treatment of ML model weights as an output category that cannot be manually checked, including risk of model memorisation of sensitive records and requirement to address model artefact export in policy |
| 3.4.01   | Information Search and Discovery | Substantially expanded: v1.1 noted relevance for population-level TREs and caveated appropriateness; v2 adds that metadata catalogues themselves require disclosure control and rewrites the caveat more clearly                                              |

---

## Pillar 4 — Supporting Capabilities

### Structural Changes

**Capability removed: Public Involvement and Engagement (4.8)**

All four PIE requirements (4.8.1–4.8.4) have been moved to Pillar 1 as the new capability 1.7. This is documented fully in the Pillar 1 changelog. The 4.8 slot in Pillar 4 no longer exists in v2.

**Capability renumbered: Legal Services (4.9 → 4.8)**

With PIE removed, Legal Services moves from 4.9 to 4.8. All three requirements (statements, importance, and guidance) are unchanged — this is a renumbering only.

**Capability renamed: Project and Programme Management (4.2)**

v1.1 carries a typo in the capability name: `Projectect and Programme Management`. v2 corrects this to `Project and Programme Management`. No requirement changes.

**Net effect:** Pillar 4 reduces from 21 to 17 requirements (loss of 4 PIE requirements to Pillar 1).

---

### New Requirements

None.

---

### Removed Requirements

| v1.1 index  | Capability                        | Fate                                                        |
| ----------- | --------------------------------- | ----------------------------------------------------------- |
| 4.8.1–4.8.4 | Public Involvement and Engagement | Moved to Pillar 1 as 1.7.01–1.7.04 — see Pillar 1 changelog |

---

### Moved Requirements

| v1.1 index | v1.1 capability | v2 index | v2 capability  | Changes                                                       |
| ---------- | --------------- | -------- | -------------- | ------------------------------------------------------------- |
| 4.9.1      | Legal Services  | 4.8.01   | Legal Services | Renumbered only; statement, importance and guidance unchanged |
| 4.9.2      | Legal Services  | 4.8.02   | Legal Services | Renumbered only; statement, importance and guidance unchanged |
| 4.9.3      | Legal Services  | 4.8.03   | Legal Services | Renumbered only; statement, importance and guidance unchanged |

---

### Changed Importance

None.

---

### Updated Statement Text

| v2 index | Capability           | v1.1 statement                                                              | v2 statement | Nature of change               |
| -------- | -------------------- | --------------------------------------------------------------------------- | ------------ | ------------------------------ |
| 4.4.04   | Financial Management | "You should minimise the cost of your TRE infrastructure wherever possible" | Same + "."   | Minor: missing full stop added |

---

### Updated Guidance Text

| v2 index | Capability           | Nature of change                                              |
| -------- | -------------------- | ------------------------------------------------------------- |
| 4.3.01   | Knowledge Management | Minor punctuation: missing full stop added at end of guidance |
| 4.3.02   | Knowledge Management | Minor punctuation: missing full stop added at end of guidance |
| 4.3.03   | Knowledge Management | Minor punctuation: missing full stop added at end of guidance |
| 4.4.01   | Financial Management | Minor punctuation: missing full stop added at end of guidance |

---

## Pillar 5 — Federation

Pillar 5 is entirely new in v2. It comprises 21 requirements across 7 capabilities covering the governance, security, operational, and data management requirements for TREs operating as part of a federation. The pillar was developed through structured community engagement as part of the DARE UK TREvolution programme, including workshops at the UK TRE Conference in Leeds and a dedicated TREvolution programme workshop, engaging approximately 90 participants. There are no removed, moved, or modified requirements in Pillar 5 — all content is new.

| Capability                           | Index | Requirements | Mandatory              | Recommended | Optional |
| ------------------------------------ | ----- | ------------ | ---------------------- | ----------- | -------- |
| Federation Governance                | 5.1   | 10           | 7 (inc. 1 Mandatory\*) | 2           | 0        |
| Federation Researcher Accreditation  | 5.2   | 1            | 1                      | 0           | 0        |
| Federation Study Management          | 5.3   | 2            | 2                      | 0           | 0        |
| Federation Information Security      | 5.4   | 4            | 2                      | 2           | 0        |
| Federation Infrastructure Management | 5.5   | 1            | 1                      | 0           | 0        |
| Federation Data Management           | 5.6   | 2            | 1                      | 1           | 0        |
| Federation Financial Management      | 5.7   | 1            | 0                      | 1           | 0        |
| **Total**                            |       | **21**       | **15**                 | **6**       | **0**    |
