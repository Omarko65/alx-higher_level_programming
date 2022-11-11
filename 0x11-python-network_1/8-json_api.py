#!/usr/bin/python3
'''a script that send request and returns body of url'''
import requests
import sys


if __name__ == '__main__':
    url = 'http://0.0.0.0:5000/search_user'
    query = sys.argv[1] if len(sys.argv) > 1 else ""
    data = {'q': query}
    r = requests.post(url, data=data)
    try:
        content = r.json()
        if content:
            print("[{}] {}".format(content['id'], content['name']))
        else:
            print("No result")
    except Exception:
        print("Not a valid JSON")
