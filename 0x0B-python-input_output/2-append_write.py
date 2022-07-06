#!/usr/bin/python3
'''append_write module definition'''


def append_write(filename="", text=""):
    '''Append_write - a function that appends string to a file
    Args:
        filename(str): The name of the file string is to append
        text(str): The string that is to be appended
    Returns: Nothing
    '''
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
