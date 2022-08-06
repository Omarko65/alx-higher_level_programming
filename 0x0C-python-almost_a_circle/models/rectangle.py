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
            raise ValueError("width must be > 0")
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
            raise ValueError("height must be > 0")
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
            raise ValueError("x must be >= 0")
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
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        '''method that finds area of a rectangle'''
        return (self.__width * self.__height)

    def display(self):
        '''method that displays the rectangle'''
        i = self.__height
        j = self.__width
        [print("") for d in range(self.__y)]
        for s in range(i):
            print(" " * self.__x, end="")
            for k in range(j):
                print("#", end="")
            print()

    def __str__(self):
        '''str method that pinrs class description'''
        return "[{:s}] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
                type(self).__name__, self.id, self.__x, self.__y,
                self.__width, self.__height)

    def update(self, *args, **kwargs):
        '''update module that initalize the class without init'''
        count = 0
        for arg in args:
            if count == 0:
                if arg is None:
                    self.__init__(self.width, self.height, self.x, self.y)
                else:
                    self.id = arg
            elif count == 1:
                self.width = arg
            elif count == 2:
                self.height = arg
            elif count == 3:
                self.x = arg
            elif count == 4:
                self.y = arg
            count += 1

        for key, value in kwargs.items():
            temp = ["id", "width", "height", "x", "y"]
            if key in temp and temp.index(key) >= count:
                if key == temp[0]:
                    if value is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    self.id = value
                elif key == temp[1]:
                    self.width = value
                elif key == temp[2]:
                    self.height = value
                elif key == temp[3]:
                    self.x = value
                elif key == temp[4]:
                    self.y = value

    def to_dictionary(self):
        '''method that returns dictionary of class'''
        return {
                "id" : self.id,
                "width" : self.width,
                "height" : self.height,
                "x" : self.x,
                "y" : self.y
        }
