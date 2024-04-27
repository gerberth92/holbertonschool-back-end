#!/usr/bin/python3
""" Este modulo obtiene datos de una api. """

import requests
from sys import argv
from json import dump


def api():
    """ Esta funcion hace una consulta a una api. """

    url = "https://jsonplaceholder.typicode.com/users/"

    user = requests.get(url + argv[1]).json()
    todo = requests.get(url + argv[1] + '/todos').json()
    doc = str(user.get('id')) + ".json"
    info = []

    for item in todo:
        dic = {}
        dic['task'] = item.get('title')
        dic['completed'] = item.get('completed')
        dic['username'] = user.get('username')
        info.append(dic)

    with open(doc, 'w', encoding='UTF-8') as file:
        dump({str(user.get('id')): info}, file)


if __name__ == '__main__':
    api()
