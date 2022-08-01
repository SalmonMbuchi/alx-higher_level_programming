#!/usr/bin/python3
"""a function that determines if an object is an instance"""


def is_kind_of_class(obj, a_class):
    """return True if the object is an instance, else return False"""
    return isinstance(obj, a_class)
