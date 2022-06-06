#!/usr/bin/python3
def element_at(my_list, idx):
    lent = len(my_list)
    if idx < 0:
        return (None)
    elif idx > lent:
        return (None)
    else:
        return (my_list[idx])
