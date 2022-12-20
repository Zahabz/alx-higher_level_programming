#!/usr/bin/python3

"""Creation of a Square class."""

class Square:
    """
    A class to represent a square.

    Attributes:
        size (int): Defines the square size.
    """
    def __init__(self, size):
        """
        Constructs the necessary attributes for the Square object.

        Args:
            size (int): Represents the square size of the Square object.
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        elif (size < 0):
            raise ValueError('size must be >= 0')

        self.__size = size

    def area(self):
        """
        Returns the area of the Square instance created when called.

        Args:
            None.

        Returns:
            returns the area of the Square object when called.
        """
        return (self.__size * self.__size)

