#!/usr/bin/python3

"""Creation of empty class"""

class BaseGeometry:
    """Empty class"""

    def area(self):
        """
        Raises an exception

        Parameters:
        -----------
            None

        Returns:
        --------
            Raises a `NotImplementedError` exception
        """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """
        Checks whether the value parameter meets the required criteria

        Parameters:
        -----------
            name(str): String parameter
            value(int): Value to be tested

        Returns:
        --------
            `TypeError` or `ValueError`
        """

        if type(value) != int:
            raise TypeError(f'{name} must be an integer')
        elif value <= 0:
            raise ValueError(f'{name} must be greater than 0')

