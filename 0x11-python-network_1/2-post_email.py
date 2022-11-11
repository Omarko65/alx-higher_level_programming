#!/usr/bin/python3
''' a python script that sends a post request to a url'''
import urllib
import sys


if __name__ == '__main__':
    url = sys.argv[1]
    e_address = sys.argv[2]
    values = { 'email' : e_address }
    data = urllib.parse.urlencode(values)
    data = data.encode('utf-8')
    with urlopen(url, data) as response:
        body = response.read()
        print(body.decode('utf-8'))
