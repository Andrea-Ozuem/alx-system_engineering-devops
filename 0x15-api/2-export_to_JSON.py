#!/usr/bin/python3

'''Using this REST API, for a given employee ID, returns information about
his/her TODO list progress

API: https://jsonplaceholder.typicode.com/todos?userId=2&_expand=user

prints the todos associated with user
'''

import json
import requests
import sys

if __name__ == "__main__":
    u_id = sys.argv[1]
    res = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'
                       '&_expand=user'.format(u_id))
    res = res.json()
    dic = {u_id: [{'task': row.get('title'), 'completed': row.get('completed'),
                  'username': row.get('user').get('username')} for row in res]}

    with open('{}.json'.format(u_id), mode='w') as f:
        json.dump(dic, f)
