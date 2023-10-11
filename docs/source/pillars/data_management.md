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
  - {ref}`Information asset owners <data_roles>` must classify data sets according to a common process and data classification methodology.
  - To classify the data, information asset owners must have a good understanding of the datasets and the process of classification.
    Once classified, data can be stored in a TRE with an appropriate security controls (see {ref}`later section on security levels and tiering <security-level>`), which can factor in the requirements for confidentiality, integrity and availability of the data.
  - Mandatory
* - 3.1.4.
  - You must have a data ingress process which enforces information governance rules/processes.
  - The data ingress process needs to ensure that information governance is correctly followed.
    In particular, it should require that an ingress request has been approved by all required parties.
  - Mandatory
* - 3.1.5.
  - You must have a data egress process which enforces information governance rules/processes.
  - The data egress process needs to ensure that information governance requirements are adhered to.
    In particular, it should require that an egress request has been approved by all required parties.
  - Mandatory
* - 3.1.6.
  - Egress must be limited to the {ref}`information asset owners <data_roles>` or their delegates.
  - Egress of data from a TRE must be a specific permission associated with individual users
    This permission must be given by information asset owners.
    Egress may still require further approval (see 3.1.5).
  - Mandatory
* - 3.1.7.
  - Your data egress process could sometimes require project-independent approval.
  - There may be cases where there are multiple stakeholders for a piece of analysis including {ref}`information asset owners <data_roles>`, data analysts, data subjects, the {ref}`TRE operator <infrastructure_roles>`.
    A data egress process may then require approval from people not on the {ref}`project team <project_roles>`, for example an external referee or {ref}`TRE operator <infrastructure_roles>` representative
  - Optional
* - 3.1.8.
  - You must keep a record of what data your TRE holds.
  - Good records are important for ensuring compliance with legislation, understanding risk and aiding good data hygiene.
    The record should include a description of the data, its source, contact details for the data owner, which projects use the data, the date it was received, when it is expected to no longer be needed.
  - Mandatory
* - 3.1.9.
  - You must have a policy on data deletion.
  - There should be a clear, published policy on when data will be retained or deleted.
    This may allow time for data owners to consider outputs they may want to extract from the TRE.
    Any sensitive data, including all backups, should be deleted when they are no longer needed.
    Having clear policies will help to avoid problems with data being kept longer than necessary or accidental deletion of outputs.
  - Mandatory
* - 3.1.10.
  - You should have a method of providing proof of deletion/removal of files.
  - {ref}`Information asset owners <data_roles>` may require certification of the deletion of files.
    You should have a method of providing proof of deletion if challenged.
  - Recommended
* - 3.1.11.
  - You should log how input data is modified.
  - If the input data is mutable a TRE should keep records of its modification.
    For example, when the data was modified and by who.
  - Recommended
* - 3.1.12.
  - You must, to a reasonable extent, prevent unauthorised data ingress or egress.
  - Movement of data which has not been subject to information governance processes risks breaking rules and is more likely to result in a data breach.
    However, it is difficult to control for every possibility.
    For example, a user may take pictures of their computer screen to remove data, or use a device presenting as a USB HID keyboard to input large amounts of text.
    An example of a reasonable measure would be for a remote desktop based TRE to prevent data being copied from a local machine's clipboard to a workspace.
  - Mandatory
* - 3.1.13.
  - Data held within the TRE should be the minimum required for analysis or research.
  - Data stored and processed within the TRE should be limited to the amount required for that purpose.
    This increases the level of protection for {ref}`data subjects <public_roles>`, makes it easier to comply with data protection legislation and could reduce the overhead of storage and processing.
  - Recommended
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
    Encouraging openly published outputs will enhance a TRE's impact and transparency.
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
* - 3.3.6
  - You should have a statistical basis to guide the decisions of an output checker on the safety of outputs.
  - There should be a solid basis to allow decisions to be made about data based on risk factors such as re-identification of an individual or risk to commercial operations posed by outputs from the TRE.
  - Recommended
