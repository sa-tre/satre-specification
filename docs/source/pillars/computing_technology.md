(pillar_computing_technology)=

# Computing technology and Information Security

```{figure} ../../images/Capability_Map/full.drawio.svg
:alt: SATRE Pillars Capability Map
:align: center

SATRE Pillars Capability Map
```

This pillar concerns actions taken by the {ref}`TRE operator <infrastructure_roles>` to manage TRE computing systems.

Each {ref}`TRE operator <infrastructure_roles>` will have its own computing technology requirements.
The security controls needed by the computing infrastructure will depend on information governance requirements.
Other computing requirements will be influenced by the technical knowledge and experience of those using the TRE, along with the work they need to perform within the system.
For example, a data scientist will have very different requirements to a clinician.
The required compute resources will vary according to the scale of data and computational techniques employed during research.

<!-- See all pillars of the SATRE Pillars Capability Map here: {ref}`satre_pillars` -->

## End user computing

The ability of the {ref}`TRE operator <infrastructure_roles>` to provide and manage devices, workspaces, interfaces and applications used by {ref}`data consumers <project_roles>` to interact with underlying systems and data.

### End user computing interfaces

This group of {term}`application components <application component>` is a collection of systems and software that allows people to interact with the TRE.
This may include desktop, command-line and/or code-submission interfaces.

```{list-table}
:header-rows: 1
:name: tab-computing-end-user-interfaces

* -
  - Statement
  - Guidance
  - Importance
* - 2.1.1.
  - You must not allow users to copy data out of your TRE via the system clipboard.
  - A TRE user must not be able to copy sensitive data out of a workspace using the system clipboard.
    A TRE may allow user to paste text into a workspace.
    This might not be relevant to your TRE, for example if your user interface does not have a clipboard.
  - Mandatory
* - 2.1.2.
  - Your TRE workspace should provide an environment familiar to your users.
  - This may take the form of a virtual Windows or Linux desktops, non-desktop interfaces such as JupyterLab and other web applications, or a terminal.
    Bespoke TRE-specific software should be avoided when widely used alternatives already exist.
  - Recommended
* - 2.1.3.
  - A TRE could restrict data access from {ref}`data consumers <project_roles>` entirely and provide an interface for submitting code.
  - For example, you might use a system where users submit jobs that run over the data and return results without allowing direct data access.
  - Optional
```

### End user software tools

This {term}`application component <application component>` concerns the tools used by {ref}`data consumers <project_roles>` inside a TRE, such as programming languages, IDEs and desktop applications.

```{list-table}
:header-rows: 1
:name: tab-computing-end-user-software-tools

* -
  - Statement
  - Guidance
  - Importance
* - 2.1.4.
  - Your TRE should be accessed via a user interface using commonly available applications.
  - TREs which allow users to connect from their own devices should not require the installation of any bespoke TRE application on the user's device.
    In practice a web browser is the most common way to achieve this.
  - Recommended
* - 2.1.5.
  - Your TRE must provide clear guidance on how to use software tools and work with data in the TRE.
  - TREs that provide a virtual desktop environment for {ref}`data consumers <project_roles>` to work in should provide documentation detailing the available tools.
    TREs where the analysis code is developed on the access machine (as oppose to within the TRE) should provide documentation detailing the mechanism by which code is submitted to the TRE.
  - Mandatory
* - 2.1.6.
  - Your TRE should, where possible, automatically apply security related updates for user software.
  - Reducing the risk of exploitable vulnerabilities in installed software will increase the security of your TRE.
  - Recommended
* - 2.1.7.
  - Your TRE could provide shared services that are accessible to users in the same project.
  - This may include shared file storage, databases, collaborative writing, and other web applications.
    This must only be shared amongst users within the same project.
  - Optional
* - 2.1.8
  - Your TRE must ensure that any shared services are only available to users working on the same project.
  - Poorly designed shared services could enable the unintended mixing of data between projects.
  To prevent this it is necessary that each instance is only shared between users of a single project.
  - Mandatory
* - 2.1.9.
  - You must mitigate and record any risks introduced by the use in your TRE of software that requires telemetry to function.
  - For example, some licenced commercial software must contact an external licensing server at start-up.
    You must be confident that only licensing information is sent to this server and that any network connections are secure.
  - Mandatory
* - 2.1.10.
  - Your TRE must provide software applications that are required by the {ref}`data consumers <project_roles>` working in the TRE.
  - The tools provided will depend on the types of data in the TRE, and the expectations of users of the TRE.
    For users working in a TRE via a virtual desktop, this may include programming languages such as Python and R, integrated development environments, Jupyter notebooks, office type applications such as word processors and spreadsheets, command line tools, etc.
    TREs with non-desktop interfaces should similarly consider carefully which applications are best suited for the {ref}`data consumers <project_roles>` needs when interacting with the data, for example "point and click" GUI tools for querying a database and generating plots of data.
    The set of tools should be reviewed regularly to ensure they are up to date.
  - Mandatory
```

