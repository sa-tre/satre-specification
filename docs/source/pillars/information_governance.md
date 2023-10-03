(pillar_information_governance)=

# Information governance

```{figure} ../../images/Capability_Map/full.drawio.svg
:alt: SATRE Pillars Capability Map
:align: center

SATRE Pillars Capability Map
```

This pillar concerns actions taken by the {ref}`TRE operator <infrastructure_roles>` to ensure information risk is measured and managed to an acceptable level.

Each {ref}`TRE operator <infrastructure_roles>` will have its own information governance requirements.
These will be informed by the context of the organisation, the work it performs and the nature of the data it processes.
For example, some requirements will arise from national legislation such as GDPR, discipline specific regulation like GCP, or contractual requirements from a specific {ref}`information asset owner <data_roles>` such as a company or research partner organisation.

## Governance Requirements

### Requirements Gathering and Monitoring

This {term}`business process <business process>` involves collecting, documenting, and managing the functional and non-functional requirements for the TRE based on the TRE organisation's goals and data assets.

```{list-table}
:header-rows: 1
:name: tab-ig-requirements-gathering-monitoring

* -
  - Statement
  - Guidance
  - Importance
* - 1.1.1.
  - You must gather and monitor the information governance requirements needed to fulfil any legal, regulatory and ethical standards.
  - Requirements will come from a variety of sources including legislation, contractual obligations and ethical standards.
    Requirements must be monitored to ensure the TRE controls remain appropriate.
  - Mandatory
```

### Controls

This {term}`business process <business process>` involves measures, safeguards, or mechanisms implemented to manage or mitigate risks associated with your organisational requirements.

```{list-table}
:header-rows: 1
:name: tab-ig-controls

* -
  - Statement
  - Guidance
  - Importance
* - 1.1.2.
  - You must ensure controls are implemented to ensure the requirements are met.
  - Control implementation should be systematic and directly aligned to the internal and stakeholder requirements.
  - Mandatory
```

### Resource Allocation Process

This {term}`business process <business process>` involves assigning, distributing, and managing resources (such as personnel, finances, equipment, or time) within the TRE organisation to meet information governance requirements.

```{list-table}
:header-rows: 1
:name: tab-ig-resource-allocation

* -
  - Statement
  - Guidance
  - Importance
* - 1.1.3.
  - You must ensure there are adequate resources to meet information governance requirements.
  - Ensuring information governance controls are suitable and enforced requires an investment of funding and people appropriate to the size of the TRE.
  - Mandatory
```

(quality_management)=

## Quality Management

What the organisation does to measure and control quality of processes, documentation and outputs.

### Document and SOP Management Process

This {term}`business process <business process>` involves creating, organising, updating, and controlling documents and Standard Operating Procedures (SOPs) within the TRE organisation.

```{list-table}
:header-rows: 1
:name: tab-ig-document-management

* -
  - Statement
  - Guidance
  - Importance
* - 1.2.1.
  - You must ensure that changes to policies and standard operating procedures can only be made by trusted individuals.
  - It is important to ensure that policies and SOPs are relevant, up-to-date and carefully controlled to maintain the integrity and security of your TRE organisation.
  - Mandatory
* - 1.2.2.
  - You must use versioning and a codified change procedure for all policies and standard operating procedures.
  - This includes recording dates of changes, person responsible for carrying out changes, and summary of changes.
  - Mandatory
```

### Quality Management Process

This {term}`business process <business process>` involves the generation and dissemination of reports or dashboards that provide insights and metrics on the performance and effectiveness of quality management processes and activities.

```{list-table}
:header-rows: 1
:name: tab-ig-quality-management

* -
  - Statement
  - Guidance
  - Importance
* - 1.2.3.
  - You should measure the performance of information governance within the TRE with regular reporting available to your TRE organisation's management team.
  - This may include reports and dashboards showing security incidents, quality management deviations and audit findings.
  - Recommended
```

### Internal Audit Process

This {term}`business process <business process>` involves an independent evaluation process within the TRE organisation that assesses and improves its internal controls, risk management, and governance.

