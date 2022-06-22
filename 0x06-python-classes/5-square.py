#!/usr/bin/python3
'''
Module 5-square
class square module which has different classes
'''


class Square:
    '''class square is initialized here'''
    

    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
        else:
            raise TypeError("size must be an integer")

    def area(self):
        return self.__size * self.__size
    
    def my_print(self):
        if self.__size == 0:
            print()
        
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end = "")
                print()
