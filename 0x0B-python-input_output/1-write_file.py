#!/usr/bin/python3
""" writes a string to a text file and return no. of characters """


def write_file(filename="", text=""):
    """write a string to a file and return no. of characters"""
    with open(filename, mode='w', encoding='utf-8') as f:
        return f.write(text)
