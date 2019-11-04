#Exercises

## Exercise 1
Correct the following code for the `greet` method to return the expected value.

`class Person:
      def __init__(self, name):
        self.name = name

      def greet(self, other_name):
        return "Hi {0}, my name is {1}".format(other_name, name)`

Please place your code in `ch05_ex1.py`

## Exercise 2
Write and use a class of your choice. Your class must have a constructor, attributes, and methods.

Please place your code in `ch05_ex2.py`

## Exercise 3
Write the `Stack` class implementing a [stack] (https://en.wikipedia.org/wiki/Pile_ (computer)). You must implement the following methods:

* `push`: add an item to the stack
* `pop`: removes the last item added to the stack
* `top`: returns the last item added to the stack (without changing the stack)

Moreover:

* we must be able to obtain the size of the stack with the function `len`
* your class must be convertible into a Boolean expression. `False` when the stack is empty,` True` otherwise.

It is recommended to use a list to preserve the elements.

Example of use:


    >>> s = Stack()
    >>> bool(s), len(s)
    (False, 0)
    >>> s.push(4)
    >>> bool(s), len(s), s.top()
    (True, 1, 4)
    >>> s.push(8)
    >>> bool(s), len(s), s.top()
    (True, 2, 8)
    >>> s.pop()
    8
    >>> bool(s), len(s), s.top()
    (True, 1, 4)


Please place your code in `ch05_ex3.py`
