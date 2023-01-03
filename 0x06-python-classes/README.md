# Python - Classes and Objects

## Learning Objectives :dart:

The following were the objectives of this project:

* What is a class
* What is an object and an instance
* What is the difference between a class and an object or instance
* What is an attribute
* What are and how to use public, protected and private attributes
* What is `self`
* What is a method
* What is the special `__init__` method and how to use it
* What is Data Abstraction, Data Encapsulation, and Information Hiding
* What is a property
* What is the difference between an attribute and a property in Python
* What is the Pythonic way to write getters and setters in Python
* How to dynamically create arbitrary new attributes for existing instances of a class
* How to bind attributes to object and classes
* What is the `__dict__` of a class and/or instance of a class and what does it contain
* How does Python find the attributes of an object or class
* How to use the `getattr` function


## Tasks to be completed :page_with_curl:

* **0. My first square**
  * [0-square.py](0-square.py): Defines an empty class `Square`

* **1. Square with size**
  * [1-square.py](1-square.py): Involves creating a class `Square` that defines a square (based on [0-square.py](0-square.py)) with a private instance attribute
`size`

* **2. Size validation**
  * [2-square.py](2-square.py): Defines a square by private instance attribute,
instantiation with optional `size`: `def __init__(self, size=0):`.

* **3. Area of a square**
  * [3-square.py](3-square.py) defines a square by:
      * Private instance attribute `size`
      * Instantiation with optional `size`: `def __init__(self, size=0):`
      * Public instance method: `def area(self):`

* **4. Access and update private attribute**
  * [4-square.py](4-square.py) defines a square by:
      * Private instance attribute `size`:
           * property `def size(self):`: Retrieval of size
           * property setter `def size(self,value):`: Setting size value
      * Instantiation of optional `size`: `def __init__(self, size=0):`
      * Public instance method `def area(self):`: Returns the area of Square object

* **5. Printing a square**
  * [5-square.py](5-square.py) defines a square by:
      * Private instance attribute `size`:
           * property `def size(self):`: Retrieval of size
           * property setter `def size(self,value):`: Setting size value
      * Instantiation of optional `size`: `def __init__(self, size=0):`
      * Public instance method `def area(self):`: Returns the area of Square object 
      * Public instance method: `def my_print(self):` that prints in stdout the square with the character`#`:
           * if `size` is equal to 0, print an empty line
	
* **6. Coordinates of a square**
  * [6-square.py](6-square.py) defines a square by:
      * Private instance attribute `size`:
           * property `def size(self):`: Size retrieval
           * property setter `def size(self, value):`: Setting size value
      * Instantiation of optional `size`: `def __init__(self, size=0):`
      * Public instance method: `def area(self):`: Returns the area of the Square object
      * Public instance method: `def my_print(self):` that prints in stdout the square with the character `#`:
           * if `size` is equal to 0, print an empty line

* **7. Printing Square instance**
  * [101-square.py](101-square.py) defines a square by:
      * Private instance attribute `size`:
           * property `def size(self):`: Size retrieval
           * property setter `def size(self, value):`: Setting size value
      * Instantiation of optional `size`: `def __init__(self, size=0):`
      * Public instance method: `def area(self):`: Returns the area of the Square object
      * Public instance method: `def my_print(self):` that prints in stdout the square with the character `#`:
           * if `size` is equal to 0, print an empty line
      * Printing a string representation of the Square object using `def __str__(self):`

* **8. Compare 2 squares**
  * [102-square.py](102-square.py) defines a square by:
      **Private instance attribute `size`:
           * property `def size(self):`: Size retrieval
           * property setter `def size(self, value):`: Setting size value
      * Instantiation of optional `size`: `def __init__(self, size=0):`
      * Public instance method: `def area(self):`: Returns the area of the Square object
      * Public instance method: `def my_print(self):` that prints in stdout the square with the character `#`:
           * if `size` is equal to 0, print an empty line
      * `Square` instance can answer to comparison operators such as `==`, `>=` or `<` among others based on area.

