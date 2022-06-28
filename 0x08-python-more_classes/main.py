#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle

try:
    mysquare = Rectangle.square(-2) 
    print("{} / {}".format(mysquare.width, mysquare.height)) 
except Exception as e: 
    print("didnt work")
