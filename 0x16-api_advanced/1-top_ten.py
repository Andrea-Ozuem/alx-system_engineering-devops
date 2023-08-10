#!/usr/bin/python3
"""
queries the Reddit API and returns the number of subscribers
"""
import requests


def top_ten(subreddit):
    '''prints the titles of the first 10 hot posts listed for
    a given subreddit'''
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'My User Agent 1.0'}
    try:
        r = requests.get(url, headers=headers, params={'limit': 10},
                         allow_redirects=False)
        if r.status_code == 200:
            data = r.json()
            data = data.get('data').get('children')
            for item in data:
                print(item.get('data').get('title'))
        else:
            print('None')
    except Exception:
        print('None')
