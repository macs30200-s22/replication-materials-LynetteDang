[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.6483770.svg)](https://doi.org/10.5281/zenodo.6483770)

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


## Network Analysis
<p align="center"> Figure 1: Committee-Based Congressional Network </p>
<p align="center"> <img src="https://user-images.githubusercontent.com/91070896/171291227-bbd58e04-561a-48c2-9f06-e0f3867a90d5.png" data-canonical-src="https://user-images.githubusercontent.com/91070896/171291227-bbd58e04-561a-48c2-9f06-e0f3867a90d5.png" width="500" height="500" />  </p>


We will first take a look at the network structure before regression analysis. The network consists of digraphs, and has 480 nodes as individual legislators (missing a few legislators during record linkage) and 20610 edges representing their committee-based connections, with density of 0.067, and average clustering coefficient of 0.343. The graph is a visualizations of committee-based based congressional networks. Each tie in the visualization represents a committee-based connection between legislators, meaning that they serve in at least one common congressional committee. To distinguish the party affiliation of each legislator, blue nodes refer to Democrat legislators, and red nodes refer to Republican legislators. The committee-based networks formed a moderately-connected and clustered network among all legislators. Legislators from the two parties are at a roughly equal level of connectedness. Senators and house of representatives have formed two distinct clusters. The legislators who linked the two clusters are those who serve on the joint
committees.



## Regression Analysis
Do centrality measures (betweenness centrality, closeness centrality, degree centrality, and eigenvector centrality), race, and gender play a role in determining whether a legislator is effective or not? In order to find out which independent variable or combination of independent variables will affect legislative effectiveness score, I decided to run a ridge regression and cross validate with a wide range of lambda values from 0.01 to 1000 on standardized features with first-order interaction terms in R. Ridge regression models use L2 regularization to weight and penalize residuals. They will likely shrink some coefficients to 0, or closer to 0, which helps me eliminate the unimportant features. It tends to generalize better because it is less sensitive to extreme variance in the data such as outliers. After training the models, the author compute the Bayesian information criterion (BIC) for model selection. BIC is derived from Bayesian probability and inference. It is appropriate for models fit under the maximum likelihood estimation framework. Typically, lower BIC value indicates lower penalty terms, hence a better model. The BIC values for all models ranges from 174 to 203, indicating the evidence for the best model and against the weaker model is strong. The most optimal lambda value turned out to be 0.01, with BIC = 173.8858. The results from the best performing model are shown in the table below.
<p align="center"> Figure 2: Effect of Centrality (Committee-Based Network), Race and Ethnicity on Legislative Effectiveness </p>
<p align="center"> <img src="https://user-images.githubusercontent.com/91070896/171313705-4385c43c-8591-4b77-90a9-f707c0c4cabf.png" data-canonical-src="https://user-images.githubusercontent.com/91070896/171313705-4385c43c-8591-4b77-90a9-f707c0c4cabf.png" width="450" height="600" />  </p>


From the table above, we can conclude that he 6 original features (centrality measures, predicted gender and ethnicity) individually does not make a large impact on legislative effectiveness. The regression coefficients from the four centrality measures are either not in magnitude or negative, suggesting there is weak relationship or even negative relationship between the feature and legislative effectiveness.

However, the interaction effects between between closeness centrality and betweenness centrality as well as between degree centrality and betweenness centrality are remarkable. The large interaction coefficients for both measures each indicates a significant interaction effect between the two features. In other words, the legislators find it easier to reach other legislators (high closeness centrality) and more likely to control information flow (betweenness centrality) are predicted to be more effective legislators by the model. Likewise, the legislators who stand on more and larger congressional committees (high degree centrality) and more likely to control information flow (high betweenness centrality), as well as black legislators who are more likely to control information flow (high betweenness centrality) are predicted to be more effective legislators by the model. 

In conclusion, the results from regression analysis has shown that the following types of legislators are more effective than their peers based on committee-oriented congressional networks:
* information leaders who are more reachable
* information leaders who are involve in more and larger congressional committees
* black information leaders

This finding has significant implication: Rather than personal attributes alone, it suggests a combination of race and centrality measures in committee-based social networks makes a substantial impact on legislative effectiveness. It is evident that an increase in participation in committees and in the connection between House and Senate can potentially improve the effectiveness of elected representatives.



