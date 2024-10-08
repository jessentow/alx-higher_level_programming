#!/usr/bin/python3
"""Defining the same class or inherit from"""


def is_kind_of_class(obj, a_class):
    """This returns True if the object
    is an instance of, or if the object is an instance
    of a class that inherited from, the specified class;
    otherwise False
    Args:
        obj(any): object of the class
        a_class(type): describes the class
    """
    if isinstance(obj, a_class):
        return True
    return False
