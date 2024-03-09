#!/usr/bin/python3
""" Python script to export data in the JSON format. """

from json import dump
from sys import argv
import requests


def json():
    """ Exporta un documento .json. """
    url = "https://jsonplaceholder.typicode.com/users"
    task_list = []

    user = requests.get("{}/{}".format(url, argv[1])).json()
    tasks = requests.get("{}/{}/todos".format(url, argv[1])).json()

    for task in tasks:
        task_dict = {"task": task['title'], "completed": task['completed'],
                     "username": user['username']}

        task_list.append(task_dict)

    data = {user['id']: task_list}

    with open(argv[1] + ".json", 'w', encoding='utf-8') as jsonfile:
        dump(data, jsonfile)


if __name__ == "__main__":
    json()
