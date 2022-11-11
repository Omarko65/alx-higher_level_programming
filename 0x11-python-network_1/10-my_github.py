#!/usr/bin/python3
'''a script that send request and returns body of url'''
import requests
import sys


if __name__ == '__main__':
    user = sys.argv[1]
    passwd = sys.argv[2]
    url = 'https://api.github.com/user'
    r = requests.get(url, auth=(user, passwd))
    try:
        print(r.json().get('id'))
    except Exception:
        print("None")

