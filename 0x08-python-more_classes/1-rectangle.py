#!/usr/bin/python3

"""Creation of a Rectangle class"""

class Rectangle:
    """
    A class that represents a Rectangle

    Attributes
    ----------
        width(int): Defines the width of the rectangle.
        height(int): Defines the height of the rectangle.
    """

    def __init__(self, width=0, height=0):
        """
        Constructs the necessary attributes for the instantiation of the Rectangle object.

        Args
        ----
            width(int): Represents the width of the Rectangle.
            height(int): Represents the height of the Rectangle object.

        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """
        Uses the property decorator to access/get the private instance attribute `width`.

        Args
        ----
            None.

        Returns
        -------
            Private Instance attribute `width`.
            
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Assigns the `width` private instance attribute a particular value and checks if it`s an integer.

        Args:
        ----
            value(int): Value to be assigned to width attribute.

        Returns:
        -------
            None.
        """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')

        self.__width = value

    @property
    def height(self):
        """
        Accesses and gets the `height` private instance attribute.

        Args:
        -----
            None.

        Returns:
        --------
            Private Instance attribute `height`.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Assigns the `height` private instance attribute a value `value`.

        Args:
        -----
            value(int): Value to be assigned to height attribute.

        Returns:
        --------
            None.
        """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')

        self.__height = value

