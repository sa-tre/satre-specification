(specification)=

# What is the SATRE specification?

<!-- What this document intends to do (and what it doesn't), the level of detail we aim for contrasted with other technical standards -->

The SATRE specification follows a capability-evaluation model.
The specification is presented in terms of the capabilities that a team running a TRE should aim for across all aspects of TRE provision.

:::{note}
Throughout this document, we will use the term "TRE operator" to refer to the team running a particular TRE.
:::

The TRE capabilities are broken down into components.
Each component is a statement of a process, method or practice that the operators should have in place to ensure they fulfil the capability requirements.
These components are each labelled with an importance.
The importance is one of **mandatory**, **recommended** or **optional**.

:::{note}
The intended meaning of the capability component importance labels is as follows:

Mandatory
: This is required. If this component is not supported, then the capability, and the specification, is not met.

Recommended
: We believe that TREs should have this component. It makes a TRE better.

Optional
: We believe many TREs would benefit from this component. However, we recognise there are reasons a TRE operator may actively choose not to support this component.
:::

TRE operators are able to demonstrate that they meet the specification by showing they can fulfil all **mandatory** components.
Future versions of the specification may introduce more granular levels of evaluation, for instance tiered level of accreditation based on fulfilment of mandatory, recommended and optional components respectively.

Any particular TRE implementation should be able to score itself against each capability as either **supported**, **partially supported** or **unsupported** (see {ref}`evaluation` for details).

## Structure

The SATRE specification contains four key parts:

```{figure} ../images/Architecture.svg
:alt: SATRE Specification Architecture
:align: center

SATRE Specification Architecture
```

{ref}`Architectural Principles <satre_principles>`
: The {term}`principles <architectural principle>` that all TRE operators looking to use the specification should hold themselves accountable to.

{ref}`Specification Pillars <satre_pillars>`
: The broad areas of TRE provisioning the specification covers.

Each pillar is broken down into several {term}`TRE Capabilities <capability>`.

Each capability consists of one or more {term}`TRE Capability Components <component>`.

Together, these provide a framework that TRE operators can measure themselves against.

{ref}`Roles <satre_roles>`
: In addition, we also describe some {term}`roles <role>` that are necessary for the operation and use of a TRE.

(satre_principles)=

## Architectural Principles

The SATRE specification has been developed based on the following principles:

- TREs should be as easy as possible for end-users to use (_e.g._ researchers) whilst still remaining secure.
- TREs should take accessibility for all users, including those with disabilities, into account.
- TRE deployments should be offered that support data of different levels of sensitivity (_e.g._ through a tiered system of technical controls and policies).
- TREs conforming to the specification should be interoperable and provide a familiar end-user experience.
- The specification will be managed and updated following an open, community-driven process, and will not be tied to a single vendor or implementation.

Finally, the TRE operators will need to consider different {ref}`roles <satre_roles>` with which individuals might interact with the TRE.

There might be good reasons why any particular TRE does not possess one or more of the capabilities listed in this specification, but most TREs should aspire to meet them in the long-term.

(satre_pillars)=

### Specification Pillars and Capabilities

The SATRE specification contains three core pillars for a TRE:

```{figure} ../images/Capability_Map/full.drawio.svg
:alt: SATRE Pillars Capability Map
:align: center

SATRE Pillars Capability Map
```

{ref}`Information governance <pillar_information_governance>`
: What the TRE operators do to ensure information risk is measured and managed to an acceptable level.

{ref}`Computing technology <pillar_computing_technology>`
: What the TRE operators do to manage systems for storing, retrieving, and sending information.

{ref}`Data management <pillar_data_management>`
: What the TRE operators do to manage data assets and ensure information remains secure.

In addition to these capabilities, any TRE operator will need to possess various {ref}`supporting capabilities <pillar_supporting>`.
Examples of supporting capabilities include complying with legal requirements and managing relationships with stakeholders.
