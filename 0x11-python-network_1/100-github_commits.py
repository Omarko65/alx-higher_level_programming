#!/usr/bin/python3
''' a pythn script that returns the last 10 commits in a repo'''
import requests
import sys


if __name__ == '__main__':
    user = sys.argv[2]
    repo = sys.argv[1]
    url = "https://api.github.com/repos/{}/{}/commits".format(user, repo)
    r = requests.get(url)
    resp = r.json()
    try:
        for i in range(10):
            print(f"{resp[i]['sha']}: {resp[i]['commit']['author']['name']}")
    except IndexError:
        pass
