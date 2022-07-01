#!/usr/bin/python3
'''Module definition add_integer
   which takes 2 aguments
'''


def add_integer(a, b=98):
    '''module definition'''
    
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return (a + b)
