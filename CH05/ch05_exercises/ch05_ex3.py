class Stack:
    def __init__(self):
        self._stack = []
        pass

    def push(self, item):
        self._stack.insert(0, item)

    def pop(self):
        return self._stack.pop(0)

    def top(self):
        return self._stack[0]

    def __len__(self):
        return len(self._stack)

    def __bool__(self):
        return True if self.__len__() > 0 else False


s = Stack()
print(bool(s), len(s))
s.push(4)
print(bool(s), len(s), s.top())
s.push(8)
print(bool(s), len(s), s.top())
print(s.pop())
print(bool(s), len(s), s.top())
