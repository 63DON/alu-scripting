#!/usr/bin/python3
"""Recursively count keywords in the titles of a subreddit's hot posts."""
import requests

HEADERS = {"User-Agent": "linux:alu-scripting.api_advanced:v1.0"}


def print_counts(counts):
    """Print counts sorted by count (descending), then word (A to Z)."""
    ordered = sorted(counts.items(), key=lambda item: (-item[1], item[0]))
    for word, count in ordered:
        if count > 0:
            print("{}: {}".format(word, count))


def count_words(subreddit, word_list, after=None, counts=None):
    """Print a sorted count of the given keywords in hot post titles."""
    if counts is None:
        counts = {}
        for word in word_list:
            counts[word.lower()] = 0

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    params = {"limit": 100, "after": after}
    try:
        response = requests.get(url, headers=HEADERS, params=params,
                                allow_redirects=False, timeout=10)
        if response.status_code != 200:
            if after is not None:
                print_counts(counts)
            return
        data = response.json().get("data", {})
    except Exception:
        if after is not None:
            print_counts(counts)
        return

    keywords = [word.lower() for word in word_list]
    for post in data.get("children", []):
        title_words = post.get("data", {}).get("title", "").lower().split()
        for word in counts:
            # Duplicate keywords in word_list add up their counts
            counts[word] += title_words.count(word) * keywords.count(word)

    after = data.get("after")
    if after is not None:
        return count_words(subreddit, word_list, after, counts)
    print_counts(counts)
