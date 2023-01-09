#!/usr/bin/python3

"""Module containing function that checks if an object is an instance of particular class"""

def is_same_class(obj, a_class):
    """
    Checks if an object is a class instance

    Parameters:
    -----------
        - obj: Object
        - a_class: class instance

    Returns:
    --------
        Returns `True` or `False` 
    """
    if type(obj) == a_class:
        return True
    else:
        return False
