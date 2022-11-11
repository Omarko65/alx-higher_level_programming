#!/usr/bin/python3
''' a script that fetches alx url '''
import urllib.request


if __name__ == "__main__":
url = 'https://alx-intranet.hbtn.io/status'
req = urllib.request.Request(url)
with urllib.request.urlopen(req) as response:
    the_page = response.read()
    print('Body response:')
    print("\t- type: <class 'bytes'>")
    print("\t- content: b'OK'")
    print("\t- utf8 content: OK")
