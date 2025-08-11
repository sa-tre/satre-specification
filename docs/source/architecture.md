(architecture)=

# SATRE Architecture

The current version of the architecture can be viewed [here](https://satre-archimate.readthedocs.io/).

This Standard Architecture for Trusted Research Environments (TREs) provides a comprehensive high-level architecture for research organisations handling sensitive data safely.

The architecture is documented using the [ArchiMate](https://pubs.opengroup.org/architecture/archimate3-doc/) modelling language with models created using the open source modelling tool [Archi](https://www.archimatetool.com/).

Capabilities an organisation requires to run a TRE are documented and deconstructed to show the elements (Roles, processes, applications and data) needed to realise those capabilities.

The architecture and SATRE standard maps to the architecture meta-model below.

```{figure} ../images/architecture-metamodel.jpg
:alt: SATRE Architecture meta-model
:align: center

SATRE Architecture meta-model
```

Views are provided aligned to the capabilities and additional views show alignment with external frameworks such as the [Five Safes](https://ukdataservice.ac.uk/help/secure-lab/what-is-the-five-safes-framework/).

The Archimate files are managed in the [Architecture Repository](https://github.com/sa-tre/satre-archimate).

A report on the architecture is available on [zenodo](https://zenodo.org/records/10053383).

## Versions

```{list-table}
:header-rows: 1
:name: tab-information-search-and-discovery

* - Version
  - Release Date
  - Release Notes
* - [1.1.0](https://satre-archimate.readthedocs.io/v1.1.0/)
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