### Code Version Control System

This {term}`application component <application component>` is the systems and tools providing version control and collaboration features for code developed inside the TRE.

```{list-table}
:header-rows: 1
:name: tab-computing-code-vcs

* -
  - Statement
  - Guidance
  - Importance
* - 2.1.11.
  - Your TRE should provide tools to encourage best-practice in reproducibly analysing data.
  - Reproducibility of analyses improves auditability and accountability of how data has been used, as well as being best-practice in research.
    This may include version control software, and tools for developing and running data analysis pipelines.
  - Recommended
```

### Artefact Management Application

This {term}`application component <application component>` is a service that manages and organises third-party software artefacts such as packaged code libraries or containers.

```{list-table}
:header-rows: 1
:name: tab-computing-artefact-management

* -
  - Statement
  - Guidance
  - Importance
* - 2.1.12.
  - Your TRE could provide access to some public software repositories or container registries.
  - For example, a TRE may allow direct installation of packages from Python or R repositories, or provide an internal mirror.
  - Optional
* - 2.1.13.
  - Your TRE could tightly control which packages are available.
  - For example, a TRE may only allow installation of a pre-defined set of approved packages.
    You might also choose to scan for malicious packages and/or go through an approval process before allowing code into the technical environment.
  - Optional
```

(advanced_CCC)=

### Advanced Computing Systems

This {term}`application component <application component>` involves the use of advanced, powerful computer resources to solve complex problems and process large amounts of data, possibly using specialised hardware.

```{list-table}
:header-rows: 1
:name: tab-computing-advanced-computing-systems

* -
  - Statement
  - Guidance
  - Importance
* - 2.1.14.
  - Your TRE must maintain segregation of users and data from different projects when using non-standard compute.
  - High performance or specialist compute is often shared amongst multiple users.
    Users and data must remain segregated at all times.
    For example, when using physical compute resources, all sensitive data could be securely wiped before another user is given access to that same node.
    In a cloud hosted TRE virtual machines could be destroyed and recreated.
  - Mandatory
* - 2.1.15.
  - Your TRE should be able to provide access to high performance computing or other scalable compute resource if required by users.
  - If a TRE supports users conducting computationally intensive research it should provide access to dynamically scalable compute or the equivalent.
    For example this may be in the form of a batch scheduler on a HPC cluster, or a dynamically created compute nodes on a cloud platform.
  - Recommended
* - 2.1.16.
  - Your TRE should be able to provide access to accelerators such as GPUs if required by users.
  - GPUs and other accelerators are commonly used in machine learning and other computationally intensive research.
    TREs should make it clear to users whether GPUs and other resources are available whilst projects are being assessed.
  - Recommended
* - 2.1.17.
  - Your TRE could make data available to {ref}`data consumers <project_roles>` using common database systems such as PostgreSQL, MSSQL or MongoDB.
  - Databases must be secured and only accessible to users within the same project.
    If shared (multi-tenant) database servers are used, {ref}`database administrators <data_roles>` must ensure that the database server enforces segregation of users and databases belonging to different projects.
  - Optional
* - 2.1.18.
  - Your TRE could integrate with large-scale data analytics tools for working with large datasets.
  - For example, Spark and Hadoop can be used for distributed computing across a cluster.
    This may be an advantage where a TRE is using an amount of data that is too large for single-machine computing to be practical.
  - Optional
```

