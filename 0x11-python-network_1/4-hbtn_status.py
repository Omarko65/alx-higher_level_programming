#!/usr/bin/python3
'''a script that fetches a url with requests'''
import requests


url = 'https://alx-intranet.hbtn.io/status'
r = requests.get(url)
print("\t- type: {}".format(type(r.text)))
print("\t- content: {}".format(r.text))
