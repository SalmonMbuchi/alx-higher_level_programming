#!/usr/bin/python3
"""this module contains the super class"""
import json


class Base:
    """contains a private class attribute and class constructor"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns JSON string representation"""
        if list_dictionaries is None:
            return "[]"
        if list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """write JSON string representation to a file"""
        filename = cls.__name__ + ".json"
        with open(filename, 'w', encoding='utf-8') as f:
            if list_objs is None:
                f.write('[]')
            else:
                f.write(Base.to_json_string(list_objs))

    @staticmethod
    def from_fson_string(json_string):
        """returns the list of JSON string representation"""
        if json_string is None and json_string == []:
            return '[]'
        else:
            return json.loads(json_string)
