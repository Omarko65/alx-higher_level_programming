#!/usr/bin/python3
'''my_list module definition'''


class MyList(list):
    '''class Mylist inherits lists and adds an extra method'''

    def print_sorted(self):
        '''print_sorted prints the sorted version of list'''
        new = sorted(self)
        print(new)
