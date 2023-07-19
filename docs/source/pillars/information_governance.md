(pillar_information_governance)=

# Information governance

This pillar concerns what the TRE operator does to ensure information risk is measured and managed to an acceptable level.

```{figure} ../../images/Capability_Map/full.drawio.svg
:alt: SATRE Pillars Capability Map
:align: center

SATRE Pillars Capability Map
```

<!-- See all pillars of the SATRE Pillars Capability Map here: {ref}`satre_pillars` -->

## Requirements

Information governance requirements are defined by top management within the TRE implementing organisation.
These will be draw from the context of the organisation, the work it performs and the nature of the data it processes.
Gathering and monitoring these requirements are a process for the capability along with the overall ownership of risk, definition of controls for those risks and the allocation of resources across the TRE organisation.
Quality data is a key input to measuring and improving the effectiveness of the TRE in relation to governance, risk and compliance.

These requirements will be different for every TRE organisation.
TRE organisations should conduct a requirements gathering exercise to identity the applicability of each item in the specification, and to identity the best way to implement them.

For example, some requirements will arise from national legislation such as GDPR, discipline specific regulation like GCP, or contractural requirements from a specific data provider such as a company or research partner organisation.

## Information governance

### Requirements Gathering and Monitoring (Business Process)

The process of collecting, documenting, and managing the functional and non-functional requirements for the TRE based on the TRE organisation's goals and data assets.

```{list-table}
:header-rows: 1
:name: tab-ig-requirements-gathering-monitoring

* - Statement
  - Guidance
  - Importance
* - The TRE organisation must gather and monitor the information governance requirements needed to fulfil the legal and ethical standards to protect data subjects and deliver valuable research.
  - Requirements will come from a variety of sources including legislation, contractual obligations and ethical standards.
    Requirements must be monitored to ensure the TRE controls continue to match such requirements.
    New types of analysis or sources of data being brought into the scope of the TRE should be monitored to ensure requirements are current.
  - Mandatory
```

### Controls (Business Process)

Measures, safeguards, or mechanisms implemented to manage or mitigate risks and ensure the integrity, confidentiality, availability, and reliability of systems, processes, or data.

```{list-table}
:header-rows: 1
:name: tab-ig-controls

* - Statement
  - Guidance
  - Importance
* - The organisation must ensure controls are implemented to ensure the requirements are met.
  - Control implementation should be systematic and directly aligned to the internal and stakeholder requirements.
  - Mandatory
```

### Resource Allocation (Business Process)

The process of assigning, distributing, and managing resources (such as personnel, finances, equipment, or time) within the TRE organisation to meet objectives and priorities effectively.

```{list-table}
:header-rows: 1
:name: tab-ig-resource-allocation

* - Statement
  - Guidance
  - Importance
* - The organisation must ensure there is adequate resources to provide assurance and meet information governance requirements.
  - There should be adequate access to funding to implement and maintain the TRE which is under the direct control of the TRE organisation.
  - Mandatory
```

<!-- ###	Standards and Controls -->

<!-- ### Information Security Management System Scope -->

## Quality Management

What the organisation does to measure and control quality of processes, documentation and outputs.

### Document and SOP Management (Business Process)

```{list-table}
:header-rows: 1
:name: tab-ig-quality-management


* - Statement
  - Guidance
  - Importance
* - All policies & standard operating procedures relevant to the TRE organisation are controlled.
  - This may include measures like restricting edit access to relevant documents and recording acceptance of policies for all TRE organisation members.
  - Mandatory
* - All policies & standard operating procedures relevant to the TRE organisation are version controlled and have codified change processes.
  - Version control includes recording dates of changes, person responsible for carrying out changes, and summary of changes.
  - Mandatory
```

### Quality Management Reporting (Business Process)

The generation and dissemination of reports or dashboards that provide insights and metrics on the performance and effectiveness of quality management processes and activities.

```{list-table}
:header-rows: 1
:name: tab-ig-quality-management-reporting

* - Statement
  - Guidance
  - Importance
* - The performance of information governance within the TRE should be measured with regular reporting available to top management.
  - This may include reports and dashboards showing security incidents, quality management deviations and audit findings.
  - Mandatory
```

### Internal Audit (Business Process)

An independent evaluation process within the TRE organisation that assesses and improves its internal controls, risk management, and governance.

```{list-table}
:header-rows: 1
:name: tab-ig-internal-audit

* - Statement
  - Guidance
  - Importance
* - You can audit your TRE organisation against relevant requirements and standards
  - If you are publicly accredited against a standard, for instance ISO27001, DSPT, CE+ etc., you must have processes in place to ensure you remain compliant.
  - Mandatory
* - You report on and share outcomes of each audit of your TRE organisation with the required bodies.
  - This may include regulatory bodies or the organisations that manage accreditations you have
  - Mandatory
```

