#!/usr/bin/python3

"""Contains Square class that inherits from Rectangle class"""

from models.rectangle import Rectangle

class Square(Rectangle):
    """
    A class to represent a Square object
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Constructs all the necessary attributes fro the Square object

        Attributes:
        -----------
            size : int
                The width ad length of Square object

            x : int
                Position in the x-axis

            y : int
                Position in y-axis

            id : int
                Specific identifier for each and every Square instance

        """
        super().__init__(size, size, x, y, id)


    @property
    def size(self):
        """
        Gets the private instance attribute self.__width

        Args:
        -----
            None

        Returns:
        --------
            self.__width

        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Assigns a value for the Square size (width and height)

        Args:
        -----
            None

        Returns:
        --------
            None
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        THis public instance method assigns an argument to the instance attributes

        Args:
        -----
         *args(int): Arguments to be assigned

        Returns:
        --------
            None
        """
        if args:
            for idx, arg in enumerate(args):
                if idx == 0:
                    self.id = arg
                elif idx == 1:
                    self.width = arg
                elif idx == 2:
                    self.height = arg
                elif idx == 3:
                    self.x = arg
        else:
            for k, v in kwargs.items():
                if k == 'id':
                    self.id = v
                elif k == 'width':
                    self.width = v
                elif k == 'height':
                    self.height = v
                elif k == 'x':
                    self.x = v
                elif k == 'y':
                    self.y = v


    def __str__(self):
        """
        Unofficial string representation of the Square object
        """
        return f'[{self.__class__.__name__}] ({self.id}) {self.x}/{self.y} - {self.width}'

    def to_dictionary(self):
        """
        Returns a dictionary represntation of the Square object

        Args:
        -----
            None

        Returns:
        --------
            Dictionary of Square attributes
        """
        return {
            'id': getattr(self, 'id'),
            'size': getattr(self, 'size'),
            'x': getattr(self, 'x'),
            'y': getattr(self, 'y')
            }


