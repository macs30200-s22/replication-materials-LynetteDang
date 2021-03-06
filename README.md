[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.6483770.svg)](https://doi.org/10.5281/zenodo.6483770)

# MACS 30200 "Perspectives on Computational Research": Cross-Partisan Social Networks and Legislative Effectiveness

Author: Lynette Dang

## Introduction

The US Congress is known for having increasing polarization and thus questionable effectiveness with regard to making and passing bills, approving presidential nominations, as well as budgeting. While studying legislative effectiveness, existing literature focuses on the important personal and institutional attributes such as race, gender, and ethnicity that make some Congressmen and Congresswomen more effective legislators than their peers. However, only a limited amount of attention has been directed to individual-based social networks within Congress. Can issue-oriented and committee-oriented cross-partisan social networks help overcome congressional gridlocks and mitigate polarization? This project seeks to investigate the impact of these two types of social networks on legislative effectiveness score[^1] of each legislator in the 116th Congress: How does issue-oriented cross-partisan social networks[^2] and committee-oriented cross-partisan social networks affect legislative effectiveness of each legislator in the 116th Congress? Which type of networks has a larger impact on legislative effectiveness? I believe by examining these two types of social networks and their effect on legislative effectiveness, we are one step closer to understanding legislative bargaining, policy making, and political representation on a federal level. Note that I am also proposing to do the same project (or parts of it) for my perspectives and social network analysis class. Eventually, I want to answer this research question for my MA thesis and expand my analysis to include more congressional terms (ideally from 2000-2022).


[^1]: Legislative effectiveness score is a measure devised by Volden and Wiseman to account for the combination of a Congress member’s bill progress and the ability to pass more significant bills (Volden and Wiseman, 2009 and 2014). For details, please visit: https://thelawmakers.org/category/legislative-effectiveness-scores# 

[^2]: Here, issue-oriented cross-partisan networks refer to social networks formed by legislators who bring up or discuss the same issues as reflected by Congressional record: the official daily record of the debates and proceedings of the U.S. Congress.

[^3]: https://www.congress.gov/congressional-record/116th-congress/browse-by-date  note that the congressional record are daily-based

## Dependency

The code and data in this repository is an example of a reproducible research workflow for my MACS 30200 "Perspectives on Computational Research" project.

Most of the code is written in Python 3.9.7 and all of its dependencies can be installed by running the following in the terminal (with the `requirements.txt` file included in this repository):

```
pip install -r requirements.txt
```

To view the results/visualization: 

For committee-based networks, you can find the printed table and graphs in [analysis.ipynb](https://github.com/macs30200-s22/replication-materials-LynetteDang/blob/master/committee/analysis.ipynb) and [final_analysis.pdf](https://github.com/macs30200-s22/replication-materials-LynetteDang/blob/master/committee/final_analysis.pdf)

For issue-based networks, you can find the printed table and graphs in [4_construct_network.ipynb](https://github.com/macs30200-s22/replication-materials-LynetteDang/blob/master/issue/4_construct_network.ipynb) and [5_analysis.pdf](https://github.com/macs30200-s22/replication-materials-LynetteDang/blob/master/issue/5_analysis.pdf)

If you use this repository for a scientific publication, we would appreciate it if you cited the [Zenodo DOI](https://doi.org/10.5281/zenodo.6483770)
) (see the "Cite as" section on our Zenodo page for more details).


## Committee-Based Congressional Network

### Network Analysis
<p align="center"> Figure 1: Committee-Based Congressional Network </p>
<p align="center"> <img src="https://user-images.githubusercontent.com/91070896/171291227-bbd58e04-561a-48c2-9f06-e0f3867a90d5.png" data-canonical-src="https://user-images.githubusercontent.com/91070896/171291227-bbd58e04-561a-48c2-9f06-e0f3867a90d5.png" width="500" height="500" />  </p>


We will first take a look at the network structure before regression analysis. The network consists of digraphs, and has 480 nodes as individual legislators (missing a few legislators during record linkage) and 20610 edges representing their committee-based connections, with density of 0.067, and average clustering coefficient of 0.343. The graph is a visualizations of committee-based based congressional networks. Each tie in the visualization represents a committee-based connection between legislators, meaning that they serve in at least one common congressional committee. To distinguish the party affiliation of each legislator, blue nodes refer to Democrat legislators, and red nodes refer to Republican legislators. The committee-based networks formed a moderately-connected and clustered network among all legislators. Legislators from the two parties are at a roughly equal level of connectedness. Senators and house of representatives have formed two distinct clusters. The legislators who linked the two clusters are those who serve on the joint
committees.



### Regression Analysis
Do centrality measures (betweenness centrality, closeness centrality, degree centrality, and eigenvector centrality), race, and gender play a role in determining whether a legislator is effective or not? In order to find out which independent variable or combination of independent variables will affect legislative effectiveness score, I decided to run a ridge regression and cross validate with a wide range of lambda values from 0.01 to 1000 on standardized features with first-order interaction terms in R. Ridge regression models use L2 regularization to weight and penalize residuals. They will likely shrink some coefficients to 0, or closer to 0, which helps me eliminate the unimportant features. It tends to generalize better because it is less sensitive to extreme variance in the data such as outliers. After training the models, the author compute the Bayesian information criterion (BIC) for model selection. BIC is derived from Bayesian probability and inference. It is appropriate for models fit under the maximum likelihood estimation framework. Typically, lower BIC value indicates lower penalty terms, hence a better model. The BIC values for all models ranges from 174 to 203, indicating the evidence for the best model and against the weaker model is strong. The most optimal lambda value turned out to be 0.01, with BIC = 173.8858. The results from the best performing model are shown in the table below.
<p align="center"> Table 2: Effect of Centrality (Committee-Based Network), Race and Ethnicity on Legislative Effectiveness </p>
<p align="center"> <img src="https://user-images.githubusercontent.com/91070896/171313705-4385c43c-8591-4b77-90a9-f707c0c4cabf.png" data-canonical-src="https://user-images.githubusercontent.com/91070896/171313705-4385c43c-8591-4b77-90a9-f707c0c4cabf.png" width="450" height="600" />  </p>


From the table above, we can conclude that he 6 original features (centrality measures, predicted gender and ethnicity) individually does not make a large impact on legislative effectiveness. The regression coefficients from the four centrality measures are either not in magnitude or negative, suggesting there is weak relationship or even negative relationship between the feature and legislative effectiveness.

However, the interaction effects between between closeness centrality and betweenness centrality as well as between degree centrality and betweenness centrality are remarkable. The large interaction coefficients for both measures each indicates a significant interaction effect between the two features. In other words, the legislators find it easier to reach other legislators (high closeness centrality) and more likely to control information flow (betweenness centrality) are predicted to be more effective legislators by the model. Likewise, the legislators who stand on more and larger congressional committees (high degree centrality) and more likely to control information flow (high betweenness centrality), as well as black legislators who are more likely to control information flow (high betweenness centrality) are predicted to be more effective legislators by the model. 

In short, the results from regression analysis has shown that the following types of legislators are more effective than their peers based on committee-oriented congressional networks:
* information leaders who are more reachable
* information leaders who are involve in more and larger congressional committees
* black information leaders


## Issue-Based Congressional Network
### Network Analysis
<p align="center"> Figure 1: Issue-Based Congressional Network </p>
<p align="center"> <img src="https://user-images.githubusercontent.com/91070896/171289064-7bef7d4c-5e3d-410a-a7c8-ac59732f030e.png" data-canonical-src="https://user-images.githubusercontent.com/91070896/171289064-7bef7d4c-5e3d-410a-a7c8-ac59732f030e.png" width="500" height="500" />  </p>

Just like for committee-based networks, we will first take a look at the network structure before regression analysis. The issue-based network consists of digraphs, and has 411 nodes as individual legislators (missing a few legislators during record linkage and due to the lack of issue-related speeches) and 60278 edges representing their issue-based connections, with density of 0.067, and average clustering coefficient of 0.343.  Each tie in the visualization can be interpreted as the two connected legislators care about the same issue and have mentioned related keywords in their speeches as reflected by congressional records in the 116th Congress. To distinguish the party affiliation of each legislator, blue nodes refer to Democrat legislators, and red nodes refer to Republican legislators. The issue-based networks formed a moderately-connected and clustered network among all legislators. Legislators from the two parties are at a roughly equal level of connectedness. There is no major clusters as observed in the network, unlike committee-based network, where senators and house of representatives have formed two distinct clusters.

### Regression Analysis
Replicating the same ridge regression analysis workflow as committee-based social network, we found that across all trained ridge regresison models for issue-based network, the BIC values for all models ranges from 173 to 200, indicating the evidence for the best model and against the weaker model is strong. The most optimal lambda value turned out to be 0.01, with BIC = 173.8858. The results from the best performing model are shown in the table.
<p align="center"> Table 2: Effect of Centrality (Issue-Based Network), Race and Ethnicity on Legislative Effectiveness </p>
<p align="center"> <img src="https://user-images.githubusercontent.com/91070896/171294701-a6006847-ed1c-4f36-820a-970da791b32b.png" data-canonical-src="https://user-images.githubusercontent.com/91070896/171294701-a6006847-ed1c-4f36-820a-970da791b32b.png" width="450" height="600" />  </p>

From the table above, we can conclude that he 6 original features (centrality measures, predicted gender and ethnicity) individually does not make a large impact on legislative effectiveness. The regression coefficients from the four centrality measures are either not in magnitude or negative, suggesting there is weak relationship or even negative relationship between the feature and legislative effectiveness.

However, the interaction effects between between eigenvector centrality and betweenness centrality, closeness centrality and betweenness centrality as well as between degree centrality and betweenness centrality are remarkable. The large interaction coefficients for both measures each indicates a significant interaction effect between the two features. In other words, the legislators who have the most influential neighbors (high eigenvector centrality) and are more likely to control information flow (high betweenness centrality) are predicted to be more effective legislators by the model. Likewise, the legislators find it easier to reach other legislators (high closeness centrality) and more likely to control information flow (betweenness centrality), the legislators who stand on more and larger congressional committees (high degree centrality) and more likely to control information flow (high betweenness centrality), as well as black and hispanic legislators who are more likely to control information flow (high betweenness centrality) are predicted to be more effective legislators by the model. 

In conclusion, the results from regression analysis has shown that the following types of legislators are more effective than their peers based on issue-oriented congressional networks:
* information leaders who also influential neighbors
* information leaders who are more reachable
* information leaders who are involve in more and larger congressional committees
* black and hispanic information leaders

## Conclusion

The results from committee-based congressional networks also state that black information leaders, information leaders who are more reachable, or involved in more and larger congressional committees to be more effective. The results from issue-based congressional networks is similar to the results from committee-based congressional networks, yielding that personal attributes and cosponsorship activities are not the only factors accounting for legislative effectiveness. Both committee-based and issue-based congressional networks can make an impact on legislative effectiveness at an individual level. The results also suggest that personal attributes, such as race and gender, may not be the only determining factors of legislative effectiveness as scholars suggest in prior research. In reality, committee-based and issue-based congressional networks also impact legislative effectiveness. More accurately, the legislative effectiveness of US congressional representatives is influenced by a combination of their race and centrality in committee-based and issue-based social networks. In particular, more easily accessible, or more popular, or black information leaders tend to have higher level of legislative effectiveness compared to their peers in committee-based social networks; while more easily accessible, or more popular, black or hispanic information leaders surrounded by prominent legislators tend to have higher level of legislative effectiveness compared to their peers in issue-based social networks.


## Reference
1. https://github.com/lsc4ss-s21/large-scale-personal-finance/blob/main/4_Pyspark_topic_modeling.ipynb
2. https://github.com/jchaskell/scraper-cr/blob/master/clean/filterCR_fix.py
3. https://github.com/unitedstates/congressional-record/tree/master/congressionalrecord
4. https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Public/2.Text_Preprocessing_with_SparkNLP_Annotators_Transformers.ipynb#scrollTo=EgdWV7yFix8e
5. https://medium.com/trustyou-engineering/topic-modelling-with-pyspark-and-spark-nlp-a99d063f1a6e
6. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.ml.clustering.LDA.html