### Supplier Management and Monitoring (Business Process)

A structured approach to managing and monitoring relationships with external suppliers, vendors and contractors, including selection, contract management and compliance oversight.

```{list-table}
:header-rows: 1
:name: tab-ig-supplier-management-monitoring

* - Statement
  - Guidance
  - Importance
* - You ensure that suppliers, contractors and sub-contractors align with the security requirements of you TRE.
  - These should be included as mandatory, non-functional requirements in during procurement and contracting.
    This will also include contractor staff contracts for example, legal liability and NDAs.
  - Mandatory
* - You monitor compliance of your suppliers with the terms of the contracts.
  - This will include monitoring changes in the services and infrastructure being delivered and quality management within the contractor’s organisation.
    This may be done through formal audit or by monitoring change and quality documentation provided by the supplier.
  - Mandatory
```

### Asset Management Process (Business Process)

A systematic approach to acquiring, operating, maintaining, and disposing of assets within an organization, aimed at maximizing their value and minimizing risks.

```{list-table}
:header-rows: 1
:name: tab-ig-asset-management-process

* - Statement
  - Guidance
  - Importance
* - Where physical assets are used these should be tracked and maintained to ensure security is maintained.
  - Safe disposal of storage media and warranties maintained for critical infrastructure-maintained confidentiality, integrity and availability.
  - Mandatory (where physical assets are in scope)
```

### Issue Management Process (Business Process)

A systematic approach to identifying, tracking, resolving, and managing issues or problems that arise within a TRE organisation, aiming to minimize their impact and ensure timely resolution.

```{list-table}
:header-rows: 1
:name: tab-ig-issue-management-process

* - Statement
  - Guidance
  - Importance
* - Issues resulting from deviations from processes, incidents and audit findings should be logged, tracked and resolved.
  - This process should be tracked through an electronic record and workflow system with records retained.
  - Mandatory
* - Issues are a key input to process improvement and risk management and should be used to inform changes.
  - All issues should be analysed for their route cause and improvements put in place to prevent further occurrence.
  - Mandatory
```

### Quality Management Data (Including training records and configuration data)

Data collected and used to monitor, evaluate, and improve the quality of processes, or services within the TRE organisation.

```{list-table}
:header-rows: 1
:name: tab-ig-quality-management-data

* - Statement
  - Guidance
  - Importance
* - Quality data forms the basis for measuring the effectiveness of a TRE. This data should be carefully collected, maintained and visualised.
  - Marge amounts of data will be produced by elements within the TRE. These data should be analysed with reports and dashboards provided to guide TRE implementer’s improvements and provide re-assurance to data consumers and subjects.
  - Mandatory
```

### Electronic Quality Management System Application (Application Component)

A software application or platform used to manage and automate quality management processes, including document control, corrective actions, audits, and performance tracking.

```{list-table}
:header-rows: 1
:name: tab-ig-electronic-quality-management-system-application

* - Statement
  - Guidance
  - Importance
* - An eQMS (Electronic Quality Management System) helps to standardise and automate quality management tasks and workflows and can generate quality data and reports automatically.
  - A basis eQMS could be a set of spreadsheets or documents held in a repository which are manually maintained.
    More mature applications will provide workflows and generate quality data through manual and automated actions.
  - Optional
```

## Risk Management

What the organisation does to ensure information risk is measured and managed to an acceptable level.

### Risk Assessment (Process)

The systematic evaluation and analysis of potential risks, threats, or vulnerabilities, including their likelihood, potential impact, and the effectiveness of existing controls or mitigation measures.

```{list-table}
:header-rows: 1
:name: tab-ig-risk-assessment

* - Statement
  - Guidance
  - Importance
* - You have a way to score risk to understand the underlying severity.
  - You have a risk assessment methodology for scoring risks on multiple axes such as impact and likelihood.
  - Mandatory
* - You carry out a data processing assessment for all projects requiring a TRE that are working with sensitive data.
  - A data processing assessment is a process designed to identify risks arising out of the processing of sensitive data and to minimise these risks as far and as early as possible. This may take the form of an existing regulatory requirements such as Data Protection Impact Assessment.
  - Mandatory
```

### Risk Treatment (Business Process)

The selection and implementation of strategies, controls, or measures to manage or mitigate identified risks, such as risk avoidance, risk transfer, risk reduction, or risk acceptance.

```{list-table}
:header-rows: 1
:name: tab-ig-risk-treatment

* - Statement
  - Guidance
  - Importance
* - You have a way to score risk to understand the underlying severity.
  - You have a risk assessment methodology for scoring risks on multiple axes such as impact and likelihood.
  - Mandatory
```

### Risk Ownership (Business Process)

The assignment of responsibility and accountability to individuals or entities for managing and mitigating specific risks within the TRE organisation.

