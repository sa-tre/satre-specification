(pillar_computing_technology)=

# Computing technology

```{figure} ../../images/Capability_Map/full.drawio.svg
:alt: SATRE Pillars Capability Map
:align: center

SATRE Pillars Capability Map
```

This pillar concerns actions taken by the TRE operator to manage systems for storing, retrieving, analysing and sending information.

Each TRE operator will have its own computing technology requirements.
Requirements are drawn from information governance requirements which primarily specify the controls needed within the technical and computing infrastructure.
Researcher personas influence the according to the technical knowledge and experience of researchers along with the work they need to perform within the system, a data scientist will have very different requirements to a clinician for example.
The required compute resources will vary according to the scale of data and computational techniques employed during research.

<!-- See all pillars of the SATRE Pillars Capability Map here: {ref}`satre_pillars` -->

## End user computing

_The ability of the TRE operator to provide and manage devices, workspaces, interfaces and applications used by researchers to interact with underlying systems and data._

### End user computing interfaces

Software or system that allows people to interact with computers, applications, and services.
This application group includes desktop, command line and code submission interface.

```{list-table}
:header-rows: 1
:name: tab-end-user-computing-interfaces

* - Statement
  - Guidance
  - Importance

* - You should disable the ability to copy data out of your TRE via the system clipboard.
  - A TRE user must not be able to copy sensitive data out of a workspace using the system clipboard.
    A TRE may allow user to paste text into a workspace.
  - Recommended
* - Your TRE workspace should provide an environment familiar to your users.
  - This may take the form of a virtual Windows or Linux desktops, non-desktop interfaces such as JupyterLab and other web applications, or a terminal.
    Bespoke TRE-specific software should be avoided when widely used alternatives already exist.
  - Recommended
* - A TRE could restrict data access from researchers entirely and provide an interface for submitting code.
  - For example, you might use a system where users submit jobs that run over the data and return results without allowing direct data access.
  - Optional
```

### Software tools

The tools used by researchers inside a TRE, such as programming languages, IDEs and desktop applications.

```{list-table}
:header-rows: 1
:name: tab-end-user-software-tools

* - Statement
  - Guidance
  - Importance
* - Your TRE should be accessed via a user interface accessible using commonly available applications.
  - TREs which allow users to connect from their own devices should not require the installation of any bespoke TRE application on the user's device.
    In practice a web browser is the most common way to achieve this.
  - Recommended
* - Your TRE must provide clear guidance on how to use software tools and work with data in the TRE.
  - TREs that provide a virtual desktop environment for researchers to work in should provide documentation detailing the available tools.
    TREs where the analysis code is developed on the access machine (as opppose to within the TRE) should provide documentation detailing the mechanism by which code is submitted to the TRE.
  - Mandatory
* - Your TRE should, where possible, automatically apply security related updates for user software.
  - Reducing the risk of exploitable vulnerabilities in installed software will increase the security of your TRE.
  - Recommended
* - Your TRE could provide shared services that are accessible to users in the same project.
  - This may include shared file storage, databases, collaborative writing, and other web applications.
    This must only be shared amongst users within the same project.
  - Optional
* - Your TRE could include licenced commercial software if required by researchers, but additional risks must be recorded and mitigated where neccesary.
  - For example, if an application must connect to an external licensing server, you must be confident that only licensing information is sent to this server, and that any network connections are secure.
  - Optional
* - Your TRE must provide software applications that are relevant to working with the data in the TRE.
  - The tools provided will depend on the types of data in the TRE, and the expectations of users of the TRE.
    For users working in a TRE via a virtual desktop, this may include programming languages such as Python and R, integrated development environments, Jupyter notebooks, office type applications such as word processors and spreadsheets, command line tools, etc.
    TREs with non-desktop interfaces should similarly consider carefully which applications are best suited for the researchers needs when interacting with the data, for example "point and click" GUI tools for querying a database and generating plots of data.
    The set of tools should be reviewed regularly to ensure they are up to date.
  - Mandatory
```

### Code Version Control System

An application that provides version control and collaboration features for code developed inside the TRE.

```{list-table}
:header-rows: 1
:name: tab-end-user-code-vcs

* - Statement
  - Guidance
  - Importance
* - Your TRE should provide tools to encourage best-practice in reproducibly analysing data.
  - Reproducibility of analyses improves auditability and accountability of how data has been used, as well as being best-practice in research.
    This may include version control software, and tools for developing and running data analysis pipelines.
  - Recommended
```

