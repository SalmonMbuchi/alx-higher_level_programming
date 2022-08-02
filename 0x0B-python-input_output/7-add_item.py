#!/usr/bin/python3
"""add all arguments to a list and save in a JSON file"""
import json
import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

# total arguments
n = len(sys.argv)

# append all arguments to a list
aList = []
for i in range(1, n):
    """start from 1 since sys.argv[0] is the script's name"""
    aList.append(sys.argv[i])

# write object(list) to a JSON file
filename = "add_item.json"
save_to_json_file(aList, filename)

# create an object from a JSON file
filename = "add_item.json"
obj = load_from_json_file(filename)