```{list-table}
:header-rows: 1
:name: tab-ig-risk-ownership

* - Statement
  - Guidance
  - Importance
* - You have a clear set of roles and responsibilities relating to risk including who owns risks and how they are escalated and delegated.
  - The highest level of risk ownership is the top management of the TRE organisation. In order to ensure escalations to this level are rare suitable structures should be put in place to own, mitigate and accept risk.
  - Mandatory
* - You understand risk appetite.
  - This includes understanding ownership of risk, and ability to accept risk which falls outside of the appetite should that become necessary.
  - Mandatory
```

## Study Management

What the organisation does to create and maintain research projects and work packages within the TRE.

### Study Onboarding (Business Process)

The process of onboarding or initiating a research study, including setting up necessary infrastructure, obtaining approvals, and defining protocols or methodologies.

```{list-table}
:header-rows: 1
:name: tab-ig-study-onboarding

* - Statement
  - Guidance
  - Importance
* - You have checks in place to ensure a project has the legal, financial and ethical requirements in place for the duration of the project.
  - This includes checks that contracts are in place where required, adequate funding is available for the duration of the project, and responsibilities concerning data ownership are understood by all parties.
  - Mandatory
```

### Compliance Checking (Business Process)

The act of verifying and ensuring adherence to applicable laws, regulations, standards, or internal policies within the TRE organisation.

```{list-table}
:header-rows: 1
:name: tab-ig-compliance-checking

* - Statement
  - Guidance
  - Importance
* - You have checks in place to ensure that any time limited compliance requirements are maintained.
  - This includes ensuring contracts remain in valid and action is promptly taken should they expire.
    Any changes in the status of responsible persons should also be monitored, for example a data owner leaving an organisation.
  - Mandatory
* - You have checks in place to ensure that changes in regulations are met for a project.
  -
  - Mandatory
```

### Study Closure (Business process)

The formal conclusion of a research study or project, including final data analysis, reporting, documentation, and archiving.

```{list-table}
:header-rows: 1
:name: tab-ig-study-closure

* - Statement
  - Guidance
  - Importance
* - You have standard processes in place for the end of a project, that follow all legal requirements and data security best practice.
  - This includes the archiving of quality and log data along with the archiving or deletion of data sets.
  - Mandatory
```

### Study Management Portal (Application Component)

An online platform that provides centralised access to manage research studies including onboarding studies, control of access and administration of compliance tasks.

```{list-table}
:header-rows: 1
:name: tab-ig-study-management-portal

* - Statement
  - Guidance
  - Importance
* - A portal can provide a workflow engine and database which automates the processes within this capability.
  - A portal should automate as much of the processes within the capability as possible.
    Where processes are automated process maturity is easier to achieve with processes being completed more consistently and producing quality control and monitoring data automatically
  - Optional
```

### Data Asset Register (Business Data Object)

A database or other electronic record that documents and manages information about the TRE organisation's data assets, including their characteristics, ownership, usage, and other relevant details.

```{list-table}
:header-rows: 1
:name: tab-ig-data-asset-register

* - Statement
  - Guidance
  - Importance
* - Keep a complete record of all the data assets held within the system.
  - All data asset (current and past) held by the system should be retained along with meta-data useful for ensuring compliance can be demonstrated.
    This would include ownership, data lifecycle, contracts, risk assessments and other quality data.
    This is likely to already exist within the wider organisation but may require augmenting for the TRE.
  - Mandatory
```

### Study Register (Business Data Object)

A centralised record or database that tracks and manages information about research studies and projects.

```{list-table}
:header-rows: 1
:name: tab-ig-study-register

* - Statement
  - Guidance
  - Importance
* - Keep a complete record of all the research studies and projects within the TRE current and past.
  - The study register should contain all data related to a study including a reference to data assets, members (researchers, owners etc.) and any compliance activities required.
  - Mandatory
```

## Member Accreditation

Ability to ensure that people with access to data are identified correctly and they are suitably qualified.

<!-- ### Federation Foundation Services (Group) -->

### Identity Verification (Business Process)

The process of confirming or authenticating the identity of individuals or entities, often through the verification of personal information, credentials, or biometric data.

```{list-table}
:header-rows: 1
:name: tab-ig-identity-verification

* - Statement
  - Guidance
  - Importance
* - You must have a robust method for identifying accredited members of your TRE organisation, prior to their accessing of sensitive data.
  - This may include multi-factor authentication (MFA), ID checks or email/phone verification.
  - Mandatory
```

### User Onboarding

The process of introducing and integrating researchers and data consumers onto a TRE's systems, processes, including training, access provisioning, and orientation.

```{list-table}
:header-rows: 1
:name: tab-ig-user-onboarding

* - Statement
  - Guidance
  - Importance
* - You must have clear onboarding processes in place for all roles within your TRE organisation.
  - This may include all members signing role-specific terms of use and completing role specific training.
  - Mandatory
```

