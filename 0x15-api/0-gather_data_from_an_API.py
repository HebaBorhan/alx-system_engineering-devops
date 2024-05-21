#!/usr/bin/python3
"""using REST API, for a given employee ID,
returns information about his/her TODO list progress"""
import re
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"

    if len(sys.argv) > 1:
        if re.fullmatch(r'\d+', sys.argv[1]):
            id = int(sys.argv[1])
            req = requests.get('{}/users/{}'.format(url, id)).json()
            task_req = requests.get('{}/todos'.format(url)).json()
            emp_name = req.get('name')
            tasks = list(filter(lambda x: x.get('userId') == id, task_req))
            completed_tasks = list(filter(lambda x: x.get('completed'), tasks))
            print(
                'Employee {} is done with tasks({}/{}):'.format(
                    emp_name,
                    len(completed_tasks),
                    len(tasks)
                )
            )
            if len(completed_tasks) > 0:
                for task in completed_tasks:
                    print('\t {}'.format(task.get('title')))
