#!/usr/bin/python3
"""
Queries the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """A route that returns the number of subscribers"""
    req = requests.get(
        "https://www.reddit.com/r/{}/about.json".format(subreddit),
        headers={"User-Agent": "Custom"},
    )
    if req.status_code == 200:
        return req.json().get("data").get("subscribers")
    else:
        return 0
