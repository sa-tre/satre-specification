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
    - We could be more proactive about trying to stay up-to-date with changes to requirements.
    - For instance, we could hold an annual review with the Turing Legal and Data Protection teams to ensure all current requirements are still met by the TRE organisation.
* - 1.1.2.
  - 1
  - - We have documented our institutional risk appetite and understand what kinds of work we are prepared to support.
    - All projects handled in the TRE have gone through our institutional Data Protection Assessment Process and Ethics Approval Process.
    - All projects are tracked through a ticketing system with relevant documents and agreements stored on Sharepoint.
    ##### Potential Improvements
    - We would like to improve our document handling workflow.
    - This could be through the development of an Information Governance App through which all projects can be managed directly by approved users
* - 1.1.3.
  - 1
  - - The Institute has Legal and Data Protection Teams who ensure that projects meet our institutional requirements.
    - Our sysadmin team is currently appropriately sized for the number of projects we are handling.
    - The Legal and Data Protection teams do not have staff dedicated to our TRE.
    ##### Potential Improvements
    - Our TRE organisation does not control staff numbers in the legal and data protection teams.
    - Directly assigning staffing to support our TRE would help improve resource provision.
* - **Summary**
  - **?**
  - **Explanation**
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
    ##### Potential Improvements
    - We do not as of yet have an explicit process for determining who should have admin access to these folders and repositories, for instance passing a specific training module or going through an induction process.
* - 1.2.2.
  - 1
  - - All SOPs are stored in a version controlled repository. Policies, forms and project documentation are stored in a controlled Sharepoint folder.
    ##### Potential Improvements
    - We do not currently use explicit versioning for forms/documents that need to be signed.
    - We do not currently tag documents handled by git version control so that the specific document followed can be referred to.
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
    ##### Potential Improvements
    - We do not do anything in particular to flag when an issue was due to a deviation from SOP.
    - We could do better at tracking our reporting.
* - 1.2.10.
  - 2
  - - Part of our security incident response is to initiate changes to our procedures to mitigate future incidents.
    - Reporting and discussing incidents is prompt and resolving the underlying issue prioritised.
* - 1.2.11.
  - 1
  - - Training records for TRE users are recorded in Sharepoint.
    - We track the configuration data needed to manage each TRE project on a GitHub issue.
    - This issue is also used to track of changes made throughout the lifecycle of a TRE project.
    ##### Potential Improvements
    - We do use feedback and our impressions of the effectiveness of the TRE to guide development and changes.
    - We do not actively monitor the quality of services provided to end-users.
* - 1.2.12.
  - 0
  - - We do not use any quality management software.
* - **Summary**
  - **?**
  - **Explanation**
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
    - We do not regularly update our risk register.
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
    - We do not have a procedure for handling opportunities outside our risk appetite
* - **Summary**
  - **?**
  - **Explanation**
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
    - Data sharing agreements must be in place before any data is ingressed.
* - 1.4.2.
  - 1
  - - As soon as we are informed of the need to revoke user access, we will do so.
    - Lists of responsible persons are established at the beginning of each project and these are kept up-to-date.
    ##### Potential Improvements
    - We tend to reactively respond to user removal requests rather than actively confirming that users are active.
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
    - We are planning to develop a system for tracking projects and datasets.
* - 1.4.6.
  - 1
  - - We keep records for each project on which datasets are being used and any conditions attached to that use.
    - We do not have a central database of data assets.
    ##### Potential Improvements
    - We are planning to develop a system for tracking projects and datasets.
* - 1.4.7.
  - 1
  - - We manage our projects using a GitHub project board.
    - Documents pertaining to each project are kept in a private Sharepoint folder.
    ##### Potential Improvements
    - We could make this a less manual process.
* - **Summary**
  - **?**
  - **Explanation**
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
    - We do not make any further checks on user ID.
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
    - We are planning to develop a more comprehensive system for user records tracking.
* - **Summary**
  - **?**
  - **Explanation**
```