### Identity and Access Management Services (Application Services)

Govern and control user identities, access privileges, authentication, and authorization within an organisation.

```{list-table}
:header-rows: 1
:name: tab-ig-identity-access-management-services

* - Statement
  - Guidance
  - Importance
* - You must have a set of services to manage access to resources based on identity.
  - This will include a security model for role based access with technical controls to ensure the principle of least privilege is enforced.
  - Mandatory
* - Control of who has access to which assets must be within the control of the data asset owner.
  - Either through policy and process or ideally direct control access to data should be controlled by the person who owns a data asset or their delegates.
  - Mandatory
```

### Authentication Application (Application Component)

A software system that verifies and validates the identities of users or entities accessing a system through multifactor authentication.

```{list-table}
:header-rows: 1
:name: tab-ig-authentication-application

* - Statement
  - Guidance
  - Importance
* - There must be robust and secure applications in place to authenticate users (and services) within the TRE.
  - The number of authentication applications should be kept to a minimum with common controls and standards applied across all such as MFA, password complexity etc.
  - Mandatory
```

### User Identity Attributes (Data)

Characteristics or attributes associated with a user's identity, such as username, email address, role, permissions, or affiliations.

```{list-table}
:header-rows: 1
:name: tab-ig-user-identity-attributes

* - Statement
  - Guidance
  - Importance
* - Each user of the TRE must have a unique logon with changes to any record strictly controlled.
  - The unique identifier and all associated records for a user should be traceable across the entire TRE. This will include training records, affiliations, contract agreements and ethics approvals where required.
  - Mandatory
```

## Training Delivery and Management

Ability to deliver, track and maintain adequate training levels to ensure competence of all people within the TRE organisation.

### Curriculum Creation and Management (Business Process)

The process of designing, developing, and managing educational curricula, courses through training needs analysis for required competency.

```{list-table}
:header-rows: 1
:name: tab-ig-curriculum-creation-management

* - Statement
  - Guidance
  - Importance
* - You must have relevant training for all roles within the TRE organisation, and the ability to deliver this training.
  - This may include, for instance, cyber security training, GDPR training, and higher level training for system operators.
    Specific training should be designed for roles such as Senior Information Risk Owner, Data Asset owner. Identification of these specialities should be done through a systematic training needs analysis.
    Specific training may also be required based on the data or data provider such as GCP.
  - Mandatory
* - You should have a training platform capable of delivering online training in a variety of formats.
  - This should include competency testing and more simple recording of actions such as read and understood.
  - Recommended
* - Training is not a one-off event and training may need to be repeated or account for changes in competency requirements.
  - Electronic reminders for refresher training should be considered.
    Ideally training should remain relevant and so policies and processes should enable people to demonstrate competency rather than repeat training unnecessarily.
  - Mandatory
```

### Certification Management (Business Process)

The process of managing and overseeing certifications or qualifications held by individuals or entities, including tracking expiry dates, renewals, and compliance requirements.

```{list-table}
:header-rows: 1
:name: tab-ig-certification-management

* - Statement
  - Guidance
  - Importance
* - Training records should be accurate and be directly tied to the role and access levels within the TRE.
  - Electronic training records should be tied to a user record and carefully maintained.
  - Mandatory
* - You should accept proof of relevant training certifications from third parties.
  - This should include competency testing and more simple recording of actions such as read and understood.
  - Recommended
* - Training is not a one-off event and training may need to be repeated or account for changes in competency requirements.
  - Electronic reminders for refresher training should be considered.
    Ideally training should remain relevant and so policies and processes should enable people to demonstrate competency rather than repeat training unnecessarily.
  - Mandatory
```

### Learning Management System (Application Component)

A software platform or application that facilitates the administration, delivery, and tracking of educational or training programs, often including course materials, assessments, and learner progress tracking.

```{list-table}
:header-rows: 1
:name: tab-ig-learning-management-system

* - Statement
  - Guidance
  - Importance
* - An LMS should be used to manage courses and deliver training as required.
  - Where possible an LMS should support a variety of course content and testing.
  - Optional
```

### Courses Data (Data)

Information or data associated with educational courses, including course materials and syllabi, assessments.

```{list-table}
:header-rows: 1
:name: tab-ig-courses-data

* - Statement
  - Guidance
  - Importance
* - Course data should be transferable between systems where possible.
  - Support for standard formats such as SCORM allows courses to be shared between providers.
  - Optional
* - Historical versions of course may need to be retained in order to demonstrate competency at a given point in time.
  - Data providers and regulators may be required to audit historical records (EG. Clinical trials) it may be necessary to retain copies of superseded training along with versions of certifications within the training record.
  - Optional
```
