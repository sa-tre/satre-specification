(specification)=

# The SATRE specification

The specification is presented in terms of the capabilities that a team running a TRE should aim for across all aspects of TRE provision.

The specification is split into {ref}`four pillars <satre_pillars>`.

## Structure of the specification

This page explains what the specification is, and how it's structured.
Consult the {ref}`FAQs <faqs>` for more on what the specification _is not_.

:::{note}
Throughout this document, we will use the term "{ref}`TRE operator <infrastructure_roles>`" to refer to the team running a particular TRE.
:::

The TRE capabilities are broken down into components.
Each component is a statement of a process, method or practice that the operators should have in place to ensure they fulfil the capability requirements.
These components are each labelled with an importance:

:Mandatory: This is required: if this component is not supported, then the capability, and therefore the specification, is not met.
:Recommended: Most TREs should have this component, but it is not essential.
:Optional: Many TREs would benefit from this component, however, we recognise there are reasons a {ref}`TRE operator <infrastructure_roles>` may actively choose not to implement it.

{ref}`TRE operator <infrastructure_roles>`s are able to demonstrate that they meet the specification by showing they can fulfil all **mandatory** components.
Future versions of the specification may introduce more granular levels of evaluation, for instance tiered level of accreditation based on fulfilment of mandatory, recommended and optional components respectively.

Any particular TRE implementation should be able to {ref}`score itself against each capability <scoring_method>`.

## Structure

The SATRE specification contains four key parts:

```{figure} ../images/Architecture.svg
:alt: SATRE Specification Architecture
:align: center

SATRE Specification Architecture
```

:{ref}`Architectural Principles <satre_principles>`: The {term}`principles <architectural principle>` that all {ref}`TRE operator <infrastructure_roles>`s looking to use the specification should hold themselves accountable to.
:{ref}`Specification Pillars <satre_pillars>`: The broad areas of TRE provisioning the specification covers. Each pillar is broken down into one or more {term}`capabilities <capability>`. Each capability is broken down into one or more {term}`components <component>`.
:{ref}`Roles <satre_roles>`: {term}`Roles <role>` that are necessary for the operation and use of a TRE.

Together, these provide a framework that {ref}`TRE operator <infrastructure_roles>`s can measure themselves against.

## Architectural Principles

The SATRE specification has been developed based on the following principles:

- {ref}`Usability <principle_usability>`
- {ref}`Maintaining public trust <principle_maintaining_trust>`
- {ref}`Observability <principle_observability>`
- {ref}`Standardisation <principle_standardisation>`

(satre_pillars)=

## Specification Pillars and Capabilities

The SATRE specification contains three core pillars for a TRE, plus supporting capabilities:

```{figure} ../images/Capability_Map/full.drawio.svg
:alt: SATRE Pillars Capability Map
:align: center

SATRE Pillars Capability Map
```

{ref}`1. Information governance <pillar_information_governance>`
: What the {ref}`TRE operator <infrastructure_roles>`s do to ensure information risk is measured and managed to an acceptable level.

{ref}`2. Computing technology <pillar_computing_technology>`
: What the {ref}`TRE operator <infrastructure_roles>`s do to manage systems for storing, retrieving, and sending information.

{ref}`3. Data management <pillar_data_management>`
: What the {ref}`TRE operator <infrastructure_roles>`s do to manage data assets and ensure information remains secure.

{ref}`4. Supporting capabilities <pillar_supporting>`
: A {ref}`TRE operator <infrastructure_roles>` will need to possess various supporting capabilities, such as complying with legal requirements and managing relationships with stakeholders.
