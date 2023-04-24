#!/usr/bin/python3

'''using this REST API, for a given employee ID, returns information about
his/her TODO list progress
'''
import requests
import sys

u_id = sys.argv[1]
res = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'
                   '&_expand=user'.format(u_id))
res = res.json()
name = res[0].get('user').get('name')
complete = [task.get('title') for task in res if task.get('completed') is True]
print('Employee {} is done with tasks {}/{}:'.format(name, len(complete),
      len(res)))
for task in complete:
    print('\t {}'.format(task))
