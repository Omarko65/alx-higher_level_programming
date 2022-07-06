#!/usr/bin/python3
'''to_json_string module definition'''

import json
'''importing json to module'''


def to_json_string(my_obj):
    '''to_json_string - this function uses json to convert object to str
    Args:
        my_obj: this is the object to be converted
    Returns: it returns the new string
    '''
    return json.dumps(my_obj)
