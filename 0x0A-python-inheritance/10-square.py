#!/usr/bin/python3

"""This inherits from subclass - square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class representation of a square"""

    def __init__(self, size):
        """Initializes a square
        Args:
            size (int): The size of the new square.
        """
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)
        self._size = size
