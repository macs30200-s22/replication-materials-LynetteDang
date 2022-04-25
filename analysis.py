"""
Name: analysis.py
Author: Lynette Dang

Initial findings
"""

import scipy.stats
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plot

df_analysis = pd.read_csv("analysis.csv")

x = np.array(df_analysis["Number of Connections"])
y = np.array(df_analysis["Legislative Effectiveness Score"])


def generate_result(x, y):
    df = [['Pearson Correlation',  scipy.stats.pearsonr(x, y)[0], scipy.stats.pearsonr(x, y)[1]],
          ['Spearman Correlation', scipy.stats.spearmanr(x, y)[0], scipy.stats.spearmanr(x, y)[1]]]

    df = pd.DataFrame(
        df, columns=['Test', 'correlation coefficient', 'p_value'])
    df.to_csv('results/correlation_results.csv')
    sns.set_theme()
    scat = sns.scatterplot(
        data=df_analysis, x="Number of Connections", y="Legislative Effectiveness Score")
    plot.savefig("results/scatterplot.png")
    plot.clf()
    hist_conn = sns.histplot(data=df_analysis, x="Number of Connections")
    plot.savefig("results/hist_conn.png")
    plot.clf()
    hist_les = sns.histplot(
        data=df_analysis, x="Legislative Effectiveness Score")
    plot.savefig("results/hist_les.png")


if __name__ == "__main__":
    # When running script in Docker Container, save figure to /results/
    # directory
    generate_result(x, y)
