#!/usr/bin/python3

"""Module containing the Base class to be used in the entirety of the project"""

import json

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
    
    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns a json represntation of the attribute dictionaries

        Args:
        -----
            list_dictionaries : list
                - Attribute dictionary converted to list

        Returns:
        --------
            Json string
        """
        if (list_dictionaries is None) or len(list_dictionaries) == 0:
            return '[]'
        else:
            new_json = json.dumps(list_dictionaries)
            return new_json
    
    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes a list of instances that inherit from the class `Base`

        Args:
        -----
        list_objs : lists
            List of instances inheriting from Base class

        Returns:
        --------
            None
        """
        filename = str(cls.__name__) + '.json'


        if (list_objs is None) or (len(list_objs) == 0):
            with open(filename, 'w') as f:
                f.write('[]')
        else:
            list_dictionaries = [obj.to_dictionary() for obj in list_objs]
            list_json = cls.to_json_string(list_dictionaries)
            with open(filename, 'w') as f:
                f.write(list_json)
    
    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list of the JSON string representation `json_string`

        Args:
        -----
            json_string : str
                string representation of list of dictionaries

        Returns:
        --------
            list representation of json
        """
        if json_string is None or len(json_string) == 0:
            return []
        else:
            new_list = json.loads(json_string)
            return new_list

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance with all attributes set

        Args:
        -----
            dictionary : dict
                Key word arguments

        Returns:
        --------
            Instance with all attributes set
        """
        if dictionary or len(dictionary) != {}:

            if cls.__name__ == 'Square':
                obj = cls(2)
            else:
                obj = cls(3,2)

            obj.update(**dictionary)
            return obj



            