```{list-table}
:header-rows: 1
:name: tab-ig-internal-audit

* -
  - Statement
  - Guidance
  - Importance
* - 1.2.4.
  - You must audit your TRE organisation against relevant requirements and standards.
  - If you are publicly accredited against a standard, for instance ISO27001, DSPT, CE+ _etc._, you must have processes in place to ensure you remain compliant.
  - Mandatory
* - 1.2.5.
  - You must report on and share outcomes of each audit of your TRE organisation with the required bodies.
  - This may include regulatory bodies or the organisations that manage accreditations you have.
  - Mandatory
```

### Supplier Management and Monitoring Process

This {term}`business process <business process>` involves a structured approach to managing and monitoring relationships with external suppliers, vendors and contractors, including selection, contract management and compliance oversight.

```{list-table}
:header-rows: 1
:name: tab-ig-supplier-management-monitoring

* -
  - Statement
  - Guidance
  - Importance
* - 1.2.6.
  - You must ensure that suppliers, contractors and sub-contractors with access to your TRE align with your security requirements.
  - These should be included as mandatory, non-functional requirements in during procurement and contracting.
    This will also include contractor staff contracts for example, legal liability and NDAs.
  - Mandatory
* - 1.2.7.
  - You must monitor compliance of your suppliers with the terms of the contracts.
  - This will include monitoring changes in the services and infrastructure being delivered and quality management within the contractor's organisation.
    This may be done through formal audit or by monitoring change and quality documentation provided by the supplier.
  - Mandatory
```

### Asset Management Process

This {term}`business process <business process>` involves a systematic approach to acquiring, operating, maintaining, and disposing of assets within an organization, aimed at maximizing their value and minimizing risks.

```{list-table}
:header-rows: 1
:name: tab-ig-asset-management-process

* -
  - Statement
  - Guidance
  - Importance
* - 1.2.8.
  - You must track and maintain any physical assets used by your TRE.
  - All physical assets should be maintained and covered by warranty if applicable.
    At the end of their lifetime, assets should be securely disposed of in such a way that data cannot be recovered from them.
  - Mandatory (where physical assets are in scope)
```

### Issue Management Process

This {term}`business process <business process>` involves a systematic approach to identifying, tracking, resolving, and managing issues or problems that arise within a TRE organisation, aiming to minimize their impact and ensure timely resolution.

```{list-table}
:header-rows: 1
:name: tab-ig-issue-management-process

* -
  - Statement
  - Guidance
  - Importance
* - 1.2.9.
  - You must log, track and resolve any issues resulting from deviations from processes, incidents and audit findings.
  - This process could, for example, be tracked through an electronic record and workflow system with records retained.
  - Mandatory
* - 1.2.10.
  - You must use reported issues to inform changes, such as for process improvement and risk management.
  - All issues should be analysed for their root cause and improvements put in place to prevent further occurrence.
  - Mandatory
```

### Quality Management Data

This {term}`data object <data object>` consists of data, including training records and configuration data, collected and used to monitor, evaluate, and improve the quality of processes, or services within the TRE organisation.

```{list-table}
:header-rows: 1
:name: tab-ig-quality-management-data

* -
  - Statement
  - Guidance
  - Importance
* - 1.2.11.
  - You should collect and maintain quality management data for measuring the effectiveness of a TRE.
  - Large amounts of data will be produced by elements within the TRE.
    These data should be analysed with reports and dashboards provided to guide TRE implementer's improvements and provide re-assurance to {ref}`data consumers <project_roles>` and {ref}`data subjects <public_roles>`.
  - Recommended
```

### Quality Management System Application

This {term}`application component <application component>` is a software application or platform used to manage and automate quality management processes, including document control, corrective actions, audits, and performance tracking.

```{list-table}
:header-rows: 1
:name: tab-ig-quality-management-system-application

* -
  - Statement
  - Guidance
  - Importance
* - 1.2.12.
  - You could use a QMS (Quality Management System) to standardise and automate quality management tasks and workflows, and to generate quality data and reports automatically.
  - A basic QMS could be a set of spreadsheets or documents held in a repository which are manually maintained.
    More mature applications will provide workflows and generate quality data through manual and automated actions.
  - Optional
```

## Risk Management

What the organisation does to ensure information risk is measured and managed to an acceptable level.

### Risk Assessment Process

