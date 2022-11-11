#!/usr/bin/python3
'''a script that fetches head value X-Request-id from url'''
import requests
import sys


if __name__ == '__main__':
    url = sys.argv[1]
    r = requests.get(url)
    print(r.headers[X-Request-Id])
