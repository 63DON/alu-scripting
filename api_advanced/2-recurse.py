#!/usr/bin/python3
"""Recursively return the titles of all hot posts of a subreddit."""
import requests

HEADERS = {"User-Agent": "linux:alu-scripting.api_advanced:v1.0"}


def recurse(subreddit, hot_list=[], after=None):
    """Return a list of all hot post titles, or None if invalid."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    params = {"limit": 100, "after": after}
    try:
        response = requests.get(url, headers=HEADERS, params=params,
                                allow_redirects=False, timeout=10)
        if response.status_code != 200:
            return None
        data = response.json().get("data", {})
    except Exception:
        return None

    titles = [post.get("data", {}).get("title")
              for post in data.get("children", [])]
    hot_list = hot_list + titles

    after = data.get("after")
    if after is not None:
        return recurse(subreddit, hot_list, after)
    return hot_list if hot_list else None
