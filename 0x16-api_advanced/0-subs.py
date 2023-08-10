#!/usr/bin/python3
"""
queries the Reddit API and returns the number of subscribers
"""
import requests


def number_of_subscribers(subreddit):
    '''Subscriber function'''
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'My User Agent 1.0'}
    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        data = r.json()
        return data.get('data').get('subscribers')
    else:
        return 0
