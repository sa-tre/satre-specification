# Standard Architecture for Trusted Research Environments (SATRE)

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
SATRE Architecture <https://satre-archimate.readthedocs.io/en/latest/?view=id-4349bc52159b48e9b785e9809a876c03>
principles.md
roles.md
```

```{toctree}
:hidden:
:caption: FAQs <faqs.md>

```

(what_is_satre)=

## 👀 What is SATRE?

The SATRE project provides a Standard Architecture for {ref}`Trusted Research Environments (TREs) <what_tre>`.
It incorporates knowledge and best practices from multiple institutions and sectors across the UK.
This includes all aspects of TRE provision such as information governance procedures, computing technology, data management and other capabilities.

It aims to standardise the capabilities of TREs, making it easier for users, operators, and developers to work with sensitive data, and making the operation of TREs more transparent to data owners and the general public.

This specification should be useful if you are:

- a {ref}`TRE Operator <infrastructure_roles>` wanting to evaluate or improve their TRE with the suggested capabilities
- a {ref}`Developer or Builder <infrastructure_roles>` of new TREs looking for guidance in their thinking and decision making

We encourage all TREs in the UK to {ref}`evaluate <evaluation>` themselves against the SATRE specification, and to {ref}`contribute <contributing>` to the project.

## Getting started

If you are familiar with SATRE and want to evaluate your own TRE you can jump straight to the {ref}`evaluation section <evaluation>` which includes an {ref}`Excel spreadsheet <evaluate_spreadsheet>` you can use for your evaluation.

If this is your first time here we recommend reading the rest of this page to understand the background behind SATRE, followed by:

- {ref}`Frequently asked questions <faqs>`
- {ref}`The specification <specification>`
- {ref}`How to evaluate your TRE <evaluation>`

(satre_why)=

## ❓ Why do we need TREs?

Personal or sensitive data which have been collected for operational, commercial or governmental reasons need to be managed securely and safely.
A TRE enables researchers to access the data in a secure environment following best practice.
This should ensure that research projects and {ref}`data consumers <project_roles>` are properly authorised and that researchers only access the data they need, whilst minimising risk of data release or exposure.

## ❓ Why are we doing this now?

<!-- Motivation: Why a TRE specification is needed/ useful and a description of the broader SATRE project, conception and goals -->

The need for trusted research environments (TREs) is clear.
Influential reports including the UK Government's [Goldacre review](https://www.gov.uk/government/publications/better-broader-safer-using-health-data-for-research-and-analysis) and [‘Data Saves Lives’](https://www.gov.uk/government/publications/data-saves-lives-reshaping-health-and-social-care-with-data/data-saves-lives-reshaping-health-and-social-care-with-data) policy paper, have highlighted the need for change in how sensitive data are handled.
These papers set out a vision for the potential impact of research enabled by TREs.

At present operators have to interpret a range of frameworks, legislation and guidance when building and running a TRE.
These include:

- [Office for National Statistics: 5 Safes](https://blog.ons.gov.uk/2017/01/27/the-five-safes-data-privacy-at-ons/)
- [UK Health Data Research Alliance: TRE Green Paper](https://zenodo.org/records/4594704)
- [UK Health Data Research Alliance: TRE Principles and Best Practices](https://zenodo.org/records/5767586)
- [Design choices for productive, secure, data-intensive research at scale in the cloud](https://arxiv.org/abs/1908.08737)
- [ISO27001](https://www.iso.org/standard/27001)
- [Digital Economy Act](https://www.legislation.gov.uk/ukpga/2017/30/contents/enacted)
- [Handbook on Statistical Disclosure Control for Outputs](https://ukdataservice.ac.uk/app/uploads/sdc-handbook-v2.0.pdf)

This makes for inconsistent governance standards and makes it hard for researchers to work consistently in different environments.

A common specification for TREs will improve governance and practice across the sector, simplify researcher and operator journeys.
Furthermore, it will lay a foundation for interoperability that is required to maximise the impact of research by providing a trusted ecosystem for working with currently disparate and siloed data.

## ❓ Who are we?

The SATRE team contains representatives from several existing UK TREs, which host many different types of sensitive data.
We will use the reference architecture specified here to bring these into closer alignment and make it easy for others to do the same.
This supports DARE UK's aim of developing a coordinated national data research infrastructure.

## 👐 Contributing

We welcome contributions from anyone who is interested in the project.
There are lots of ways to contribute, not just writing code!
Find out more about how to {ref}`contribute to the SATRE Specification <contributing>`.

## 🙇 Acknowledgements

We are grateful for the following support for this project:

- UKRI via the DARE UK Phase 1 driver projects programme ([SATRE](https://dareuk.org.uk/how-we-work/previous-activities/dare-uk-phase-1-driver-projects/satre-standardised-architecture-for-trusted-research-environments/))
