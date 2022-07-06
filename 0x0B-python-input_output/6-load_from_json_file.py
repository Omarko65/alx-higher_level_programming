#!/usr/bin/python3
'''defining load_from_json_file module'''

import json
'''importing json'''


def load_from_json_file(filename):
    '''
    load_from_json_file: this is a function that creates an  obj from jsonfile
    Args:
        filename: this is the file to be used to create obj
    Return: Returns the new object file
    '''
    with open(filename) as f:
        data = json.load(f)
        return data
