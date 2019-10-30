class Stack:
  def __init__(self, name):
    self.stack = []
    self.name = name

  def push(self, val):
    self.stack.append(val)
    return self

  def pop(self):
    self.stack = self.stack[0:-1]
    return self

  def top(self):
    return self.stack[-1]