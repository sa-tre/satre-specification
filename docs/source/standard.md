(standard)=

# A Standard Architecture for TREs

<!-- What this document intends to do (and what it doesn't), the level of detail we aim for contrasted with other technical standards -->

## Design

### Overview

The SATRE specification follows a capability-evaluation model.

The specification is presented in terms of capabilities teams should aim for across all aspects of TRE provision.
These capabilities in turn are broken down into components.
Each component is a statement of a process, method or practice teams should have in place to ensure they fulfil the capability requirements.

Any particular component is labelled as mandatory, recommended or optional in order to meet the specification.
Currently, teams are able to either meet the specification (show they can fulfil all mandatory components) or not.
Future versions of the specification may introduce more granular levels of evaluation, for instance tiered level of accreditation based on fulfilment of mandatory, recommended and optional components respectively.

Any particular TRE implementation should be able to score itself against each capability as either supported, partially supported or unsupported (see {ref}`evaluation` for details).

### Architecture

```{figure} ../images/Architecture.svg
:alt: SATRE Specification Architecture
:align: center
```

The SATRE specification contains four key parts:

Architectural Principles
: The principles that all teams looking to use the specification should hold themselves accountable to.

Specification Pillars
: The broad areas of TRE provisioning the specification covers.

TRE Capabilities
: The capabilities within these pillars teams can measure themselves against.

TRE Capability Components
: The statements concerning processes, controls, practices and applications that make up a capability, labelled as mandatory, recommended or optional.

### Pillars and Capability Map

```{figure} ../images/Capability_Map.svg
:alt: SATRE Pillars Capability Map
:align: center
```

The SATRE Specification contains three core pillars for a TRE:

{ref}`Information governance <standard_capability_information_governance>`
: What the organisation does to ensure information risk is measured and managed to an acceptable level.

{ref}`Computing technology <standard_capability_computing_technology>`
: What the organisation does to manage systems for storing, retrieving, and sending information.

{ref}`Data management <standard_capability_data_management>`
: What the organisation does to manage data assets and ensure information remains secure.

In addition to these capabilities, any organisation running a TRE (TRE organisation) will need to possess various {ref}`supporting capabilities <standard_capability_supporting>`.
These will include legal requirements and relationship management.

## Principles

The SATRE standard has been developed based on the following principles:

- TREs should be as as easy as possible for end-users to use (_e.g._ researchers) whilst still remaining secure.
- TRE deployments should be offered that support data of different levels of sensitivity (_e.g._ through a tiered system of technical controls and policies).
- TREs conforming to the standard should be interoperable and provide a familiar end-user experience.
- The standard will be managed and updated following an open, community-driven process, and will not be tied to a single vendor or implementation.

Finally, the TRE organisation will need to consider different {ref}`roles <standard_capability_roles>` with which individuals might interact with the TRE.

There might be good reasons why any particular TRE does not possess one or more of the capabilities listed in this specification, but most TREs should aspire to meet them in the long-term.

<!-- List of capabilities. Each of these hould be described in prose and accompanied by a short requirements table of "Statement" and "Guidance" for each requirement. -->

(standard_capability_information_governance)=

## 1. Information governance

This capability concerns what the TRE organisation does to ensure information risk is measured and managed to an acceptable level.

### 1.1 Compliance, monitoring and reporting

_The ability of the TRE organisation to monitor compliance with internal and external requirements, agreements, laws and standards._

```{list-table}
:header-rows: 1
:name: tab-compliance-monitoring-reporting
* - Statement
  - Guidance
  - Importance
* - You are able to audit your TRE organisation against relevant requirements and standards
  - If you are publicly accredited against a standard, for instance ISO27001, DSPT, CE+ etc., you must have processes in place to ensure you remain compliant
  - Mandatory
* - You report on and share outcomes of each audit of your TRE organisation with the required bodies
  - This may included regulatory bodies or the organisations that manage accreditations you have
  - Mandatory
```

### 1.2 Policy regulation and management

_How the TRE organisation determines what policies and regulations are required and ensures alignment to changes in requirements._

```{list-table}
:header-rows: 1
:name: tab-policy-regulation-management

* - Statement
  - Guidance
  - Importance
* - You have a process in place to ensure any new project requiring a TRE meets relevant legal, ethical and contractual requirements
  - For example national legislation such as GDPR, discipline specific regulation like GCP or contractural requirements from a specific data provider such as a company or research partner organisation
  - Mandatory
* - You have a process in place to monitor changes to any legal, ethical and contractual requirements, and to update your policies accordingly
  -
  - Mandatory
```

### 1.3 Quality management

_The ability of the TRE organisation to measure and control quality of processes, documentation and outputs._

#### 1.3.1 Document management

```{list-table}
:header-rows: 1
:name: tab-document-management

* - Statement
  - Guidance
  - Importance
* - All policies & standard operating procedures relevant to the TRE organisation are controlled
  - This may include measures like restricting edit access to relevant documents, and recording acceptance of policies for all TRE organisation members
  - Mandatory
* - All policies & standard operating procedures relevant to the TRE organisation are version controlled and have codified change processes
  - Version control includes recording dates of changes, person responsible for carrying out changes, and summary of changes
  - Mandatory
```

#### 1.3.2 Issue management

```{list-table}
:header-rows: 1
:name: tab-issue-management

* - Statement
  - Guidance
  - Importance
* - You have a clear process in place for addressing activity within your TRE organisation that deviates from your policies and standard operating procedures
  - This can include measures like triage analysis and a process for updating policies
  - Mandatory
* - You have methods in place to record progress in resolving issues with, and deviations against, your policies
  -
  - Mandatory
```

### 1.4 Risk management

_The ability of the TRE organisation to measure, forecast and evaluate risks to information._

#### 1.4.1 Risk assessment

```{list-table}
:header-rows: 1
:name: tab-risk-assessment

* - Statement
  - Guidance
  - Importance
* - You have a way to score risk to understand the underlying severity
  - You have a risk assesment methodology for scoring risks on multiple axes such as impact and likelihood
  - Mandatory
* - You have a process for mitigating risk using additional controls
  - Risks can be reduced to a level which brings it within agreed levels of appetite
  - Mandatory
* - You have an understanding of risk appetite
  - This includes understanding ownership of risk, and ability to accept risk which falls outside of the appetite should that become necessary
  - Mandatory
* - You carry out a data processing assessment for all projects requiring a TRE that are working with sensitive data
  - A data processing assessment is a process designed to identify risks arising out of the processing of sensitive data and to minimise these risks as far and as early as possible
  - Mandatory
```

### 1.5 Project management

_The ability of the TRE organisation to manage projects effectively._

#### 1.5.1 Project onboarding

```{list-table}
:header-rows: 1
:name: tab-project-onboarding

* - Statement
  - Guidance
  - Importance
* - You have checks in place to ensure a project has the legal, financial and ethical requirements in place for the duration of the project
  - This includes checks that contracts are in place where required, adequate funding is available for the duration of the project, and responsibilities concerning data ownership are understood by all parties
  - Mandatory
```

#### 1.5.2 Project closure

```{list-table}
:header-rows: 1
:name: tab-project-closure

* - Statement
  - Guidance
  - Importance
* - You have standard processes in place for the end of a project, that follow all legal requirements and data security best practice
  - This includes the archiving of quality and log data along with the archiving or deletion of data sets
  - Mandatory
```

#### 1.5.3 Roles and responsibilities

```{list-table}
:header-rows: 1
:name: tab-roles-responsibilities
* - Statement
  - Guidance
  - Importance
* - You have clearly defined roles and responsibilities within your TRE organisation for all members
  - This may include roles such as users, system administrators, system operators, data providers and more. Every member of your TRE organisation should have a pre-defined role with clear powers and responsibilities
  - Mandatory
```

### 1.6 Member accreditation

_The ability of the TRE organisation to ensure that people with access to data are identified correctly and they are suitably qualified._

#### 1.6.1 Onboarding members

```{list-table}
:header-rows: 1
:name: tab-onboarding-members

* - Statement
  - Guidance
  - Importance
* - You have clear onboarding processes in place for all roles within your TRE organisation
  - This may include all members signing role-specific terms of use, and completing role specific training
  - Mandatory
* - You have a robust method for identifying accredited members of your TRE organisation, prior to their accessing of sensitive data
  - This may include multi-factor authentication (MFA), ID checks or email/phone verification
  - Mandatory
```

#### 1.6.2 Training management and delivery

```{list-table}
:header-rows: 1
:name: tab-training-management-delivery

* - Statement
  - Guidance
  - Importance
* - You have relevant training for all roles within the TRE organisation, and the ability to deliver this training
  - This may include: Cyber security training, GDPR training, and higher level training for system operators
  - Mandatory
* - All TRE organisation members have completed relevant training within the last 12 months
  -
  - Mandatory
* - You have a process in place to monitor all TRE organisation training completions & requirements
  - This process should document which members have completed which training, when the training was completed, and the date the training expires. It should also document how you will notify members when their training is about to expire, and ensure they do not have access to any TRE if relevant training is out-of-date
  - Mandatory
```

(standard_capability_computing_technology)=

## 2. Computing technology

This capability concerns what the TRE organisation does to manage systems for storing, retrieving, analysing and sending information.

### 2.1 End user computing

_The ability of the TRE organisation to provide and manage devices, workspaces, interfaces and applications used by researchers to interact with underlying systems and data._

#### 2.1.1 User interface

_The interfaces used for interacting with the TRE management system and the TRE workspace._

```{list-table}
:header-rows: 1
:name: tab-end-user-user-interface

* - Statement
  - Guidance
  - Importance
* - A TRE should be accessed via a user interface accessible using commonly available applications.
  - TREs which allow users to connect from their own devices should not require the installation of any bespoke TRE application on the user's device.
    In practice a web browser is the most common way to achieve this.
  - Recommended
* - A TRE workspace should provide an environment familiar to the users of the TRE.
  - This may be in the form of a virtual Windows or Linux desktops, web applications, or a terminal.
    The use of custom developed TRE-specific software should be avoided when widely used open-source alternatives already exist.
  - Recommended
* - A TRE should take accessibility for users with disabilities into account.
  - The restricted nature of TREs means many assistive tools such as screenreaders in a virtual desktop may not be allowed, but other options such as colour schemes, font sizes, and resizing user interface elements, should be supported.
  - Recommended
* - Copying out data via the system clipboard must be disabled.
  - A TRE user must not be able to copy sensitive data out of a workspace using the system clipboard.
    A TRE may allow user to paste text into a workspace.
  - Mandatory
```

#### 2.1.2 Software tools

_The tools used by researchers inside a TRE, such as programming languages, IDEs and desktop applications._

```{list-table}
:header-rows: 1
:name: tab-end-user-software-tools

* - Statement
  - Guidance
  - Importance
* - A TRE must provide software applications that are relevant to working with the data in the TRE.
  - The tools provided will depend on the types of data in the TRE, and the expectations of users of the TRE.
    This may include programming languages such as Python and R, integrated development environments, Jupyter notebooks, office type applications such as word processors and spreadsheets, command line tools, etc.
    The set of tools should be reviewed regularly to ensure they are up to date.
  - Mandatory
* - A TRE should provide tools to encourage best-practice in reproducibly analysing data.
  - Reproducibility of analyses improves auditability and accountability of how data has been used, as well as being best-practice in research.
    This may include version control software, and tools for developing and running data analysis pipelines.
  - Recommended
* - A TRE may provide shared services that are accessible to users in the same project.
  - This may include shared file storage, databases, collaborative writing, and other web applications.
    This must only be shared amongst users within the same project.
  - Optional
* - A TRE may provide limited access to some software repositories
  - For example, a TRE may allow installation of packages from Python or R repositories, or provide an internal mirror with approved packages.
  - Optional
```

#### 2.1.3 Advanced or cluster computing

_The ability to run analyses requiring more compute resources, or more specialised hardware, than is present in the user's workspace._

```{list-table}
:header-rows: 1
:name: tab-end-user-advanced-cluster-computing

* - Statement
  - Guidance
  - Importance
* - A TRE should be able to provide access to high performance computing or other scaleable compute resource if required by users.
  - If a TRE supports users conducting computationally intensive research it should provide access to dynamically scaleable compute or the equivalent.
    For example this may be in the form of a batch scheduler on a HPC cluster, or a dynamically created compute nodes on a cloud platform.
  - Recommended
* - A TRE should be able to provide access to accelerators such as GPUs if required by users.
  - GPUs and other accelerators are commonly used in machine learning and other computationally intensive research.
    TREs should make it clear to users whether GPUs and other resources are available whilst projects are being assessed.
  - Recommended
* - Segregation of users and data must be maintained when using non-standard compute.
  - High performance or specialist compute is often shared amongst multiple users.
    Users and data must remain segregated at all times.
    For example, when using physical compute resources all sensitive data must be securely wiped before another user is given access to that same node.
    In a cloud hosted TRE virtual machines should be destroyed and recreated.
  - Mandatory
```

#### 2.1.4 Databases

```{list-table}
:header-rows: 1
:name: tab-end-user-databases

* - Statement
  - Guidance
  - Importance
* - A TRE may make data available to researchers using comonly used databases servers such as PostgreSQL, MSSQL, MongoDB, etc.
  - Databases must be secured and only accessible to users within the same project.
    If shared (multi-tenant) database servers are used database administrators must ensure the database server enforces segregation of users and databases.
  - Optional
```

### 2.2 Infrastructure analytics

_The ability of the TRE organisation to record and analyse data about the usage of the TRE._

```{list-table}
:header-rows: 1
:name: tab-end-user-infrastructure-analytics

* - Statement
  - Guidance
  - Importance
* - A TRE must record usage of the TRE.
  - This may include the number of users, number of projects, the amount of data stored, number of datasets, the number of workspaces, etc.
  - Mandatory
* - A TRE should record which datasets are accessed, and when
  - This helps auditability of how sensitive data has been used
  - Recommended
* - A TRE should record computational resource usage at the user or aggregate level
  - This is useful for optimising allocation of resources, and managing costs.
  - Recommended
```

### 2.3 Network management

_The ability of the TRE organisation to administer and secure network infrastructure using applications, tools and processes._

```{list-table}
:header-rows: 1
:name: tab-end-user-network-management

* - Statement
  - Guidance
  - Importance
* - Networks must be managed and controlled to protect information in systems and applications
  - Network infrastructure must prevent unauthorised access to resources on the network.
    This may include firewalls, network segmentation, and restricting connections to the network.
  - Mandatory
* - Networks must be continually monitored for misconfigurations and vulnerabilities
  - This may include regular vulnerability scanning, and penetration testing.
  - Mandatory
* - Connectivity between users in different projects, or with access to different datasets, must not be allowed.
  - Connectivity between users in the same project may be allowed, for example to support shared network services within the project.
  - Mandatory
* - Outbound connections to the internet must be blocked by default.
  - Limited outbound connectivity may be allowed for some services.
  - Mandatory
```

### 2.4 Infrastructure lifecycle management

_The ability of the TRE organisation to manage necessary physical or virtual infrastructure._

#### 2.4.1 Deployment management

_The ability of the TRE organisation to instantiate, deploy, change or remove deployed infrastructure._

```{list-table}
:header-rows: 1
:name: tab-deployment-management

* - Statement
  - Guidance
  - Importance
* - You must have a documented procedure for deploying infrastructure.
  - This might, for instance, be a handbook that is followed or a set of automated scripts.
  - Mandatory
* - Where possible, you should automate any repeatable aspects of your deployment.
  - This might involve using infrastructure-as-code tools or simply a series of scripts.
  - Recommended
* - You must have a documented procedure for making changes to deployed infrastructure.
  - This refers both to changes that might be expected in the course of normal operation and emergency changes that might be needed.
    Your change management process may form part of a wider accreditation such as ISO 27001.
  - Mandatory
* - You must test changes before they are used in production.
  - This might involve a separate development environment or another system for testing.
  - Mandatory
* - You could test changes in a development environment that mirrors your production system.
  - Consider the costs and practicality of whether this will work for your situation.
  - Optional
* - You must have a documented procedure for removing infrastructure when it is no longer needed
  - Removing unused infrastructure not only reduces costs and management burden but also reduces the attack surface of a TRE and reduces the risk of unaddressed vulnerabilities.
  - Mandatory
```

#### 2.4.2 Capacity management

_The ability of the TRE organisation to ensure the right amount of resources are available at the right time to provide a service._

```{list-table}
:header-rows: 1
:name: tab-capacity-management

* - Statement
  - Guidance
  - Importance
* - You must ensure that all projects understand what resources are available and what the associated costs will be before the project starts.
  - For on-premises systems this might be related to the available hardware, for cloud-based systems there might be limits on how many instances of a particular resource (_e.g._ GPUs) can be used. Projects should use this information to understand whether the available resources will be sufficient for their requirements.
  - Mandatory
* - You should ensure that the anticipated needs of projects can be satisfied using available resources.
  - Note that this does not require you to accept requests for additional resources, but rather that promises made about resource availability before a project starts should be honoured wherever possible.
  - Recommended
* - You must ensure that the anticipated resource requirements will not result in overspending by the TRE.
  - For cloud-based TREs this may involve budgeting and/or restricting resource consumption on a project-by-project basis.
    For on-premises TREs this may involve managing expectations to match the available resource.
  - Mandatory
* - You must have a procedure for increasing/decreasing available resources.
  - For cloud-based TREs this may involve scaling resources, such as virtual machines or databases, or deploying additional resources.
    For on-premises TREs this may involve a procurement process to ensure that necessary resources are available.
  - Mandatory
* - You must have a procedure to decide when to change capacity.
  - Not all requests for capacity increase must necessarily be granted, but having a clear process will help projects understand when/why/how they can make use of additional capacity.
  - Mandatory
```

#### 2.4.3 Configuration management

_The ability of the TRE organisation to identify, maintain, and verify information on IT assets and configurations in the TRE organisation._

```{list-table}
:header-rows: 1
:name: tab-configuration-management

* - Statement
  - Guidance
  - Importance
* - You must have a documented procedure for configuring infrastructure.
  - This might, for instance, be a handbook that is followed or a set of automated scripts.
  - Mandatory
* - You should use configuration management tools to automate application of your configuration wherever possible.
  - This might involve configuration-as-code tools such as Ansible, Chef, Puppet or Windows Desired State Configuration or simply automated scripts.
  - Recommended
* - You should be able to verify whether the configuration is valid.
  - This might, for instance, involve running your configuration management tool in 'check' mode.
  - Recommended
* - You should, if possible, regularly verify your TRE configuration.
  - This will limit the amount of time the TRE can spend in a non-compliant state.
  - Mandatory
* - You must be able to replace a non-compliant TRE with a compliant system.
  - This might involve reconfiguring a running system or by replacing it with a compliant one.
  - Mandatory
```

### 2.5 Availability management

_The ability of the TRE organisation to ensure all IT infrastructure, processes, tools, roles etc are appropriate for the agreed availability targets._

```{list-table}
:header-rows: 1
:name: tab-availability-management

* - Statement
  - Guidance
  - Importance
* - You should understand the availability and uptime guarantees of any providers that you rely on.
  - For remote TREs this might include your cloud provider(s) and/or data centre operators.
    For on-premises TREs, it might be worth considering your ISP and electricity provider.
  - Recommended
* - You should develop an availability target or statement and share this with your users.
  - Understanding how and when the TRE might be unavailable will help your projects in planning their work.
  - Recommended
```

(standard_capability_data_management)=

## 3. Data management

This capability concerns the ability of the TRE organisation to manage data assets and ensure information remains secure.

### 3.1 Data lifecycle management

_The ability of the TRE organisation to manage how and where data is stored, how it moves, changes and is removed._

```{list-table}
:header-rows: 1
:name: tab-data-lifecycle-management

* - Statement
  - Guidance
  - Importance
* - A TRE must have a data ingress process which enforces information governance rules/processes.
  - The data ingress process needs to ensure that information governance is correctly followed.
    In particular, it should require that an ingress request has been approved by all required parties.
  - Mandatory
* - A TRE must have a data egress process which enforces information governance rules/processes.
  - The data egress process needs to ensure that information governance requirements are adhered to.
    In particular, it should require that an egress request has been approved by all required parties.
  - Mandatory
* - A TRE's data egress process could sometimes require project-independent approval.
  - There may be cases where there are multiple stakeholders for a piece of analysis including data providers, data analysts, data subjects, the TRE organisation.
    A data egress process may then require approval from people not on the project team, for example an external referee or TRE organisation representative
  - Optional
* - A TRE must keep a record of what data it holds.
  - Good records are important for ensuring compliance with legislation, understanding risk and aiding good data hygiene.
    The record should include a description of the data, its source, contact details for the data owner, which projects use the data, the date it was received, when it is expected to no longer be needed.
  - Mandatory
* - A TRE must have a policy on data deletion.
  - There should be a clear, published policy on when data will be retained or deleted.
    This may allow time for data owners to consider outputs they may want to extract from the TRE.
    Any sensitive data, including all backups, should be deleted when they are no longer needed.
    Having clear policies will help to avoid problems with data being kept longer than necessary or accidental deletion of outputs.
  - Mandatory
* - A TRE could keep backups of data and research environments, provided that this is permitted by law.
  - Keeping backups could help reduce the impact of events like accidental deletion and data corruption on work in a TRE.
    TRE developers may want to consider how different elements, for example sensitive input data or users workspaces, may be backed up or if they should be.
  - Optional
* - A TRE should log how input data is modified.
  - If the input data is mutable a TRE should keep records of its modification.
    For example, when the data was modified and by who.
  - Recommended
* - A TRE must, to a reasonable extent, prevent unauthorised data ingress or egress
  - Movement of data which has not been subject to information governance processes risks breaking rules and is more likely to result in a data breach.
    However, it is difficult to control for every possibility.
    For example, a user may take pictures of their computer screen to remove data, or use a device presenting as a USB HID keyboard to input large amounts of text.
    An example of a reasonable measure would be for a remote desktop based TRE to prevent data being copied from a local machine's clipboard to a workspace.
  - Mandatory
```

### 3.2 Identity and access management

_The ability of the TRE organisation to ensure the right people (identities) can access the tools and data they need and no more._

```{list-table}
:header-rows: 1
:name: tab-identity-and-access-management

* - Statement
  - Guidance
  - Importance
* - A TRE must not create user accounts for use by more than one person.
  - It is important that each user account should be used by one, and only one, person in order to facilitate the assignment of roles or permissions and to log the actions of individuals.
  - Mandatory
* - A TRE must be reasonably convinced of the identity of the person being granted an account.
  - It is important to ensure access, via an account, has been given to the correct person.
    For example, multiple credentials may be used before account creation to verify identity or, when appropriate, photo ID checks may be required.
  - Mandatory
* - A TRE must restrict a users access to only data required in their work.
  - There is no need to grant an individual access to data they do not require.
    Access may be assigned in a manner appropriate to a TREs design, for example through roles granted to user accounts or through isolated project workspaces.
  - Mandatory
* - A TRE must ensure multi-factor authentication for users.
  - Multi-factor authentication ensures that to successfully connect a user must have more than one piece of evidence in different categories.
    Categories include something the user knows (_e.g._ a password), something the user possesses (_e.g._ a TOTP key) or something the user is (_e.g._ biometric data).
    A TRE does not need to implement multi-factor authentication checks itself if it is provided by a third-party identity provider.
  - Mandatory
* - A TRE could restrict access to particular locations.
  - Restricting access to a set of known, static, personal or institutional IP addresses can help avoid speculative attacks.
    When appropriate, access could also be restricted to physical locations with security controls and access requirements.
  - Optional
```

### 3.3 Output management

_The ability of the TRE organisation to ensure outputs are safely published and shared._

```{list-table}
:header-rows: 1
:name: tab-output-management

* - Statement
  - Guidance
  - Importance
* - A TRE should have a system to aid classifying outputs.
  - Removing data from a TRE can be a difficult process as there is potential for sensitive data to be revealed.
    Having guidance, processes and methods will help ensure that outputs are correctly classified and, furthermore, that outputs due to be openly published are identified.
    Encouraging openly published outputs rather than handing all outputs to the data provider will enhance a TRE's impact.
  - Recommended
* - A TRE should establish each project's intended outputs from the outset.
  - Identifying the purpose of a piece of work is important for compliance with data protection legislation.
    Results will be produced which address the project's purpose, some of which may be outputs that are removed from the TRE.
    Understanding what these outputs are likely to be and their sensitivity as early as possible will help prepare for their processing and publication.
  - Recommended
```

(standard_capability_information_security)=

## 4. Information security

This capability relates to the ability of the TRE organisation to protect against the unauthorized use of information, especially electronic data.

Measures taken to ensure information security can be further categorised into:

- {ref}`vulnerability management <vulnerability-management>`: applying security updates or fixes for identified vulnerabilities
- {ref}`security testing <security-testing>`: proactive penetration testing of a deployed system
- {ref}`encryption <encryption>`: ensuring that data is protected even if the TRE is compromised
- {ref}`physical security <physical-security>`: restricting TRE access to known secure locations

A TRE conforming to the SATRE standard should enact broadly similar measures to protect against the unauthorised use of information, especially electronic data.
These measures include vulnerability management of TRE infrastructure (whether physical or virtual/cloud-based), carrying out compliance checks and security tests of the TRE, common approaches to data encryption, and (where appropriate) physical security measures to prevent unauthorised access to the TRE .

(vulnerability-management)=

### 4.1 Vulnerability management

_The ability of the TRE organisation to identify, assess, report on, manage and remediate technical vulnerabilities across endpoints, workloads, and systems._

```{list-table}
:header-rows: 1
:name: tab-vulnerability-management

* - Statement
  - Guidance
  - Importance
* - All computing infrastructure belonging to the TRE should be kept up-to-date with security patches and antivirus (if appropriate)
  - This might involve scheduling regular automated scanning and application of updates. Infrastructure that is isolated from the internet or immutable in some way may not need to be updated.
  - Recommended
* - Regular vulnerability scans of TRE infrastructure should be conducted
  - Ensuring that scans are done on a regular basis can enable TRE operators can identify and address weaknesses that may have been introduced during the operational lifetime of the TRE.
  - Recommended
* - TREs should regularly check the compliance of machine and resource configurations
  - This might involve automated "desired state" enforcement, manual checks or checks over what is possible, for example ensuring that only certain network connections are allowed.
  - Recommended
* - TREs should adhere to one or more external security standards
  - The TRE organisation should identify appropriate security standards and best practices that it will adhere too. These should be stated to all stakeholders in advance of any data being brought in to the TRE.
  - Recommended
```

(security-testing)=

### 4.2 Security testing

_Security testing enables the TRE organisation to gain assurance in the security of a TRE by testing or attempting to breach some or all of that system's security._

```{list-table}
:header-rows: 1
:name: tab-security-testing

* - Statement
  - Guidance
  - Importance
* - Penetration tests should be carried out on TREs
  - By intentionally attempting to breach their TRE, organisations can proactively discover unnoticed vulnerabilities before they are exploited maliciously. Tests can evaluate the effectiveness of security controls in preventing data breaches, unauthorised access, or other security incidents
  - Recommended
* - TRE security controls should be updated based on the results of security tests
  - Security testing can reveal bugs and discrepancies in the TRE architecture which should be addressed in advance of sensitive data being uploaded, or with urgency in the case of an operational TRE. Regular testing will allow organisations to refine their TRE security controls and incident response capabilities, enabling them to adapt to any new security concerns that may arise as a result of changes in the underlying software.
  - Recommended
* - TRE operators must have procedures in place for rapid incident response
  - There may well be legal requirements to disclose details of any incidents, _e.g._ data breaches for organisations subject to GDPR. Having robust processes in place will ensure a swift and effective response when an incident occurs.
  - Mandatory
* - TREs should publish details of their security testing strategy and positive results or outcomes (e.g. security fixes) resulting from the testing
  - Knowledge that regular security testing occurs will help to ensure stakeholders, including researchers and data providers, can trust that the data they work with or are responsible for is secure within a TRE.
  - Recommended
```

(encryption)=

### 4.3 Encryption

_The ability of the TRE organisation to deploy and manage encryption to protect information assets, including data for TRE research projects._

Here we define 'project' data as the data brought in for work which is very likely to be sensitive and 'user' data, as the working files of a project which might hold copies of all or part of the project data or otherwise reveal sensitive data (_e.g._ through hard coded row/column names).

```{list-table}
:header-rows: 1
:name: tab-encryption

* - Statement
  - Guidance
  - Importance
* - TREs must encrypt project and user data at rest
  - This prevents unauthorised access to the data even if the storage media is compromised. This may involve encrypted filesystems or tools to encrypt and decrypt data on demand. The encryption keys may be managed by the TRE organisation or by a trusted external actor (_e.g._ a cloud services provider).
  - Mandatory
* - TREs must encrypt data when in transit between the TRE and the outside world
  - Data encryption must be used to safeguard against interception or tampering during transmission. This includes both data ingress and egress and users accessing the TRE, for example over a remote desktop or shell session
  - Mandatory
* - TREs should encrypt data when in transit inside the TRE
  - If possible, data transfers between different components of a TRE should also be encrypted
  - Recommended
* - Encryption software should be updated
  - The latest security patches and updates should be applied to any encryption software being used by the TRE. This helps address any known vulnerabilities or weaknesses in the encryption implementation.
  - Recommended
* - TREs should use secure key management
  - TREs should employ secure key management practices, including storing encryption keys separately from the encrypted data and implementing strong access controls (_e.g._ Single Sign On) for key management systems.
  - Recommended
```

(physical-security)=

### 4.4 Physical security

_The ability of the TRE organisation to manage and protect physical assets from unauthorised access, damage or destruction._

Physical security controls can provide TREs using highly sensitive data an extra layer of security, even if technical controls are already in place for less sensitive data:

```{list-table}
:header-rows: 1
:name: tab-physical-security

* - Statement
  - Guidance
  - Importance
* - TREs could offer physical protection measures against data leakage or theft via physical means
  - Restricting access to research facilities containing computers logged into TREs can help prevent malicious actors from viewing or stealing sensitive data, for example by photographing a computer screen. Physical controls on access to a TRE could include surveillance systems, restricting access to locked rooms that limit entry to authorised personnel only, visitor management systems and employee training.
  - Optional
* - TREs hosting particularly sensitive data may need to comply with specific regulatory requirements
  - Regulatory frameworks such as GDPR emphasise the need for physical security controls to protect sensitive data. Compliance with these regulations could require organisations to implement specific physical security measures to safeguard their TRE from unauthorised access.
  - Optional
```

(standard_capability_supporting)=

## 5. Supporting

### 5.1 Legal

_The ability of the TRE organisation to access suitable and timely legal advice._

<!-- Specific requirements? _e.g._ Article 32 of the GDPR requires organisations to regularly test and evaluate the effectiveness of the technical and organisational measures employed to protect personal data, and penetration testing is an effective way of assessing your technical defences. -->

```{list-table}
:header-rows: 1
:name: tab-legal

* - Statement
  - Guidance
  - Importance
* -
  -
  -
```

### 5.2 Relationship management

_The ability of the TRE organisation to maintain engagement with its customers, stakeholders and other interested parties._

```{list-table}
:header-rows: 1
:name: tab-relationship-management

* - Statement
  - Guidance
  - Importance
* -
  -
  -
```

### 5.3 Other

_The ability of the TRE organisation to access other supporting capabilities such as financial or business continuity._

```{list-table}
:header-rows: 1
:name: tab-other

* - Statement
  - Guidance
  - Importance
* -
  -
  -
```

(standard_capability_roles)=

## Roles

A TRE conforming to the SATRE standard should provide a broadly similar experience for stakeholders operating in each of these defined roles.
There is not necessarily a one-to-one mapping between roles and people.
One person can have multiple roles.

### TRE users

The researchers working on projects that involve logging into a TRE to access data.

<!-- The document will explain that user experience of the platform and associated documentation should feel similar across TREs conforming to SATRE standard. -->

```{list-table}
:header-rows: 1
:name: tab-tre-role-user

* - Statement
  - Guidance
  - Importance
* -
  -
  -
```

### TRE administration roles

The IT and related professionals who will be responsible for deploying and managing instances of a TRE conforming to the SATRE standard.
These roles cover managing TRE computing infrastructure, but also administering the TRE itself (_e.g._ managing users and projects).

<!-- The document will explain that SATRE conforming TREs should have documentation and infrastructure deployment code/apps that conform to software engineering best practices, which are also defined here, making them "simple" for an IT professional to follow; troubleshooting steps included. -->

```{list-table}
:header-rows: 1
:name: tab-tre-role-administrator

* - Statement
  - Guidance
  - Importance
* -
  -
  -
```

### TRE developer roles

The software engineers responsible for developing and maintaining TRE software, including adding functionality, bug fixes and general maintenance.

<!-- The document will explain recommended practices suitable for developing a software of this complexity and reference learnings from existing TRE developers. -->

```{list-table}
:header-rows: 1
:name: tab-tre-role-developer

* - Statement
  - Guidance
  - Importance
* -
  -
  -
```

### TRE governance roles

Roles that uphold the governance of TREs.
Such governance responsibilities typically involve establishing policies and procedures to ensure the responsible use of data, protecting the privacy and confidentiality of research participants, and promoting transparency and accountability in research activities.
Typical roles might include data custodians, ethicists, an independent board or a lay panel.

```{list-table}
:header-rows: 1
:name: tab-tre-role-governance
* - Statement
  - Guidance
  - Importance
* -
  -
  -
```

## Architecture

<!--
Includes diagrams of how the TRE features connect together, but remains a high level description that doesn't specify which exact technologies a TRE developer should use.
This can also offer an explanation of how people from different roles interact/experience these features.
-->

## Conclusion

<!--
Benefits of adopting this standard for developing a TRE.
Benefits of existing TRE efforts working to conform to this standard (users and admin roles as well as developers).
-->
