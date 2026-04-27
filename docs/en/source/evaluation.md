(evaluation)=

# Evaluating TREs against SATRE

This section details the method for evaluating a TRE against the SATRE specification.

## Who should evaluate a TRE against SATRE?

This section is aimed at {ref}`Operators <infrastructure_roles>` and {ref}`Information Governance Managers <governance_roles>` of TREs at institutions hosting sensitive data research projects.
The example evaluations provided may also be of use to TRE {ref}`Developers <infrastructure_roles>` who wish to review existing implementations as well as the specification.

(why_evaluate)=

## Why should I evaluate my institution's TRE?

The SATRE specification has been compiled from the knowledge around successful TRE provision from a variety of institutions.
This includes information governance procedures, computing technology, data management and other capabilities.

By scoring your institutions' TRE against the specification using the method below, you can:

1. Identify any technical oversights in the way your TRE is designed that could lead to unintended disclosure of sensitive data or inappropriate user access.
2. Identify any operating procedures that could be improved for your TRE and how to improve them, which will also minimise risks and ensure the smooth operation of TRE-based research projects.
3. Compile a wish list of capabilities that your TRE lacks (or could be improved).
   You could for example, cite the SATRE specification as evidence for resources (computational or human) needing to be allocated by your institution.

:::{note}
SATRE is _not_ a technical standard for which formal accreditation can be achieved.
For more info see: {ref}`is_standard`
:::

## Publicly available evaluations

Example evaluations from UK TREs are now hosted on the [SATRE UKTRE Community site](https://satre.uktre.org/en/) site.
These examples demonstrate how different institutions have evaluated their TREs against the SATRE specification and can help guide your own evaluation process.

We encourage organisations to share their evaluations to benefit the community and contribute towards openness.
By making evaluations publicly available, we can collectively improve TRE provision across the sector and learn from each other's experiences and approaches.

(scoring_method)=

## Method

You should score your TRE against each statement in the SATRE specification using this scoring system:

:0 Not met: The TRE does not meet this requirement (if this is **Mandatory** this means the TRE is not SATRE compliant)
:1 Sufficient: The TRE meets this requirement met but there is substantial scope for improvement
:2 Satisfied: The TRE meets this requirement met but there may still be scope for improvement
:N/A: Not applicable: The statement is not relevant to a TRE, may apply to **Recommended** or **Optional** statements, and a very limited number of **Mandatory\*** statements.

A score of **1** or above means you have met the requirement.
Optionally you can use **1** and **2** to indicate potential areas of improvement in your TRE.

An evaluation may simply give your TRE scores for each statement.
We recommend a more detailed evaluation, which includes a score, a justification and, where applicable, suggestions for improvement.

The example evaluations are detailed, including the supporting text as well as scores.

### Combining scores

The scores for each statement can be easily combined at the capability, pillar or overall level.
If all the **Mandatory** statements in a capability are met, either at level **1** or level **2**, then the capability is met.
If all capabilities in a pillar are met then the pillar is met.
If all pillars are met then the SATRE specification is met.

(evaluate_spreadsheet)=

## Evaluation spreadsheet

You can use this [spreadsheet](satre.xlsx){.external} as a template for your evaluation.
