#!/usr/bin/python3

"""Creation of a Square class"""

class Square:
    """
    A class to represent a square

    Attributes:
       - size (int): Represents the square size

    Methods:
       - area(self): Returns the area of the square 
    """
    def __init__(self, size):
        """
        Constructs the necessary attributes, in this case size, for the square object

        Args:
           - size (int): An integer that represents the size of the square
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
            None

        Returns:
            - returns the area of the Square object when called
        """
        return (self.__size) ** 2

