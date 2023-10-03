(specification)=

# What is the SATRE specification?

<!-- What this document intends to do (and what it doesn't), the level of detail we aim for contrasted with other technical standards -->

The SATRE specification follows a capability-evaluation model.
The specification is presented in terms of the capabilities that a team running a TRE should aim for across all aspects of TRE provision.
This page explains what the specification is, and how it's structured. Consult the {ref}`FAQs <faqs>` for more on what the specification _is not_.

:::{note}
Throughout this document, we will use the term "{ref}`TRE operator <infrastructure_roles>`" to refer to the team running a particular TRE.
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
: We believe many TREs would benefit from this component. However, we recognise there are reasons a {ref}`TRE operator <infrastructure_roles>` may actively choose not to support this component.
:::

{ref}`TRE operator <infrastructure_roles>`s are able to demonstrate that they meet the specification by showing they can fulfil all **mandatory** components.
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
: The {term}`principles <architectural principle>` that all {ref}`TRE operator <infrastructure_roles>`s looking to use the specification should hold themselves accountable to.

{ref}`Specification Pillars <satre_pillars>`
: The broad areas of TRE provisioning the specification covers.

Each pillar is broken down into several {term}`TRE Capabilities <capability>`.

Each capability consists of one or more {term}`TRE Capability Components <component>`.

Together, these provide a framework that {ref}`TRE operator <infrastructure_roles>`s can measure themselves against.

{ref}`Roles <satre_roles>`
: In addition, we also describe some {term}`roles <role>` that are necessary for the operation and use of a TRE.

(satre_principles)=

### Architectural Principles

Architectural principles influence and shape the way you design and deliver a SATRE-aligned TRE.
They are a set of guiding considerations that sit above any specific architectural requirement, and can be applied across the entire architecture.

Finally, the {ref}`TRE operator <infrastructure_roles>`s will need to consider different {ref}`roles <satre_roles>` with which individuals might interact with the TRE.

They consist of the following parts:
**Statement**: A singular sentence that summarises the principle
**Rationale**: Justification as to why this principle is important for the specification
**Implications**: Things you need to consider or do to practise this principle

#### Usability

##### Statement

A TRE instance that works for all users minimises barriers to use, and provides a productive and accessible analysis environment for research.

##### Rationale

There is often a trade-off between increased operational security and the usability of a TRE.
In order to maintain productivity, a TRE must balance these two competing aims.
The design and configuration of a TRE should allow all individuals involved with a TRE to effectively fulfil their roles.

##### Implications

- Robust TRE design and implementation should start by understanding users’ diverse expectations, needs, existing skillsets and preferences and responsibilities.
- Design, configuration and testing of TREs must recognise a diversity of users. For instance, not all users are researchers and not all researchers are users. Other users include TRE operators, information governance officers, and TRE builders/developers.
- Because of diverse user needs, it is unlikely that a specific TRE instance will perfectly match the needs of all users.
- A TRE that is overly strict on tool and software provision may risk becoming unusable for users with different and varied backgrounds and skillsets.
- Working environments can differ significantly from users’ preferred setups. This has design and resource implications for supporting new users, and consideration should be given to resources and time required to help users get up to speed with new and unfamiliar TRE instances.
- Improving user experience takes time and resource, and will involve trade-offs between investing time in improved standards, better functional design, improving work and organisational culture, boosting users' skills and knowledge through training and making help more readily available at an organisational level. These trade-offs will need to be addressed at an organisational level, and teams may want to consider resourcing staff to focus specifically on these questions, for instance in the positions of product managers or service functions.

#### Maintaining public trust

##### Statement

TREs holding public data should build and maintain the trust of data subjects and any other impacted individuals, groups, communities and organisations by protecting privacy, keeping data secure and being transparent about their work.

##### Rationale

Maintaining trust in TREs to hold and use data is essential to prevent backlash or resistance to the use of data.
This can include maintaining the trust of members of the public who are impacted by research, as well as the trust of commercial data providers.

In the case of public sector data, public engagement work has indicated there is widespread support for the use of regulated and ethical TREs working for the public benefit.
Consulting impacted parties, including the public, can help ensure TREs are being used for positive, impactful and agreed-upon purposes.
Being transparent about the data held and the projects or organisations who access the data can also help maintain trust.

##### Implications

- Being as transparent as possible is key to building trust. TREs holding public data should practice transparency, for instance making adherence to any accreditation body, or framework (for instance the Five Safes) publicly available information, and making information on the projects or organisations which access their data available to impacted parties.
- A strong public engagement programme takes time and resource. TREs holding public data should consider allocating specific staffing to public engagement activities.
- TREs open to consultation by impacted parties should be auditable, and impacted parties should be part of any decision making processes. This may include the provision of documentation and educational resources for a diverse audience.
- Access to public sector data should be reviewed by an independent panel and follow agreed-upon governance to ensure projects using this data are in the public benefit, and provide clarity around any commercial access.

#### Observability

##### Statement

Human initiated and automated processes resulting in change within the TRE should be observable.

##### Rationale

System/process observability is key to understanding whether your policies and controls are actually doing what is intended.

It also allows operators to continuously improve their systems and processes, measure their effectiveness, and identify the causes of incidents. Data can also be made available to other parties such as auditors, data subjects and data providers as part of the assurance process.

This applies to both technical systems and policies/processes.

##### Implications

- In order to understand what is happening within the TRE, both automated and human initiated processes should generate sufficient data. Any generated data should follow standards for provenance and transparency for audit trails.
- Different levels of observability may be needed for different users. Any data collected from an observability perspective should consider the needs of those who will use it, and minimise collection accordingly.
- There may be ethical and confidential issues to consider when implemeting the observability principle.

#### Standardisation

##### Statement

TREs should adhere to standards or well-known patterns wherever possible.

##### Rationale

Standardisation makes it easier to design, operate, use and understand TREs, and reduces duplication of work.
This includes making TREs easier to use, deploy, and audit.

TREs should be built in such a way that they do not restrict or prevent interoperability where this may be desirable in future, by identifying and avoiding or removing barriers to interoperability.

Standardisation is also linked to the public trust principle, as a standard approach to TRE provision will make it eaiser for impacted parties to understand how their data will be used within TREs.

##### Implications

- Owing to the broad definition of {ref}`TREs <what_tre>`, there are no specific TRE technical standards. The SATRE specification has therefore been designed to help {ref}`Developers and Operators <infrastructure_roles>` with a variety of technical/policy requirements consider their options
- TRE {ref}`Developers and Operators <infrastructure_roles>` should be prepared identify the technical standards that are appropriate for them to work towards meeting whilst developing or maintaining their particular TRE(s).
- Standards that TREs adhere to may range in scope, including technical, operational and governance requirements.
- TRE {ref}`Developers and Operators <infrastructure_roles>` should ensure that when they aim to meet multiple standards, those standards align with one another to ensure there is no contradiction in requirements. 

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
: What the {ref}`TRE operator <infrastructure_roles>`s do to ensure information risk is measured and managed to an acceptable level.

{ref}`Computing technology <pillar_computing_technology>`
: What the {ref}`TRE operator <infrastructure_roles>`s do to manage systems for storing, retrieving, and sending information.

{ref}`Data management <pillar_data_management>`
: What the {ref}`TRE operator <infrastructure_roles>`s do to manage data assets and ensure information remains secure.

In addition to these capabilities, any {ref}`TRE operator <infrastructure_roles>` will need to possess various {ref}`supporting capabilities <pillar_supporting>`.
Examples of supporting capabilities include complying with legal requirements and managing relationships with stakeholders.
