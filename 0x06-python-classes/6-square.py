#!/usr/bin/python3

"""Creation of Square class."""

class Square:
    """
    A class to represent a square.

    Attributes:
        size(int): Defines the size of the square.
        position(tuple): Defines the coordinates of position (0,0) of the square.
    """

    def __init__(self, size=0, position=(0,0)):
        """
        Constructs the necessary attributes for the Square object.

        Args:
            size(int): Represents the size of the Square object.
            position(tuple(int, int)): Represents the position of (0,0) of the Square object in the Cartesian plane.
        """
        
        self.position = position
        self.size = size

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

    @property
    def position(self):
        """
        Gets the property position for value assignment.

        Args:
            None.

        Returns:
            None.
        """
        return self.__position


    @position.setter
    def position(self, value):
        """
        This public instance method assigns a value to the private insatnce attribute 'position'.

        Args:
            Value(int, int): The tuple to be assigned to 'position'.

        Returns:
            None.
        """
        if (not isinstance(num, int) for num in value) or (len(value) != 2) or (not all(num >= 0 for num in value)) or (not isninstance(value, tuple)):
            raise TypeError('position must be a tuple of 2 positive integers')

        self.__position = value

    def my_print(self):
        """
        Prints out a square using hashmarks '#' at a position (x, y).

        Args:
            None.

        Returns:
            None.
        """

        for y in range(self.__position[1]):
            print("")

        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                for x in range(self.__position[0]):
                    print(' ', end='')
                for j in range(self.__size):
                    print('#', end='')

                print('')

