#!/usr/bin/python3
def uniq_add(my_list=[]):
    c = 0
    for i in sorted(set(my_list)):
        c = c + i
    return c
