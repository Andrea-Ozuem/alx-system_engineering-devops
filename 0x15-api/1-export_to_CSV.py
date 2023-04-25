#!/usr/bin/python3

'''Using this REST API, for a given employee ID, returns information about
his/her TODO list progress

API: https://jsonplaceholder.typicode.com/todos?userId=2&_expand=user

prints the todos associated with user
'''

import csv
import requests
import sys

if __name__ == "__main__":
    u_id = sys.argv[1]
    res = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'
                       '&_expand=user'.format(u_id))
    res = res.json()
    content = [[row.get('userId'), row.get('user').get('username'),
                row.get('completed'), row.get('title')] for row in res]
    with open('{}.csv'.format(u_id), mode='w', newline='') as csv_f:
        writer = csv.writer(csv_f, quoting=csv.QUOTE_ALL)
        writer.writerows(content)
