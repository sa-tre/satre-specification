.. _evaluation_dundee_hic:

Health Informatics Centre Trusted Research Environment (HIC-TRE), University of Dundee
======================================================================================

`Health Informatics Centre (HIC) <https://www.dundee.ac.uk/hic>`_ supports high impact research through the collection and management of population based data.
HIC runs a cloud based TRE based on an older fork of the open-source `TREEHOOSE <https://github.com/HicResearch/TREEHOOSE>`_ platform.
This evaluation applies to the HIC-TRE, but it should be possible to satisfy all **Mandatory** SATRE technical requirements using TREEHOOSE.

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

