(faqs)=

# Frequently Asked Questions

- {ref}`what_tre`
- {ref}`why_satre`
- {ref}`how_developed`
- {ref}`who_developed`
- {ref}`is_standard`
- {ref}`is_everything`
- {ref}`developer_gain`
- {ref}`operator_gain`
- {ref}`how_build`
- {ref}`set_in_stone`
- {ref}`other_tre_types`
- {ref}`support_federation`

(what_tre)=

## What is a TRE?

TRE stands for _Trusted Research Environment_.
The simplest definition tends to be _any_ kind of computing environment set up for research with sensitive data that has built-in security controls and user access management features.
The definition of TRE relevant to SATRE encompasses the set of information governance and data management processes alongside the computing technology used to support research with sensitive data; the definition of sensitive data being broadly any data for which there may be considerations around disclosure control, for any reason.

We recognise that in the UK several other names such a _Secure Data Environment_ or _Data Safe Haven_ have been used in the literature on computing with sensitive data, and that these systems may go by other names elsewhere.
For more information about TREs, visit the [UK TRE Community website](https://www.uktre.org/en/latest/).

(why_satre)=

## Why do we need a Standard Architecture for TREs

A variety of approaches have been taken to building computing infrastructure and designing processes and policies for research with sensitive data.
In recognition of this, SATRE aims to find the commonalities and compile a resource for TRE {ref}`Operators, Builders and Developers <infrastructure_roles>` to refer to and benefit from.
See {ref}`what_is_satre` for more information.

(how_developed)=

## How has the SATRE specification been developed and why?

See the information on the homepage of {ref}`these docs <satre_why>`.

(who_developed)=

## Who has developed the SATRE specification?

Take a look at our {ref}`contributors` page.

(is_standard)=

## Is SATRE an ISO technical standard?

No.
The SATRE specification aims to provide a helpful guide for TRE {ref}`Operators, Builders and Developers <infrastructure_roles>`.
It can be used to inform the development process of new TREs, or to evaluate existing TREs and inform how they could be improved.
Evaluating a TRE with the SATRE specification may help to identify which technical standards (e.g. ISO 27001) are already met and which (if any) are desirable to work towards meeting.

(is_everything)=

## Does SATRE provide everything I need to build a TRE?

No.
The SATRE specification defines a set of stakeholder {ref}`roles <satre_roles>` and feature {term}`capabilities <capability>` for TREs, which were decided according to our {ref}`architectural principles <satre_principles>`.
It does not dictate which specific technologies could or should be used to build a TRE.

(developer_gain)=

## What do TRE {ref}`Builders/Developers <infrastructure_roles>` gain by reading the SATRE specification?

By reading through the SATRE specification, developers tasked by their institution with designing and/or building a TRE for sensitive data projects can avoid re-inventing the wheel.
The specification does not dictate answers to the specific technology or policy choices that need to be made when developing a TRE, but it does provide a guide for thinking about which choices need to be made and what {ref}`capabilities <satre_pillars>` the TRE should possess.

(operator_gain)=

## What do TRE {ref}`Operators <infrastructure_roles>` gain by evaluating their TRE with SATRE?

See: {ref}`why_evaluate`

(how_build)=

## How do I build and run a SATRE compliant TRE?

We encourage TRE {ref}`Operators and Builders <infrastructure_roles>` to publicly evaluate their TREs against the SATRE specification; see {ref}`evaluation`.
TRE {ref}`Developers <infrastructure_roles>` can use the specification and published TRE evaluations as a starting point.
Some of evaluated TREs such as the Alan Turing Institute's _[Data Safe Haven](https://data-safe-haven.readthedocs.io/en/latest/)_ and the University of Dundee Health Informatics Centre's _[TREEHOOSE](https://github.com/HicResearch/TREEHOOSE/)_ are deployed from open source infrastructure-as-code, and can be deployed by other institutions.

(set_in_stone)=

## Is the SATRE specification set in stone?

Absolutely not.
We know that TREs vary greatly in their design architecture, purposes for being built, the kinds of research they support and data they handle.
We have tried to build a specification with as broadly useful a set of capabilities as possible, whilst acknowledging these different approaches.
We won't have covered everything, and if you find SATRE valuable but think there is something we've missed, please consider {ref}`contributing <contributing>`.
Additionally, the best practices in TRE provision may evolve over time as technologies and regulations change.
We hope that the SATRE specification will be maintained in the future and accommodate these changes as appropriate.

(other_tre_types)=

## My TRE is designed for data that doesn't require this level of protection. Should I still follow SATRE?

Yes.
At the moment, the SATRE specification contains a set of capabilities marked as "Mandatory" which we believe are essential for a system to be defined as a TRE, as well as many "Recommended" and "Optional" capabilities.
Some of the non-mandatory capabilities will likely not be needed for TREs containing data that does not require all the possible protections, and there may well be tradeoffs to be made in terms of accessibility vs security that depend on the data the TRE holds.
A future specification may include the idea of different archetypes of TREs, or data sensitivity tiers, with different requirements for each.

(support_federation)=

## Does SATRE describe approaches to TRE federation or interoperability of TREs?

No.
However, it's intended that SATRE could form the foundation for future standards and guidance on federation, interoperability, and related work.
