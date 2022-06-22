#!/usr/bin/python3
"""
class square that defines a square
"""
class Square:
    '''    
    class square that defines a square
    Args:
        size (int): size of square in int default 0 if none
    '''
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be integer")
        elif size < 0:
            raise TypeError("size must be >= 0")
        else:
            self.__size = size
