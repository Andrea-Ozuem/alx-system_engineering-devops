#!/usr/bin/python3
'''queries the Reddit API
and prints the titles of the first 10 hot posts listed for
a given subreddit
'''
import requests


def top_ten(subreddit):
    """ Queries to Reddit API """
    limit = 10
    url = "https://www.reddit.com/r/{}/top.json?limit={}".format(subreddit,
                                                                 limit)
    res = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'},
                       allow_redirects=False)
    if res.status_code != 200:
        print('None')
        return
    res = res.json()
    res = res.get('data', 0).get('children', 0)
    if res:
        [print(res_t.get('data').get('title')) for res_t in res]
    else:
        print('None')
