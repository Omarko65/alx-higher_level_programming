#!/usr/bin/python3
'''is_same_class module definition'''


def is_same_class(obj, a_class):
    '''a function that returns true if obj is same as a_class'''
    if obj is None or a_class is None or type(obj) is not a_class:
        return False
    if type(obj) is a_class:
        return True
