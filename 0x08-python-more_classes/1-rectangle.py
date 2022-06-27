#!/usr/bin/python3
'''define class rectangle module'''


class Rectangle:
    '''class rectangle initialized'''
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    '''private attribute getter for width'''
    @property
    def width(self):
        return self.__width

    '''private attribute setter for width'''
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    '''private attribute getter for width'''
    @property
    def height(self):
        return self.__height

    '''private attribute setter for width'''
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
