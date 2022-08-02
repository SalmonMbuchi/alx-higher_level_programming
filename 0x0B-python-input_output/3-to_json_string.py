#!/usr/bin/python3
""" a function that returns JSON representation of a string"""
import json


def to_json_string(my_obj):
    """output JSON object as a string"""
    new_str = json.dumps(my_obj)
    return new_str
