# Standard Architecture for Trusted Research Environments (SATRE)

```{toctree}
:hidden:
:caption: Overview

specification.md
principles.md
roles.md
faqs.md
```

```{toctree}
:hidden:
:numbered: 2
:caption: Specification

pillars/information_governance.md
pillars/computing_technology.md
pillars/data_management.md
pillars/supporting.md
```

```{toctree}
:hidden:
:caption: Evaluation

evaluation.md
evaluations/alan_turing_institute.md
evaluations/dundee_hic.md
```

```{toctree}
:hidden:
:caption: Glossary

glossary.md
```

```{toctree}
:hidden:
:caption: Contributing

contributing/index.md
contributing/walkthrough.md
contributing/contributors.md
```

The SATRE project provides a Standard Architecture for {ref}`Trusted Research Environments (TREs) <what_tre>`, incorporating knowledge and best practices from multiple institutions and sectors across the UK.

It aims to standardise the capabilities of TREs, making it easier for users, operators, and developers to work with sensitive data, and making the operation of TREs more transparent to data owners and the general public.

We encourage all TREs in the UK to {ref}`evaluate <evaluation>` themselves against the SATRE specification, and to {ref}`contribute <contributing>` to the project.

## Getting started

If you are familiar with SATRE and want to evaluate your own TRE you can jump straight to the {ref}`evaluation section <evaluation>` which includes an {ref}`Excel spreadsheet <evaluate_spreadsheet>` you can use for your evaluation.

If this is your first time here we recommend reading the rest of this page to understand the background behind SATRE, followed by:

- {ref}`Frequently asked questions <faqs>`
- {ref}`The specification <specification>`
- {ref}`How to evaluate your TRE <evaluation>`

(what_is_satre)=

## 👀 What is SATRE?

The SATRE project aims to provide a Standard Architecture for {ref}`Trusted Research Environments (TREs) <what_tre>`.

The SATRE specification is our attempt to compile and document knowledge, best practices and capabilities around TRE building and operation from different institutions.
This includes all aspects of TRE provision such as information governance procedures, computing technology, data management and other capabilities.

SATRE should

- Enable the {ref}`Operators <infrastructure_roles>` of TREs to benefit from this knowledge, and empower them to improve their TREs with the suggested capabilities.
- Aid the {ref}`Developers and Builders <infrastructure_roles>` of new TREs in their thinking and decision making.

(satre_why)=

## ❓ Why are we doing this?

<!-- Motivation: Why a TRE specification is needed/ useful and a description of the broader SATRE project, conception and goals -->

The need for TREs is clear.
Personal or sensitive data which have been collected for operational, commercial or governmental reasons need to be managed securely and safely for research use in an environment that encourages best practice.

TREs are designed to enable access to sensitive data only for authorised projects and {ref}`data consumers <project_roles>`, whilst minimising risk of data release or exposure.
Influential reports from DARE UK and Health Data Research UK, together with the UK Government Goldacre review and ‘Data Saves Lives’ policy paper, have all highlighted the need for change in how sensitive data are handled.

The SATRE team contains representatives from several existing UK TREs, which host many different types of sensitive data.
We will use the reference architecture specified here to bring these into closer alignment and make it easy for others to do the same.
This supports DARE UK's aim of developing a coordinated national data research infrastructure.

## 👐 Contributing

We welcome contributions from anyone who is interested in the project.
There are lots of ways to contribute, not just writing code!
Find out more about how to {ref}`contribute to the SATRE Specification <contributing>`.

## 🙇 Acknowledgements

We are grateful for the following support for this project:

- UKRI via the DARE UK Phase 1 driver projects programme ([SATRE](https://dareuk.org.uk/driver-project-satre/))
