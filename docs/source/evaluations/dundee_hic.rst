.. _evaluation_dundee_hic:

Dundee/HIC
==========

.. datatemplate:csv:: satre-uod-evaluation-20231011.csv
    :headers:
    :dialect: excel

    {{ make_list_table_from_mappings(
        [("Section","Section"),("Item","Item"),("Statement","Statement"),("Guidance","Guidance")],
        data,
        title="",
    ) }}


:download:`satre-uod-evaluation-20231011.csv`
