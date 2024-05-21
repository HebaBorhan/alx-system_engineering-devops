#!/usr/bin/python3
"""using REST API, for a given employee ID,
returns information about his/her TODO list progress"""
import json
import re
import sys
import urllib


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
            EMPLOYEE_NAME = request.get('name')

            # Filter tasks by employee ID
            TOTAL_NUMBER_OF_TASKS = list(filter(
                lambda x: x.get('userId') == employee_id, todo_req))

            # Filter done tasks
            NUMBER_OF_DONE_TASKS = list(
                filter(lambda x: x.get('completed'), TOTAL_NUMBER_OF_TASKS))

            # Print the result
            print(
                "Employee {} is done with tasks({}/{}):".format(
                    EMPLOYEE_NAME, len(
                        NUMBER_OF_DONE_TASKS), len(TOTAL_NUMBER_OF_TASKS)))
            for task in NUMBER_OF_DONE_TASKS:
                print('\t {}'.format(task.get('title')))
