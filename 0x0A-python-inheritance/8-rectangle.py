#!/usr/bin/python3

"""Contains a Rectangle class that inherits from a BaseGeometry class"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """Creation of a Rectangle class"""
    
    def __init__(self, width, height):
        """
        Constructs the necessary attributes to obtain a Rectangle object

        Parameters:
        -----------
            width(int): The width of Rectangle object
            height(int): The height of Rectangle object

        Returns:
        --------
            None
        """
        self.integer_validator('width', width)
        self.__width = width
        self.integer_validator('height', height)
        self.__height = height

