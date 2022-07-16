#!/usr/bin/python3
'''module for square class'''


Rectangle = __import__('9-rectangle').Rectangle
'''rectangle class import'''


class Square(Rectangle):
    '''class initialization'''
    def __init__(self, size):
        self.__size = size
        self.integer_validator("size", self.__size)
        super().__init__(size, size)

    '''area implementation'''
    def area(self):
        return self.__size ** 2
