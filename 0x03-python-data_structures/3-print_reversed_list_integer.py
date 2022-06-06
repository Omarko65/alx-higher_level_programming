#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    lent = len(my_list) - 1
    if not my_list:
        pass
    else:
        while 0 <= lent:
            print("{:d}".format(my_list[lent]))
            lent = lent - 1
