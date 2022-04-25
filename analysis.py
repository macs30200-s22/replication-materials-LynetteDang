"""
Name: analysis.py
Author: Lynette Dang

Initial findings
"""

import scipy.stats
import pandas as pd
import numpy as np
import seaborn as sns

df_analysis = pd.read_csv("analysis.csv")

x = np.array(df_analysis["Number of Connections"])
y = np.array(df_analysis["Legislative Effectiveness Score"])

df = [['Pearson Correlation',  scipy.stats.pearsonr(x, y)[0], scipy.stats.pearsonr(x, y)[1]],
      ['Spearman Correlation', scipy.stats.spearmanr(x, y)[0], scipy.stats.spearmanr(x, y)[1]]]

df = pd.DataFrame(df, columns=['Test', 'correlation coefficient', 'p_value'])

scat = sns.scatterplot(
    data=df_analysis, x="Number of Connections", y="Legislative Effectiveness Score")
hist_conn = sns.histplot(data=df_analysis, x="Number of Connections")
hist_les = sns.histplot(data=df_analysis, x="Legislative Effectiveness Score")
