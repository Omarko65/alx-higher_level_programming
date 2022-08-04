#!/usr/bin/python3
'''rectangle module definition'''

from models.base import Base
'''importing Base module'''


class Rectangle(Base):
    '''rectangle class definition'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''rectangle class initialization'''

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        '''getter for width attribute'''
        return self.__width

    @width.setter
    def width(self, value):
        '''setter for width attribute'''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise TypeError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        '''getter for height attribute'''
        return self.__height

    @height.setter
    def height(self, value):
        '''setter for width attribute'''
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise TypeError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        '''getter for x attribute'''
        return self.__x

    @x.setter
    def x(self, value):
        '''setter for x attribute'''
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise TypeError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        '''getter for y attribute'''
        return self.__y

    @y.setter
    def y(self, value):
        '''setter for y attribute'''
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise TypeError("y must be >= 0")
        self.__y = value
