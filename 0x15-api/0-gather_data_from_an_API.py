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
            try:
                with urllib.request.urlopen(f"{url}/users/{employee_id}") as response:
                    req = json.loads(response.read().decode())
            except urllib.error.HTTPError as e:
                print(f"Error: Employee with ID {employee_id} not found.")
                sys.exit(1)

            # Fetch employee's todos
            with urllib.request.urlopen(f"{url}/todos") as response:
                task_req = json.loads(response.read().decode())

            # Extract employee name
            emp_name = req.get('name')

            # Filter tasks by employee ID
            tasks = list(filter(lambda x: x.get('userId') == employee_id, task_req))

            # Filter completed tasks
            completed_tasks = list(filter(lambda x: x.get('completed'), tasks))

            # Print the result
            print(f"Employee {emp_name} is done with tasks({len(completed_tasks)}/{len(tasks)}):")
            for task in completed_tasks:
                print(f"\t {task.get('title')}")
        else:
            print("Error: Employee ID must be an integer.")
    else:
        print("Usage: python script.py <employee_id>")
