#!/usr/bin/python3
'''class rectangle module definition'''


class Rectangle:
    '''class rectangle initalization'''
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    '''private instance attribute width property setter'''
    @property
    def width(self):
        return self.__width

    '''private instance attribute width property getter'''
    @width.setter
    def width(self, value):
        self.__width = value

    '''private instance attribute height property setter'''
    @property
    def height(self):
        return self.__height

    '''private instance attribute height property getter'''
    @height.setter
    def height(self, value):
        self.__height = value

    '''public instance method to find area of rectangle'''
    def area(self):
        return (self.__width * self.__height)

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (2 * (self.__width + self.__height))
