#!/usr/bin/python3
'''square class module'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''sqaure class definition'''

    def __init__(self, size, x=0, y=0, id=None):
        '''square class initialization'''
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        '''Getter method for size'''
        return self.width

    @size.setter
    def size(self, value):
        '''Setter method for size'''
        self.width = value
        self.height = value

    def __str__(self):
        '''str initialization of class'''
        return "[{}] ({}) {}/{} - {}".format(
                type(self).__name__, self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        '''adding args and kwargs function to class'''
        attrs = ('id', 'size', 'x', 'y')
        for key, val in zip(attrs, args):
            setattr(self, key, val)
        if (type(args) is None or len(args) == 0) and (type(kwargs) is dict):
            for key, val in kwargs.items():
                if key in attrs:
                    setattr(self, key, val)

    def to_dictionary(self):
        '''method that returns dict of class'''
        return {
                "id": self.id,
                "size": self.size,
                "x": self.x,
                "y": self.y
        }
