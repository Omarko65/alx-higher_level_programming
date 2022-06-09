#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    c = a_dictionary.copy()
    for i in c:
        c[i] *= 2 
    return c
