# 0x0A. Python-Inheritance

## Learning objectives :dart:

* What is a superclass, baseclass or parentclass
* What is a subclass
* How to list all attributes and methods of a class or instance
* When can an instance have new attributes
* How to inherit class from another
* How to define a class with multiple base classes
* What is the default class every class inherit from
* How to override a method or attribute inherited from the base class
* Which attributes or methods are available by heritage to subclasses
* What is the purpose of inheritance
* What are, when and how to use isinstance, issubclass, type and super built-in functions

## Tasks to be completed :page_with_curl:

* **0. Lookup**
  * [0-lookup.py](./0-lookup.py)Involves using the prototype function `def lookup(obj):` to return a list of available attributes and method of an object.
  * It also returns the result in a list.

* **1. My list**
  * [1-my_list.py](./1-my_list.py) contains a class `MyList` that inherits from list:
        * Public instance method: `def print_sorted(self):`: prints the list and sorts it in ascending order.

* **2. Exact same object**
  * [2-is_same_class.py](./2-is_same_class.py) contains a function that returns `True` if `obj` is exactly an instance of the specified class.
	* Prototype function: `def is_same_class(obj, a_class):`

* **3. Same class or inherit from**
  * [3-is_kind_of_class.py](./3-is_kind_of_class.py) contains a function that returns `True` if `obj` is an instance of, or if the object is an instance of a class that inherited from the specified class; otherwise `False`.
        * Prototype function: `def is_kind_of_class(obj, a_class):`

*  **4. Only sub class of**
   * [4-inherits_from.py](./4-inherits_from.py) contains a function that returns `True` if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise `False`.
	* Prototype function: `def inherits_from(obj, a_class):`

* **5. Geometry module**
  * [5-base_geometry.py](./5-base_geometry.py) creates an empty class `BaseGeometry`

* **6. Improve Geometry**
  * [6-base_geometry.py](./6-base_geometry.py) containing:
        * Public Instance method `def area(self):` that raises an `Exception` with the message `area() is not implemented`

* **7. Integer validator**
  * [7-base_geometry.py](./7-base_geometry) containing class `BaseGeometry` containing
        * Public Instance method `def area(self):` that raises an `Exception` with the message `area() is not implemented`
        * Public instance method: `def integer_validator(self, name, value):` that validates `value`:
	      * you can assume name is always a string
    	      * if `value` is not an integer: raise a `TypeError` exception, with the message `<name> must be an integer`
              * if `value` is less or equal to 0: raise a `ValueError` exception with the message `<name> must be greater than 0`

* **8. Rectangle**
  * [8-rectangle.py](./8-rectangle.py) contains class Rectangle that:
	* Instantiation with `width` and `height`: `def __init__(self, width, height):`
   	      * `width` and `height` must be private. No getter or setter
              * `width` and `height` must be positive integers, validated by integer_validator

