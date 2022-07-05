#!/usr/bin/python3
'''read_file module definition'''


def read_file(filename=""):
    '''read_file function definition'''
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
