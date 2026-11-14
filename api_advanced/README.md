# API advanced

Python functions that query the [Reddit API](https://www.reddit.com/dev/api/)
without authentication, using a custom User-Agent and without following
redirects (invalid subreddits redirect to search results).

| File | Description |
|------|-------------|
| `0-subs.py` | `number_of_subscribers(subreddit)`: total subscribers, or 0 if invalid |
| `1-top_ten.py` | `top_ten(subreddit)`: prints the titles of the first 10 hot posts, or None |
| `2-recurse.py` | `recurse(subreddit, hot_list=[])`: recursively returns all hot post titles, or None |
| `3-count.py` | `count_words(subreddit, word_list)`: recursively counts keywords in hot post titles |
