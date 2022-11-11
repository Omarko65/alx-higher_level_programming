#!/usr/bin/python3
''' a python script that sends request to url and print body'''
import urllib.request
import urllib.error
import sys


if __name__ == '__main__':
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        try:
            body = response.read()
            print(body.decode('utf-8'))
        except urllib.error.HTTPError as e:
            print('Error code: {}'.format(e.code))
