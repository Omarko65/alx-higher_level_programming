#!/usr/bin/python3
def to_uppa(chr):
    if ord(chr) >= 97 and ord(chr) <= 122:
        return (ord(chr)-32)
    else:
        return ord(chr)


def uppercase(str):
    new_str = ""
    for chr in str:
        new_str += "%c" % to_uppa(chr)
    print("{:s}".format(new_str))
