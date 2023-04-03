Standard Architecture for Trusted Research Environments (TREs)
==============================================================

Note:
> This is a living document under active development.

Contents
--------

- {ref}`comparisons`
- {ref}`features`

(features)=

TRE features
------------

- Control over data ingress and egress (including an approval process)
- MFA on login
- Environments isolated from one another
- Ability to forbid incoming/outgoing network connections
- Ability to forbid copy-and-paste
- Ability to install (some) packages from PyPI/CRAN/others
- Custom compute image and/or easy to customise default image
- Logging of user actions inside the TRE
- Logging of network connection attempts
- Logging of infrastructure actions
- Delegation of control to specified user roles (eg. permissions to turn VMs on and off)
- Automatic updates
- Anti-virus
- Automatic backup
- Ability to add/remove compute as needed
- Ability to use GPU VMs
- Git server (eg. GitLab/Gitea)
- Collaborative document writing (eg. CodiMD)
- Collaborative Jupyter notebooks
- Compute beyond VMs (e.g. clusters, ML workbench, databricks)
- Ease of deployment (e.g. via Infrastructure as Code)
- Ease of use by end-users

(comparisons)=

Comparisons of existing open-source TREs
----------------------------------------

Note:
> This section may reference separate paper "Comparing open-source trusted research environments", which evaluates Turing Data Safe Haven, AzureTRE and TREEHOOSE.

