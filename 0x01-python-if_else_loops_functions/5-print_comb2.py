#!/usr/bin/python3
for i in range(0, 100):
    if i == 99:
        print("{}".format(i))
    if i >= 0 and i <= 9:
        print(f"0{i}")
    else:
        print("{}, ".format(i))
