#!/usr/bin/python3
'''defining from_json_string module'''

import json
'''importing the json function to our module'''

def from_json_string(my_str):
    '''from_json_string - converts a str to  an obj using json
    Args:
        my_str: the string to be converted back to obj
    Returns: it returns the new obj
    '''
    return json.loads(my_str)
