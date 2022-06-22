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
        if isinstance(size, int):
            if size >= 0:
                self.__size = size
            else:
                raise TypeError("size must be >= 0")
        else:
            raise TypeError("sise must be an integer")
