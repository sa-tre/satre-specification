(pillar_data_management)=

# Data management

This capability concerns the ability of the TRE organisation to manage data assets and ensure information remains secure.

```{figure} ../../images/Capability_Map/data_management.drawio.svg
:alt: SATRE Pillars Capability Map
:align: center

SATRE Pillars Capability Map
```

See all pillars of the SATRE Pillars Capability Map here: {ref}`satre_pillars`

## Data lifecycle management

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

## Identity and access management

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

## Output management

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

## Information security

This capability relates to the ability of the TRE organisation to protect against the unauthorized use of information, especially electronic data.

Measures taken to ensure information security can be further categorised into:

- {ref}`vulnerability management <vulnerability-management>`: applying security updates or fixes for identified vulnerabilities
- {ref}`security testing <security-testing>`: proactive penetration testing of a deployed system
- {ref}`encryption <encryption>`: ensuring that data is protected even if the TRE is compromised
- {ref}`physical security <physical-security>`: restricting TRE access to known secure locations

A TRE conforming to the SATRE standard should enact broadly similar measures to protect against the unauthorised use of information, especially electronic data.
These measures include vulnerability management of TRE infrastructure (whether physical or virtual/cloud-based), carrying out compliance checks and security tests of the TRE, common approaches to data encryption, and (where appropriate) physical security measures to prevent unauthorised access to the TRE .

(vulnerability-management)=

### Vulnerability management

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

### Security testing

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

### Encryption

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

### Physical security

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
