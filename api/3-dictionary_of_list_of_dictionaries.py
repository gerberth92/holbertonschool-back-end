#!/usr/bin/python3
""" Este modulo obtiene datos de una api. """

import requests
from json import dump


def api():
    """ Esta funcion hace una consulta a una api. """

    url = "https://jsonplaceholder.typicode.com/users/"

    users = requests.get(url).json()
    dic = {}

    for u in users:
        lista = []
        todo = requests.get(url + str(u.get('id')) + '/todos').json()

        for item in todo:
            info = {}
            info['username'] = u.get('username')
            info['task'] = item.get('title')
            info['completed'] = item.get('completed')
            lista.append(info)

        dic[u.get('id')] = lista

    with open('todo_all_employees.json', 'w', encoding='UTF-8') as file:
        dump(dic, file)


if __name__ == '__main__':
    api()
