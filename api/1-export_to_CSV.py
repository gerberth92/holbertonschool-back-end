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
    doc = str(user.get('id')) + ".csv"

    with open(doc, 'a', encoding='UTF-8') as file:
        for item in todo:
            file.write('"{}","{}","{}","{}"\n'.format(user.get('id'), name,
                                                      item.get('completed'),
                                                      item.get('title')))


if __name__ == '__main__':
    api()
