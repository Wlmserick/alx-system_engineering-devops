#!/usr/bin/python3
"""Defines a function that queries the reddit API"""

import requests


def number_of_subscribers(subreddit):
    """Returns the  number of subscribers (not active users,
    total subscribers) for a given subreddit
    """
    subreddit_url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'linux:0x16.api.advanced:v1.0.0(by/u/bdov_)'}
    try:
        response = requests.get(subreddit_url, headers=headers,
                                allow_redirects=False).json()

        return response.get('data').get('subscribers')
    except Exception:
        return 0
