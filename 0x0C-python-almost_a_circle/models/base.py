#!/usr/bin/python3
'''module definition for base class'''
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        '''method that returns json repr of dict'''
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''method that save repr of list with json'''
        filename = cls.__name__ + ".json"
        with open(filename, "w") as f:
            if list_objs is None:
                f.write("[]")
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                f.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        '''static method that returns list of json repr'''
        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        '''method that returns a list of instances'''
       polygons = {
            'Rectangle': (1, 1, 0, 0),
            'Square': (1, 0, 0, None)
        }
        if cls.__name__ in polygons.keys():
            polygon = cls(*polygons[cls.__name__])
            polygon.update(**dictionary)
            return polygon

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, encoding="utf-8") as f:
                list_instances = cls.from_json_string(f.read())
                return [cls.create(**d) for d in list_instances]
        except IOError:
            return []        