## Infrastructure management

The ability of the {ref}`TRE Builder <infrastructure_roles>` to deploy, change or remove physical or virtual infrastructure.

(infrastructure_deployment_process)=

### Infrastructure Deployment Process

This {term}`business process <business process>` involves setting up and configuring infrastructure components and resources to support applications or services.
This requires development, installation, configuration, and validation.

```{list-table}
:header-rows: 1
:name: tab-computing-infrastructure-deployment

* -
  - Statement
  - Guidance
  - Importance
* - 2.2.1.
  - You must have a documented procedure for deploying infrastructure.
  - This might, for instance, be a handbook that is followed or a set of automated scripts.
  - Mandatory
* - 2.2.2.
  - You should, where possible, automate any repeatable aspects of your deployment.
  - This might involve using infrastructure-as-code tools or a series of scripts.
  - Recommended
* - 2.2.3.
  - You must have a documented procedure for making changes to deployed infrastructure.
  - This refers both to changes that might be expected in the course of normal operation and emergency changes that might be needed.
    Your change management process may form part of a wider accreditation such as ISO 27001.
  - Mandatory
* - 2.2.4.
  - You must test changes before they are used in production.
  - This might involve a separate development environment or another system for testing.
  - Mandatory
* - 2.2.5.
  - You should have a development environment that mirrors your production environment which you use to test infrastructure changes before committing them to production.
  - If possible, you should automate application of changes between development and production environments.
    Consider the costs and practicality of whether this will work for your situation.
  - Recommended
```

### Infrastructure Removal Process

This {term}`business process <business process>` involves retiring or removing infrastructure assets that are no longer needed or outdated, ensuring proper data handling and disposal.

```{list-table}
:header-rows: 1
:name: tab-computing-infrastructure-removal

* -
  - Statement
  - Guidance
  - Importance
* - 2.2.6.
  - You must have a documented procedure for removing infrastructure when it is no longer needed.
  - Removing unused infrastructure not only reduces costs and management burden but also reduces the attack surface of a TRE and reduces the risk of unaddressed vulnerabilities.
  - Mandatory
```

### Availability Management Process

This {term}`business process <business process>` involves ensuring all IT infrastructure meets the agreed levels of availability.

```{list-table}
:header-rows: 1
:name: tab-computing-infrastructure-availability-management

* -
  - Statement
  - Guidance
  - Importance
* - 2.2.7.
  - You should understand the availability and uptime guarantees of any providers that you rely on.
  - For remote TREs this might include your cloud provider(s) and/or data centre operators.
    For on-premises TREs, it might be worth using an uninterruptable power supply (UPS) and planning how you would deal with internet outages.
  - Recommended
* - 2.2.8.
  - You should develop an availability target or statement and share this with your users.
  - Understanding how and when the TRE might be unavailable will help your projects in planning their work.
  - Recommended
```

### Network Management Application

This {term}`application component <application component>` is an application used to manage network infrastructure, ensuring proper functioning, security, and performance.

