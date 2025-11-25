# Standard Architecture for Trusted Research Environments (SATRE)

```{toctree}
:hidden:
:caption: About SATRE

self
```

```{toctree}
:hidden:
:caption: Specification

The SATRE Specification <new-spec-test.md>
Evaluating against SATRE <evaluation.md>
SATRE Control Alignment <alignment.md>
Glossary <https://glossary.uktre.org/en/stable/>
```

```{toctree}
:hidden:
:caption: Architecture

Architecture Overview <architecture.md>
principles.md
roles.md
SATRE Architecture <https://satre-archimate.readthedocs.io/en/latest/?view=id-4349bc52159b48e9b785e9809a876c03>
```

```{toctree}
:hidden:
:caption: FAQs

faqs.md
```

(what_is_satre)=

## What is SATRE?

SATRE (Standard Architecture for Trusted Research Environments) is the UK's first open, community-led specification for Trusted Research Environments (TREs). Developed through extensive collaboration with over 60 organizations and informed by public engagement, SATRE provides a comprehensive framework for building, operating, and evaluating TREs across academia, healthcare, industry, and government.

TREs are secure computing environments specifically designed for research using sensitive or personal data. They enable researchers to access and analyse data safely while minimising the risk of data exposure or release. SATRE brings consistency and best practice to how these environments are designed, operated, and governed.

SATRE is built on four [guiding principles](principles.md): **Usability, Maintaining Public Trust, Observability, and Standardisation.** These principles ensure that TREs are not only secure and compliant but also accessible to researchers and trustworthy to the public.

### Introduction to the SATRE Project

```{raw} html
<div style="max-width: 640px; margin: 20px auto;">
  <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden;">
    <iframe src="https://www.youtube-nocookie.com/embed/auExNHEGwcc" 
            style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;" 
            frameborder="0" 
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
            allowfullscreen>
    </iframe>
  </div>
</div>
```

## Why SATRE Matters

Personal and sensitive data collected for operational, commercial, or governmental purposes hold immense value for research that benefits society. However, accessing this data requires robust security, governance, and ethical frameworks. Without standardization, TREs across the UK have developed independently, leading to:

- Inconsistent governance standards and security approaches
- Difficulty for researchers working across multiple TREs
- Challenges for data owners in understanding and trusting TRE operations
- Barriers to collaboration and data sharing between institutions
- Duplication of effort in developing TRE capabilities

## The SATRE Specification

The [SATRE specification](new-spec-test.md) defines 160 requirements organized into capabilities that TREs should implement to ensure safe, secure, and effective research with sensitive data. Each requirement is classified as either Mandatory or Optional, providing flexibility while maintaining essential standards.

The requirements are structured across four interconnected pillars.

### Four Pillars of SATRE

