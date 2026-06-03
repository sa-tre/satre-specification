# SATRE Specification Repository

**[View the SATRE Specification on Read the Docs](https://satre-specification.readthedocs.io/en/latest/)**

This repository contains the source files for the SATRE (Standard Architecture for Trusted Research Environments) specification documentation, built with Sphinx and hosted on Read the Docs.

## About SATRE

SATRE is the UK's first open, community-led specification for Trusted Research Environments (TREs). Developed through extensive collaboration with over 60 organisations and informed by public engagement, SATRE provides a comprehensive framework for building, operating, and evaluating TREs across academia, healthcare, industry, and government.

## Contributing

We welcome contributions from the community! There are several ways to get involved:

### Report an Issue

The easiest way to contribute is to [log an issue](https://github.com/sa-tre/satre-specification/issues/new) on GitHub. Your issue will be:

- Reviewed by the SATRE team
- Shared with the community for discussion
- Addressed in future updates to the specification

### Contact the Team

You can also reach out directly to any of our [technical contacts](#technical-contacts) with questions, suggestions, or proposals.

### Other Ways to Contribute

- [Join the UKTRE Community](https://www.uktre.org/en/latest/background/index.html)

## Key Features

### Dynamic Specification Tables

The specification is generated from `docs/source/spec/specification.yaml` using a custom Sphinx extension (`yamlspec.py`). The specification is organized into four pillars:

- Information governance
- Computing technology and Information Security
- Data management
- Supporting capabilities
- Federation (extension for federated TREs)

## Building the Documentation Locally

### Prerequisites

- Python 3.11+
- pip

### Installation

1. Clone the repository:

```bash
git clone https://github.com/sa-tre/satre-specification.git
cd satre-specification
```

2. Install dependencies:

```bash
cd docs
pip install -r requirements.txt
```

3. Build the documentation:

```bash
make html
```

4. View the built documentation:

```bash
# Open docs/build/html/index.html in your browser
```

## Updating the Specification

To update the specification content:

1. Edit the YAML specification file: `docs/source/spec/specification.yaml`
2. Rebuild the documentation

## Community

- **Slack**: [Join the RSE TRE Working Group](https://ukrse.slack.com/archives/rse-tre-wg)
- **Mailing List**: [RSE TRE Community](https://www.jiscmail.ac.uk/cgi-bin/wa-jisc.exe?SUBED1=RSE-TRE-COMM&A=1)
- **Contact List**: [Sign up for updates](https://forms.office.com/e/FuFyNGx3hw)

## Code of Conduct

The SATRE project is committed to fostering an inclusive, equitable, and respectful environment for all participants. Please review our [Code of Conduct](CODE_OF_CONDUCT.md).

## License

The content of this repository is licensed under the [Creative Commons License](LICENSE.md).

## Technical Contacts

For technical questions about this repository:

- **Tim Machin** - [@machintim](https://github.com/machintim)
- **Simon Li** - [@manics](https://github.com/manics)
- **Chris Cole** - [@drchriscole](https://github.com/drchriscole)
- **Rob Baxter** - [@rmbaxter67](https://github.com/rmbaxter67)

## Acknowledgements

This project is supported by UKRI via the DARE UK Phase 1 driver projects programme. We are grateful to all [DARE Phase 1 contributors](CONTRIBUTORS.md) who have helped develop the SATRE specification.
