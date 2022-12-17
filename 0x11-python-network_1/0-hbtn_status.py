#!/usr/bin/python3
''' a script that fetches url using urllib'''
import urllib.request


if __name__ == '__main__':
    '''script definition'''
    url = 'https://alx-intranet.hbtn.io/status'
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        html = response.read()
        print('Body reponse:')
        print('\t- type: {}'.format(type(html)))
        print('\t- content: {}'.format(html))
        print('\t- utf8 content: {}'.format(html.decode('utf-8')))
