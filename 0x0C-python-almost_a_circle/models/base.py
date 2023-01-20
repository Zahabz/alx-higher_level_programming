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

    @classmethod
    def load_from_file(cls):
        """
        Returns a list of instances

        Args:
        -----
            None

        Returns:
        --------
            List of instances
        """
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Write the CSV serialization of a list of objects to a file.

        Args:
            list_objs (list): A list of inherited Base instances.
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Return a list of classes instantiated from a CSV file.

        Reads from `<cls.__name__>.csv`.

        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw Rectangles and Squares using the turtle module.

        Args:
            list_rectangles (list): A list of Rectangle objects to draw.
            list_squares (list): A list of Square objects to draw.
        """
        turt = turtle.Turtle()
        turt.screen.bgcolor("#b7312c")
        turt.pensize(3)
        turt.shape("turtle")

        turt.color("#ffffff")
        for rect in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()
            for i in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
            turt.hideturtle()

        turt.color("#b5e3d8")
        for sq in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(sq.x, sq.y)
            turt.down()
            for i in range(2):
                turt.forward(sq.width)
                turt.left(90)
                turt.forward(sq.height)
                turt.left(90)
            turt.hideturtle()

