#!/usr/bin/python3
"""Function to query subscribers on a subreddit."""
import requests


def number_of_subscribers(subreddit):
    """Returns the total number of subscribers of subreddit."""
    subreddit_url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    response = requests.get(subreddit_url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return 0
    subs = response.json().get("data")
    return subs.get("subscribers")
