class Stack:
    def __init__(self):
        self.stack = []

    def __bool__(self):
        if self.__len__():
            return True
        return False

    def __len__(self):
        return len(self.stack)

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.__len__():
            self.stack.pop()
        return None

    def top(self):
        if self.__len__():
            return self.stack[-1]
        return None
