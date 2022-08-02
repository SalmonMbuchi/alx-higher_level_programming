#!/usr/bin/python3
"""a class that defines a student"""


class Student:
    """contains public instance attributes and public method"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return self.__dict__
