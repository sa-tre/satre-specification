# SATRE Specification Repository: Technical Document for the Standard Architecture for Trusted Research Environments Project

**[The specification is a living document hosted here on our GitHub pages site](https://sa-tre.github.io/satre-specification/)**. It can also be viewed here on GitHub at [docs/source/index.md](docs/source/index.md).

Welcome to the SATRE Specification Repository! 
This repository stores the technical documents that outlines a reference architecture for Trusted Research Environments.
***By October 2023*** we will aim to have drafted the document with input from members of the Systems Architecture, Research Software Engineering and Cyber Security community, with core support from DARE UK funded project members as part of a collaborative effort between the University of Dundee, Ulster University, UCL, Health Data Research UK, The Alan Turing Institute and Research Data Scotland.

If you have experience designing or using Trusted/Secure Research Environments and want to get involved in developing a reference architecture for UK TREs then please read on to find out how you can contribute.

## Overview of the SATRE Project
The need for trusted research environments (TREs) is clear. 
Personal or sensitive data which have been collected for operational, commercial or governmental reasons need to be managed securely and safely for research use in an environment that encourages best practice.
TREs are designed to enable access to sensitive data only for authorised projects and researchers, whilst minimising risk of data release or exposure. 
Influential reports from DARE UK and Health Data Research UK, together with the UK Government Goldacre review and ‘Data Saves Lives’ policy paper, have all highlighted the need for change in how sensitive data are handled.

SATRE will compare openly available UK TREs hosting health, manufacturing, commercial, science and humanities data and bring them into alignment with a standardised TRE reference architecture (or structural template). 
The development teams at the University of Dundee’s Health Informatics Centre and the Alan Turing Institute, fully supported by their infrastructure partners, will lead the reference alignment in collaboration with a consortium of higher education, charity and industry organisations.

The reference architecture and its implementation will be informed and strengthened by a programme of community building and engagement with DARE UK and partner working groups, other stakeholders and inclusive public representation.
SATRE outputs will include an informed TRE reference technical specification and a collection of educational media and detailed reports – all supporting DARE UK’s aim of a coordinated national data research infrastructure.

## Community-Driven Approach

[![Slack](https://img.shields.io/badge/Slack-Join%20Our%20Channel-blue?logo=slack)](https://ukrse.slack.com) #rse-tre-wg

The SATRE project values the importance of equity, diversity, and inclusion (EDI) in fostering a kind and supportive environment for all participants.
We are committed to making the project as inclusive as possible and appreciate the unique perspectives and input that each community member brings.

While there are core members funded by DARE to contribute to this project, our primary goal is to involve as many members of the community as possible.
We strongly believe that the best results come from collaboration, diverse perspectives, and fostering a culture of kindness and mutual respect.

## Getting Started
There are a number of ways you can get involved with the SATRE project!

1. **Collaborate with us**: We are running a number of collaborative sessions for the duration of the project you can get involved with!

| Meeting | Description | Time | Link
|----------|----------|----------|----------|
| Bi-weekly Collaboration Cafe  | An open meeting for anyone interested in discussing & contributing to the project to work collaboratively with the team, community and others  | Every 1st Tuesday and 3rd Thursday of the month |[HackMD link please fill]()|
| Monthly Open Roadmap Review  | During the Thursday Collaboration Cafe, the core funded team will provide updates to the Open Roadmap based on community contributions  | Every 3rd Thursday of the month  |[HackMD link please fill]()|


2. **Contribute**: Review open issues, join SATRE meetings, and provide your input on the design, implementation, and best practices for TREs. To contribute to the project, please join discussions on open issues to help guide content for the documentation. 
If you have a specific idea or proposal, feel free to open a new issue or start a GitHub Discussions thread.
Currently we are writing documentation in `.md` files and will decide on a more refined documentation format with the Community.
3. **Sign up to our contact list**: You can sign up by filling in [this short form](https://forms.office.com/e/FuFyNGx3hw). 
Sign up for updates about the project, further invitations to workshops & roundtables, and opportunities for feedback & knowledge sharing :sparkles:

4. **Join the RSE TRE community**: The RSE TRE community was established at RSE Con in September 2022, and brings together those building, using, operating and generally affected by and interested in TREs together to solve common challenges and share knowledge. You can register for the JISC mailing list [by following this link](https://www.jiscmail.ac.uk/cgi-bin/wa-jisc.exe?SUBED1=RSE-TRE-COMM&A=1)
## Code of Conduct and Inclusivity
The SATRE project is committed to fostering an inclusive, equitable, and respectful environment for all participants. 
Please review our [Code of Conduct](CODE_OF_CONDUCT.md) to ensure that your interactions with the community align with our values and expectations.
We encourage everyone to contribute to creating a kind and supportive atmosphere, appreciating each community member's input.

## License
The content of this repository is licensed under the [Creative Commons License](LICENSE.md).

## Contact
For any questions or concerns, please reach out to SATRE project team member [Hari Sood](mailto:hsood@turing.ac.uk).

We look forward to your participation and contributions to the SATRE project, as we work together to build a standard architecture for Trusted Research Environments in an inclusive and supportive environment!

## Sphinx docs build
Build the document locally with:
1. Ensure you have a working Python 3 installation
2. Install Sphinx: `pip install sphinx myst-parser`
3. Clone this repo: `git clone https://github.com/sa-tre/satre-specification`
4. From inside the repo run `sphinx-build -b html docs/source/ docs/build/html`
5. Open the generated html files at `docs/build/html` in a browser
