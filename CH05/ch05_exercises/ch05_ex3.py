class Stack:
    def __bool__(self):
        if self.__len__():
            return True
        return False

    def __len__(self):
        return len(self.stack)

    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        self.stack.pop()

    def top(self):
        return self.stack[-1]
