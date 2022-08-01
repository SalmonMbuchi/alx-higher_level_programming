#!/usr/bin/python3
"""determine if the object is an instance of an inherited class"""


def inherits_from(obj, a_class):
    """return True if object is an instance else return fALSE"""
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
