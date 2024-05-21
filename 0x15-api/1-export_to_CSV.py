#!/usr/bin/python3
"""export data in the CSV format"""
import csv
import requests
import sys


url = "https://jsonplaceholder.typicode.com"

if __name__ == "__main__":
    if len(sys.argv) > 1:
        EMPLOYEE_ID = int(sys.argv[1])

        # Fetch employee details
        employee_response = requests.get(f"{url}/users/{EMPLOYEE_ID}")
        EMPLOYEE_DATA = employee_response.json()

        # Extract employee name
        EMPLOYEE_NAME = employee_response.json().get('name')

        # Fetch user's TODO list
        tasks_response = requests.get(
            f"{url}/todos", params={"userId": EMPLOYEE_ID})
        tasks = tasks_response.json()

        # Write to CSV file
        file = f"{EMPLOYEE_ID}.csv"
        with open(file, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
            for task in tasks:
                writer.writerow(
                    [EMPLOYEE_ID, EMPLOYEE_NAME, task.get(
                        'completed'), task.get('title')])
