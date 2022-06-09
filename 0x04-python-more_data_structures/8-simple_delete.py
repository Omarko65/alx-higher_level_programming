#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if key in a_dictionary:
        del a_dictionary[key]
        c = a_dictionary.copy()
        return c
    else:
        return a_dictionary
