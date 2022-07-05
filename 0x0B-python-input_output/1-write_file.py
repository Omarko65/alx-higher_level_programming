#!/usr/bin/python3
'''module definition write_file'''


def write_file(filename="", text=""):
    '''write_file function writes string to file
    Args:
        Filename(str): The name of file to write string to
        Text(str): Text to be written in file
    Returns:
        The length of string passed to file
    '''
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
