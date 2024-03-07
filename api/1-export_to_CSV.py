#!/usr/bin/python3
""" Python script to export data in the CSV format """

from sys import argv
import requests


def csv():
    """ Consulta y exporta en formato csv """

    url = "https://jsonplaceholder.typicode.com/users"
    file_name = argv[1] + ".csv"

    user = requests.get("{}/{}".format(url, argv[1])).json()
    tasks = requests.get("{}/{}/todos".format(url, argv[1])).json()

    for task in tasks:
        data = '"{}","{}","{}","{}"\n'.format(user['id'],
                                              user['username'],
                                              task['completed'],
                                              task['title'])

        with open(file_name, 'a', encoding='utf-8') as csvfile:
            csvfile.write(data)


if __name__ == "__main__":
    csv()
