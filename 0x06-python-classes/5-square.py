#!/usr/bin/python3

"""Creation of Square class."""

class Square:
    """
    A class to represent a square.

    Attributes:
        size(int): Defines the size of the square.
    """

    def __init__(self, size=0):
        """
        Constructs the necessary attributes for the Square object.

        Args:
            size(int): Represents the size of the Square object.
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    def area(self):
        """
        Returns the area of the Square instance created when called.

        Args:
            None.

        Returns:
            Area of the Square object.
        """
        return (self.__size * self.__size)

    @property
    def size(self):
        """
        Retrieves the size attribute of the square.

        Args:
            None.

        Returns:
            The size attribute of the Square instance.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Assigns a value to the size attribute after retrieval.

        Args:
            value(int): The value assigned to the size attribute.

        Returns:
            None.
        """
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')

        self.__size = value

    def my_print(self):
        """
        Prints out a square using hashmarks '#'.

        Args:
            None.

        Returns:
            None.
        """
        if size == 0:
            print("")
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print('#', end='')

                print('')

