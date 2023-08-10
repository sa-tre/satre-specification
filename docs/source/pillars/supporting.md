(pillar_supporting)=

# Supporting Capabilities

```{figure} ../../images/Capability_Map/full.drawio.svg
:alt: SATRE Pillars Capability Map
:align: center

SATRE Pillars Capability Map
```

<!-- See all pillars of the SATRE Pillars Capability Map here: {ref}`satre_pillars` -->

## Business continuity management

What the TRE operator does to ensure the development, testing, and maintenance of business continuity plans.

```{list-table}
:header-rows: 1
:name: tab-business-continuity-subject

* -
  - Statement
  - Guidance
  - Importance
* - 4.1.1
  - You should have a business continuity plan that includes consideration of loss of service for deployed TREs.
  - This may be due to downtime from service providers, a breach, or loss of power. Your plan should detail your process for managing loss of service for deployed TREs, and evaluation of impact of such loss.
  - Recommended
* - 4.1.2
  - You should regularly test the aspects of your business continuity plan concerning TREs, and have a process in place to iterate the plan if required.
  -
  - Recommended
```

## Project and programme management

What the TRE operator does to ensure effective management of programmes and projects.

```{list-table}
:header-rows: 1
:name: tab-project-programme-management

* -
  - Statement
  - Guidance
  - Importance
* - 4.2.1
  - You should ensure that all projects using your TRE have a named project manager.
  - The project manager has responsibility to ensure the smooth running of the project.
    Their responsibilities may include budget management, tracking TRE status, managing communications with the TRE operations team, and other project support tasks.
  - Recommended
* - 4.2.2
  - You should not give project managers direct access to the TRE.
  - Doing so ensures a separation between those able to access sensitive data, and those overseeing access to sensitive data.
  - Recommended
```

## Knowledge management

What the TRE operator does to acquire, enrich, share, store, publish and enhance expertise across their organisation.

```{list-table}
:header-rows: 1
:name: tab-knowledge-management

* -
  - Statement
  - Guidance
  - Importance
* - 4.3.1
  - You must document all features of your TRE implementation.
  - This includes ensuring all documentation is discoverable, clear, and able to be easily updated based on stakeholder feedback
  - Mandatory
* - 4.3.2
  - You should have an education programme in place to upskill stakeholders in the use and management of your TRE.
  - This may include learning modules, workshops and other resources on how to effectively access and use a TRE, FAQ pages, and accessible pathways for additional support
  - Recommended
* - 4.3.3
  - You should periodically carry out a training needs analysis (TNA) for all stakeholders included within your TRE provision.
  - At least once every 12 months you should assess the training needs of your stakeholders, and ensure they have easy access to all required training materials
  - Recommended
```

## Financial management

All activities aimed at the efficient and effective management of money (funds) in such a manner as to allow the TRE operator to accomplish its objectives.

```{list-table}
:header-rows: 1
:name: tab-financial-management

* -
  - Statement
  - Guidance
  - Importance
* - 4.4.1
  - You must ensure that all projects using your TRE are aware of any associated costs and are able and willing to pay them.
  - Costs may include provision of the underlying TRE infrastructure, additional resources required in a specific TRE (for instance memory or additional compute), hardware including managed devices, and staff support costs
  - Mandatory
* - 4.4.2
  - You should be able to track the costs associated with each TRE project.
  - This includes knowing which costs are associated with which project, and having an appropriate charging mechanism in place in line with your organisational policy.
  - Recommended
* - 4.4.3
  - You should have a process in place to ensure your TRE provision remains financially sustainable.
  - This could include having a cost recovery process in place, or setting up a long-term funding mechanism to support projects with TREs.
    At any given time, you should have funds free to cover all potential foreseen TRE provision for at least 12 months.
  - Recommended
* - 4.4.4
  - You should minimise the cost of your TRE infrastructure wherever possible
  - You should have regular reviews of your TRE provision and actively work to bring down costs, streamline provision, and optimise support.
  - Recommended
```

## Procurement

What the TRE operator does to ensure the effective sourcing, purchasing and supply of the goods and services that enable them to operate.

```{list-table}
:header-rows: 1
:name: tab-procurement

* -
  - Statement
  - Guidance
  - Importance
* - 4.5.1
  - You must identify any goods or services that will be needed to operate the TRE and ensure that a plan is in place to purchase them as needed.
  - These may include computing hardware, cloud credits or devices through which users access the TRE.
  - Mandatory
```

