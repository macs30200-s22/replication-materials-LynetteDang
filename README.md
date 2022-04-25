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

You can then use the `generate_result` function in the `analysis` module will reproduce all the findings (one scatterplot, two histograms, and one csv) under subdirectory ```result``` 


```python
python3 analysis.py
```



[Distribution of Number of Connections for All Legislators](https://github.com/macs30200-s22/replication-materials-LynetteDang/blob/master/result/hist_conn.png)



Alternatively, to replicate the analysis and produce all of the figures and quantitative analyses from the (hypothetical) publication that this code supplements, build and run the `Dockerfile` included in this repository via the instructions in the file).
