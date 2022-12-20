#!/usr/bin/python3

"""Creation of a Square class."""

class Square:
    """
    A class to represent a square.
    
    Attributes:
        size(int): Represents the square size.
    """
    def __init__(self, size=0):
        """
        Constructs the attributes necessary for the Square object

        Args:
            size(int): Represents the size of the square object
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    def area(self):
        """
        Returns the area of the Square instance when called.

        Args:
            None.

        Returns:
            returns the area of the Square object created.
        """
        return (self.__size * self.__size)
    
    @property
    def size(self):
        """
        Returns the value of the size property of the Square object.

        Returns:
            returns the private instance attribute 'size'.
        """

        return self.__size

    @size.setter
    def size(self, value):
        """
        After retrieval of the value of the size property, this function assigns it a value.

        Returns:
            None.
        """
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')

        self.__size = value

