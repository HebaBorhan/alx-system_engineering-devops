#!/usr/bin/python3
"""using REST API, for a given employee ID,
returns information about his/her TODO list progress"""
import json
import requests
import sys


if __name__ == "__main__":
    URL = "https://jsonplaceholder.typicode.com/"

    # Fetch employee details
    EMPLOYEE_DATA = requests.get(URL + "users/{}".format(sys.argv[1])).json()
    EMPLOYEE_NAME = EMPLOYEE_DATA.get("name")

    # Fetch employee's todos
    TASKS_FOR_EMPLOYEE = requests.get(
        URL + "todos", params={"userId": sys.argv[1]}).json()

    # Filter completed tasks
    COMPLETED_TASKS = [task.get(
        "title") for task in TASKS_FOR_EMPLOYEE if task.get("completed")]

    # Calculate the number of completed tasks and total tasks
    NUMBER_OF_DONE_TASKS = len(COMPLETED_TASKS)
    TOTAL_NUMBER_OF_TASKS = len(TASKS_FOR_EMPLOYEE)

    # Print the result
    print("Employee {} is done with tasks({}/{}):".format(
        EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))

    for task in COMPLETED_TASKS:
        print("\t {}".format(task))
