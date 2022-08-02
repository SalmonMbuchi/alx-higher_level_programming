#!/usr/bin/python3
"""return object represented be a JSON string"""
import json


def from_json_string(my_str):
    """return object from a JSON string"""
    new_obj = json.loads(my_str)
    return new_obj
