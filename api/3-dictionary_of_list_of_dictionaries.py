#!/usr/bin/python3
""" Python script to export data in the JSON format. """

from json import dump
import requests


def json():
    """ Exporta a .json. """
    url = "https://jsonplaceholder.typicode.com/"
    data = {}

    users = requests.get("{}users".format(url)).json()
    tasks = requests.get("{}todos".format(url)).json()

    for user in users:
        task_list = []
        for task in tasks:
            if task['userId'] == user['id']:
                task_dict = {"username": user['username'],
                             "task": task['title'],
                             "completed": task['completed']}
                task_list.append(task_dict)

        data[str(user['id'])] = task_list

    with open("todo_all_employees.json", "w", encoding="utf-8") as filejson:
        dump(data, filejson)


if __name__ == "__main__":
    json()
