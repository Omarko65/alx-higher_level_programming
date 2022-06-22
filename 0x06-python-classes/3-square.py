#!/usr/bin/python3
'''
Class square with an argument
Args:
    size (int): size of the square
    area (int): area of a square
'''


class Square:
    '''
    class square definition
    Args:
        size (int): size of the square
        area (int): area of the square
    '''
    def __init__(self, size):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
    '''
    class square area function definition
    Args:
        self (object): this is the class object
    
    Return: the area of the circle
    '''
    def area(self):
        return self.__size ** 2
