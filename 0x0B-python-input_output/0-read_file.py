#!/usr/bin/python3
""" read a text file and print to stdout """


def read_file(filename=""):
    """ open, read and print file contents to stdout """
    with open(filename, encoding='utf-8') as file:
        print(file.read(), end="")
