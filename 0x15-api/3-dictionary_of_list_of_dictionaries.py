#!/usr/bin/python3
"""export data in the JSON format"""
import json
import requests
import sys


url = "https://jsonplaceholder.typicode.com"

if __name__ == "__main__":
    # Fetch all users
    users_response = requests.get(f"{url}/users")
    users_response.raise_for_status()
    users = users_response.json()

    all_tasks = {}

    # Iterate over each user
    for user in users:
        USER_ID = user.get('id')
        USERNAME = user.get('username')

        # Fetch user's TODO list
        todos_response = requests.get(
            f"{url}/todos", params={"userId": USER_ID})
        todos_response.raise_for_status()
        tasks = todos_response.json()

        tasks_list = [{"username": USERNAME, "task": task.get(
            'title'), "completed": task.get('completed')} for task in tasks]

        # Add tasks to the all_tasks dictionary
        all_tasks[str(USER_ID)] = tasks_list

    # JSON file
    file = 'todo_all_employees.json'
    with open(file, 'w') as jsonfile:
        json.dump(all_tasks, jsonfile, indent=4)