## IT Service management

The implementation and management of quality IT services that meet the needs of the TRE operator.

```{list-table}
:header-rows: 1
:name: tab-it-service-management

* -
  - Statement
  - Guidance
  - Importance
* - 4.6.1
  - You TRE must have a team in place to support projects working with TREs.
  - This may be part of your organisation's IT support team, or separate.
    Responsibility should be clear and stakeholders should easily be able to access support appropriate to their needs.
  - Mandatory
```

## Relationship management

All activities aimed at ensuring a continuous level of engagement is maintained between the TRE operator and its customers, stakeholders and other interested parties.

### Stakeholder relationships

Activities aimed at engaging with TRE stakeholders.

```{list-table}
:header-rows: 1
:name: tab-relationship-stakeholder

* -
  - Statement
  - Guidance
  - Importance
* - 4.7.1
  - You should have a clear process in place for stakeholders to feedback on your TRE infrastructure.
  - This may include a GitHub repository where people can open issues and discussions, communication streams like Slack or email, or forms stakeholders can fill in.
  - Recommended
```

## Public Involvement and Engagement

How the TRE operator involves the public in its processes and work in order to maintain trust in its operations.

<!--
Rationale:

- PIE work is important to building and maintaining trust.
- Use of public data is sometimes critical to research, for example health research.
- The public can benefit from sharing their data, to trustworthy and safe research projects, for example in the development of better health treatments or social policies.
- Meeting other parts of this specification helps ensure that data is secure and that data processing is legal, appropriate and ethical.
- Optional as there are cases (for example research with purely non-personal, commercial data) where involving the public is less important and may even be undesirable.
- We particularly encourage meeting this capability for work involving personal data belonging to the public such as health or administrative data.
-->

```{list-table}
:header-rows: 1
:name: tab-supporting-pie
* -
  - Statement
  - Guidance
  - Importance
* - 4.8.1
  - You should ensure that all public engagement activities are representative and inclusive.
  - Any public engagement activity carried out by TREs should make sure they are involving a representative sample where possible and that activities are accessible and open.
    This could include following guidelines such as [PEDRI](https://www.pedri.org.uk/).
  - Recommended
* - 4.8.2
  - You could publicly share the details of any projects which use the TRE.
  - This may be via the TRE website or annual reports.
  - Optional
* - 4.8.3
  - You could include members of the public in your approvals process.
  - This may be carried out via a separate public panel or by including members of the public on an approvals panel.
  - Optional
```

## Legal services

The ability of the TRE operator to access suitable and timely legal advice.

<!-- Specific requirements? _e.g._ Article 32 of the GDPR requires organisations to regularly test and evaluate the effectiveness of the technical and organisational measures employed to protect personal data, and penetration testing is an effective way of assessing your technical defences. -->

### Legal advisory

The ability of the TRE operator to provide suitable and timely legal advice.

```{list-table}
:header-rows: 1
:name: tab-legal-services

* -
  - Statement
  - Guidance
  - Importance
* - 4.9.1
  - You should have identify areas where legal advice may be required and ensure that you have ready access to it.
  - It is likely that legal advice will be necessary for several issues around the handling of sensitive data, and managing project contracts.
    TRE operators should have ready access to legal advice, including a way to solicit advice and carry out associated actions.
  - Recommended
```

### Data protection

Ability to ensure data is used fairly, lawfully and transparently; for specified, explicit purposes; and in a way that is adequate, relevant and limited to only what is necessary.

```{list-table}
:header-rows: 1
:name: tab-legal-dp

* -
  - Statement
  - Guidance
  - Importance
* - 4.9.2
  - You should identify areas where legal advice may be required and ensure that you have ready access to it.
  - It is likely that data protection advice will be necessary for several issues around the handling of sensitive data.
  - Recommended
```

### Contract management

What the organisation does to ensure that all contracts are effectively managed within required frameworks.

```{list-table}
:header-rows: 1
:name: tab-legal-cm

* -
  - Statement
  - Guidance
  - Importance
* - 4.9.3
  - You should identify who will be responsible for managing contracts related to the TRE.
  - These contracts may include data sharing agreements, secondments of personnel or limitations on how results obtained with the data can be distributed.
  - Recommended
```