```{list-table}
:header-rows: 1
:name: tab-computing-infrastructure-network-management

* -
  - Statement
  - Guidance
  - Importance
* - 2.2.9.
  - Your TRE must control and manage all of its network infrastructure in order to protect information in systems and applications.
  - Network infrastructure must prevent unauthorised access to resources on the network.
    This may include firewalls, network segmentation, and restricting connections to the network.
  - Mandatory
* - 2.2.10.
  - Your TRE must not allow connectivity between users in different projects, or with access to different datasets.
  - Connectivity between users in the same project may be allowed, for example to support shared network services within the project.
  - Mandatory
* - 2.2.11.
  - Your TRE must block outbound connections to the internet by default.
  - Limited outbound connectivity may be allowed for some services.
  - Mandatory
* - 2.2.12.
  - You should be able to monitor the network configuration of your TRE to check for misconfigurations and vulnerabilities.
  - This may include regular vulnerability scanning, and penetration testing.
  - Recommended
* - 2.2.13.
  - You should regularly monitor the network configuration of your TRE to check for misconfigurations and vulnerabilities.
  - This will involve following the monitoring procedure detailed above.
  - Recommended
```

### Infrastructure analytics application

This {term}`application component <application component>` is an application which enables the {ref}`TRE operator <infrastructure_roles>` to record and analyse data about the usage of the TRE.

```{list-table}
:header-rows: 1
:name: tab-computing-infrastructure-analytics

* -
  - Statement
  - Guidance
  - Importance
* - 2.2.14.
  - Your TRE must record usage data.
  - This may include the number of users, number of projects, the amount of data stored, number of datasets, the number of workspaces, etc.
  - Mandatory
* - 2.2.15.
  - Your TRE should record which datasets are accessed, when and by who.
  - This helps maintain auditability of how sensitive data has been used.
  - Recommended
* - 2.2.16.
  - Your TRE should record computational resource usage at the user or aggregate level.
  - This is useful for optimising allocation of resources, and managing costs.
  - Recommended
```

## Capacity management

The ability of the {ref}`TRE operator <infrastructure_roles>` to ensure the right amount of resources are available at the right time to provide a cost-effective service.

### Capacity Planning Process

This {term}`business process <business process>` involves forecasting and determining the resources required to meet the demands of an application or system, ensuring that adequate resources are available when needed.

```{list-table}
:header-rows: 1
:name: tab-computing-capacity-planning

* -
  - Statement
  - Guidance
  - Importance
* - 2.3.1.
  - You must ensure that all project members understand what resources are available and what the associated costs will be before the project starts.
  - For on-premises systems this might be related to the available hardware, for cloud-based systems there might be limits on how many instances of a particular resource (_e.g._ GPUs) can be used.
    Projects should use this information to understand whether the available resources will be sufficient for their requirements.
  - Mandatory
* - 2.3.2.
  - You should ensure that the anticipated needs of projects can be satisfied using available resources.
  - Note that this does not require you to accept requests for additional resources, but rather that promises made about resource availability before a project starts should be honoured wherever possible.
  - Recommended
* - 2.3.3.
  - You must have a procedure for allocating available resources among projects.
  - For cloud-based TREs this may involve scaling resources, such as virtual machines or databases, or deploying additional resources.
    For on-premises TREs this may involve a procurement process to ensure that necessary resources are available.
    Not all requests for capacity increase must necessarily be granted, but having a clear process will help projects understand when/why/how they can make use of additional capacity.
  - Mandatory
```

### Billing Process

This {term}`business process <business process>` involves generating and managing invoices and bills for projects within the TRE.
It involves calculation, issuance, and recording of payments and receipts.

```{list-table}
:header-rows: 1
:name: tab-computing-billing

* -
  - Statement
  - Guidance
  - Importance
* - 2.3.4.
  - You must ensure that the anticipated resource requirements will not result in overspending by the TRE.
  - For cloud-based TREs this may involve budgeting and/or restricting resource consumption on a project-by-project basis.
    For on-premises TREs this may involve managing expectations to match the available resource.
  - Mandatory
```

## Configuration management

### Configuration Management Process

This {term}`business process <business process>` involves the {ref}`TRE operator <infrastructure_roles>` identifying, maintaining, and verifying information on IT assets and configurations in the TRE organisation.

