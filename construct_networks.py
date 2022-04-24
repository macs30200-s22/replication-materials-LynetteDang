"""
Name: construct_networks.py
Author: Lynette Dang

Crawl the Ballotpedia committee page and generates json files consisting of the
committees for the 116th Congress, their members, and the connections between
members
"""

# import scraping libraries
import requests
from bs4 import BeautifulSoup

# import other libraries
import json
from util import web_crawl, web_scrape, construct_committee_network, construct_ind_network

url = "https://ballotpedia.org/116th_United_States_Congress"
headers = {"User-Agent": "web scraper for classroom purposes"}
results = requests.get(url, headers=headers)
soup = BeautifulSoup(results.text, "html")  # html.parser
committees = {}
comm_members_raw = []
pat = "\>.*\<"
committee_links = web_crawl(soup, committees)
committees = web_scrape(committee_links, committees, headers)
comm_network = construct_committee_network(committees)
ind_network = construct_ind_network(comm_network)
with open("comm_network.json", "w") as outfile1:
    json.dump(comm_network, outfile1)
with open("ind_network.json", "w") as outfile2:
    json.dump(ind_network, outfile2)
