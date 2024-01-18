#!/usr/bin/python3
"""
This module retrieves the number of subscribers from a given subredit
"""
import requests
from sys import argv


def number_of_subscribers(subreddit):
    """
    returns the number of subscribers from a given subredit
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    headers = {'User-Agent': 'Sandra'}

    try:
        return url.get('data').get('subscribers')
    except Exception:
        return 0


if __name__ == "__main__":
    number_of_subscribers(argv[1])
