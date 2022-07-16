#!/usr/bin/python3
'''module definition for class BaseGeometry'''


class BaseGeometry:
    '''BaseGeomeetry definition'''
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''int validator that checks if value is int'''
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
