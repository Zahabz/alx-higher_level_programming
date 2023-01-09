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

bg = BaseGeometry()

try:
    print(bg.area())
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
