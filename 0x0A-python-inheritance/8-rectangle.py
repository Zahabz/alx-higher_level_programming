#!/usr/bin/python3

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
        self.__width = width
        self.integer_validator('width', self.__width)
        self.__height = height
        self.integer_validator('height', self.__height)

