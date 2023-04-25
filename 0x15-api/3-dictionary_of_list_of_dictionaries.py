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
    res = requests.get('https://jsonplaceholder.typicode.com/users')
    res = res.json()
    dic_do = {}
    for user in res:
        u_id = user.get('id')
        rows = requests.get('https://jsonplaceholder.typicode.com/todos?'
                            'userId={}&_expand=user'.format(u_id)).json()
        dic = {u_id: [{'username': row.get('user').get('username'), 'task':
               row.get('title'), 'completed': row.get('completed')} for row
               in rows]}
        dic_do.update(dic)

    with open('todo_all_employees.json', mode='w') as f:
        json.dump(dic_do, f)
