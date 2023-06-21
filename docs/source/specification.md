(specification)=

# A Standard Architecture for TREs

<!-- What this document intends to do (and what it doesn't), the level of detail we aim for contrasted with other technical standards -->

## Design

### Overview

The SATRE specification follows a capability-evaluation model.

The specification is presented in terms of capabilities teams should aim for across all aspects of TRE provision.
These capabilities are broken down into components.
Each component is a statement of a process, method or practice teams should have in place to ensure they fulfil the capability requirements.

Any particular component is labelled with an importance.
The importance is one of mandatory, recommended or optional.
Teams are able demonstrate that they meet the specification by showing they can fulfil all mandatory components.
Future versions of the specification may introduce more granular levels of evaluation, for instance tiered level of accreditation based on fulfilment of mandatory, recommended and optional components respectively.

Any particular TRE implementation should be able to score itself against each capability as either supported, partially supported or unsupported (see {ref}`evaluation` for details).

### Architecture

The SATRE specification contains four key parts:

```{figure} ../images/Architecture.svg
:alt: SATRE Specification Architecture
:align: center

SATRE Specification Architecture
```

Architectural Principles
: The principles that all teams looking to use the specification should hold themselves accountable to.

Specification Pillars
: The broad areas of TRE provisioning the specification covers.

TRE Capabilities
: The capabilities within these pillars teams can measure themselves against.

TRE Capability Components
: The statements concerning processes, controls, practices and applications that make up a capability, including an importance label.

### Capability Component Importance Labels

Our interpretation of the capability component importance labels are:

Mandatory
: We believe this is required. If this component is not supported, then the capability, and the specification, is not met.

Recommended
: We believe that TREs should have this component. It makes a TRE better.

Optional
: We believe many TREs would benefit from this component. However, we recognise there are reasons a team may actively choose not to support this component.

### Pillars and Capability Map

The SATRE specification contains three core pillars for a TRE:

```{figure} ../images/Capability_Map.svg
:alt: SATRE Pillars Capability Map
:align: center

SATRE Pillars Capability Map
```

{ref}`Information governance <pillar_information_governance>`
: What the organisation does to ensure information risk is measured and managed to an acceptable level.

{ref}`Computing technology <pillar_computing_technology>`
: What the organisation does to manage systems for storing, retrieving, and sending information.

{ref}`Data management <pillar_data_management>`
: What the organisation does to manage data assets and ensure information remains secure.

In addition to these capabilities, any organisation running a TRE (TRE organisation) will need to possess various {ref}`supporting capabilities <pillar_supporting>`.
These will include legal requirements and relationship management.

## Principles

The SATRE specification has been developed based on the following principles:

- TREs should be as as easy as possible for end-users to use (_e.g._ researchers) whilst still remaining secure.
- TRE deployments should be offered that support data of different levels of sensitivity (_e.g._ through a tiered system of technical controls and policies).
- TREs conforming to the specification should be interoperable and provide a familiar end-user experience.
- The specification will be managed and updated following an open, community-driven process, and will not be tied to a single vendor or implementation.

Finally, the TRE organisation will need to consider different {ref}`roles <tre_roles>` with which individuals might interact with the TRE.

There might be good reasons why any particular TRE does not possess one or more of the capabilities listed in this specification, but most TREs should aspire to meet them in the long-term.

<!-- List of capabilities. Each of these hould be described in prose and accompanied by a short requirements table of "Statement" and "Guidance" for each requirement. -->

## Specification

Details of the SATRE specification are shown below, together with the breakdown of the pillars into capabilities and components.

```{toctree}
:numbered:
pillars/information_governance.md
pillars/computing_technology.md
pillars/data_management.md
pillars/supporting.md
```

(tre_roles)=
## Roles

A TRE conforming to the SATRE specification should provide a broadly similar experience for stakeholders operating in each of these defined roles.
There is not necessarily a one-to-one mapping between roles and people.
One person can have multiple roles.

### TRE users

The researchers working on projects that involve logging into a TRE to access data.

<!-- The document will explain that user experience of the platform and associated documentation should feel similar across TREs conforming to SATRE specification. -->

```{list-table}
:header-rows: 1
:name: tab-tre-role-user

* - Role name
  - Role description
* -
  -
```

### TRE administration roles

The IT and related professionals who will be responsible for deploying and managing instances of a TRE conforming to the SATRE specification.
These roles cover managing TRE computing infrastructure, but also administering the TRE itself (_e.g._ managing users and projects).

<!-- The document will explain that SATRE conforming TREs should have documentation and infrastructure deployment code/apps that conform to software engineering best practices, which are also defined here, making them "simple" for an IT professional to follow; troubleshooting steps included. -->

```{list-table}
:header-rows: 1
:name: tab-tre-role-administrator

* - Role name
  - Role description
* -
  -
```

### TRE developer roles

The software engineers responsible for developing and maintaining TRE software, including adding functionality, bug fixes and general maintenance.

<!-- The document will explain recommended practices suitable for developing a software of this complexity and reference learnings from existing TRE developers. -->

```{list-table}
:header-rows: 1
:name: tab-tre-role-developer

* - Role name
  - Role description
* -
  -
```

### TRE governance roles

Roles that uphold the governance of TREs.
Such governance responsibilities typically involve establishing policies and procedures to ensure the responsible use of data, protecting the privacy and confidentiality of research participants, and promoting transparency and accountability in research activities.
Typical roles might include data custodians, ethicists, an independent board or a lay panel.

```{list-table}
:header-rows: 1
:name: tab-tre-role-governance

* - Role name
  - Role description
* -
  -
```
