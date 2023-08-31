(evaluation_alan_turing_institute)=

# Alan Turing Institute Data Safe Haven

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
    - Project specific requirements are discussed with data providers before start of each project.
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
    - We also have a flowchart that project teams and data providers must follow to agree on the security tier of their project before it starts.
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
    - Data egress needs to be agreed by the project stakeholders: the principal investigator, data provider and a referee representing the interests of the Institute.
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
  - - Onboarding documentation exists for both TRE operators and project teams.
    - Users must complete appropriate training and sign our terms of use before being granted access to the TRE.
* - 1.5.3.
  - 2
  - - We use Microsoft Entra to manage user accounts.
    - Access to resources and data is controlled by RBAC.
* - 1.5.4.
  - 2
  - - We have a process for agreeing which people are able to take which actions involving sensitive data.
    - Delegation of approval authority is also included here.
    - A document summarising these decisions must be signed by the principal investigator, data provider and referee before the project begins.
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
    - TRE operators must pass all user training requirements as well as data handling and cyber security training.
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
* - 2.4.6.
  - 1
  - - Many cloud services, for example virtual networks, are kept up to date by the cloud provider.
    - All Windows and Ubuntu virtual machines have system package updates automatically applied on a weekly schedule.
    - Other parts of the TRE infrastrcture, for example Docker images used by the remote desktop and package proxy servers, are not automatically updated.
    ##### Potential Improvements
    - We should add a process for recognising when container images are out of date and for updating them.
* - 2.4.7.
  - 1
  - Daily anti-virus definition updates and scans are carried out by ClamAV on all Linux VMs.
    ##### Potential Improvements
    - Extend anti-virus coverage to user-inacessible Windows machines, and also scan data (block and object storage) if possible.
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
  - We implement data handling restrictions on data coming into the environment.
    These involve getting agreement from the data provider, principal investigator of the project and an independent representative from the Institute before any data or outputs are moved into the TRE.
    These stakeholders must sign a form detailing the requested ingress to confirm their agreement.
* - 3.1.4.
  - 2
  - We implement data handling restrictions on data coming out of the environment.
    These involve getting agreement from the data provider, principal investigator of the project and an independent representative from the Institute before any data or outputs are moved out of the TRE.
    These stakeholders must sign a form detailing the requested egress to confirm their agreement.
    These signed forms are kept in a private sharepoint folder, maintained by the TRE operators.
* - 3.1.5.
  - 2
  - Our data egress procedure requires signed agreement from representatives of all data providers, the project team and a referee external to the project.
* - 3.1.6.
  - 2
  - Input data is recorded in the aforementioned forms.
    The record includes a description of the data, its source (the data provider) and the data owner's contact details.
    This project initialisation document is specific to the particular TRE project that uses the data and will include the date of data ingress.
    At, or shortly after, the project end date, the data is securely and irreversibly deleted from the TRE.
* - 3.1.7.
  - 2
  - At the end of the project we require all relevant contact people to confirm that their environment can be torn down.
    Any data, code or other files that have not been brought out through the egress process will be irretrievably lost and any users associated only with this project will have their accounts disabled.
    #### Potential improvement
    - We should draft a clear policy on data deletion in the case that communication breaks down between the project team and TRE operators.
      In particular, this should focus on ensuring GDPR rules and data sharing agreements are not broken.
* - 3.1.8.
  - 1
  - Some research environment data is backed up.
    This includes virtual disks and object storage accounts which contain users personal/configuration files and working data.
    Backups are distributed across data centres within a single region.
    Input data is only kept as a single, immutable copy which is not backed up (although users may make copies which would be).
    Because input data is always a copy, we are not concerned about the loss of input data.
    #### Potential improvement
    - We could ensure that non-file working data, such as database contents are also backed up.
* - 3.1.9.
  - 2
  - The input data is immutable to users, it is kept in a folder that is read-only for TRE users.
    The only way input data can be modified is through the ingress process, which is logged.
* - 3.1.10.
  - 2
  - Ingress and egress are only possible by approved parties using a secure upload/download procedure.
    This involves using secure email to share a time-limited upload/download token for use with Azure Storage Explorer.
    Copying data into the TRE from the clipboard is not permitted.
    All users must complete relevant training before accessing a TRE, and sign our terms-of-use, which make them aware that they must not attempt to move data in or out of the environment without authorisation.
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
  - Each project's data is held separately and users are only able to access data for one project at a time.
    It is not possible to mix data between projects, even if an individual is a member of multiple projects.
* - 3.2.4.
  - 2
  - MFA is enforced for all users through Microsoft Entra.
    The second factor can be either push notification or a phone call.
* - 3.2.5.
  - 2
  - We use dedicated credentials for our TRE that are separate from any other accounts.
    A user who has is working on multiple projects will use the same credentials for each of them.
* - 3.2.6.
  - 2
  - We are able to restrict access to known IP addresses.
    Where appropriate, IP addresses are restricted to the static institutional or personal IP addresses of the users allowed to connect to the environment.
    Where appropriate, users are required to only access the TRE from inside the Institute's office space.
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
  - All outputs from a TRE go through our security classification process, carried out by the project investigator, data provider representative and an independent referee at the Turing.
    Different egress processes are required according to the sensitivity of the outputs.
    #### Potential improvements
    - We would like to create better guidance and documentation for classification, or possibly build tools to classify/create classification reports.
    - We would also like to better document the different methods available for outputs, depending on the security level of the classification.
