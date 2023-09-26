(pillar_data_management)=

# Data management

This capability concerns the ability of the {ref}`TRE operator <infrastructure_roles>` to manage data assets and ensure information remains secure.

```{figure} ../../images/Capability_Map/full.drawio.svg
:alt: SATRE Pillars Capability Map
:align: center

SATRE Pillars Capability Map
```

<!-- See all pillars of the SATRE Pillars Capability Map here: {ref}`satre_pillars` -->

(data_lifecycle_management)=

## Data lifecycle management

The ability of the {ref}`TRE operator <infrastructure_roles>` to manage how and where data is stored, how it moves, changes and is removed.

```{list-table}
:header-rows: 1
:name: tab-data-lifecycle-management

* -
  - Statement
  - Guidance
  - Importance
* - 3.1.1.
  - You must have processes in place to assess the legal and regulatory implications of handling the data through its full lifecycle.
  - This involves considering your obligations to data controllers and subjects, and whether any security controls may be legally or contractually required.
    An assessment of the risks involved will also be needed.
    It may involve classifying the project into a predefined sensitivity category or defining bespoke controls.
  - Mandatory
* - 3.1.2.
  - You should keep records of data handling decisions.
  - Decisions that are made as part of the process discussed above should be recorded and made available for inspection by all stakeholders.
  - Recommended
* - 3.1.3.
  - You must have a data ingress process which enforces information governance rules/processes.
  - The data ingress process needs to ensure that information governance is correctly followed.
    In particular, it should require that an ingress request has been approved by all required parties.
  - Mandatory
* - 3.1.4.
  - You must have a data egress process which enforces information governance rules/processes.
  - The data egress process needs to ensure that information governance requirements are adhered to.
    In particular, it should require that an egress request has been approved by all required parties.
  - Mandatory
* - 3.1.5.
  - Your data egress process could sometimes require project-independent approval.
  - There may be cases where there are multiple stakeholders for a piece of analysis including {ref}`information asset owners <data_roles>`, data analysts, data subjects, the {ref}`TRE operator <infrastructure_roles>`.
    A data egress process may then require approval from people not on the {ref}`project team <project_roles>`, for example an external referee or {ref}`TRE operator <infrastructure_roles>` representative
  - Optional
* - 3.1.6.
  - You must keep a record of what data your TRE holds.
  - Good records are important for ensuring compliance with legislation, understanding risk and aiding good data hygiene.
    The record should include a description of the data, its source, contact details for the data owner, which projects use the data, the date it was received, when it is expected to no longer be needed.
  - Mandatory
* - 3.1.7.
  - You must have a policy on data deletion.
  - There should be a clear, published policy on when data will be retained or deleted.
    This may allow time for data owners to consider outputs they may want to extract from the TRE.
    Any sensitive data, including all backups, should be deleted when they are no longer needed.
    Having clear policies will help to avoid problems with data being kept longer than necessary or accidental deletion of outputs.
  - Mandatory
* - 3.1.8.
  - You could keep backups of data and research environments, provided that this is permitted by law.
  - Keeping backups could help reduce the impact of events like accidental deletion and data corruption on work in a TRE.
    {ref}`TRE developers <infrastructure_roles>` may want to consider how different elements such as sensitive input data or users' workspaces may be backed up, and whether they should be.
  - Optional
* - 3.1.9.
  - You should log how input data is modified.
  - If the input data is mutable a TRE should keep records of its modification.
    For example, when the data was modified and by who.
  - Recommended
* - 3.1.10.
  - You must, to a reasonable extent, prevent unauthorised data ingress or egress.
  - Movement of data which has not been subject to information governance processes risks breaking rules and is more likely to result in a data breach.
    However, it is difficult to control for every possibility.
    For example, a user may take pictures of their computer screen to remove data, or use a device presenting as a USB HID keyboard to input large amounts of text.
    An example of a reasonable measure would be for a remote desktop based TRE to prevent data being copied from a local machine's clipboard to a workspace.
  - Mandatory
```

## Identity and access management

The ability of the {ref}`TRE operator <infrastructure_roles>` to ensure the right people (identities) can only access the tools and data they need.

