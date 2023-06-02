(standard)=

# A Standard Architecture for TREs

<!-- What this document intends to do (and what it doesn't), the level of detail we aim for contrasted with other technical standards -->

The SATRE standard has been developed based on the following principles:

- TREs should be as as easy as possible for end-users to use (_e.g._ researchers) whilst still remaining secure.
- TRE deployments should be offered that support data of different levels of sensitivity (_e.g._ through a tiered system of technical controls and policies).
- TREs conforming to the standard should be interoperable and provide a familiar end-user experience.
- The standard will be managed and updated following an open, community-driven process, and will not be tied to a single vendor or implementation.

The SATRE standard is based around the idea of capabilities, some of which are required and some of which are optional.
Any particular TRE implementation should be able to score itself against each capability as either "supported", "partially supported" or "unsupported" (see {ref}`evaluation` for details).
The capabilities are grouped into the following broad categories:

- information governance
- computing technology
- data management
- information security

In addition to these capabilities, any organisation running a TRE will need to consider:

- legal requirements — particularly around data protection and contract management
- relationship management — engagement with internal and external stakeholders as well as the wider public

<!-- ## Required TRE features

> Crowdsourced list of functionality from TRE developers survey that were considered the most important/ <u>essential components in order to define a software as a TRE</u>. Each of these should be described in prose and where appropriate examples of these features present in existing TRE implementations provided. Where features vary across existing TREs this should be highlighted. -->

<!-- ### Feature A
### Feature B
## Optional TRE features

Also crowdsourced from the survey, but this time all the features that were considered less important and/or are not needed in order to simply define something as a TRE (for example this might include something like HPC-connectability).

### Feature X
### Feature Y -->

## TRE capabilities

There might be good reasons why any particular TRE does not possess one or more of the capabilities listed in this specification, but we think all TREs should aspire to meet them in the long-term.

### Information governance

#### Compliance, monitoring and reporting

#### Policy regulation and management

#### Quality management

- Internal audit and reporting

#### Risk management

#### Project and study management

#### Researcher accreditation

- Training management
- Training delivery

### Computing technology

#### End user computing

- User interface (eg. terminal, desktop, notebook, webapp etc.)
- Software tools

#### Compute beyond the desktop

- High performance computing
- Accelerators (GPU, FPGA, ASIC, xPU)
- Cluster computing (SLURM, Kubernetes etc.)
- Databases (both SQL and noSQL)

#### Data analytics

#### Network management

#### Application lifecycle management

#### Infrastructure lifecycle management

- Capacity management
- Deployment management
- Configuration management

### Data management

#### Data lifecycle management

#### Identity and access management

#### Management of outputs

#### Recording available datasets

## 4. Information security

A TRE conforming to the SATRE standard should enact broadly similar measures to protect against the unauthorized use of information, especially electronic data. This should include, measures taken to manage vulnerabilities of infrastructure (whether physical or virtual/cloud-based) and carry out compliance checks, measures to test the security of the TRE, common approaches to data encryption, common approaches to administrative control over data movement and (where appropriate) physical security measures to prevent unauthorised access to the TRE .

### 4.1 Vulnerability management

The ability of the organisation to identify, assess, report on, manage and remediate cyber vulnerabilities across endpoints, workloads, and systems.

| Statement | Guidance |
| --------- | -------- |
| TRE undergoes compliance checking of machine and resource configurations to ensure adherence to security standards and best practices | This should be done in advance of any sensitive data being uploaded to the environment. Adhering to the highest level of security standards suggested by the IT department of the TRE operators organisation will reduce the risk of security breaches and data leakage.  |
| Regular vulnerability scans of infrastructure should be conducted, so that TRE operators can identify and address weaknesses that may have been introduced during the TRE's operational lifetime | Ensuring that scans are done on a regular basis can enable proactive mitigation measures to be implemented promptly. One way this can be achived is by ensuring that all machines (whether physical or virtual/cloud-based) are set to check for operating system updates on a regular basis, and install any security patches pushed by the developers of those operating systems.

### 4.2 Security testing

The ability of the organisation to gain assurance in the security of an IT system by testing or attempting to breach some or all of that system's security.

### 4.3 Encryption

The ability of the organisation to deploy and manage encryption to protect information assets, including data for TRE research projects.

| Statement | Guidance |
| --------- | -------- |
| Use encryption algorithms for data | Encryption can be seen as an extra layer of protection for sensitive data already protected by security controls of a TRE. For particularly sensitive data, the most up to date industry standards for encryption should be used.
| Secure key management | TREs should employ secure key management practices, including storing encryption keys separately from the encrypted data and implementing strong access controls for key management systems. For example, you could use a cloud-based solution such as Azure Key Vault.
| Encrypt data at rest | Encrypt sensitive data when it is stored on storage devices such as databases, file systems, or cloud storage. This prevents unauthorized access to the data even if the storage media is compromised.
| Encrypt data in transit | TRE architectures that are built such that data gets transmitted over networks (between machines), should ensure data is encrypted in transit. This safeguards the data from interception or tampering during transmission.
| Keep encryption software updated | Ensure the latest security patches and updates are applied to enctyption being used by the TRE. This helps address any known vulnerabilities or weaknesses in the encryption implementation.

### 4.4 Physical security

The ability of the organisation to manage and protect physical assets from unauthorised access, damage or destruction. Physical security controls can provide TREs using highly sensitive data an extra layer of security, even if technical controls are already in place for less sensitive data:

| Statement | Guidance |
| --------- | -------- |
| Protection against data theft via physical means | Restricting access to research facilities containing computers logged into TREs can help prevent malicious actors from viewing or stealing sensitive data, for example by photographing a computer screen.
| Physical access controls | Physical controls on access to a TRE could include surveillance systems, restricting access to locked rooms that limit entry to authorized personnel only, visitor management systems and employee training.
| Compliance with regulatory requirements | Many regulatory frameworks, such as GDPR, emphasize the need for physical security controls to protect sensitive data. Compliance with these regulations often requires organizations to implement specific physical security measures to safeguard sensitive data properly.

## Roles

A TRE conforming to the SATRE standard should provide a broadly similar experience for stakeholders operating in each of these defined roles.
There is not necessarily a one-to-one mapping between roles and people.
One person can have multiple roles.

### TRE users

The researchers working on projects that involve logging into a TRE to access data.
The document will explain that user experience of the platform and associated documentation should feel similar across TREs conforming to SATRE standard.

### TRE administration roles

The IT and related professionals who will be responsible for deploying and managing instances of a TRE conforming to the SATRE standard.
The document will explain that SATRE conforming TREs should have documentation and infrastructure deployment code/apps that conform to software engineering best practices, which are also defined here, making them "simple" for an IT professional to follow; troubleshooting steps included.

These roles cover managing TRE computing infrastructure, but also administering the TRE itself (e.g. managing users and projects).

### TRE developer roles

The software engineers responsible for developing and maintaining TRE software, including adding functionality, bug fixes and general maintenance.
The document will explain recommended practices suitable for developing a software of this complexity and reference learnings from existing TRE developers.

### TRE governance roles

Roles that uphold the governance of TREs.
Such governance responsibilities typically involve establishing policies and procedures to ensure the responsible use of data, protecting the privacy and confidentiality of research participants, and promoting transparency and accountability in research activities.
Typical roles might include data custodians, ethicists, an independent board or a lay panel.

## Architecture

Includes diagrams of how the TRE features connect together, but remains a high level description that doesn't specify which exact technologies a TRE developer should use.
This can also offer an explanation of how people from different roles interact/experience these features.

## Conclusion

Benefits of adopting this standard for developing a TRE. 
Benefits of existing TRE efforts working to conform to this standard (users and admin roles as well as developers).
