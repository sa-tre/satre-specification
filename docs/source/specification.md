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
A TRE instance that works for everyone minimises barriers to use, and provides a productive and accessible analysis environment for research.

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
