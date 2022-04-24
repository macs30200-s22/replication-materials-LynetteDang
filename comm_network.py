"""
Name: comm_network.py
Author: Lynette Dang

Crawl the Ballotpedia committee page and generates a json file consisting of the
committees for the 116th Congress and their members
"""

# import scraping libraries
import requests
from bs4 import BeautifulSoup

# import other libraries
import json
from util import web_crawl, web_scrape, construct_network

url = "https://ballotpedia.org/116th_United_States_Congress"
headers = {"User-Agent": "web scraper for classroom purposes"}
results = requests.get(url, headers=headers)
soup = BeautifulSoup(results.text, "html")  # html.parser
committees = {}
comm_members_raw = []
pat = "\>.*\<"
network = {}
committee_links = web_crawl(soup, committees)
committees = web_scrape(committee_links, committees, headers)
construct_network(committees, network)
with open("comm_network.json", "w") as outfile:
    json.dump(network, outfile)
