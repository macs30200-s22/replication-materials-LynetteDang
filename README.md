<img src="https://zenodo.org/badge/DOI/10.5281/zenodo.6483770.svg">

# MACS 30200 "Perspectives on Computational Research": Cross-Partisan Social Networks and Legislative Effectiveness

Author: Lynette Dang

## Introduction

My research topic is centered around cross-partisan social networks and legislative effectiveness. In particular, I am interested in investigating, comparing and contrasting two types of social networks and their effect on the legislative effectiveness score of each legislator during a particular period of time: How does issue-oriented cross-partisan social networks and committee-oriented cross-partisan social networks affect legislative effectiveness of each legislator from 116th to 117th Congress (from 2019 to 2022)? Which type of networks has a larger impact on legislative effectiveness? I believe by examining these two types of social networks and their effect on legislative effectiveness, we are one step closer to understanding legislative bargaining, policy making, and political representation on a federal level.

## Dependency

The code and data in this repository is an example of a reproducible research workflow for my MACS 30200 "Perspectives on Computational Research" project.

The code is written in Python 3.9.7 and all of its dependencies can be installed by running the following in the terminal (with the `requirements.txt` file included in this repository):

```
pip install -r requirements.txt
```

You can then use the `generate_result` function in the `analysis` module will reproduce all the findings (one scatterplot, two histograms, and one csv) under subdirectory `result`

```python
python3 analysis.py
```

To view the results, you can find the printed table and graphs in `analysis.ipynb`.

Alternatively, to replicate the analysis and produce all of the figures and quantitative analyses from the (hypothetical) publication that this code supplements, build and run the `Dockerfile` included in this repository via the instructions in the file).

If you use this repository for a scientific publication, we would appreciate it if you cited the [Zenodo DOI](https://doi.org/10.5281/zenodo.6483770)
) (see the "Cite as" section on our Zenodo page for more details).

## Results

For committee-based network analysis, for each legislator, I calculated the number of connections one has based on the committees one serve in, and used record linkage to connect the number of connections with legislative effectiveness score based on the name of the legislator, store the result in a csv file and perform some initial analysis.\
Distribution of Number of Connections for All Legislators:\
<img src="https://github.com/macs30200-s22/replication-materials-LynetteDang/blob/master/results/hist_conn.png">\
Distribution of Legislative Effectiveness Score (out of 10) for All Legislators:\
<img src="https://github.com/macs30200-s22/replication-materials-LynetteDang/blob/master/results/hist_les.png">\
Number of Connections and Legislative Effectiveness Score (out of 10) for All Legislators:\
<img src="https://github.com/macs30200-s22/replication-materials-LynetteDang/blob/master/results/scatterplot.png">

| Test                 | Correlation Coefficient | P_value             |
| -------------------- | ----------------------- | ------------------- |
| Pearson Correlation  | -0.032418072507163775   | 0.47812566986331323 |
| Spearman Correlation | 0.02959769709785644     | 0.5172559149646156  |

The results indicates that there is no correlation between number of connections within networks and a legislator's legislative effectiveness score, which is surprising. However, I do want to make a note that the current joined csv file mentioned above only contains information of 480 legislators (I have manually checked for these 480 match but will have to go back and check for the `535 - 480 = 55` missing legislators in the future). This can contribute to the null result. Also, I haven't controlled for gender or race, which can be important indictors for legislative effectiveness score.
