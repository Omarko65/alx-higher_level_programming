#!/usr/bin/python3
def safe_print_integer(value):
    num = 1
    try:
        num = (1 - num) + value
    except (ValueError, TypeError):
        return (False)
    else:
        print("{:d}".format(num))
        return True
