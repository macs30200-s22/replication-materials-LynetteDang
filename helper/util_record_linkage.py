"""
Name: util_record_linkage.py
Author: Lynette Dang

Utility function to help link the LES dataset and the connection dictionary
using
"""
import pandas as pd
import fuzzy_pandas as fpd
import json

house = pd.read_excel("House116.xlsx")
senate = pd.read_excel("Senate116.xlsx")
with open('ind_network.json') as json_file:
    ind_network = json.load(json_file)
house = house[['Legislator name', 'Legislative Effectiveness Score']]
senate = senate[['Legislator name', 'Legislative Effectiveness Score']]
df_les = pd.concat([house, senate], axis=0)
df_conn = pd.DataFrame(ind_network.items(), columns=[
                       "Legislator name", "Number of Connections"])
# df_analysis contain information of 480 legislators,
# I have manually checked for these 480 match,
# but will have to go back and check for the 535-480 = 55 missing legislators
# in the future
df_analysis = fpd.fuzzy_merge(df_conn, df_les,
                              left_on='Legislator name',
                              right_on='Legislator name',
                              method='levenshtein',
                              threshold=0.80)
df_analysis.to_csv("analysis.csv")
