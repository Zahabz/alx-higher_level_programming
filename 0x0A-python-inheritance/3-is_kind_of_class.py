#!/usr/bin/python3

"""Module containing key function"""

def is_kind_of_class(obj, a_class):
    """
    Checks if the object is an instance of, or if an object is an instance of a class that inherited from, the specified class

    Parameters:
    -----------
        - obj(any): Object to be tested
        - a_class(object): class object to be used for check

    Returns:
    --------
        Returns `True` or `False`
    """
    if isinstance(obj, a_class):
        return True
    return False
