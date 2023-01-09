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
