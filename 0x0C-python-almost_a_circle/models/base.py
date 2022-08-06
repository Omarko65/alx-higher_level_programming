#!/usr/bin/python3
'''module definition for base class'''


class Base:
    '''class initialization of base'''
    __nb_objects = 0

    def __init__(self, id=None):
        '''initalization of class'''

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        '''method that returns json repr of dict'''
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)