```{list-table}
:header-rows: 1
:name: tab-identity-and-access-management

* -
  - Statement
  - Guidance
  - Importance
* - 3.2.1.
  - You must not create user accounts for use by more than one person.
  - It is important that each user account should be used by one, and only one, person in order to facilitate the assignment of roles or permissions and to log the actions of individuals.
  - Mandatory
* - 3.2.2.
  - You must be reasonably convinced of the identity of each person being granted an account.
  - It is important to ensure an account has been given to the correct person.
    For example, multiple credentials may be used before account creation to verify identity or, when appropriate, photo ID checks may be required.
  - Mandatory
* - 3.2.3.
  - You must restrict a user's access to only data required in their work.
  - There is no need to grant an individual access to data they do not require.
    Access may be assigned in a manner appropriate to a TREs design, for example through roles granted to user accounts or through isolated project workspaces.
  - Mandatory
* - 3.2.4.
  - You must ensure that multi-factor authentication is enabled for all users.
  - Multi-factor authentication ensures that to successfully connect a user must have more than one piece of evidence in different categories.
    Categories include something the user knows (_e.g._ a password), something the user possesses (_e.g._ a TOTP key) or something the user is (_e.g._ biometric data).
    A TRE does not need to implement multi-factor authentication checks itself if it is provided by a third-party identity provider.
  - Mandatory
* - 3.2.5.
  - You could use federated authentication or single sign-on (SSO) for user login.
  - Institutions that use a SSO for other applications may wish to extend this login capability to a TRE.
    This will simplify the login process for {ref}`data consumers <project_roles>` using a TRE and prevent them having to remember or store multiple login credentials.
  - Optional
* - 3.2.6.
  - You could restrict access to particular networks or physical locations.
  - Restricting access to a set of known, static, personal or institutional IP addresses can help avoid speculative attacks.
    When appropriate, access could also be restricted to physical locations with security controls and access requirements.
  - Optional
```

(output_management)=

## Output management

The ability of the {ref}`TRE operator <infrastructure_roles>` to ensure outputs are safely published and shared.

```{list-table}
:header-rows: 1
:name: tab-output-management

* -
  - Statement
  - Guidance
  - Importance
* - 3.3.1.
  - You should have a system to help classify outputs.
  - Removing data from a TRE can be a difficult process as there is potential for sensitive data to be revealed.
    Having guidance, processes and methods will help ensure that outputs are correctly classified and, furthermore, that outputs due to be openly published are identified.
    Encouraging openly published outputs rather than handing all outputs to the {ref}`information asset owner <data_roles>` will enhance a TRE's impact.
  - Recommended
* - 3.3.2.
  - You should establish the intended outputs of each project from the outset.
  - Identifying the purpose of a piece of work is important for compliance with data protection legislation.
    Results will be produced which address the project's purpose, some of which may be outputs that are removed from the TRE.
    Understanding what these outputs are likely to be and their sensitivity as early as possible will help prepare for their processing and publication.
  - Recommended
* - 3.3.3.
  - You must have a documented process for disclosure control of outputs from the TRE.
  - This process should define expected risks and how to mitigate them.
    All TRE outputs must be subject to this process.
    You might choose to follow existing guidelines, for example around statistical disclosure.
  - Mandatory
* - 3.3.4.
  - You must have a process for assigning responsibility for output checking.
  - {ref}`Output checkers <data_roles>` should be given responsibility for checking outputs.
    They must follow your disclosure control process and will be responsible for any automated parts of this process.
    Output checking can help mitigate against unintentional data disclosure or leaks.
  - Mandatory
* - 3.3.5.
  - You must have a documented policy for handling disclosure risks associated with any outputs that cannot be manually checked.
  - Some categories of output, for instance binary files or very large numeric files, can be difficult to manually check.
    If egress of such files is permitted then the risks of inadvertent disclosure must be mitigated and documented.
    Refusing to allow egress of such files is also a valid policy decision.
  - Mandatory
```

(information-search-and-discovery)=

## Information search and discovery

The ability to query and browse the data within an environment at various levels of abstraction.

```{list-table}
:header-rows: 1
:name: tab-information-search-and-discovery

* -
  - Statement
  - Guidance
  - Importance
* - 3.4.1.
  - You could make a catalogue of sensitive data that you make available to users.
  - This is particularly relevant for TREs that are an interface to a common data collection.
    This may not be appropriate for TREs where each project has its own data sharing agreement with one or more {ref}`information asset owners <data_roles>`.
  - Optional
```

