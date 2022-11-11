#!/usr/bin/python3
''' a scrip that list 10most recents commits from a repo'''
import sys
import requests


if __name__ == ' __main__':
    url = 'https://api.github.com/repos/{}/{}/commits'.format(
            sys.argv[2], sys.argv[1])
    r = requests.get(url)
    commit = r.json()
    try:
        for i in range(10):
            print(f"{commits[i]['sha']}: {commits[i]['commit']['author']['name']}")
    except IndexError:
        pass