```{list-table}
:header-rows: 1
:name: tab-computing-configuration-management

* -
  - Statement
  - Guidance
  - Importance
* - 2.4.1.
  - You must have a documented procedure for configuring infrastructure.
  - This might, for instance, be a handbook that is followed or a set of automated scripts.
  - Mandatory
* - 2.4.2.
  - You should use configuration management tools to automate application of your configuration wherever possible.
  - This might involve configuration-as-code tools such as Ansible, Chef, Puppet or Windows Desired State Configuration or simply automated scripts.
  - Recommended
* - 2.4.3.
  - You should be able to verify whether the configuration is valid.
  - This might, for instance, involve running your configuration management tool in 'check' mode.
  - Recommended
* - 2.4.4.
  - You should regularly verify your TRE configuration.
  - This will limit the amount of time the TRE can spend in a non-compliant state.
  - Recommended
* - 2.4.5.
  - You must be able to replace a non-compliant TRE with a compliant system.
  - This might involve reconfiguring a running system or by replacing it with a compliant one.
  - Mandatory
```

## Information security

What the {ref}`organisation <infrastructure_roles>` does to safeguard research to ensure the confidentiality, integrity and availability of research resources and data.

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

### Vulnerability Management: Resilience Processes

A set of processes which ensures the TRE infrastructure can withstand disruption from incidents that risk confidentiality, integrity or availability of data.

```{list-table}
:header-rows: 1
:name: tab-computing-vulnerability-resilience

* -
  - Statement
  - Guidance
  - Importance
* - 2.5.1.
  - You should keep backups of data and research environments, provided that this is permitted by law.
  - Keeping backups could help reduce the impact of events like accidental deletion and data corruption on work in a TRE.
    {ref}`TRE developers <infrastructure_roles>` may want to consider how different elements such as sensitive input data or users' workspaces may be backed up, and whether they should be.
  - Recommended
* - 2.5.2.
  - You should build redundancy into infrastructure and storage.
  - Infrastructure should be as resilient as necessary to interruption.
    This could include redundant infrastructure in different physical locations, load balancing and replication of data between multiple storage locations.
  - Recommended
* - 2.5.3.
  - You should keep backups of infrastructure, applications and configurations.
  - This may include virtualised infrastructure snapshots which can restored as needed to recover from failure.
  - Recommended
```

### Vulnerability Management: Response Process

A process which ensures the organisation can quickly deal with incidents that risk confidentiality, integrity or availability of data.

```{list-table}
:header-rows: 1
:name: tab-computing-vulnerability-response

* -
  - Statement
  - Guidance
  - Importance
* - 2.5.4.
  - You must have procedures in place for rapid incident response.
  - There may be legal requirements to disclose details of any incidents, such as data breaches for organisations subject to GDPR.
    Having robust processes in place will ensure a swift and effective response when an incident occurs.
  - Mandatory
* - 2.5.5.
  - You should test your incident response through simulation.
  - During simulated incidents the TRE organisation can measure their effectiveness.
    This may involve people across the broader enterprise and/or external suppliers.
  -	Recommended

```

### Vulnerability Scanning

The automated process of scanning computer systems or networks to identify and assess potential security vulnerabilities.

```{list-table}
:header-rows: 1
:name: tab-computing-vulnerability-scanning

* -
  - Statement
  - Guidance
  - Importance
* - 2.5.6.
  - You should have an application in place to scan for vulnerabilities across infrastructure.
  - Software used to identify vulnerabilities should also report and alert.
    Such an alert should be triaged, risk assessed and treated accordingly.
  -	Recommended

```

### Security Patching

The process of applying updates or patches to software and systems to address known security vulnerabilities and flaws.

