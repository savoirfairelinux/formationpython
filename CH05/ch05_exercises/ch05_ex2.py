
class Stack:
    def __init__(self):
        self.contents = []

    def push(self, value):
        self.contents.append(value)
        
    def pop(self):
        if len(self.contents) == 0:
            return None
        return self.contents.pop()

    def top(self, value):
        length = len(self.contents)
        if length == 0:
            return None
        return self.contents[length - 1]

    def __bool__(self):
        if len(self.contents) == 0:
            return False
        return True

    def __len__(self):
        return len(self.contents)


