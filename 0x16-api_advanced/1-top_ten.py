#!/usr/bin/python3
"""
prints the titles of the first 10 hot posts listed for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """Return the title of the first 10 hot posts
    listed for a given subreddit."""
    try:
        url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
        headers = {
            "User-Agent": "linux:0x16.api.advanced:v1.0.0",
        }
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            posts = response.json().get('data', {}).get('children', [])
            for post in posts:
                print(post.get('data', {}).get('title', 'None'))
        else:
            print('None')
    except requests.RequestException:
        print('None')
