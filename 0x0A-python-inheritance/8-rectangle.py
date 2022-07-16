#!/usr/bin/python3
'''module definition of rectangle class definition'''


BaseGeometry = __import__('7-base_geometry').BaseGeometry
'''importing parent directory to be used'''


class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        '''rectangle class initialization'''
        self.__width = width
        self.__height = height
        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)