This {term}`business process <business process>` involves the systematic evaluation and analysis of potential risks, threats, or vulnerabilities, including their likelihood, potential impact, and the effectiveness of existing controls or mitigation measures.

```{list-table}
:header-rows: 1
:name: tab-ig-risk-assessment

* -
  - Statement
  - Guidance
  - Importance
* - 1.3.1.
  - You must have a way to score risk to understand the underlying severity.
  - You have a risk assessment methodology for scoring risks on multiple axes such as impact and likelihood.
  - Mandatory
* - 1.3.2.
  - You must carry out a data processing assessment for all projects requiring a TRE.
  - A data processing assessment is a process designed to identify risks arising out of the processing of sensitive data and to minimise these risks as far and as early as possible.
    This may take the form of an existing regulatory requirements such as Data Protection Impact Assessment.
  - Mandatory
```

### Risk Treatment Process

This {term}`business process <business process>` involves the selection and implementation of strategies, controls, or measures to manage or mitigate identified risks, such as risk avoidance, risk transfer, risk reduction, or risk acceptance.

```{list-table}
:header-rows: 1
:name: tab-ig-risk-treatment

* -
  - Statement
  - Guidance
  - Importance
* - 1.3.3.
  - You must have a process for designing, implementing and recording risk mitigations where indicated by a risk assessment.
  - Actions that are taken or not taken following a risk assessment must be recorded.
  - Mandatory
```

(risk_ownership_process)=

### Risk Ownership Process

This {term}`business process <business process>` involves the assignment of responsibility and accountability to individuals or entities for managing and mitigating specific risks within the TRE organisation.

```{list-table}
:header-rows: 1
:name: tab-ig-risk-ownership

* -
  - Statement
  - Guidance
  - Importance
* - 1.3.4.
  - You must have a clear set of roles and responsibilities relating to risk including who owns risks and how they are escalated and delegated.
  - The highest level of risk ownership is the Top Management of the TRE organisation (see {ref}`governance_roles`).
    In order to ensure escalations to this level are rare, suitable structures should be put in place to own, mitigate and accept risk.
  - Mandatory
* - 1.3.5.
  - You must understand the risk appetite of your TRE organisation.
  - This includes understanding ownership of risk, and ability to accept risk which falls outside of the appetite should that become necessary.
  - Mandatory
```

## Study Management

What the organisation does to create and maintain research projects and work packages within the TRE.

### Study Onboarding Process

This {term}`business process <business process>` involves onboarding or initiating a research study, including setting up necessary infrastructure, obtaining approvals, and defining protocols or methodologies.

```{list-table}
:header-rows: 1
:name: tab-ig-study-onboarding

* -
  - Statement
  - Guidance
  - Importance
* - 1.4.1.
  - You must have checks in place to ensure a project has the legal, financial and ethical requirements in place for the duration of the project.
  - This includes checks that contracts are in place where required, adequate funding is available for the duration of the project, and responsibilities concerning data handling are understood by all parties.
  - Mandatory
```

### Compliance Checking Process

This {term}`business process <business process>` involves verifying and ensuring adherence to applicable laws, regulations, standards, or internal policies within the TRE organisation.

```{list-table}
:header-rows: 1
:name: tab-ig-compliance-checking

* -
  - Statement
  - Guidance
  - Importance
* - 1.4.2.
  - You must have checks in place to ensure that any time limited compliance requirements are maintained.
  - This includes ensuring contracts remain in valid and action is promptly taken should they expire.
    Any changes in the status of responsible persons should also be monitored, for example a data owner leaving an organisation.
  - Mandatory
* - 1.4.3.
  - You must have checks in place to ensure that changes in regulations are met for a project.
  -
  - Mandatory
```

### Study Closure Process

This {term}`business process <business process>` involves the formal conclusion of a research study or project, including final data analysis, reporting, documentation, and archiving.

```{list-table}
:header-rows: 1
:name: tab-ig-study-closure

* -
  - Statement
  - Guidance
  - Importance
* - 1.4.4.
  - You must have standard processes in place for the end of a project, that follow all legal requirements and data security best practice.
  - This includes the archiving of quality and log data along with the archiving or deletion of data sets.
  - Mandatory
```

### Study Management Portal