* - 3.3.7
  - You could create a semi-automated system for checks on common research outputs.
  - Automation helps make decisions on outputs more consistent and reduces the overhead for output checkers.
    It’s unlikely however that a fully automated output checking system (without humans in the loop) would be appropriate, given the risks associated with accidental data disclosure.
  - Optional
* - 3.3.8.
  - TRE outputs should be limited to the minimum required for sharing results of any analyses.
  - This decreases the risk of inadvertent disclosure, and makes it easier to comply with data protection legislation (e.g. GDPR).
  - Recommended
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
  - You should provide a metadata catalogue of available datasets for users.
  - This is particularly relevant for TREs with population-level data collection of general interest.
    This may not be appropriate for TREs where each project has its own data sharing agreement with one or more data provider or very sensitive datasets.
  - Recommended
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
* - 3.5.1.
  - You must be able to specify what categories of data your TRE is able to support.
  - Your TRE must provide an explanation of the kinds of data it has been designed to hold, with reference to its security capabilities, that can be understood by all stakeholders.
    Relevant stakeholders may include {ref}`information asset owners <data_roles>` and {ref}`project teams <project_roles>` and they may have different levels of technical expertise.
  - Mandatory
* - 3.5.2.
  - Your TRE could support projects with differing security requirements through configurable security controls.
  - This allows projects with different security requirements to each be met with a suitable level of controls.
    It helps ensure that users can work effectively, with minimal barriers.
  - Optional
* - 3.5.3.
  - Your TRE could offer a pre-defined set of security control tiers.
  - Security control tiers can be designed to cover the types of project or data you expect to handle.
    Projects may be placed into the most suitable tier rather than having a bespoke design.
    This reduces the number of unique configurations that need to be supported.
  - Optional
```

## Research Meta-Data

Descriptive information about research data, helping researchers understand and manage the data effectively.

```{list-table}
:header-rows: 1
:name: tab-meta-data

* -
  - Statement
  - Guidance
  - Importance
* - 3.6.1.
  - You should have a consistent and easily accessible meta-data data model or similar to describe what a data asset contains.
  - Where possible, existing data models should be employed (and extended if necessary).
    More detailed information on the data schema for data assets should also be provided to assist researchers in understanding what data may be available without the need to see the underlying data.
  - Recommended
* - 3.6.2.
  - You could provide summary, abstracted or synthetic data to researchers without exposing the underlying data set.
  - To reduce the need for access to row level data researchers could be provided with non-sensitive versions of the data either as summary data or using synthetic versions of the data for activities such as code development and cohort planning.
  - Optional
```

## Meta-Data Search and Discovery Application

Software designed to help users locate and retrieve specific metadata or information within a database or system.

```{list-table}
:header-rows: 1
:name: tab-meta-data-search

* -
  - Statement
  - Guidance
  - Importance
* - 3.7.1.
  - You could provide an interface application for {ref}`data consumers <project_roles>` and {ref}`data subjects <public_roles>` to query elements of the data.
  - In order to make data findable, an application which queries the meta-data or elements of the research data could be made more easily accessible than the data itself.
  - Optional
```

## Data Archiving

The practice of storing data that is no longer actively used but needs to be retained for historical or compliance reasons.

```{list-table}
:header-rows: 1
:name: tab-data-archiving

* -
  - Statement
  - Guidance
  - Importance
* - 3.8.1.
  - Archived data within the TRE should be read only.
  - Archived data by its very nature should not change and therefore be maintained as a read only store.
    If an update is required, it may be pulled from archive into a separate operational store.
  - Recommended
* - 3.8.2.
  - Long-term archives must be held in simple, standard formats to ensure accessibility.
  - Some data archives may be required by policy or legislation to be kept for very long periods within the scope of the TRE.
    Such data should be held in the simplest possible file format, conforming to international standards if available, to ensure they are platform and application agnostic.
  - Recommended

```
