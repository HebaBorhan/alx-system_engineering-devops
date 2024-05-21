#!/usr/bin/python3
"""using REST API, for a given employee ID,
returns information about his/her TODO list progress."""
import re
import requests
import sys


if __name__ == "__main__":
    URL = "https://jsonplaceholder.typicode.com/"
    EMPLOYEE_DATA = requests.get(URL + "users/{}".format(sys.argv[1])).json()
    EMPLOYEE_NAME = EMPLOYEE_DATA.get("name")

    Tasks_4_emply = requests.get(
        URL + "todos/", params={"userId": sys.argv[1]}).json()
    COMPLETED_TASKS = []
    for TASK_TITLE in Tasks_4_emply:
        if TASK_TITLE.get("completed"):
            COMPLETED_TASKS.append(TASK_TITLE.get("title"))
    len_T_C = (len(COMPLETED_TASKS))
    len_e_t_c = (len(Tasks_4_emply))
    print("Employee {} is done with tasks({}/{}):".format(
        EMPLOYEE_NAME, len_T_C, len_e_t_c))
    for task in COMPLETED_TASKS:
        print("\t {}".format(TASK_TITLE))
