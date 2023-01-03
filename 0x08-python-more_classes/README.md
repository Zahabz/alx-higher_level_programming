# 0.08. More Classes and Objects

## Learning Objectives :dart:

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
* What are the special `__str__` and `__repr__` methods and how to use them
* What is the difference between `__str__` and `__repr__`
* What is a class attribute
* What is the difference between a object attribute and a class attribute
* What is a class method
* What is a static method

## Tasks to be undertaken :page_with_curl;

* **0. Simple Rectangle**
  * [0-rectangle.py](./0-rectangle.py): defines an empty `Rectangle` class

* **1. Rectangle definition**
  * [1-rectangle.py](./1-rectangle.py) defines a rectangle by:
      * Private instance attribute `width`:
           * property `def width(self):`: Width retrieval
           * property setter `def width(self, value):`: Setting width value
      * Private instance attribute `height`:
           * property `def height(self):`: Height retrieval
           * property setter `def height(self, value):`: Setting height value
      * Instantiation with optional `width` and `height`: `def __init__(self, width=0, height=0)`

* **2. Area and Perimeter**
  * [2-rectangle.py](./2-rectangle.py) defines a rectangle by:
      * Private instance attribute `width`:
           * property `def width(self):`: Width retrieval
           * property setter `def width(self, value):`: Setting width value
      * Private instance attribute `height`:
           * property `def height(self):`: Height retrieval
           * property setter `def height(self, value):`: Setting height value
      * Instantiation with optional `width` and `height`: `def __init__(self, width=0, height=0)`
      * Public instance method: `def area(self):`: Returns the area of the rectangle
      * Public instance method: `def perimeter(self):`: Returns the rectangle`s perimeter 

* **3. String representation**
  * [3-rectangle.py](./3-rectangle.py) defines a rectangle by:
      * Private instance attribute `width`:
           * property `def width(self):`: Width retrieval
           * property setter `def width(self, value):`: Setting width value
      * Private instance attribute `height`:
           * property `def height(self):`: Height retrieval
           * property setter `def height(self, value):`: Setting height value
      * Instantiation with optional `width` and `height`: `def __init__(self, width=0, height=0)`
      * Public instance method: `def area(self):`: Returns the area of the rectangle
      * Public instance method: `def perimeter(self):`: Returns the rectangle`s perimeter
      * Use of the magic method `def __str__(self):` to print an informal string representation of the Rectangle object.

* **4. Eval is magic**
  * [4-rectangle.py](./4-rectangle.py) defines a rectangle by:
     * Private instance attribute `width`:
           * property `def width(self):`: Width retrieval
           * property setter `def width(self, value):`: Setting width value
      * Private instance attribute `height`:
           * property `def height(self):`: Height retrieval
           * property setter `def height(self, value):`: Setting height value
      * Instantiation with optional `width` and `height`: `def __init__(self, width=0, height=0)`
      * Public instance method: `def area(self):`: Returns the area of the rectangle
      * Public instance method: `def perimeter(self):`: Returns the rectangle`s perimeter
      * Use of the magic method `def __str__(self):` to print an informal string representation of the Rectangle object.
      * Use of `__repr__` to return an official string representation of the `Rectangle` object and using the `eval()` to create a new class instance

* **5. Instance deletion**
  * [5-rectangle.py](./5-rectangle.py) defines a rectangle by:
      * Private instance attribute `width`:
           * property `def width(self):`: Width retrieval
           * property setter `def width(self, value):`: Setting width value
      * Private instance attribute `height`:
           * property `def height(self):`: Height retrieval
           * property setter `def height(self, value):`: Setting height value
      * Instantiation with optional `width` and `height`: `def __init__(self, width=0, height=0)`
      * Public instance method: `def area(self):`: Returns the area of the rectangle
      * Public instance method: `def perimeter(self):`: Returns the rectangle`s perimeter
      * Use of the magic method `def __str__(self):` to print an informal string representation of the Rectangle object.
      * Use of `__repr__` to return an official string representation of the `Rectangle` object and using the `eval()` to create a new class instance
      * Prints the message `Bye rectangle...` when an instance is deleted.

* **6. How many instances**
  * [6-rectangle.py](./6-rectangle.py) defines a rectangle by:
      * Private instance attribute `width`:
           * property `def width(self):`: Width retrieval
           * property setter `def width(self, value):`: Setting width value
      * Private instance attribute `height`:
           * property `def height(self):`: Height retrieval
           * property setter `def height(self, value):`: Setting height value
      * Public class attribute `number_of_instances` that is initialized to 0 and increases or decreases upon ceation or deletion of an instance.
      * Instantiation with optional `width` and `height`: `def __init__(self, width=0, height=0)`
      * Public instance method: `def area(self):`: Returns the area of the rectangle
      * Public instance method: `def perimeter(self):`: Returns the rectangle`s perimeter
      * Use of the magic method `def __str__(self):` to print an informal string representation of the Rectangle object.
      * Use of `__repr__` to return an official string representation of the `Rectangle` object and using the `eval()` to create a new class instance
      * Prints the message `Bye rectangle...` when an instance is deleted.

* **7. Change representation**
  * [7-rectangle.py](./7-rectangle.py) defines a rectangle by:
      * Private instance attribute `width`:
           * property `def width(self):`: Width retrieval
           * property setter `def width(self, value):`: Setting width value
      * Private instance attribute `height`:
           * property `def height(self):`: Height retrieval
           * property setter `def height(self, value):`: Setting height value
      * Public class attribute `number_of_instances` that is initialized to 0 and increases or decreases upon ceation or deletion of an instance.
      * Public class attribute `print_symbol` intialized to `#` and is used as the symbol for string representation.
      * Instantiation with optional `width` and `height`: `def __init__(self, width=0, height=0)`
      * Public instance method: `def area(self):`: Returns the area of the rectangle
      * Public instance method: `def perimeter(self):`: Returns the rectangle`s perimeter
      * Use of the magic method `def __str__(self):` to print an informal string representation of the Rectangle object.
      * Use of `__repr__` to return an official string representation of the `Rectangle` object and using the `eval()` to create a new class instance
      * Prints the message `Bye rectangle...` when an instance is deleted.
     
