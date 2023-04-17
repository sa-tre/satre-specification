Standard Architecture for Trusted Research Environments (TREs)
==============================================================

```{toctree}
contributors.md
```

## Introduction

### Trusted Research Environments

What are they, how many exist, the broad categories

### About the authors

Our respective development and use of TREs, with brief descriptions of the three examples

### A Standard Architecture for TREs

Motivation: Why a TRE standard is needed/ useful and a description of the broader SATRE project, conception and goals

### Standard aims

What this document intends to do (and what it doesn't), the level of detail we aim for contrasted with other technical standards

## Required TRE features

> Crowdsourced list of functionality from TRE developers survey that were considered the most important/ <u>essential components in order to define a software as a TRE</u>. Each of these should be described in prose and where appropriate examples of these features present in existing TRE implementations provided. Where features vary across existing TREs this should be highlighted.

### Feature A
### Feature B
## Optional TRE features

Also croudsourced from the survey, but this time all the features that were considered less important and/or are not needed in order to simply define something as a TRE (for example this might include something like HPC-connectability).

### Feature X
### Feature Y

## Roles

A TRE conforming to the SATRE standard should provide a broadly similar experience for stakeholders operating in each of these defined roles.

### TRE users

The researchers working on projects that involve logging into a TRE to access data. The document will explain that user experience of the platform and associated documentation should feel similar across TREs conforming to SATRE standard.

### TRE admins

The IT or software engineering professionals who will be responsible for deploying and managing instances of a TRE conforming to the SATRE standard. The document will explain that SATRE conforming TREs should have documentation and infrastructure deployment code/apps that conform to software engineering best practices, which are also defined here, making them "simple" for an IT professional to follow; troubleshooting steps included.

### TRE developers

The software engineers responsible for developing and maintaining TRE software, including adding functionality, bug fixes and general maintenance. The document will explain recommended practices suitable for developing a software of this complexity and reference learnings from existing TRE developers.

### TRE Governance roles

Roles that uphold the governance of TREs. Such governance responsibilities typically involve establishing policies and procedures to ensure the responsible use of data, protecting the privacy and confidentiality of research participants, and promoting transparency and accountability in research activities. Typical roles might include data custodians, ethicists, an independent board or a lay panel.

## Architecture

Includes nice diagrams of how the TRE features connect together, but remains a high level description that doesn't specify which exact technologies a TRE developer should use. This can also offer an explanation of how people from different roles interact/experience these features.
## Conclusion

Benefits of adopting this standard for developing a TRE. Benefits of existing TRE efforts working to conform to this standard (users and admin roles as well as developers).