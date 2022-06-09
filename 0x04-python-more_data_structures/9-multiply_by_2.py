#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_d = a_dictionary.copy()

    for i in new_d:
        new_d[i] *= 2
    
    return new_d
