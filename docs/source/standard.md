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

In addition to these capabilities, any organisation running a TRE will need to possess various {ref}`supporting capabilities <standard_capability_supporting>`, particularly around:

- legal requirements — particularly around data protection and contract management
- relationship management — engagement with internal and external stakeholders as well as the wider public

Finally, the organisation will need to consider different {ref}`roles <standard_capability_roles>` with which individuals might interact with the TRE.

There might be good reasons why any particular TRE does not possess one or more of the capabilities listed in this specification, but most TREs should aspire to meet them in the long-term.

<!-- List of capabilities. Each of these hould be described in prose and accompanied by a short requirements table of "Statement" and "Guidance" for each requirement. -->

(standard_capability_information_governance)=

## 1. Information governance

What the organisation does to ensure information risk is measured and managed to an acceptable level.

### 1.1 Compliance, monitoring and reporting

The ability of the organisation to monitor compliance with internal and external requirements, agreements, laws and standards.

| Statement | Guidance |
| --------- | -------- |
|           |          |

### 1.2 Policy regulation and management

TODO: someone needs to write a sentence

| Statement | Guidance |
| --------- | -------- |
|           |          |

### 1.3 Quality management

The ability of the organisation to measure and control quality of processes, documentation and outputs.

| Statement | Guidance |
| --------- | -------- |
|           |          |

#### 1.4 Audit and reporting

The ability of the organisation to adhere to stated processes and external standards.

| Statement | Guidance |
| --------- | -------- |
|           |          |

### 1.5 Risk management

The ability of the organisation to measure, forecast and evaluate risks to information.

| Statement | Guidance |
| --------- | -------- |
|           |          |

### 1.6 Project management

The ability of the organisation to manage projects effectively.

### 1.7 Researcher accreditation

The ability of the organisation to ensure that people with access to data are identified correctly and they are suitably qualified.

#### 1.7.1 Training management

The ability of the organisation to track and maintain adequate training levels.

| Statement | Guidance |
| --------- | -------- |
|           |          |

#### 1.7.2 Training delivery

The ability of the organisation to deliver training.

| Statement | Guidance |
| --------- | -------- |
|           |          |

(standard_capability_computing_technology)=

## 2. Computing technology

What the organisation does to manage systems for storing, retrieving, analysing and sending information.

### 2.1 End user computing

The ability of the organisation to provide and manage devices workspaces, interfaces and applications used by researchers to interact with underlying systems and data.

#### 2.1.1 User interface

terminal, desktop, notebook, webapp etc.

| Statement | Guidance |
| --------- | -------- |
|           |          |

#### 2.1.2 Software tools

programming languages, IDEs, desktop applications etc.

| Statement | Guidance |
| --------- | -------- |
|           |          |

#### 2.1.3 High performance computing

| Statement | Guidance |
| --------- | -------- |
|           |          |

#### 2.1.4 Accelerators

GPU, FPGA, ASIC, xPU

| Statement | Guidance |
| --------- | -------- |
|           |          |

#### 2.1.5 Cluster computing

SLURM, Kubernetes etc.

| Statement | Guidance |
| --------- | -------- |
|           |          |

#### 2.1.6 Databases

SQL, noSQL, etc.

| Statement | Guidance |
| --------- | -------- |
|           |          |

### 2.2 Infrastructure analytics

The ability of the organisation to process and analyse data about the usage of the TRE.

| Statement | Guidance |
| --------- | -------- |
|           |          |

### 2.3 Network management

The ability of the organisation to administer and secure network infrastructure using applications, tools and processes.

| Statement | Guidance |
| --------- | -------- |
|           |          |

### 2.4 Infrastructure lifecycle management

The ability of the organisation to manage necessary physical or virtual infrastructure.

| Statement | Guidance |
| --------- | -------- |
|           |          |

#### 2.4.1 Deployment management

The ability of the organisation to instantiate, deploy, change or remove deployed infrastructure.

| Statement | Guidance |
| --------- | -------- |
|           |          |

#### 2.4.2 Capacity management

The ability of the organisation to ensure the right amount of resources are available at the right time to provide a service.

| Statement | Guidance |
| --------- | -------- |
|           |          |

#### 2.4.3 Configuration management

The ability of the organisation to identify, maintain, and verify information on IT assets and configurations in the organisation.

| Statement | Guidance |
| --------- | -------- |
|           |          |

### 2.5 Availability management

The ability of the organisation to ensure all IT infrastructure, processes, tools, roles etc are appropriate for the agreed availability targets.

| Statement | Guidance |
| --------- | -------- |
|           |          |

(standard_capability_data_management)=

## 3. Data management

The ability of the organisation to manage data assets and ensure information remains secure.

### 3.1 Data lifecycle management

The ability of the organisation to manage how and where data is stored, how it moves, changes and is removed.

