#!/usr/bin/python3
def max_integer(my_list=[]):
    highest_num = my_list[0]
    if len(my_list) < 1:
        return None
    else:
        for i in my_list:
            if i > highest_num:
                highest_num = i
        return highest_num
