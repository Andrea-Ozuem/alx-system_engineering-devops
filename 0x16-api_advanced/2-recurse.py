#!/usr/bin/python3
"""
queries the Reddit API and returns the number of subscribers
"""
import requests


def recurse(subreddit, hot_list=[])
    '''Recursuvely executes task 1'''
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'My User Agent 1.0'}
    if not hot_list:
        try:
            r = requests.get(url, headers=headers, pa
                             allow_redirects=False)
            if r.status_code == 200:
                data = r.json()
                data = data.get('data').get('children')
            else:
                return None
        except Exception:
            return None
    return recurse(subreddit, hot_list)
