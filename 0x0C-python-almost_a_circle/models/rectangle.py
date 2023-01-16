#!/usr/bin/python3

"""Module that contains the Rectangle class that inherit from Base class"""
from models.base import Base


class Rectangle(Base):
    """Creation of Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Constructs the necessary instance attributes to obtain the Rectangle object

        Args:
        -----
            width(int): Width of Rectangle instance
            height(int): Height of Rectangle object
            id(int): Public instance attribute inherited from the Base class
            x(int): Position of Rectangle in x-axis
            y(int): Position of object in y-axis

        """

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """
          Gets the private instance attribute `width`

          Args:
          -----
              None

          Returns:
          --------
              `self.__width`
          """
        return self.__width

    @width.setter
    def width(self, value):
        """
         Assigns a value to width after it is obtained

         Args:
         -----
             value(int): Integer to be assigned to the width attribute

         Returns:
         --------
             Raises exceptions if `value` does not meet the requisite threshold

         """
        if type(value) != int:
            raise TypeError('width must be an integer')
        elif value <= 0:
            raise ValueError('width must be > 0')

        self.__width = value

    @property
    def height(self):
        """
         Gets the private instance attribute `height`

         Args:
         -----
             None

         Returns:
         --------
             `self.__height`
         """
        return self.__height

    @height.setter
    def height(self, value):
        """
         Assigns a value to height after it is obtained

         Args:
         -----
             value(int): Integer to be assigned to the height attribute

         Returns:
         --------
             Raises exceptions if `value` does not meet the requisite threshold

         """
        if type(value) != int:
            raise TypeError('height must be an integer')
        elif value <= 0:
            raise ValueError('height must be > 0')

        self.__height = value

    @property
    def x(self):
        """
         Gets the private instance attribute `x`

         Args:
         -----
             None

         Returns:
         --------
             `self.__x`
         """
        return self.__x

    @x.setter
    def x(self, value):
        """
         Assigns a value to x after it is obtained

         Args:
         -----
             value(int): Integer to be assigned to the x attribute

         Returns:
         --------
             Raises exceptions if `value` does not meet the requisite threshold

         """
        if type(value) != int:
            raise TypeError('x must be an integer')
        elif value < 0:
            raise ValueError('x must be >= 0')

        self.__x = value

    @property
    def y(self):
        """
          Gets the private instance attribute `y`

          Args:
          -----
              None

          Returns:
          --------
              `self.__y`
          """
        return self.__y

    @y.setter
    def y(self, value):
        """
         Assigns a value to y after it is obtained

         Args:
         -----
             value(int): Integer to be assigned to the y attribute

         Returns:
         --------
             Raises exceptions if `value` does not meet the requisite threshold

         """
        if type(value) != int:
            raise TypeError('y must be an integer')
        elif value < 0:
            raise ValueError('y must be >= 0')

        self.__y = value

    def area(self):
        """
        Returns the area of the Rectangle object

        Args:
        -----
            None

        Returns:
        --------
            area
        """
        area = self.__width * self.__height

        return area

    def display(self):
        """
        Prints a string representation of the Rectangle object

        Args:
        -----
            None

        Returns:
        --------
            Prints string of Rectangle object
        """

        for y in range(self.__y):
            print("")
        for _  in range(self.height):
            for x in range(self.__x):
                print(" ", end="") 
            for _ in range(self.__width):
                print('#', end="")
            print("")

    def __str__(self):
        """
        Returns an unofficial string representation of the Rectangle object in the format `[Rectangle] (<id>) <x>/<y> - <width>/<height>`

        Args:
        -----
            None

        Returns:
        --------
            [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        return f'[{self.__class__.__name__}] ({self.id}) {self.__x}/{self.__y} - {self.__width}/{self.__height}'

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
                elif idx == 4:
                    self.y = arg
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
            'width': getattr(self, 'width'),
            'height': getattr(self, 'height'),
            'x': getattr(self, 'x'),
            'y': getattr(self, 'y')
            }



