# ✨ Contributing to the SATRE Specification

🎉  **Welcome to the SATRE specification!** 🎉

_We're excited that you want to contribute_ 🚀

[**Jump straight to contribution process**](#contribution-process)

We want to ensure that every user and contributor feels welcome, included and supported to participate in the SATRE project and community.
We hope that the information provided in this document will make it as easy as possible for you to get involved.

We welcome contributions to this project via GitHub issues and pull requests.
Please follow these guidelines to make sure your contributions can be easily integrated into the project.
As you start contributing don't forget that your ideas are more important than perfectly formatted contributions ❤️.

If you have any questions that aren't discussed below, please let us know through one of the many ways to [get in touch](#get-in-touch).

## Code of Conduct

SATRE is a community-led and collaboratively-developed project.
Therefore, we require that all our contributors and their contributions **adhere to our [Code of Conduct](https://github.com/sa-tre/satre-specification/blob/main/CODE_OF_CONDUCT.md) (CoC)**.
Please familiarise yourself with our [CoC](https://github.com/sa-tre/satre-specification/blob/main/CODE_OF_CONDUCT.md) and ensure your contributions and engagement with this project follow it!

## Contributing Through GitHub

[Git](https://git-scm.com/) is a really useful tool for version control.
[GitHub](https://github.com/) sits on top of Git and supports collaborative and distributed working.

We know that it can be daunting to start using Git and GitHub if you haven't worked with them in the past. We are here to help you figure out any of the jargon or confusing instructions you encounter❤️!

In order to contribute via GitHub, you'll need to set up a free account and sign in.
Here are some [instructions](https://help.github.com/articles/signing-up-for-a-new-github-account/) to help you get going.
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

### Contribution Process

All contributions and discussions will take place in issues - including the drafting of content.
This is to provide as accessible as possible an environment for all contributors to engage in the conversation.

To contribute to the project:

1. Open an issue on this repo. If your issue is for a discussion, add a `discussion point` label. If it is for a proposed change to the repo, add a `proposed change` label and provide wording for the proposed change. If it is for a governance discussion or change, add a `governance` label.
1. Have a discussion with the community within the issue comments. All issues will be left open for a minimum of 7 days to allow community members to engage if they want to.
1. If your issue is a proposed change, amend the wording of the contribution as required.
1. Once the final wording is ready for review,  add the label `request review`.
1. The issue will be reviewed at the next regular SATRE meeting by the SATRE team. Approval requires a simply majority, with at least 3 votes.
1. If the issue is not approved, the SATRE team will provide reasons why in the comments of the issue.
1. If the issue is approved, the label `approved change` will be added by the SATRE team, along with a comment updating the contributors/community that engaged with the issue.
1. The Pull Request (PR) is built (either by the contributor or by the SATRE team) with the wording as finalised in the issue
1. The PR is merged, and the issue is closed.

### Consensus Mechanism

Approval from the SATRE team is based on [lazy consensus](https://medlabboulder.gitlab.io/democraticmediums/mediums/lazy_consensus/).
Once a pull request has been open for 7 days, unless there are outstanding objections within the comments, the SATRE team will approve the change.
If any of the SATRE team objects to a particular issue, this will be raised by individuals in the comments of the pull request.
The SATRE team will only approve pull requests that have no outstanding objections.

## Writing in Markdown

The [Myst Parser](inv:myst-parser:std:doc#syntax/typography) documentation has a guide on the Markdown format used in the specification source files.
GitHub also has a helpful page on [getting started with writing and formatting on GitHub](https://help.github.com/articles/getting-started-with-writing-and-formatting-on-github), which will be useful when writing Markdown for GitHub (for example in issue or pull request comments).

You can think of Markdown as a few little symbols around your text that instruct how to render the text.
For example, you could write words in **bold** (`**bold**`), in _italics_ (`_italics_`), or as a [link](https://youtu.be/dQw4w9WgXcQ) (`[link](https://youtu.be/dQw4w9WgXcQ)`) to another web page.

Also when writing in Markdown, please [start each new sentence on a new line](https://sembr.org/).
Having each sentence on a new line will make no difference to how the text is displayed.
A blank line is needed to start a new paragraph.
However, it makes the source and [diffs produced during the pull request](https://help.github.com/en/articles/about-comparing-branches-in-pull-requests) review easier to read ✨!

## SATRE Team Contributions

SATRE team members are free to contribute to the repo in the same way as any contributor, following the process above.
The SATRE team is also doing ongoing work to identify the key features of this specification.
Some contributions by SATRE team members may represent the output of this work.
Any contribution that represents this work will be explicitly mentioned in the contribution.

This work is taking on two main forms:

1. Identifying what features the community feels are important for a TRE via the [features survey](https://dundee.onlinesurveys.ac.uk/satre-tre-operatorsbuilders-survey).
   We will synthesise responses from this survey to suggest features here.
1. Evaluating the TREs used in production as part of [the Alan Turing Institute DSH](https://github.com/alan-turing-institute/data-safe-haven),  [Microsoft's Azure TRE](https://github.com/microsoft/AzureTRE), and the [TREEHOOSE TRE](https://github.com/HicResearch/TREEHOOSE/tree/v1.0.0-beta1).
   The SATRE team will make recommendations for features of the specification based on similarities/differences across these three TRE provisions.

## Get in Touch

To get in touch with the SATRE team, please email [satre-contact@dundee.ac.uk](mailto:satre-contact@dundee.ac.uk).

To report Code-of-Conduct violations, please use the contact [specified in the Code of Conduct](https://github.com/sa-tre/satre-specification/blob/main/CODE_OF_CONDUCT.md).

## Recognising Contributions

We welcome and recognise all kinds of contributions, from discussing ideas, suggesting features, improving governance, maintaining the project, and more.

This project follows the [All Contributors specification](https://allcontributors.org/docs/en/overview).
The All Contributors bot usage is described [here](https://allcontributors.org/docs/en/bot/usage).

To add yourself or someone else as a contributor, comment on the relevant Issue or Pull Request with the following:

```
@all-contributors please add <username> for <contributions>
```

You can see the [Emoji Key (Contribution Types Reference)](https://allcontributors.org/docs/en/emoji-key) for a list of valid `<contribution>` types.
The bot will then create a Pull Request to add the contributor and reply with the pull request details.

**PLEASE NOTE: Only one contributor can be added with the bot at a time!**
Add each contributor in turn, merge the pull request and delete the branch (`all-contributors/add-<username>`) before adding another one.
Otherwise, you can end up with dreaded [merge conflicts][github-mergeconflicts].
Therefore, please check the open pull requests first to make sure there aren't any [open requests from the bot](https://github.com/sa-tre/satre-specification/pulls/app%2Fallcontributors) before adding another.

What happens if you accidentally run the bot before the previous run was merged and you got those pesky merge conflicts?
(Don't feel bad, we have all done it! 🙈)
Simply close the pull request and delete the branch (`all-contributors/add-<username>`).
If you are unable to do this for any reason, please let us know by opening an issue, and SATRE  team members will be very happy to help!
