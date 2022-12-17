#!/usr/bin/python3
''' a script that takes a url sends request and displays header variable'''
import urllib.request
import sys


if __name__ == '__main__':
    '''module definition'''
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        print(response.headers.get('X-Request-Id', None))
