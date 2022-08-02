#!/usr/bin/python3
"""create an object from a JSON file"""
import json


def load_from_json_file(filename):
    """create an object from a JSON file"""
    with open(filename, 'r', encoding='utf-8') as file:
        new_obj = json.load(file)
