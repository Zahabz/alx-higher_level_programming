#!/usr/bin/python3

"""Creation of a Rectangle class"""

class Rectangle:
    """
    A class that represents a Rectangle

    Class attributes:
    -----------------
        number_of_instances(int): Stores the number of class instances as an integer.
        print_symbol(str): Symbol used to produce the string repesentation of the Rectangle Object 

    Instance Attributes
    -------------------
        width(int): Defines the width of the rectangle.
        height(int): Defines the height of the rectangle.
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        Constructs the necessary attributes for the instantiation of the Rectangle object.

        Args
        ----
            width(int): Represents the width of the Rectangle.
            height(int): Represents the height of the Rectangle object.

        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        """
        Returns the area of the Rectangle object

        Args:
        -----
            None

        Returns:
        --------
            Area of Rectangle object
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Returns the perimeter of the Rectangle object if both height and width are greater than 0 else zero 

        Args:
        -----
            None

        Returns:
        --------
            Perimeter of Rectangle object/instance
        """
        if self.__width == 0 or self.__height == 0:
            return 0

        return (self.__width + self.__height) * 2

    def __str__(self):
        """
        Returns an informal string representation of the REctangle object

        Args:
        -----
            None

        Returns:
        --------
            Rectangle object  made up of hash marks
        """
        if self.__width == 0 or self.__height == 0:
            return ''
        else:
            return '\n'.join(Rectangle.print_symbol * self.__width for y in range(self.__height))

    def __repr__(self):
        """
        Returns an official representation of the Rectangle object

        Args:
        -----
          - None

        Returns:
        --------
          - String rep of Rectangle object
        """

        return f"Rectangle({str(self.__width)}, {str(self.__height)})"

    def __del__(self):
        """
        Returns a string when the Rectangle is deleted

        Args:
        -----
          - None

        Returns:
        --------
          - A string object to signify deletion
        """
        Rectangle.number_of_instances -= 1
        print('Bye rectangle...')
