#!/usr/bin/python3
'''a script that fetches head value X-Request-id from url'''
import requests
import sys


if __name__ == '__main__':
    url = sys.argv[1]
    e_address = sys.argv[2]
    mail = {'email': e_address}
    r = requests.post(url, data= mail)
    print(r.text)
