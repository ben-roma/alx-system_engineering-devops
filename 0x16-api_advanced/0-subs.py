#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0"
    }
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code != 200:
            return 0
        data = response.json().get("data", {})
        return data.get("subscribers", 0)
    except requests.RequestException as e:
        print(f"Request failed: {e}")
        return 0
    except ValueError as e:
        print(f"Error parsing JSON: {e}")
        return 0


if __name__ == "__main__":
    subreddit = input("Enter subreddit name: ")
    print("Number of subscribers:", number_of_subscribers(subreddit))
