#!/usr/bin/python3
'''is_kind_of_class module definition'''


def is_kind_of_class(obj, a_class):
    '''a function that returns true if obj an instance is same as a_class'''
    if a_class is None or isinstance(obj, a_class) is not True:
        return False
    if isinstance(obj, a_class) is True:
        return True
