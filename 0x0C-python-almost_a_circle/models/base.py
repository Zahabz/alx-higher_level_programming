#!/usr/bin/python3

"""Module containing the Base class to be used in the entirety of the project"""

class Base:
    """
    Creation of Base class containing a private class attribute that acts as an `instance counter`

    Private instance attribute:
    ---------------------------
        __nb_objects

    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Constructs the necessary attributes required to obtain the Base object

        Args:
        -----
            id (int): Public instance attribute assigned to the Base object if not None otherwise increment nb_objects by 1 and assign to id. 
        """
        if id is not None:
            self.id = id

        else:
           Base.__nb_objects += 1
           self.id = Base.__nb_objects

