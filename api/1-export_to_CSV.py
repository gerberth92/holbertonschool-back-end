#!/usr/bin/python3
""" Este modulo obtiene datos de una api. """

import csv
import requests
from sys import argv


def api():
    """ Esta funcion hace una consulta a una api. """

    url = "https://jsonplaceholder.typicode.com/"

    id = argv[1]
    user = requests.get(url + 'users/{}'.format(id)).json()
    todo = requests.get(url + 'todos', params={"userId": id}).json()

    with open("{}.csv".format(id), "w") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for employee in todo:
            user_id = id
            username = user.get('username')
            task_com = employee.get('completed')
            task_title = employee.get('title')

            fila = [user_id, username, task_com, task_title]

            writer.writerow(fila)


if __name__ == '__main__':
    api()
