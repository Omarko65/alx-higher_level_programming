#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    ret_list = [i for i in my_list if isinstance(i, int)]
    count = 0
    num = 0
    for j in list(my_list):
        num += 1

    for i in ret_list:
        count += 1
    try:
        if x<=num:
            if x<= count:
                print(''.join(str(i) for i in ret_list[:x]))
            else:
                print(''.join(str(i) for i in ret_list[:count]))
        else:
            raise IndexError('list index out of range')
    except IndexError:
        raise
    else:
        if x <= count:
            return x
        else:
            return count
