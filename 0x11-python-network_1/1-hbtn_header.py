#!/usr/bin/python3
''' a python script that request value of X-Request ID in header '''
from urllib.request import urlopen
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    with urlopen(url) as response:
        print(response.headers.get('X-Request-Id', None))
