#!/usr/bin/python3
"""
Module to recursively get all hot post titles for a subreddit
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively queries the Reddit API and returns a list containing the
    titles of all hot articles for a given subreddit.
    If no results are found for the given subreddit, the function returns None.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent":
        "linux:0x16.api.advanced:v1.0.0 (by /u/Large_Alternative_30)"
    }
    params = {
        "limit": 100,
        "after": after
    }
    try:
        response = requests.get(url, headers=headers,
                                params=params, allow_redirects=False)
        if response.status_code != 200:
            return None
        data = response.json().get("data", {})
        children = data.get("children", [])
        for child in children:
            hot_list.append(child["data"]["title"])
        after = data.get("after", None)
        if after is not None:
            return recurse(subreddit, hot_list, after)
        return hot_list
    except requests.RequestException:
        return None
