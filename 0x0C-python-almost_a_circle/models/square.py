#!/usr/bin/python3
from models.rectangle import Rectangle
'''importing the rectangle module'''


class Square(Rectangle):
    '''sqaure class definition'''

    def __init__(self, size, x=0, y=0, id=None):
        '''square class initialization'''
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        '''Getter method for size'''
        return self.__size

    @size.setter
    def size(self, value):
        '''Setter method for size'''
        self.width = value
        self.height = value

    def __str__(self):
        '''str initialization of class'''
        return "[{}] ({}) {}/{} - {}".format(type(self).__name__, self.id, self.x, self.y, self.height)