This {term}`application component <application component>` is an online platform that provides centralised access to manage research studies including onboarding studies, control of access and administration of compliance tasks.

```{list-table}
:header-rows: 1
:name: tab-ig-study-management-portal

* -
  - Statement
  - Guidance
  - Importance
* - 1.4.5.
  - You could implement a portal that can provide a workflow engine and database which automates the processes within this capability.
  - A portal should automate as much of the processes within the capability as possible.
    Where processes are automated, process maturity is easier to achieve, with more consistent completion and automatic production of quality control and monitoring data.
  - Optional
```

### Data Asset Register

This {term}`data object <data object>` is a database or other electronic record that documents and manages information about the TRE organisation's data assets, including their characteristics, ownership, usage, and other relevant details.

```{list-table}
:header-rows: 1
:name: tab-ig-data-asset-register

* -
  - Statement
  - Guidance
  - Importance
* - 1.4.6.
  - You must keep a complete record of all the data assets held within the system.
  - Details of all data assets (current and past) held by the system should be retained along with meta-data useful for ensuring compliance can be demonstrated.
    This would include ownership, data lifecycle, contracts, risk assessments and other quality data.
    This is likely to already exist within the wider organisation but may require augmenting for the TRE.
  - Mandatory
```

### Study Register

This {term}`data object <data object>` is a centralised record or database that tracks and manages information about research studies and projects.

```{list-table}
:header-rows: 1
:name: tab-ig-study-register

* -
  - Statement
  - Guidance
  - Importance
* - 1.4.7.
  - You should keep a complete record of all the research studies and projects within the TRE current and past.
  - The study register should contain all data related to a study including a reference to data assets, {ref}`project team members <project_roles>`, {ref}`information asset owners <data_roles>` and any compliance activities required.
  - Recommended
```

## Member Accreditation

Ability to ensure that people with access to data are correctly identified and they are suitably qualified.

### Identity Verification Process

This {term}`business process <business process>` involves confirming or authenticating the identity of individuals or entities, often through the verification of personal information, credentials, or biometric data.

```{list-table}
:header-rows: 1
:name: tab-ig-identity-verification

* -
  - Statement
  - Guidance
  - Importance
* - 1.5.1.
  - You must have a robust method for identifying accredited members of your TRE organisation, prior to their accessing of sensitive data.
  - This may include ID checks or email/phone verification.
  - Mandatory
```

### User Onboarding Process

This {term}`business process <business process>` involves introducing and integrating {ref}`data consumers <project_roles>` onto a TRE's systems, processes, including training, access provisioning, and orientation.

```{list-table}
:header-rows: 1
:name: tab-ig-user-onboarding

* -
  - Statement
  - Guidance
  - Importance
* - 1.5.2.
  - You must have clear onboarding processes in place for all roles within your TRE organisation.
  - This may include all members signing role-specific terms of use or confirming that they have completed role specific training.
  - Mandatory
```

### Identity and Access Management Services

This {term}`application component <application component>` is a system to govern and control user identities, access privileges, authentication, and authorization within an organisation.

```{list-table}
:header-rows: 1
:name: tab-ig-identity-access-management-services

* -
  - Statement
  - Guidance
  - Importance
* - 1.5.3.
  - You must have a set of services to manage access to resources based on identity.
  - This will include a security model for role based access with technical controls to ensure the principle of least privilege is enforced.
  - Mandatory
* - 1.5.4.
  - You must not give anyone access to datasets without agreement from the Data Controller.
  - The Data Controller may choose to delegate this authority.
  - Mandatory
```

### Authentication Application

This {term}`application component <application component>` is a software system that verifies and validates the identities of users or entities accessing a system through multifactor authentication.

```{list-table}
:header-rows: 1
:name: tab-ig-authentication-application

* -
  - Statement
  - Guidance
  - Importance
* - 1.5.5.
  - You must have robust and secure applications in place to authenticate users (and services) within the TRE.
  - The number of authentication applications should be kept to a minimum with common controls and standards applied across all such as MFA, password complexity _etc._.
  - Mandatory
```

### User Identity Attributes

This {term}`data object <data object>` consists of characteristics or attributes associated with a user's identity, such as username, email address, role, permissions, or affiliations.

