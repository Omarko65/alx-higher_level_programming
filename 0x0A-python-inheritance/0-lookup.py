#!/usr/bin/python3
'''lookup module definition'''


def lookup(obj):
    '''lookup returns list of available attr and method of a class obj'''
    return (dir(obj))
