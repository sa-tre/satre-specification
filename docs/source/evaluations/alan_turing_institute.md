(evaluation_alan_turing_institute)=

# Alan Turing Institute Data Safe Haven

[The Alan Turing Institute](https://www.turing.ac.uk/) is the UK's national institute for data science and artificial intelligence.
The Data Safe Haven project's goal is to remove barriers to working safely and effectively with sensitive data, by promoting and demonstrating a culture of open, community-led development of interoperable foundational infrastructure and governance.
The project maintains an [open-source TRE project](https://github.com/alan-turing-institute/data-safe-haven) which covers governance, documentation and programmatic deployment of a TRE.
Data Safe Haven can be freely used and adapted to deploy a TRE to Microsoft Azure.

The Turing uses the Data Safe Haven TRE and governance to enable research on sensitive data.
This includes work with external partners and our [Data Study Group](https://www.turing.ac.uk/collaborate-turing/data-study-groups) collaborative hackathons.
The evaluation below has been carried out for the Turing's production TRE, using the Data Safe Haven technical implementation and [institutional governance processes](https://alan-turing-institute.github.io/trusted-research).

## Governance Requirements

```{list-table}
:header-rows: 1
:name: tab-turing-dsh-ig-governance-requirements

* -
  - Score
  - Response
* - 1.1.1.
  - 1
  - - We rely on the Alan Turing Institute legal and data protection teams to inform us of necessary legal requirements.
    - Our TRE (the Alan Turing Institute Data Safe Haven) is self-assessed against the NHS Data Security and Protection Toolkit.
    - The Institute has a centralised ethics approval procedure which all projects are required to follow.
    - Project specific requirements are discussed with {ref}`information asset owners <data_roles>` before start of each project.
    ##### Potential Improvements
    - Be more proactive about trying to stay up-to-date with changes to requirements.
    - Hold an annual review with the Turing Legal and Data Protection teams to ensure all current requirements are still met by the TRE organisation.
* - 1.1.2.
  - 1
  - - We have documented our institutional risk appetite and understand what kinds of work we are prepared to support.
    - All projects handled in the TRE have gone through our institutional Data Protection Assessment Process and Ethics Approval Process.
    - All projects are tracked through a ticketing system with relevant documents and agreements stored on Sharepoint.
    ##### Potential Improvements
    - Improve our document handling workflow by developing an Information Governance App through which all projects can be managed directly by approved users.
* - 1.1.3.
  - 1
  - - The Institute has Legal and Data Protection Teams who ensure that projects meet our institutional requirements.
    - Our sysadmin team is currently appropriately sized for the number of projects we are handling.
    - The Legal and Data Protection teams do not have staff dedicated to our TRE.
    - Our TRE organisation does not control staff numbers in the legal and data protection teams.
    ##### Potential Improvements
    - Ensure that staff time is explicitly allocated to TRE support.
* - **Capability met?**
  - **YES**
  -
```

## Quality Management

```{list-table}
:header-rows: 1
:name: tab-turing-dsh-ig-quality-management

* -
  - Score
  - Response
* - 1.2.1.
  - 1
  - - Our SOPs are held on a public website backed by a private GitHub repository with limited edit access.
    - Policies and other forms that need signatures as part of our SOPs are held in a private Sharepoint folder with limited access.
    - Acceptance of policies is recorded in a document held in a private Sharepoint folder.
    - We do not have an explicit process for determining who should have administrator access to these folders and repositories.
    ##### Potential Improvements
    - Develop an induction process and/or mandatory training programme for potential administrators.
* - 1.2.2.
  - 1
  - - All SOPs are stored in a version controlled repository.
    - Policies, forms and project documentation are stored in a controlled Sharepoint folder.
    - We do not currently use explicit versioning for forms/documents that need to be signed.
    ##### Potential Improvements
    - Use tags to refer to documents handled by git version control.
    - Use in-file versioning for files stored on Sharepoint.
* - 1.2.3.
  - 0
  - - We regularly discuss our information governance processes with impacted projects and look for ways to improve and streamline them.
    - We have SOPs for handling security incidents and running investigations.
    - We do not have a formal measurement process.
    - We do not regularly report our information governance performance to management.
    ##### Potential Improvements
    - Develop a formal information governance measurement and reporting process.
* - 1.2.4.
  - 1
  - - Our TRE deployment is self-assessed against the NHS Data Security and Protection Toolkit.
    - In principle, following our processes will ensure that we remain DSPT compliant.
    - However, we don't have a formal process to ensure we resubmit our self assessment each year and update our procedures if required.
    ##### Potential Improvements
    - Develop a process for maintaining compliance.
* - 1.2.5.
  - 2
  - - We do not formally audit our TRE organisation, however, there are no bodies with which we are required to share outcomes.
* - 1.2.6.
  - 2
  - - We have an enterprise agreement with Azure which includes data safety provisions.
    - We do not currently use contractors, but if we were to, any contractors would have contracts agreed with our legal team, and would not have access to our production system.
* - 1.2.7.
  - 2
  - - The Institute's legal team have reviewed and approved our enterprise agreement with Azure.
    - We do not use contractors.
* - 1.2.8.
  - 2
  - - No physical assets used as part of TRE infrastructure.
    - Chromebooks owned by the Institute are used to make secure connections to the TRE infrastructure, they do not hold any data.
    - These Chromebooks are tracked and maintained by IT team.
* - 1.2.9.
  - 1
  - - We have an SOP covering security incident reporting.
    - A report is written for each security incident and saved in a controlled Sharepoint folder.
    - Deviations that do not result in an incident report are not centrally tracked.
    - We do not do anything in particular to flag when an issue was due to a deviation from SOP.
    ##### Potential Improvements
    - Develop a centralised system for tracking and addressing process deviations.
* - 1.2.10.
  - 2
  - - Part of our security incident response is to initiate changes to our procedures to mitigate future incidents.
    - Reporting and discussing incidents is prompt and resolving the underlying issue prioritised.
* - 1.2.11.
  - 1
  - - Training records for TRE users are recorded in Sharepoint.
    - We track the configuration data needed to manage each TRE project on a GitHub issue.
    - This issue is also used to track of changes made throughout the lifecycle of a TRE project.
    - We do use feedback and our impressions of the effectiveness of the TRE to guide development and changes.
    ##### Potential Improvements
    - Actively monitor the quality of services provided to end-users.
* - 1.2.12.
  - 0
  - - We do not use any quality management software.
* - **Capability met?**
  - **YES**
  -
```

## Risk Management

```{list-table}
:header-rows: 1
:name: tab-turing-dsh-ig-risk-management

* -
  - Score
  - Response
* - 1.3.1.
  - 1
  - - We have a risk register which scores risks in a matrix based on their likelihood and potential consequences.
    ##### Potential Improvements
    - Regularly update our risk register.
* - 1.3.2.
  - 2
  - - All Turing projects must carry out a Data Protection Assessment Process.
    - We also have a flowchart that {ref}`project teams <project_roles>` and {ref}`information asset owners <data_roles>` must follow to agree on the security tier of their project before it starts.
* - 1.3.3.
  - 1
  - - We decide on risk mitigations during our risk assessment process, but this tends to be an _ad-hoc_ process rather than anything formalised..
    ##### Potential Improvements
    - Develop a formal risk mitigation process.
* - 1.3.4.
  - 1
  - - We have a documented set of roles together with responsibilities required for each role.
    - There is an implicit association of risks with particular roles, but we are not explicit about the relationship between risks and roles.
    ##### Potential Improvements
    - Create explicit mapping of risks to roles.
* - 1.3.5.
  - 1
  - - Our TRE deployment is guided by the risk appetite of the wider Institute.
    - We have not yet encountered risks that fall outside our known risk appetite.
    ##### Potential Improvements
    - Develop a procedure for handling opportunities outside our risk appetite
* - **Capability met?**
  - **YES**
  -
```

## Study Management

```{list-table}
:header-rows: 1
:name: tab-turing-dsh-ig-study-management

* -
  - Score
  - Response
* - 1.4.1.
  - 2
  - - All Turing projects must carry out a Data Protection Assessment Process.
    - All projects must have an agreed security tier before starting.
    - We inform projects in advance of their estimated directly incurred infrastructure costs and require them to confirm that they will be able to pay for these.
    - Data sharing agreements must be in place before any data ingress.
* - 1.4.2.
  - 1
  - - As soon as we are informed of the need to revoke user access, we will do so.
    - Lists of responsible persons are established at the beginning of each project and these are kept up-to-date.
    - We tend to reactively respond to user removal requests rather than actively confirming that users are active.
    ##### Potential Improvements
    - Develop a regular process for confirming that users are active.
* - 1.4.3.
  - 1
  - - Our updating process is passive, as we rely on our Data Protection and Legal teams to inform us of changes to relevant legislation.
    - We do not have formal checks in place.
    ##### Potential Improvements
    - Regularly check for changed requirements with Legal and Data Protection teams.
* - 1.4.4.
  - 2
  - - We have processes in place to handle egressing results, removing access, securely deleting any data and destroying the infrastructure.
    - Data egress needs to be agreed by the project stakeholders: the {ref}`project manager <project_roles>`, {ref}`information asset owner <data_roles>` and a referee representing the interests of the Institute.
* - 1.4.5.
  - 0
  - - We manage our projects using a GitHub project board.
    - We do not use an automated application.
    ##### Potential Improvements
    - Develop a system for tracking projects and datasets.
* - 1.4.6.
  - 1
  - - We keep records for each project on which datasets are being used and any conditions attached to that use.
    - We do not have a central database of data assets.
    ##### Potential Improvements
    - Develop a system for tracking projects and datasets.
* - 1.4.7.
  - 1
  - - We manage our projects using a GitHub project board.
    - Documents pertaining to each project are kept in a private Sharepoint folder.
    ##### Potential Improvements
    - Reduce manual steps in this process.
* - **Capability met?**
  - **YES**
  -
```

## Member Accreditation

```{list-table}
:header-rows: 1
:name: tab-turing-dsh-ig-member-accreditation

* -
  - Score
  - Response
* - 1.5.1.
  - 1
  - - Project managers are required to provide an email address and phone number for each user before we set up their account.
    - Their username is sent to their email address together with a link to a self-service password reset page.
    - Their password cannot be updated without providing a code that is sent to their registered phone number.
    ##### Potential Improvements
    - Consider making more detailed checks on user ID, possibly delegating to a trusted third-party.
* - 1.5.2.
  - 2
  - - Onboarding documentation exists for both {ref}`TRE operators <infrastructure_roles>` and {ref}`project teams <project_roles>`.
    - Users must complete appropriate training and sign our terms of use before being granted access to the TRE.
* - 1.5.3.
  - 2
  - - We use Microsoft Entra to manage user accounts.
    - Access to resources and data is controlled by RBAC.
* - 1.5.4.
  - 2
  - - We have a process for agreeing which people are able to take which actions involving sensitive data.
    - Delegation of approval authority is also included here.
    - A document summarising these decisions must be signed by the {ref}`project manager <project_roles>`, {ref}`information asset owner <data_roles>` and referee before the project begins.
* - 1.5.5.
  - 2
  - - Initial log in is delegated to Microsoft Entra via OAuth.
    - This requires username, password and MFA.
    - Log in to computing resources within the TRE is controlled by the same username and password, accessed via LDAP.
* - 1.5.6.
  - 1
  - - Each user has a unique username.
    - If a user works on multiple different projects, the same username will be used.
    - Mapping of usernames to named individuals are kept in Microsoft Entra.
    - Other user documentation such as training records is associated to their name (not their username).
    ##### Potential Improvements
    - Develop a more comprehensive system for user records tracking.
* - **Capability met?**
  - **YES**
  -
```

## Training Delivery and Management

```{list-table}
:header-rows: 1
:name: tab-turing-dsh-ig-training-delivery

* -
  - Score
  - Response
* - 1.6.1.
  - 1
  - - Part of the project initiation process involves agreeing on appropriate user training.
    - All TRE users carry out GDPR and cyber security training.
    - Depending on the project, they may also complete eLfH data security awareness training (level 1) and MRC Research, GDPR & Confidentiality Training
    - {ref}`TRE operators <infrastructure_roles>` must pass all user training requirements as well as data handling and cyber security training.
    ##### Potential Improvements
    - Put a regular systematic training needs analysis into place.
* - 1.6.2.
  - 1
  - - Turing employees have access to internal GDPR and Cyber Security courses.
    - For non-Turing users we rely on their host organisation having sufficient training in these areas.
    - The eLfH and MRC courses are available to all.
    ##### Potential Improvements
    - Develop data handling courses that will be available to all to close the current gap between Turing and non-Turing users.
* - 1.6.3.
  - 1
  - - We require all users and administrators to keep their training up-to-date.
    - All training certifications must be refreshed each year.
    ##### Potential Improvements
    - Implement a system that creates alerts for users/admins when training is needed.
* - 1.6.4.
  - 1
  - - We have a register of people, their training requirements and when they last completed training.
    - We require training to have been completed in the last year, if this is not done then user access will be revoked.
    - This is stored as a spreadsheet in a private Sharepoint folder.
    ##### Potential Improvements
    - Implement a system that creates alerts for users/admins when training is needed.
* - 1.6.5.
  - 2
  - - We trust certifications provided by Turing's university and commercial partners.
* - 1.6.6.
  - 1
  - - We currently use third-party training platforms.
    - Not all training is on the same platform.
    - There are plans to integrate training into a single platform.
    ##### Potential Improvements
    - Develop automated tracking of whether training is up-to-date.
* - 1.6.7.
  - 0
  - - We do not currently do this, but we have plans to do so in future.
    ##### Potential Improvements
    - Decide whether an LMS is useful and document the decision.
* - 1.6.8.
  - 0
  - - We use third-party training courses, whose format we have not analysed for transferability and standardisation.
    ##### Potential Improvements
    - Find out whether existing modules are in transferable formats.
* - 1.6.9.
  - 0
  - - We do not control the course content and are unable to maintain copies of the course materials.
    - We have not explored whether this information is available from our training providers.
    ##### Potential Improvements
    - Find out whether historical course content can be accessed.
* - **Capability met?**
  - **YES**
  -
```

## End user computing interfaces

```{list-table}
:header-rows: 1
:name: tab-turing-dsh-computing-end-user-interfaces

* -
  - Score
  - Response
* - 2.1.1.
  - 2
  - We do not allow data to move between the system clipboard and workspace in any instance.
* - 2.1.2.
  - 2
  - We provide both virtual desktop and command line interfaces to Linux virtual machines.
    Self-hosted web applications focused on collaborative work are accessible within the environment.
* - 2.1.3.
  - 2
  - We do not provide a job-submission interface, all users have direct access to the data they are working with.
* - **Capability met?**
  - **YES**
  -
```

## End user software tools

```{list-table}
:header-rows: 1
:name: tab-turing-dsh--computing-end-user-software-tools

* -
  - Score
  - Response
* - 2.1.4.
  - 2
  - We use a virtual Linux desktop, accessible via a web browser.
    We use standard, open-source tools, like Apache Guacamole, to support this.
* - 2.1.5.
  - 1
  - - We have a user guide that explains how to use the installed software, as well as how to configure your user account.
    ##### Potential Improvements
    - We intend to iterate on the design of the user guide to make it easier to navigate, follow and understand - and separate it entirely from developer docs.
* - 2.1.6.
  - 2
  - We use the Azure platform-level automation tools to run weekly software updates on all virtual machines that make up the TRE.
    Any update failures are flagged by the automation software.
* - 2.1.7.
  - 2
  - Within each project environment we have a range of shared services.
    These include shared folders, user services such as GitLab, for collaborating on code, CodiMD, for collaborating on document writing and several database systems.
* - 2.1.8.
  - 2
  - These shared services are only available to users working within the same environment.
* - 2.1.9.
  - 2
  - User-facing software and tools are all open source.
    We do not allow any software to contact external licensing servers.
* - 2.1.10.
  - 2
  - We provide a wide range of tools and applications for data science, influenced by the needs of users.
    Our users are typically data scientists working with data directly.
    This data can only be accessed from inside the TRE, either via a database or a shared folder.
* - **Capability met?**
  - **YES**
  -
```

## Code Version Control System

```{list-table}
:header-rows: 1
:name: tab-turing-dsh-computing-code-vcs

* -
  - Score
  - Response
* - 2.1.11.
  - 1
  - - Version control tools are provided to users, including an internal GitLab instance.
    - Users are encouraged to version control their code and we provide training for those who are unfamiliar with git.
    ##### Potential Improvements
    - We do not provide specific tools to aid or encourage reproducibility or creating data analysis pipelines.
    - We do not support CI pipelines on our GitLab server.
    - We do not have a method to ensure that work done inside the environment can be reproduced outside such as containerisation.
* - **Capability met?**
  - **YES**
  -
```

## Artefact Management Application

```{list-table}
:header-rows: 1
:name: tab-turing-dsh-computing-artefact-management

* -
  - Score
  - Response
* - 2.1.12.
  - 2
  - We provide proxied access to external software repositories, currently PyPI and CRAN, using Sonatype Nexus.
    For our highest sensitivity projects we instead provide a local mirror.
    In either case, we can support either access to every package in the remote repository or a pre-specified allowed list of approved packages.
* - 2.1.13.
  - 2
  - - For higher sensitivity environments, we restrict access to a pre-specified allowed list.
      These allowed lists are configurable on a per-project basis and, by default, include a minimal set of well-used and useful packages plus their dependencies.
* - **Capability met?**
  - **YES**
  -
```

## Advanced Computing Systems

```{list-table}
:header-rows: 1
:name: tab-turing-dsh-computing-advanced-computing-systems

* -
  - Score
  - Response
* - 2.1.14.
  - 2
  - Non-standard resources are segregated in the same way as standard resources.
    We do not share any resources between projects.
* - 2.1.15.
  - 2
  - We are able to deploy high capacity virtual machines if required.
    These can have many cores and/or large amounts of RAM.
* - 2.1.16.
  - 2
  - We are able to deploy VM sizes featuring GPUs within the limits of what is available on Azure and compatible with our pre-built x64 image.
* - 2.1.17.
  - 2
  - We make Microsoft SQL server and/or PostgreSQL servers available to projects as needed.
    These databases are only accessible from inside a single project environment.
* - 2.1.18.
  - 1
  - We do not currently support large-scale data analytics tools.
    ##### Potential Improvements
    - We would consider supporting Spark but it has not been requested by users.
* - **Capability met?**
  - **YES**
  -
```

## Infrastructure Deployment Process

```{list-table}
:header-rows: 1
:name: tab-turing-dsh-computing-infrastructure-deployment

* -
  - Score
  - Response
* - 2.2.1.
  - 2
  - We have a detailed deployment guide which system managers follow to deploy a TRE instance.
* - 2.2.2.
  - 1
  - - We use reproducible Powershell scripts that are stored in GitHub to handle our deployments.
    - This code is regularly tested and new versions released.
    ##### Potential Improvements
    - We do not currently use third-party infrastructure-as-code tools but we are in the process of moving to them.
* - 2.2.3.
  - 1
  - - We have documented procedures to add/remove users and to resize, add or remove infrastructure components such as GPU-enabled machines.
    - We do not make ad-hoc or unusual changes to deployed infrastructure in the course of normal operation.
    - In emergencies, we would deploy a fix that had been tested in development and then hold an incident report meeting.
    ##### Potential Improvements
    - We do not currently have a formal process for making emergency changes to our production system.
* - 2.2.4.
  - 1
  - - We use separate development environments to test changes before they make it into a release.
    - Emergency fixes to our production environments are also tested on development environments before being deployed.
    - Production environments are created from known, tested releases of the codebase.
    ##### Potential Improvements
    - We do not currently have a formal process for making emergency changes to our production system.
* - 2.2.5.
  - 1
  - - We do have separate development environments, but these are not permanent clones of our production environment.
    - We do not automate promotion of development environments to production.
    ##### Potential Improvements
    - We would consider moving to a blue/green deployment environment as long as this is possible from a cost perspective.
* - **Capability met?**
  - **YES**
  -
```

## Infrastructure Removal Process

```{list-table}
:header-rows: 1
:name: tab-turing-dsh-computing-infrastructure-removal

* -
  - Score
  - Response
* - 2.2.6.
  - 2
  - We use Powershell scripts to automate the removal of unused infrastructure.
    We have documented procedures that detail when this should be done.
* - **Capability met?**
  - **YES**
  -
```

## Availability Management Process

```{list-table}
:header-rows: 1
:name: tab-turing-dsh-computing-infrastructure-availability-management

* -
  - Score
  - Response
* - 2.2.7.
  - 2
  - Azure publishes availability and uptime guarantees for relevant services.
    We have chosen replication levels which balance high availability while keeping data within a single region.
* - 2.2.8.
  - 0
  - We do not have an availability target.
    We do not make any availability guarantees to our users.
* - **Capability met?**
  - **YES**
  -
```

## Network Management Application

```{list-table}
:header-rows: 1
:name: tab-turing-dsh-computing-infrastructure-network-management

* -
  - Score
  - Response
* - 2.2.9.
  - 2
  - We use Azure network security groups and firewalls to control network traffic between different parts of the TRE.
    Only the minimum necessary categories of traffic are permitted.
    The TRE gateway only permits connections from pre-approved IP addresses.
* - 2.2.10.
  - 2
  - Different projects are isolated at the virtual network level.
    Data sets belong to a single project only and are stored in storage accounts which only that project can access.
    Normal users have no way to directly connect to other project environments even if they have valid accounts for them.
* - 2.2.11.
  - 2
  - We block outbound connections to the internet unless these are required for functionality, such as system updates.
    All outbound connections are monitored by the Azure firewall.
* - 2.2.12.
  - 0
  - We do not actively monitor our TRE for misconfiguration.
    Unexpected connections would show up in our firewall logs.
    ##### Potential Improvements
    - We are interested in hearing how other community members approach this.
* - 2.2.13.
  - 0
  - We do not actively monitor our TRE for misconfiguration.
    ##### Potential Improvements
    - We are interested in hearing how other community members approach this.
* - **Capability met?**
  - **YES**
  -
```

## Infrastructure analytics application

```{list-table}
:header-rows: 1
:name: tab-turing-dsh-computing-infrastructure-analytics

* -
  - Score
  - Response
* - 2.2.14.
  - 1
  - We keep track of users in Microsoft Entra, projects on a GitHub project board, datasets associated with each project in Sharepoint and workspaces associated with each project on GitHub issues.
    ##### Potential Improvements
    - This data is not currently stored in one place, and the processes for tracking data are not clearly defined.
* - 2.2.15.
  - 1
  - Each dataset is associated with a single project.
    Only users associated with that project are able to access it.
    We do not keep track of instances of individual users accessing particular datasets.
    ##### Potential Improvements
    - We cannot think think of a better way to do this now, but are interested in exploring options with the community.
* - 2.2.16.
  - 2
  - We record computational resource usage at the project level.
    We have no way to break down usage at the per-user level and do not think this would be useful for us since costs are managed at the project level.
* - **Capability met?**
  - **YES**
  -
```

## Capacity Planning Process

```{list-table}
:header-rows: 1
:name: tab-turing-dsh-computing-capacity-planning

* -
  - Score
  - Response
* - 2.3.1.
  - 2
  - At the planning stage, we make projects aware of possible resources, and associated costs.
    This information includes common configurations and requirements (such as GPUs), possible additional resources, and their costs.
    The costs of the shared aspects of the TRE and the TRE service (support, admin time) are also explained and broken down on a per-project basis.
* - 2.3.2.
  - 1
  - For our projects, we rely on the Azure availability guarantees about compute resources.
    We have limited control over the availability of Azure resources and sometimes there may not be available capacity.
* - 2.3.3.
  - 1
  - Our TRE is deployed on the Azure cloud.
    The availability of resources is therefore determined by the capacity of the cloud provider.
    Deciding on the distribution of resources between projects is not a large concern as the availability of resources, generally, greatly exceeds our need.
    ##### Potential Improvements
    - Allocating resources to projects is currently done on an ad-hoc basis depending on project needs.
      We would like to make this process more formal and better documented.
* - **Capability met?**
  - **YES**
  -
```

## Billing Process

```{list-table}
:header-rows: 1
:name: tab-turing-dsh-computing-billing

* -
  - Score
  - Response
* - 2.3.4.
  - 2
  - We provide projects with estimates of their spend which are dependent on their requirements.
    We track spending on a per-project basis and allow the project manager to monitor spending.
    Spending alerts are sent out when spending reaches set thresholds: 50%, 90%, 100% of the pre-agreed limit.
    Overspend is possible but the additional spending must still be recovered from the project.
    ##### Potential Improvements
    - We should be clearer about the consequences of overspending.
* - **Capability met?**
  - **YES**
  -
```

## Configuration management

```{list-table}
:header-rows: 1
:name: tab-turing-dsh-computing-configuration-management

* -
  - Score
  - Response
* - 2.4.1.
  - 1
  - We have a detailed deployment guide which system managers follow to deploy and configure a TRE instance.
    We have a limited set of documentation covering making common configuration changes after a TRE has been deployed.
* - 2.4.2.
  - 0
  - We do not use configuration management tools.
    We have a limited set of scripts to make some common configuration changes.
    Some changes involve manual steps which may be documented.
* - 2.4.3.
  - 0
  - There is no general, automated way to check the configuration of our TRE.
    A manual check would be time consuming and no process for doing so has been established.
    Security package update compliance for Ubuntu and Windows virtual machines can be confirmed.
* - 2.4.4.
  - 0
  - We are unable to verify configuration and so do not regularly check for compliance.
* - 2.4.5.
  - 1
  - We can replace non-compliant instances and/or components using out deployment processes and scripts.
    We are able to do this in a manner which avoids data loss.
    However, it will generally involve destruction and redeployment of infrastructure.
* - **Capability met?**
  - **YES**
  -
```

## Information security

```{list-table}
:header-rows: 1
:name: tab-turing-dsh-information-security

* -
  - Score
  - Response

* - 2.5.1.
  - 1
  - Some research environment data is backed up.
    This includes virtual disks and object storage accounts which contain users personal/configuration files and working data.
    Backups are distributed across data centres within a single region.
    Input data is only kept as a single, immutable copy which is not backed up (although users may make copies which would be).
    Because input data is always a copy, we are not concerned about the loss of input data.
    #### Potential improvement
    - We could ensure that non-file working data, such as database contents are also backed up.
* - 2.5.2.
  - 2
  - We use Microsoft Azure's features for geo-redundant storage for data, which can handle load balancing and replication of data between multiple storage locations.
  For TRE computng infrastructure, components are replicable via infrastructure as code.
* - 2.5.3.
  - 2
  - Infrastructure is defined by configuration files and replicable via infrastructure as code.
* - 2.5.4
  - 2
  - Our terms-of-use require users to report any potential data incident.
    We have a process in place for managing data incidents, whether raised by users or discovered independently, that ensures we meet our legal requirements and also implement any necessary changes, such as disabling access to a TRE if necessary.
* - 2.5.5.
  - 0
  - Although we have have a process for incidents, we don't have a incident response simulation process.
* - 2.5.6.
  - 0
  - Azure handles update automation, but not vulnerability scanning specifically.
* - 2.5.7.
  - 1
  - - Many cloud services, for example virtual networks, are kept up to date by the cloud provider.
    - All Windows and Ubuntu virtual machines have system package updates automatically applied on a weekly schedule.
    - Other parts of the TRE infrastructure, for example Docker images used by the remote desktop and package proxy servers, are not automatically updated.
    ##### Potential Improvements
    - We should add a process for recognising when container images are out of date and for updating them.
* - 2.5.8.
  - 2
  - Any security patches will get automatically applied to VMs during Azure's update management process.
* - 2.5.9.
  - 1
  - A thorough external penetration test is carried out upon each major release of the Data Safe Haven codebase used by our TRE.
    The results are used to identify and make security improvements to infrastructure, processes and documentation.
    #### Potential improvements
    - We could additionally test our production deployments.
* - 2.5.10.
  - 2
  - The Data Safe Haven codebase used by our TRE has a system for creating internal security advisories and vulnerability reports.
    After a penetration test these are updated and new advisories are added.
    Each one is ranked for severity and it is decided whether they can be fixed technically or addressed with workarounds or mitigations.
    #### Potential improvements
    - Ensure that changes are made to production systems rather than simply incorporated into the next code release.
* - 2.5.11.
  - 1
  - The Data Safe Haven codebase used by our TRE makes public the overall results of our regular penetration tests, although the detailed report remains confidential.
    We have a publicly available document that describes the security checks our code goes through before release.
    These security checks are also carried out on our production systems.
    #### Potential improvements
    - We could try to find a way to securely run penetration tests on our production environments rather than setting up dedicated testing environments.
    - We should run regular security tests rather than only doing so at deployment time.
* - 2.5.12.
  - 2
  - We rely on Azure platform level encryption.
    This is done via platform managed keys rather than customer managed keys.
    #### Potential improvements
    - We could take over management of our own encryption keys but we would then need an independent solution for securing these.
* - 2.5.13.
  - 2
  - We use Azure Storage Explorer to securely copy data from a local or cloud datasource to our TRE, and from our TRE to known external locations.
    Connections made through Azure Storage Explorer are encrypted.
    User connections to access the TRE are made over https.
* - 2.5.14.
  - 0
  - Once a user has access to a TRE, they are able to work with any input data in a collaborative space.
    Any transfer of data within the TRE would be a movement from one folder to another on the same virtual machine.
    This would be restricted to the approved users who already have access, and so encryption is not needed.
* - 2.5.15.
  - 2
  - We rely on Azure's encryption implementation and trust that this is kept up to date.
    Details are available [here](https://learn.microsoft.com/en-us/azure/security/fundamentals/encryption-atrest).
* - 2.5.16.
  - 2
  - We rely on Azure's secure key management practices and trust that these are kept up to date.
    Details are available [here](https://learn.microsoft.com/en-us/azure/security/fundamentals/encryption-atrest#azure-key-vault).
* - 2.5.17.
  - 1
  - We do not apply physical protection methods.
    Our infrastructure is virtual and we allow users to connect on their own devices from an allowed IP address.
    Our terms-of-use require that users take reasonable precautions against physical attack.
    For example, connecting from a location that is as secure as practical such as via a VPN from a home office rather than insecure wifi in a public area.
* - 2.5.18.
  - 2
  - We are not hosting data that has specific regulatory requirements.
* - **Capability met?**
  - **YES**
  -
```

## Data lifecycle management

```{list-table}
:header-rows: 1
:name: tab-turing-dsh-data-lifecycle-management

* -
  - Score
  - Response
* - 3.1.1.
  - 2
  - Legal and regulatory implications are considered as part of the Data Protection Assessment Process (DPAP) when projects are first proposed.
    Each project is classified into one of five pre-defined security tiers before any work starts.
    Each tier has an associated set of security controls, although additional controls can be imposed on top of these if required.
* - 3.1.2.
  - 2
  - A signed approval form is required for each instance of data ingress or egress.
    A signed validation form must be filled out by the project team to confirm that any data moved in or out of the environment is as expected.
    A signed approval form for the security tier of each project is also required.
    These signed forms are kept in a private sharepoint folder, maintained by the TRE operators.
* - 3.1.3.
  - 2
  - {ref}`Information asset owners <data_roles>` must undergo a data classification process by following a flow chart to determine which of five sensitivity tiers data falls into.
    The data will then only be used within a TRE of an equivalent security tier (or higher).
* - 3.1.4.
  - 2
  - We implement data handling restrictions on data coming into the environment.
    These involve getting agreement from the {ref}`information asset owner <data_roles>`, {ref}`project manager <project_roles>` of the project and an independent representative from the Institute before any data or outputs are moved into the TRE.
    These stakeholders must sign a form detailing the requested ingress to confirm their agreement.
* - 3.1.5.
  - 2
  - We implement data handling restrictions on data coming out of the environment.
    These involve getting agreement from the {ref}`information asset owner <data_roles>`, {ref}`project manager <project_roles>` of the project and an independent representative from the Institute before any data or outputs are moved out of the TRE.
    These stakeholders must sign a form detailing the requested egress to confirm their agreement.
    These signed forms are kept in a private sharepoint folder, maintained by the TRE operators.
* - 3.1.6.
  - 2
  - Egress can only be performed by individuals with a secure access token, provided by secure email.
    Administrators will only provide access to named egress contact(s) that are signed off on by the {ref}`information asset owner <data_roles>`, amongst other stakeholders.
* - 3.1.7.
  - 2
  - Our data egress procedure requires signed agreement from representatives of all {ref}`information asset owners <data_roles>`, the project team and a referee external to the project.
* - 3.1.8.
  - 2
  - Input data is recorded in the aforementioned forms.
    The record includes a description of the data, its source (the {ref}`information asset owner <data_roles>`) and the data owner's contact details.
    This project initialisation document is specific to the particular TRE project that uses the data and will include the date of data ingress.
    At, or shortly after, the project end date, the data is securely and irreversibly deleted from the TRE.
* - 3.1.9.
  - 2
  - At the end of the project we require all relevant contact people to confirm that their environment can be torn down.
    Any data, code or other files that have not been brought out through the egress process will be irretrievably lost and any users associated only with this project will have their accounts disabled.
    #### Potential improvement
    - We should draft a clear policy on data deletion in the case that communication breaks down between the project team and TRE operators.
      In particular, this should focus on ensuring GDPR rules and data sharing agreements are not broken.
* - 3.1.10.
  - 2
  - The platform is based on Microsoft Azure cloud service and data is held within an Azure Storage Account.
    We have process forms in place for data deletion during the TRE project duration, and end-project termination whereby all data and TRE cloud infrastructure is deleted.
    An administrator could provide proof that the data has been deleted by showing the Azure Storage Account no longer exists, or that it is empty.
* - 3.1.11.
  - 2
  - The input data is immutable to users, it is kept in a folder that is read-only for TRE users.
    The only way input data can be modified is through the ingress process, which is logged.
* - 3.1.12.
  - 2
  - Ingress and egress are only possible by approved parties using a secure upload/download procedure.
    This involves using secure email to share a time-limited upload/download token for use with Azure Storage Explorer.
    Copying data into the TRE from the clipboard is not permitted.
    All users must complete relevant training before accessing a TRE, and sign our terms-of-use, which make them aware that they must not attempt to move data in or out of the environment without authorisation.
* - 3.1.13.
  - 2
  - Before data is added to the TRE, the research PI and other stakeholders must complete an ingress request form detailing the data to be included.
    The decision on what data is required for the project is with the {ref}`information asset owner <data_roles>` and project PI.
* - **Capability met?**
  - **YES**
  -
```

## Identity and access management

```{list-table}
:header-rows: 1
:name: tab-turing-dsh-identity-and-access-management

* -
  - Score
  - Response
* - 3.2.1.
  - 2
  - Each user only has a single account.
    We assume that only the authorised user will have possession of the correct username, password and physical MFA device.
* - 3.2.2.
  - 2
  - Our user creation process involves multiple identification factors to reasonably convince us of the identity of the person holding access to an account.
    #### Potential improvements
    - We could perform more detailed ID checks, perhaps by requiring photo ID.
* - 3.2.3.
  - 2
  - Each project's data is held separately.
    It is not possible to mix data between projects, even if an individual is a member of multiple projects.
* - 3.2.4.
  - 2
  - MFA is enforced for all users through Microsoft Entra.
    The second factor can be either push notification or a phone call.
* - 3.2.5.
  - 2
  - We use dedicated credentials for our TRE that are separate from any other accounts.
    A user who is working on multiple projects will use the same credentials for each of them.
* - 3.2.6.
  - 2
  - We are able to restrict access to known IP addresses.
    Where appropriate, IP addresses are restricted to the static institutional or personal IP addresses of the users allowed to connect to the environment.
    Sometimes, users are required to only access the TRE from inside the Institute's office space.
* - **Capability met?**
  - **YES**
  -
```

## Output management

```{list-table}
:header-rows: 1
:name: tab-turing-dsh-output-management

* -
  - Score
  - Response
* - 3.3.1.
  - 1
  - All outputs from a TRE go through our security classification process, carried out by the project investigator, {ref}`information asset owner <data_roles>` representative and an independent referee at the Turing.
    Different egress processes are required according to the sensitivity of the outputs.
    #### Potential improvements
    - We would like to create better guidance and documentation for classification, or possibly build tools to classify/create classification reports.
    - We would also like to better document the different methods available for outputs, depending on the security level of the classification.
* - 3.3.2.
  - 1
  - We require all projects to classify work packages, which considers all input data and the work to be done within the project.
    This process does not require a detailed description of the outputs and it does not restrict what outputs may be suggested for egress.
    #### Potential improvements
    Ensure we more precisely define the expected outputs for projects before they begin.
* - 3.3.3.
  - 1
  - We rely on the project stakeholders to reach a consensus on output disclosure risks.
    They must classify all outputs and, depending on the classification, the outputs might be made publicly available, available to named parties or available only inside another TRE.
    We do not feel that existing statistical disclosure processes are sufficient for the types of data we encounter, for example, unlabelled image files.
    #### Potential improvements
    - We should improve documentation of this process
* - 3.3.4.
  - 2
  - The {ref}`project manager <project_roles>`, {ref}`information asset owner <data_roles>` representative and referee are jointly responsible for output checking.
* - 3.3.5.
  - 2
  - We do not allow egress of files that cannot be manually checked except in the case of release back to the original {ref}`information asset owner <data_roles>`.
* - 3.3.6.
  - 1
  - There is a process in place to decide on the security tier of outputs before egress.
    This involves following a flowchart.
    There are no specific statistical rules.
* - 3.3.7.
  - 0
  - All output checking is manual.
* - 3.3.8.
  - 1
  - There is a process in place for tracking everything destined for egress, which requires sign off from relevant stakeholders.
    It should be possible for output checkers (project team) to make a call on what is the minimum requirement for results sharing.
    The process itself does not prevent the project team exporting more data, provided it has been signed off by stakeholders (including the {ref}`information asset owner <data_roles>`).
* - **Capability met?**
  - **YES**
  -
```

## Information search and discovery

```{list-table}
:header-rows: 1
:name: tab-turing-dsh-information-search-and-discovery

* -
  - Score
  - Response
* - 3.4.1.
  - 2
  - As each project brings its own data we do not have a catalogue of available datasets.
* - **Capability met?**
  - **YES**
  -
```

## Security Levels and Tiering

```{list-table}
:header-rows: 1
:name: tab-turing-dsh-security-level

* -
  - Score
  - Response
* - 3.5.1.
  - 2
  - We categorise projects into one of five security tiers.
    These are clearly defined in our documentation.
    We are able to support four of those tiers and would reject any projects falling into the most sensitive tier.
* - 3.5.2.
  - 2
  - We support projects with differing security requirements through security controls that are pre-defined for each tier.
* - 3.5.3.
  - 2
  - We support a documented set of security control tiers that projects can choose from at the outset.
* - **Capability met?**
  - **YES**
  -
```

## Research Meta-Data

```{list-table}
:header-rows: 1
:name: tab-turing-dsh-meta-data

* -
  - Score
  - Response
* - 3.6.1.
  - 0
  - We do not hold a catalogue of data in this format for this purpose.
    The data is provided to us by the {ref}`information asset owner <data_roles>` for a specific purpose.
    Researchers do not apply to us to access specific datasets and thus do not need to have access to a description of the data.
* - 3.6.2.
  - 0
  - This is something we would expect the {ref}`information asset owner <data_roles>` to do, rather than implement ourselves.
    For example, they could use a high-security tier 3 TRE to summarise or produce a synthetic version of a sensitive dataset for use in a lower security, tier 2 TRE.
* - **Capability met?**
  - **YES (no mandatory statements)**
  -
```

## Meta-Data Search and Discovery Application

```{list-table}
:header-rows: 1
:name: tab-turing-dsh-meta-data-search

* -
  - Score
  - Response
* - 3.7.1.
  - 0
  - We do not provide such an application.
    We do not maintain meta-data for sets of available datasets, since we do not maintain a corpus of datasets for people to apply for access to.
* - **Capability met?**
  - **YES (no mandatory statements)**
  -
```

## Data Archiving

```{list-table}
:header-rows: 1
:name: tab-turing-dsh-data-archiving

* -
  - Score
  - Response
* - 3.8.1.
  - 1
  - We don’t have a particular method for data archiving in the TRE, though administrators do have the ability to move data to a read-only location if needed.
* - 3.8.2.
  - 0
  - We don’t have a particular method for archiving data in the TRE, though it is possible to keep data in the Azure Storage Accounts whilst restricting access to users.
    We don’t handle formatting or maintaining of datasets, which is up to project teams using the TRE.
* - **Capability met?**
  - **YES (no mandatory statements)**
  -
```

## Business continuity management

```{list-table}
:header-rows: 1
:name: tab-business-continuity-subject

* -
  - Score
  - Response
* - 4.1.1.
  - 1
  - We rely on redundancy options provided by Azure, such as load-balancing and geo-redundancy, to maximise the uptime of the TRE.
    If there is a catastrophic failure of Azure, access to TREs will be lost until service is resumed.
    We believe this is an acceptable risk that does not need further mitigation.
* - 4.1.2.
  - 1
  - No part of our business continuity plan depends on actions that we can take, so we are not able to test it.
* - **Capability met?**
  - **YES**
  -
```

## Project and programme management

```{list-table}
:header-rows: 1
:name: tab-project-programme-management

* -
  - Score
  - Response
* - 4.2.1.
  - 2
  - All projects have a project manager named in a Sharepoint document that is signed by all stakeholders.
    This individual is responsible for all project support tasks.
    They will liaise with the TRE operations team as necessary.
* - 4.2.2.
  - 2
  - Only a list of named {ref}`data consumers <project_roles>` get access to to the TRE.
    The project manager is not currently forbidden from being a project team member but this situation has never arisen.
    #### Potential improvements
    - We could create a policy that the project manager is not allowed to be part of the project team.
* - **Capability met?**
  - **YES**
  -
```

## Knowledge management

```{list-table}
:header-rows: 1
:name: tab-knowledge-management

* -
  - Score
  - Response
* - 4.3.1.
  - 2
  - Our documentation is hosted across two public web sites.
    One site contains documentation for the TRE implementation, including deployment and user guides.
    The other describes the Institutes particular processes for TRE operations.
    These sites are generated from GitHub repositories which can be easily updated in response to feedback as needed.
* - 4.3.2.
  - 2
  - We have documentation in place for using and managing our TRE.
    #### Potential improvements
    - We could offer a consistent training programme for all projects.
* - 4.3.3.
  - 1
  - We have identified training needs for stakeholders and made plans to address this, but we do not currently have plans for reviewing these.
    #### Potential improvements
    - We should perform a regular training needs analysis review.
* - **Capability met?**
  - **YES**
  -
```

## Financial management

```{list-table}
:header-rows: 1
:name: tab-financial-management

* -
  - Score
  - Response
* - 4.4.1.
  - 2
  - We make estimates of our infrastructure costs publicly available in advance.
    The project manager for each project is also able to see real-time infrastructure spending.
    We do not currently charge for person-time, although we plan to do so in future.
    Our charging structure is simple, publicly available, and discussed with the project manager before each project starts.
* - 4.4.2.
  - 2
  - We make use of Azure's spending calculators and other bespoke tools developed by the Institute to manage this.
    We have dedicated management professionals for charging costs back to projects.
* - 4.4.3.
  - 1
  - We recover the infrastructure costs each project.
    Infrastructure common to all projects is centrally funded on a year-by-year basis.
    We do not currently recover person-time costs.
    We do not have a process in place for ensuring funding in the long-term.
    #### Potential improvements
    - We could look to secure longer-term commitments for ongoing funding.
* - 4.4.4.
  - 2
  - We use the Data Safe Haven codebase which is under active development and which considers cost-effectiveness as part of its update process.
    We start by deploying cheaper resources and resize them to more powerful (and expensive) versions only when requested by end users, for instance, GPU-enabled machines are available only on request.
    We turn off infrastructure components when not in use.
* - **Capability met?**
  - **YES**
  -
```

## Procurement

```{list-table}
:header-rows: 1
:name: tab-procurement

* -
  - Score
  - Response
* - 4.5.1.
  - 2
  - We have systems in place for ensuring cloud credits required for TRE provision can be purchased by projects requiring a TRE.
    We also have systems in place for providing Chromebooks to TREs users who require access to higher-security TREs where managed devices are required.
* - **Capability met?**
  - **YES**
  -
```

## IT Service management

```{list-table}
:header-rows: 1
:name: tab-it-service-management

* -
  - Score
  - Response
* - 4.6.1.
  - 2
  - We have a dedicated service team for deploying TREs and supporting processes.
    This is well documented and made available to {ref}`data consumers <project_roles>` via the company intranet.
    The documents themselves are [publicly available online](https://alan-turing-institute.github.io/trusted-research/).
* - **Capability met?**
  - **YES**
  -
```

## Relationship management

```{list-table}
:header-rows: 1
:name: tab-relationship-stakeholder

* -
  - Score
  - Response
* - 4.7.1.
  - 2
  - The code that deploys our TRE infrastructure is open-source and open to contributions from anyone.
    We also have a dedicated Slack channel and email address for stakeholders to engage with the project team.
* - **Capability met?**
  - **YES**
  -
```

## Public Involvement and Engagement

```{list-table}
:header-rows: 1
:name: tab-supporting-pie
* -
  - Score
  - Response
* - 4.8.1.
  - 1
  - All public engagement activities we have undertaken as a project have been led by public engagement professionals and have followed best practice as outlined in PEDRI guidelines.
    #### Potential improvements
    - We should develop a public engagement strategy for the Turing DSH project in collaboration with the Institute's public engagement specialists.
* - 4.8.2.
  - 0
  - We do not currently share the details of projects using our TRE.
    #### Potential improvements
    - We might consider doing this after discussion our legal team and other stakeholders.
* - 4.8.3.
  - 0
  - We do not include members of the public in our approval process.
    We do not think this is appropriate in the case of commercially-sensitive data and we already have an Institute-wide ethics approvals process.
* - 4.8.4.
  - 0
  - There is a clear process in place for internal incident reporting.
    There is no process for publicly sharing this information.
* - **Capability met?**
  - **YES**
  -
```

## Legal services

```{list-table}
:header-rows: 1
:name: tab-legal-services

* -
  - Score
  - Response
* - 4.9.1.
  - 2
  - The Institute has a legal team who can be contacted with matters relating to the handling of sensitive data, which includes TRE projects.
    The TRE operators can get legal advice from this team as required.
* - 4.9.2.
  - 2
  - The Institute has a data protection team who can be contacted with matters relating to the handling of sensitive data, which includes TRE projects.
    The TRE operators can get legal advice from this team as required.
* - 4.9.3.
  - 2
  - The project manager has responsibility for managing contracts related to data sharing and secondment agreements.
    The TRE operations team together with the project manager have responsibility for ensuring that user-access terms-of-use are signed.
* - **Capability met?**
  - **YES**
  -
```