**1. [Information Governance](new-spec-test.md#information-governance)**
Quality management, risk management, training delivery, member accreditation, and governance procedures that ensure TREs operate safely and ethically.<br>
**2. [Computing Technology](new-spec-test.md#computing-technology-and-information-security)**
End-user computing experience, infrastructure management, information security, and configuration management for secure data analysis environments.<br>
**3. [Data Management](new-spec-test.md#data-management)**
Data lifecycle management, identity and access management, output management, information discovery, and research metadata capabilities.<br>
**4. [Supporting Capabilities](new-spec-test.md#supporting-capabilities)**
Financial management, public engagement and involvement, project management, procurement, and other essential operational functions.

## The SATRE Architecture

The [Architecture](architecture.md) provides a comprehensive high-level architecture for research organisations handling sensitive data. Required capabilities are documented along with the key roles, processes, data and applications that realise those capabilities. By providing this architecture, TRE designers and implementers will be able to identify additions and changes within their organisation to ensure sensitive data research can be conducted safely.

## Public Trust at the Core

SATRE embeds public involvement and engagement throughout its development and within the specification itself. Through workshops with members of the public, we identified that cybersecurity, oversight, transparency, and public involvement were essential for maintaining trust in TREs.

**Public Voice in Action**<br>
Two public members served on the core SATRE project team from the beginning, ensuring public perspectives shaped all work packages. Public workshop feedback directly led to:

- Upgrading Public Involvement and Engagement statements from Optional to Mandatory* for TREs using personal data
- Including requirements for TREs to publicly report on incidents and near-misses
- Adding detailed specifications on transparency and public-facing information
- Strengthening oversight and governance requirements

## Get Involved with SATRE

- [Contribute on GitHub](https://github.com/sa-tre/satre-specification)
- [Join the UK TRE Community](https://www.uktre.org/)

## Releases

```{list-table}
:header-rows: 1

* - Version
  - Release Date
  - Release Notes
* - [1.1.0](https://satre-archimate.readthedocs.io/en/v1.1.0/)
  - 2025-07-01
  - - Output Management added as capability as per specification.
    - Specification Statements added as requirements and linked to capabilities.
    - Added URL to specification statements in "documentation" where possible
    - Supporting Capabilities pillar aligned to specification.
    - Views created for all supporting capabilities.
    - All requirements added to views.
* - 1.0.0
  - 2023-10-05
  -
```

## Publications

- Ed Chalstrey, Jim Madge, James Robinson, Simon Li, Hari Sood, Arron Lacey, Matt Craddock, Tim Machin, Chris Cole, & Martin O'Reilly. (2025). sa-tre/satre-specification: Version 1.1.1 (v1.1.1). Zenodo. https://doi.org/10.5281/zenodo.17353472
- Simon, L. (2025, October 15). A standard architecture for TREs: why is it important in a federated world?. Health Data Research UK Conference 2025, Glasgow. Zenodo. https://doi.org/10.5281/zenodo.17305295
- Johnston, J., Sheane, S., Almond, E., Whiting, A., Higgins, D., Nadin, R., Hagen, J.-A., & Billins, T. (2025). SATRE Centric Control Alignment Table for Trusted Research Environments. TRE Community, Leeds. Zenodo. https://doi.org/10.5281/zenodo.16837077
- Machin, T., Chalstrey, E., Cole, C., Craddock, M., Hetherington, J., Li, S., Madge, J., O'Reilly, M., Robinson, J., Swanepoel, N., & Hari, S. (2023). A Standard Architecture for Trusted Research Environments (1.01). Zenodo. https://doi.org/10.5281/zenodo.10053383
- Katie Oldfield, Dr Christian Cole, Jillian Beggs, & Antony Chuter. (2023). SATRE Public Involvement and Engagement Final Report. Zenodo. https://doi.org/10.5281/zenodo.10084354
- Dr Christian Cole, Hari Sood, Dr Simon Li, Katie Oldfield, Matt Craddock, Nel Swanepoel, Professor Sonya Coleman, Dr Martin O'Reilly, Dr Dermot Kerr, Dr Cian O'Donovan, Professor James Hetherington, Dr Jim Madge, David Sarmiento-Perez, Ed Chalstrey, Dr James Robinson, Jillian Beggs, Tim Machin, & Antony Chuter. (2023). SATRE: Standardised Architecture for Trusted Research Environments. Zenodo. https://doi.org/10.5281/zenodo.10055345
- Li, S., Christian, C., O'Reilly, M., Jim, M., Craddock, M., Chalstrey, E., & Sarmiento-Perez, D. (2023, October 25). SATRE Evaluation workshop: Evaluating your TRE. Zenodo. https://doi.org/10.5281/zenodo.10040590
- Chalstrey, E., Cole, C., Coleman, S., Craddock, M., Hetherington, J., Kerr, D., Li, S., Madge, J., O'Donovan, C., Oldfield, K., O'Reilly, M., Sarmiento-Perez, D., Sood, H., & Swanepoel, N. (2023, April 18). SATRE – Standardised Architecture for Trusted Research Environments (Kick off). Zenodo. https://doi.org/10.5281/zenodo.7853186

## Acknowledgements

We are grateful for the following support for this project:

- UKRI via the DARE Phase 2 - TREvolution Programme [DARE Phase 2](https://dareuk.org.uk/news-and-events/dare-uk-phase-2-is-underway-but-what-does-this-mean-for-everyone/)
- UKRI via the DARE UK Phase 1 driver projects programme ([SATRE](https://dareuk.org.uk/how-we-work/previous-activities/dare-uk-phase-1-driver-projects/satre-standardised-architecture-for-trusted-research-environments/))