* - 3.3.2.
  - 1
  - We require all projects to classify work packages, which considers all input data and the work to be done within the project.
    This is done broadly, and doesn’t strictly enforce consideration for expected outputs.
    #### Potential improvements
    Ensure we more precisely define the expected outputs for projects before they begin.
* - 3.3.3.
  - 1
  - We rely on the project stakeholders to collaboratively decide on output disclosure risks.
    They must classify all outputs and, depending on the classification, the outputs might be made publicly available, available to named parties or available only inside another TRE.
    We do not feel that existing statistical disclosure processes are sufficient for the types of data we encounter, for example, unlabelled image files.
    #### Potential improvements
    - We should improve documentation of this process
* - 3.3.4.
  - 2
  - The principal investigator, data provider representative and referee are jointly responsible for output checking.
* - 3.3.5.
  - 2
  - We do not allow egress of files that cannot be manually checked except in the case of release back to the original data provider.
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

## Information security

```{list-table}
:header-rows: 1
:name: tab-turing-dsh-information-security

* -
  - Score
  - Response
* - 3.5.1.
  - 1
  - We comply with the NHS DSPT standard which allows us to process anonymised patient-derived data.
    #### Potential improvements
    - We would like to gain accreditation for more wide-ranging standards, for instance CyberEssentials+, ISO27001 and DEA, which cover holistic safe data and research management above and beyond NHS patient data.
* - 3.5.2.
  - 1
  - A thorough external penetration test is carried out upon each major release of the Data Safe Haven codebase used by our TRE.
    The results are used to identify and make security improvements to infrastructure, processes and documentation.
    #### Potential improvements
    - We could penetration test our production system instead of an equivalent dummy system.
* - 3.5.3.
  - 2
  - The Data Safe Haven codebase used by our TRE has a system for creating internal security advisories and vulnerability reports.
    After a penetration test these are updated and new advisories are added.
    Each one is ranked for severity and it is decided whether they can be fixed technically or addressed with workarounds or mitigations.
    #### Potential improvements
    - Ensure that changes are made to production systems rather than simply incorporated into the next code release.
* - 3.5.4.
  - 2
  - Our terms-of-use require users to report any potential data incident.
    We have a process in place for managing data incidents, whether raised by users or discovered independently, that ensures we meet our legal requirements and also implement any necessary changes, such as disabling access to a TRE if necessary.
* - 3.5.5.
  - 1
  - The Data Safe Haven codebase used by our TRE makes public the overall results of our regular penetration tests, although the detailed report remains confidential.
    We have a publicly available document that describes the security checks our code goes through before release.
    These security checks are also carried out on our production systems.
    #### Potential improvements
    - We could try to find a way to securely run penetration tests on our production environments rather than setting up dedicated testing environments.
    - We should run regular security tests rather than only doing so at deployment time.
* - 3.5.6.
  - 2
  - We rely on Azure platform level encryption.
    This is done via platform managed keys rather than customer managed keys.
    #### Potential improvements
    - We could take over management of our own encryption keys but we would then need an independent solution for securing these.
* - 3.5.7.
  - 2
  - We use Azure Storage Explorer to securely copy data from a local or cloud datasource to our TRE, and from our TRE to known external locations.
    Connections made through Azure Storage Explorer are encrypted.
    User connections to access the TRE are made over https.
* - 3.5.8.
  - 0
  - Once a user has access to a TRE, they are able to work with any input data in a collaborative space.
    Any transfer of data within the TRE would be a movement from one folder to another on the same virtual machine.
    This would be restricted to the approved users who already have access, and so encryption is not needed.
* - 3.5.9.
  - 2
  - We rely on Azure's encryption implementation and trust that this is kept up to date.
    Details are available [here](https://learn.microsoft.com/en-us/azure/security/fundamentals/encryption-atrest).
* - 3.5.10.
  - 2
  - We rely on Azure's secure key management practices and trust that these are kept up to date.
    Details are available [here](https://learn.microsoft.com/en-us/azure/security/fundamentals/encryption-atrest#azure-key-vault).
* - 3.5.11.
  - 1
  - We do not apply physical protection methods.
    Our infrastructure is virtual and we allow users to connect on their own devices from an allowed IP address.
    Our terms-of-use require that users take reasonable precautions against physical attack, for instance, by connecting from a location that is as secure as practical, such as using a VPN from a home office, rather than a public coffee shop.
* - 3.5.12.
  - 2
  - We are not hosting data that has specific regulatory requirements.
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
* - 3.6.1.
  - 2
  - We categorise projects into one of five security tiers.
    These are clearly defined in our documentation.
    We are able to support four of those tiers and would reject any projects falling into the most sensitive tier.
* - 3.6.2.
  - 2
  - We support projects with differing security requirements through security controls that are pre-defined for each tier.
* - 3.6.3.
  - 2
  - We support a documented set of security control tiers that projects can choose from at the outset.
* - **Capability met?**
  - **YES**
  -
```
