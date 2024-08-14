#!/usr/bin/python3
"""Function to count words in all hot posts of a given Reddit subreddit."""
import requests


def count_words(subreddit, word_list, instances=None, after="", count=0):
    """Prints counts of given words found in hot posts of a given subreddit."""
    if instances is None:
        instances = {}

    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }

    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)
        response.raise_for_status()
        results = response.json().get("data")
        if results is None:
            return

        after = results.get("after")
        count += results.get("dist", 0)
        for c in results.get("children"):
            title = c.get("data").get("title").lower().split()
            for word in word_list:
                times = title.count(word.lower())
                if times > 0:
                    instances[word] = instances.get(word, 0) + times

        if after is None:
            if len(instances) == 0:
                return
            instances = sorted(instances.items(), key=lambda kv: (-kv[1], kv[0]))
            [print("{}: {}".format(k, v)) for k, v in instances]
        else:
            count_words(subreddit, word_list, instances, after, count)
    
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return
