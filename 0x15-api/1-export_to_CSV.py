#!/usr/bin/python3
"""export data in the CSV format"""
import csv
import requests
import sys


url = "https://jsonplaceholder.typicode.com"

if __name__ == "__main__":
    USER_ID = int(sys.argv[1])

    # Fetch employee details
    EMPLOYEE_DATA = requests.get(
        "{}/users/{}".format(url, USER_ID)).json()

    # Extract employee name
    USERNAME = EMPLOYEE_DATA.get('name')

    # Fetch user's TODO list
    response = requests.get(
        f"{url}/todos", params={"userId": USER_ID})
    response.raise_for_status()
    tasks = response.json()

    # CSV file
    file = f"{USER_ID}.csv"
    with open(file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in tasks:
            TASK_COMPLETED_STATUS = task.get('completed')
            TASK_TITLE = task.get('title')
            writer.writerow(
                [USER_ID, USERNAME, TASK_COMPLETED_STATUS, TASK_TITLE])
