"""
Write the Stack class implementing a [stack] (https://en.wikipedia.org/wiki/Pile_ (computer)). You must implement the
following methods:

push: add an item to the stack
pop: removes the last item added to the stack
top: returns the last item added to the stack (without changing the stack)
Moreover:

we must be able to obtain the size of the stack with the function len
your class must be convertible into a Boolean expression. False when the stack is empty,True otherwise.
It is recommended to use a list to preserve the elements.

Example of use:
"""


class Stack:

    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        self.stack.pop()

    def top(self):
        return self.stack[-1]

    def __bool__(self):
        return bool(self.stack)

    def __len__(self):
        return len(self.stack)




