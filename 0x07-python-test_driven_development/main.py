#!/usr/bin/python3
""" Doc """

say_my_name = __import__('3-say_my_name').say_my_name

try:
    say_my_name("Bob", 12)
except Exception as e:
    print(e)
