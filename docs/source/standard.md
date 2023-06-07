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

_The ability of the TRE organisation to monitor compliance with internal and external requirements, agreements, laws and standards._

| Statement                                                                                        | Guidance                                                                                                                                                  | Mandatory status |
| ------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- |
| You are able to audit your TRE organisation against relevant requirements and standards          | If you are publicly accredited against a standard, for instance ISO27001, DSPT, CE+ etc., you must have processes in place to ensure you remain compliant | Mandatory        |
| You report on and share outcomes of each audit of your TRE organisation with the required bodies | This may included regulatory bodies or the organisations that manage accreditations you have                                                              | Mandatory        |

### 1.2 Policy regulation and management

_How an organsation determines what policies and regulations are required and ensures alignment to changes in requirements._

| Statement                                                                                                                                  | Guidance                                                                                                                                                                                             | Manditory Status |
| ------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- |
| You have a process in place to ensure any new project requiring a TRE meets relevant legal, ethical and contractual requirements           | For example national legislation such as GDPR, discipline specific regulation like GCP or contractural requirements from a specific data provider such as a company or research partner organisation | Mandatory        |
| You have a process in place to monitor changes to any legal, ethical and contractual requirements, and to update your policies accordingly |                                                                                                                                                                                                      | Mandatory        |

### 1.3 Quality management

_The ability of the TRE organisation to measure and control quality of processes, documentation and outputs._

#### Document management

| Statement                                                                                                                               | Guidance                                                                                                                                            | Mandatory status |
| --------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- |
| All policies & standard operating procedures relevant to the TRE organisation are controlled                                            | This may include measures like restricting edit access to relevant documents, and recording acceptance of policies for all TRE organisation members | Mandatory        |
| All policies & standard operating procedures relevant to the TRE organisation are version controlled and have codified change processes | Version control includes recording dates of changes, person responsible for carrying out changes, and summary of changes                            | Mandatory        |

#### Issue management

| Statement                                                                                                                                                 | Guidance                                                                           | Mandatory status |
| --------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------- |
| You have a clear process in place for addressing activity within your TRE organisation that deviates from your policies and standard operating procedures | This can include measures like triage analysis and a process for updating policies | Mandatory        |
| You have methods in place to record progress in resolving issues with, and deviations against, your policies                                              |                                                                                    | Mandatory        |

### 1.4 Risk management

_The ability of the TRE organisation to measure, forecast and evaluate risks to information._

#### Risk assessment

| Statement                                                                                                        | Guidance                                                                                                                                                                         | Mandatory Status |
| ---------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- |
| You have a way to score risk to understand the underlying severity                                               | You have a risk assesment methodology for scoring risks on multiple axes such as impact and likelihood                                                                           | Mandatory        |
| You have a process for mitigating risk using additional controls                                                 | Risks can be reduced to a level which brings it within agreed levels of appetite                                                                                                 | Mandatory        |
| You have an understanding of risk appetite                                                                       | This includes understanding ownership of risk, and ability to accept risk which falls outside of the appetite should that become necessary                                       | Mandatory        |
| You carry out a data processing assessment for all projects requiring a TRE that are working with sensitive data | a data processing assessment is a process designed to identify risks arising out of the processing of sensitive data and to minimise these risks as far and as early as possible | Mandatory        |

### 1.5 Project management

_The ability of the TRE organisation to manage projects effectively._

#### Project onboarding

| Statement                                                                                                                               | Guidance                                                                                                                                                                                                     | Mandatory status |
| --------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------- |
| You have checks in place to ensure a project has the legal, financial and ethical requirements in place for the duration of the project | This includes checks that contracts are in place where required, adequate funding is available for the duration of the project, and responsibilities concerning data ownership are understood by all parties | Mandatory        |

#### Project closure

| Statement                                                                                                                         | Guidance                                                                                              | Mandatory status |
| --------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ---------------- |
| You have standard processes in place for the end of a project, that follow all legal requirements and data security best practice | This includes the archiving of quality and log data along with the archiving or deletion of data sets | Mandatory        |

#### Roles and responsibilities

| Statement                                                                                        | Guidance                                                                                                                                                                                                            | Mandatory status |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- |
| You have clearly defined roles and responsibilities within your TRE organisation for all members | This may include roles such as users, system administrators, system operators, data providers and more. Every member of your TRE organisation should have a pre-defined role with clear powers and responsibilities | Mandatory        |

### 1.6 Member accreditation

