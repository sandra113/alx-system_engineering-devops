#!/usr/bin/python3
"""
This module queries the Reddit API and
returns a list containing the titles of all hot articles for a given subreddit.
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    This function returns titles of all hot articles for a given subreddit
    """

    if hot_list and after is None:
        return hot_list

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100&after={after}"
    headers = {'User-Agent': 'YourAppName/1.0'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        for post in posts:
            title = post['data']['title']
            hot_list.append(title)
        new_after = data['data']['after']
        return recurse(subreddit, hot_list, new_after)
    elif response.status_code == 404:
        print(f"Subreddit '{subreddit}' not found.")
        return None
    else:
        print(f"Error: {response.status_code}")
        return None
