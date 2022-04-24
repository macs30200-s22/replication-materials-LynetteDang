"""
Name: comm_network.py
Author: Lynette Dang

Utility functions to help construct the committee-based networks
"""
# import scraping libraries
import requests
from bs4 import BeautifulSoup


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


def construct_network(committees, network):
    """
    Clean up and construct the networks based on the dictionary returned by
    web_scrape

    Inputs:
        committees: a dictionary with keys being the name of the committee and
        values being the names of its members, this dictionary will need further
        clean up
        network: an empty dictionary to populate
    Outputs:
        network: a dictionary with keys being the name of the committee and
        values being the names of its members, all cleaned up
    """
    for comm, mems in committees.items():
        network[comm] = []
        # some regex cleanup to do, because scraped member names contain their positions in the committee as well
        for mem in mems:
            val = mem.text
            if " Ranking Member" in val:
                val = val.replace(" Ranking Member", "")
            elif " Vice Chairman" in val:
                val = val.replace(" Vice Chairman", "")
            elif " Vice" in val:
                val = val.replace(" Vice", "")
            elif " Chair" in val:
                val = val.replace(" Chair", "")
            elif " Vice Chair" in val:
                val.replace(" Vice Chair", "")
            else:
                pass
            network[comm].append(val)
