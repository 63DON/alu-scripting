#!/usr/bin/python3
"""Print the titles of the first 10 hot posts of a subreddit."""
import requests

HEADERS = {"User-Agent": "linux:alu-scripting.api_advanced:v1.0"}


def top_ten(subreddit):
    """Print the titles of the first 10 hot posts, or None if invalid."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    try:
        response = requests.get(url, headers=HEADERS, params={"limit": 10},
                                allow_redirects=False, timeout=10)
        if response.status_code != 200:
            print(None)
            return
        posts = response.json().get("data", {}).get("children", [])
        if not posts:
            print(None)
            return
        for post in posts[:10]:
            print(post.get("data", {}).get("title"))
    except Exception:
        print(None)
