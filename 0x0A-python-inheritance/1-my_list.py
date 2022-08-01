#!/usr/bin/python3
"""this module contains a class that inherits from list and a method"""


class MyList(list):
    """inherits from list"""

    def print_sorted(self):
        """print the list in ascending order"""
        a_list = []
        for num in self:
            a_list.append(num)
        print(sorted(a_list))
