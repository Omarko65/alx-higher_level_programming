#!/usr/bin/python3
def uniq_add(my_list=[]):
    c = 0
    for i in sorted(set(my_list)):
        print(i)
        c = c + i
    return c
