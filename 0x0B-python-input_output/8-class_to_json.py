#!/usr/bin/python3
"""return dictionary description"""
import json


def class_to_json(obj):
    """returns dictionary description with data structure"""
    return obj.__dict__
