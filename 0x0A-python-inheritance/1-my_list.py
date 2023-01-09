#!/usr/bin/python3

"""Creation of MyList class"""

class MyList(list):
    """A class that inherits from the list object"""

    def print_sorted(self):
        """
        Prints out a sorted list

        Parameters:
        -----------
            None

        Returns:
        --------
            Prints out a sorted list
        """
        print(sorted(self))
