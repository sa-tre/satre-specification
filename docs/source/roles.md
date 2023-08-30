(satre_roles)=

# Roles

A TRE conforming to the SATRE specification should provide a broadly similar experience for stakeholders operating in each of these defined roles.
There is not necessarily a one-to-one mapping between roles and people.
One person can have multiple roles.

(user_roles)=

## TRE user roles

Roles for people using the TRE to conduct research or analyse data in the TRE.

```{list-table}
:header-rows: 1
:name: tab-tre-role-users

* - Role name
  - Role description
* - Researcher
  - People responsible for carrying out the research project using a TRE. These could be programmers and data scientists, but could also be scientists working in fields where deep computing expertise is less common. Researchers working with TREs that meet the SATRE standard should to have a broadly similar user experience, at least where the type of researcher is consistent (e.g. data scientists). This includes both the user experience of the platforms themselves, and the associated documentation.
* - Data Steward
  - People who ensure data within a TRE is maintained and processed in ways useful to researchers, including providing data extracts to specific projects or researchers. May also be known as Data Wranglers or Data Cleaners.

```

(admin_roles)=

## TRE administration roles

The IT and related professionals who will be responsible for deploying and managing instances of a TRE conforming to the SATRE specification.

```{list-table}
:header-rows: 1
:name: tab-tre-role-administrator

* - Role name
  - Role description
* - TRE Operator
  - People responsible for the management of the TRE's IT infrastructure and general processes. Examples include carrying out data ingress/egress and managing user access. TRE operators should expect to have access to documentation regarding all processes they are required to carry out, developed by themselves or (in partnership with) the TRE Developers. This documentation should be comprehensive and include troubleshooting steps. See {ref}`knowledge_management`.
* - Infrastructure Deployment Role
  - People responsible for carrying out the {ref}`infrastructure_deployment_process`. This role could be taken on by either the TRE Operators or the TRE Developers.
* - Output Checker
  - People responsible for checking the disclosure risk of project outputs, before egress, as part of the disclosure control process. See {ref}`output_management`.
* - Database Administrator
  - People responsible for managing any databases included in the TRE. Where a database is used by multiple projects, this includes handling segregation of users and databases belonging to different projects. See {ref}`advanced_CCC`.
```

(developer_roles)=

## TRE developer roles

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

## TRE governance roles

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
* - Information Asset Owner
  - This could be the custodian or owner of a dataset, project or other information asset within a TRE.
* - Lay panel
  - Members of the public charged with oversight of TRE operational decisions on behalf of parties affected by data usage.

```
