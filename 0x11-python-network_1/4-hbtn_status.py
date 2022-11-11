#!/usr/bin/python3
'''a script that fetches a url with requests'''
import requests


r = requests.get('https://alx-intranet.hbtn.io/status')
print("\t- type: ".format(type(r.text)))
print("\t- content: ".format(r.text))
