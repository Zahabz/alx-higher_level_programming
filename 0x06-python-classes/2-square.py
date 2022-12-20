#!/usr/bin/python3

"""Creation of Square class."""
class Square:
    """
    A class to represent a square
    
    Attributes:
        size (int): Defines the square size
    """
    def __init__(self, size=0):
        """
        Constructs all the necessary attributes for the Square object
        
        Args:
            size (int): Represents the square size of the Square object
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

