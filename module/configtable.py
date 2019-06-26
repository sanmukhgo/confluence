"""Merges all configurations tables of Inventory Features in one."""

import hdata


def configurations():
    """
    Returns combine configurations table as a dict of columns:

        .Source
        .Configurtions
        .Description
        .Values
        .Default
    """

    configtable = {"Source": [], "Configurations": [],
                   "Description": [], "Values": [], "Default": []}
    data = hdata.data()                 # All data of the page

    for d in data:
        for tbl in d['table']:
            """Finds the table with particular headers"""

            if tbl[0] == ["Source", "Configuration", "Description", "Values", "Default"]:

                for row in tbl[1:]:  # Adding data to configtable
                    for (rdata, ctdata) in zip(row, configtable.values()):
                        ctdata.append(rdata)

    return configtable


if __name__ == "__main__":
    print(configurations())