### Artefact management

A service that manages and organizes software artefacts such as code libraries, dependencies, and build outputs in a centralised repository.

```{list-table}
:header-rows: 1
:name: tab-end-user-artefact-management

* - Statement
  - Guidance
  - Importance
* - Your TRE could provide limited access to some public software repositories or container registries.
  - For example, a TRE may allow installation of packages from Python or R repositories, or provide an internal mirror with approved packages.
    Similarly a subset of public containers could be made available, or individual container images via an internal container registry.
  - Optional
* - You could choose to tightly control access to public repositories.
  - This might involve only allowing a limited selection of allowed repositories.
    You might also choose to scan for malicious packages and/or go through an approval process before allowing code into the technical environment.
  - Optional
```

### Advanced or cluster computing

Advanced, powerful computer resources to solve complex problems and process large amounts of data, possibly using specialised hardware.

```{list-table}
:header-rows: 1
:name: tab-end-user-advanced-cluster-computing

* - Statement
  - Guidance
  - Importance
* - Your TRE should be able to provide access to high performance computing or other scaleable compute resource if required by users.
  - If a TRE supports users conducting computationally intensive research it should provide access to dynamically scaleable compute or the equivalent.
    For example this may be in the form of a batch scheduler on a HPC cluster, or a dynamically created compute nodes on a cloud platform.
  - Recommended
* - Your TRE could make data available to researchers using common database systems such as PostgreSQL, MSSQL or MongoDB.
  - Databases must be secured and only accessible to users within the same project.
    If shared (multi-tenant) database servers are used, database administrators must ensure that the database server enforces segregation of users and databases belonging to different projects.
  - Optional
* - Your TRE should be able to provide access to accelerators such as GPUs if required by users.
  - GPUs and other accelerators are commonly used in machine learning and other computationally intensive research.
    TREs should make it clear to users whether GPUs and other resources are available whilst projects are being assessed.
  - Recommended
* - Your TRE must maintain segregation of users and data from different projects when using non-standard compute.
  - High performance or specialist compute is often shared amongst multiple users.
    Users and data must remain segregated at all times.
    For example, when using physical compute resources, all sensitive data could be securely wiped before another user is given access to that same node.
    In a cloud hosted TRE virtual machines could be destroyed and recreated.
  - Mandatory
* - Your TRE could integrate with large-scale data analytics tools for working with large datasets.
  - For example, Spark and Hadoop can be used for distributed computing across a cluster.
    This may be an advantage where a TRE is using an amount of data that is too large for single-machine computing to be practical.
  - Optional
```

## Infrastructure management

The ability of the TRE operator to instantiate, deploy, change or remove physical or virtual infrastructure.

### Infrastructure deployment

The process of setting up and configuring infrastructure components and resources to support applications or services.
This involves development, installation, configuration, and validation.

```{list-table}
:header-rows: 1
:name: tab-infrastructure-deployment

* - Statement
  - Guidance
  - Importance
* - You must have a documented procedure for deploying infrastructure.
  - This might, for instance, be a handbook that is followed or a set of automated scripts.
  - Mandatory
* - You must have a documented procedure for making changes to deployed infrastructure.
  - This refers both to changes that might be expected in the course of normal operation and emergency changes that might be needed.
    Your change management process may form part of a wider accreditation such as ISO 27001.
  - Mandatory
* - You should, where possible, automate any repeatable aspects of your deployment.
  - This might involve using infrastructure-as-code tools or simply a series of scripts.
  - Recommended
* - You must test changes before they are used in production.
  - This might involve a separate development environment or another system for testing.
  - Mandatory
* - You should have separate technical environments for development and testing infrastructure changes before they are committed to production.
  - If possible, you should automate application of changes between development and production environments.
    Consider the costs and practicality of whether this will work for your situation.
  - Recommended
```

### Infrastructure decommissioning

The process of retiring or removing infrastructure assets that are no longer needed or outdated, ensuring proper data handling and disposal.

```{list-table}
:header-rows: 1
:name: tab-infrastructure-decommissioning

* - Statement
  - Guidance
  - Importance
* - You must have a documented procedure for removing infrastructure when it is no longer needed
  - Removing unused infrastructure not only reduces costs and management burden but also reduces the attack surface of a TRE and reduces the risk of unaddressed vulnerabilities.
  - Mandatory
```

### Availability management

The process of ensuring all IT infrastructure meets the agreed levels of availability.

