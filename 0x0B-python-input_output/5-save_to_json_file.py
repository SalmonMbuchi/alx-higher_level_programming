#!/usr/bin/python3
"""writes an object to a text file"""
import json


def save_to_json_file(my_obj, filename):
    """write an object to a file using JSON format"""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
