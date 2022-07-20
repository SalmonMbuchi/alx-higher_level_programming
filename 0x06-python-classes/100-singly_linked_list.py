#!/usr/bin/python3
"""Write a class Node that defines a node of a singly linked list by:

    Private instance attribute: data:
        property def data(self): to retrieve it
        property setter def data(self, value): to set it:
            data must be an integer, otherwise raise a TypeError
    Private instance attribute: next_node:
        property def next_node(self): to retrieve it
        property setter def next_node(self, value): to set it:
            next_node can be None or must be a Node, else raise a TypeError
Instantiation with data and next_node:
    def __init__(self, data, next_node=None):

And, write a class SinglyLinkedList that defines a singly linked list by:

    Private instance attribute: head (no setter or getter)
    Simple instantiation: def __init__(self):
    Should be printable:
        print the entire list in stdout
        one node number by line
Public instance method: def sorted_insert(self, value):
inserts a new Node into the correct sorted position in the list
"""


class Node:
    """defines a node of a singly linked list"""
    def __init__(self, data, next_node=None):
        assert isinstance(data, int), f"data must be an integer"
        assert next_node=None or next_node=Node, f"next_node must be a Node object"

        self.__data = data
        self.__next_node = next_node
    
    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        assert isinstance(data, int), f"data must be an integer"
        self.__value = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        assert next_node=None or next_node=Node, f"next_node must be a Node object"
        self.__next_node = value


class SinglyLinkedList:
    """defines a singly linked list"""
    def __init__(self):

    def sorted_insert(self, value):
        self.__head = value