(standard_capability_information_security)=

## Information security

The ability of the {ref}`TRE operator <infrastructure_roles>` to protect against the unauthorised use of information, especially electronic data.

Measures taken to ensure information security can be further categorised into:

- {ref}`vulnerability management <vulnerability-management>`: applying security updates or fixes for identified vulnerabilities
- {ref}`security testing <security-testing>`: proactive penetration testing of a deployed system
- {ref}`encryption <encryption>`: ensuring that data is protected even if the TRE is compromised
- {ref}`physical security <physical-security>`: restricting TRE access to known secure locations

A TRE conforming to the SATRE standard should enact broadly similar measures to protect against the unauthorised use of information, especially electronic data.
These measures include vulnerability management of TRE infrastructure (whether physical or virtual/cloud-based), carrying out compliance checks and security tests of the TRE, common approaches to data encryption, and (where appropriate) physical security measures to prevent unauthorised access to the TRE.

(vulnerability-management)=

### Vulnerability Management

The ability of the {ref}`TRE operator <infrastructure_roles>` to identify, assess, report on, manage and remediate technical vulnerabilities across endpoints, workloads, and systems.

```{list-table}
:header-rows: 1
:name: tab-vulnerability-management

* -
  - Statement
  - Guidance
  - Importance

* - 3.5.1.
  - You must have a process in place for applying security updates to all software that forms part of the TRE infrastructure.
  - This includes any software used for remote desktop portals, databases, webapps, creating and destroying compute infrastructure, configuration management, or software used for monitoring the TRE.
  - Mandatory
* - 3.5.2.
  - You must run regular anti-virus/malware scans on all TRE systems where infection could be a problem.
  - Virus and malware scans will help identify malicious code which may compromise the security, or correct operation, of the TRE.
  - Mandatory
* - 3.5.3.
  - Your TRE should adhere to one or more external security standards.
  - These should be stated to all stakeholders in advance of any data being brought in to the TRE.
  - Recommended
```

(security-testing)=

### Security testing

Security testing enables the {ref}`TRE operator <infrastructure_roles>` to gain assurance in the security of a TRE by testing or attempting to breach some or all of that system's security.

```{list-table}
:header-rows: 1
:name: tab-security-testing

* -
  - Statement
  - Guidance
  - Importance
* - 3.5.4.
  - You should carry out penetration tests on your TRE.
  - By intentionally attempting to breach their TRE, organisations can proactively discover unnoticed vulnerabilities before they are exploited maliciously. Tests can evaluate the effectiveness of security controls in preventing data breaches, unauthorised access, or other security incidents.
  - Recommended
* - 3.5.5.
  - You should update the security controls of your TRE based on the results of security tests.
  - Security testing can reveal bugs and discrepancies in the TRE architecture which should be addressed in advance of sensitive data being uploaded, or with urgency in the case of an operational TRE.
    Regular testing will allow organisations to refine their TRE security controls and incident response capabilities.
    It enables them to adapt to any new security concerns that may arise as a result of changes in the underlying software.
  - Recommended
* - 3.5.6.
  - You must have procedures in place for rapid incident response.
  - There may be legal requirements to disclose details of any incidents, such as  data breaches for organisations subject to GDPR.
    Having robust processes in place will ensure a swift and effective response when an incident occurs.
  - Mandatory
* - 3.5.7.
  - You should publish details of your security testing strategy and, where possible, the results of each test.
  - Knowledge that regular security testing occurs will help to ensure stakeholders, including {ref}`data consumers <project_roles>` and {ref}`information asset owners <data_roles>`, can trust that the data they work with or are responsible for is secure within a TRE.
    If security flaws are identified in a test, it may not be sensible to publicise these until a fix is in place.
  - Recommended
```

(encryption)=

### Encryption

The ability of the {ref}`TRE operator <infrastructure_roles>` to deploy and manage encryption to protect information assets, including data for TRE research projects.

Here we define 'project' data as the data brought in for work which is very likely to be sensitive and 'user' data, as the working files of a project which might hold copies of all or part of the project data or otherwise reveal sensitive data (_e.g._ through hard coded row/column names).

