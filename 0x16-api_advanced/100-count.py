#!/usr/bin/python3
"""
Module to count keyword occurrences in subreddit hot posts
"""

import requests
from collections import Counter


def count_words(subreddit, word_list, hot_list=[], after=None):
    """
    Recursively queries the Reddit API and counts the occurrences of
    given keywords in the titles of all hot articles for a given subreddit.
    Prints the count sorted by occurrences in descending order and
    alphabetically by keyword in ascending order if counts are equal.
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
            return count_words(subreddit, word_list, hot_list, after)

        # Now we process the hot_list to count the words
        word_count = Counter()
        for title in hot_list:
            words = title.lower().split()
            for word in word_list:
                word_count[word.lower()] += words.count(word.lower())

        # Filter out words with zero occurrences
        word_count = {k: v for k, v in word_count.items() if v > 0}

        # Sort the word count dictionary
        sorted_word_count = sorted(word_count.items(),
                                   key=lambda item: (-item[1], item[0]))

        # Print the results
        for word, count in sorted_word_count:
            print(f"{word}: {count}")

    except requests.RequestException:
        return None
