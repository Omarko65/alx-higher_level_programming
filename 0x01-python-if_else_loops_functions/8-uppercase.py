#!/usr/bin/python3
def uppercase(str):
    for i in str:
        value = ord(i)
        alpha = 0
        if value > 96 and value < 124:
            alpha = value - 32
        else:
            alpha = value
        print(chr(alpha),end="")
