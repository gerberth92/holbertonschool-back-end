#!/usr/bin/python3
""" Este modulo obtiene datos de una api. """

import requests
from sys import argv
import csv


def api():
    """ Esta funcion hace una consulta a una api. """

    url = "https://jsonplaceholder.typicode.com/users/"

    user = requests.get(url + argv[1]).json()
    todo = requests.get(url + argv[1] + '/todos').json()
    name = user.get('name')
    # doc = str(user.get('id')) + ".csv"

    with open("{}.csv".format(argv[1]), "w") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for employee in todo:
            user_id = argv[1]
            username = name
            task_com = employee.get('completed')
            task_title = employee.get('title')

            fila = [user_id, username, task_com, task_title]

            writer.writerow(fila)

if __name__ == '__main__':
    api()
