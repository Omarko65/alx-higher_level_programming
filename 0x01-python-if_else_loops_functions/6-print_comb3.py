#!/usr/bin/python3
i = 0
while i < 89:
    if i % 10 == 0:
        i += 1 + i//10
    if i < 89:
        print("{:0>2d}, " .format(i),end="")
    elif i == 89:
        print(89)
    i += 1
