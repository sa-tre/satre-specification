.. _evaluation_dundee_hic:

Dundee/HIC
==========

.. datatemplate:csv:: satre-uod-evaluation-20231011.csv
    :headers:
    :dialect: excel

    {{ make_list_table_from_mappings(
        [
            ("Section", "Section"),
            ("Item", "Item"),
            ("Statement", "Statement"),
            ("Guidance", "Guidance"),
            ("Importance", "Importance"),
            ("Score", "Score"),
            ("Response", "Response"),
            ("Improvements", "Improvements"),
        ],
        data,
        title="",
    ) }}


:download:`satre-uod-evaluation-20231011.csv`

Note the HIC-TRE is related to but not the same as the open-source [TREEHOOSE](https://github.com/HicResearch/TREEHOOSE) platform.
However it should be possible to satisfy all **Mandatory** SATRE technical requirements using TREEHOOSE.
