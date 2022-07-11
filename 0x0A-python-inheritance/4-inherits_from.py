#!/usr/bin/python3
'''is_kind_of_class module definition'''


def inherits_from(obj, a_class):
    '''a function that returns true if obj a subclass of a_class'''
    if type(obj) == a_class:
        return False
    return isinstance(obj, a_class)