The ability of the TRE organisation to ensure that people with access to data are identified correctly and they are suitably qualified.

#### Onboarding members

| Statement                                                                                                                        | Guidance                                                                                               | Mandatory status |
| -------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ | ---------------- |
| You have clear onboarding processes in place for all roles within your TRE organisation                                          | This may include all members signing role-specific terms of use, and completing role specific training | Mandatory        |
| You have a robust method for identifying accredited members of your TRE organisation, prior to their accessing of sensitive data | This may include multi-factor authentication (MFA), ID checks or email/phone verification              | Mandatory        |

#### Training management and delivery

| Statement                                                                                                      | Guidance                                                                                                                                                                                                                                                                                                                    | Mandatory status |
| -------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- |
| You have relevant training for all roles within the TRE organisation, and the ability to deliver this training | This may include: Cyber security training, GDPR training, and higher level training for system operators                                                                                                                                                                                                                    | Mandatory        |
| All TRE organisation members have completed relevant training within the last 12 months                        |                                                                                                                                                                                                                                                                                                                             | Mandatory        |
| You have a process in place to monitor all TRE organisation training completions & requirements                | This process should document which members have completed which training, when the training was completed, and the date the training expires. It should also document how you will notify members when their training is about to expire, and ensure they do not have access to any TRE if relevant training is out-of-date | Mandatory        |

(standard_capability_computing_technology)=

## 2. Computing technology

What the TRE organisation does to manage systems for storing, retrieving, analysing and sending information.

### 2.1 End user computing

The ability of the TRE organisation to provide and manage devices, workspaces, interfaces and applications used by researchers to interact with underlying systems and data.

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

The ability of the TRE organisation to process and analyse data about the usage of the TRE.

| Statement | Guidance |
| --------- | -------- |
|           |          |

### 2.3 Network management

The ability of the TRE organisation to administer and secure network infrastructure using applications, tools and processes.

| Statement | Guidance |
| --------- | -------- |
|           |          |

### 2.4 Infrastructure lifecycle management

The ability of the TRE organisation to manage necessary physical or virtual infrastructure.

#### 2.4.1 Deployment management

_The ability of the TRE organisation to instantiate, deploy, change or remove deployed infrastructure._

```{list-table}
:header-rows: 1
:name: tab-deployment-management
* - Statement
  - Guidance
  - Mandatory status
* - You must have a documented procedure for deploying infrastructure.
  - This might, for instance, be a handbook that is followed or a set of automated scripts.
  - Mandatory
* - Where possible, you should automate any repeatable aspects of your deployment.
  - This might involve using infrastructure-as-code tools or simply a series of scripts.
  - Recommended
* - You must test changes before they are used in production.
  - This might involve a separate development environment or another system for testing.
  - Mandatory
* - You could test changes in a development environment that mirrors your production system.
  - Consider the costs and practicality of whether this will work for your situation.
  - Optional
* - You must have a documented procedure for making changes to deployed infrastructure.
  - This refers both to changes that might be expected in the course of normal operation and emergency changes that might be needed.
  - Mandatory
* - You must have a documented procedure for removing infrastructure when it is no longer needed
  -
  - Mandatory
```

#### 2.4.2 Capacity management

_The ability of the TRE organisation to ensure the right amount of resources are available at the right time to provide a service._

```{list-table}
:header-rows: 1
:name: tab-capacity-management
* - Statement
  - Guidance
  - Mandatory status
* - You must ensure that all projects understand what resources are available and what the associated costs will be before the project starts.
  - For on-premises systems this might be related to the available hardware, for cloud-based systems there might be limits on how many instances of a particular resource (_e.g._ GPUs) can be used. Projects should use this information to understand whether the available resources will be sufficient for their requirements.
  - Mandatory
* - You should ensure that the anticipated needs of projects can be satisfied using available resources.
  - Note that this does not require you to accept requests for additional resources, but rather that promises made about resource availability before a project starts should be honoured wherever possible.
  - Recommended
* - You must ensure that sufficient budget is available to support the anticipated need for resources.
  - For cloud-based TREs this may involve budgeting and/or restricting resource consumption on a project-by-project basis.
    For on-premises TREs this may involve managing expectations to match the available resource.
  - Mandatory
* - You must have a procedure for increasing/decreasing available resources.
  - For cloud-base TREs this may involve scaling resource attributes or deploying additional resources.
  - For on-premises TREs this may involve a procurement process to ensure that necessary resources are available.
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
  - Mandatory status
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
  - Mandatory status
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
