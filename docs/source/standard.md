(standard)=

# A Standard Architecture for TREs

<!-- What this document intends to do (and what it doesn't), the level of detail we aim for contrasted with other technical standards -->

The SATRE standard has been developed based on the following principles:

- TREs should be as as easy as possible for end-users to use (_e.g._ researchers) whilst still remaining secure.
- TRE deployments should be offered that support data of different levels of sensitivity (_e.g._ through a tiered system of technical controls and policies).
- TREs conforming to the standard should be interoperable and provide a familiar end-user experience.
- The standard will be managed and updated following an open, community-driven process, and will not be tied to a single vendor or implementation.

The SATRE standard is based around the idea of capabilities, some of which are required and some of which are optional.
Any particular TRE implementation should be able to score itself against each capability as either "supported", "partially supported" or "unsupported" (see {ref}`evaluation` for details).
The capabilities are grouped into the following broad categories:

- {ref}`information governance <standard_capability_information_governance>`
- {ref}`computing technology <standard_capability_computing_technology>`
- {ref}`data management <standard_capability_data_management>`
- {ref}`information security <standard_capability_information_security>`

In addition to these capabilities, any organisation running a TRE (TRE organisation) will need to possess various {ref}`supporting capabilities <standard_capability_supporting>`, particularly around:

- legal requirements — particularly around data protection and contract management
- relationship management — engagement with internal and external stakeholders as well as the wider public

Finally, the TRE organisation will need to consider different {ref}`roles <standard_capability_roles>` with which individuals might interact with the TRE.

There might be good reasons why any particular TRE does not possess one or more of the capabilities listed in this specification, but most TREs should aspire to meet them in the long-term.

<!-- List of capabilities. Each of these hould be described in prose and accompanied by a short requirements table of "Statement" and "Guidance" for each requirement. -->

(standard_capability_information_governance)=

## 1. Information governance

What the TRE organisation does to ensure information risk is measured and managed to an acceptable level.

### 1.1 Compliance, monitoring and reporting

The ability of the TRE organisation to monitor compliance with internal and external requirements, agreements, laws and standards.

| Statement | Guidance |
| --------- | -------- |
|           |          |

### 1.2 Policy regulation and management

TODO: someone needs to write a sentence

| Statement | Guidance |
| --------- | -------- |
|           |          |

### 1.3 Quality management

The ability of the TRE organisation to measure and control quality of processes, documentation and outputs.

| Statement | Guidance |
| --------- | -------- |
|           |          |

#### 1.4 Audit and reporting

The ability of the TRE organisation to adhere to stated processes and external standards.

| Statement | Guidance |
| --------- | -------- |
|           |          |

### 1.5 Risk management

The ability of the TRE organisation to measure, forecast and evaluate risks to information.

| Statement | Guidance |
| --------- | -------- |
|           |          |

### 1.6 Project management

The ability of the TRE organisation to manage projects effectively.

### 1.7 Researcher accreditation

The ability of the TRE organisation to ensure that people with access to data are identified correctly and they are suitably qualified.

#### 1.7.1 Training management

The ability of the TRE organisation to track and maintain adequate training levels.

| Statement | Guidance |
| --------- | -------- |
|           |          |

#### 1.7.2 Training delivery

The ability of the TRE organisation to deliver training.

| Statement | Guidance |
| --------- | -------- |
|           |          |

(standard_capability_computing_technology)=

## 2. Computing technology

What the TRE organisation does to manage systems for storing, retrieving, analysing and sending information.

### 2.1 End user computing

The ability of the TRE organisation to provide and manage devices, workspaces, interfaces and applications used by researchers to interact with underlying systems and data.

#### 2.1.1 User interface

The interfaces used for interacting with the TRE management system and the TRE workspace.

```{list-table}
:header-rows: 1
:name: tab-end-user-user-interface
* - Statement
  - Guidance
* - A TRE must be accessed via a user interface accessible using commonly available applications.
  - TREs which allow users to connect from their own devices should not require the installation of any bespoke TRE application on the user's device.
    In practice a web browser is the most common way to achieve this.
* - A TRE workspace should provide an environment familiar to the users of the TRE.
  - This may be in the form of a virtual Windows or Linux desktops, web applications, or a terminal.
    The use of custom developed TRE-specific software should be avoided when widely used open-source alternatives already exist.
* - A TRE should take accessibility for users with disabilities into account.
  - The restricted nature of TREs means many assistive tools such as screenreaders in a virtual desktop may not be allowed, but other options such as colour schemes, font sizes, and resizing user interface elements, should be supported.
* - Copying out data via the system clipboard must be disabled.
  - A TRE user must not be able to copy sensitive data out of a workspace using the system clipboard.
    A TRE may allow user to paste text into a workspace.
```

#### 2.1.2 Software tools

The tools used by researchers inside a TRE
programming languages, IDEs, desktop applications etc.

```{list-table}
:header-rows: 1
:name: tab-end-user-software-tools
* - Statement
  - Guidance
* - A TRE must provide software applications that are relevant to working with the data in the TRE.
  - The tools provided will depend on the types of data in the TRE, and the expectations of users of the TRE.
    This may include programming languages such as Python and R, integrated development environments, Jupyter notebooks, office type applications such as word processors and spreadsheets, command line tools, etc.
    The set of tools should be reviewed regularly to ensure they are up to date.
* - A TRE should provide tools to encourage best-practice in reproducibly analysing data.
  - Reproducibility of analyses improves auditability and accountability of how data has been used, as well as being best-practice in research.
    This may include version control software, and tools for developing and running data analysis pipelines.
* - A TRE may provide shared services that are accessible to users in the same project.
  - This may include shared file storage, databases, collaborative writing, and other web applications.
    This must only be shared amongst users within the same project.
* - A TRE may provide limited access to some software repositories
  - For example, a TRE may allow installation of packages from Python or R repositories, or provide an internal mirror with approved packages.
```

#### 2.1.3 High performance or cluster computing

The ability to run analyses requiring more compute resources than is present in the user's workspace.

```{list-table}
:header-rows: 1
:name: tab-end-user-high-performance-cluster-computing
* - Statement
  - Guidance
* - A TRE should be able to provide access to high performance computing or other scaleable compute resource if required by users.
  - If a TRE supports users conducting computationally intensive research it should provide access to dynamically scaleable compute or the equivalent.
    For example this may be in the form of a batch scheduler on a HPC cluster, or a dynamically created compute nodes on a cloud platform.
    Users from different projects must not have access to the same compute nodes.
    When using physical compute resources all sensitive data must be securely wiped before another user is given access to that same node.
```

#### 2.1.4 Accelerators

The ability to provide accelerators such as GPUs

```{list-table}
:header-rows: 1
:name: tab-end-user-accelerators
* - Statement
  - Guidance
* - A TRE should be able to provide access to accelerators such as GPUs if required by users.
  - GPUs and other accelerators are commonly used in machine learning and other computationally intensive research.
    TREs should make it clear to users whether GPUs and other resources are available whilst projects are being assessed.
```

#### 2.1.5 Databases

Provision of databases for users
SQL, noSQL, etc.

```{list-table}
:header-rows: 1
:name: tab-end-user-software-tools
* - Statement
  - Guidance
* - A TRE may make data available to researchers using comonly used databases such as PostgreSQL, MSSQL, MongoDB, etc.
  - Databases must be secured and only accessible to users within the same project.
    If shared database servers are used database administrators must ensure the database enforces segregation of users.
```

### 2.2 Infrastructure analytics

The ability of the TRE organisation to record and analyse data about the usage of the TRE.

```{list-table}
:header-rows: 1
:name: tab-end-user-software-tools
* - Statement
  - Guidance
* - A TRE must record usage of the TRE.
  - This may include the number of users, number of projects, the amount of data stored, number of datasets, the number of workspaces, etc.
* - A TRE should record which datasets are accessed, and when
  - This helps auditability of how sensitive data has been used
* - A TRE should record computational resource usage at the user or aggregate level
  - This is useful for optimising allocation of resources, and managing costs.
```

### 2.3 Network management

The ability of the TRE organisation to administer and secure network infrastructure using applications, tools and processes.

```{list-table}
:header-rows: 1
:name: tab-end-user-software-tools
* - Statement
  - Guidance
* - Networks must be managed and controlled to protect information in systems and applications
  - Network infrastructure must prevent unauthorised access to resources on the network.
    This may include firewalls, network segmentation, and restricting connections to the network.
* - Networks must be continually monitored for misconfigurations and vulnerabilities
  - This may include regular vulnerability scanning, and penetration testing.
* - Connectivity between users in different projects, or with access to different datasets, must not be allowed.
  - Connectivity between users in the same project may be allowed, for example to support shared network services within the project.
* - Outbound connections to the internet must be blocked by default.
  - Limited outbound connectivity may be allowed for some services.
```

### 2.4 Infrastructure lifecycle management

The ability of the TRE organisation to manage necessary physical or virtual infrastructure.

| Statement | Guidance |
| --------- | -------- |
|           |          |

#### 2.4.1 Deployment management

The ability of the TRE organisation to instantiate, deploy, change or remove deployed infrastructure.

| Statement | Guidance |
| --------- | -------- |
|           |          |

#### 2.4.2 Capacity management

The ability of the TRE organisation to ensure the right amount of resources are available at the right time to provide a service.

| Statement | Guidance |
| --------- | -------- |
|           |          |

#### 2.4.3 Configuration management

The ability of the TRE organisation to identify, maintain, and verify information on IT assets and configurations in the TRE organisation.

| Statement | Guidance |
| --------- | -------- |
|           |          |

### 2.5 Availability management

The ability of the TRE organisation to ensure all IT infrastructure, processes, tools, roles etc are appropriate for the agreed availability targets.

| Statement | Guidance |
| --------- | -------- |
|           |          |

(standard_capability_data_management)=

## 3. Data management

The ability of the TRE organisation to manage data assets and ensure information remains secure.

### 3.1 Data lifecycle management

The ability of the TRE organisation to manage how and where data is stored, how it moves, changes and is removed.

| Statement | Guidance |
| --------- | -------- |
|           |          |

### 3.2 Identity and access management

The ability of the TRE organisation to ensure the right people (identities) can access the tools and data they need and no more.

| Statement | Guidance |
| --------- | -------- |
|           |          |

### 3.3 Output management

The ability of the TRE organisation to ensure outputs are safely published and shared.

| Statement | Guidance |
| --------- | -------- |
|           |          |

### 3.4 Information discovery

The ability of the TRE organisation to support users who want to browse the data available within an environment at various levels of abstraction.

| Statement | Guidance |
| --------- | -------- |
|           |          |

(standard_capability_information_security)=

## 4. Information security

_The ability of the TRE organisation to protect against the unauthorized use of information, especially electronic data._

Measures taken to ensure information security can be further categorised into:

- {ref}`vulnerability management <vulnerability-management>`: applying security updates or fixes for identified vulnerabilities
- {ref}`security testing <security-testing>`: proactive penetration testing of a deployed system
- {ref}`encryption <encryption>`: ensuring that data is protected even if the TRE is compromised
- {ref}`physical security <physical-security>`: restricting TRE access to known secure locations

A TRE conforming to the SATRE standard should enact broadly similar measures to protect against the unauthorised use of information, especially electronic data.
These measures include vulnerability management of TRE infrastructure (whether physical or virtual/cloud-based), carrying out compliance checks and security tests of the TRE, common approaches to data encryption, and (where appropriate) physical security measures to prevent unauthorised access to the TRE .

(vulnerability-management)=

### 4.1 Vulnerability management

Vulnerability management describes the ability of the TRE organisation to identify, assess, report on, manage and remediate cyber vulnerabilities across endpoints, workloads, and systems.

| Statement                                                                                                                        | Guidance                                                                                                                                                                                                       |
| -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| All computing infrastructure belonging to the TRE should be kept up-to-date with security patches and antivirus (if appropriate) | This might involve scheduling regular automated scanning and application of updates. Infrastructure that is isolated from the internet or immutable in some way may not need to be updated.                    |
| Regular vulnerability scans of TRE infrastructure should be conducted                                                            | Ensuring that scans are done on a regular basis can enable TRE operators can identify and address weaknesses that may have been introduced during the operational lifetime of the TRE.                         |
| TREs should regularly check the compliance of machine and resource configurations                                                | This might involve automated "desired state" enforcement, manual checks or checks over what is possible, for example ensuring that only certain network connections are allowed.                               |
| TREs should adhere to one or more external security standards                                                                    | The TRE organisation should identify appropriate security standards and best practices that it will adhere too. These should be stated to all stakeholders in advance of any data being brought in to the TRE. |

(security-testing)=

### 4.2 Security testing

Security testing enables the TRE organisation to gain assurance in the security of a TRE by testing or attempting to breach some or all of that system's security.

| Statement                                                                                                                                        | Guidance                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Penetration tests should be carried out on TREs                                                                                                  | By intentionally attempting to breach their TRE, organisations can proactively discover unnoticed vulnerabilities before they are exploited maliciously. Tests can evaluate the effectiveness of security controls in preventing data breaches, unauthorised access, or other security incidents                                                                                                                                              |
| TRE security controls should be updated based on the results of security tests                                                                   | Security testing can reveal bugs and discrepancies in the TRE architecture which should be addressed in advance of sensitive data being uploaded, or with urgency in the case of an operational TRE. Regular testing will allow organisations to refine their TRE security controls and incident response capabilities, enabling them to adapt to any new security concerns that may arise as a result of changes in the underlying software. |
| TRE operators must have procedures in place for rapid incident response                                                                          | There may well be legal requirements to disclose details of any incidents, _e.g._ data breaches for organisations subject to GDPR. Having robust processes in place will ensure a swift and effective response when an incident occurs.                                                                                                                                                                                                       |
| TREs should publish details of their security testing strategy and positive results or outcomes (e.g. security fixes) resulting from the testing | Knowledge that regular security testing occurs will help to ensure stakeholders, including researchers and data providers, can trust that the data they work with or are responsible for is secure within a TRE.                                                                                                                                                                                                                              |

(encryption)=

### 4.3 Encryption

_The ability of the TRE organisation to deploy and manage encryption to protect information assets, including data for TRE research projects._

Here we define 'project' data as the data brought in for work which is very likely to be sensitive and 'user' data, as the working files of a project which might hold copies of all or part of the project data or otherwise reveal sensitive data (_e.g._ through hard coded row/column names).

| Statement                                                                    | Guidance                                                                                                                                                                                                                                                                                                     |
| ---------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| TREs must encrypt project and user data at rest                              | This prevents unauthorised access to the data even if the storage media is compromised. This may involve encrypted filesystems or tools to encrypt and decrypt data on demand. The encryption keys may be managed by the TRE organisation or by a trusted external actor (_e.g._ a cloud services provider). |
| TREs must encrypt data when in transit between the TRE and the outside world | Data encryption must be used to safeguard against interception or tampering during transmission. This includes both data ingress and egress and users accessing the TRE, for example over a remote desktop or shell session                                                                                  |
| TREs should encrypt data when in transit inside the TRE                      | If possible, data transfers between different components of a TRE should also be encrypted                                                                                                                                                                                                                   |
| Encryption software should be updated                                        | The latest security patches and updates should be applied to any encryption software being used by the TRE. This helps address any known vulnerabilities or weaknesses in the encryption implementation.                                                                                                     |
| TREs should use secure key management                                        | TREs should employ secure key management practices, including storing encryption keys separately from the encrypted data and implementing strong access controls (_e.g._ Single Sign On) for key management systems.                                                                                         |

(physical-security)=

### 4.4 Physical security

The ability of the TRE organisation to manage and protect physical assets from unauthorised access, damage or destruction.
Physical security controls can provide TREs using highly sensitive data an extra layer of security, even if technical controls are already in place for less sensitive data:

| Statement                                                                                         | Guidance                                                                                                                                                                                                                                                                                                                                                                                                                |
| ------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| TREs could offer physical protection measures against data leakage or theft via physical means    | Restricting access to research facilities containing computers logged into TREs can help prevent malicious actors from viewing or stealing sensitive data, for example by photographing a computer screen. Physical controls on access to a TRE could include surveillance systems, restricting access to locked rooms that limit entry to authorised personnel only, visitor management systems and employee training. |
| TREs hosting particularly sensitive data may need to comply with specific regulatory requirements | Regulatory frameworks such as GDPR emphasise the need for physical security controls to protect sensitive data. Compliance with these regulations could require organisations to implement specific physical security measures to safeguard their TRE from unauthorised access.                                                                                                                                         |

(standard_capability_supporting)=

## 5. Supporting

### 5.1 Legal

The ability of the TRE organisation to access suitable and timely legal advice.

<!-- Specific requirements? _e.g._ Article 32 of the GDPR requires organisations to regularly test and evaluate the effectiveness of the technical and organisational measures employed to protect personal data, and penetration testing is an effective way of assessing your technical defences. -->

| Statement | Guidance |
| --------- | -------- |
|           |          |

### 5.2 Relationship management

The ability of the TRE organisation to maintain engagement with its customers, stakeholders and other interested parties.

| Statement | Guidance |
| --------- | -------- |
|           |          |

### 5.3 Other

The ability of the TRE organisation to access other supporting capabilities such as financial or business continuity.

| Statement | Guidance |
| --------- | -------- |
|           |          |

(standard_capability_roles)=

## 6. Roles

A TRE conforming to the SATRE standard should provide a broadly similar experience for stakeholders operating in each of these defined roles.
There is not necessarily a one-to-one mapping between roles and people.
One person can have multiple roles.

### 6.1 TRE users

The researchers working on projects that involve logging into a TRE to access data.

<!-- The document will explain that user experience of the platform and associated documentation should feel similar across TREs conforming to SATRE standard. -->

| Statement | Guidance |
| --------- | -------- |
|           |          |

### 6.2 TRE administration roles

The IT and related professionals who will be responsible for deploying and managing instances of a TRE conforming to the SATRE standard.
These roles cover managing TRE computing infrastructure, but also administering the TRE itself (_e.g._ managing users and projects).

<!-- The document will explain that SATRE conforming TREs should have documentation and infrastructure deployment code/apps that conform to software engineering best practices, which are also defined here, making them "simple" for an IT professional to follow; troubleshooting steps included. -->

| Statement | Guidance |
| --------- | -------- |
|           |          |

### 6.3 TRE developer roles

The software engineers responsible for developing and maintaining TRE software, including adding functionality, bug fixes and general maintenance.

<!-- The document will explain recommended practices suitable for developing a software of this complexity and reference learnings from existing TRE developers. -->

| Statement | Guidance |
| --------- | -------- |
|           |          |

### 6.4 TRE governance roles

Roles that uphold the governance of TREs.
Such governance responsibilities typically involve establishing policies and procedures to ensure the responsible use of data, protecting the privacy and confidentiality of research participants, and promoting transparency and accountability in research activities.
Typical roles might include data custodians, ethicists, an independent board or a lay panel.

| Statement | Guidance |
| --------- | -------- |
|           |          |

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
