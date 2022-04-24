"""
Name: util.py
Author: Lynette Dang

Utility functions to help construct the committee-based networks
"""
# import scraping libraries
import requests
from bs4 import BeautifulSoup
import re


def web_crawl(soup, committees):
    """
    Crawl the Ballotpedia committee page and save the links to each committee
    in the 116th Congress into a list

    Inputs:
        soup: souped results from the parent Ballotpedia link
        committees: an empty dictionary to populate
    Outputs:
        committee_links: a list of links to each committee
    """
    committee_links = []
    for element in soup.find_all('a', href=True):
        if element.get('title'):
            if "Committee" in element.get('title') and "United" in element.get('title') and "Deficit" not in element.get('title'):
                committee_links.append(
                    "https://ballotpedia.org" + element['href'])
                committees[element['href'].replace("/United", "United")] = []
    return committee_links


def web_scrape(committee_links, committees, headers):
    """
    Scrape all links in the list of links to each committee and extract the
    names of the members, store this information in a dictionary "committee"

    Inputs:
        committee_links: a list of links to each committee
        committees: a dictionary with keys being the committee names
                                but no values
        headers: header for the request
    Outputs:
        committees: a dictionary with keys being the name of the committee and
        values being the names of its members, this dictionary will need further
        clean up
    """
    for link in committee_links:
        results = requests.get(link, headers=headers)
        soup = BeautifulSoup(results.text, "html")
        comm_members_raw = soup.find_all(
            "div", class_="congressional-committees")[1]
        committees[link.replace("https://ballotpedia.org/", "")
                   ] = comm_members_raw.find_all("li")
    return committees


def construct_committee_network(committees):
    """
    Clean up and construct the networks based on the dictionary returned by
    web_scrape, unit of analysis is committee

    Inputs:
        committees: a dictionary with keys being the name of the committee and
        values being the names of its members, this dictionary will need further
        clean up
    Outputs:
        network: a dictionary with keys being the name of the committee and
        values being the names of its members, all cleaned up
    """
    network = {}
    for comm, mems in committees.items():
        network[comm] = []
        # some regex cleanup to do, because scraped member names contain their positions in the committee as well
        for mem in mems:
            val = mem.text
            val = re.sub(r'\s+$', '', val)
            if " Ranking Member" in val:
                val = val.replace(" Ranking Member", "")
            if " Vice Chairman" in val:
                val = val.replace(" Vice Chairman", "")
            if " Vice" in val:
                val = val.replace(" Vice", "")
            if " Chair" in val:
                val = val.replace(" Chair", "")
            if " Vice Chair" in val:
                val.replace(" Vice Chair", "")
            if " Ex Officio" in val:
                val.replace(" Ex Officio", "")
            if " Interim chairman" in val:
                val.replace(" Interim chairman", "")
            network[comm].append(val)
    return network


def construct_ind_network(network):
    """
    Clean up and construct a dictionary for individual legislators' connections

    Inputs:
        network: a dictionary with keys being the name of the committee and
        values being the names of its members, all cleaned up
    Outputs:
        ind_network: a dictionary with keys being individual legislators, and
        values being the number of inner-committee connections one has
    """

    ind_network = {}
    for com, mems in network.items():
        for mem in mems:
            if mem not in ind_network:
                ind_network[mem] = len(network[com]) - 1
            else:
                ind_network[mem] = ind_network[mem] + len(network[com]) - 1
    return ind_network
