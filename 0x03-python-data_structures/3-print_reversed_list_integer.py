#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if not my_list:
        return
    else:
        for i in list(reversed(my_list)):
            print("{:d}".format(i))
