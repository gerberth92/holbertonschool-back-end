#!/usr/bin/python3
""" Este modulo obtiene datos de una api. """

import requests
from sys import argv


def api():
    """ Esta funcion hace una consulta a una api. """

    url = "https://jsonplaceholder.typicode.com/users/"

    user = requests.get(url + argv[1]).json()
    todo = requests.get(url + argv[1] + '/todos').json()
    name = user.get('name')
    contador = 0
    tareas_completas = []

    for item in todo:
        contador += 1
        if item.get('completed') is True:
            tareas_completas.append(item['title'])

    print(f"Employee {name} is done with tasks"
          f"({len(tareas_completas)}/{contador}):")

    print("\t " + "\n\t ".join(tareas_completas))


if __name__ == '__main__':
    api()
