# import os
# from datetime import datetime
# import pandas as pd
# import pybliometrics.scopus
# from pybliometrics.scopus import ScopusSearch, AbstractRetrieval
# os.environ["SCOPUS_APIKEY"] = "5e924c899ac331e82be6f6c34a50e831"
# pybliometrics.scopus.init()
# # pybliometrics.scopus.utils.constants.CONFIG_FILE

# print(pybliometrics.scopus.utils.constants.CONFIG_FILE)


# # Download
# start = datetime.now().replace(microsecond=0)


# scopus_filter = r"AFFIL (\"Technology, Policy and Management\" OR \"Technology Policy and Management\") AND AFFIL (\"TU Delft\") AND PUBYEAR > 2023"

# search = ScopusSearch(scopus_filter,  max_entries=10, subscriber=False)
# print("Number of results:", search.get_results_size())

# end = datetime.now().replace(microsecond=0)
# print(end-start)

# print(len(search.results))  # Number of papers

import pybliometrics
pybliometrics.scopus.init()  # read API keys
# Document-specific information
from pybliometrics.scopus import AbstractRetrieval
ab = AbstractRetrieval("https://doi.org/10.1016/j.softx.2019.100263")
ab.title