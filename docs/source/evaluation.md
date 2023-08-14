(evaluation)=

# Evaluating TREs against SATRE

## How to score

You should score your TRE against each statement in the SATRE specification.
The scoring system is:

- **0 (Fail)**: we do not do this
- **1 (Needs improvement)**: we do this but want to do better
- **2 (Sufficient)**: we do this and are currently happy with it

## Examples

### Alan Turing Institute Data Safe Haven

```{list-table}
:header-rows: 1
:name: tab-turing-dsh-ig

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
```

### TREEHOOSE
