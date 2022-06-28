#!/usr/bin/python3
'''class rectangle module definition'''


class Rectangle:
    '''class rectangle initalization'''
    number_of_instances = 0
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

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

    '''public instance method to find perimeter of a rectangle'''
    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (2 * (self.__width + self.__height))

    '''str initialization that returns rectangle with #'''
    def __str__(self):
        myprint = ""
        count = 1
        if self.__height == 0 and self.__width == 0:
            return myprint
 
        else:
            for i in range(self.__height):
                for j in range(self.__width):
                    myprint += '#'
                if count < self.__height:
                    myprint += "\n"
                    count += 1
        return myprint

    '''repr initialization that returns rectangle with #'''
    def __repr__(self):
        return "Rectangle(" + str(self.__width) + ', ' + str(self.__height) + ')'

    '''del method definition'''
    def __del__(self):
        print("Bye rectangle...")
        type(self).number_of_instances -= 1
