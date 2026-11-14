#!/usr/bin/python3
"""Query the Reddit API for the number of subscribers of a subreddit."""
import requests

HEADERS = {"User-Agent": "linux:alu-scripting.api_advanced:v1.0"}


def number_of_subscribers(subreddit):
    """Return the total number of subscribers, or 0 if invalid."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    try:
        response = requests.get(url, headers=HEADERS,
                                allow_redirects=False, timeout=10)
        if response.status_code != 200:
            return 0
        return response.json().get("data", {}).get("subscribers") or 0
    except Exception:
        return 0