```{list-table}
:header-rows: 1
:name: tab-infrastructure-availability

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

### Network management

An application used to manage and control network devices, ensuring proper functioning, security, and performance of the network.

```{list-table}
:header-rows: 1
:name: tab-infrastructure-network

* - Statement
  - Guidance
  - Importance
* - Your TRE must control and manage all of its network infrastructure in order to protect information in systems and applications.
  - Network infrastructure must prevent unauthorised access to resources on the network.
    This may include firewalls, network segmentation, and restricting connections to the network.
  - Mandatory
* - Your TRE must not allow connectivity between users in different projects, or with access to different datasets.
  - Connectivity between users in the same project may be allowed, for example to support shared network services within the project.
  - Mandatory
* - Your TRE must block outbound connections to the internet by default.
  - Limited outbound connectivity may be allowed for some services.
  - Mandatory
* - You must monitor the network configuration of your TRE to check for misconfigurations and vulnerabilities.
  - This may include regular vulnerability scanning, and penetration testing.
  - Mandatory
```

### Infrastructure analytics

The ability of the TRE operator to record and analyse data about the usage of the TRE.

```{list-table}
:header-rows: 1
:name: tab-end-user-infrastructure-analytics

* - Statement
  - Guidance
  - Importance
* - Your TRE must record usage data.
  - This may include the number of users, number of projects, the amount of data stored, number of datasets, the number of workspaces, etc.
  - Mandatory
* - Your TRE should record which datasets are accessed, when and by who.
  - This helps maintain auditability of how sensitive data has been used.
  - Recommended
* - Your TRE should record computational resource usage at the user or aggregate level.
  - This is useful for optimising allocation of resources, and managing costs.
  - Recommended
```

## Capacity management

### Capacity planning

The process of forecasting and determining the resources required to meet the demands of an application or system, ensuring that adequate resources are available when needed.

```{list-table}
:header-rows: 1
:name: tab-infrastructure-capacity

* - Statement
  - Guidance
  - Importance
* - You must ensure that all projects understand what resources are available and what the associated costs will be before the project starts.
  - For on-premises systems this might be related to the available hardware, for cloud-based systems there might be limits on how many instances of a particular resource (_e.g._ GPUs) can be used. Projects should use this information to understand whether the available resources will be sufficient for their requirements.
  - Mandatory
* - You should ensure that the anticipated needs of projects can be satisfied using available resources.
  - Note that this does not require you to accept requests for additional resources, but rather that promises made about resource availability before a project starts should be honoured wherever possible.
  - Recommended
* - You must have a procedure for increasing/decreasing available resources.
  - For cloud-based TREs this may involve scaling resources, such as virtual machines or databases, or deploying additional resources.
    For on-premises TREs this may involve a procurement process to ensure that necessary resources are available.
    Not all requests for capacity increase must necessarily be granted, but having a clear process will help projects understand when/why/how they can make use of additional capacity.
  - Mandatory
```

### Billing

The process of generating and managing invoices and bills for projects within the TRE.
It involves calculation, issuance, and recording of payments and receipts.

```{list-table}
:header-rows: 1
:name: tab-infrastructure-billing

* - Statement
  - Guidance
  - Importance
* - You must ensure that the anticipated resource requirements will not result in overspending by the TRE.
  - For cloud-based TREs this may involve budgeting and/or restricting resource consumption on a project-by-project basis.
    For on-premises TREs this may involve managing expectations to match the available resource.
  - Mandatory
```

### Configuration management

The ability of the TRE operator to identify, maintain, and verify information on IT assets and configurations in the TRE operator.

```{list-table}
:header-rows: 1
:name: tab-infrastructure-configuration

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
* - You should regularly verify your TRE configuration.
  - This will limit the amount of time the TRE can spend in a non-compliant state.
  - Recommended
* - You must be able to replace a non-compliant TRE with a compliant system.
  - This might involve reconfiguring a running system or by replacing it with a compliant one.
  - Mandatory
* - You must have a process in place for applying security updates to all software that forms part of the TRE infrastructure.
  - This includes any software used for remote desktop portals, databases, webapps, creating and destroying compute infrastructure, configuration management, or software used for monitoring the TRE.
  - Mandatory
* - You must also run regular anti-virus/malware scans on all TRE systems where infection could be a problem.
  - Virus and malware scans will help identify malicious code which may compromise the security, or correct operation, of the TRE.
  - Mandatory
```
