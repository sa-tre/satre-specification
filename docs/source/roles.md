(satre_roles)=

# Roles

A TRE conforming to the SATRE specification should provide a broadly similar experience for stakeholders operating in each of these defined roles.
There is not necessarily a one-to-one mapping between roles and people.
One person can have multiple roles.

(user_roles)=

## TRE user roles

Roles for people using the TRE to conduct research or analyse data in the TRE.

<!-- The document will explain that user experience of the platform and associated documentation should feel similar across TREs conforming to SATRE specification. -->

```{list-table}
:header-rows: 1
:name: tab-tre-role-users

* - Role name
  - Role description
* - Researcher
  - People responsible for carrying out the research project using a TRE.
* - Data Steward
  - People who ensure data within a TRE is maintained and processed in ways useful to the researchers, including providing data extracts.

```

(admin_roles)=

## TRE administration roles

The IT and related professionals who will be responsible for deploying and managing instances of a TRE conforming to the SATRE specification.
These roles cover managing TRE computing infrastructure, but also administering the TRE itself (_e.g._ managing users and projects).

<!-- The document will explain that SATRE conforming TREs should have documentation and infrastructure deployment code/apps that conform to software engineering best practices, which are also defined here, making them "simple" for an IT professional to follow; troubleshooting steps included. -->

```{list-table}
:header-rows: 1
:name: tab-tre-role-administrator

* - Role name
  - Role description
* - TRE operator
  - People responsible for the management of the TRE's IT infrastructure and general processes. Examples include carrying out data ingress/egress and managing user access.
* - Infrastructure Deployment Role
  - People responsible for carrying out (and documenting) the {ref}`infrastructure_deployment_process`.
* - Output Checker
  - People responsible for checking the disclosure risk of project outputs, before egress, as part of the disclosure control process. See {ref}`output_management`.
* - Database Administrator
  - People responsible for managing any databases included in the TRE. Where a database is used by multiple projects, this includes handling segregation of users and databases belonging to different projects. See {ref}`advanced_CCC`.
```

(developer_roles)=

## TRE developer roles

The software engineers responsible for developing and maintaining TRE software, including adding functionality, bug fixes and general maintenance.

<!-- The document will explain recommended practices suitable for developing a software of this complexity and reference learnings from existing TRE developers. -->

```{list-table}
:header-rows: 1
:name: tab-tre-role-developer

* - Role name
  - Role description
* - TRE Developer
  - People responsible for building the software infrastructure that can be used as a TRE. These could be Research Software Engineers, whose job involves applying professional software engineering expertise to challenges in scientific research. Alternatively these could be developers who are contracted to build a TRE for a given insitution or project.
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
  - Person or group of persons who leads and controls an organization at the highest level. This definition is taken from *ISO 9000:2015* and in this context refers to the most senior governance official who own the risks associated with TRE research, can make decisions and allocate resources. See {ref}`risk_ownership_process`.
* - Information Asset Owner/ Data Custodian
  - Owner of a dataset, project or work package within a TRE.
* - Lay panel
  - Members of the public charged with oversight of TRE operational decisions on behalf of parties affected by data usage.

```