```{list-table}
:header-rows: 1
:name: tab-data-lifecycle-management

* - Statement
  - Guidance
* - A TRE must have a data ingress process which enforces information governance rules/processess.
  - The data ingress process needs to ensure that information governance is correctly followed.
    in particular, it should require that an ingress request has been approved by all required par ties.
* - A TRE must have a data egress process which enforces information governance rules/processess.
  - The data egress process needs to ensure that information governance is correctly followed.
    in particular, it should require that an egress request has been approved by all required par ties.
* - A TRE could require independent approval for data ingress and egress events.
  - A person indepdent to a project, for example a TRE admin or dedicated referee, could check ingress and egress requests to ensure information governance is correctly followed in the absence of an automated process.
* - A TRE must keep a record of what data it holds.
  - Good records are important for ensuring compliance with legislation, understanding risk and aiding good data hygiene.
    The record should include a description of the data, its source, contact details for the data owner, which projects use the data, the data it was recieved, when it is expected to no longer be needed.
* - A TRE must have a policy on data deletion.
  - There should be a clear, published policy on when data will be deleted beyond at the conclusion of a project.
    This may allow time for data owners to consider outputs they may want to extract from the TRE.
    Any sensitive data, including all backups, should be deleted when they are no longer needed.
    Having clear policy will help to avoid problems with data being kept longer than necessary or accidental deletion of outputs.
* - A TRE could keep backups of data and research environments
  - Keeping backups could help reduce the impact of events like accidental deletion and data corruption on work in a TRE.
    TRE developers may want to consider how different elements, for example sensitive input data or users workspaces, may be backed up or if they should be.
* - A TRE should log how input data is modified.
  - If the input data is mutable a TRE should keep records of its modification.
    For example when the data was modified and by who.
* - A TRE must, to a reasonable extent, prevent unathorised data ingress or egress
  - Movement of data which has not been subject to information governance processes risks breaking rules and is more likely to result in a data breach.
    However, it is difficult to control for every possibility.
    For example, a user may take pictures of their computer screen to remove data, or using a device presnting as a USB HID keyboard to input large amounts of text.
    An example of a reasonable measure would be for a remote desktop based TRE to prevent data being shared between a workspace's and local machine's clipboards.
```

### 3.2 Identity and access management

The ability of the organisation to ensure the right people (identities) can access the tools and data they need and no more.

```{list-table}
:header-rows: 1
:name: tab-identity-and-access-management

* - Statement
  - Guidance
* - A TRE must not create user accounts for use by more than one person.
  - It is important that each user account should be used by one, and only one, person in order to facilitate the assignment of roles or permissions and to log the actions of individuals.
* - A TRE must be reasonably convinced of the identity of the person being granted an account.
  - It is important to ensure access, via an account, has been given to the correct person.
    For example, multiple credentials may be used in account creation to verify identitity or, when appropriate, photo ID checks may be required.
* - A TRE must restrict a users access to only data required in their work.
  - There is no need to grant an individual access to data they do not require.
    Access may be assigned in a manner appropriate to a TREs design, for example through roles granted to user accounts or through isolated project workspaces.
* - A TRE must ensure multi-factor authentication for users.
  - Multi-factor authentication ensures that to successfully connect a user must have more than one piece of evidence in different categories.
    Categories include something the user knows (_e.g._ a password), something the user possesses (_e.g._ a TOTP key) or something the user is (_e.g._ biometric data).
    A TRE does not need to implement multi-factor authentication checks itself if it is provided by a third-party identity provider.
* - A TRE could restrict access to particular locations.
  - Restricting access to a set of known, static, personal or instiutional IP addresses can help avoid speculative attacks.
    When appropriate, access could also be restricted to physical locations with security controls and access requirements.
```

### 3.3 Output management

The ability of the organisation to ensure outputs are safely published and shared.

```{list-table}
:header-rows: 1
:name: tab-output-management

* - Statement
  - Guidance
* - A TRE should have a system to aid classifying outputs.
  - Removing data from a TRE can be a difficult process as there is potential for sensitive data to be revealed.
    Having guidance, processess and methods to help will ensure that outputs are correctly classified and, furthermore, that outputs when may be openly published are identified.
    Encouraging openly published outputs will enhance a TREs impact over handing all outputs to the data provider.
* - A TRE should establish projects intended outputs from the outset.
  - Identifying the purpose of a piece of work is important for compliance with data protection legilation.
    Results will be produced which address the projects purpose, some of which may be outputs removed from the TRE.
    Understanding what these outputs are likely to be and their sensitivity as early as possible will help prepare for their processing and publication.
```

(standard_capability_information_security)=

## 4. Information security

The ability of the organisation to protect against the unauthorized use of information, especially electronic data and the measures taken to achieve this.

### 4.1 Vulnerability management

The ability of the organisation to identify, assess, report on, manage and remediate cyber vulnerabilities across endpoints, workloads, and systems.

| Statement | Guidance |
| --------- | -------- |
|           |          |

### 4.2 Security testing

The ability of the organisation to gain assurance in the security of an IT system by testing or attempting to breach some or all of that system's security.

| Statement | Guidance |
| --------- | -------- |
|           |          |

### 4.3 Encryption

The ability of the organisation to deploy and manage encryption to protect information assets.

| Statement | Guidance |
| --------- | -------- |
|           |          |

### 4.4 Physical security

The ability of the organisation to manage and protect physical assets from unauthorised access, damage or destruction.

| Statement | Guidance |
| --------- | -------- |
|           |          |

(standard_capability_supporting)=

## 5. Supporting

### 5.1 Legal

The ability of the organisation to access suitable and timely legal advice.

| Statement | Guidance |
| --------- | -------- |
|           |          |

### 5.2 Relationship management

The ability of the organisation to maintain engagement with its customers, stakeholders and other interested parties.

| Statement | Guidance |
| --------- | -------- |
|           |          |

### 5.3 Other

The ability of the organisation to access other supporting capabilities such as financial or business continuity.

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
These roles cover managing TRE computing infrastructure, but also administering the TRE itself (e.g. managing users and projects).

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
