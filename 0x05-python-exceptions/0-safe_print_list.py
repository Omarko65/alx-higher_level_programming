#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    mass = 0
    c = ""
    ret_list = list(my_list)
    for j in my_list:
        mass+=1
    try:
        if x <= mass:
            print(''.join(str(i) for i in ret_list[:x]))
        elif x > mass:
            print(''.join(str(i) for i in ret_list[:mass]))
    except TypeError:
        print("Invalid type")
    else:
        if x <= mass:
            return (x)
        else:
            return (mass)
