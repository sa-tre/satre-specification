(pillar_information_governance)=

# Information governance

This pillar concerns what the TRE operator does to ensure information risk is measured and managed to an acceptable level.

```{figure} ../../images/Capability_Map/full.drawio.svg
:alt: SATRE Pillars Capability Map
:align: center

SATRE Pillars Capability Map
```

<!-- See all pillars of the SATRE Pillars Capability Map here: {ref}`satre_pillars` -->

## Policy regulation and management

_How a TRE operator determines what policies and regulations are required and ensures alignment to changes in requirements._

```{list-table}
:header-rows: 1
:name: tab-policy-regulation-management

* - Statement
  - Guidance
  - Importance
* - You must have a process in place to ensure any new project requiring a TRE meets relevant legal, ethical and contractual requirements.
  - For example national legislation such as GDPR, discipline specific regulation like GCP or contractural requirements from a specific data provider such as a company or research partner organisation.
  - Mandatory
* - You must have a process in place to monitor changes to any legal, ethical and contractual requirements, and to update your policies accordingly.
  -
  - Mandatory
```

## Quality management

_The ability of a TRE operator to measure and control quality of processes, documentation and outputs._

### Document management

```{list-table}
:header-rows: 1
:name: tab-document-management

* - Statement
  - Guidance
  - Importance
* - You must control all of your policies and standard operating procedures.
  - This may include measures like restricting edit access to relevant documents, and recording acceptance of policies for all TRE operators.
  - Mandatory
* - You should use codified change processes when altering your policies and standard operating procedures.
  -
  - Recommended
* - You could use version control to track changes to their policies and processes.
  - Version control includes recording dates of changes, person responsible for carrying out changes, and summary of changes.
  - Optional
```

### Issue management

_The ability of a TRE operator to track deviations from stated policies._

```{list-table}
:header-rows: 1
:name: tab-issue-management

* - Statement
  - Guidance
  - Importance
* - You must have a clear process in place for addressing any activity that deviates from your policies and standard operating procedures.
  - This can include measures like triage analysis and a process for updating policies.
  - Mandatory
* - You must have methods in place to record progress in resolving issues with, and deviations against, your policies.
  -
  - Mandatory
```

### Compliance, monitoring and reporting

_The ability of the TRE organisation to monitor compliance with internal and external requirements, agreements, laws and standards._

```{list-table}
:header-rows: 1
:name: tab-compliance-monitoring-reporting
* - Statement
  - Guidance
  - Importance
* - You must be able to audit your TRE organisation against whichever external standards are relevant to you.
  - If you are publicly accredited against a standard, for example ISO27001, DSPT or CyberEssentials+, you must have processes in place to ensure you remain compliant
  - Mandatory
* - You should report on and share outcomes of each audit of your TRE organisation with the required bodies.
  - This may be a requirement of continued accreditation by external organisations or regulatory bodies.
  - Recommended
* - You log data access queries and publish these logs
  - Transparency is a key principle for an environment that is trusted for research.
    With these logs publicly available, there is transparency around how the data was used, and any actions that could compromise the security of the sensitive data.
  - Recommended
* - You log user actions other than data access, for example network connection attempts or infrastructure actions within a TRE.
  - Logging can help to identify actions, intentional or unintentional, that could compromise the security of the SRE, or result in the accidental disclosure of data outside the TRE.
    Any measures that TRE operators deem valuable for reporting should be logged.
  - Optional
```

## Risk management

_The ability of the TRE organisation to measure, forecast and evaluate risks to information._

```{list-table}
:header-rows: 1
:name: tab-risk-assessment

* - Statement
  - Guidance
  - Importance
* - You must have a way to score risk to understand the underlying severity.
  - You have a risk assesment methodology for scoring risks on multiple axes such as impact and likelihood.
  - Mandatory
* - You must have a process for mitigating risk using additional controls.
  - Risks can be reduced to a level which brings it within agreed levels of appetite.
  - Mandatory
* - You must have an understanding of risk appetite.
  - This includes understanding ownership of risk, and ability to accept risk which falls outside of the appetite should that become necessary.
  - Mandatory
* - You must carry out a data processing assessment for all projects requiring a TRE that are working with sensitive data.
  - A data processing assessment is a process designed to identify risks arising out of the processing of sensitive data and to minimise these risks as far and as early as possible.
  - Mandatory
```

## Project management

_The ability of the TRE organisation to manage projects effectively._

### Project onboarding

```{list-table}
:header-rows: 1
:name: tab-project-onboarding

* - Statement
  - Guidance
  - Importance
* - You must have checks in place to ensure a project has the legal, financial and ethical requirements in place for the duration of the project.
  - This includes checks that contracts are in place where required, adequate funding is available for the duration of the project, and responsibilities concerning data ownership are understood by all parties.
  - Mandatory
```

### Project closure

```{list-table}
:header-rows: 1
:name: tab-project-closure

* - Statement
  - Guidance
  - Importance
* - You must have standard processes in place for the end of a project, that follow all legal requirements and data security best practice.
  - This includes the archiving of quality and log data along with the archiving or deletion of data sets.
  - Mandatory
```

### Roles and responsibilities

```{list-table}
:header-rows: 1
:name: tab-roles-responsibilities
* - Statement
  - Guidance
  - Importance
* - You must have clearly defined roles and responsibilities for all operators and users of your TRE.
  - This may include roles such as users, system administrators, system operators or data providers.
    Every member of your TRE organisation should have at least one pre-defined role with clear powers and responsibilities.
  - Mandatory
```

## Member accreditation

_The ability of the TRE organisation to ensure that people with access to data are identified correctly, and they are suitably qualified._

### Onboarding members

```{list-table}
:header-rows: 1
:name: tab-onboarding-members

* - Statement
  - Guidance
  - Importance
* - You must have clear onboarding processes in place for all roles within your TRE organisation.
  - This may include all members signing role-specific terms of use, and completing role specific training.
  - Mandatory
* - You must have a robust method for identifying accredited members of your TRE organisation, prior to their accessing of sensitive data.
  - This may include multi-factor authentication (MFA), ID checks or email/phone verification.
  - Mandatory
```

### Training management and delivery

```{list-table}
:header-rows: 1
:name: tab-training-management-delivery

* - Statement
  - Guidance
  - Importance
* - You must have relevant training for all roles within the TRE organisation, and the ability to deliver this training.
  - This may include, for instance, cyber security training, GDPR training, and higher level training for system operators.
  - Mandatory
* - You must ensure that all users and operators of your TRE complete their training satisfactorily.
  - This may involve assessing their level of knowledge and repeating the training if necessary.
  - Mandatory
* - You should ensure that all users and operators of your TRE repeat their training regularly.
  - For instance, you may want everyone to have completed their training within the last 12 months.
  - Recommended
* - You must have a process in place to monitor all TRE organisation training completions and requirements.
  - This process should document which members have completed which training, when the training was completed, and the date the training expires.
    It should also document how you will notify members when their training is about to expire, and, if appropriate revoke access to the TRE.
  - Mandatory
```
