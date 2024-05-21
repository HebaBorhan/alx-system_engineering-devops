#!/usr/bin/python3
"""using REST API, for a given employee ID,
returns information about his/her TODO list progress"""
import json
import re
import sys
import urllib.request


url = "https://jsonplaceholder.typicode.com"

if __name__ == "__main__":
    if len(sys.argv) > 1:
        if re.fullmatch(r'\d+', sys.argv[1]):
            employee_id = int(sys.argv[1])

            # Fetch employee details
            with urllib.request.urlopen(
                    f"{url}/users/{employee_id}") as response:
                request = json.loads(response.read().decode())

            # Fetch employee's todos
            with urllib.request.urlopen(f"{url}/todos") as response:
                todo_req = json.loads(response.read().decode())

            # Extract employee name
            employee_name = request.get('name')

            # Filter tasks by employee ID
            tasks = list(filter(
                lambda x: x.get('userId') == employee_id, todo_req))

            # Filter completed tasks
            completed_tasks = list(filter(lambda x: x.get('completed'), tasks))

            # Print the result
            print("Employee {} is done with tasks({}/{}):".format(
                employee_name, len(completed_tasks), len(tasks)))
            for task in completed_tasks:
                print('\t {}'.format(task.get('title')))
