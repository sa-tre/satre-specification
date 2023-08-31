(evaluation)=

# Evaluating TREs against SATRE

## How to score

You should score your TRE against each statement in the SATRE specification.
The scoring system is:

0 (Not met)
: The TRE does not meet this requirement
1 (Sufficient)
: The TRE meets this requirement met but there is substantial scope for improvement
2 (Satisfied)
: The TRE meets this requirement met but there may still be scope for improvement

Although both **1** and **2** indicate a TRE meets the requirement, they indicate different levels of possible improvement.

### Combining scores

The scores for each statement can be easily combined at the capability, pillar or overall level.
If all the **Mandatory** statements in a capability are met, either at level **1** or level **2**, then the capability is met.
If all capabilities in a pillar are met then the pillar is met.
If all pillars are met then the SATRE specification is met.

## Examples

- Evaluation of {ref}`The Alan Turing Institute Data Safe Haven <evaluation_alan_turing_institute>`.
- Evaluation of {ref}`Dundee/HIC TREEHOOSE <evaluation_dundee_hic>`.

You can use this {download}`spreadsheet <../build/satrecsv/satre.xlsx>` as a template for your evaluation
