#!/usr/bin/python3
def max_integer(my_list=[]):
    highest_num = 0
    for i in my_list:
        if i > highest_num:
            highest_num = i
    return highest_num