```{list-table}
:header-rows: 1
:name: tab-ig-user-identity-attributes

* -
  - Statement
  - Guidance
  - Importance
* - 1.5.6.
  - You must give each user of the TRE a unique logon with changes to any records strictly controlled.
  - The unique identifier and all associated records for a user should be traceable across the entire TRE.
    This will include training records, affiliations, contract agreements and ethics approvals where required.
  - Mandatory
```

## Training Delivery and Management

Ability to deliver, track and maintain adequate training levels to ensure competence of all people within the TRE organisation.

### Curriculum Creation and Management Process

This {term}`business process <business process>` involves designing, developing, and managing educational curricula, courses through training needs analysis for required competency.

```{list-table}
:header-rows: 1
:name: tab-ig-curriculum-creation-management

* -
  - Statement
  - Guidance
  - Importance
* - 1.6.1.
  - You must determine what training is relevant for all roles within the TRE organisation.
  - This may include, for instance, cyber security training, GDPR training, and higher level training for system operators.
    Specialised roles are likely to need more tailored training.
    Identification of these specialities should be done through a systematic training needs analysis.
    Specific training may also be required based on the data or {ref}`information asset owner <data_roles>` such as GCP.
  - Mandatory
* - 1.6.2.
  - You must ensure that relevant training is available for all roles within the TRE organisation.
  - All TRE organisation members need to complete all relevant training and keep their training current.
    You may need to provide help or guidance to enable them to do so.
    Details of what training is needed will have been determined above.
  - Mandatory
* - 1.6.3.
  - You must provide repeat or updated training where necessary to account for changes in competency requirements.
  - Training is not a one-off event.
    Electronic reminders for refresher training should be considered.
    Ideally, training should remain relevant and so policies and processes should enable people to demonstrate competency rather than unnecessarily repeating training.
  - Mandatory
```

### Certification Management Process

This {term}`business process <business process>` involves managing and overseeing certifications or qualifications held by individuals or entities, including tracking expiry dates, renewals, and compliance requirements.

```{list-table}
:header-rows: 1
:name: tab-ig-certification-management

* -
  - Statement
  - Guidance
  - Importance
* - 1.6.4.
  - You must maintain accurate training records that are directly tied to the role and access levels within the TRE.
  - Training records should be tied to a user record and carefully maintained.
    Maintaining training records enables you to ensure all people have completed the required training and that repeat training happens regularly.
  - Mandatory
* - 1.6.5.
  - You should accept proof of relevant training certifications from trusted third parties.
  - You might choose to trust certifications provided by known training providers or your institution's partner organisations.
  - Recommended
```

### Learning Management System

This {term}`application component <application component>` is a software platform or application that facilitates the administration, delivery, and tracking of educational or training programs, often including course materials, assessments, and learner progress tracking.

```{list-table}
:header-rows: 1
:name: tab-ig-learning-management-system

* -
  - Statement
  - Guidance
  - Importance
* - 1.6.6.
  - You could have a training platform capable of delivering online training in a variety of formats.
  - This could be a simple content delivery platform or a more comprehensive LMS platform.
    It could also include a range of multimedia delivery formats, and accessible training modules for those with access requirements.
  - Optional
* - 1.6.7.
  - You could implement a learning management system (LMS) to manage courses and deliver training as required.
  - Where possible an LMS should support a variety of course content and testing.
  - Optional
```

### Courses Data

This {term}`data object <data object>` consists of information or data associated with educational courses, including course materials and syllabi, assessments.

```{list-table}
:header-rows: 1
:name: tab-ig-courses-data

* -
  - Statement
  - Guidance
  - Importance
* - 1.6.8.
  - You could ensure that any courses you use are available in standard, transferable formats.
  - Support for standard formats such as SCORM allows courses to be shared between providers.
    This could help facilitate standardisation of training provision for TRE users across organisations.
  - Optional
* - 1.6.9.
  - You could keep historical copies of courses in order to demonstrate competency at a given point in time.
  - {ref}`Information asset owners <data_roles>` and regulators may be required to audit historical records, _e.g._ for clinical trials.
    It may be necessary to retain copies of superseded training along with versions of certifications within the training record.
  - Optional
```
