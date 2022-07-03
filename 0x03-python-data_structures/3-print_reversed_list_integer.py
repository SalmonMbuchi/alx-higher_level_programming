#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    idx = (len(my_list) - 1) *-1
    for i in range(-1, idx):
        print("{}".format(my_list[idx]))
        #idx -= 1
