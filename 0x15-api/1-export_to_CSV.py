#!/usr/bin/python3
"""export data in the CSV format"""
import csv
import requests
import sys


url = "https://jsonplaceholder.typicode.com"

if __name__ == "__main__":
    if len(sys.argv) > 1:
        employee_id = int(sys.argv[1])

        # Fetch employee details
        employee_response = requests.get(f"{url}/users/{employee_id}")
        EMPLOYEE_DATA = employee_response.json()

        # Extract employee name
        EMPLOYEE_NAME = employee_response.json().get('name')

        # Fetch user's TODO list
        tasks_response = requests.get(
            f"{url}/todos", params={"userId": employee_id})
        tasks = tasks_response.json()

        # Write to CSV file
        with open(f"{employee_id}.csv", 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(
                ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
            for task in tasks:
                writer.writerow(
                    [employee_id, EMPLOYEE_NAME, task.get(
                        'completed'), task.get('title')])
