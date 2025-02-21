#!/usr/bin/python3
# get subs
from requests import get
from sys import argv

def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts for a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'MyRedditBot/0.1'}
    params = {'limit': 10}  # Fetch only the first 10 posts

    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    if response.status_code != 200:
        print(None)
        return

    try:
        data = response.json()
        posts = data.get("data", {}).get("children", [])

        if not posts:
            print(None)
            return

        for post in posts:
            print(post["data"]["title"])
    except ValueError:
        print(None)

