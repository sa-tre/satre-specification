(satre_roles)=

# Roles

A TRE conforming to the SATRE specification should provide a broadly similar experience for stakeholders operating in each of these defined roles.
There is not necessarily a one-to-one mapping between roles and people.
One person can have multiple roles.

(project_roles)=

## TRE Project Roles

Roles for TRE end-users conducting research or analysing data in the TRE and others involved in managing this research.

```{list-table}
:header-rows: 1
:name: tab-tre-role-project

* - Role name
  - Role description
* - Researcher
  - People responsible for carrying out the research project using a TRE. These could be programmers and data scientists, but could also be scientists working in fields where deep computing expertise is less common. Researchers working with TREs that meet the SATRE standard should to have a broadly similar user experience, at least where the type of researcher is consistent (e.g. data scientists). This includes both the user experience of the platforms themselves, and the associated documentation.
* - Data Consumer
  - General term for any individuals who will be provided access to data via a TRE.
* - Project Manager
  - The person in charge of coordinating other roles for the duration of a specific TRE project. See {ref}`project_management`.
* - Project Team
  - Refers to the team of researchers and manager(s) working on a specific project that uses a TRE.

```

(data_roles)=

## TRE Data Roles

Roles for people managing data and databases used in a TRE.

```{list-table}
:header-rows: 1
:name: tab-tre-role-data

* - Role name
  - Role description
* - Data Steward
  - People who ensure data within a TRE is maintained and processed in ways useful to researchers, including providing data extracts to specific projects or researchers. May also be known as Data Wranglers or Data Cleaners.
* - Database Administrator
  - People responsible for managing any databases included in the TRE. Where a database is used by multiple projects, this includes handling segregation of users and databases belonging to different projects. See {ref}`advanced_CCC`.
* - Data provider
  - The custodian or owner of a dataset, who provides access to the data for research in a TRE. This could be done via liasing with the TRE Operator on {ref}`secure data ingress <data_lifecycle_management>`.
* - Information Asset Owner
  - General term for custodians or owners of a datasets, projects or other information assets within a TRE.

```

(admin_roles)=

## TRE Administration Roles

The IT and related professionals who will be responsible for deploying and managing instances of a TRE conforming to the SATRE specification.

```{list-table}
:header-rows: 1
:name: tab-tre-role-administrator

* - Role name
  - Role description
* - TRE Operator
  - People responsible for the management of the TRE's IT infrastructure and general processes documented throughout the SATRE specification. Examples include carrying out data ingress/egress and managing user access. TRE operators should expect to have access to documentation regarding all processes they are required to carry out, developed by themselves or (in partnership with) the TRE Developers. This documentation should be comprehensive and include troubleshooting steps (see {ref}`knowledge_management`).
* - Infrastructure Deployment Role
  - People responsible for carrying out the {ref}`infrastructure_deployment_process`. This role could be taken on by either the TRE Operators or the TRE Developers.
* - Output Checker
  - People responsible for checking the disclosure risk of project outputs, before egress, as part of the disclosure control process. See {ref}`output_management`.
```

(developer_roles)=

## TRE Developer Roles

The software engineers responsible for developing and maintaining TRE software, including adding functionality, bug fixes and general maintenance.

```{list-table}
:header-rows: 1
:name: tab-tre-role-developer

* - Role name
  - Role description
* - TRE Developer
  - People responsible for building the software infrastructure that can be used as a TRE. These could be Research Software Engineers, whose job involves applying professional software engineering expertise to challenges in scientific research. Alternatively these could be developers who are contracted to build a TRE for a given insitution or project. TRE developers include people creating bespoke platforms catering to the specific requirements of a project or dataset, as well as developers building generalisable solutions to TRE provision that can be configured based on the research context.
```

(governance_roles)=

## TRE Governance Roles

Roles that uphold the governance of TREs.
Such governance responsibilities typically involve establishing policies and procedures to ensure the responsible use of data, protecting the privacy and confidentiality of research participants, and promoting transparency and accountability in research activities.

```{list-table}
:header-rows: 1
:name: tab-tre-role-governance

* - Role name
  - Role description
* - Quality Manager
  - People responsible for ensuring the TRE is operating correctly and that all processes are working as intended, and being followed by other roles. See {ref}`quality_management`.
* - Top Management
  - People who lead and control an organisation at the highest level. This definition is taken from *ISO 9000:2015* and in this context refers to the most senior governance official who own the risks associated with TRE research, can make decisions and allocate resources. See {ref}`risk_ownership_process`.
* - Data Protection Team
  - The team responsible for {ref}`data protection <data_protection>` at the organisation hosting the TRE.

```

(public_roles)= 

## Public Roles

Roles that concern members of the public with regard to TREs and TRE research.

```{list-table}
:header-rows: 1
:name: tab-tre-role-public

* - Role name
  - Role description
* - Lay Panel
  - Members of the public charged with oversight of TRE operational decisions on behalf of parties affected by data usage.
* - Data Subject
  - People who are identifiable by data being used for research, e.g. patients in healthcare record data.
```