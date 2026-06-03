(faqs)=

# Frequently Asked Questions

- {ref}`what_tre`
- {ref}`why_satre`
- {ref}`how_developed`
- {ref}`who_developed`
- {ref}`how_structured`
- {ref}`is_standard`
- {ref}`relate_standards`
- {ref}`is_everything`
- {ref}`developer_gain`
- {ref}`evaluate_tre`
- {ref}`evaluate_incr`
- {ref}`how_long`
- {ref}`operator_gain`
- {ref}`what_is_compliance`
- {ref}`how_build`
- {ref}`set_in_stone`
- {ref}`other_tre_types`
- {ref}`support_federation`
- {ref}`how_contribute`

(what_tre)=

## What is a TRE?

TRE stands for _Trusted Research Environment_.
The simplest definition tends to be _any_ kind of computing environment set up for research with sensitive data that has built-in security controls and user access management features.
The definition of TRE relevant to SATRE encompasses the set of information governance and data management processes alongside the computing technology used to support research with sensitive data; the definition of sensitive data being broadly any data for which there may be considerations around disclosure control, for any reason.

We recognise that in the UK several other names such a _Secure Data Environment_ or _Data Safe Haven_ have been used in the literature on computing with sensitive data, and that these systems may go by other names elsewhere.
For more information about TREs, visit the [UK TRE Community website](https://www.uktre.org/en/latest/).

(why_satre)=

## Why do we need a Standard Architecture for TREs?

A variety of approaches have been taken to building computing infrastructure and designing processes and policies for research with sensitive data.
There are also a range of standards or frameworks that may apply to TREs such as [ISO27001](https://www.iso.org/standard/27001) or [5 Safes](https://blog.ons.gov.uk/2017/01/27/the-five-safes-data-privacy-at-ons/).
However, they don't provide prescriptive guidance on how TREs comply or achieve accreditation.
In recognition of this, SATRE aims to find the commonalities and compile a resource for TRE {ref}`Operators, Builders and Developers <infrastructure_roles>` to refer to and benefit from.
See {ref}`what_is_satre` for more information.

(how_developed)=

## How has the SATRE specification been developed and why?

SATRE has been developed as a community-led specification, bringing together knowledge, experience, and best practice from a wide range of organisations across the UK TRE community, including academia, healthcare, industry, and government. It was created through collaboration with over 60 organisations, public engagement, and ongoing feedback to ensure it reflects real‑world needs and practice.  
The specification was developed to address the lack of TRE‑specific guidance and to provide a consistent framework for designing, operating, and evaluating Trusted Research Environments. Its aim is to improve trust, interoperability, and efficiency by defining shared capabilities and enabling organisations to assess and enhance their TREs in a structured way.

(who_developed)=

## Who has developed the SATRE specification?

The SATRE specification has been developed by the UK Trusted Research Environment community, led by a collaboration of organisations including the University of Dundee, University College London, the Alan Turing Institute, and partners across academia, healthcare, industry, and government.
It is a community‑driven effort, involving contributions from over 60 organisations, ensuring that the specification reflects shared experience, best practice, and the needs of those building and operating TREs in the UK.

(how_structured)=

## How is SATRE structured?

SATRE is structured as a specification that defines the key capabilities required to design, build, and operate a TRE. It is organised around four core pillars-such as information governance, computing technology, and data management—supported by a set of capabilities and detailed statements that describe expected practices. Together, these provide a consistent way to understand how a TRE should function across all aspects of its operation. 
The specification is hierarchical: high-level principles and pillars are broken down into capabilities, which are then expressed as individual requirements (statements). These statements are classified (e.g. mandatory, recommended, optional) and used as the basis for evaluation, allowing organisations to assess implementation in a structured and comparable way.

(is_standard)=

## Is SATRE an ISO technical standard?

No.
The SATRE specification aims to provide a helpful guide for TRE {ref}`Operators, Builders and Developers <infrastructure_roles>`.
It can be used to inform the development process of new TREs, or to evaluate existing TREs and inform how they could be improved.
Evaluating a TRE with the SATRE specification may help to identify which technical standards (e.g. ISO 27001) are already met and which (if any) are desirable to work towards meeting.

(relate_standards)=

## How does SATRE relate to other standards?

SATRE is designed to complement, not replace, existing standards and frameworks. It is not an ISO technical standard; instead, it provides a structured approach to understanding and improving Security Awareness, Training, and Education (SATE) capability. While standards such as ISO/IEC 27001 or the NIST Cybersecurity Framework set out what organisations should do, SATRE focuses on how effectively those expectations are delivered through people and behaviour.

The SATRE Control Alignment Table ({ref}`alignment`) shows how SATRE practices map to recognised standards and frameworks, helping organisations link SATRE activity to existing control requirements. This enables organisations to demonstrate alignment, identify gaps, and strengthen the human element of their security posture without duplicating or replacing established frameworks.

(is_everything)=

## Does SATRE provide everything I need to build a TRE?

No.
The SATRE specification defines a set of stakeholder {ref}`roles <satre_roles>` and feature capabilities for TREs, which were decided according to our {ref}`architectural principles <satre_principles>`.
It does not dictate which specific technologies could or should be used to build a TRE.

(developer_gain)=

## What do TRE {ref}`Builders/Developers <infrastructure_roles>` gain by reading the SATRE specification?

By reading through the SATRE specification, developers tasked by their institution with designing and/or building a TRE for sensitive data projects can avoid re-inventing the wheel.
The specification does not dictate answers to the specific technology or policy choices that need to be made when developing a TRE, but it does provide a guide for thinking about which choices need to be made and what {ref}`capabilities <satre_pillars>` the TRE should possess.

(evaluate_tre)=

## How do I evaluate a TRE?

A TRE is evaluated in SATRE through a structured self‑assessment against the SATRE specification. Organisations use the SATRE evaluation template (an Excel workbook derived from the specification) to review each requirement across the five pillars and supporting capabilities, scoring their current implementation and recording evidence, justification, and any improvements identified.

In practice, this involves assembling a cross‑functional team (e.g. technical, governance, and data roles), working systematically through each statement, and assigning a score (0 = not met, 1 = sufficient, 2 = satisfied, N/A = not applicable). A detailed evaluation should include supporting rationale and suggested improvements, enabling organisations to identify gaps, prioritise actions, and track progress over time. Further guidance available in the evaluation guidance page ({ref}`evaluation`) and past evaluations by other organisations available on our [community website](https://satre.uktre.org/en/evaluations/).

(evaluate_incr)=

## Can SATRE be applied incrementally?

Yes—SATRE can be applied incrementally.

It is designed as a self‑assessment framework that helps organisations identify gaps, prioritise improvements, and progress over time. The use of **Mandatory**, **Recommended**, and **Optional** requirements supports a phased approach, where organisations meet baseline expectations first and then enhance their capabilities progressively based on need and context.

(how_long)=

## How long does it take to implement or evaluate SATRE?

The time required will vary depending on factors such as the size and maturity of the TRE, availability of evidence, and level of detail in the evaluation (e.g. simple scoring vs. full justification and improvement planning).

As a guideline, if you have the relevant information governance and operations team members available it should take a maximum of two days.

(operator_gain)=

## What do TRE {ref}`Operators <infrastructure_roles>` gain by evaluating their TRE with SATRE?

See: {ref}`why_evaluate`

(what_is_compliance)=

## What does compliance mean?

Compliance, in the context of SATRE, refers to meeting defined requirements or obligations set by standards, regulations, or organisational policies. This often focuses on whether specific controls or activities—such as delivering training or maintaining records—are in place as expected.

SATRE recognises that compliance alone does not ensure effectiveness. While it is important to demonstrate that requirements are met, SATRE emphasises going beyond compliance to understand whether security awareness and training activities are actually influencing behaviours and contributing to better security outcomes.

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

(who_is_using)=

## Who is currently using SATRE?

SATRE is being adopted and used by a growing range of organisations across the UK TRE community, including academic institutions, NHS environments, and research organisations.

Examples published on the SATRE community site include the Scottish National Safe Haven, Grampian Data Safe Haven, Health Informatics Centre (University of Dundee), and the East of England SDE, among others. These organisations have used SATRE to evaluate and improve their TREs and to share their results with the wider community.

SATRE is designed for broad use, so any organisation building or operating a Trusted Research Environment can adopt it and contribute to its continued development.

(support_federation)=

## Does SATRE describe approaches to TRE federation or interoperability of TREs?

Yes.
As of v2.0, SATRE includes a Federation Pillar which provides a framework for establishing and maintaining a SATRE-compliant TRE Federation.

(how_contribute)=

## How can I contribute to SATRE?

You can contribute to SATRE by engaging with the community and helping to improve the specification. This includes providing feedback, sharing your organisation’s evaluations, raising issues or suggestions via the [SATRE GitHub repositories](https://github.com/sa-tre/satre-specification), and participating in community discussions and events.

SATRE is community-led, so contributions from TRE operators, developers, and users are actively encouraged to help refine and evolve the framework over time. Our [community website](https://satre.uktre.org/en/evaluations/) has a list of resources for following our project and connecting with us.
