#!/usr/bin/python3
"""determine if an object is an instance of the specified class"""


def is_same_class(obj, a_class):
    """return True if the object is an exact instance, else return False"""
    return isinstance(obj, a_class)
