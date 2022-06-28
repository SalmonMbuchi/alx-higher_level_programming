#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) >= 97 and ord(i) <= 122:
            upp = ord(i) - 32
            print("{}".format(upp))
        else:
            print("{}".format(i))
