#!/usr/bin/python3
""" Python script that, using this REST API, for a given employe/
ID, returns information about his/her TODO list progress. """

import requests
from sys import argv


def api_requests():
    """ funcion que hace una consulta api. """
    user_id = int(argv[1])
    user_name = ""
    task_done = 0
    task_total = 0
    task_title = []
    url = "https://jsonplaceholder.typicode.com/users"

    users = requests.get("{}".format(url)).json()

    tasks = requests.get("{}/{}/todos".format(url, user_id)).json()

    for user in users:
        if user['id'] == user_id:
            user_name = user['name']

    for task in tasks:
        task_total += 1

        if task['completed'] is True:
            task_done += 1
            task_title.append(task['title'])

    print("Employee {} is done with tasks({}/{}):"
          .format(user_name, task_done, task_total))

    for task in task_title:
        print(f"\t {task}")


if __name__ == "__main__":
    api_requests()
