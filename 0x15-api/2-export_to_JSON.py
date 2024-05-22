#!/usr/bin/python3
"""export data in the CSV format"""
import csv
import json
import requests
import sys


url = "https://jsonplaceholder.typicode.com"

if __name__ == "__main__":
    USER_ID = int(sys.argv[1])

    # Fetch employee details
    EMPLOYEE_DATA = requests.get(
        "{}/users/{}".format(url, USER_ID)).json()

    # Extract employee name
    USERNAME = EMPLOYEE_DATA.get('username')

    # Fetch user's TODO list
    response = requests.get(
        f"{url}/todos", params={"userId": USER_ID})
    response.raise_for_status()
    tasks = response.json()

    tasks_list = [{"task": task.get('title'), "completed": task.get(
        'completed'), "username": USERNAME} for task in tasks]

    # Data to be written to JSON file
    data = {str(USER_ID): tasks_list}

    # JSON file
    file = f"{USER_ID}.json"
    with open(file, 'w') as jsonfile:
        json.dump(data, jsonfile, indent=4)
