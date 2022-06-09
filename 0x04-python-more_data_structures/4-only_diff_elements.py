#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    c = []
    for i in set_1 ^ set_2:
        c.append(i)
    return c
