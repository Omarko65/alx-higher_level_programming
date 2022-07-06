#!/usr/bin/python3
'''class_to_json module definition'''


def class_to_json(obj):
    '''
    class_to_json: A function that returns dictionary description
    Args:
        obj: A class dictionary that the descriptionis to be returned
    Returns: returns description of a dictionary
    '''
    return obj.__dict__
