(contributing)=

# ✨ Contributing to the SATRE Specification

🎉 **Welcome to the SATRE specification!** 🎉

_We're excited that you want to contribute_ 🚀

We want to ensure that every user and contributor feels welcome, included and supported to participate in the SATRE project and community.
We hope that the information provided in this document will make it as easy as possible for you to get involved.

We welcome contributions to this project via GitHub issues and pull requests.
Please follow these guidelines to make sure your contributions can be easily integrated into the project.
As you start contributing don't forget that your ideas are more important than perfectly formatted contributions :heart:.

If you have any questions that aren't discussed below, please let us know through one of the many ways to [get in touch](contributing-get-in-touch).

[**Jump straight to our contribution walkthrough**](walkthrough.md)

## Code of Conduct

SATRE is a community-led and collaboratively-developed project.
Therefore, we require that all our contributors and their contributions **adhere to our [Code of Conduct](https://github.com/sa-tre/satre-specification/blob/main/CODE_OF_CONDUCT.md) (CoC)**.
Please familiarise yourself with our [CoC](https://github.com/sa-tre/satre-specification/blob/main/CODE_OF_CONDUCT.md) and ensure your contributions and engagement with this project follow it!

## Contributing through GitHub

[Git](https://git-scm.com/) is a really useful tool for version control.
[GitHub](https://github.com/) sits on top of Git and supports collaborative and distributed working.

We know that it can be daunting to start using Git and GitHub if you haven't worked with them in the past.
We are here to help you figure out any of the jargon or confusing instructions you encounter ❤️!

In order to contribute via GitHub, you'll need to set up a free account and sign in.
Here are some [instructions](https://docs.github.com/articles/signing-up-for-a-new-github-account/) to help you get going.
Remember that you can ask us any questions you need to along the way.

## Contribution Model

We have designed our contribution model to be as accessible as possible, while utilising the full power of GitHub's collaboration and version-control tools.

This specification, including its governance procedures and contribution models, are open for the community to evaluate, challenge, amend and discuss.
If you have improvements we can make to anything we are doing, please suggest them!

The community can suggest any amendments to the specification at any point.
If you see a part of the specification you don't like, open an issue about it and start a conversation with the community ✨.

:::{important}
We are in a bootstrapping phase to get an initial specification written.
As part of this initial work we will propose a more formal governance model for the specification going forwards.

We have chosen to keep all discussion to issues for now, so contributors have a single place to engage in conversation.
Pull requests are used when a specific change is ready to be proposed.
This can be without discussion, however, it is best for substantial or significant changes to be discussed first in an issue.
We have opted to not use GitHub Discussions at this point.

The community can suggest governance changes at any point.
This includes the SATRE team, and any decision must be openly documented in the repo.
:::

### Specification Format

The specification source is kept in the [specification repository](https://github.com/sa-tre/satre-specification).
It is written as a [Sphinx](https://www.sphinx-doc.org/) document in [Markdown](https://www.markdownguide.org/) format.

The most up-to-date 'source of truth' will be the specification on the `main` branch of the specification repository.
The community can decide when to 'tag' a new version of the specification.
They may also decide to where to publish the specification.

The specification repository is self-contained and relates only to the specification specifically, or its governance.
Any contributions to the wider SATRE project should be made through a different medium via the [SATRE GitHub organisation](https://github.com/sa-tre), or by contacting the SATRE team at [satre-contact@dundee.ac.uk](mailto:satre-contact@dundee.ac.uk).

(contributing-contribution-process)=

### Contribution Process

Issues should be used to discuss ideas, potential changes and to ask questions.
Issue templates have been designed for common issue types to help collect the most important information and present it in a clear, consistent way.
It is possible, however, to open a blank issue if none of the templates are suitable.

While we encourage opening issues, we understand that some may be more comfortable contributing ideas in other ways such as through discussions and notes at SATRE Collaboration Cafés.
The SATRE Team will aim to collate ideas and draft issues that welcome further discussion and attribute those involved in initial discussions.
The SATRE Team will try to capture the ideas as accurately as possible, in good faith, and be guided by the SATRE Community to correct any misconceptions.

When ready, changes will be proposed in pull requests.
Similarly to issues, there is a pull request template.
This template prompts contributors to include important details which helps explain the contribution and makes triage and review easier.

Pull requests will be used to review changes.
During the review process, the pull request will be used for discussion, to suggest amendments and ultimately accept or reject the change.

We use this process to ensure that as much as possible of the discussion and decision making process can be public.
This is to provide as open and accessible as possible an environment for all contributors to engage in the conversation.

### Consensus Mechanism

Approval from the SATRE team is based on [lazy consensus](https://medlabboulder.gitlab.io/democraticmediums/mediums/lazy_consensus/).
After a pull request has been open for at least 7 days, unless there are outstanding objections, the change will be presumed as accepted.
SATRE team members are then free to merge the pull request at any point.

If any of the SATRE team objects to a particular issue, this will be raised by individuals using [pull request reviews](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests/about-pull-request-reviews).
The SATRE team will only merge pull requests that have no outstanding objections.

## Writing in Markdown

The [Myst Parser](https://myst-parser.readthedocs.io/en/stable/syntax/typography.html) documentation has a guide on the Markdown format used in the specification source files.
GitHub also has a helpful page on [getting started with writing and formatting on GitHub](https://docs.github.com/articles/getting-started-with-writing-and-formatting-on-github), which will be useful when writing Markdown for GitHub (for example in issue or pull request comments).

You can think of Markdown as a few little symbols around your text that instruct how to render the text.
For example, you could write words in **bold** (`**bold**`), in _italics_ (`_italics_`), or as a [link](https://medium.com/satre) (`[link](https://medium.com/satre)`) to another web page.

Also when writing in Markdown, please [start each new sentence on a new line](https://sembr.org/).
Having each sentence on a new line will make no difference to how the text is displayed.
A blank line is needed to start a new paragraph.
However, it makes the source and [diffs produced during the pull request](https://docs.github.com/en/articles/about-comparing-branches-in-pull-requests) review easier to read ✨!

### Linting and auto-formatting

We take advantage of pre-commit and related tools to help maintain consistent formatting within a repo, which improves review efficiency, and readability.
`pre-commit can be installed using pip:

```sh
pip install pre-commit
```

When you make some changes, you should run

```sh
pre-commit run -a
```

before committing any changes.
See the [pre-commit](https://pre-commit.com/) documentation for more advanced usage, including automatically running it as part of a commit.

## SATRE Team Contributions

SATRE team members are free to contribute to the repo in the same way as any contributor, following the process above.
The SATRE team is also doing ongoing work to identify the key features of this specification.
Some contributions by SATRE team members may represent the output of this work.
Any contribution that represents this work will be explicitly mentioned in the contribution.

This work is taking on two main forms:

1. Identifying what features the community feels are important for a TRE via the [features survey](https://dundee.onlinesurveys.ac.uk/satre-tre-operatorsbuilders-survey).
   We will synthesise responses from this survey to suggest features here.
1. Evaluating the TREs used in production as part of [the Alan Turing Institute DSH](https://github.com/alan-turing-institute/data-safe-haven), [Microsoft's Azure TRE](https://github.com/microsoft/AzureTRE), and the [TREEHOOSE TRE](https://github.com/HicResearch/TREEHOOSE/tree/v1.0.0-beta1).
   The SATRE team will make recommendations for features of the specification based on similarities/differences across these three TRE provisions.

(contributing-get-in-touch)=

## Get in touch

To get in touch with the SATRE team, please email [satre-contact@dundee.ac.uk](mailto:satre-contact@dundee.ac.uk).

To report Code-of-Conduct violations, please use the contact [specified in the Code of Conduct](https://github.com/sa-tre/satre-specification/blob/main/CODE_OF_CONDUCT.md).

## Recognising Contributions

We welcome and recognise all kinds of contributions, from discussing ideas, suggesting features, improving governance, maintaining the project, and more.

This project follows the [All Contributors specification](https://allcontributors.org/docs/en/overview).
The All Contributors bot usage is described [here](https://allcontributors.org/docs/en/bot/usage).

To add yourself or someone else as a contributor, comment on the relevant Issue or Pull Request with the following:

```text
@all-contributors please add <username> for <contributions>
```

You can see the [Emoji Key (Contribution Types Reference)](https://allcontributors.org/docs/en/emoji-key) for a list of valid `<contribution>` types.
The bot will then create a Pull Request to add the contributor and reply with the pull request details.

:::{hint}
**Please only add one contributor with the bot at a time!**

It is best to add each contributor in turn and merge the pull request before adding another one.
Otherwise, you can end up with merge conflicts.
Please check the open pull requests first to make sure there aren't any [open requests from the bot](https://github.com/sa-tre/satre-specification/pulls/app%2Fallcontributors) before adding another.

What happens if you accidentally run the bot before the previous run was merged and you got those pesky merge conflicts?
(Don't feel bad, we have all done it! 🙈)
Simply close the pull request and delete the branch (`all-contributors/add-<username>`).
If you are unable to do this for any reason, please let us know by opening an issue, and SATRE team members will be very happy to help!
:::