```{list-table}
:header-rows: 1
:name: tab-encryption

* -
  - Statement
  - Guidance
  - Importance
* - 3.5.8.
  - Your TRE must encrypt project and user data at rest.
  - This prevents unauthorised access to the data even if the storage media is compromised.
    This may involve encrypted filesystems or tools to encrypt and decrypt data on demand.
    The encryption keys may be managed by the {ref}`TRE operator <infrastructure_roles>` or by a trusted external actor, for example a cloud provider.
  - Mandatory
* - 3.5.9.
  - Your TRE must encrypt data when in transit between the TRE and external networks or computers.
  - Data encryption must be used to safeguard against interception or tampering during transmission.
    This includes both data ingress and egress and users accessing the TRE, for example over a remote desktop or shell session.
  - Mandatory
* - 3.5.10.
  - Your TRE should encrypt data when in transit inside the TRE.
  - If possible, data transfers between different components of a TRE should also be encrypted.
  - Recommended
* - 3.5.11.
  - You should use encryption algorithms and software that are widely accepted as secure.
  - Encryption algorithms widely accepted as secure today may become insecure in the future, for instance due to newly-identified flaws, or advances in compute capabilities.
    The latest security patches and updates should be applied to any encryption software being used by the TRE.
    This helps address any known vulnerabilities or weaknesses in the encryption implementation.
  - Recommended
* - 3.5.12.
  - Your TRE should use secure key management.
  - TREs should employ secure key management practices, including storing encryption keys separately from the encrypted data and implementing strong access controls (_e.g._ Single Sign On) for key management systems.
  - Recommended
```

(physical-security)=

### Physical security

The ability of the {ref}`TRE operator <infrastructure_roles>` to manage and protect physical assets from unauthorised access, damage or destruction.

Physical security controls can provide TREs using highly sensitive data an extra layer of security, even if technical controls are already in place for less sensitive data:

```{list-table}
:header-rows: 1
:name: tab-physical-security

* -
  - Statement
  - Guidance
  - Importance
* - 3.5.13.
  - Your TRE could offer physical protection measures against data leakage or theft via physical means.
  - Restricting access to research facilities containing computers logged into TREs can help prevent malicious actors from viewing or stealing sensitive data, for example by photographing a computer screen.
    Physical controls on access to a TRE could include surveillance systems, restricting physical access to authorised personnel only, visitor management systems and employee training.
  - Optional
* - 3.5.14.
  - Your TRE may need to comply with specific regulatory requirements due to the types of data it is hosting.
  - Regulatory frameworks often emphasise the need for security controls to protect sensitive data.
    Compliance with these regulations could require organisations to implement specific security measures to safeguard their TRE from unauthorised access.
  - Mandatory
```

(security-level)=

## Security Levels and Tiering

The ability of the TRE deployment software (or active TRE) to configure security controls appropriate to the sensitivity of the data used in a project or workspace.

Security controls can add friction to the user experience and hinder work.
A one-size-fits-all approach forces all projects to use the strictest security configuration even when that is unnecessary.
Throughout the rest of this document, we will refer to each pre-defined security configuration supported by a particular TRE as a "security tier".

```{list-table}
:header-rows: 1
:name: tab-security-level

* -
  - Statement
  - Guidance
  - Importance
* - 3.6.1.
  - You must be able to specify what categories of data your TRE is able to support.
  - Your TRE must provide an explanation of the kinds of data it has been designed to hold, with reference to its security capabilities, that can be understood by all stakeholders.
    Relevant stakeholders may include {ref}`information asset owners <data_roles>` and {ref}`project teams <project_roles>` and they may have different levels of technical expertise.
  - Mandatory
* - 3.6.2.
  - Your TRE could support projects with differing security requirements through configurable security controls.
  - This allows projects with different security requirements to each be met with a suitable level of controls.
    It helps ensure that users can work effectively, with minimal barriers.
  - Optional
* - 3.6.3.
  - Your TRE could offer a pre-defined set of security control tiers.
  - Security control tiers can be designed to cover the types of project or data you expect to handle.
    Projects may be placed into the most suitable tier rather than having a bespoke design.
    This reduces the number of unique configurations that need to be supported.
  - Optional
```
