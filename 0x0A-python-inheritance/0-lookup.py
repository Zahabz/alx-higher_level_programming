#!/usr/bin/python3

""" Module containing `def lookup(obj):` function."""
def lookup(obj):
    """
    Collects all attributes and methods in a class object into a list

    Parameters:
    -----------
        - obj: A class object

    Returns:
    --------
        Returns a list object of the attributes and methods available for the object 
    """
    obj_list = list(dir(obj))

    return obj_list
