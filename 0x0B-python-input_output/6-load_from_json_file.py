#!/usr/bin/python3
"""create an object from a JSON file"""
import json


def load_from_json_file(filename):
    """create object from a JSON file"""
    with open(filename, 'r', encoding='utf-8') as f:
        new_obj = json.load(f)
        return new_obj
