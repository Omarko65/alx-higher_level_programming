#!/usr/bin/python3
def common_elements(set_1, set_2):
    c = []
    for i in set_1 & set_2:
        c.append(i)
    return c
