#!/usr/bin/python3
"""Defining only sub class of.
"""


def inherits_from(obj, a_class):
    """This will return True if the object is
    an instance of a class that inherited (directly or indirectly)
    from the specified class;
    otherwise False.
    Args:
        obj(any): object of the class
        a_class(type): describes the class
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
