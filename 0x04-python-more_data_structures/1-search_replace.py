#!/usr/bin/python3
def search_replace(my_list, search, replace):
    c = []
    for i in my_list:
        if i == search:
            i = replace
        c.append(i)
    return c
