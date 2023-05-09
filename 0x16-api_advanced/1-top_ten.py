#!/usr/bin/python3

'''queries the Reddit API and returns the number of subscribers (not active
users, total subscribers) for a given subreddit. If an invalid subreddit is
given, the function should return 0.
'''

import requests


def top_ten(subreddit):
    limit = 10
    url = "https://www.reddit.com/r/{}/top.json?limit={}".format(subreddit,
                                                                 limit)
    res = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'},
                       allow_redirects=False)
    if res.status_code != 200:
        print('None')
        return
    res = res.json()
    if type(res) is not dict:
        print('None')
        return
    res = res.get('data', 0).get('children', 0)
    if res:
        [print(res_t.get('data').get('title')) for res_t in res]
    else:
        print('None')