```{list-table}
:header-rows: 1
:name: tab-computing-vulnerability-patching

* -
  - Statement
  - Guidance
  - Importance
* - 2.5.7.
  - You must have a process in place for applying security updates to all software that forms part of the TRE infrastructure.
  - This includes any software used for remote desktop portals, databases, webapps, creating and destroying compute infrastructure, configuration management, or software used for monitoring the TRE.
  - Mandatory
* - 2.5.8.
  - Infrastructure should be automatically patched for vulnerabilities.
  -	Planning will be required across infrastructure and software systems to ensure security patches remain available from suppliers.
    Many systems may be isolated from the internet making TRE infrastructure more difficult to automatically patch.
  - Recommended
```

(security-testing)=

### Security testing

Security testing enables the {ref}`TRE operator <infrastructure_roles>` to gain assurance in the security of a TRE by testing or attempting to breach some or all of that system's security.

```{list-table}
:header-rows: 1
:name: tab-computing-security-testing

* -
  - Statement
  - Guidance
  - Importance
* - 2.5.9.
  - You should carry out penetration tests on your TRE.
  - By intentionally attempting to breach their TRE, organisations can proactively discover unnoticed vulnerabilities before they are exploited maliciously.
    Tests can evaluate the effectiveness of security controls in preventing data breaches, unauthorised access, or other security incidents.
  - Recommended
* - 2.5.10.
  - You should update the security controls of your TRE based on the results of security tests.
  - Security testing can reveal bugs and discrepancies in the TRE architecture which should be addressed in advance of sensitive data being uploaded, or with urgency in the case of an operational TRE.
    Regular testing will allow organisations to refine their TRE security controls and incident response capabilities.
    It enables them to adapt to any new security concerns that may arise as a result of changes in the underlying software.
  - Recommended
* - 2.5.11.
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
:name: tab-computing-encryption

* -
  - Statement
  - Guidance
  - Importance
* - 2.5.12.
  - Your TRE must encrypt project and user data at rest.
  - This prevents unauthorised access to the data even if the storage media is compromised.
    This may involve encrypted filesystems or tools to encrypt and decrypt data on demand.
    The encryption keys may be managed by the {ref}`TRE operator <infrastructure_roles>` or by a trusted external actor, for example a cloud provider.
  - Mandatory
* - 2.5.13.
  - Your TRE must encrypt data when in transit between the TRE and external networks or computers.
  - Data encryption must be used to safeguard against interception or tampering during transmission.
    This includes both data ingress and egress and users accessing the TRE, for example over a remote desktop or shell session.
  - Mandatory
* - 2.5.14.
  - Your TRE should encrypt data when in transit inside the TRE.
  - If possible, data transfers between different components of a TRE should also be encrypted.
  - Recommended
* - 2.5.15.
  - You should use encryption algorithms and software that are widely accepted as secure.
  - Encryption algorithms widely accepted as secure today may become insecure in the future, for instance due to newly-identified flaws, or advances in compute capabilities.
    The latest security patches and updates should be applied to any encryption software being used by the TRE.
    This helps address any known vulnerabilities or weaknesses in the encryption implementation.
  - Recommended
```

### Key Management Application

Software or tools dedicated to generating, storing, and managing encryption keys securely, ensuring their availability and protection.

```{list-table}
:header-rows: 1
:name: tab-computing-keymanagement

* -
  - Statement
  - Guidance
  - Importance
* - 2.5.16.
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
:name: tab-computing-physical-security

* -
  - Statement
  - Guidance
  - Importance
* - 2.5.17.
  - Your TRE could offer physical protection measures against data leakage or theft via physical means.
  - Restricting access to research facilities containing computers logged into TREs can help prevent malicious actors from viewing or stealing sensitive data, for example by photographing a computer screen.
    Physical controls on access to a TRE could include surveillance systems, restricting physical access to authorised personnel only, visitor management systems and employee training.
  - Optional
* - 2.5.18.
  - Your TRE may need to comply with specific regulatory requirements due to the types of data it is hosting.
  - Regulatory frameworks often emphasise the need for security controls to protect sensitive data.
    Compliance with these regulations could require organisations to implement specific security measures to safeguard their TRE from unauthorised access.
  - Mandatory
```
